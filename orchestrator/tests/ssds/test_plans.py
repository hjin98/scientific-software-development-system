"""Phase E step 2: change plans, item declarations and work contracts in the content model (catalogue §11.1, §13.1).

Expected values are written from the catalogue's grammar and the Stage S case named, never computed by the
parser under test.
"""

from __future__ import annotations

import unittest

from ssds.content import REVIEW, Check, EvidenceVerifier, Item, ItemFailure, Ref, parse_item, plans
from ssds.derivation import Policy

from ._fixtures import tree, view

MANIFEST = """
[[unit]]
id = "plan.solver"
kind = "PLAN"
role = "composite"
scope = [{ file = "plans/solver.md" }]

[[unit]]
id = "plan.solver.objective"
part_of = "plan.solver"
subject = false
scope = [{ file = "plans/solver.md", heading = ["Objective"] }]

[[unit]]
id = "plan.solver.timestep"
part_of = "plan.solver"
subject = false
scope = [{ file = "plans/solver.md", heading = ["Item timestep"] }]

[[unit]]
id = "plan.solver.output"
part_of = "plan.solver"
subject = false
scope = [{ file = "plans/solver.md", heading = ["Item output"] }]
"""

TIMESTEP_BLOCK = """\
item = "timestep"
kind = "IMPLEMENT"
objective = { ref = "#item-timestep" }
governing = ["numerics.solver@sha256:%s"]
acceptance_criteria = [ { id = "ac1", evidence = "tests.solver-convergence" } ]
affected = ["src/solver/"]
gates = ["d2-owner-review"]
depends_on = ["output"]
[contract]
scientific = "APPLIES"
budget = 3
[contract.boundaries]
write_scope = ["src/solver/", "tests/solver/"]
frozen = ["pkg.solver.step"]
dependencies = { python = ["numpy>=1.26"] }
[[contract.obligations]]
id = "o1"
statement = { ref = "#o1" }
verifier = { check = "OBLIGATION.required_evidence", params = { spec = "tests.solver-convergence" } }
secondary = [ { check = "TEST_INTEGRITY.no_skips" } ]
[[contract.obligations]]
id = "o2"
statement = { ref = "#goal" }
verifier = "REVIEW"
[[contract.obligations]]
id = "o3"
statement = { ref = "#o1" }
verifier = { evidence = "tests.solver-convergence", runner = "ci" }
[contract.expectations]
artifacts = ["src/solver/timestep.py"]
evidence = ["tests.solver-convergence"]
slots = ["findings", "choices", "retention", "claims"]
[contract.escalation]
triggers = ["SCOPE_DEVIATION", "D1_D2_TOUCH"]
""" % ("a" * 64)

OUTPUT_BLOCK = """\
item = "output"
kind = "DOCUMENT"
objective = { ref = "#item-output" }
"""


def document(timestep_block: str = TIMESTEP_BLOCK, timestep_prose: str = "The step adapts to the CFL bound.\n",
             output_prose: str = "Write the results.\n", objective: str = "Stable solver.\n") -> str:
    return (
        "# Solver plan\n\n"
        "## Objective\n\n"
        f"<!-- ssds:begin goal -->\n{objective}<!-- ssds:end goal -->\n\n"
        "## Item timestep\n\n"
        f"{timestep_prose}\n"
        "### o1\n\nThe convergence test passes at second order.\n\n"
        f"```ssds-item\n{timestep_block}```\n\n"
        "## Item output\n\n"
        f"{output_prose}\n"
        "### o1\n\nAn output obligation of the other item.\n\n"
        f"```ssds-item\n{OUTPUT_BLOCK}```\n"
    )


def plan_of(text: str):
    v = view(tree({"plans/solver.md": text}, MANIFEST))
    return v, plans(v)["plan.solver"]


class PlanParts(unittest.TestCase):
    def test_objective_and_items(self) -> None:
        _, plan = plan_of(document())
        self.assertEqual(plan.objective, "plan.solver.objective")
        self.assertEqual(sorted(plan.items), ["plan.solver.output", "plan.solver.timestep"])
        item = plan.items["plan.solver.timestep"].parsed
        assert isinstance(item, Item), item
        self.assertEqual((item.id, item.kind, item.objective), ("timestep", "IMPLEMENT", Ref("item-timestep")))
        self.assertEqual(item.governing, (("numerics.solver", "sha256:" + "a" * 64),))
        self.assertEqual(item.acceptance_criteria, (("ac1", "tests.solver-convergence"),))
        self.assertEqual((item.affected, item.gates, item.depends_on), (("src/solver/",), ("d2-owner-review",), ("output",)))
        contract = item.contract
        assert contract is not None
        self.assertEqual((contract.scientific, contract.budget), ("APPLIES", 3))
        self.assertEqual(contract.write_scope, ("src/solver/", "tests/solver/"))
        self.assertEqual(contract.dependencies, (("python", ("numpy>=1.26",)),))
        o1, o2, o3 = contract.obligations
        self.assertEqual(o1.verifier, Check("OBLIGATION.required_evidence", (("spec", "tests.solver-convergence"),)))
        self.assertEqual(o1.secondary, (Check("TEST_INTEGRITY.no_skips"),))
        self.assertEqual(o2.verifier, REVIEW)
        self.assertEqual(o3.verifier, EvidenceVerifier("tests.solver-convergence", "ci"))
        self.assertEqual(contract.slots, ("findings", "choices", "retention", "claims"))
        self.assertEqual(contract.triggers, ("SCOPE_DEVIATION", "D1_D2_TOUCH"))
        output = plan.items["plan.solver.output"].parsed
        assert isinstance(output, Item)
        self.assertIsNone(output.contract)  # an accepted item without a contract owes CONTRACT (§10.2)

    def test_a_part_without_a_block_is_not_an_item(self) -> None:
        text = document().replace(f"```ssds-item\n{OUTPUT_BLOCK}```\n", "")
        _, plan = plan_of(text)
        self.assertEqual(sorted(plan.items), ["plan.solver.timestep"])

    def test_two_blocks_in_one_part_fail(self) -> None:
        text = document(timestep_prose=f"```ssds-item\n{OUTPUT_BLOCK}```\n")
        _, plan = plan_of(text)
        self.assertEqual(plan.items["plan.solver.timestep"].parsed.reason, "BLOCKS")

    def test_item_revision_is_its_part(self) -> None:
        """Item-level revisions give locality (§11.2): an edit of one item leaves the other's revision."""

        v0, _ = plan_of(document())
        v1, _ = plan_of(document(output_prose="Write the results and a summary.\n"))
        self.assertEqual(v0.rev("plan.solver.timestep"), v1.rev("plan.solver.timestep"))
        self.assertNotEqual(v0.rev("plan.solver.output"), v1.rev("plan.solver.output"))


class ClosedSchema(unittest.TestCase):
    """Unknown keys, missing fields and values outside the grammar fail (§13.1, C5)."""

    def assertFails(self, body: str, reason: str = "GRAMMAR") -> None:
        parsed = parse_item(body.encode("utf-8"))
        self.assertIsInstance(parsed, ItemFailure, body)
        self.assertEqual(parsed.reason, reason, parsed)

    def test_refusals(self) -> None:
        base = 'item = "x"\nkind = "IMPLEMENT"\nobjective = { ref = "#x" }\n'
        self.assertIsInstance(parse_item(base.encode()), Item)
        contract = ('[contract]\nscientific = "NOT_APPLIES"\nbudget = 2\n[contract.boundaries]\nwrite_scope = ["src/"]\n'
                    '[[contract.obligations]]\nid = "o1"\nstatement = { ref = "#o1" }\nverifier = "REVIEW"\n')
        self.assertIsInstance(parse_item((base + contract).encode()), Item)
        cases = {
            "unknown item key": base + 'owner = "me"\n',
            "missing objective": 'item = "x"\nkind = "IMPLEMENT"\n',
            "unknown kind": base.replace("IMPLEMENT", "REFACTOR"),
            "AUTHOR without authority": base.replace("IMPLEMENT", "AUTHOR"),
            "authority on IMPLEMENT": base + 'authority = "D2"\n',
            "specialist on IMPLEMENT": base + 'specialist = "MAINTENANCE_AUDIT"\n',
            "ref not '#name'": base.replace('"#x"', '"x"'),
            "governing without revision": base + 'governing = ["numerics.solver"]\n',
            "unknown contract key": base + contract + 'owner = "me"\n'.replace("owner", "[contract.extra]\nk"),
            "unknown boundary key": base + contract.replace('write_scope = ["src/"]', 'write_scope = ["src/"]\nscope = []'),
            "no obligation": base + '[contract]\nscientific = "APPLIES"\nbudget = 1\nobligations = []\n'
                                    '[contract.boundaries]\nwrite_scope = []\n',
            "zero budget": base + contract.replace("budget = 2", "budget = 0"),
            "scientific outside": base + contract.replace("NOT_APPLIES", "MAYBE"),
            "unknown slot": base + contract + '[contract.expectations]\nslots = ["opinions"]\n',
            "duplicate obligation id": base + contract + '[[contract.obligations]]\nid = "o1"\nstatement = { ref = "#o1" }\n'
                                                         'verifier = "REVIEW"\n',
            "verifier not a template": base + contract.replace('"REVIEW"', '{ check = "required_evidence" }'),
        }
        for name, body in cases.items():
            with self.subTest(case=name):
                self.assertFails(body)
        self.assertFails('item = "x"\nkind = \n', "PARSE")


class RefLocality(unittest.TestCase):
    """A ref resolves only in the item's own part and the Objective (§13.2; S5 §13 ``ref_outside_item_part_rejected``)."""

    def test_where_a_ref_resolves(self) -> None:
        _, plan = plan_of(document())
        own = "plan.solver.timestep"
        # S5 §13 ref_outside_item_part_rejected: (item1 in item1, Objective in item1, item2 in item1) = (True, True, False)
        self.assertEqual(len(plan.resolve_ref(own, Ref("item-timestep"))), 1)
        self.assertEqual(len(plan.resolve_ref(own, Ref("goal"))), 1)
        self.assertEqual(len(plan.resolve_ref(own, Ref("item-output"))), 0)
        # The other item's heading of the same name is never consulted: exactly one ``#o1`` for each item.
        self.assertEqual(len(plan.resolve_ref(own, Ref("o1"))), 1)
        self.assertEqual(len(plan.resolve_ref("plan.solver.output", Ref("o1"))), 1)

    def test_an_ambiguous_ref_is_not_one_span(self) -> None:
        _, plan = plan_of(document(timestep_prose="### o1\n\nA second span of the same name.\n"))
        self.assertEqual(len(plan.resolve_ref("plan.solver.timestep", Ref("o1"))), 2)

    def test_a_repeated_anchor_is_not_one_span(self) -> None:
        objective = "Stable.\n<!-- ssds:begin goal -->\nagain\n<!-- ssds:end goal -->\n"
        _, plan = plan_of(document(objective=objective))
        self.assertNotEqual(len(plan.resolve_ref("plan.solver.timestep", Ref("goal"))), 1)


class ItemProse(unittest.TestCase):
    """The prose an amendment must keep byte-identical to be control tightening (§13.4)."""

    def test_prose_excludes_the_block_only(self) -> None:
        text = document()
        narrower = document(TIMESTEP_BLOCK.replace('"src/solver/", "tests/solver/"', '"src/solver/"'))
        reworded = document(timestep_prose="The step adapts to the CFL bound, strictly.\n")
        prose = []
        for t in (text, narrower, reworded):
            v, plan = plan_of(t)
            part = plan.items["plan.solver.timestep"]
            prose.append(part.prose(v.tree[part.path].data))
        self.assertEqual(prose[0], prose[1])
        self.assertNotEqual(prose[0], prose[2])
        self.assertNotIn(b"ssds-item", prose[0])


class WorkflowPolicy(unittest.TestCase):
    """The ``[workflow]`` keys of Phase E reading E10: system defaults, and nothing weaker than a floor."""

    def test_defaults_and_values(self) -> None:
        empty = Policy.parse(b"schema = 1\n")
        self.assertEqual((empty.flow("budget"), empty.flow("standing_plan"), empty.flow("floors")), (3, None, ()))
        policy = Policy.parse(
            b'schema = 1\n[workflow]\nstanding_plan = "plan.standing"\nbudget = 2\nprovisional_kinds = ["REVIEW"]\n'
            b'waive_item_level_review = ["DOCUMENT"]\nconcern_tags = { security = ["src.auth"] }\n'
            b'[[workflow.floors]]\nkind = "FINDING"\nreason = "ANOMALY"\nmateriality = "MATERIAL"\n'
        )
        self.assertEqual(policy.flow("standing_plan"), "plan.standing")
        self.assertEqual(policy.flow("budget"), 2)
        self.assertEqual(policy.flow("provisional_kinds"), ("REVIEW",))
        self.assertEqual(policy.flow("concern_tags"), {"security": ("src.auth",)})
        self.assertEqual(policy.flow("floors"), ({"kind": "FINDING", "materiality": "MATERIAL", "reason": "ANOMALY"},))

    def test_refusals(self) -> None:
        cases = {
            "unknown key": b"[workflow]\nrecurrence = 5\n",
            "budget above the system cap": b"[workflow]\nbudget = 11\n",
            "zero budget": b"[workflow]\nbudget = 0\n",
            "provisional gate": b'[workflow]\nprovisional_kinds = ["GATE"]\n',
            "provisional human attention": b'[workflow]\nprovisional_kinds = ["HUMAN_ATTENTION"]\n',
            "unknown concern": b'[workflow]\nconcern_tags = { style = ["x"] }\n',
            "unknown item kind": b'[workflow]\nwaive_item_level_review = ["REFACTOR"]\n',
            "floor without materiality": b'[[workflow.floors]]\nkind = "FINDING"\n',
            "floor outside the vocabulary": b'[[workflow.floors]]\nkind = "FINDING"\nmateriality = "URGENT"\n',
        }
        for name, text in cases.items():
            with self.subTest(case=name), self.assertRaises(ValueError):
                Policy.parse(b"schema = 1\n" + text)


if __name__ == "__main__":
    unittest.main()

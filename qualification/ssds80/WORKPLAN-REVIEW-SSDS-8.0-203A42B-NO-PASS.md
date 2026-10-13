# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 15

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 203a42bddf559234cb7b39283f014ada7a86d8d6
    SCOPE: whole proposed architecture; (a) the revision-15 repairs: content-anchored
           evidentiary premises (present, bears, about in S0; passing-side currency on unit
           revisions); never-lost salvage on every rejection after authentication and
           retired-key verification (§6.8 steps 3 and 6); independence of human
           dispositions; the D1/D2 floor keyed on any obligation qual reads; bearing after a
           rebase; the extended bounded model check (REPART, P8, REV14 sensitivity);
           (b) workflow execution and verification layer and the doctrine-realization
           objective; (c) persistence, derivation, concurrency and migration; (d) Protocol
           7.2.1 inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: c5b344b26e83465a31494955768ec74642939ad6 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72, 62C0B24;
           all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; each revision-15 repair attacked as a new
           mechanism: every S0 fact that `present`, `bears` and `about` read was varied by
           structural-only, retirement, rejection and salvage routes, and every newly
           admitted record class was checked for permissive fields; prior-finding
           re-derivation; exact-candidate structural tests, whitespace check and bounded
           model check in all requested modes
    REVIEWER: Claude (same model family as the author), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-15.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-203A42B-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.24-§27.25), the model check's green result and every prior verdict as hypotheses.

The two blockers below are deductions from the proposed contracts, not observed SSDS runtime failures. Their asserter is the reviewer named above; their disposition is **OPEN** against the exact candidate. This record is their canonical home. Revisit after the D3 owner repairs `about` (§6.6) and the step-6 salvage (§6.8), regenerates §0.1, §22, §27 and the model check from those rules, and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable here. It requires keeping separate “the **evidentiary target** (proposition/invariant evaluated) and **execution dependency**”, says “A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority”, and in Assessment disagreement says: “preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence. […] When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” A D3 design in which only a change of the evaluated content, or an authorized standing disposition, ends adversity satisfies all of these together. Both blockers lie in the candidate's concretization, which is D3.

The stakeholder record (blob `edbf40da…`, unchanged since `644eb72`) supports what the workplan attributes to it. SD-5 and SD-6 accept the revision-5 principles and an aspiration that is measured, not claimed; SD-8 directs this same-family sub-agent cycle “until all remaining blocking issues are closed”. Nothing in the candidate claims that a sub-agent PASS accepts the architecture; acceptance of objectives, product scope and the major change stays with the stakeholder (§25 items 11-12; [workflow owner][workflow]).

## Verdict

**NO-PASS.** Two blockers remain, both introduced by revision-15 repairs:

- **A — `about` re-keys adversity on an undefined, structure-dependent “claim unit”.** The repair moved bearing onto content, but it also replaced revision 14's record-syntax anchor (“a failing assessment *on* a claim unit of `s`”, the realization's recorded target) with a current-state predicate: the evaluated content must be “present in a claim unit of `s`”. “Claim unit” is defined nowhere except §10's “`EVIDENCES` -> claim unit”, and §27.24 relies on that narrow reading. Under it, a byte-preserving shrink of the claim unit, a boundary move that puts the claim sentence in a sibling leaf no specification targets, a split with the required retarget, or a retirement of the specification relation (the `644eb72` B route) ends `adverse`, `qual`, the adjudication obligation and the `disputed` label, while the subject's revision and acceptance are unchanged.
- **B — the widened never-lost salvage admits records whose own authorization failed, and supersession is record syntax.** §6.8 step 6 now admits every never-lost record “whenever Admission rejects a request after authenticating its task binding, for any reason at any step”. That includes a failing assessment rejected *because* its `supersedes` field is unauthorized. S0 reads `superseded(x)` from admitted syntax on the premise that “authorization was checked at admission”. An independent agent who is neither the failing assessor nor the owner can therefore get its own failing assessment admitted as a superseder of another actor's failing assessment, then supersede it with its own authorized passing reassessment, disposing of the dissent through the chain.

Revision 15 genuinely closes `62c0b24` A on the trajectories that review named (boundary *growth*, merge into a unit that the retargeted specification then targets, adopted re-partition of the same shape) and repairs N2-N7 as found, with residues below. A and B are the sixth consecutive appearance of one family, “what can make a failing assessment stop counting”. Each repair has introduced a new input to that decision; both new inputs here (current claim-unit membership, the fields of a rejected record) are of the kind the family has already shown to be permissive. The repair for each is one rule, not a new mechanism (§5 below).

Requested checks: the four routing tests pass; `git diff --check` is clean; the model check is green at depths 4 and 5 (23/23 discriminators; 1,879,651 transitions at depth 5, matching §0.1) and red under `REV14=1`, `REV13=1`, `REV12=1`, `REV11=1` and `REV10=1`, each failing owner-grounded properties (P7 and Q in all five; P8 under `REV14`; P5 under `REV12`; P1 under `REV10`), not only the oracle. The model has one claim unit, no claim-unit membership, no `about` and no Admission, so it can see neither blocker (§6 below). None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — `about` makes adversity depend on current claim-unit membership

**Owner text at the candidate.**

- §6.6: `present(p) ⇔ ∃ effective unit v, ∃ admitted position m ≤ n : the content p evaluated (bytes and semantic declarations) lies unchanged in scope(v) in T_m, and rev(v, T_m) = cur(v), or […] reaches cur(v) through admitted EQUIVALENCE judgments`; `bears(a-) ⇔ every evidentiary premise p of real(a-) is present`; `about(a-, s) ⇔ the target premise of real(a-) is present in a claim unit of s -- may hold for several s`; `adverse(s, e) = { failing assessments a- admissible for e with about(a-, s) : bears(a-) }`; `qual(s) = ⋀_{e named by an admitted failing assessment a- with about(a-, s)} undisputed(s, e) -- whether or not e is still required`.
- §6.6 role table, evidentiary premise: “A structural change alone (boundary move, merge, split, adopted re-partition) never ends bearing (`62c0b24` Blocker A)”; Assessment disagreement: “A specification change that removes, splits or retargets the obligation: `qual(s)` still reads it”; the stated asymmetry: “`bears` under-approximates which moves remove *adversity*.”
- §10: “specification | evidence unit with `EVIDENCES` -> claim unit”; realization “**target** (claim unit revision)”. No other definition of “claim unit” exists in the candidate.
- §27.24, attacks on the repair: “Move the claim content out of every claim unit | `about` fails only if the content is no longer in any claim unit. The claim itself is then gone, and its subject's evidence obligations change through accepted structure”.
- §6.1: a quarantined delta is “**governance-neutral**: a re-partition of leaves inside one subject's unchanged regions into parts of that subject with its kind and domain”; §11.2: a governance-neutral delta “cannot change any subject or acceptance, so where policy permits, Admission may adopt it by a mechanical intake request”; §12.2: “Structural refinement makes no semantic claim. […] The subject's revision is therefore unchanged and its acceptance remains valid”; §15.7: “Agents may propose structural declarations in the unit manifest as ordinary content; those take effect only through Admission (§6.8 step 4).”
- §7.9 floor: a failing assessment “for any obligation that `qual` reads (§6.6)”.

**Trajectory (every step locally compliant).**

1. Subject `s` (a D3 design document, or D1/D2 authority) has leaf parts `c` = sentences “p q” and an adjacent leaf `d` = “r”, in that order. Specification `σ EVIDENCES c`. A deterministic realization `ρ` targets `c` at revision `r_c`; its evaluated target content is `E` = the bytes and declarations of “p q”. `X` assesses PASS and `Y` assesses FAIL (a tolerance-interpretation disagreement on one observation). `a_Y` bears, `about(a_Y, s)` holds (`E` is in `c`), `ev(s, e) = P`, the evidence is `disputed`, and an adjudication obligation is open.
2. An implementer whose write scope includes `s`'s manifest entries moves the boundary so that `c` = “p” and `d` = “q r”. (Equivalents: a foreign manifest edit adopted as a governance-neutral delta, mechanically where policy permits; a boundary move that places the claim sentence in `d` and leaves `c` covering a neighbour; `c` retired and split into new leaves `c1` = “p”, `c2` = “q”, with step 4's reference check forcing `σ` to be retargeted to one of them.) No content byte changes. `rev(s)`, `scope_id(s)`, tenure and acceptance of `s` are unchanged.
3. `present(E)` holds through `v = s` (the composite still contains “p q”), so `bears(a_Y)` holds: the §6.6 row is satisfied literally. But no claim unit contains `E`: the only `EVIDENCES` target is `c`, which now holds “p”. So `about(a_Y, s)` is false, `adverse(s, e) = ∅`, `qual(s)` no longer reads `e` through `a_Y`, the adjudication obligation disappears and the `disputed` label goes. If the move preceded the first passing assessment of a D1/D2 claim, the §7.9 floor never fires, because `qual` never read `e` while a passing assessment existed.
4. `X`'s assessment is stale (`rev(c)` moved). The designated runner reruns `σ` on the new `c`; the observation is the same, since `σ` evaluates code, not the claim's wording. If the assigned assessor reads the tolerance as `X` did, `ev(s, e) = T`, `qual(s) = T`, `valid(s) = T`, and §7.4 discharge is unqualified. The claim sentence “p q” that `Y` competently disputed is still in `s`, still accepted at the same revision, and now carries no qualification and no disposition.
5. **Retirement variant (`644eb72` B regression).** Instead of step 2, a specification change accepted at R2 removes `σ EVIDENCES c`. Under the §10 reading `c` is no longer a claim unit, `about(a_Y, s)` is false, and `qual(s)` drops `e`: exactly the outcome revision 14 repaired and §22 still forbids (“a specification change, accepted at R2, that removes the obligation's `EVIDENCES` relation […] must leave the claim qualified”).

The broad reading (“claim unit” means any unit of `s`) excludes all of this, but then §27.24's justification is false in the other direction, and the candidate never states that reading. An implementer must choose, and the reading the candidate's own rationale uses is the permissive one.

**What it violates.**

- The [evidence owner][evidence]: “Keep separate the **evidentiary target** (proposition/invariant evaluated) and **execution dependency**”; “A valid failing observation is evidence” (the observation and the evaluated proposition are unchanged, and the current authority is the same accepted revision of `s`); “supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified”; “Do not suppress contradictory admissible observations to manufacture a pass”.
- The [architecture owner][architecture]: “When an architectural concept carries normative meaning, define it before dependent invariants use it”. “Claim unit” is now the load-bearing term of an S0 predicate and is undefined.
- The candidate's S4 (“failing evidence whose realization still bears on the claim keeps it qualified until disposed of”), S10 (scope identity never implies anything about bytes or meaning), the §6.6 row and §0.1 claim that a structural change alone never ends bearing (true of `bears`, false of adversity), the §6.6 rule that retirement is not a disposition, and §12.2's “Structural refinement makes no semantic claim”.
- §27.24's premise “evidence obligations change through accepted structure” is false for the trajectory: the obligation `σ EVIDENCES c` is unchanged, and the change of what `c` covers was admitted as governance-neutral, which by §11.2 “cannot change any subject or acceptance”. No one judged it.

**Earliest owner.** D3 §6.6, the definition of `about` (with §10's realization target and the §27.24 rationale). Not Manual: whether a structural move of the claim's container ends adversity is the semantic decision `62c0b24` A already placed at D3, and the candidate's own rationale endorses the permissive outcome.

**Minimum repair direction.** Key `about` on the subject, not on current claim-unit membership. Either option keeps it in S0 and adds no record kind:

- *Subject scope.* `about(a-, s) ⇔ the target premise of real(a-) is present within scope(s)`, for any effective subject `s` and any unit inside it, claim-bearing or not. Content that leaves `s` only by a byte change of `s` or an accepted scope change then qualifies wherever it went, which is already the candidate's “may hold for several `s`” behaviour.
- *Immutable anchor plus content.* `about(a-, s)` holds for the subject that contained the target at `a-`'s admission (a record fact, as in revision 14) and for every subject whose scope now contains the target content.

Then delete or correct the §27.24 row, state beside the role table that a structural change alone never ends *adversity* (not only bearing), and either define “claim unit” or stop using it in derivation.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers, each followed by a passing rerun and assessment:

- a byte-preserving shrink of the claim unit that splits the evaluated content across two leaves of `s`: still qualified and `disputed`, adjudication obligation open;
- a boundary move that places the evaluated claim sentence in a sibling leaf that no specification targets: the same;
- `c` retired and split into new leaves with the required retarget to a leaf that does not contain the evaluated content: the same;
- removal of the only `EVIDENCES` relation targeting `c`: the same (the existing §22 case, now stated against `about`);
- each of the above on a D1/D2 claim with the structural change *before* the first passing assessment: the floor item is created;
- contrasts: an edit of the evaluated bytes without equivalence ends bearing; a scope change accepted for both subjects moves the qualification to the destination subject.

### B — the step-6 salvage admits never-lost records whose own authorization failed

**Owner text at the candidate.**

- §6.8 step 6: “Whenever Admission rejects a request after authenticating its task binding, for any reason at any step, the admission record that rejects it still admits every never-lost record it carries, bound to the same task, so nothing reported or observed adversely is lost with the rejected work”. Never-lost records are “reports, challenges […] and failing assessments”.
- §6.6 S0: “*Record syntax:* record targets, and `superseded(x)` ⇔ some admitted record names `x` in its `supersedes` field (authorization was checked at admission).” “Supersession is purely syntactic (S0).”
- §6.6, effective disposition: “`d` supersedes `a-`, directly or through a chain of supersessions: an explicit reassessment of the realization by `a-`'s own assessor, or the owner's adjudication or discriminating new assessment”; `eff(d) = current(d)` for an independent support-tier superseder.
- §6.8 step 3: “actor class qualified for each judgment kind; […] the bound role permits each record kind and outcome”.
- A5: “What it may write, which record kinds and outcomes it may submit, and which decisions it may make are fixed by the role and the task's work contract and are checked at Admission”. T1: “Agent outputs are untrusted proposals until admitted.”
- §0.1 (revision 15, N2 repair): “Every rejection after authentication admits the never-lost records a request carries”.

**Trajectory (every step but one locally compliant; the non-compliant step is the one Admission exists to refuse).**

1. Claim `s` has the live disagreement of A's step 1 (`X` PASS, `Y` FAIL as `a_Y`, both on realization `ρ`); `ev(s, e) = P`.
2. Agent `Z` holds an authenticated task whose role may submit assessments (for example an assessment of an unrelated realization). `Z` is neither `a_Y`'s assessor nor bound to the owner's adjudication obligation, and its lineage is `ATTESTED_FRESH` and disjoint from the claim's author. `Z` submits a request carrying a failing assessment `a_Z` of `ρ` whose `supersedes` field names `a_Y`.
3. Step 3 rejects the request: `Z` is not authorized to supersede `a_Y`. The binding was authenticated earlier in step 3, so step 6's salvage admits `a_Z`, a failing assessment, “for any reason at any step”. Nothing in the candidate strips or voids the unauthorized field. `superseded(a_Y)` becomes true in S0. `a_Z` itself bears and is adverse, so `ev` stays `P` for now.
4. In a later request of the same task, `Z` submits a passing reassessment `p_Z` of `ρ` superseding `a_Z`. That is authorized: “an explicit reassessment of the realization by `a-`'s own assessor”.
5. `p_Z` disposes of `a_Z` directly and of `a_Y` “through a chain of supersessions”. `eff(p_Z) = current(p_Z) = T`, so `undisputed(s, e) = T`; `p_Z` is also a current passing assessment, so `ev(s, e) = T`, `valid(s) = T` and §7.4 discharge is unqualified. The `disputed` label and the adjudication obligation go. For a D1/D2 claim the existence-keyed floor item survives, but validity and discharge are unqualified meanwhile. If `a_Z` instead assesses a realization that is inadmissible for `e`, step 4 is unnecessary.

The same route lets a role-forbidden or unqualified actor's failing assessment or challenge enter as evidence or as a block. Those effects are restrictive, but they also defeat A5's Admission check.

**What it violates.**

- The [evidence owner][evidence]: “route adjudication to the governing claim/owner”; “Do not resolve material assessment disagreement by […] latest-editor order […]. When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement.” Here the dissent is resolved by an actor the candidate does not authorize to resolve it, through a record Admission rejected.
- The candidate's S0 premise that supersession “authorization was checked at admission”, the §6.6 disposing relation (own assessor or owner only), A5, T1, and §7.5's assignment of dispositions to the owner's R2/R3 decision.

**Earliest owner.** D3 §6.8 step 6 (the salvage clause), read with step 3. Not Manual: which records a rejecting entry admits, and with which fields, decides what enters S0.

**Minimum repair direction.** One clause: a rejecting entry admits a never-lost record only if that record itself passes schema, reference and its own step-3 checks (actor qualification, role permission for its kind and outcome, and authority for every `supersedes` and target it names). A record that fails its own checks is recorded as refused, with its identity, for provenance, and is never read by S0. Revision 14's purpose survives: what is salvaged is a record rejected *because of the rest of its request*, not a record rejected for itself.

**Required discriminators**, through real Admission and Derivation:

- the trajectory above: after both requests the claim stays qualified and `superseded(a_Y)` is false;
- a failing assessment, a challenge and a report each submitted under a role that does not permit its kind: rejected, not salvaged, and inert in S0;
- contrast: an authorized failing assessment (including an own-assessor reassessment carrying `supersedes`) co-submitted with a stale task result is salvaged with its fields, as revision 14 required.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged from `62c0b24` N1. The 2026-10-12 adoption instruction is still a paraphrase (§0.4; stakeholder record, Not covered). The handoff independently binds this Review to 7.2.1, and the release state names 7.2.1 accepted-current. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — salvage residue outside blocker B

- Steps 1-2 run before the binding is authenticated in step 3, so a request rejected for a *sibling* record's schema, secret-check or reference failure still loses its failing assessment. Either authenticate the binding first or validate each never-lost record separately.
- Step 3 now accepts envelopes signed by “a retired issue key that was never compromised”, with no bound on when the envelope was issued. Whoever keeps the retired key material can mint new envelopes for never-lost records indefinitely. Bind such envelopes to an issue position before the retirement record (Manual item 14).

Earliest owner: §6.8 steps 1-3; Manual items 6 and 14.

### N3 — human independence: §6.6 and step 3 disagree

§6.6 now says that, where policy names no other qualified human, the claim's author may dispose as owner and “step 3 admits the disposition as satisfying the requirement with the common-mode dependency recorded”. Step 3's text still says a disposition satisfies independence “only when its lineage class is `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` and its lineage is disjoint from the author's”, which the author's own judgment never is. Under step 3 the `62c0b24` N3 restriction persists; under §6.6 the intended routing holds. The failure mode is restrictive. Also unstated: who “authored the claim” after a structural change or a merge (A's step 2), and which decision class applies when `about` holds for subjects of different domains. Repair: carry the §6.6 exception into step 3's text; define claim authorship by the content's authoring records; take the highest class among the subjects `about` names. Earliest owner: §6.8 step 3; Manual item 3.

### N4 — presence anywhere keeps repaired failures bearing

`present` accepts the evaluated bytes in *any* effective unit. Byte-identical archives, frozen profile resources, vendored copies and verbatim quotations are ordinary content (this repository holds all of them). Once the evaluated claim or code also exists in such a copy, a genuine content change never ends bearing. Every repaired failure then needs an explicit R2 (or R3) disposition, and §22's contrast “an edit of the claim's own bytes without equivalence ends bearing” fails whenever an old copy exists. The candidate calls this restrictive (§27.24); it is, but it transfers routine burden to owners and the inspector (§1.2: SSDS succeeds only if machinery reduces, rather than transfers, complexity). Repair: search for each premise within its role's scope (the target within the subjects `about` names, execution content within the specification's current execution closure), so that copies elsewhere count only through `about`. Earliest owner: §6.6; Manual item 5; §26 empirical trigger.

### N5 — content presence is underdefined for semantic declarations and unavailable bytes

`E` includes “semantic declarations”, and §6.2 places authored relations “inside the subject unit's scope (or its manifest declaration)”. A relation declared for `c` names or implies its declaring unit, and a manifest-held declaration does not lie “in scope(v)” at all. After a merge into `cd` the declaration's subject changes. Unless presence compares declarations in a form that does not depend on the declaring unit's identity, the merge discriminator fails for every claim unit that carries an authored relation, which is ordinary for D1-D3 content. Separately, the evaluated bytes of a frame record live in a candidate commit; if that object becomes unavailable, presence must count as true (“uncertainty never removes adversity”), which needs retention or recording of `E`. Earliest owner: Manual items 5 and 14; add a §22 merge case with an authored relation on the claim unit.

### N6 — the support-graph acyclicity claim no longer holds

§6.6 says the edges from a subject to dispositions of failing assessments on its claim units “change only when admitted records are added. Absorption adds none”, and that a cycle “can arise only from corrupted input”. Because `about` is now a function of current content, an absorbed or admitted content change that copies `E` into another subject `t` adds a `valid(t) → disp(a-)` dependency without any new record, and step 5 does not examine it. The least fixed point stays unique (S2 is monotone), and a resulting cycle evaluates to `F`, which is restrictive. But the one-pass topological claim, the step-5 guarantee and the “corrupted input” diagnosis are false as stated. Repair: make the static over-approximation range over every subject (or every subject that ever contained `E`), or compute the lfp without relying on acyclicity and classify such a cycle as an ordinary finding. Earliest owner: §6.6 Uniqueness; §6.8 step 5.

### N7 — the model check is accurate but cannot see A or B

All numbers in §0.1 reproduce. `REPART` is a useful addition, and `REV14` fails P7, P8 and Q. What remains:

- one claim unit, with no membership, no `about` and no content location, so the model cannot represent A, and its `RETIRE` flag never interacts with claim-unit status;
- Admission and authorization are outside the model, and every `supersedes` is taken as authorized, so it cannot represent B;
- P8 fails under `REV14` only through retirement (without retirement, `REPART` cannot raise the term because it stales every earlier pass), so it tests one interaction, not structural moves in general.

Earliest owner: §22 and the model check. Add A's and B's discriminators to §22. Extending the model is optional; if done, add a second leaf and a claim-unit relation so that `about` can be false (PEM DS-001).

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 62C0B24

| Finding | Disposition | Basis |
|---|---|---|
| A — boundary move that grows the claim unit | **Closed** | `present` through `v = c` at `m = n`; `about` holds because `c` still contains `E` |
| A — merge into `cd` with `σ` retargeted to `cd` | **Closed** on the stated trajectory | `cd` contains `E` and is an `EVIDENCES` target; residue N5 for claim units with authored relations |
| A — adopted governance-neutral re-partition | **Closed** for growth and merge; **open** for shrink, move-out and split | Blocker A |
| A — family “structural change ends adversity” | **Open** | Blocker A: moved from `bears` to `about` |
| N1 adoption provenance | **Partly closed** | Unchanged (N1) |
| N2 salvage narrower than stated | **Closed in text, over-broad** | Blocker B; residue N2 |
| N3 independence of human dispositions | **Partly closed** | Defined in §6.6; step 3 contradicts it (N3) |
| N4 floor keyed per obligation | **Closed** | “for any obligation that `qual` reads […] on a claim that has any admitted passing assessment”; inherits A through `qual` |
| N5 bearing after a rebase | **Closed** | §6.9 Rebase: “it is never dropped because `X` itself was not integrated” |
| N6 model's single `MOVE` | **Partly closed** | `REPART` and P8 added; A and B outside the model (N7) |
| N7 obligations only in a candidate frame | **Closed** | Stated as intended and restrictive (§6.6) |

### Earlier Reviews

The `62c0b24..203a42b` workplan diff touches §0, §0.1, the S0 bearing line, the §6.6 role table, `present`/`bears`/`about`/`adverse`/`qual` and their prose, decision class and floor text, §6.8 steps 3 and 6, the §6.9 rebase sentence, the §7.9 floor, §10, §21 items 5 and 14, §22, §26, §27.24-§27.25 and §28. It touches no persistence, publication, intake, migration, component or inheritance section. No `source/`, `dist/`, `orchestrator/`, test, release-state, PEM or stakeholder-record path changed (verified with `git diff --stat`).

- **644EB72 A (co-submitted stale records, contract tightening, discharged-first): closed.** The salvage is wider, not narrower; blocker B concerns over-admission only.
- **644EB72 B (obligation removed, split or retargeted): partly closed.** It holds under the broad reading of “claim unit” and regresses under the §10 reading (blocker A, step 5).
- **4C35D92 A1-A2 and 97E753F A, B1, B2: closed.** `ev`, `undisputed`, `disp`, `eff` and `contested` are unchanged; the discriminators give the expected values.
- **124B0B7 A and FFBAD17 A: closed.** P1-P4 are green to depth 5.
- **FB3E542 A: closed**; `bind(j)` is unchanged. **FB3E542 B: partly closed**, through blockers A and B.
- **Strata.** `present` and `about` read observed trees at admitted positions, effective structure and record syntax, so they are S0, and S0 stays a function. S1 is unchanged. S2 is monotone with one least fixed point; the acyclicity claim needs correction (N6), but single-valuedness does not depend on it. The `f9d9de8` configuration and mutual-validity cycles remain rejected by step 5.

The remaining 730490D, AC71FA9, F3608F5 and FFBAD17 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Boundary move growing the claim unit; passing rerun | Holds |
| Merge into `cd`, `σ` retargeted to `cd`; passing rerun | Holds (N5 for claim units with authored relations) |
| Byte-preserving shrink of the claim unit splitting the evaluated content | **Fails** (A) |
| Claim sentence moved into a sibling leaf no specification targets | **Fails** (A; §27.24 endorses the outcome) |
| `c` retired and split, `σ` retargeted to a part without the evaluated content | **Fails** (A) |
| Removal of the only `EVIDENCES` relation on `c` | **Fails** under the §10 reading (A, `644eb72` B regression) |
| Byte-preserving refinement of `c` into parts (`c` kept as composite target) | Holds |
| Merge, then editorial edit of `cd` with equivalence | Holds (`m` at the merge position) |
| Foreign file rename absorbed (content leaves every effective unit) | Bearing lapses while `s` is invalid anyway; returns on realignment; holds |
| Edit of the claim's bytes without equivalence, no other copy | Ends bearing, as designed; consistent with “A rerun on a changed candidate creates a new realization” |
| Same edit with a byte-identical archived copy of the old text | Keeps bearing (N4, restrictive) |
| Code fix while a frozen copy of the old code exists | Keeps bearing (N4, restrictive) |
| Failing assessment with unauthorized `supersedes`, rejected at step 3, then own passing reassessment | **Fails** (B) |
| Role-forbidden failing assessment or challenge, rejected at step 3 | Salvaged; restrictive, defeats A5 (B) |
| Request rejected at step 1 or 2 for a sibling record | Failing assessment lost (N2) |
| Envelope minted on a retired, uncompromised key after retirement | Accepted for never-lost records (N2) |
| Author-owner disposition in a single-human project | §6.6 and step 3 disagree; restrictive under step 3 (N3) |
| Evaluated content copied into another subject's claim unit by absorption | Restrictive spill-over; support edge added without a record (N6) |
| Frame-`X` failing and passing assessments, clean rebase to `X'`, integration | Holds (§6.9) |
| Split obligation with passing assessments on the successor only (D1/D2) | Floor fires (N4 of `62c0b24` closed) |
| Loss boundary with retained failing assessment and pre-boundary disposition | Holds (`cont`) |
| Workflow layer, publication, frame, intake and migration trajectories of earlier records | Hold as recorded; untouched by revision 15 |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Revision 15 removes the unit-revision test and adds two S0 functions (`present`, `about`). No primitive, record kind, store or component is added (§27.25). Both repairs needed here are one-rule changes: `about` keyed on subject scope or an immutable anchor, and the salvage limited to records that pass their own checks. Neither adds a mechanism.

**Convergence.** The [convergence owner][convergence] says: “Recurrence around a complicated mechanism is evidence to challenge that delegated concretization, not evidence that the mechanism has become authority.” The family “what makes a failing assessment stop counting” has now produced blockers in six consecutive Reviews (`124b0b7`, `97e753f`, `4c35d92`, `644eb72`, `62c0b24` and this one). The common cause is visible: each repair adds an input to that decision, and each input that reflects *current* structure or a *rejected* record's content opens a route. A bounded family closure is now justified. Write one rule and check every predicate against it: *a failing assessment stops counting only when the content it evaluated changes without equivalence, or when an authorized, standing disposition names it; every other input is an immutable record fact or a restriction.* Then enumerate the S0 facts that `adverse`, `qual`, `disp` and the floor read (claim-unit membership, obligation existence, unit identity, supersession syntax, salvage) and test each against that rule. Revision 15 has the right content anchor; the blockers are where its new inputs break the rule.

**Predecessor comparison.** Revision 15 did not touch §16.2 or §18. Blobs verified at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The frozen Core profile resources `ssdp-protocol-6.0` through `6.6`, `7.0`, `7.1` and `7.2` (and `sdp-protocol-5.16`) are present at the candidate under `orchestrator/src/sdp_orchestrator/core/resources/protocol/`, consistent with PC-001 and §24. The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. The uncovered later interval proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model check is green in all 23 discriminators while A and B hold; it has one claim unit, no about and no Admission, so its green result cannot discriminate either defect.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; present at the candidate; preserved by §24. Their byte copies also feed N4.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair at the owning D3 rules (§6.6 about, §6.8 step 6) and regenerate §0.1, §22, §27 and the check from them.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 15.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current, with public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff. The `62c0b24..203a42b` diff changes no `source/`, `dist/`, `orchestrator/`, release-state or PEM path, and no §0.4, §19 or §24 text, so the earlier owner comparison between `22f4bdba` and `aaeaf8b6`, the §0.4 obligation table and the §19 landing points stand. The inherited evidence doctrine is not yet realized at A and B.

## 6. Qualification-program adequacy

§22's disagreement group now carries the `62c0b24` discriminators (boundary growth, merge with retarget, adopted delta, D1/D2, the refinement and content-edit contrasts), the salvage cases (step 5 or 8 rejection, rotated key) and the rebase and frame-only cases. It cannot discriminate A or B. Its only structural cases *grow* or *merge into* the claim unit, which are exactly the cases `about` handles; its salvage cases test that more is admitted, never that an unauthorized field is refused. The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 15 read with the narrow “claim unit” is such a concretization for A, and the literal salvage clause is one for B: every listed §22 case and every model-check property stays green. Add A's and B's discriminators, the N2 and N5 cases, and a content-edit contrast that runs with and without a byte-identical copy elsewhere (N4).

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `c5b344b2…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `9722979`, were excluded.
- **Owners read** at `aaeaf8b6` with `git show`: the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge); architecture (read first: admissibility, “one authoritative representation/state”, “define it before dependent invariants use it”, Review); evidence (target vs execution dependency; Applicability, immutable observation and superseding assessment; binding health; Assessment disagreement); testing (smallest plausible wrong concretization); convergence (family reasoning, recurrence as evidence against a concretization); workflow (Optional independent cognitive trajectories); the kernel's Challenge text. Release identities resolved from `PROTOCOL-RELEASE-STATE.yaml` at the candidate.
- **Candidate read.** §0, §0.1, §1, §2, §5, §6.1-§6.9 in full, §7.1-§7.10, §9.3, §10, §11.1-§11.3, §12.1-§12.2, §15.6-§15.7, §21 items 5-7 and 14, §22 (disagreement and model-check groups), §27.24-§27.25 and §28; the full `62c0b24..203a42b` diff including the authority index and the model check; the stakeholder record; the routing test; and the model check source.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.022 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check 62c0b245… 203a42bd…`: **exit 0**, no diagnostics.
- **Model check**, depth 4 (76,366 transitions in every mode):
  - default mode (revision 15): **0 failures, 23/23 discriminators as expected, exit 0**;
  - `REV14=1`: **1,266 failures (P7 60, P8 148, Q 420, O 638)**; one discriminator differs (`62c0b24` A); **exit 1**;
  - `REV13=1`: **11,492 failures (P7 872, Q 3,628, O 6,992)**; three differ; **exit 1**;
  - `REV12=1`: **11,944 failures (P5 81, P7 872, Q 3,797, O 7,194)**; five differ; **exit 1**;
  - `REV11=1`: **11,900 failures (P7 872, Q 3,786, O 7,242)**; eight differ; **exit 1**;
  - `REV10=1`: **13,028 failures (P1 262, P7 872, Q 3,620, O 8,274)**; nine differ; **exit 1**.
- **Model check**, depth 5, default mode: **1,879,651 transitions, 0 failures, 23/23 discriminators, exit 0** (about 120 s), matching §0.1.

  Each sensitivity mode fails at least one owner-grounded property (P1-P8 or Q), not only the oracle.
- **A and B.** Deductive, from the quoted contract text. Neither is representable in the model's vocabulary, so no scratch reproduction was attempted.
- **Identities.** Verified the predecessor blobs, the release-state identities, the frozen-profile presence, the PEM blob identity, the stakeholder-record blob and the changed-path list above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, structural change, admission and salvage, supersession, disagreement and closure. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed through multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering and evidence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run on the working-tree file whose blob equals the candidate's, failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for historical evidence routes (`55c08526…`, `81375d81…`), which `git cat-file` cannot resolve. This checkout is a **shallow clone**. That is an environment limitation, not a PEM defect and not a pass.
- **Remote state.** `origin/main` is the local tracking ref. No fetch was performed and no remote-state claim is made.
- **Readings and Manual compositions.** A rests on the narrow reading of “claim unit” that §10 and §27.24 support; the candidate states no other. Its trajectory assumes an implementer's write scope may include the manifest entries of a claim's subject (§15.7 permits it; policy may narrow it) and that the rerun is assessed as `X` assessed. B assumes that step 3's authorization of `supersedes` is the check that fails, as §6.6 S0 states, and that one task may submit a second request after a rejection; it needs nothing the Manual decides. N2, N3 and N5 assume Manual compositions (items 3, 5, 6 and 14).
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The [workflow owner][workflow] says: “Separate context improves process independence but not epistemic independence when agents share model, source corpus, toolchain or oracle”. In particular, the `62c0b24` Review (same family) proposed the very repair direction revision 15 adopted, and this Review found its edges only by attacking the new inputs that repair introduced. A different family might frame the family differently.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair of `about` (§6.6, A) and of the step-6 salvage (§6.8, B), with §0.1, §22, §27 and the model check regenerated from them, and a replacement immutable candidate. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/203a42bddf559234cb7b39283f014ada7a86d8d6/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[architecture]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md

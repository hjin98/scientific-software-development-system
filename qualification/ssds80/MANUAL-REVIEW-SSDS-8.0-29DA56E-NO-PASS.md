# SSDS 8 Architecture Manual — Independent D3 Review, candidate 29da56e

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 29da56e68960b29fb9a55471e99f0703e6d8c4c7
    SCOPE: the whole proposed durable Manual: (a) §21/§16.2 closure, (b) fidelity to the reviewed
           contract and the §0.3 refinements R1-R13, (c) adequacy (out-of-matrix), (d) inheritance and
           capability transfer, (e) qualification design, (f) doctrine-realization map, (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
           blob 6200928b46b50efcb857cfcd5fbbcb91dd242109 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md
           blob c083d85502422f97c1fa0e99f10513443b8a80cf (verified; aid, not authority)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
           design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216 (verified)
    PHASE B CANDIDATE: e23f14208be869e6a78cfd7b312e447254ee1851
           workplan blob 610f373b97fb8152d2a5742e17fa172e12204756 (verified)
    PHASE B REVIEW: qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
           (both read from PROTOCOL-RELEASE-STATE.yaml accepted_current, not assumed)
    FROZEN ARCHITECTURE 1.6.0: orchestrator/docs/architecture.md
           blob 39e6de727f6c35402962509d30d947962992eaad (byte-unchanged, verified)
    HANDOFF: qualification/ssds80/MANUAL-REVIEW-HANDOFF-SSDS-8.0-29DA56E.md (prompt below its rule)
    PRIOR REVIEWS: every Manual NO-PASS record the handoff names (6FF4ED1 through 51070E5) and
           the Phase B E23F142 PASS: hypotheses and regression inputs only, never authority
    REVIEW METHOD: immutable git-archive snapshot of the candidate; governing owners read with
           git show at the public-source ref; diff 51070e5..29da56e read hunk by hunk; Part 0,
           §3, §5, §6.5-§6.8, §8, §10, §12, §13.7, §18.4, §19.5 and §31 read in full, the rest
           located and spot-checked for the mechanisms prior closures rely on; family-level
           falsification of the permissive-resolution family (convergence owner, "Review strategy
           after recurrence"), attacked in both directions; requested document checks
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session,
           given only the handoff file; no authoring conversation
    MUTATION: this record only; no commit, push, source change or PEM update

Line numbers below refer to Manual blob `6200928b`. Scratch files were kept under `$TMPDIR/ssds80-manual-review-29da56e/`; nothing in this record depends on them remaining available.

## SERIOUS CHALLENGE

**None against accepted authority.** The blocker below lies in the proposed Manual's realization of the independence and decision-class floors. Those floors are coherent at SSDP 7.2.1, in the parent's governing invariants (A5, A9, restated in Manual §0.4) and in the stakeholder's direction. The reviewed workplan's S1 adjudicator rule ("qualified actors per policy") shares the shape of the defect for failing assessments. That rule is a cycle contract, not accepted-current authority, and narrowing it is surfaced below as a contract change to list in §0.3, not as a challenge to SSDP. No accepted project D1/D2 proposition is relied on.

Governing statements used (paths at `aaeaf8b6`):

| Owner and locator | Text applied |
|---|---|
| `source/roles/software-design/SKILL.md` | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| `source/shared/references/architecture-and-design.md`, D3 formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| `source/shared/references/workflow-and-workplans.md`, Review | "Review independence means the reviewing context did not author the candidate and does not inherit author conclusions" |
| Same, human gates | "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." |
| `source/shared/references/evidence-evolution-and-dependencies.md`, Assessment disagreement | "route adjudication to the governing claim/owner or obtain discriminating evidence. Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position." |
| `source/shared/references/convergence-and-cycle-economy.md`, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism" |
| Same, Review strategy after recurrence | the next Review "proportionately shifts from isolated finding discovery toward bounded sibling/family closure, simplification/re-derivation" |
| `source/shared/references/testing-and-validation.md` | "Ask whether evidence could remain green while that owner is materially broken. If yes, it cannot close that owner claim." |

## Verdict

**NO-PASS. One blocking family survives (B1): independence and decision class are attached to the challenged record's tier, not to the effect of the adjudication.**

The `51070e5` B1 repair introduced one predicate, `res`, and states that it "governs every record whose effect ends an objection to a judgment" (§5.5, line 777). R13 (line 98) states that the A5/A9 floor "applies to every adjudication that ends an objection". The text enforces `res` and the new class floor only for "an `ADJUDICATION` of a challenge against a support-tier record" (§5.3 `gate`, line 674; §8.3 step 3, lines 1109-1110). S1, however, carries permissive effects through challenge-tier records, observations and subject triples as well:

- an upheld counter-challenge lifts a revocation (lines 668, 691);
- a dismissal restores an observation's standing for the staleness stops (lines 963-965);
- a dismissal unblocks a subject revision (line 684).

Each of these ends an independent objection with no independence or class check. The concrete trajectory (§1) restores an acceptance that an independent adjudicator revoked, through the author's own upholding of a counter-challenge.

This is the fourth consecutive round in the authority-of-permissive-resolution branch (`051cce3` B1, `9e5a763` B1, `51070e5` B1, now this). It is a non-local recurrence with a shared cause, so §1 gives a family-level assessment and options. The matching, content-identity, partition, revision-run, acting-rule, gate-minimum, publication and witness families held under the trajectories in §6. The requested document checks pass (§10). They do not exercise this defect. G1 stays open.

## 1. Blocker

### B1 — Permissive adjudications outside "a challenge against a support-tier record" end objections with no independence or class check

**Earliest owner:** proposed D3 Manual §5.3 `gate` (lines 674-675) and §8.3 step 3 (independence and adjudication-class bullets, lines 1109-1110), with §5.5's one-predicate paragraph (line 777), the §3.4 `ADJUDICATION` row (line 486) and R13 (line 98). Parent closure obligations implicated: workplan §21 items 3, 5, 7, 23 and 27. This is an architecture defect. The reviewed S1 rule shares the assessment-family siblings (b) and (d) below, so the repair must list that narrowing in §0.3, as R13 already does for its own narrowing.

**Family:** judgment disagreement, authority of permissive resolution. Shared cause: eligibility is attached by enumerating the target classes and routes that end an objection, not to every record whose S1/S2 effect is permissive. Each round has found a route the enumeration missed. This round's route is chain depth and target tier. The repair said "one predicate" but keyed its application on the challenged record's tier.

#### Exact text

§5.3, lines 666-668 and 674-678:

```text
relaxer(y)  ⇔ y ∈ WITHDRAWAL ∪ RISK_OVERRIDE ∪ CONTINUITY_ATTESTATION
              ∨ (y ∈ ADJUDICATION ∧ y.outcome = DISMISSED ∧ ¬counter(y.target))
              ∨ (y ∈ ADJUDICATION ∧ y.outcome = UPHELD ∧ counter(y.target))
gate(y)     = cont(y) ∧ (res(y) if y ∈ ADJUDICATION of a challenge against a support-tier record, else T)
                  if relaxer(y); T otherwise
in_force(y) ⇔ gate(y) ∧ ¬∃ c ∈ CHALLENGE : c.target = y ∧ (upheld(c) ∨ (c.blocking ∧ open(c) ∧ ¬counter(c)))
```

§5.3, line 691: "a revocation ends only when a counter-challenge is upheld, and that upholding is itself a relaxer (challengeable, suspended by an open blocking challenge, withheld by a later loss boundary)". No independence condition is named.

§8.3 step 3, line 1109: independence applies to "every `ADJUDICATION` of a challenge whose target is a support-tier record (51070e5 B1) … An adjudication is judged against the authors of the challenged record's target." Line 1110 applies the class floor only to "an `ADJUDICATION` of a challenge against a support-tier record decided by an authenticated human in class R3".

§5.5, line 777: "**One predicate governs every record whose effect ends an objection to a judgment** … Each counts only where `res(d)`; a record admitted as non-independent is kept as data and resolves nothing."

Closure map line 273: "each by a record admitted as independent (R13: adjudications included; an R2 adjudicator never lifts an R3 human decision)".

A counter-challenge targets an adjudication. A challenge against a realization targets an observation-tier record. A challenge against a triple targets no record at all. None of these is "a challenge against a support-tier record", so `gate` and step 3 never examine the adjudicator.

#### Concrete trajectory (author restores a revoked acceptance)

This uses a D4 subject `s` whose policy assigns R2 acceptance and ordinary-challenge adjudication in D4 to a qualified class that includes humans and agents. Both are within the §3.5 floors. Executions, slots and bindings are clean, and nothing is forged, stale or seeded.

1. Alice, a human, authors revision `r` of `s` through an `IMPLEMENT` task. It integrates. Independent reviewer `P` (`ATTESTED_FRESH`, disjoint) records `ACCEPTANCE PASS` `z` on `(s, σ, r)`, so `valid(s) = T`.
2. Reviewer `H` finds a contract violation and raises an ordinary, **non-blocking** challenge `c1` against `z`. Any role may raise one (§12.3). `ADJUDICATE(c1)` is derived.
3. Independent adjudicator `A` records `a1 = ADJUDICATION UPHELD` on `c1`. `a1` is restrictive, so `status1(z) = REVOKED`, `valid(s) = F`, `ACCEPT(s)` is derived again and descendants relying on `s` in `validity` mode lose currency. The system is behaving as intended at this point.
4. Someone, possibly Alice, raises `c2`, a counter-challenge against `a1` (`counter(c2)`, since `a1` is restrictive). `ADJUDICATE(c2)` is derived for "the actor policy names (R2/R3)" (§10.2).
5. Alice is in the policy-named adjudicator class, and she records `a2 = ADJUDICATION UPHELD` on `c2`. Alternatively, the `ADJUDICATE(c2)` envelope runs on a manual route in the implementing session, with `UNKNOWN` lineage. Step 3 checks actor class, envelope, role and kind. Neither the independence bullet nor the class bullet applies, because `c2`'s target is an adjudication. `a2` is admitted with full effect.
6. `relaxer(a2)` holds, and `gate(a2) = cont(a2) = T` because the `res` conjunct is skipped. So `in_force(a2)` and `upheld(c2)` hold, `in_force(a1) = F`, `upheld(c1) = F`, and since `c1` is non-blocking, `status1(z) = CLEAR`.
7. `base(z) = T`, so `valid(s) = T` again. `ACCEPT(s)` disappears, and dependants regain currency.

An independent revocation has been undone by the revision's own author, or by a non-independent session. No record of a common-mode dependency is made and no inspector entry shows it. This violates A5 ("no actor reviews or accepts its own work") and A9 ("reviewer independence is constructed, not requested"). It also contradicts the Manual's own R13 and line-777 claims. The trajectory has the `51070e5` B1 shape on a route that repair did not cover.

#### Bounded sibling list (one family-level problem)

| Variant | Candidate result | Required result |
|---|---|---|
| (a) The trajectory above, against a passing `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS` or `GATE_DECISION ACCEPT`, and against an upheld challenge on a **subject triple** ("revokes it permanently", line 779), whose stated repair is "a successful challenge of the upholding" (line 691) | the revocation is lifted by a non-independent counter-upholding | no effect without `res`; no agent or author restores it |
| (b) A blocking challenge against an **observation** (a realization serving stops (1)/(3), §6.6 "standing"), dismissed by the claim's author or an `UNKNOWN`-lineage adjudicator | the observation stands again and can make a failing assessment stale, so `undisputed` rises | the reviewed rule requires every disposition to be independent of the claim's authors (workplan §6.6); a dismissal that restores a stop is permissive and must meet it |
| (c) A blocking challenge against a **subject triple**, dismissed by the revision's author | the block lifts and `valid(s)` returns | the same floor as a dismissal of a blocking challenge against the triple's acceptance, which `gate` already requires |
| (d) A blocking **counter-challenge** against an independent upholding that disposed of an adverse judgment or failing assessment (`contested`, §5.5 `stands⁻`, §6.7), or a blocking challenge against an independent relaxer adjudication, dismissed non-independently. `DISMISSED` of a counter has polarity "none", so `gate` is `T` | the objection to the resolution ends; the veto or qualification lifts again | the same eligibility as any record ending an objection |
| (e) **Class:** an R3 human upholds a challenge against a human `GATE_DECISION ACCEPT`, or a Serious Challenge against a D1 triple, and an R2 agent upholds the counter-challenge. Line 1110 does not apply; §3.5's floor names only "Serious Challenge adjudication"; §3.4's "D1/D2 claims" does not say what domain a counter-challenge's target has | an R2 record lifts an R3 human decision, contrary to the closure map's "an R2 adjudicator never lifts an R3 human decision" and §12.4 ("never down") | class not lower than the highest class in the chain |
| (f) **Reference set:** "the authors of the challenged record's target" (line 1109) names, for a counter-challenge, the authors of `c1`, which is the objector, and it is undefined for targets that are obligations or reports | wrong or undefined set | the authors of the content at the root of the chain |
| (g) The support route itself: §5.5 says "independence is required to support, never to object", and §4.4 says a non-independent equivalence "covers nothing". Yet the normative `base`, `current`, `sat(content)` and `ACC` read no `res` (only discharge does, §10.4). Literally, a non-independent `ACCEPTANCE PASS`, such as a human author's direct record, enters `ACC(s)` and makes `valid(s) = T`, which retires `ACCEPT(s)` | prose and formula disagree; one literal reading is permissive. Inherited from the reviewed `valid` formula | `res` is a condition of support for every kind with an independence requirement |
| Held: upheld challenge against an adverse judgment, dismissal of a blocking challenge against a passing support-tier record, supersession, relief and assessment disposition, each non-independent | no effect (lines 768, 674, 1111, 773, 995) | keep |

The rows share one cause: `res` is consulted at named consumer sites (`stands⁻`, `relieved`, `eff`, `gate` for one target tier) and not at the two places every permissive effect passes through. Those places are `base` for support-tier records and `in_force` for challenge-tier records.

#### Convergence assessment and options

The active simplification trigger applies. The same mechanism, which records may end an objection, has been patched in four consecutive rounds. Each round added or qualified one route. The `51070e5` Review's recommended direction ("one S0 eligibility predicate … for every record whose effect ends an objection") was adopted in name, but it was applied by target tier. Per Phase C handoff §5, the options for the stakeholder are:

1. **Bounded simplification at Admission (recommended; narrows; removes `res` from S1).** Admit an `ADJUDICATION` only if it is independent of the authors of the content at the root of its challenge chain (the owner exception and common-mode record as §6.8), and only if its class is not lower than the highest class of any record in that chain. Otherwise refuse it (`AUTH_ACTOR`/independence code). Then:
   - `gate` returns to `cont` alone;
   - `stands⁻` drops its `res(a)` conjunct;
   - the line-777 route list and line-1110 bullet collapse into that one admission rule.

   A refused adjudication answers nothing, so `ADJUDICATE(c)` stays dispatchable, which also closes N1 here. Every challenge is never-lost, so no objection is lost. A blocking challenge still blocks, and a non-blocking one keeps its S3 obligation. List the narrowing of the reviewed S1 adjudicator rule in §0.3, extending R13.
2. **Bounded simplification in derivation (adds nothing; keeps the current S0 fact).** Read `res` in exactly two places:
   - `base(z) = F` when `z` has an independence requirement and `¬res(z)`, which closes (g) and makes the separate `relieved` and supersession conjuncts redundant;
   - `in_force(y)` for every `ADJUDICATION` whose effect can be permissive in S1 or S2, which is every adjudication. Its independence is measured against the chain root, and class is checked by the same root rule.

   Then delete the per-route list.
3. **Pause** for stakeholder direction if the author judges that neither option preserves an owner-required capability, for example correcting a wrong revocation where no independent adjudicator exists. The §6.8 owner exception already covers that case.

Do not repair this by adding a fifth route to the list. Do not read any S2 value inside `in_force` or `stands⁻`, because S1's well-founded recursion and §5.6's monotonicity depend on S0/S1 inputs only.

#### Required discriminator (real owners, G3)

The chain is: a Dispatcher-issued `ADJUDICATE(c2)`; then a genuine manual-route return with no lineage attestation, or a direct record by the revision's human author; then Admission, Derivation (S1 `in_force`, S2 `valid`), discharge, readiness of `ACCEPT(s)`, integration and the inspector.

- Run the trajectory for `ACCEPTANCE`, `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE`, `GATE_DECISION ACCEPT` and a revoked subject triple, with `UNKNOWN` and overlapping lineage. The counter-upholding must not restore support, discharge or validity. An `ATTESTED_FRESH`, disjoint counter-adjudicator does restore it.
- Variants (b)-(d): a non-independent dismissal leaves the observation not standing, the triple blocked and the resolution contested.
- Variant (e): an R2 counter-upholding against an R3 human upholding is refused or routed to R3.
- Variant (g): a human author's direct `ACCEPTANCE PASS` on their own revision leaves `valid(s) ≠ T` and `ACCEPT(s)` derived.
- No fixture may seed `in_force`, `res` or a revocation as already resolved. §31.5/§31.6 currently contain none of these cases (N5), so a faithful implementation of the defect passes the whole program (DS-001).

## 2. Non-blocking findings

**N1 — A non-independent adjudication still answers `ADJUDICATE(c)` (restrictive; liveness; `51070e5` N2 partly closed).**
- §10.3's repair (line 1229) exempts only "a passing judgment admitted as non-independent". An `ADJUDICATION` has no passing outcome, so a non-independent `DISMISSED` of a blocking challenge against a passing judgment is the first adjudication bound to `ADJUDICATE(c)` and answers it. The challenge stays open (`gate = F`) and the passing record stays `BLOCKED`. The obligation "is never dispatched again", so on an agent-only adjudication policy only a human's direct record can move it.
- Separately, a non-independent `UPHELD` against an adverse judgment closes `c` in S1 and shows the adverse judgment `REVOKED` (line 683) while it still vetoes (line 768). "Kept as data and resolves nothing" (line 777) overstates this, and the inspector shows a contradiction.
- Option 1 of B1 removes both. Otherwise, extend the §10.3 sentence to adjudications and have views show the S1 status of a non-independent upholding as non-effective.

**N2 — Human independence now reaches every listed kind, but its cure is schema-restricted (restrictive; unlisted narrowing).**
- Step 3 (line 1109) now defines human independence "of any of these kinds" with "unknown authorship fails closed, §6.8". The classification may use "any co-submitted … `NON_AUTHORSHIP_ATTESTATION`".
- §3.4 (line 477), in a closed schema (§3.6), restricts that kind's target to "a disposition record and the claim content", and its producer to the "human disposer".
- So a human `ACCEPTANCE`, `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE` or adjudication on a revision containing any absorbed, legacy, restored or manually merged byte is non-independent, except under the owner exception. With option 1 or 2 of B1 or (g) repaired, such a human acceptance of a human-pushed D1/D2 change, or a dismissal of a blocking challenge on one, can never count.
- The workplan's human rule (§6.6) is stated for dispositions. Extending its unknown-authorship clause to every kind is a narrowing not listed in §0.3.
- Repair without new mechanism: widen the attestation's target grammar to any record step 3 classifies, or state how an intake `ABSORB` establishes authorship. List the narrowing.

**N3 — The new R3 adjudication floor is missing from §3.5's floors (liveness, consistency).** §3.5 (line 524) lists the human floors policy "may raise and never lower", but not "an adjudication of a challenge against an R3 human judgment". Policy may therefore name an R2 holder for such an `ADJUDICATE(c)`. Admission refuses each agent result (`AUTH_ACTOR`), and the obligation is redispatched to agents until its budget runs out. §6.8's "routed to a human mechanically" covers independence, not class. Add the floor to §3.5 and route by class. No mechanism is needed.

**N4 — Two definitional residues (both fail closed; `51070e5` N5 partly closed).**
- (a) §10.2 (line 1214) now names "a machinery `ABSORB` outside any transformation". §18.4 (line 1837) says an `ABSORB` adoption is carried by "an admission request … which makes the delta part of its transformation's identity `A`", and the mechanical `ABSORB` is one such request. Either no such event exists, or a task-less transformation has an undefined enactment. State that a machinery `ABSORB` request's run identity is its entry identity.
- (b) §13.7 says an in-flight replaced part's result "is recorded and routed to revalidation (§8.3 step 7)". Step 7's first check, "the bound obligation exists at the current head", rejects the request instead, and only never-lost records are salvaged. Pick one.

**N5 — Qualification gaps (DS-001).**
- §31.5/§31.6 add the `51070e5` B1 cases. They contain no counter-challenge, observation-dismissal, triple-dismissal, chain-class or support-route case (B1 (a)-(g)), and no `ADJUDICATE(c)` recovery case for N1.
- The closure map line 273 and R13 ("every adjudication that ends an objection") overclaim as written.
- These are design-program omissions. Execution belongs to G3.

**N6 — No floor separates the adjudicator from the parties (stakeholder-level; policy-configurable).**
- Nothing excludes the challenger, the challenged record's author, or the author of a contrary judgment from adjudicating a challenge. The agent route is a fresh `ADJUDICATE` task whose lineage is checked only against the target's authors. A human peer named by policy can raise a challenge against a contrary `NO_PASS` and uphold it.
- The `9e5a763` different-family Review noted that "ordinary contrary peer review is not owner adjudication", and the evidence owner forbids resolution "by majority vote … reviewer seniority, count".
- The reviewed S1 rule leaves adjudicator identity to policy. This is not a blocker, because a sound policy avoids it. Put to the stakeholder whether a system floor should exclude the parties to the disagreement (narrowing; no mechanism).

**N7 — Disclosed costs and trade-offs remain live (not blockers).** These carry `51070e5` N6:
- bounded-only reproduction (partial SD-17 reversal);
- SD-24's narrowing;
- D1/D2 re-gating after exact-identity change, fences and `OVERTAKEN`;
- per-enactment acceptance and gate (R12);
- no support from another pending enactment's frame;
- adverse frame decisions vetoing after abandonment;
- gate-minimum accumulation;
- the cutover race and fenced-cutover half state;
- the context-revert residue.

R13 and this round's repair direction were the author's under stakeholder-record item 19, not stakeholder decisions.

**N8 — Retained historical and empirical limits.** These carry `51070e5` N7:
- Phase B N1 provenance;
- no established reader adequacy, burden reduction, witness availability, template operating characteristic or runtime usefulness at G1;
- unpinnable passing evidence;
- unrecorded execution variation;
- submodule retention, clone tracking and quarantine-path movement;
- VM snapshot/ABA;
- later-`ABSENT` detection.

## 3. Closure audit: workplan §21 and §16.2

The closure map was used only to locate text. Its claims were checked against the Manual.

| Item | Result |
|---|---|
| 1-2 | §§1-2: answer present. Later-`ABSENT` detection is a disclosed limit (§32.2). |
| 3 | §§3.4-3.5, 5.3-5.5, 12.4: **not substantively closed (B1)**. The `ADJUDICATION` kind's independence and class are defined only for one target tier. §3.5's floors omit the new R3 floor (N3). `NON_AUTHORSHIP_ATTESTATION`'s target is too narrow for its new use (N2). |
| 4 | §4, §6.3, §7.3: answer present. §4.4's "covers nothing" is prose not realized in the formula (B1 (g)). |
| 5 | §§5-7: **not substantively closed for the permissive semantics (B1)**. Single-valuedness and stratification hold: `res` is S0, `gate` stays in S1's well-founded recursion, and the veto reads S0/S1 only. |
| 6 | §8 and §§21-23: answer present. The step-3 bullets are the B1 locus, recorded under items 3 and 23. |
| 7 | §§10-11: **not substantively closed (B1)**. Validity and discharge return on a non-independent counter-upholding. N1 is a liveness clarification. |
| 8-22 | Answers present at the sections the closure map names. §29.7 and §30 record items 21-22 (rationale, not adequacy evidence). |
| 23 | §§12-13, 16.3: **not substantively closed (B1)**. Role separation ("May not: judge work … its own execution or lineage authored", line 1329) is unenforced for chained adjudications. |
| 24 | §13: answer present. N4(b) is definitional. |
| 25-26 | §14, §§15-16: answers present. No `HARD` template is claimed qualified. |
| 27 | §29: **partly**. The §29.3 E0 claim for independent acceptance (line 2422) fails on the counter-challenge route (B1). |

**§16.2, both tables:** none found unresolved. Each product invariant and frozen surface has an explicit disposition in §26.4 with a replacement owner. The delta since `51070e5` does not touch §26. This is a document-level transfer check.

## 4. Refinements R1-R13

| # | Assessment |
|---|---|
| R1 | Sound in the bounded design examined: one recorded basis with frozen resolution context; `on⁺ ⇒ on⁻ ⇒ link⁻` by construction (line 921); the class rule leaves no named dimension outside `ext`. Bounded-only stops are the disclosed partial SD-17 reversal (N7). The new adjudication rule does not reach observation-standing dismissals (B1 (b)), which is a defect in the disposition family, not in R1's matching. |
| R2 | Sound: non-trivial SCCs are clamped to `F` before presentation. |
| R3 | Sound fail-closed handling of authenticated corrupt prefixes. |
| R4 | Sound under the declared crash model. The re-gating cost is disclosed. |
| R5 | Sound: single-pass partition, equal/partial-overlap `ABSENT`, no cascade (lines 243-253). |
| R6, R7 | Sound. |
| R8 | Sound for supersession and relief (exact target, gate exception, independent superseder and reliever, agent owner defined by binding, line 1111). |
| R9 | The veto, answered obligations, `REFUSED` and the S0/S1-only veto are sound. Its claim that each stop counts "only if admitted as independent" holds for the first-order stops and fails one level down the challenge chain (B1). |
| R10, R11 | Sound. |
| R12 | A deliberate, surfaced narrowing (SD-25/SD-26). Its costs are N7. |
| R13 | **Unsound as realized, and incomplete as a listing.** Its stated principle (A5/A9 for "every adjudication that ends an objection") is right. Its realization covers only adjudications of challenges against support-tier records (B1). It also omits the human-independence narrowing to every kind (N2). |

## 5. Re-verification of previous findings

The Manual delta from `51070e5` to `29da56e` is ten hunks:
- R9/R13 and the revision log;
- the §3.4 `ADJUDICATION` row;
- §5.3 `gate`;
- §5.5 `stands⁻`, `relieved` and the paragraph at line 777;
- the §6.7 `eff` comment;
- §8.3 step 3 (independence, adjudication class, agent owner);
- §10.2's event list;
- §10.3's answering rule;
- §13.7;
- §31.5/§31.6.

Every earlier closure whose mechanism lies outside those hunks was re-checked for presence of its mechanism in the candidate text. The checked mechanisms include:
- the acting rule (§5.2);
- `rid` and the run rules (§10.2);
- `gterm` (§5.5);
- `on⁺`/`on⁻`/`link⁻` and the four conditions (§6.5-§6.6);
- `eff` (§6.7);
- partition (§1.4);
- step 3 supersession and `AUTH_SUPERSEDES`;
- step 7 `OBLIGATION_REENACTED`;
- the §19.5 carrier rules;
- incarnation fencing;
- `INTEGRITY_HALT`.

None was disturbed. "Closed" excludes the original deductive mechanism, not every conceivable sibling. Records of this reviewer's family were treated as hypotheses.

### Blockers

| Review | Disposition and basis |
|---|---|
| 51070E5 B1 | **Closed for its named route; family open (B1 here).** `stands⁻` conjoins `res(a)` (line 768). A non-independent first-order upholding no longer lifts a veto, and a first-order dismissal against a passing support-tier record needs `res` (line 674). The R3 floor applies to first-order adjudications (line 1110). Agent owner identity is bound to `ADJUDICATE_DISAGREEMENT` (line 1111). Counter-challenge, observation, triple and chain-class routes remain open. |
| 9E5A763-DF B1 | Closed: `relieved` requires `res(y)` (line 773); supersession requires independence (line 1111). |
| 051CCE3 B1 | Closed: exact-target review supersession; per-target relief. |
| 63DDF91 B1 | Closed: the `COMPLETENESS` target includes member revisions (line 460). |
| F03B15E B1-B2 | Closed: same-target supersession with the gate exception; a cutover record is admitted only while its carrier is pending (§19.5). |
| 61CD09B B1-B2 | Closed: gate relief has cross-run reach; human `MODE_TRANSITION` in an `AUTHOR`/`MIGRATE` carrying frame. |
| 362AF9F B1 (A, B) | Closed: gate `REJECT` reaches the same triple in every run; cutover carried by integration. |
| F22B4DC B1 (A-F) | Closed: the enactment is the producing task plus clean rebases; a second integration is refused. |
| B46C250 B1; B46C250-DF B1-A to B1-D | Closed by the one acting rule and event-identified runs. |
| F7419D5 B1; 575DC78 B1 | Closed: `gterm` is the minimum over eligible unsuperseded decisions. |
| 5C55D4B B1-B2 | Closed: bounded reproduction anchors `link⁻`; content-not-offset comparison. |
| 27EF339 B1-B3 | Closed: `link⁻`; innermost byte ownership; frame gate decisions. |
| 0B6C4FA B1-B2 | Closed: `UNBOUNDED` serves no permissive use; no tenure filter. |
| A18B544 B1-B2 | Closed: only a completeness judgment bounds a closure; qualification lives in the minimum. |
| E9E6E9F B1-B2; E2154AC B1; 3540D98 B1-B4 | Closed: one content representation without exception; the full `ext` class; qualified gate in the minimum; equal regions `ABSENT`. |
| 798B2B4 B1-B4; 71CF9B3 B1-B2; 86AB683 B1 | Closed: run-keyed currency as a target condition; display predecessor; symlink traversal recorded; R10 restores S11. |
| 1FFBBF0 B1-B2; 53669A5 B1-B3; D837363 B1-B4 | Closed: free seed and unobserving runner classes in the class rule; acceptance-target duty in every frame; effect-keyed write set. |
| CC005DB B1-B3; C6DA678 B1-B3 | Closed: effective comparison with frozen context; surface-only product-scope veto; item-revision-independent `same`. |
| B595F2C B1-B4 | B1-B3 closed. **B4 partly closed**: no re-dispatch, count or order resolution, but B1 here resolves a disagreement through a non-independent chained adjudication. |
| 6FF4ED1 B1-B4 | Closed. |

### Non-blocking findings

| Review | Status |
|---|---|
| 51070E5 | N1 **mostly closed**: (a) classification fixed at admission (line 1109); (b) human independence defined for every kind, though with the cure gap N2 here; (c) agent owner by binding. N2 **partly closed**: passing judgments no longer answer when non-independent; adjudications still do (N1 here). N3 **partly closed**: the challenge-route, class, author, `DISMISSED` and N2 cases were added; the B1 siblings here are missing (N5). N4 closed: the line-777 separator is fixed; §13.7 says "(for a re-partition, its undischarged obligations)"; the closure map is updated, though it now overclaims for B1. N5 **partly closed**: (a) reworded but conflicting with §18.4; (b) stated but conflicting with step 7 (N4 here). N6 and N7 open as N7-N8 here. |
| 9E5A763-DF | N1 closed for its named composition; N2 closed; N3 closed in text, with the in-flight residue N4(b) here; N4-N5 open as disclosed (N7-N8). |
| 051CCE3 | N1-N5 closed for their named cases; N6-N7 open as disclosed. |
| 63DDF91 | N1 closed as a liveness limit: its only relief, an upheld challenge, is now first-order-independent. N2-N5 closed. N6 open. |
| F03B15E | N1, N2, N4, N5 closed. N3 open as a disclosed half state. N6 open. |
| 61CD09B | N1, N3-N6 closed. N2 closed as disclosure. N7 open. |
| 362AF9F | N1-N6 closed. N7 open. |
| F22B4DC | N1-N5 closed (N4 as disclosed churn). N6 open. |
| B46C250 (same family); B46C250-DF | N1, N3, N4 (and DF N6) closed. Gate-minimum accumulation (N2) and provenance (N5) open as disclosed. |
| F7419D5; 575DC78; 5C55D4B | Closed for their named cases. The trade-offs (F7419D5 N6) are disclosed. |
| 27EF339 | N1 open as a disclosed reproduction cost. N2 open as the stakeholder-level SD-17 reversal. N3-N7 closed. |
| 0B6C4FA | N1-N6 closed. N7 partly closed: old filters gone; B1 family open. |
| A18B544; E9E6E9F; E2154AC | Closed, with disclosures. |
| 3540D98 | N1, N3 closed. N2 (later-`ABSENT`) and N4 (operational limits, defaults) open as disclosed. |
| 798B2B4; 71CF9B3; 86AB683 | Closed except the retained later-`ABSENT` limit and the map's aid status. |
| 1FFBBF0 | N1-N4, N6 closed. N5 open as a disclosed class-change cost. N7 partly closed (B1 family). |
| 53669A5; D837363; CC005DB; C6DA678 | Closed except the noted partials: annotations do not decide adequacy; the R9/R13 accounting overclaims (B1); the same-content amendment veto is deliberately retained; reviewer-quality E3. |
| B595F2C | N6 partly closed: independence enforcement is subject to B1. Others closed. |
| 6FF4ED1 | N1-N11 closed. N12 partly closed: defaults stated; the map is subordinate. |

### Phase B closures and N1-N4

The `552AC01` Y1/Y2 and `EF8445A` X1-X3 closures hold: dual reading coverage, the candidate-own latch, and no ordinary later `PASS` settling interpretive disagreement (lines 971-977). So do:
- the start latch;
- salvage of never-lost records (line 1119);
- refusal of unauthorized `supersedes`;
- SCC and SDG legality;
- quarantine and freezes;
- witness admission before effects;
- the loss boundary;
- counter-challenge polarity (lines 664-668).

**Regression in the assessment family, both directions.**
- Permissive: first-order dispositions carry `res` (line 995). B1 (b) and (d) are disposition-family siblings one level down: a non-independent dismissal restores a stop or uncontests an upholding.
- Restrictive: no stop was withdrawn without cause, and no settled failure resurrects through this delta. `res` only removes effects of records that were non-independent at admission.

**Phase B N2 re-tested on the text.** The case is an alternate tree differing only outside a recorded narrow basis, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld:
- a differing old-content run stays in (2) through `link⁻` with `o' = real(a⁻)`;
- a yielding present-content run keeps (4) false;
- losing completeness only shrinks `on⁺`.

The SCC clamp precedes presentation (§5.6), and authenticated corrupt prefixes halt (§5.7). Closed at design level, unexecuted at G3. Phase B N1 is open (N8). N3 is open as a diagnostic limit. N4 is open as an empirical cost and applicability limit.

## 6. Out-of-matrix trajectories attempted

| Trajectory | Result |
|---|---|
| Author or `UNKNOWN`-lineage counter-upholding against an independent revocation of a passing acceptance, review, gate or triple | **B1** |
| Non-independent dismissal of a blocking challenge against a realization serving (1)/(3) | **B1 (b)** |
| Author dismissal of a blocking challenge against own subject triple | **B1 (c)** |
| Non-independent dismissal of a blocking counter-challenge against an independent upholding (`contested`) | **B1 (d)** |
| R2 counter-upholding against an R3 human upholding (gate, Serious Challenge) | **B1 (e)** |
| Human author's direct non-independent `ACCEPTANCE PASS` against `valid`/`ACC` | **B1 (g)**: literal formula permissive; prose restrictive |
| First-order non-independent upholding against an adverse judgment; first-order dismissal against a passing support-tier record | Held (lines 768, 674) |
| R2 first-order adjudication of a challenge against a human R3 judgment | Held (refused, line 1110); liveness N3 |
| Non-independent superseder, reliever or disposition | Held |
| Non-independent `DISMISSED` answering `ADJUDICATE(c)` | Fails closed; dead-ends the agent route (N1) |
| Peer who holds the contrary judgment acting as adjudicator | Not excluded; policy-level (N6) |
| `res` and the class bullet against stratification | Held: both are S0; `gate` stays inside S1's decreasing-position recursion; `stands⁻`/`vetoed` read S0/S1 only |
| `rid` uniqueness and stability; `D_n[X]` equal to the post-integration state | Held (lines 651, 1214); §10.2's machinery-`ABSORB` wording is N4(a), fail-closed |
| Withdrawn reliance on another pending enactment's frame records | Disclosed narrowing (R12); no owner-required capability shown dropped |
| Completeness polarity, support cycles, corrupt prefixes; structure/`ignore`/analyzer/system-version change with fixed bytes; free attributes, pins and locator sets; unobserving runners; equal, partial and nested regions; mode-only, symlink, gitlink and LFS changes | Held under §§1.4-1.5, 5.6-5.7, 6.3-6.6 |
| Gate minimum across holders, frames, rebases, iterations and runs; gate `REJECT` across runs; cutover ordering | Held (§5.5, §19.5) |
| Slow publisher, fence chains, stale-consistent restore, positive-only attestation | Held within the declared crash and witness models |

This is bounded falsification, not a proof over all ledgers. Discovery in the families that held was stopped where it duplicated earlier records' systematic cases or became implementation-like. In the B1 family it stopped once the shared cause, attachment by target tier, explained every sibling found.

## 7. Minimum architecture and capability transfer

The four primitives, six components and stores each carry a capability a governing invariant requires (§30). The two removals (the publication-attempt log via R4; the dynamic partition check via R5) are sound. B1's recommended option 1 removes mechanism:
- `res` leaves S1;
- the route list and class bullet collapse into one admission rule.

No new record kind, store or latch is needed. Option 2 also removes the per-route list. The Manual's own "minimum" claim is rationale, not independent evidence.

The 1.6.0 supersession preserves the version-bound Level 0 Core, frozen profiles and the single composition root (§26.3-§26.4, §28). The frozen document, `source/` and `dist/` are byte-unchanged from `fad3ee41` (PEM PC-001). Workplan §18's consolidated-control-plane and BEFE678 capability classes still map to current owners. No dropped capability was established.

PEM activates (mature replacement, recurrence). The accepted base was resolved independently of branch position:
- local `main` is `af0455753e20ee54a969c844872e29e270007211`;
- the PEM blob is `1561797125622f355f84eb27319f87e8fa4227d9`, identical at the candidate (no overlay);
- schema validation passed (§10).

```yaml
has:
  - {id: PC-001, disposition: APPLICABLE, reason: frozen Core/profile isolation required by the current versioning owner; preserved}
  - {id: DS-001, disposition: APPLICABLE, reason: §31 lacks every B1 sibling case; green fixtures could coexist with the defect}
  - {id: SP-001, disposition: APPLICABLE, reason: evidence-only; one canonical owner with regenerated projections}
  - {id: SP-002, disposition: APPLICABLE, reason: evidence-only; records never name their containing commit (G3 invariant)}
  - {id: FF-001, disposition: APPLICABLE, reason: evidence-only; validate-before-publish genesis and replacement lineage}
```

Absence of a 7.x episode in PEM proves nothing.

## 8. Qualification-design adequacy

The owner boundaries are right: Derivation and Content Model consumed by Admission and the Interface; the real publisher, fences and witnesses; genuine Dispatcher envelopes and runner custody; real acceptance, gate and inspector paths. Every runtime group is labelled UNEXECUTED, and the diagnostic model is kept apart.

The program is **not adequate for the permissive-resolution family**. §31.6(P) covers first-order adjudications only (line 2618). It has no case for:
- counter-challenge, observation-dismissal, triple-dismissal, chain-class or support-route variants;
- `ADJUDICATE(c)` liveness after a non-independent adjudication.

A faithful implementation of the current text passes the program (N5). These are G1 design-program gaps; their execution is G3. Proposed thresholds and defaults are neither accepted nor calibrated here.

## 9. Doctrine-realization map and O1

This Review read the D3 role entrypoint and the architecture, workflow, evidence and convergence owners at `aaeaf8b6`; it did not re-read every role and specialist entrypoint, because the delta does not touch §29, and it relies on the presence of §29's mapping (a stated limit, not a pass). §29 maps each duty to E0-E3 with an explicit E3 catch-all. No omitted duty was proved.

**One E0 claim fails as assembled.** §29.3's "durable authority mutation needs its acceptance process, independent falsification … **E0**: `ACCEPTANCE` classes and independence" (line 2422) does not hold when a revocation of an acceptance is lifted by a non-independent counter-upholding (B1 (a)), or, on the literal formula, when a non-independent acceptance enters `ACC` (B1 (g)).

O1 (§0.5) states the realized record, readers, routine questions, canonical and projected ownership, drill-down identity, retention, interim exposure, restart continuity and privacy. It marks **no** surface beyond the requested deliverable. This Review accepts no product-scope mark; technical D3 Review does not accept such items.

## 10. What was verified and how; what could not be

Executed against an immutable `git archive` of `29da56e6` at `$TMPDIR/ssds80-manual-review-29da56e/cand`:

| Check | Result and limit |
|---|---|
| Object identities (Manual, map, workplan at candidate, Phase B workplan, frozen 1.6.0, release-state refs) | Match the header |
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` | 4 tests OK; routing, index and lifecycle evidence only |
| `git diff --check 51070e5… 29da56e…` | Clean (exit 0) |
| `git diff --stat fad3ee41… 29da56e…` | 65 files, 20,494 insertions, 1 deletion. Every changed path is under `qualification/ssds80/`, the Manual, or `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. No executable SSDS code |
| `git diff --exit-code fad3ee41… 29da56e… -- source/ dist/ orchestrator/docs/architecture.md` | Exit 0: byte-unchanged |
| PEM `source/project_engineering_memory.py` in the archive, with `PYTHONPATH` set to the archive's `source/` and `GIT_DIR` bound to the repository | "PEM schema 1 valid: 5 families, 0 notices". Structural only |

Not executed:
- the optional diagnostic model, which does not model R9, R13 or the challenge chain;
- any production owner, since none exists at G1;
- G2-G4 programs;
- package build or distribution parity, because no protocol source or generated descendant changed.

Not verified:
- every parser or scope-term input;
- full S1/S2 history enumeration;
- remote homes;
- the authoring conversation;
- each older Review's full trajectory set beyond mechanism presence and the named cases.

These limits supply no pass and do not weaken B1.

## 11. Scientific checks

- **Findings:**
  - B1 and N1-N8 are architecture and evidence-method findings by this AI reviewer (Claude family, author-launched fresh-context sub-agent).
  - No material finding about a realized scientific result.
  - This file is their canonical home, bound to candidate `29da56e` and the identities above.
  - Revisit B1 when a replacement candidate changes which records may end an objection.
- **Realized results:**
  - None produced, run or reviewed.
  - The only executions were document, test-suite and schema checks.
  - The material scope is the architecture that will mediate scientific evidence. Datasets, numerical trajectories and real assessors were unexamined.
- **Variants:**
  - One immutable candidate was judged. Prior candidates supplied failure hypotheses, not a selection campaign.
  - Seven sibling routes (B1 (a)-(g)) were each evaluated against the written predicates by one criterion: does a non-independent or lower-class record end an objection or restore support.
  - No analysis, pipeline, preprocessing, model or parameter variants were run or selected.
- **Tensions:**
  - No accepted project D1/D2 authority was relied on for a consequential judgment, so the tension-search trigger did not fire.
  - No delegates.
- **Gaps:** none beyond §10's verification limits.

## 12. Common-mode note

This reviewer is of the **Claude** family:
- the same family as the Manual's author;
- the same as every Manual reviewer except the `3540d98`, different-family `b46c250` and different-family `9e5a763` reviewers and the Phase B reviewer, who were of the GPT family.

It was engaged as a fresh-context sub-agent **launched by the authoring session**, with only the handoff. Fresh context is not epistemic independence. Shared dependencies:
- the candidate and its framing;
- the inherited workplan framing;
- all prior Review records, including same-family ones whose suggestions led to repairs that later failed (`51070e5`'s "one predicate" direction was adopted here and realized by target tier);
- the protocol corpus;
- the Git/Python toolchain;
- the author-written handoff.

The handoff gave no author conclusions. The verdict rests on the quoted predicates and the explicit trajectory, not on reviewer count or family diversity. A different-family Review would reduce the model-family common mode.

## 13. D4 statement

**D4 is NOT AUTHORIZED.** This NO-PASS is technical evidence for G1 only.

- The Manual, its proposed defaults and its product-scope marks remain proposed.
- Closing B1 needs a replacement immutable candidate and an independent Review. The choice among B1's options, and N6, are for the stakeholder or the author under item 19 as the record states.
- Stakeholder acceptance of the Manual remains separate.
- G2 additionally needs a reviewed shadow D3→D4 workplan and explicit stakeholder authorization.
- G3 production-owner qualification and G4 per-subject cutover remain separate.

No commit or push was made.

# SSDS 8 Architecture Manual — Independent D3 Review, candidate 51070e5

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 51070e5e9346c878cffd9bbc70588fa75ad681fc
    SCOPE: the whole proposed durable Manual: (a) §21/§16.2 closure, (b) fidelity to the reviewed
           contract and the §0.3 refinements, (c) adequacy (out-of-matrix), (d) inheritance and
           capability transfer, (e) qualification design, (f) doctrine-realization map, (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
           blob c21423ddcc02b71a8b4c99ffd77bde7f143747b0 (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md
           blob 1bab4afa1ab7a09cfb51ff59af8f4f7ad6d4ad8f (verified; aid, not authority)
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
    HANDOFF: qualification/ssds80/MANUAL-REVIEW-HANDOFF-SSDS-8.0-51070E5.md
    PRIOR REVIEWS: every Manual NO-PASS record the handoff names (6FF4ED1 through
           9E5A763-DIFFERENT-FAMILY) and the Phase B E23F142 PASS: hypotheses and
           regression inputs only, never authority
    REVIEW METHOD: immutable git-archive snapshot of the candidate; governing owners read with
           git show at the public-source ref; full read of the Manual; diff 9e5a763..51070e5 read;
           family-level falsification of the permissive-resolution family (convergence owner,
           "Review strategy after recurrence"); clause-level closure audit; refinement audit;
           prior-finding re-verification; requested document checks; one bounded predicate
           transcription probe (diagnostic only)
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session,
           given only the handoff file; no authoring conversation
    MUTATION: this record only; no commit, push, source change or PEM update

Line numbers below refer to Manual blob `c21423dd`. Scratch files were kept under `$TMPDIR/ssds80-manual-review-51070e5/`; nothing in this record depends on them remaining available.

## SERIOUS CHALLENGE

**None against accepted authority.** The blocker below is in the proposed Manual's realization of independence and adjudication requirements that are coherent at SSDP 7.2.1, in the reviewed parent contract and in the stakeholder's chosen direction. No accepted project D1/D2 proposition is relied on.

Governing statements used in the consequential reasoning (paths at `aaeaf8b6`):

| Owner and locator | Text applied |
|---|---|
| `source/roles/software-design/SKILL.md` | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| `source/shared/references/architecture-and-design.md`, Formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| Same, Architecture Manual | "Each material current architecture claim has one semantic owner." |
| `source/shared/references/workflow-and-workplans.md`, Review | "Review independence means the reviewing context did not author the candidate and does not inherit author conclusions" |
| Same | "A synthesizer reconciles findings through evidence and owner adjudication; it cannot erase unresolved contradictory material evidence by vote." |
| `source/shared/references/evidence-evolution-and-dependencies.md` | "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified." |
| `source/shared/references/convergence-and-cycle-economy.md` | "Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism" |
| Same, Review strategy after recurrence | "route one family-level problem rather than intentionally returning one cheap sibling per review cycle"; "Review sufficiency is not proof of zero conceivable defects." |
| `source/shared/references/testing-and-validation.md` | "Ask whether evidence could remain green while that owner is materially broken. If yes, it cannot close that owner claim." |

The Manual restates the parent's A5 ("no actor reviews or accepts its own work") and A9 ("reviewer independence is constructed, not requested") in §0.4. The defect below needs neither weakened.

## Verdict

**NO-PASS. One blocking family survives: an upheld challenge ends an adverse judgment's veto with no independence or decision-class check (B1).**

The `9e5a763` B1 repair added one rule, "Permissive resolution needs independence" (§5.5, line 775), and applied it to supersession, `relieved` and `eff`. A fourth route that ends an adverse judgment's standing was left out. That route is the upheld challenge in the second clause of `stands⁻`. Admission's independence classification (§8.3 step 3) never applies to an `ADJUDICATION` of a challenge against an adverse support-tier judgment. So a non-independent adjudicator, an agent with `UNKNOWN` lineage or the judged work's own author, can revoke an independent reviewer's `NO_PASS`, `NONCONFORMANT`, `FAIL` or `REJECTED`. The contrary passing judgment then discharges. For a failing assessment the same record kind on the same route is checked: §6.7 `eff` is `F` for a non-independent upholding. R9, which claims to apply "the reviewed assessment rule" to every adverse judgment kind, therefore dropped that rule's independence condition on its upheld-adjudication stop without listing the change.

This is the third consecutive round in the authority-of-permissive-resolution branch of the judgment-disagreement family (`051cce3` B1 cross-target relief, `9e5a763` B1 non-independent reliever, now the challenge route). It is a non-local recurrence. The assessment-matching (§6.3-§6.6), content-identity, partition, revision-run, acting-rule, gate-minimum, publication and witness families held under the trajectories in §6.

The requested document checks pass (§10). They do not exercise this semantic defect. G1 stays open. Runtime evidence assigned to G2-G4 is not demanded here.

## 1. Blocker

### B1 — An upheld challenge lifts an adverse judgment's veto without the independence or class check every other permissive resolution has

**Earliest owner:** proposed D3 Manual §5.5 (`stands⁻` second clause, line 765-766, and the new paragraph at line 775), with §8.3 step 3 (independence list, line 1107), the `ADJUDICATION` row of §3.4 (line 485) and refinement R9 (line 94). Parent closure obligations implicated: workplan §21 items 3, 5, 7, 23 and 27. This is an architecture defect, not an implementation bug, and not a defect in the reviewed contract: the reviewed assessment rule requires independence on this route (below).

**Family:** judgment disagreement, authority of permissive resolution. Shared cause: the Manual enumerates the routes that end an objection and attaches eligibility to each route separately. Every round has found one route the enumeration missed. Here the missed condition is independence, and for human decisions also the decision class, on the challenge-adjudication route.

#### Exact conflicting text

§5.5, lines 762-766:

```text
stands⁻(j⁻) ⇔ ¬∃ d : d supersedes j⁻, … ∧ acts(d) ∧ ¬superseded(d) ∧ status1(d) = CLEAR ∧ cont(d)
             ∧ ¬∃ a ∈ ADJUDICATION : a.target is a challenge targeting j⁻ ∧ a.outcome = UPHELD
                     ∧ in_force(a) ∧ cont(a) ∧ ¬contested(a)          -- contested as in §6.7
```

There is no independence or class conjunct on `a`.

§5.5, line 775 (new in this candidate):

> Every record that resolves a disagreement permissively (a superseder of an adverse judgment or failing assessment, §8.3 step 3; a reliever in `relieved`; a disposition in §6.7 `eff`) counts only if it was admitted as independent where its kind has an independence requirement

§8.3 step 3, line 1107, says which judgments carry an independence requirement:

> for equivalence and completeness about the request's own change, and for every review, conformance, acceptance and plan-acceptance judgment and every disposition of a failing assessment

An `ADJUDICATION` of a challenge whose target is a `REVIEW`, `CONFORMANCE`, `ACCEPTANCE`, `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS`, `GATE_DECISION` or `PRODUCT_SCOPE_ACCEPTANCE` is in none of these classes. It is never classified non-independent, and the line-775 rule exempts it because "its kind has [no] independence requirement".

For the same record kind on the same route against a failing assessment, §6.7 (lines 993-996) gives `eff(d, a⁻) = F` when "`d` admitted as non-independent (§8.3)", including "otherwise, `d` an `UPHELD` adjudication". The reviewed workplan has the same `eff` line (workplan blob `91bde23`, §6.6, "d admitted as non-independent (§6.8 step 3; S0)").

R9 (line 94) says it "Applies the reviewed assessment rule (a failure counts by existence until disposed of) to every judgment kind with an adverse outcome". The rule as applied drops the reviewed rule's independence condition on the upheld-adjudication stop.

§3.4's `ADJUDICATION` producer is "the qualified actor policy names; R2, or R3 (Serious Challenge, D1/D2 claims)". §3.5's human floor covers only Serious Challenge adjudication. §12.4 describes R2 as "an independent agent or human reviewer (A9)", but no rule makes Admission or Derivation enforce or read that independence for adjudications.

The program then encodes the defect as expected behaviour. §31.5 (line 2609) says an `ACCEPTANCE FAIL`/`PASS` pair leaves `s` invalid "until the owner adjudicates or the `FAIL` is withdrawn by its own author's reassessment or disposed by an upheld challenge". The closure map §5 (line 273) offers the stakeholder the same three routes for R9 without the condition.

#### Concrete trajectory (agent route, `REVIEW`)

This uses an accepted `IMPLEMENT` item `I` on D4 units whose contract requires an independent `REVIEW`. Policy assigns ordinary-challenge adjudication in D4 to a qualified R2 reviewer class, which the §3.5 floors allow. Executions and result slots are clean throughout. Nothing is forged, malformed, stale or seeded.

1. Task `T0` yields `X0`. Independent reviewer `H` (`ATTESTED_FRESH`, disjoint lineage) records `REVIEW NO_PASS` on `X0`, which answers `REVIEW(X0)`.
2. Within budget, the next iteration `T1` yields `X1` with the same changed-unit content, for example on a moved base. `same(H's NO_PASS, ·)` reaches `X1` (§5.5: same item, same candidate content).
3. Independent peer `P` records `z = REVIEW PASS` on `X1`. `vetoed(z)` holds, `REVIEW(X1)` is `REFUSED` and `ADJUDICATE_DISAGREEMENT` is derived. So far the candidate behaves as intended.
4. The plan's principal records a `COORDINATION_DECISION` with outcome `CHALLENGE` (§15.5): an ordinary `CHALLENGE c`, reason `CONFORMANCE_DEFECT`, targeting `H`'s `NO_PASS`. Any role may raise a challenge (§12.3). `ADJUDICATE(c)` is derived for "the qualified actor policy names" (§10.2, §15.3).
5. The `ADJUDICATE(c)` envelope is executed on a manual or Git-envelope route, for instance pasted into the session that drafted `X1`'s content. Its lineage is `UNKNOWN`, and it may in fact overlap the author's. It records `ADJUDICATION UPHELD` on `c`. Step 3 checks actor class, envelope, role and kind. The independence bullet does not apply to this record, so it is admitted with full effect, never "as non-independent".
6. In S1, `upheld(c)` holds and `status1(H's NO_PASS) = REVOKED`. In S2, the second clause of `stands⁻` is satisfied (`in_force(a) ∧ cont(a) ∧ ¬contested(a)`), so `stands⁻ = F` and `vetoed(z) = F`.
7. `z` is current and independent, so `discharged(REVIEW(X1))` holds (§10.4) and `REFUSED` no longer applies. `ADJUDICATE_DISAGREEMENT` is no longer triggered. `X1` integrates under §11.5. An independent objection has been removed by a record that no independence rule examined.

Steps 5-6 are the 9e5a763 B1 laundering pattern on a route the repair did not cover. One independent pass plus one non-independent resolution of the contrary independent objection integrates the work.

#### Bounded sibling list (one family-level problem)

| Variant | Candidate result | Required result |
|---|---|---|
| The trajectory above for `CONFORMANCE NONCONFORMANT`, `ACCEPTANCE FAIL` (agent R2 acceptance), `EQUIVALENCE NOT_EQUIVALENT` and `COMPLETENESS INCOMPLETE` | veto ends | no effect from a non-independent adjudicator |
| `PLAN_ACCEPTANCE REJECTED` after the rejected set was amended. §8.3 step 3 makes "an upheld challenge" the **only** relief there. The plan's principal, who authored the contract, raises the challenge, and a non-independent adjudicator upholds it | rejection lifted; a peer's `ACCEPTED` makes the items issuable | plan acceptance stays "never by the contract's author lineage" (§12.3) |
| Human-author variant (A5): Alice authors a D1 revision through an `AUTHOR` task she executes. `H` records `ACCEPTANCE FAIL` and Bob `ACCEPTANCE PASS`. Alice, whom policy names for R3 D1 adjudication, challenges `H`'s `FAIL` and upholds it herself | veto ends; no common-mode record; inspector silent | the §6.8 owner exception's conditions at least: independence, or the author as owner only where policy names no other qualified human, with the common-mode dependency recorded and shown |
| Decision-class variant: an R2 agent upholds an ordinary challenge against a human's `GATE_DECISION REJECT` on a D3/D4 gate, or against the stakeholder's `PRODUCT_SCOPE_ACCEPTANCE REJECTED` | a disagreement between two humans' R3 decisions is resolved by an agent | adjudication class not lower than the challenged decision's (§12.4: "An agent may move a decision up … never down") |
| `DISMISSED` adjudication of a **blocking challenge** against a passing judgment, by a non-independent adjudicator | the block lifts and the pass discharges | same eligibility question. This shape comes from the reviewed contract's S1 adjudicator rule ("qualified actors per policy"), so the repair should decide it at family level and list any narrowing in §0.3 |
| Owner identity for agent records: "the owner" in `relieved` and supersession is "the actor policy names" (§8.3 step 3). Agent identities are per task (`agent:<task id>/<attempt>`, §25.1), so for agents policy can name only a qualification. Under that reading a `REVIEW(X1)` peer holding the owner qualification relieves itself (the `b595f2c` B4 shape) | ambiguous; one literal reading is permissive | define an agent's owner record by its binding to the `ADJUDICATE_DISAGREEMENT` obligation of that adverse judgment |
| `UPHELD` adjudication disposing of a failing assessment, non-independent | `eff = F` (held) | keep |
| Non-independent superseder or reliever | rejected, or no relief (held) | keep |

A bounded transcription of the written stop rules (10 route × objection × independence rows) found exactly one non-independent permissive resolution: an upheld adjudication against an adverse judgment. It is a diagnostic of the written predicates, not production evidence. The deductive trajectory warrants B1.

#### Convergence assessment and options

The trigger in the convergence owner applies. The same mechanism (which records may end an objection) has been patched in four consecutive rounds, each by adding or qualifying one route. Per Phase C handoff §5 the options are:

1. **Bounded simplification (recommended; narrows, adds no record kind, latch or store).** State **one** S0 eligibility predicate and use it for every record whose effect ends an objection to a judgment. That covers a superseder, a reliever, a disposition, and an `ADJUDICATION` whose outcome ends an adverse judgment's standing or lifts a blocking challenge from a passing judgment. Such a record counts only if, at admission, it met the independence requirement of the judged kind against the author of the judged target, under the same owner exception and common-mode record as §6.8, and only if its decision class is not lower than the challenged record's. Then:
   - add that `ADJUDICATION` case to step 3's independence list;
   - conjoin the classification in `stands⁻`;
   - replace the per-route enumerations in §5.5 line 775, §8.3 step 3 and R8/R9 with a pointer to the one predicate;
   - define the owner of an agent record by its binding.

   This adds one list entry and one conjunct. It removes the route lists.
2. **Subtractive alternative.** Delete the upheld-challenge clause from `stands⁻`. A revoked adverse judgment then still vetoes until its author's reassessment or the owner's adjudication, both of which are already independence-checked. This removes mechanism and costs liveness only where the owner is unavailable. It does not address the `DISMISSED` sibling, whose source is the reviewed contract.
3. **Pause** for stakeholder direction if neither preserves an owner-required capability in the author's assessment.

No new stakeholder decision is needed merely to enforce the independence floor already binding under A5/A9. A narrowing of the reviewed S1 adjudicator rule for the `DISMISSED` sibling is a contract change and must be surfaced in §0.3.

Do not repair this by reading `current(a)` or any S2 value inside `stands⁻`. The veto's S0/S1 constancy, and with it §5.6's monotonicity argument, depends on `stands⁻` reading only S0/S1 facts.

#### Required discriminator (real owners, G3)

The chain is a Dispatcher-issued `ADJUDICATE(c)`, then a genuine manual or Git-envelope return with no lineage attestation, then Admission, Derivation, discharge, the integration decision and the inspector.

- Reproduce the trajectory for `REVIEW`, `CONFORMANCE`, `ACCEPTANCE`, `PLAN_ACCEPTANCE`, `EQUIVALENCE` and `COMPLETENESS`, with `UNKNOWN` and overlapping lineage. The upholding must be preserved as data. It must not end the veto, discharge the obligation or permit integration, and `ADJUDICATE_DISAGREEMENT` must remain derived.
- Repeat with an `ATTESTED_FRESH`, disjoint adjudicator. The veto then ends.
- For the human-author variant, the upholding counts only under the owner exception, with the common-mode dependency recorded and shown.
- For the class variant, an R2 adjudication of a challenge against a human gate or product-scope rejection is refused or routed to R3.
- For whichever `DISMISSED` rule is chosen, test it in both directions.
- No fixture may seed `stands⁻`, the classification or the adjudication as already resolved. §31.5's current expected outcome "disposed by an upheld challenge" must be rewritten. As written, a faithful implementation of the defect passes it (DS-001).

## 2. Non-blocking findings

**N1 — The independence classification the new rule consumes is not fully defined (restrictive or precision; one reading permissive, listed in B1).**
- (a) Timing of `LINEAGE_ATTESTATION`. §12.2 says a manual-route judgment is `UNKNOWN` "unless an authenticated human attests" (`HUMAN_ATTESTED_FRESH`). The attestation is a separate support-tier record targeting a judgment. Nothing says whether it must be co-submitted, or whether a later attestation changes the "admitted classification, an S0 fact" (line 775). Nothing says whether a later revocation of the attestation withdraws independence; the judgment's own challenge route still exists.
- (b) Independence of a human's non-disposition judgment. Step 3 defines it only "for a human disposition". A human reviewer's `REVIEW`/`CONFORMANCE`, and so a human author's or owner's relief, has no stated lineage class.
- (c) Owner identity for agent records (B1 sibling).
- Repair: state that the classification is fixed at admission from the binding and any co-submitted attestation; define human independence for every kind; define owner identity by binding. No mechanism needed.

**N2 — A non-independent judgment answers its obligation, so the fail-closed route has a dead end (restrictive; liveness).** §10.3 counts the first acting judgment bound to an obligation as its answer, whatever its independence. §8.3 step 7 then refuses any later passing judgment bound to it (`OBLIGATION_ANSWERED`). Two consequences follow:
- A non-independent owner pass `y` answers `ADJUDICATE_DISAGREEMENT`, so §31.6(P)'s "an independently attested owner pass of `X1` then relieves it" is reachable only by an authenticated human's direct record, or by a later attestation if N1(a) allows one.
- A non-independent `REVIEW PASS` on `X` answers `REVIEW(X)` for good (§31.5 "Fail-closed independence"), so only a new iteration recovers.

Both fail closed. Repair, subtractive: a judgment admitted as non-independent does not answer an obligation whose discharge requires independence, in the way §10.3 already treats refused passing judgments.

**N3 — Qualification gaps (DS-001).**
- §31.5 (line 2609) expects "disposed by an upheld challenge" with no independence or class condition. That makes B1 the expected behaviour.
- §31.6(P) covers non-independent relief but not the challenge route, the `PLAN_ACCEPTANCE` only-challenge relief, the human-author variant, the class variant or the N2 recovery.
- No §31 case covers the §13.7 example: a reopened part obligation of a superseded `PARTITION` being dispatched while the replaced part stays unrequired.

These are design-program omissions. Their execution belongs to G3.

**N4 — Editorial residue in the newest text.**
- Line 775: "Admission enforces this for supersession, `relieved` and `eff` read the admitted classification" lacks a separator. Read literally, it says Admission enforces the rule for `relieved`.
- §13.7's first sentence still says the parts' obligation sets "partition the item's obligations exactly", while a re-partition partitions only the undischarged ones. The second sentence and the new example settle it.
- The closure map §5 R9 bullet (line 273) offers "a challenge against it is upheld" without its independence or class condition.
- R9's "Applies the reviewed assessment rule" overclaims (B1).

**N5 — Two small definitional residues (fail closed).**
- (a) §10.2 lists "an adopting disposition" among events whose run identity is "the admitting entry's identity". §18.4 makes every adoption part of a transformation's `A`, whose integration's run is its enactment, and the frame rule says the same. Read literally, the two rules could disagree for an adopting records-only request `X = (B, B, A)`. The frame rule governs it, and a mismatch would only make a prospective acceptance non-current, which fails closed. Remove the entry, or state which adoption it means: a machinery `ABSORB` with no task.
- (b) §13.7 does not say what happens to a replaced pending part `b` whose task or enactment is in flight when `P2` is admitted: whether its bound obligation still "exists" for step 7 legality. Either reading is safe under revalidation; state one.

**N6 — Disclosed costs and stakeholder-level trade-offs remain live (not blockers).** These carry `9e5a763` N4, `051cce3` N6/N7 and `63ddf91` N6:
- bounded-only mechanical reproduction partly reverses SD-17;
- SD-24's narrowing;
- exact identity, and fences, cause D1/D2 re-gating;
- per-enactment acceptance and gate (SD-26, R12);
- no support from another pending enactment's frame records;
- adverse frame decisions keep vetoing after abandonment;
- gate-minimum accumulation;
- the cutover race and the fenced-cutover half state, with no re-check of conditions 1-6 on re-application;
- the context-revert residue (§32.2, `051cce3` N6).

Repair directions from candidate 13 onward were the author's under stakeholder-record item 19, not stakeholder decisions. That includes this candidate's line-775 rule. Acceptance and defaults belong to the stakeholder.

**N7 — Retained historical and empirical limits.**
- Phase B N1: the 2026-10-12 adoption instruction is paraphrase only.
- No scientific-reader adequacy, burden reduction, witness availability, template operating characteristic or runtime usefulness is established at G1.
- Unpinnable passing evidence, unrecorded execution variation, submodule retention, clone tracking, quarantine-path movement, VM snapshot/ABA, all-information-lost and later-`ABSENT` detection remain the bounded, disclosed contract.

## 3. Closure audit: workplan §21 and §16.2

The closure map was used only to locate text. Each §21 item was matched against the Manual sections read in full. "Answer present" means a substantive D3 decision; runtime qualification stays unexecuted.

| Item | Result |
|---|---|
| 1 | §§1.1-1.11: answer present. Later-`ABSENT` detection is a disclosed limit (§32.2). |
| 2 | §§2.1-2.6: answer present. |
| 3 | §§3.2-3.6, 5.4-5.5, 12.4: **not substantively closed (B1)**. The `ADJUDICATION` kind's independence and class requirement against adverse judgments is undefined, and the line-775 rule is inconsistent with `stands⁻`. |
| 4 | §§4.1-4.6, 6.3, 7.3: answer present. |
| 5 | §§5-7: **not substantively closed for the derivation's permissive semantics (B1)**. S0/S1/S2 single-valuedness and stratification hold (§6 below). |
| 6 | §8 and §§21-23: answer present. Step 3's independence list is the B1 locus, recorded under items 3 and 23. |
| 7 | §§10-11: **not substantively closed (B1)**. Discharge follows the unvetoed pass. N2 is a bounded liveness clarification; N5(a) is definitional. |
| 8-22 | Answers present at §§11, 9, 16, 17, 18, 19, 20-24, 25.1-25.2, 25.3, 26, 27, 28, 29.7 and 30 respectively. §29.7 records the item-21 landing decisions and §30 the item-22 reassessment (rationale, not adequacy evidence). |
| 23 | §§12-13, 16.3: **not substantively closed (B1)**. A non-independent adjudication bypasses role separation and plan-acceptance independence. |
| 24 | §13: answer present. N3/N5(b) concern the re-partition example's qualification and in-flight parts. |
| 25-26 | §14 and §§15-16: answers present. No `HARD` template is claimed qualified now. |
| 27 | §29: **partly**. The E0 independence claims in §29.3 ("`ACCEPTANCE` classes and independence (§3.5, §8.3)") do not hold for the challenge route (B1). The duty-to-mechanism mapping is otherwise present. |

**§16.2, both tables:** none found unresolved. Each of the 26 product invariants and each frozen surface (§§3-22, including the §§4/14 surfaces the parent table omitted) has an explicit preserved, replaced, retired, adopted, mapped or declined disposition in §26.4 with its replacement owner (§26.1-§26.3, §21, §23.8, §19.7, §28). This is a document-level transfer check, not proof that future components preserve the capabilities.

## 4. Refinements R1-R12

| # | Assessment |
|---|---|
| R1 | Sound in the bounded design examined:<br>• one recorded basis with frozen resolution context;<br>• `on⁺ ⇒ on⁻ ⇒ link⁻` by construction;<br>• the class rule leaves no named dimension outside `ext`.<br>Bounded-only stops are a disclosed narrowing of SD-17 (N6). |
| R2 | Sound: non-trivial SCCs are clamped to `F` before presentation. |
| R3 | Sound fail-closed handling of authenticated corrupt prefixes; an unreadable newer schema is not corruption. |
| R4 | Sound under the declared crash model. VM snapshot/ABA and the re-gating cost are disclosed. |
| R5 | Sound: single-pass partition with innermost precedence, equal/partial-overlap `ABSENT`, no cascade. |
| R6 | Sound: subject-declared scope expression; refinement preserves identity and tenure. |
| R7 | Sound: evidential `CHALLENGES` is excluded from legality and prerequisites. |
| R8 | Sound for supersession and relief as now stated (exact target, gate exception, independent reliever). It is incomplete as a statement of who may end an objection: the challenge route is unconstrained (B1), and the owner identity for agent records is underdefined (B1 sibling). |
| R9 | **Unsound as assembled, and a change needing different treatment.** It claims to apply the reviewed assessment rule, but its upheld-challenge stop omits that rule's independence condition (reviewed `eff`, first line) and has no class floor. The change is unsurfaced (B1). The veto, answered obligations, the `REFUSED` value and the S0/S1-only veto remain sound. |
| R10 | Sound stated scope: native D1/D2 run-keyed currency; non-D1/D2 early cutoff; no cross-tenure revival. |
| R11 | Sound: minimum over eligible decisions; `INADEQUATE` refused; qualification lifts only by its own decision's supersession. |
| R12 | A deliberate narrowing, correctly surfaced and stakeholder-directed (SD-25/SD-26). Its listed costs are N6. |

## 5. Re-verification of previous findings

The Manual delta from `9e5a763` to `51070e5` consists of:
- the line-775 rule, the `relieved` independence conjunct and the §8.3 step 3 wording (relief family);
- R8/R9 wording;
- the §13.7 re-partition example;
- one §31.6(P) case;
- one closure-map line.

Every earlier closure whose mechanism lies outside those clauses was re-checked for presence of its mechanism in the text read in full here; none was disturbed by the delta. "Closed" excludes the original deductive mechanism, not every conceivable sibling. Earlier records share this reviewer's model family (except the GPT-family records) and were treated as hypotheses.

### Blockers

| Review | Disposition and basis |
|---|---|
| 9E5A763-DF B1 | **Closed for its named routes; family open.** `relieved` now requires "admitted as independent" (line 770), and supersession requires it at step 3. The non-independent owner or author pass no longer relieves. The challenge route is B1 here. |
| 051CCE3 B1 | Closed: review supersession is exact-target only; relief is per exact target; a revert to `X1` does not inherit `X2`'s relief. |
| 63DDF91 B1 | Closed: the `COMPLETENESS` target includes member revisions (§3.4); supersession across revisions is refused. |
| F03B15E B1-B2 | B1 closed: "the same target" holds for every kind, with only the gate exception. B2 closed: a cutover record is admitted only while its carrier of the stated kind is pending (§19.5). |
| 61CD09B B1-B2 | B1 closed: gate relief has cross-run reach; review relief is exact-target and now independent. B2 closed: a human `MODE_TRANSITION` in an `AUTHOR`/`MIGRATE` carrying frame, conditions checked at integration. |
| 362AF9F B1 (A, B) | A closed: a gate `REJECT` reaches the same triple in every run. B closed: the cutover is carried by an integration of a ledger-known transformation. |
| F22B4DC B1 (A-F) | Closed: the enactment is the producing task plus clean rebases (§5.2); a second integration is refused (step 7); sibling, replaced and abandoned frames do not act. |
| B46C250 B1 (same family); B46C250-DF B1-A to B1-D | Closed by the one acting rule (§5.2) and event-identified runs (§10.2); `D_n[X]` reads exactly the post-integration acting set. |
| F7419D5 B1; 575DC78 B1 | Closed: `gterm` is the minimum over eligible unsuperseded decisions in one state. |
| 5C55D4B B1-B2 | Closed: a bounded reproduction is required; region comparison is by content, not offset. |
| 27EF339 B1-B3 | Closed: `link⁻`; innermost byte ownership with modes to every resolving unit; frame gate decisions declare their frame. |
| 0B6C4FA B1-B2 | Closed: `UNBOUNDED` serves no permissive use and counts as admitted content; no isolated tenure filter. |
| A18B544 B1-B2 | Closed: only a completeness judgment bounds a closure, with a tracked-path fallback; qualification lives in the gate minimum. |
| E9E6E9F B1-B2 | Closed: one representation with no fallback (LFS as external, gitlink read entries); the minimum keeps qualification. |
| E2154AC B1 | Closed: the single representation is materialized by every runner. |
| 3540D98 B1-B4 | Closed: exact type/mode/blob identity with classified anchor removal; full locator/pin set in `ext`; qualified gate in the minimum; equal regions `ABSENT` in one pass. |
| 798B2B4 B1-B4 | Closed: unintegrated acceptances define no admitted run; run-keyed consumers; display predecessor; symlink traversal recorded. |
| 71CF9B3 B1-B2 | Closed: one event class per run; `tgt` read by validity, not only readiness; R10 restores S11. |
| 86AB683 B1 | Closed: the run key replaces predecessor equality. |
| 1FFBBF0 B1-B2 | Closed: a free seed is an attribute; unobserving classes are unpinnable; the acceptance-target duty applies in every frame. |
| 53669A5 B1-B3 | Closed: the class rule over free attributes; acceptance and gate both need counting assessments; the intake target rule is about targets, not timing. |
| D837363 B1-B4 | Closed: free environment in `ext`; capture-time context with a pure resolver; acceptance-target duty; effect-keyed write set at the current head. |
| CC005DB B1-B3 | Closed: effective kind/content/region comparison; frozen system version; surface-only product-scope veto. |
| C6DA678 B1-B3 | B1 closed (external differences adverse-only). B2 closed for the item-amendment escape (`same` ignores item revision). B3 closed (effect-keyed write set). |
| B595F2C B1-B4 | B1-B3 closed (term-level recording; ref locality; `DOCUMENT` cannot write D1-D3). **B4 partly closed**: no re-dispatch, count or order resolution, but B1 here resolves a review disagreement through a non-independent adjudication. |
| 6FF4ED1 B1-B4 | Closed: recorded terms and `on⁺` conjunction; byte-identical prose tightening; pinned analyzers; `AUTHOR`/`DOCUMENT` items with duties. |

### Non-blocking findings

| Review | Status |
|---|---|
| 9E5A763-DF | N1 **partly closed**: §31.6(P) adds the non-independent-relief case, but not the challenge route (N3). N2 closed: relief prose names supersession or relief (§5.5, §8.3), and R9 distinguishes item-revision amendments. N3 closed in text: the §13.7 example states required, ready and replaced parts; qualification of the example is still missing (N3 here); in-flight replaced part is N5(b). N4 open: disclosed trade-offs (N6). N5 open: retained limits (N7). |
| 051CCE3 | N1 closed: row targets exact (objective revision; frame "is where it resolves, not part of its target"); `EQUIVALENCE` named in step 3; the `vetoed`-keyed trigger fails closed. N2 closed: lint against undischarged obligations; superseded part obligations stay derived; first-sentence residue in N4. N3 closed: a refused second carrier has no frame (§7.4, §19.5). N4 closed except the closure-map "never crosses content" phrase, now bounded by its stated exception. N5 closed for revert, objective, refused-carrier and keep-discharged cases; the reopened-part case is still missing (N3). N6 open: disclosed residue (§32.2). N7 open: trade-offs. |
| 63DDF91 | N1 closed as a stated liveness limit. Its only remaining relief, "an upheld challenge", is now a B1 sibling. N2 closed (§13.7). N3 closed or disclosed (§7.4, §19.5). N4 closed. N5 partly closed (as 051CCE3 N5). N6 open: trade-offs. |
| F03B15E | N1 closed: "bound to it there". N2 closed: the `PARTITION` record identity is in the part obligation id. N3 open as a disclosed half state (§19.5, §32.2). N4 closed. N5 closed for its named cases. N6 open. |
| 61CD09B | N1 closed: the gate core lists every reaching adverse judgment. N2 closed as disclosure (fence/overtaken re-gating). N3 closed. N4 closed: partition identity specified. N5 closed: an identical resubmission joins the first submitter. N6 closed for its program; the challenge-route case is missing (N3 here). N7 open. |
| 362AF9F | N1 closed: re-application is a new enactment (R12). N2 closed: part obligation identity. N3 closed: first-submitter enactment. N4 closed: the rebase tuple is checked at step 2. N5 closed. N6 closed for its program. N7 open. |
| F22B4DC | N1 closed: the observation exception to acting is explicit. N2 closed: R12. N3 closed: `REJECT` behaviour disclosed. N4 closed as disclosed drift churn (§32.3). N5 closed for its program. N6 open. |
| B46C250 (same family) | N1, N3, N4 closed. N2 open: gate-minimum accumulation, a disclosed reopen trigger. N5 open. |
| B46C250-DF | N1, N3, N4 and N6 closed. N2 and N5 open as disclosed costs or provenance. |
| F7419D5 | N1-N5 closed. N6 open as disclosed trade-offs. |
| 575DC78 | N1-N7 closed; N3 as a disclosed line-granular cost. |
| 5C55D4B | N1-N7 closed for their named cases; runtime unexecuted. |
| 27EF339 | N1 open: disclosed reproduction cost. N2 open: stakeholder-level partial SD-17 reversal. N3-N7 closed. |
| 0B6C4FA | N1 closed as provenance (item 19). N2 closed for second-holder qualification; record-challenge identity is a stated limit. N3 closed: a qualified-actor owner route; agent-owner identity is B1's sibling. N4-N6 closed. N7 partly closed: old filters gone, current B1 open. |
| A18B544 | N1-N6 closed; N4/N5 as disclosures. |
| E9E6E9F | N1-N5 closed. |
| E2154AC | N1-N3 closed. N4/N5 closed as disclosed precision or narrowing costs. |
| 3540D98 | N1 closed. N2 open: later-`ABSENT` limit (§32.2). N3 closed. N4 open: operational and historical limits, proposed defaults. |
| 798B2B4 | N1-N4, N6 closed. N5 partly closed: the later-absence limit is retained. N7 closed for its prescribed cases. N8 partly closed: the map remains an aid. |
| 71CF9B3 | N1-N6 closed. N7 partly closed: later-`ABSENT` is disclosed. N8 partly closed: the map is an aid. |
| 86AB683 | N1-N3, N5, N6 closed. N4 partly closed: later-`ABSENT`. N7 partly closed: scientific/operational limits retained. |
| 1FFBBF0 | N1-N4, N6 closed. N5 open: disclosed class-change cost (§17.5). N7 partly closed: the old named paths are corrected, current B1 is open. |
| 53669A5 | N1-N8 closed. N9 partly closed: annotations do not decide adequacy. |
| D837363 | N1-N5, N7 closed. N6 partly closed: accounting present, current R9 overclaim (N4). N8 partly closed. |
| CC005DB | N1-N5, N7 closed. N6 partly closed: the same-content amendment veto is deliberately retained. N8 partly closed: the aid cannot establish B1 closure. |
| C6DA678 | N1-N9 and N11 closed. N10 and N12 partly closed: reviewer-quality E3, current accounting overclaim (N4). |
| B595F2C | N1-N5, N7, N8 closed. N6 partly closed: test-integrity minima present, independence enforcement subject to B1. |
| 6FF4ED1 | N1-N11 closed. N12 partly closed: defaults and residuals stated, the map remains subordinate. |

### Phase B closures and N1-N4

The `552AC01` Y1/Y2 and `EF8445A` X1-X3 closures still hold: dual reading coverage, the class rule's candidate-own latch, and no ordinary later `PASS` settling interpretive disagreement (§6.6-§6.8). So do the earlier family closures:
- the start latch and monotone `home`;
- salvage of never-lost records;
- refusal of unauthorized `supersedes`;
- SCC and SDG legality;
- quarantine and freezes;
- witness admission before effects;
- the loss boundary;
- counter-challenge polarity;
- before-image, output and context roles;
- incarnation fencing.

**Regression for the assessment-disagreement family:** its dispositions still carry independence (§6.7 first line; §6.8), so B1 is outside the assessment family proper. The defect lies in R9's extension of that family to other judgment kinds.

**Phase B N2, both directions:** re-tested on the text. An alternate tree differing only outside a recorded narrow basis, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld:
- a differing old-content run stays in (2) through `link⁻` with `o' = real(a⁻)`;
- a yielding present-content run keeps (4) false;
- losing `c` only shrinks `on⁺`, so (1) and (3).

The SCC clamp precedes presentation (§5.6), and authenticated corrupt prefixes halt (§5.7). Closed at design level, unexecuted at G3.

Phase B N1 open (N7). N3 open: diagnostic and reader-quality limit. N4 open: empirical cost and applicability.

## 6. Out-of-matrix trajectories attempted

| Trajectory | Result |
|---|---|
| Non-independent upheld adjudication of a challenge against an adverse judgment, with an independent contrary pass | **B1**, across all adverse-capable kinds |
| `PLAN_ACCEPTANCE` rejection relieved after amendment | **B1 sibling**: the only relief is the unconstrained challenge route |
| R2 adjudication of a challenge against a human R3 rejection | **B1 sibling** (class) |
| Author self-adjudication of a challenge against `FAIL` of own revision | **B1 sibling** (A5; no common-mode record) |
| Non-independent owner or author relief, or supersession (9e5a763 B1) | Held: `relieved` requires the classification; step 3 rejects the superseder |
| Non-independent relief answering `ADJUDICATE_DISAGREEMENT` | Fails closed but dead-ends agent re-adjudication (N2) |
| Same agent actor reassessing in a later task | Held: agent identity is per task (§25.1), so no "own author" route for agents |
| `rid` uniqueness and stability | Held: an integration's ι is the producing task's 128-bit identity, issued before dispatch; other events use the unique entry identity. Clean rebases share ι; re-dispatch, partition parts, overtaken or fenced re-application and re-cutover get new tasks. Frame and post-integration ι are equal. The adopting-request wording is N5(a), fail-closed |
| `D_n[X]` equal to the post-integration state | Held: the acting set in the frame is exactly the admitted, integrated-enactment and own-enactment records; adverse records act everywhere; observations are placed by matching |
| Withdrawn reliance on another pending enactment's frame records | Disclosed narrowing (R12, SD-26); no owner-required capability shown dropped beyond the listed cost |
| Completeness polarity (Phase B N2), support cycles, corrupt prefixes | Held (§5 above) |
| Structure, `ignore`, analyzer or system-version change with fixed bytes; free seed, backend, precision, environment, pin and locator-set differences; unobserving runner classes | Held: the guard freezes `on⁻`; `ext` compares the complete class; unpinnable reads fail closed. Unrecorded attributes remain a disclosed residual |
| Equal, partial and nested dynamic regions; residual subtraction; mode-only, empty-file, symlink, gitlink and LFS changes; write set against the current head | Held under §1.2, §1.4 and §1.5 |
| Gate minimum with qualified and unqualified holders across frames, rebases, iterations and runs; abandoned-frame supersession; gate `REJECT` across runs | Held (§5.5 `gterm`, §5.2 acting) |
| Cutover carrier ordering, second carrier, fenced cutover | Held or disclosed (§19.5) |
| Slow publisher, shared host key, restored operator state, fence chains, stale-consistent restore, positive-only attestation | Held within the declared crash and witness models |
| Re-partition after an integrated part, then drift | Held in text (§13.7 example). In-flight replaced part is N5(b) |

This is bounded falsification, not a proof over all ledgers or parsers. Further discovery in the families that held was stopped where it became implementation-like or duplicated the earlier records' systematic cases.

## 7. Minimum architecture and capability transfer

The primitives (unit, relation, record, basis), the six components and the stores each carry a capability a governing invariant requires (§30). The two removals (the publication-attempt log via R4; the dynamic partition check via R5) are sound. B1's recommended repair needs no new primitive, store, record kind or latch. It replaces route enumerations with one predicate.

The Manual's own "minimum" claim is rationale, not independent evidence.

The 1.6.0 supersession preserves the version-bound Level 0 Core, frozen profiles and single composition root (§26.3-§26.4, §28). The frozen document, `source/` and `dist/` are byte-unchanged from `fad3ee41` (PEM PC-001, current versioning owner).

Workplan §18's consolidated-control-plane and BEFE678 capability classes still map to current owners:
- semantic and control separation;
- typed relations and completeness;
- versioned replay;
- no prose-driven transitions;
- accepted modular plans;
- atomic admission;
- context and impact;
- safe parallelism;
- static intake;
- progressive migration;
- confidentiality;
- immutable rollback.

No additional dropped capability was established.

PEM activates (mature replacement, recurrence). The accepted base was resolved independently of branch position: local `main` = `af0455753e20ee54a969c844872e29e270007211`, PEM blob `1561797125622f355f84eb27319f87e8fa4227d9`, identical at the candidate (no overlay). Schema validation passed (§10).

HAS:

```yaml
has:
  - {id: PC-001, disposition: APPLICABLE, reason: frozen Core/profile isolation required by the current versioning owner; preserved}
  - {id: DS-001, disposition: APPLICABLE, reason: §31.5 encodes B1 as expected; green fixtures could coexist with the defect}
  - {id: SP-001, disposition: APPLICABLE, reason: evidence-only; one canonical owner with regenerated projections}
  - {id: SP-002, disposition: APPLICABLE, reason: evidence-only; records never name their containing commit (G3 invariant)}
  - {id: FF-001, disposition: APPLICABLE, reason: evidence-only; validate-before-publish genesis and replacement lineage}
```

Absence of a 7.x episode in PEM proves nothing.

## 8. Qualification-design adequacy

The owner boundaries are right:
- Derivation and Content Model consumed by Admission and the Interface;
- the real publisher, fences and witnesses;
- genuine Dispatcher envelopes and runner custody;
- real acceptance, gate and inspector paths.

Every runtime group is labelled UNEXECUTED. The diagnostic model is kept apart from qualification.

The program is **not adequate for the permissive-resolution family**. Its R9 case (§31.5) expects the defect, and §31.6(P) does not test the challenge route, the `PLAN_ACCEPTANCE` only-challenge relief, the human-author or class variants, or the N2 recovery (N3). A faithful implementation of the current text passes those cases. These are G1 design-program gaps; their execution is G3.

Proposed thresholds and defaults (§14.7, §5.9, §13.7, §22.3, §23.3, §24.1, §19.5) are neither accepted nor calibrated here.

## 9. Doctrine-realization map and O1

The four role and three specialist entrypoints were read at `aaeaf8b6` with the scientific-checks fragment. §29 maps each duty to E0/E1/E2/E3 with an explicit E3 catch-all, and §16.3 carries the full domain and specialist cores. No omitted duty was proved.

**One E0 claim fails as assembled.** §29.3 says "durable authority mutation needs its acceptance process, independent falsification … **E0**: `ACCEPTANCE` classes and independence (§3.5, §8.3)", and the B1 challenge route lets a non-independent or author adjudication decide an acceptance disagreement. Other E0/E1/E2/E3 distinctions are appropriately bounded. The catch-all cannot downgrade an explicit E0 obligation.

O1 (§0.5) states the realized record, readers, routine questions, canonical and projected ownership, drill-down identity, retention, interim exposure, restart continuity and privacy. It marks **no** surface beyond the requested deliverable. This Review accepts no product-scope mark. Per the architecture owner, technical D3 Review does not accept such items.

## 10. Verification

Executed against an immutable `git archive` of `51070e5e` at `$TMPDIR/ssds80-manual-review-51070e5/cand`:

| Check | Result and limit |
|---|---|
| Object identities (Manual, map, workplan at candidate, Phase B workplan, frozen 1.6.0, release-state refs) | Match the header |
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` | 4 tests OK; routing, index and lifecycle evidence only |
| `git diff --check 9e5a763… 51070e5…` | Clean (exit 0) |
| `git diff --stat fad3ee41… 51070e5…` | 63 files, 19,893 insertions, 1 deletion. Every changed path is under `qualification/ssds80/`, the Manual, or `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. No executable SSDS code |
| `git diff --exit-code fad3ee41… 51070e5… -- source/ dist/ orchestrator/docs/architecture.md` | Exit 0: byte-unchanged |
| PEM `source/project_engineering_memory.py` in the archive | First run without a Git directory failed binding-health route realization (`REVIEW_REQUIRED: local Git repository is unavailable`). Rerun with `GIT_DIR` bound to the repository object store and `GIT_WORK_TREE` to the archive: "PEM schema 1 valid: 5 families, 0 notices". Not a pass of anything semantic |
| Predicate transcription probe (`probe/routes.py`, run with `python3 -I`) | 10 rows; one non-independent permissive resolution (B1). Diagnostic only |

Not executed:
- the optional diagnostic model (it does not model R9 or the challenge route);
- any production owner, since none exists at G1;
- G2-G4 programs;
- package build or distribution parity, because this change touches no protocol source or generated descendant.

Not verified:
- every parser or scope-term input;
- full S1/S2 history enumeration;
- remote native issues or homes;
- the authoring conversation;
- each older Review's full trajectory set beyond mechanism presence and the named cases above.

These limits supply no pass and do not weaken B1.

## 11. Scientific checks

- **Findings:**
  - B1 and N1-N7 are architecture and evidence-method findings by this AI reviewer (Claude family, author-launched fresh-context sub-agent).
  - No material finding about a realized scientific result.
  - This file is their canonical review home, bound to candidate `51070e5` and these identities.
  - Revisit B1 when a replacement candidate changes who may end an objection.
- **Realized results:**
  - None produced, run or reviewed.
  - The only executions were document and schema checks and one deterministic predicate transcription.
  - The material scope examined is the architecture that will mediate scientific evidence. Datasets, numerical trajectories, campaigns and real assessors were unexamined.
- **Variants:**
  - One immutable candidate was judged. Prior candidates supplied failure hypotheses, not a selection campaign.
  - The probe enumerated 10 written-rule rows (criterion: does a non-independent record end the objection).
  - No analysis, pipeline, preprocessing, model or parameter variants were run or selected, and no held-out data exist.
- **Tensions:**
  - No accepted project D1/D2 authority was relied on for a consequential judgment, so the tension-search trigger did not fire.
  - No delegates; no unanswered delegate parts.
- **Gaps:** none of the owed questions was left unanswered beyond the verification limits in §10.

## 12. Common-mode note

This reviewer is of the **Claude** family:
- the same family as the Manual's author;
- the same as every Manual reviewer except the `3540d98`, different-family `b46c250` and `9e5a763` reviewers and the Phase B reviewer (GPT family).

It was engaged as a fresh-context sub-agent **launched by the authoring session**, with only the handoff. Fresh context is not epistemic independence. Shared dependencies:
- the candidate and its framing;
- the inherited workplan framing;
- all prior Review records, including the same-family ones whose suggestions produced earlier defects;
- the protocol corpus;
- the Git/Python toolchain;
- the author-written handoff.

The handoff deliberately gave no author conclusions. The verdict rests on the quoted predicates and the explicit trajectory, not on family diversity or reviewer count. A different-family review would reduce the model-family common mode.

## 13. D4 statement

**D4 is NOT AUTHORIZED.** This NO-PASS is technical evidence for G1 only:
- The Manual, its proposed defaults and its product-scope marks remain proposed.
- Closing B1 requires a replacement immutable candidate and an independent Review.
- Stakeholder acceptance of the Manual remains separate.
- G2 additionally needs a reviewed shadow D3→D4 workplan and explicit stakeholder authorization.
- G3 production-owner qualification and G4 per-subject cutover remain separate.

No commit or push was made.

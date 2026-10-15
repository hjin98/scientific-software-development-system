# SSDS 8 Architecture Manual — Independent D3 Review, candidate 6b986de

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 6b986deea8900fa5844621a6dfc0400f999e0d09
    SCOPE: the whole proposed durable Manual: (a) §21/§16.2 closure, (b) fidelity to the reviewed
           contract and the §0.3 refinements R1-R13, (c) adequacy (out-of-matrix), (d) inheritance and
           capability transfer, (e) qualification design, (f) doctrine-realization map, (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
           blob 82e36ecf2c3901b6986f54b4d1f05633964d527f (verified)
    REVIEW AID: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md
           blob d9547283b2cc02c15ce5b6d79617ef9f3da61394 (verified; aid, not authority)
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
    HANDOFF: qualification/ssds80/MANUAL-REVIEW-HANDOFF-SSDS-8.0-6B986DE.md (prompt below its rule)
    PRIOR REVIEWS: every Manual NO-PASS record the handoff names (6FF4ED1 through 29DA56E) and the
           Phase B E23F142 PASS: hypotheses and regression inputs only, never authority
    REVIEW METHOD: immutable git-archive snapshot of the candidate; governing owners read with
           git show at the public-source ref; diff 29da56e..6b986de read hunk by hunk (word diff);
           Part 0, §2.6, §3.3-§3.5, §4.1-§4.4, §5.2-§5.5, §6.6-§6.8, §8.3, §10.2-§10.4, §12,
           §13.7, §18.4, §19.1-§19.5, §31.5-§31.10 read in full, the rest located and spot-checked
           for the mechanisms prior closures rely on; family-level falsification of the independence
           realization (convergence owner, "Review strategy after recurrence"), attacked in both
           directions, with the new mechanism (the Admission eligibility rule and `res` in `base`)
           attacked hardest; requested document checks
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session,
           given only the handoff file; no authoring conversation
    MUTATION: this record only; no commit, push, source change or PEM update

Line numbers below refer to Manual blob `82e36ecf`. Scratch files were kept under `$TMPDIR/ssds80-manual-review-6b986de/`; nothing in this record depends on them remaining available.

## SERIOUS CHALLENGE

**None against accepted authority.** The blocker below lies in the proposed Manual's definition of the two independence enforcement points it introduces. The governing floors it must realize are coherent at SSDP 7.2.1, in the parent's invariants (A5, A9, restated at Manual §0.4) and in the reviewed workplan's disposition rule (§6.6). No accepted project D1/D2 proposition is relied on.

Governing statements used (paths at `aaeaf8b6`):

| Owner and locator | Text applied |
|---|---|
| `source/roles/software-design/SKILL.md`, Independent Review | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| Same | "Coherent D3, D4 violates it -> D4 blocker; D3 contradictory/ambiguous/inadequate/unrealizable -> SERIOUS CHALLENGE to D3" (applied here to the proposed D3, which is not yet accepted, so its defects are blockers) |
| `source/shared/references/architecture-and-design.md`, D3 formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| `source/shared/references/workflow-and-workplans.md`, Review | "Review independence means the reviewing context did not author the candidate and does not inherit author conclusions" |
| Same, human gates | "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." |
| `source/shared/references/evidence-evolution-and-dependencies.md`, Assessment disagreement | "route adjudication to the governing claim/owner or obtain discriminating evidence. Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position." |
| `source/shared/references/convergence-and-cycle-economy.md`, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism" |
| Same, Review readiness and independent review sufficiency | "route one family-level problem rather than intentionally returning one cheap sibling per review cycle" |
| Same, Review strategy after recurrence | "A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign." |
| `source/shared/references/testing-and-validation.md` | "Ask whether evidence could remain green while that owner is materially broken. If yes, it cannot close that owner claim." |

## Verdict

**NO-PASS. One blocking family survives (B1): the independence predicate's two inputs, which records must be independent and of whose authorship, are still stated locally and inconsistently, so the two enforcement points the repair introduced read undefined or contradictory definitions.**

The `29da56e` B1 repair is the right shape. It removes `res` from S1, refuses every non-independent or under-class adjudication at Admission (§8.3 step 3, line 1110), and reads `res` in `base` (§5.5, line 718). The main `29da56e` trajectory (the author's own counter-upholding of an independent revocation) is refused under step 3, and the sibling routes through observations, triples, counter-challenges and chain class are covered. The defects are now in what those two points read:

- (a) `base` reads `res` for every record "of a kind with an independence requirement", while step 3 classifies records by a conditional list and gives `res` only to a judgment with an `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` lineage. Read literally, no `MACHINERY` record can ever support, so §2.6's analyzer completeness, a workplan §21 item 2 capability, is never current. The alternative reading lets a self-declared equivalence support.
- (b) The §3.4 `ADJUDICATION` row still states the superseded rule ("independent of the challenged record's target's authors where it ends an objection"). Under that row the `29da56e` B1 trajectory is admitted again.
- (c) The root reference set, "for a support-tier judgment, the authors of its target content", is undefined where the root judges a record, task or obligation rather than content. For a disposition (`IMMATERIALITY`) the literal set is the failing assessor, not the claim's authors, so the claim's author can end an independent objection to the disposition of a failure on her own claim.

This is the sixth consecutive round in the independence branch of the judgment-disagreement family. It is not another missing route: both enforcement points now exist. It is a definitional consolidation that the repair left undone, and the recommended repair removes local restatements rather than adding mechanism (§1). The matching, content-identity, partition, revision-run, acting-rule, gate-minimum, publication and witness families held under the trajectories in §6. The requested document checks pass (§10) and do not exercise this defect. G1 stays open.

## 1. Blocker

### B1 — The independence floor's inputs are not defined once: `res` in `base` is keyed on kind but defined per classified record, the §3.4 row contradicts step 3, and the root reference set is undefined for record-targeted roots

**Earliest owner:** proposed D3 Manual:
- §5.5 `base`, line 718, and the paragraph at line 777;
- R13, line 98;
- §8.3 step 3, the independence and adjudication-eligibility bullets, lines 1109-1110;
- the §3.4 `ADJUDICATION` row, line 486;
- §2.6, line 401, and §4.4, line 589, as the contradicted statements.

Parent closure obligations implicated: workplan §21 items 2 (analyzer completeness declarations), 3 (independence of each disposition kind), 5, 13 (legacy and external import) and 23. This is an architecture defect. No reviewed contract is at fault: the workplan states independence per record ("for equivalence/completeness about the request's own change … every disposition of a failing assessment") and measures dispositions against "the claim's author" (workplan §6.6).

**Family:** judgment disagreement, independence of what ends an objection or supports a judgment. Shared cause across the last six rounds: independence is specified by local restatement at each consumer, not by one definition read everywhere. This round consolidated the consumers to two enforcement points but left their inputs locally defined, in six places that disagree:
- §3.4 rows;
- §4.4;
- §6.8 ("the claim's authors");
- step 3's independence bullet ("the authors of the judged target");
- step 3's eligibility bullet ("the authors of the content at the root", with a per-tier table);
- R13 and `base` ("a kind with an independence requirement").

#### Exact text

§5.5, lines 717-718:

```text
base(z)  = F  if ¬acts(z) ∨ superseded(z) ∨ status1(z) ∈ {REVOKED, BLOCKED} ∨ ¬cont(z) ∨ ¬tgt(z) ∨ vetoed(z)
                 ∨ (z's kind has an independence requirement ∧ ¬res(z))      -- §8.3 step 3; 29da56e B1(g)
```

§8.3 step 3, line 1109: "for equivalence and completeness about the request's own change, for every review, conformance, acceptance and plan-acceptance judgment, and every disposition of a failing assessment, a judgment satisfies an independence requirement only when its lineage class is `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` and its lineage is disjoint from the author's (for an authenticated human, of any of these kinds, when the human is not among the authors of the judged target … unknown authorship fails closed, §6.8) … `res(d)` (§5.5) is the S0 fact that `d` was admitted as independent".

§8.3 step 3, line 1110: "every `ADJUDICATION` is admitted only if it is independent, by the rule above, of the authors of the content at the **root** of its challenge chain (follow targets from its challenge through challenge-tier records to the first record or triple that is not challenge-tier; for a support-tier judgment, the authors of its target content; for an observation, the authors of the content it ran on; for a subject triple, the authors of that revision; for any other record, its author)".

§3.4, line 486 (`ADJUDICATION`, producer column, unchanged by this round): "independent of the challenged record's target's authors where it ends an objection (§8.3 step 3)".

§2.6, line 401: an analyzer supplies completeness "as an ordinary `COMPLETENESS` record with actor class `MACHINERY` (R0) … so it is current only while its content holds and its analyzer is pinned … and the only form in which analyzer completeness narrows a closure (§4.6) or a recorded basis (§6.5)".

§0.1, line 44: "Each such claim has exactly one statement here."

#### (a) `res` in `base`: kind-level read, record-level definition

`res` is defined only as "admitted as independent". Only a judgment carrying an `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` lineage can be admitted as independent. Step 3 classifies only the records its conditional list reaches. `base` reads `res` for every record whose *kind* has a requirement.

**Trajectory (restrictive, capability drop; Manual-internal contradiction).**
1. A project relies on analyzer completeness (§2.6), as the Manual's own §31.3 case does (line 2578: "a current `COMPLETENESS(EXEC)` judgment bounds the closure (an analyzer completeness declaration …)").
2. The analyzer emits `COMPLETENESS(X, EXEC)` with actor class `MACHINERY`. `COMPLETENESS` is a kind with an independence requirement (step 3; §4.4).
3. A machinery record has no `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` lineage (§12.2 defines lineage only for task executions; §12.4 says R0 is "never a judgment"). So it is never "admitted as independent", and `res = F`.
   - When the record is "about the request's own change", step 3 classifies it non-independent outright.
   - Otherwise `res` is simply undefined, and the literal definition gives `F`.
4. `base = F` and `current = F`, so §4.6's closure never sees a current `COMPLETE`. Every closure that relied on the analyzer falls back to the whole tree, `UNBOUNDED`. Such closures serve no permissive use (§6.5, §6.6 "Bounded and unbounded bases"), so every red-then-green stop that depended on analyzer bounding goes to the owner.

§2.6 states the opposite. Workplan §21 item 2 requires "analyzer completeness declarations" as a working coverage source (workplan lines 981 and 1813). The same reading reaches:
- `LEGACY_ACCEPTANCE` and `EXTERNAL_ACCEPTANCE`, if "acceptance judgment" in step 3 includes them. Their content has no admitted authoring record, so "unknown authorship fails closed" and "an unknown author lineage is never disjoint from an agent's". An agent import never supports, and a human import supports only with an attestation or the owner exception. This silently narrows workplan §21 item 13 and §19.2, which import "the fact that the legacy process accepted" without claiming SSDS reviewed it.
- A machinery `ABSORB` `INTAKE_DISPOSITION`, whose §3.4 row says "independent reviewer" although step 3 does not list the kind.

**The alternative reading is permissive.** To keep §2.6, an implementer can read "a kind with an independence requirement" as the kinds whose requirement is unconditional. Then a self-declared `EQUIVALENCE` about the author's own change is `current`, and `sat(content)` lets it cover reliant records. That contradicts §4.4 ("a self-declared one is admitted as non-independent (§8.3) and covers nothing") and A5.

An implementer must choose between §2.6 and §5.5 (or between §4.4 and §5.5). Either choice violates a stated rule.

#### (b) The §3.4 `ADJUDICATION` row contradicts step 3 on the `29da56e` trajectory

Take `29da56e` B1's trajectory: Alice authors `r`, `P` accepts it, `H` challenges, independent `A` upholds (revocation `a1`), and Alice upholds the counter-challenge `c2`.
- Under step 3 the chain root is `z`, whose target content's author is Alice, so `a2` is refused.
- Under the §3.4 row, "the challenged record" is `a1`, and its target is `c1`, whose author is `H`. Alice is independent of `H`, so `a2` is admitted and the revocation lifts.

The row also limits the requirement to adjudications "where it ends an objection", while step 3 applies it to every adjudication of any outcome. Its class column ("a challenge against an R3 human judgment") is narrower than step 3's chain-class rule. §3.4 is a [D3 decision] kind table in a closed schema (§3.6), so it is normative. The two statements contradict each other on exactly the trajectory the repair targeted.

#### (c) The root reference set is undefined where the root judges a record

"For a support-tier judgment, the authors of its target content" presumes the target is content. Several support-tier kinds target records, tasks or obligations:
- `IMMATERIALITY` (failing assessments, line 462);
- a revising reviewer's `TASK_RESULT` (a task, line 469);
- `COORDINATION_DECISION`, `MATERIALITY_RECLASSIFICATION`, `HUMAN_DECISION`, `LINEAGE_ATTESTATION` and `NON_AUTHORSHIP_ATTESTATION`.

"Target content" is defined nowhere. §6.8's "evaluated target content" is defined for assessments only.

**Trajectory (permissive; the claim's author ends an objection to a disposition of a failure on her own claim).**
1. Alice authors the claim content of D4 subject `s`. Independent assessor `Q` records failing assessment `a⁻` on its realization.
2. The independent owner `O` records `IMMATERIALITY d` covering `a⁻`. `d` is admitted as independent, `disp(a⁻) = T` and `undisputed = T`.
3. Reviewer `H` thinks the failure is material and raises a blocking challenge `c` against `d`. Then:
   - `status1(d) = BLOCKED`, `base(d) = F` and `eff = F`;
   - `undisputed(s, e) = P`, so `valid(s)` and discharge are provisional, or `OPEN` where policy forbids provisional continuation.
4. `ADJUDICATE(c)` is derived. Policy names qualified D4 adjudicators, and Alice is among them; nothing in §3.5 or §12 excludes her.
5. Alice records `ADJUDICATION DISMISSED` on `c`. Step 3: the chain is `c → d`, and `d` is the root. The literal reference set, "the authors of its target content", is the authors of `a⁻`: `Q`, or the machinery that produced the realization. Alice is not among them. The chain's highest class is R2, which Alice meets. The adjudication is admitted.
6. The dismissal is a relaxer with `gate = cont = T`, so it is in force. Then:
   - `open(c) = F`, `status1(d) = CLEAR` and `base(d) = T`;
   - `eff(d, a⁻) = current(d) = T`;
   - `undisputed = T`, and `valid(s)` returns to `T`.

The claim's author has ended an independent objection to the disposition of a failure on her own claim. This violates:
- workplan §6.6, which says every disposition "must be independent of the claim's author";
- A5;
- R13's own claim that "the same floor applies to every record that can end an objection".

The dismissal is not itself a "disposition", so §6.8's claim-author rule never reaches it. Only the root rule applies, and it names the wrong set.

The same gap lets a D2 revision's author dismiss a blocking challenge against the revising reviewer's revision-assessment record. The root is a `TASK_RESULT` whose target is "task", which has no content. The record then counts again (§10.2), and `ACCEPT` and `GATE` become ready. Independent acceptance and the gate still follow, so the effect is bounded, but the SD-16/SD-19 safeguard's objection was ended by the reviewed party.

#### Related, pre-existing

Step 3's independence bullet measures human independence against "the authors of the judged target". For an `IMMATERIALITY` that is the failing assessor. §6.8 measures it against the claim's authors. §6.8 is more specific, so this is resolvable, but it is a fourth local definition of the same set.

#### Bounded sibling list (one family-level problem)

| Variant | Candidate result | Required result |
|---|---|---|
| (a1) machinery `COMPLETENESS` (§2.6), in any request | literal `base = F`; analyzer completeness never bounds; contradicts §2.6 and §31.3 | supports while content and analyzer hold, as §2.6 says |
| (a2) `EQUIVALENCE`/`COMPLETENESS` not about the request's own change, by an agent or human with no classification | `res` undefined | supports unless admitted as non-independent |
| (a3) `LEGACY_ACCEPTANCE`, `EXTERNAL_ACCEPTANCE` if read as "acceptance judgments" | agent imports never support; human imports need an attestation or the owner exception | state whether imports carry an independence requirement (the reviewed contract imports a fact and does not judge) |
| (a4) self-declared `EQUIVALENCE` about own change, under the reading that keeps (a1) | supports | covers nothing (§4.4) |
| (b) author's counter-upholding of an independent revocation, under §3.4's row | admitted | refused (step 3) |
| (c1) claim author dismisses a blocking challenge against an `IMMATERIALITY` or a superseding reassessment | admitted on the literal set | refused: reference set is the claim's authors |
| (c2) revision author dismisses a blocking challenge against a revising reviewer's `TASK_RESULT` | admitted (target "task" has no content) | refused: the content the record assessed |
| (c3) challenges against `COORDINATION_DECISION`, `HUMAN_DECISION`, attestations | set undefined | defined by the same recursion |
| Held: the `29da56e` B1 main trajectory and its siblings (b)-(e) under step 3; a human author's direct non-independent `ACCEPTANCE PASS` (`base` now `F`); non-independent superseder, reliever and disposition | refused or no effect | keep |

#### Convergence assessment and options

The active simplification trigger applies to the family. The same mechanism, deciding which records count as independent and against whom, has been patched in six consecutive rounds.

This round's repair moved in the right direction: it removed `res` from S1 and collapsed the route list into two enforcement points. What remains is not a missing route. The predicate the two points read is defined in six places. A further local patch, such as fixing only the §3.4 row or only `IMMATERIALITY`, would leave the cause.

Options for the stakeholder (Phase C handoff §5):

1. **Define the inputs once (recommended; subtractive).**
   - Define one record-level S0 fact, `nonind(z)`: `z` was subject to an independence requirement at admission and was not admitted as independent. Have `base` read `nonind(z)` in place of "kind has … ∧ ¬res(z)". Records outside every requirement, machinery records and (if so stated) imports are then never non-independent.
   - Define one function, `authors(x)`, from any record or triple to the authors of the repository content it ultimately judges. Content targets give their authors. A record target recurses to the content it is about: an assessment's claim content, a disposition's claim content through the assessments it covers, a `TASK_RESULT`'s candidate or assessed revision. An observation gives the content it ran on, and a triple gives its revision's authors.
   - Use that one function in step 3's independence bullet, in §6.8, in the eligibility rule and, by reference only, in §3.4. Replace the §3.4 row's producer clause with "eligible by §8.3 step 3".
   - State in §19.2 and §20.2 whether imports carry a requirement.

   This deletes text and adds no record kind, store, latch or S1/S2 input.
2. **Narrow `base`'s read to the unconditional kinds and §4.4's case explicitly (adds a clause).** Name exactly the kinds and conditions in `base`. This keeps the local definitions, so (b) and (c) still need separate edits; it is not recommended.
3. **Pause** for stakeholder direction if the author judges that one `authors(x)` function cannot serve both the support floor and adjudication eligibility. For example, the stakeholder may want eligibility against the parties as well, which is `29da56e` N6, now a listed stakeholder item.

Do not read S2 values inside the eligibility rule, and do not move independence back into S1.

#### Required discriminator (real owners, G3)

The chain is Admission (step 3), Derivation (`base`, `current`, `sat`, `eff`, §4.6 closure), discharge, readiness and the inspector. No fixture may seed `res`, `nonind`, `current` or a closure bound.
- (a1): a machinery `COMPLETENESS(X, EXEC)` with no marker, submitted both with and without a content change to `X`, bounds the closure, and the §31.3 red-then-green case completes. An implementation that reads `res` by kind must fail.
- (a3): an agent's `LEGACY_ACCEPTANCE` of a Case B subject makes it valid, or, if the stakeholder chooses otherwise, the restriction is listed in §0.3 and §19.2.
- (a4): an author's self-declared `EQUIVALENCE` about the author's own change covers no reliant record.
- (b): run the `29da56e` chain case against an Admission whose kind constraints are generated from §3.4. It must refuse.
- (c1): the `IMMATERIALITY` trajectory above. The claim author's dismissal is refused, and an independent adjudicator's dismissal restores the disposition.
- (c2): the revision author's dismissal of a challenge against a revising reviewer's record is refused.

§31.6 has none of (a1)-(a4) or (c1)-(c3), so a faithful implementation of either literal reading passes the program (DS-001).

## 2. Non-blocking findings

**N1 — A refused adjudication is not re-dispatchable under §10.3's literal text (liveness; contradicts step 3).**
- Step 3 (line 1110) says a refused adjudication "answers nothing, and `ADJUDICATE(c)` stays dispatchable".
- §10.3 (line 1229) re-dispatches an unanswered obligation "only when its task ended without an admitted judgment (a `BLOCKED` result, or passing judgments refused at admission)". An `ADJUDICATION` has no passing outcome.
- Nor is it stated whether a refused adjudication rejects the whole request or is refused with its `TASK_RESULT` admitted, as step 7 does for `CONFORMANCE_RESULT`.

Extend the §10.3 parenthesis to "any judgment refused at admission", and state the request shape. No mechanism is needed. §31.6 already expects dispatchability, so it would catch the literal reading.

**N2 — `res` is fixed at admission, so an upheld challenge against an attestation changes nothing (disclosure).**
- Step 3 fixes the classification "from the binding and any co-submitted `LINEAGE_ATTESTATION` or `NON_AUTHORSHIP_ATTESTATION`; a later attestation does not change it."
- Now that `base` reads `res`, a credited record keeps supporting after an upheld challenge proves its attestation false. The correction route is a challenge against the credited record itself.

State this in §5.5 or §32. Alternatively, have `nonind` also hold while a co-submitted attestation is `REVOKED`; that is an S1 read in `base`, which `base` already makes, and it adds mechanism, so it is marked as such.

**N3 — Over-broad reference sets are fail-closed costs, not disclosed.**
- An observation root's set is "the authors of the content it ran on". For an `UNBOUNDED` realization that is every author of the whole tree.
- An assessment root's target content includes its specification revision, so the specification's authors are excluded too.
- A triple with absorbed bytes admits only humans with `NON_AUTHORSHIP_ATTESTATION`, or the owner exception. That exception needs policy to name no other qualified human.

The result is that some blocking challenges can be dismissed only by rerunning evidence or by the owner exception. List this in §32.2, and measure its rate in §31.9.

**N4 — "R3 human record" (§3.5) and "highest decision class of any record in that chain" (step 3) differ for challenges.** A `CHALLENGE` has no class in §3.4, while §12.3 gives the Human role class R3. If a human-raised ordinary challenge is an "R3 human record", every challenge a human raises forces human adjudication. Say which. Either reading fails closed.

**N5 — Wording now false or overclaiming.**
- §5.5, line 777, says "independence is required to support, never to object". Step 3 now refuses a non-independent restrictive upholding too. That is surfaced in R13 ("Every `ADJUDICATION` … or it is refused"), but the §5.5 sentence should say "never for an adverse judgment".
- Closure map line 40 marks "decision class and independence of each disposition kind" `CARRIED`, although R13 refines it, and it cites the stale §3.4 row.
- R13's "the same floor applies to every record that can end an objection" overclaims while B1 (b) and (c) stand.

**N6 — Qualification gaps (DS-001).** §31.6 now contains the `29da56e` B1 chain, support-route and dispatchability cases, which closes `29da56e` N5 for those cases. It has no case for B1 (a1)-(a4) or (c1)-(c3). These are design-program omissions; execution is G3.

**N7 — Party exclusion is a stakeholder item (carried `29da56e` N6).** It is now listed in closure map §5. Under the root rule, the author of the judgment at the root (for example the accepting reviewer `P`) may adjudicate a counter-challenge that restores `P`'s own acceptance. That is policy-level today and not a blocker.

**N8 — Disclosed costs and trade-offs remain live (not blockers).** These carry `29da56e` N7:
- bounded-only reproduction (partial SD-17 reversal);
- SD-24's narrowing;
- D1/D2 re-gating after exact-identity change, fences and `OVERTAKEN`;
- per-enactment acceptance and gate (R12);
- no support from another pending enactment's frame;
- adverse frame decisions vetoing after abandonment;
- gate-minimum accumulation;
- the cutover race and fenced-cutover half state;
- the context-revert residue.

R13 and this round's repair direction were the author's under stakeholder-record item 19, not stakeholder decisions. The question this reviewer would put to the stakeholder is option 1 versus option 3 of B1, together with N7.

**N9 — Retained historical and empirical limits.** These carry `29da56e` N8:
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
| 1 | §1: answer present. |
| 2 | §2: **not substantively closed for analyzer completeness (B1 a1)**. §2.6 states the contract, but §5.5 `base` withholds support from every `MACHINERY` record on the literal reading. |
| 3 | §§3.4-3.5, 6.8, 8.3: **not substantively closed (B1 b, c)**. The independence of disposition-related adjudications has no defined reference set for record-targeted roots, and the §3.4 row contradicts step 3. The new §3.5 floor closes `29da56e` N3. |
| 4 | §4: answer present. The §4.4 "covers nothing" rule is now realized in `base`, but in a form that conflicts with §2.6 (B1 a). |
| 5 | §§5-7: **partly**. Single-valuedness and stratification hold: `res` is S0, `base` reads S0/S1 only, S1 reads no independence fact, and §5.6's monotonicity is unaffected. The permissive semantics of dispositions are open (B1 c1). |
| 6 | §8 and §§21-23: answer present. The step-3 bullets are the B1 locus, recorded under item 3. |
| 7 | §§10-11: answer present, with the N1 liveness clarification. |
| 8-12 | Answers present at the sections the closure map names. |
| 13 | §19.2, §20.2: **partly (B1 a3)**. Whether imports carry an independence requirement, and therefore whether they support, is undecided. |
| 14-22 | Answers present. §29.7 and §30 record items 21-22 (rationale, not adequacy evidence). |
| 23 | §§12-13, 16.3: **partly (B1 c)**. Role separation ("May not: judge work … its own execution or lineage authored") is unenforced for a dismissal on a disposition root. |
| 24-26 | §13, §14, §§15-16: answers present. No `HARD` template is claimed qualified. |
| 27 | §29: **partly**. The §29.3 E0 claim for independent acceptance holds under step 3. It depends on B1 (b) being resolved in step 3's favour, and on B1 (c) for disposition-backed evidence. |

**§16.2, both tables:** none found unresolved. Each product invariant and frozen surface has an explicit disposition in §26.4 with a replacement owner. The delta since `29da56e` does not touch §26. This is a document-level transfer check.

## 4. Refinements R1-R13

| # | Assessment |
|---|---|
| R1 | Sound in the bounded design examined: one recorded basis with frozen resolution context; `on⁺ ⇒ on⁻ ⇒ link⁻` by construction; the class rule leaves no named dimension outside `ext`. Bounded-only stops are the disclosed partial SD-17 reversal (N8). B1 (a1) would, on its literal reading, silently remove analyzer bounding, the main route by which R1's permissive stops are reachable. That is a B1 defect, not an R1 defect. |
| R2, R3 | Sound: the SCC clamp precedes presentation; authenticated corrupt prefixes halt. |
| R4 | Sound under the declared crash model; re-gating cost disclosed. |
| R5, R6, R7 | Sound. |
| R8 | Sound for supersession and relief (exact target, gate exception, independence of superseder and reliever). |
| R9 | Sound in its veto, answering, `REFUSED` and S0/S1-only reads. Its stop rule ("each counting only if independent (`res` for a judgment, admission for an adjudication …)") is realized except where B1 (b)/(c) apply. |
| R10, R11 | Sound. |
| R12 | A deliberate, surfaced narrowing (SD-25/SD-26). Its costs are N8. |
| R13 | **Sound in principle and in its two-point structure; unsound as realized, and incomplete as a listing.** Admission eligibility plus a support floor is the right simplification. Its inputs are inconsistently defined (B1). The listing does not mention the effect on machinery records and imports (a1, a3). R13 now does list the extension of human unknown-authorship to every kind, which closes `29da56e` N2. |

## 5. Re-verification of previous findings

The Manual delta from `29da56e` to `6b986de` touches:
- R9/R13 and the revision log;
- the §3.4 `NON_AUTHORSHIP_ATTESTATION` row;
- the §3.5 floor;
- §5.3 `gate`;
- §5.5 `base`, `stands⁻` and the paragraph at line 777;
- §8.3 step 3 (independence, eligibility);
- §10.2's event list;
- §13.7;
- §31.6.

The closure map gains one stakeholder item and an R13 wording. Every earlier closure whose mechanism lies outside those hunks was re-checked for presence of its mechanism in the candidate text. The checked mechanisms include:
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
| 29DA56E B1 | **Mostly closed; residue in B1 here.** Step 3 now refuses every adjudication not independent of the chain root or below the chain's highest class (line 1110). This covers the counter-challenge, observation, triple, contested-upholding and chain-class siblings, (a)-(e). (g) is closed in direction: `base` reads `res`, but in a form that creates B1 (a). (f) is partly closed: the root is defined, but its set is undefined for record-targeted roots (B1 c). The §3.4 row was not updated (B1 b). |
| 51070E5 B1 | Closed: first-order upholding and dismissal now pass the Admission eligibility rule. |
| 9E5A763-DF B1 | Closed: `relieved` requires `res(y)`; supersession requires independence. |
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
| A18B544 B1-B2 | Closed: only a completeness judgment bounds a closure; qualification lives in the minimum. B1 (a1) here threatens the analyzer form of that judgment, not the A18B544 mechanism. |
| E9E6E9F B1-B2; E2154AC B1; 3540D98 B1-B4 | Closed: one content representation without exception; the full `ext` class; qualified gate in the minimum; equal regions `ABSENT`. |
| 798B2B4 B1-B4; 71CF9B3 B1-B2; 86AB683 B1 | Closed: run-keyed currency as a target condition; display predecessor; symlink traversal recorded; R10 restores S11. |
| 1FFBBF0 B1-B2; 53669A5 B1-B3; D837363 B1-B4 | Closed: free seed and unobserving runner classes in the class rule; acceptance-target duty in every frame; effect-keyed write set. |
| CC005DB B1-B3; C6DA678 B1-B3 | Closed: effective comparison with frozen context; surface-only product-scope veto; item-revision-independent `same`. |
| B595F2C B1-B4 | B1-B3 closed. **B4 partly closed**: no re-dispatch, count or order resolution, but B1 (c) here lets a non-independent party end an objection to a disposition. |
| 6FF4ED1 B1-B4 | Closed. |

### Non-blocking findings

| Review | Status |
|---|---|
| 29DA56E | N1 closed in substance: a non-independent adjudication is refused and answers nothing. The §10.3 re-dispatch wording lags (N1 here). N2 closed: the attestation target is widened to any record step 3 classifies, and R13 lists the narrowing. N3 closed: the §3.5 floor names chains containing an R3 human record. N4 closed: (a) machinery `ABSORB` runs by entry identity; (b) the in-flight request is rejected at step 7 and its records salvaged. N5 partly closed: the chain, support-route and dispatchability cases were added; the B1 siblings here are missing (N6 here). N6 is surfaced as a stakeholder item (N7 here). N7 and N8 are open as N8 and N9 here. |
| 51070E5 | N1 closed (classification fixed at admission, now with the N2 disclosure gap here); N2 closed (adjudications refused rather than answering); N3-N5 closed; N6-N7 open as disclosed. |
| 9E5A763-DF | N1-N3 closed; N4-N5 open as disclosed. |
| 051CCE3 | N1-N5 closed for their named cases; N6-N7 open as disclosed. |
| 63DDF91 | N1-N5 closed; N6 open. |
| F03B15E | N1, N2, N4, N5 closed. N3 open as a disclosed half state. N6 open. |
| 61CD09B | N1, N3-N6 closed. N2 closed as disclosure. N7 open. |
| 362AF9F | N1-N6 closed. N7 open. |
| F22B4DC | N1-N5 closed (N4 as disclosed churn). N6 open. |
| B46C250 (same family); B46C250-DF | N1, N3, N4 (and DF N6) closed. Gate-minimum accumulation (N2) and provenance (N5) open as disclosed. |
| F7419D5; 575DC78; 5C55D4B | Closed for their named cases. The trade-offs are disclosed. |
| 27EF339 | N1 open as a disclosed reproduction cost. N2 open as the stakeholder-level SD-17 reversal; B1 (a1) would deepen it on the literal reading. N3-N7 closed. |
| 0B6C4FA | N1-N6 closed. N7 partly closed: B1 family open. |
| A18B544; E9E6E9F; E2154AC | Closed, with disclosures. |
| 3540D98 | N1, N3 closed. N2 (later-`ABSENT`) and N4 (operational limits, defaults) open as disclosed. |
| 798B2B4; 71CF9B3; 86AB683 | Closed except the retained later-`ABSENT` limit and the map's aid status. |
| 1FFBBF0 | N1-N4, N6 closed. N5 open as a disclosed class-change cost. N7 partly closed (B1 family). |
| 53669A5; D837363; CC005DB; C6DA678 | Closed except the noted partials: annotations do not decide adequacy; the R13 accounting overclaims (N5 here); the same-content amendment veto is deliberately retained; reviewer-quality E3. |
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
- **Permissive:** first-order dispositions carry `res` in `eff` (line 995). An upholding against `a⁻` must also pass eligibility, whose root is `a⁻`; that root's target content includes the reading, and so the claim content. B1 (c1) is a disposition-family sibling one level up: a dismissal that restores a disposition, measured against an undefined set.
- **Restrictive:** no stop was withdrawn without cause, and no settled failure resurrects. Refusing restrictive adjudications by non-independent actors leaves the challenge open and blocking, so it removes no stop. B1 (a1) is restrictive in the other sense: on its literal reading it removes analyzer bounding, so more failures go to the owner. That is fail-closed, but it is an undisclosed capability loss.

**Phase B N2 re-tested on the text.** The case is an alternate tree differing only outside a recorded narrow basis, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld:
- a differing old-content run stays in (2) through `link⁻` with `o' = real(a⁻)`;
- a yielding present-content run keeps (4) false;
- losing completeness only shrinks `on⁺`.

A machinery completeness judgment non-current under B1 (a1) is the "lost completeness" case and shrinks only `on⁺`, so polarity holds on either reading. The SCC clamp precedes presentation (§5.6), and authenticated corrupt prefixes halt (§5.7). Closed at design level, unexecuted at G3. Phase B N1 is open (N9). N3 is open as a diagnostic limit. N4 is open as an empirical cost and applicability limit.

## 6. Out-of-matrix trajectories attempted

| Trajectory | Result |
|---|---|
| `29da56e` B1 main: author or `UNKNOWN`-lineage counter-upholding of an independent revocation (acceptance, review, conformance, plan acceptance, gate, triple) | Held under step 3; **admitted under the §3.4 row (B1 b)** |
| Non-independent dismissal of a blocking challenge against an observation, a triple, or an independent upholding (`contested`) | Held: refused; the observation's root set is the content it ran on |
| R2 counter-upholding against an R3 human upholding | Held: refused by the chain-class rule; §3.5 routes to a human |
| Claim author dismisses a blocking challenge against an independent `IMMATERIALITY` | **B1 (c1)**: admitted on the literal root set |
| Revision author dismisses a blocking challenge against a revising reviewer's `TASK_RESULT` | **B1 (c2)** |
| Machinery analyzer `COMPLETENESS` under `base` | **B1 (a1)**: literal `base = F` |
| Agent `LEGACY_ACCEPTANCE` / `EXTERNAL_ACCEPTANCE` | **B1 (a3)**: undecided whether imports carry a requirement |
| Self-declared `EQUIVALENCE` under the reading that keeps (a1) | **B1 (a4)**: supports |
| Human author's direct non-independent `ACCEPTANCE PASS` | Held: `base = F`, `ACCEPT(s)` stays derived |
| Non-independent superseder, reliever or disposition | Held |
| Non-independent restrictive upholding | Refused; challenge stays open and blocking; no stop lost (N5 wording) |
| Refused adjudication and `ADJUDICATE(c)` | Fails closed; literal §10.3 dead-ends it (N1) |
| Upheld challenge against a false `NON_AUTHORSHIP_ATTESTATION` | Credited record keeps `res`; correction by challenging the record (N2) |
| Unbounded realization or absorbed-byte triple as chain root | Fails closed; liveness cost (N3) |
| Accepting reviewer adjudicates the counter-challenge restoring own acceptance | Not excluded; policy-level (N7) |
| `res`, eligibility and the class rule against stratification | Held: eligibility is decided at admission from S0 facts and fixed chains (targets are strictly earlier and immutable); `base` reads S0/S1 only; S1 reads no independence fact; §5.6 monotonicity unchanged |
| `rid` uniqueness and stability; `D_n[X]` equal to the post-integration state; machinery `ABSORB` runs | Held (lines 651, 1214) |
| Withdrawn reliance on another pending enactment's frame records | Disclosed narrowing (R12); no owner-required capability shown dropped |
| Completeness polarity, support cycles, corrupt prefixes; structure/`ignore`/analyzer/system-version change with fixed bytes; free attributes, pins and locator sets; unobserving runners; equal, partial and nested regions; mode-only, symlink, gitlink and LFS changes | Held under §§1.4-1.5, 5.6-5.7, 6.3-6.6 (unchanged text since `29da56e`) |
| Gate minimum across holders, frames, rebases, iterations and runs; gate `REJECT` across runs; cutover ordering | Held (§5.5, §19.5) |
| Slow publisher, fence chains, stale-consistent restore, positive-only attestation | Held within the declared crash and witness models |

This is bounded falsification, not a proof over all ledgers. In the families that held, discovery stopped where it duplicated earlier records' systematic cases or became implementation-like. In the B1 family it stopped once the shared cause, local definitions of the predicate's inputs, explained every sibling found. Enumerating every record kind as a chain root would duplicate option 1's recursion.

## 7. Minimum architecture and capability transfer

The four primitives, six components and stores each carry a capability a governing invariant requires (§30).

The two enforcement points of R13 are a genuine simplification over the earlier per-route list:
- `res` left S1;
- `gate` and `stands⁻` shed their conjuncts.

B1's recommended option removes text. It replaces six local definitions with one S0 fact and one authorship function, and adds no record kind, store or latch.

**One capability is at risk on the literal reading:** analyzer completeness (§2.6, workplan §21 item 2), with legacy and external import support as the second. Neither is dropped by intent, but the text does not keep them.

The 1.6.0 supersession preserves the version-bound Level 0 Core, frozen profiles and the single composition root (§26.3-§26.4, §28). The frozen document, `source/` and `dist/` are byte-unchanged from `fad3ee41` (PEM PC-001). Workplan §18's consolidated-control-plane and BEFE678 capability classes still map to current owners.

PEM activates (mature replacement, recurrence). The accepted base was resolved independently of branch position:
- local `main` is `af0455753e20ee54a969c844872e29e270007211`;
- the PEM blob is `1561797125622f355f84eb27319f87e8fa4227d9`, identical at the candidate (no overlay);
- schema validation passed (§10).

```yaml
has:
  - {id: PC-001, disposition: APPLICABLE, reason: frozen Core/profile isolation required by the current versioning owner; preserved}
  - {id: DS-001, disposition: APPLICABLE, reason: §31 lacks B1 (a1)-(a4) and (c1)-(c3); green fixtures could coexist with either literal reading}
  - {id: SP-001, disposition: APPLICABLE, reason: evidence-only; one canonical owner with regenerated projections; B1 is a one-owner-definition defect of the same shape inside the Manual}
  - {id: SP-002, disposition: APPLICABLE, reason: evidence-only; records never name their containing commit (G3 invariant)}
  - {id: FF-001, disposition: APPLICABLE, reason: evidence-only; validate-before-publish genesis and replacement lineage}
```

Absence of a 7.x episode in PEM proves nothing.

## 8. Qualification-design adequacy

The owner boundaries are right: Derivation and Content Model consumed by Admission and the Interface; the real publisher, fences and witnesses; genuine Dispatcher envelopes and runner custody; real acceptance, gate and inspector paths. Every runtime group is labelled UNEXECUTED, and the diagnostic model is kept apart.

§31.6 now discriminates the `29da56e` B1 chain and support-route cases at real owners. That includes the §3.4-row reading of (b): the chain case requires refusal, so an implementation following the row fails.

The program is **not adequate for B1 (a) or (c)**:
- No case runs analyzer completeness after `base` reads `res`. The §31.3 red-then-green case assumes analyzer bounding, but it does not assert that the analyzer record is current through `base`, so an implementation choosing `res = F` for machinery records could pass by using a reviewer completeness judgment in the fixture.
- No case covers imports, record-rooted chains or the `TASK_RESULT` root.

These are G1 design-program gaps; their execution is G3. Proposed thresholds and defaults are neither accepted nor calibrated here.

## 9. Doctrine-realization map and O1

This Review read the D3 role entrypoint and the architecture, workflow, evidence, convergence and testing owners at `aaeaf8b6`. It listed the seven entrypoints there (four roles, three specialists) and confirmed that §29.2-§29.5 map all seven, with an explicit E3 catch-all (§29.6). It did not re-read every entrypoint's full text, because the delta does not touch §29. That is a stated limit, not a pass. No omitted duty was proved.

**One E0 claim is conditional.** §29.3's "durable authority mutation needs its acceptance process, independent falsification … **E0**: `ACCEPTANCE` classes and independence" holds under step 3. It fails on a reading of §3.4's row (B1 b), and for disposition-backed evidence on the literal root set (B1 c1).

O1 (§0.5) states:
- the realized record and its readers;
- routine questions;
- canonical and projected ownership;
- drill-down identity;
- retention;
- interim exposure;
- restart continuity;
- privacy.

It marks **no** surface beyond the requested deliverable. This Review accepts no product-scope mark; technical D3 Review does not accept such items.

## 10. What was verified and how; what could not be

Executed against an immutable `git archive` of `6b986dee` at `$TMPDIR/ssds80-manual-review-6b986de/snap`:

| Check | Result and limit |
|---|---|
| Object identities (Manual, map, workplan at candidate, Phase B workplan, frozen 1.6.0, release-state refs) | Match the header |
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` | 4 tests OK; routing, index and lifecycle evidence only |
| `git diff --check 29da56e… 6b986de…` | Clean (exit 0) |
| `git diff --stat fad3ee41… 6b986de…` | 67 files, 21,071 insertions, 1 deletion. Every changed path is under `qualification/ssds80/`, the Manual, or `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. No executable SSDS code |
| `git diff --exit-code fad3ee41… 6b986de… -- source/ dist/ orchestrator/docs/architecture.md` | Exit 0: byte-unchanged |
| PEM `source/project_engineering_memory.py` in the archive, with `PYTHONPATH` set to the archive's `source/` and `GIT_DIR` bound to the repository | "PEM schema 1 valid: 5 families, 0 notices". Structural only |

Not executed:
- the optional diagnostic model, which does not model R9, R13, Admission eligibility or `base`'s independence read;
- any production owner, since none exists at G1;
- G2-G4 programs;
- package build or distribution parity, because no protocol source or generated descendant changed.

Not verified:
- every parser or scope-term input;
- full S1/S2 history enumeration;
- remote homes;
- the authoring conversation;
- each older Review's full trajectory set beyond mechanism presence and the named cases;
- the full text of every role and specialist entrypoint against §29.

These limits supply no pass and do not weaken B1.

## 11. Scientific checks

- **Findings:**
  - B1 and N1-N9 are architecture and evidence-method findings by this AI reviewer (Claude family, author-launched fresh-context sub-agent).
  - No material finding about a realized scientific result.
  - This file is their canonical home, bound to candidate `6b986de` and the identities above.
  - Revisit B1 when a replacement candidate changes how `base`, Admission eligibility or §3.4 define independence or its reference set.
- **Realized results:**
  - None produced, run or reviewed.
  - The only executions were document, test-suite and schema checks.
  - The material scope is the architecture that will mediate scientific evidence. Datasets, numerical trajectories and real assessors were unexamined.
- **Variants:**
  - One immutable candidate was judged. Prior candidates supplied failure hypotheses, not a selection campaign.
  - Two kinds of variants were evaluated against the written predicates, each by one criterion:
    - eleven sibling cases (B1 a1-a4, b, c1-c3, and the held rows of §6) were checked against whether a record supports or ends an objection without the independence the governing owners require, or is denied support that the Manual elsewhere grants;
    - two textual readings of `base` were each evaluated against §2.6 and §4.4.
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
- all prior Review records, including same-family ones whose suggestions led to repairs. The `29da56e` record's options 1 and 2 were adopted together here. Option 2's suggestion was "`base(z) = F` when `z` has an independence requirement"; it was realized at kind level, which is where B1 (a) entered.
- the protocol corpus;
- the Git/Python toolchain;
- the author-written handoff.

The handoff gave no author conclusions. The verdict rests on the quoted predicates and explicit trajectories, not on reviewer count or family diversity. A different-family Review would reduce the model-family common mode.

## 13. D4 statement

**D4 is NOT AUTHORIZED.** This NO-PASS is technical evidence for G1 only.

- The Manual, its proposed defaults and its product-scope marks remain proposed.
- Closing B1 needs a replacement immutable candidate and an independent Review.
- The choice among B1's options, and N7, belong to the stakeholder, or to the author under item 19 as the record states.
- Stakeholder acceptance of the Manual remains separate.
- G2 additionally needs a reviewed shadow D3→D4 workplan and explicit stakeholder authorization.
- G3 production-owner qualification and G4 per-subject cutover remain separate.

No commit or push was made.

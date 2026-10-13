# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 16

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: a4145880878b71c1cb3134f003d83b519e206f56
    SCOPE: whole proposed architecture; (a) the revision-16 repairs: anchored `about`
           (anchor recorded at a failing assessment's admission, `succ*` over admitted
           structural changes, per-role search scopes `where`, `adverse` requiring the target
           within the subject's own scope; claim-unit membership removed from derivation);
           own-check salvage, record-by-record checking, retired-key envelopes bounded by the
           retirement record, human-disposition independence in step 3; the §22 discriminators
           for both; (b) workflow execution and verification layer and the doctrine-realization
           objective; (c) persistence, derivation, concurrency and migration; (d) Protocol
           7.2.1 inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 08a3a7cfdc97e7d9c406653a96aa22f848eee0ec (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72, 62C0B24,
           203A42B; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; each revision-16 mechanism (anchor, succ*,
           where, own-check salvage, authorship) attacked as a new input to the decision
           "when does a failing assessment stop counting", on frames, nested subjects,
           content relocation, uncovered regions, execution closures and absorbed content;
           prior-finding re-derivation; exact-candidate structural tests, whitespace check
           and bounded model check in all requested modes
    REVIEWER: Claude Opus 5.5 (model id claude-opus-5-5), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-16.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-A414588-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.26-§27.27), the model check's green result and every prior verdict as hypotheses.

The two blockers below are deductions from the proposed contracts, not observed SSDS runtime failures. Their asserter is the reviewer named above; their disposition is **OPEN** against the exact candidate. This record is their canonical home. Revisit after the D3 owner repairs the search scopes of §6.6 (with §6.5, §6.9 and §10) and the authorship rule of §6.6 and §6.8 step 3, regenerates §0.1, §22 and §27 from those rules, and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable here. It keeps separate “the **evidentiary target** (proposition/invariant evaluated) and **execution dependency**”, says “A valid failing observation is evidence”, forbids resolving disagreement by “serialized record position”, and requires that “An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” The [workflow owner][workflow] says “when a claim relies on independence, record material common-mode dependencies”. A D3 design in which a failing assessment follows the evaluated content wherever governed authority carries it, and in which independence is credited only on positive knowledge, satisfies all of these. Both blockers lie in the candidate's concretization, which is D3.

The stakeholder record (blob `edbf40da…`, unchanged) supports what the workplan attributes to it. SD-5 and SD-6 accept the revision-5 principles and an aspiration that is measured, not claimed; SD-8 directs this same-family sub-agent cycle “until all remaining blocking issues are closed”. Nothing in the candidate claims that a sub-agent PASS accepts the architecture (§25 items 11-12).

## Verdict

**NO-PASS.** Two blockers remain, both introduced by revision-16 repairs:

- **A — the new search scopes under-approximate where the evaluated claim lives.** Revision 16 replaced claim-unit membership with an anchor plus admitted region transfers (`succ*`) and confined presence to per-role scopes (`where`). Each of the four new inputs is narrower than the set of subjects that carry the evaluated content: the anchor is recorded in a frame that may never be enacted; it is singular although subjects nest; `succ*` follows only region transfers, not content relocation; and the execution scope is read from the current closure, which itself reads S2 currency. In each case a failing assessment stops counting while the content it evaluated is unchanged and still accepted.
- **B — independence is credited when the claim's authorship is unknown.** The claim's author is now “the set of actors whose admitted records authored the evaluated target content”. For absorbed content that set is empty, so the human who wrote the claim passes the independence test and disposes of the dissent against it, with no common-mode dependency recorded.

Revision 16 genuinely closes `203a42b` A on the trajectories that Review named (shrink, move into an untargeted sibling leaf, split with retarget, removal of the `EVIDENCES` relation, D1/D2 floor before the first pass) and `203a42b` B on its trajectory (the unauthorized `supersedes` is refused). A is the seventh consecutive appearance of the family “what can make a failing assessment stop counting”; per the [convergence owner][convergence] it is routed here as one family-level problem with four sibling trajectories, not as four findings.

Requested checks: the four routing tests pass; `git diff --check` is clean; the model check (unchanged since revision 15) is green at depths 4 and 5 (23/23 discriminators; 1,879,651 transitions at depth 5, matching §0.1) and red under `REV14=1`, `REV13=1`, `REV12=1`, `REV11=1` and `REV10=1`, each failing owner-grounded properties (P7 and Q in all five; P8 under `REV14`; P5 under `REV12`; P1 under `REV10`), not only the oracle. The model contains no anchor, `succ*`, `where`, frame, nesting, authorship or Admission, so it can see neither blocker. None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — the revision-16 search scopes narrow adversity below the content's real locations

**Owner text at the candidate.**

- §6.6: “It also records each failing assessment's **anchor**: the subject that contained the evaluated target at the assessment's admission, in its frame.” `succ*(s0) = s0 and every effective subject that received regions of scope(s0), or of a subject in succ*(s0), by an admitted structural change -- S0 fold over Σ`; `about(a-, s) ⇔ s ∈ succ*(anchor(a-))`; `where(p, a-) = ⋃ { scope(s) : about(a-, s) }` for the target premise, `= the specification's execution closure` for an execution premise “(its fallback included)”; `adverse(s, e)` requires `bears(a-) ∧ the target premise is present within scope(s)`.
- §6.6 prose: “`about`, `where` and `bears` read only observed trees at admitted positions, the effective structure and record syntax, so they are S0”; “A scope change that moves the evaluated content into another subject adds that subject as a successor, and the dispute follows the content there”; “Copies elsewhere (archives, vendored code, quotations) neither keep failing evidence bearing nor attach it to their subjects”; “A failing assessment therefore stops counting only when content an evidentiary premise evaluated changes without equivalence, or by disposition”; “A failing assessment made in the frame of a never-integrated candidate […] if its evaluated content is present in its anchored subjects in `D_n`, `qual` reads it there too.”
- §6.9 Rebase: “Bearing follows the same mapping: a frame-`X` failing assessment bears for `X'`, and after `X'` integrates, exactly when the content its evidentiary premises evaluated is present in their roles; it is never dropped because `X` itself was not integrated.”
- §6.1: “A subject may contain nested subjects (a carve-out, §12.2); its scope, and so its revision, still covers their content.” §12.2: “`P` keeps its frozen scope, which still includes `A`'s bytes, and so keeps its tenure.”
- §6.5 closure: “if not exists `X_i` in `chain(u)` with **current** `COMPLETENESS(X_i, R)` for every member class: `W := X_m`”.
- §10: “Failing evidence whose evaluated content […] changed without an admitted equivalence never qualifies the current claim, and a structural change alone never counts as such a change; any other failing evidence does, until it is disposed of (§6.6).”
- §1.2: “mechanically decidable only conservatively -> deterministic machinery, answered by sound over-approximation (never under-approximation)”.

**Trajectories (every step locally compliant).** Common setup: D2 subject `s` contains claim leaf `c` (“p q”); specification `σ EVIDENCES c` gives obligation `e`; `X` assesses PASS (`a+`) and `Y` assesses FAIL (`a_Y`) on a tolerance-interpretation disagreement over one observation. Where the trajectory needs a second subject, `t` is another D2 subject.

1. **A1 — frame-local anchor.** A reorganization task proposes transformation `X = (B, C, ∅)` whose manifest moves leaf `c` from `s` to `t` (no content byte changes; `rev(c)` is unchanged because structural declarations are excluded from `rev`). Evidence is rerun on the merged tree (§6.8 step 7), and `Y`'s failing assessment `a_Y` is made in frame `X`, so its anchor is `t`. The integrating request is rejected because `a_Y` defeats its discharge, and step 6 salvages `a_Y` (it passes its own checks). In `D_n`, `c` is still in `s`; `succ*(t)` over `Σ_n` is `{t}`, because `s` never received regions of `t`. So `where(target) = scope(t)`, the target is absent there, `bears(a_Y)` is false, `about(a_Y, s)` is false, and `a_Y` is inert: `qual(s)` does not read it, `ev(s, e) = T` from the earlier pass, no `disputed` label, no adjudication obligation, and no floor item (it never bore at an admitted position of `D_n`). Variant: a later iteration `X2` of the same obligation moves `c` to `u` instead; in frame `X2` and after integration, `u` is not in `succ*(t)`, so the claim lands in `u` unqualified. Both contradict the §6.6 and §6.9 sentences quoted above.
2. **A2 — singular anchor under nesting.** Part `A` of `P` is promoted (§12.2); `P` keeps its frozen scope including `A`'s bytes, so `c` lies in both subjects. If `a_Y` is admitted **before** the promotion, the anchor is `P`, `A` is a successor, and both are qualified. If it is admitted **after**, “the subject that contained the evaluated target” has two candidates; the natural reading `subj(c) = A` makes `about(a_Y, P)` false, so `qual(P)` and, where `e` is required for `P`, `ev(P, e) = T` while `ev(A, e) = P`. The same records in a different order yield a different qualification of `P`, whose holistic acceptance still covers the disputed claim and which every validity reliance on `P`'s remaining parts routes to.
3. **A3 — relocation without a region transfer.** (i) One integrating request cuts “p q” from `c` and pastes it into a leaf `c'` of `t`, retargeting `σ` to `c'`: no structural change, so `t` is not a successor; the target is absent from `scope(s)`, `bears(a_Y)` is false, and the rerun on `c'` passes under `X`'s reading. (ii) The same arises from a plain `git mv` of the file from a path matched by `s`'s path pattern into one matched by `t`'s, with the manifest untouched (§6.1 scopes are declared by “path patterns”). (iii) A structural route: one admitted change removes `c`'s region from `s` into the uncovered region, a later one declares it into `t`; `t` received regions from the uncovered region, not from `scope(s)`. In all three the proposition `Y` competently disputed is unchanged, now accepted in `t`, unqualified and unlabelled. §27.26 defends only “a structural change that moves regions”.
4. **A4 — execution search scope read from current, S2-dependent structure.** `where` for an execution premise is “the specification's execution closure (its fallback included)”, and §6.5 computes that closure from **current** `COMPLETENESS` judgments, which are S2 values (`current(x)`). So either `where`, `bears` and `adverse` are not S0 (the stratification, the “constants” premise of §6.6 Uniqueness and the support graph, which has no edge from `valid`/`current` to these completeness judgments, are then all mis-stated, and the one-pass evaluation can read a value before it is computed), or the implementer must invent a different closure. Under the current-closure reading: `Y`'s failure exercised module `m`, positively named by `σ`. `σ` is edited to stop naming `m` (an interpretive move, which §6.6 lists among “What does not end a disagreement”); the edit stales `σ`'s chain completeness, which still holds via the fallback, but a fresh, correct `COMPLETENESS` judgment on `σ`'s new scope narrows the closure, `m` falls outside `where`, and `bears(a_Y)` is false although `m` is unchanged and still the production code.

**What it violates.**

- The [evidence owner][evidence]: “Keep separate the **evidentiary target** (proposition/invariant evaluated) and **execution dependency**”; “A valid failing observation is evidence”; “Do not suppress contradictory admissible observations to manufacture a pass”; “Do not resolve material assessment disagreement by […] serialized record position” (A2); “An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.”
- The [architecture owner][architecture]: “When an architectural concept carries normative meaning, define it before dependent invariants use it”. The anchor's cardinality and frame, the start position of the `succ*` fold, “received regions” for nested promotion, and which closure `where` reads are all undefined.
- The candidate's §1.2 over-approximation rule, S4, C8 (A4), §10's “any other failing evidence does” qualify, and its own §6.6 and §6.9 sentences quoted above.

**Earliest owner.** D3 §6.6 (anchor, `succ*`, `where`), with §6.5 (closure currency), §6.9 (frame mapping) and §10. Not Manual: §21 item 5 lists “anchors and successors, search scopes” for the Manual, but the candidate states at D3 both the rule and the intended outcomes, and they contradict each other.

**Minimum repair direction.** Apply one family rule, which `203a42b` §5 already stated, to every input: *a premise's search scope, and the set of subjects a failing assessment qualifies, may be narrowed only by an immutable record fact, never by current structure, current relations, frames that were not enacted, or S2 values.* Concretely, without new record kinds:

- record the anchor as a **set**: every subject whose scope contains the target at admission, in the record's frame **and** in the admitted state at its base; state the position from which `succ*` folds;
- `about(a-, s) ⇔ s ∈ succ*(anchors(a-))`, or the evaluated target is absent from every subject in `succ*(anchors(a-))` and present within `scope(s)`. A claim that stays home keeps N4's benefit (stray copies ignored); a claim that leaves home by any route is followed, restrictively, which is what §1.2 requires;
- fix the execution search scope at admission as a record fact (the closure as computed then), unioned with the current one; no `current()` is read in S0.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers, each followed by a passing rerun and assessment: A1 (rejected restructuring frame; re-iteration to a third subject); A2 in both orders, with `ev(P, e) = ev(A, e)`; A3 (i)-(iii); A4 (specification edit plus fresh completeness judgment); contrasts: a genuine edit of the claim's bytes with no other copy ends bearing; a stray archive copy of a claim that stayed home neither keeps bearing nor qualifies the archive.

### B — the authorship rule credits independence where authorship is unknown

**Owner text at the candidate.**

- §6.6: “Every disposition, including the failing assessor's own reassessment, must be independent of the claim's author. […] The claim's author is the set of actors whose admitted records authored the evaluated target content. For an authenticated human judgment, independence means that the human is not among them.”
- §6.8 step 3: a disposition satisfies independence “(for a disposition by an authenticated human, when the human is not among the claim's authors, or under the owner exception of §6.6 with the common-mode dependency recorded)”; for agents, “its lineage is disjoint from the author's”.
- §6.8 Absorption: “its only content is `obs` […]”; §11.1: content “already on the live integration ref is absorbed mechanically”.
- §7.5: “Independence, however, is credited only to positively attested lineage. An `UNKNOWN` judgment is recorded but satisfies no independence requirement (A9).” A5: “no actor reviews or accepts its own work”. A9: “material common-mode dependencies are recorded”.

**Trajectory.** Human `H` edits the claim of NATIVE D2 subject `s` directly on the integration branch, as §11.1 permits. Admission absorbs it; a principal's intake `ABSORB` disposition and human `K`'s R3 acceptance follow. Neither of those records, nor the absorption record, *authored* the content, so the author set of the evaluated target is empty. `X` passes, `Y` fails. Policy names `H` and `K` as qualified humans. `H` records an R3 `IMMATERIALITY` judgment covering `a_Y`. Step 3 finds `H` “not among the claim's authors” (the empty set), credits the disposition as independent and records no common-mode dependency. `eff = current = T`, so the qualification, the `disputed` label and the adjudication obligation go. The same holds for an agent disposition on an R2 subject, where “disjoint from the author's” lineage is vacuously true for absorbed content. Legacy imports, manual merges and restored content (§11.3) all have this shape.

**What it violates.** The [workflow owner][workflow]: “when a claim relies on independence, record material common-mode dependencies”. Also the candidate's A5 and A9, its own §6.6 rule above, and the asymmetry with §7.5, where unknown lineage on the disposer's side fails closed but unknown authorship on the author's side fails open (C5 in spirit). The evidence owner lets the owner adjudicate, so the defect is the false *independence* credit and the missing common-mode record, not the owner's authority to decide.

**Earliest owner.** D3 §6.6 (decision class and independence), carried into §6.8 step 3.

**Minimum repair direction.** One clause: where any part of the evaluated target content has no admitted authoring record, a disposition is credited as independent only with the disposer's authenticated attestation of non-authorship (an R3 record for a human), or under the owner exception with the common-mode dependency recorded; for agents, an unknown author lineage is never disjoint.

**Required discriminators:** the trajectory above, which must leave the claim qualified or record the common-mode dependency; the same with an agent on an R2 subject; contrast: `K`, with a non-authorship attestation, disposes and the qualification lifts.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged since `62c0b24` N1 (§0.4; stakeholder record, “Not covered”). The handoff independently binds this Review to 7.2.1, and the release state at the candidate names 7.2.1 accepted-current. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — the retired-key bound is self-attested

Step 3 now accepts a retired-key envelope only “for an envelope issued before that key's retirement record”. The envelope (§7.5: task identity, bound obligation, role, contract revision, route, lineage class) carries no issue position, and task issue lives only in the Dispatcher's operator journal (§6.3). Any issue field would be signed by the retired key itself, so whoever keeps that key can backdate. The effects are restrictive (never-lost records only). Repair: bind to a ledger fact, for example a list or root of outstanding envelopes recorded in the retirement record. Earliest owner: §6.8 step 3; Manual item 14.

### N3 — step 3 does not state supersession authority

S0 reads `superseded(x)` “(authorization was checked at admission)”, and step 6 now refers to a never-lost record's “own […] step-3 checks: […] authority for every `supersedes` field and target it names”. Step 3's text has no such item; the only statement of who may supersede is §6.6's list of disposing records. Implementers will probably read it in, but the check that closes `203a42b` B should be written where it is enforced. Earliest owner: §6.8 step 3 (editorial at D3; detail for Manual item 3).

### N4 — a salvaged failing assessment's own realization

Never-lost records are reports, challenges and failing assessments; observations are not. When the realization a failing assessment assesses is co-submitted in the rejected request, the assessment's own reference check either fails, so it is lost, or passes against the request, so it is admitted with a dangling `real(a-)`, from which no premises or anchor can be computed. State that a salvaged failing assessment carries the observation it assesses, or that observations are admitted before their assessments. Earliest owner: §6.8 step 6; Manual item 6.

### N5 — the execution half of the stray-copy repair is mostly absent

`where` for execution premises includes the closure's fallback, which is the whole governed tree whenever no completeness judgment exists (the ordinary `UNBOUNDED` case, §6.5). A byte-identical copy of the evaluated code anywhere then keeps a repaired failure bearing, as before. §0.1's N4 row and the §22 case “outside the execution closure” overstate the repair; the effect is restrictive. Earliest owner: §0.1, §22; resolved together with A4.

### N6 — about-edges added by structural changes are not checked at step 5

The support graph now has edges from every subject `about` names to the dispositions of those failing assessments. A structural change that adds a successor adds such edges. Step 5 examines only “the edges of existing records whose `validity` endpoints the request's structural changes re-route through `subj`”. A disposition whose basis has a `validity` entry on the new successor then forms an unchecked cycle. It evaluates to `F`, which is restrictive, but “A cycle found at derivation can arise only from corrupted input” remains false in that case. Earliest owner: §6.8 step 5.

### N7 — residual “claim unit” text in §10

§10 still defines a specification as “`EVIDENCES` -> claim unit” and the realization's target as “claim unit revision”, and its rule “any other failing evidence does [qualify]” contradicts the `where` narrowing (A3). Editorial once A is repaired. Earliest owner: §10.

### N8 — the convergence owner is cited for a rule it does not state

§27.26: “Since revision 13 the family's repairs have narrowed boundaries of one abstraction […] which the convergence owner treats as convergence, not recurrence of the same defect.” The [convergence owner][convergence] contains no such rule. It says instead: “Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism, patch-on-patch repair […]”, and “route one family-level problem rather than intentionally returning one cheap sibling per review cycle”. Revision 16 is additive (anchor, `succ*`, `where`, own-check salvage), and this Review again finds the family. Remove the attribution, and treat the repair of A as a family re-derivation tested against the one rule above, not as a further patch. Earliest owner: §27.26.

### N9 — the model check's default mode is labelled `REV15`

At the revision-16 candidate, the unchanged script reports “mode REV15”. Cosmetic, but a reader may take it for a stale run. Earliest owner: the model check.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 203A42B

| Finding | Disposition | Basis |
|---|---|---|
| A — shrink, move into an untargeted sibling leaf, split with retarget | **Closed** | Anchor `s`, target bytes still within `scope(s)`: `bears` and `adverse(s, e)` hold |
| A — removal of the only `EVIDENCES` relation (`644eb72` B regression) | **Closed** | `about` reads no specification targets; `qual` reads `e` “whether or not `e` is still required” |
| A — D1/D2 floor with structural change before the first pass | **Closed** | “where any subject a failing assessment is about is D1 or D2” is decided from the anchor |
| A — family “structural or locational change ends adversity” | **Open** | Blocker A (A1-A4) |
| B — unauthorized `supersedes` through the salvage | **Closed** | Fails its own step-3 check and is refused; S0 never reads it (N3 editorial residue) |
| N1 adoption provenance | **Partly closed** | Unchanged (N1) |
| N2 salvage before authentication; unbounded retired-key envelopes | **Partly closed** | Record-by-record checking closes the sibling route; the retirement bound is self-attested (N2) |
| N3 §6.6 and step 3 disagreed | **Closed** for the contradiction | Step 3 now carries the owner exception; the new authorship rule fails open (Blocker B) |
| N4 stray copies | **Closed** for a claim that stays home; **regressed** into Blocker A3 for one that leaves; **open** for execution content (N5) | |
| N5 declarations and unavailable bytes | **Closed in text** | Declaring-unit identity abstracted; unavailable bytes count as present; tree retained (Manual items 5, 14) |
| N6 support-graph edges changed with content | **Partly closed** | Edges now change only with records; structural successors escape step 5 (N6) |
| N7 model cannot see A or B | **Recorded**; §22 adds discriminators for A and B | None for A1-A4 or Blocker B |

### Earlier Reviews

The `203a42b..a414588` workplan diff touches §0, §0.1, §6.6 (anchor, `succ*`, `about`, `where`, `present`, `adverse`, prose, independence, floor), §6.8 steps 3 and 6, §7.9, §21 items 5 and 14, §22, §27.26-§27.27 and §28, plus six lines of the authority index. No `source/`, `dist/`, `orchestrator/`, test, model-check, release-state, PEM or stakeholder-record path changed (verified with `git diff --stat`).

- **62C0B24 A (boundary growth; merge with retarget; adopted delta): closed.** Growth and intra-subject merge keep the target within the anchor; a cross-subject merge makes the destination a successor.
- **644EB72 A and B: closed** (B as above).
- **4C35D92 A1-A2, 97E753F A, B1, B2, 124B0B7 A, FFBAD17 A: closed.** `ev`, `undisputed`, `disp`, `eff` and `contested` are unchanged; P1-P8 and Q are green to depth 5.
- **FB3E542 A: closed**; `bind(j)` is unchanged. **FB3E542 B: partly closed**, through blockers A and B.
- **Strata.** S1 and S2 are unchanged. S0 remains a function on the target branch of `where`; on the execution branch the candidate's S0 claim is false or underdefined (A4).

The remaining 730490D, AC71FA9, F3608F5, 8A75346, 441CF5C and F9D9DE8 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| `203a42b` A trajectories (shrink, sibling leaf, split with retarget, `EVIDENCES` removal); passing rerun | Hold |
| Scope change accepted for both subjects moving the evaluated content `s -> t` | Holds: `t` is a successor; `s` drops out once the target leaves its scope |
| Merge of `c` (in `s`) with `d` (in `t`) into a unit of `t` | Holds (`t` received regions of `s`) |
| Demotion of `s` into a new composite `P` | Holds (`P` received `s`'s regions) |
| Promotion of `A` out of `P` after an assessment anchored at `P` | Holds (`A` is a successor) |
| Assessment admitted after that promotion | **Fails** (A2) |
| Restructuring frame rejected or abandoned; re-iteration with a different destination | **Fails** (A1) |
| Clean rebase with the same structural delta, then integration | Holds (§6.9) |
| Cut-and-paste of the claim into another subject; `git mv` across path-pattern scopes | **Fails** (A3) |
| Region laundered through the uncovered region | **Fails** (A3) |
| Specification edit dropping the failing code, plus a fresh completeness judgment | **Fails** (A4) |
| Specification edit alone | Holds: chain completeness goes stale, the fallback keeps the code in scope |
| Edit of the claim's bytes, archive copy elsewhere | Holds: bearing ends; the copy is ignored |
| Code fix with a frozen copy and an `UNBOUNDED` closure | Keeps bearing (N5, restrictive) |
| Unauthorized `supersedes`, rejected at step 3, then own passing reassessment | Holds: refused |
| Role-forbidden failing assessment, challenge or report | Holds: refused, inert |
| Request rejected for a sibling record's schema failure | Holds: record-by-record |
| Salvaged failing assessment whose realization was co-submitted | Underdefined (N4) |
| Backdated envelope on a retired, uncompromised key | Accepted (N2, restrictive) |
| Absorbed claim; its human author disposes of the dissent | **Fails** (B) |
| Single-human project, author disposes as owner | Holds: step 3 now carries the exception, common mode recorded |
| Structural successor whose disposition relies on its validity | Restrictive cycle outside step 5 (N6) |
| Workflow layer, publication, frame, intake and migration trajectories of earlier records | Hold as recorded; untouched by revision 16 |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Revision 16 removes claim-unit membership from derivation and unconditional salvage, and adds one recorded field (the anchor), an S0 fold (`succ*`), per-role search scopes and own-check salvage (§27.27). No primitive, record kind, store or component is added. Own-check salvage is the minimum repair of `203a42b` B. The anchor is sound in kind but defined with the wrong cardinality and frame, and `where` adds two mutable inputs. The repairs of A and B above remove inputs rather than adding mechanisms.

**Convergence.** `203a42b` §5 proposed one rule and asked that every S0 fact read by `adverse`, `qual`, `disp` and the floor be tested against it. Revision 16 enumerated claim-unit membership, obligation existence and supersession syntax, but not the frame of the anchor, nesting, content relocation or the closure's currency, and each of those is where A arises. The family is now seven Reviews deep. The [convergence owner][convergence] makes re-derivation mandatory before another additive repair (N8).

**Predecessor comparison.** Revision 16 did not touch §16.2 or §18. Blobs verified at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. The uncovered later interval proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model check is green in all 23 discriminators while A and B hold; it has no anchor, succ*, where, frame, nesting, authorship or Admission, and the §22 list has no case for A1-A4 or B.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; preserved by §24; their byte copies feed N5.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair at the owning D3 rules (§6.6 search scopes, authorship) and regenerate §0.1, §22 and §27 from them.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 16.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current, with public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff; `source/PROTOCOL_VERSION` is 7.2.1 at both. The diff changes no §0.4, §19 or §24 text and no `source/`, `dist/`, `orchestrator/`, release-state or PEM path, so the §0.4 obligation table and §19 landing points stand. The inherited evidence doctrine is not yet realized at A, and the inherited independence doctrine at B.

## 6. Qualification-program adequacy

§22's disagreement group now carries the `203a42b` discriminators: shrink, sibling leaf, split with retarget, `EVIDENCES` removal, the D1/D2 floor, the unauthorized `supersedes`, role-forbidden records, salvage with fields, the stray copy and the merge with an authored relation. It cannot discriminate A or B. Every structural case keeps the claim inside its anchor or moves it by a region transfer; every frame case integrates or keeps the same structure; no case nests subjects, relocates content by edit or rename, passes through the uncovered region, narrows an execution closure, or disposes of absorbed content. The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 16 as written is such a concretization for A and B: every listed §22 case and every model-check property stays green. Add the discriminators named in §1.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `08a3a7cf…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `88a59da`, were excluded.
- **Owners read** at `aaeaf8b6` with `git show`: the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge); architecture (read first: admissibility, “one authoritative representation/state”, “define it before dependent invariants use it”); evidence (target vs execution dependency; applicability; Assessment disagreement; suppression); workflow (Optional independent cognitive trajectories: process vs epistemic independence, common-mode recording); testing (smallest plausible wrong concretization); convergence (family routing, mandatory re-derivation, search-strategy switch); the kernel's Challenge text. Release identities resolved from `PROTOCOL-RELEASE-STATE.yaml` at the candidate (the file at `aaeaf8b6` itself still lists 7.2.1 as an unfrozen candidate, as expected for that commit).
- **Candidate read.** §0.1, §1-§2, §5, §6.1-§6.9 in full, §7.5, §10, §11.1-§11.3, §12.1-§12.2, §15.1, §21 items 5 and 14, §22 (disagreement group), §27.26-§27.27 and §28; the full `203a42b..a414588` diff, including the authority index; the stakeholder record; the routing test; and the model-check output.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.039 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check 203a42bd… a4145880…`: **exit 0**, no diagnostics.
- **Model check**, depth 4 (76,366 transitions in every mode):
  - default mode (labelled `REV15`): **0 failures, 23/23 discriminators as expected, exit 0**;
  - `REV14=1`: **1,266 failures (P7 60, P8 148, Q 420, O 638)**; one discriminator differs (`62c0b24` A); **exit 1**;
  - `REV13=1`: **11,492 failures (P7 872, Q 3,628, O 6,992)**; three differ; **exit 1**;
  - `REV12=1`: **11,944 failures (P5 81, P7 872, Q 3,797, O 7,194)**; five differ; **exit 1**;
  - `REV11=1`: **11,900 failures (P7 872, Q 3,786, O 7,242)**; eight differ; **exit 1**;
  - `REV10=1`: **13,028 failures (P1 262, P7 872, Q 3,620, O 8,274)**; nine differ; **exit 1**.
- **Model check**, depth 5, default mode: **1,879,651 transitions, 0 failures, 23/23 discriminators, exit 0** (2 min 16 s), matching §0.1.

  Each sensitivity mode fails at least one owner-grounded property (P1-P8 or Q), not only the oracle.
- **A and B.** Deductive, from the quoted contract text. Neither is representable in the model's vocabulary, so no scratch reproduction was attempted.
- **Identities.** Verified the predecessor blobs, the release-state identities, the PEM blob identity and `origin/main`, the stakeholder-record blob and the changed-path list above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, structural and content relocation, frames, admission and salvage, independence, disagreement and closure. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed through multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering, evidence and workflow doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, run on the working-tree file whose blob equals the candidate's, failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for historical evidence routes (`55c08526…`, `81375d81…`). This checkout is a **shallow clone** (`git rev-parse --is-shallow-repository`: `true`). That is an environment limitation, not a PEM defect and not a pass.
- **Remote state.** `origin/main` is the local tracking ref. No fetch was performed and no remote-state claim is made.
- **Readings and Manual compositions.** A1 assumes evidence for an obligation is rerun and assessed in a restructuring frame, as §6.8 step 7 and §6.9 provide. A2 assumes the singular anchor is read as `subj` of the target unit; the other reading moves the defect to the inner subject only if “received regions” excludes nested promotion, which the candidate does not define. A3 (ii) assumes path-pattern scopes resolve against the current tree, as §6.1 states. A4 assumes the §6.5 closure is the one `where` names. B assumes absorption, intake and acceptance records are not “authoring” records, as their definitions indicate. N2-N4 assume Manual compositions (items 3, 6 and 14).
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The [workflow owner][workflow] says: “Separate context improves process independence but not epistemic independence when agents share model, source corpus, toolchain or oracle”.

There is concrete evidence of that dependency in this cycle. The `203a42b` Review (same family) proposed the “immutable anchor plus content” option, “execution content within the specification's current execution closure” and “define claim authorship by the content's authoring records”. Revision 16 adopted the first in part and the other two verbatim, and A1-A2, A4 and B sit exactly there. Same-family reviewers both find and seed this family's defects. A different family might frame it differently.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair of the search scopes (§6.6 with §6.5, §6.9 and §10; A) and of the authorship rule (§6.6 and §6.8 step 3; B), done as a family re-derivation against one rule, with §0.1, §22 and §27 regenerated from it and a replacement immutable candidate. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/a4145880878b71c1cb3134f003d83b519e206f56/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[architecture]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/architecture-and-design.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md

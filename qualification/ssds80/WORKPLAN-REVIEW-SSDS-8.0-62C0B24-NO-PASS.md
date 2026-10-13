# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 14

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 62c0b24533f31b933f698c6f376a12ed689759f9
    SCOPE: whole proposed architecture; (a) the revision-14 repairs: the never-lost class
           (reports, challenges, failing assessments) at both Admission clauses, the step-6
           salvage and the step-7 task-state exemption; qual(s) over every obligation an
           admitted failing assessment names, in validity and §7.4 discharge, and retirement
           as a non-disposition; independence in the eff equation; admissibility against the
           realization's specification revision; the D1/D2 floor keyed on having borne at
           some admitted position; the extended bounded model check (P7, challengeable
           equivalence, non-independent superseders, REV13 sensitivity); (b) workflow
           execution and verification layer and the doctrine-realization objective;
           (c) persistence, derivation, concurrency and migration; (d) Protocol 7.2.1
           inheritance reconciliation
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 2b4046b3c81d44380498fb060d5e890cb08ecc2c (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction; the enumeration the 644eb72 Review asked
           for, performed independently: every route by which a submitted or admitted
           failing assessment can stop affecting validity and discharge (evidentiary move,
           disposition, inadmissibility, obligation change, non-admission, frame, loss),
           each tested for whether it is an evidentiary move in the owner's sense or an
           accountable disposition; attack of each revision-14 repair as a new mechanism;
           prior-finding re-derivation; exact-candidate structural tests and bounded model
           check in all requested modes
    REVIEWER: Claude (same model family as the author), a fresh-context sub-agent launched
           by the authoring session from REVIEW-HANDOFF-SSDS-8.0-REVISION-14.md (stakeholder
           SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-62C0B24-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.22-§27.23), the model check's green result and every prior verdict as hypotheses.

The blocker below is a deduction from the proposed contracts, not an observed SSDS runtime failure. Its asserter is the reviewer named above; its disposition is **OPEN** against the exact candidate. This record is its canonical home. Revisit after the D3 owner decides, at §6.6, what moves of a claim unit end adversity, regenerates §0.1, §22, §27 and the model check from that rule, and freezes a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable here. It separates the “**evidentiary target** (proposition/invariant evaluated)” from execution dependency, says “A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority”, requires `review-required` “when applicability is uncertain”, forbids resolving disagreement by “latest-editor order […] or serialized record position”, and requires that “supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement”. A D3 design that ends adversity only when the evaluated target or the named execution content actually changes, or by an accountable disposition, satisfies all of these together. The blocker below lies in how the candidate concretizes “governed-claim revision”, which is D3.

The stakeholder record (blob `edbf40da…`, unchanged since `644eb72`) supports what the workplan attributes to it. SD-5 and SD-6 accept the revision-5 principles and an aspiration that is measured, not claimed. SD-8 quotes the instruction verbatim (“until all remaining blocking issues are closed”) and directs this same-family sub-agent cycle. Nothing in the candidate claims that a sub-agent PASS accepts the architecture; acceptance of objectives, product scope and the major change stays with the stakeholder (§25 items 11-12; [workflow owner][workflow]).

## Verdict

**NO-PASS.** One blocker remains:

- **A — a byte-preserving structural re-partition of a claim unit ends adversity without an evidentiary move or a disposition.** `bears` keys the claim-side evidentiary premise on the *unit's* revision, and a unit's revision changes whenever its scope changes, even when no byte of the claim, of its subject or of the executed code changes. A governance-neutral manifest change, admitted without any judgment about the evidence, therefore drops every bearing failing assessment on that claim from `adverse`, `qual`, the adjudication obligation and the `disputed` label, while the accepted authority revision stays exactly what it was. No equivalence route exists to prevent it when the change retires the unit's identity.

Revision 14 genuinely closes both `644eb72` blockers on their stated trajectories: the never-lost class now governs the step-6 salvage and step 7 for failing assessments, and `qual(s)` keeps a retired, split or retargeted obligation's disagreement until a disposition. The `eff` equation, the admissibility anchor and the floor key are repaired as found. Blocker A is the claim-side sibling of `644eb72` B: B ended a disagreement by moving the *obligation*; A ends it by moving the *container of the claim*. It needs one rule at §6.6, not a new mechanism.

Requested checks: the four routing tests pass; `git diff --check` is clean; the model check is green at depths 4 and 5 (21/21 discriminators) and red under `REV13=1`, `REV12=1`, `REV11=1` and `REV10=1`, each failing owner-grounded properties (P7 and Q in all four; P5 under `REV12`; P1 under `REV10`), not only the oracle. The model represents every claim or execution change as one abstract `MOVE`, so it cannot distinguish a content move from a structural re-partition, and it cannot see A (§6 below). None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### A — structural re-partition of the claim unit is treated as an evidentiary move

**Owner text at the candidate.**

- §6.6 role table: “governed-claim revision (the realization's target); execution content the specification positively names […] | **evidentiary premise** | a move ends bearing unless an admitted equivalence links the revisions: the observation is then about something else”.
- §6.6: `bears(a-) ⇔ every evidentiary premise (u, r, k) of real(a-) passes, in its role and frame: r = cur(u), or r reaches cur(u) through admitted EQUIVALENCE judgments on u of class k`; `adverse(s, e) = { failing assessments a- admissible for e on s's claim unit : bears(a-) }`; `qual(s) = ⋀_{e named by an admitted failing assessment on a claim unit of s} undisputed(s, e)`; “S3 derives an adjudication obligation for each adverse assessment with no standing disposition”. §10: the realization's “**target** (claim unit revision)”.
- §6.1: “`rev(u, T)` = hash(content identity of `scope(u)` in tree `T`, semantic declarations within `scope(u)`). […] pure structural boundary markers carry no relation payload and are normalized out. […] **Structural declarations** are excluded from `rev`, but they determine scope”. A quarantined delta is “**governance-neutral**: a re-partition of leaves inside one subject's unchanged regions into parts of that subject with its kind and domain.”
- §6.7: “Machinery decides equivalence only for byte identity and rule-defined conservative normalizations. […] An equivalence judgment relates two revisions of one unit.” §12.2: “An equivalence judgment relates revisions of one unit; it never relates different scopes.”
- §12.2: “Structural refinement makes no semantic claim. A byte-preserving refinement leaves the subject's scope identity, content identity, signature and tenure unchanged […] The subject's revision is therefore unchanged and its acceptance remains valid”.
- §15.7: “Agents may propose structural declarations in the unit manifest as ordinary content; those take effect only through Admission (§6.8 step 4).” §21 item 12: “policy for mechanical adoption of governance-neutral deltas”.
- §6.6 decision class: dispositions are R2, “for a claim unit that is D1 or D2 authority they are R3”.
- §22, as the intended outcome: “These must not qualify the claim at all: a failing assessment whose claim revision or named execution content moved with no admitted equivalence”.
- The candidate's own stated asymmetry (§6.6): “currency over-approximates which moves remove *support*, and `bears` under-approximates which moves remove *adversity*.”

**Trajectory (every step locally compliant).**

1. Subject `s` (a D3 design document, or D1/D2 authority) has leaf parts `c` (the claim unit) and `d` (an adjacent remark). Specification `σ EVIDENCES c`. Realization `ρ` (deterministic) is assessed PASS by `X` and FAIL by `Y` (a tolerance-interpretation disagreement on the same observation), or seeds 1 and 2 disagree. `ev(s, e) = P`, the evidence is labelled `disputed`, and an adjudication obligation is open.
2. An implementer whose item write scope includes the manifest entries of `s`'s parts (§15.7 permits this) moves the boundary between `c` and `d` so that `c` absorbs the remark: one sentence changes leaf. No byte of the repository's content changes except a structural marker, which §6.1 normalizes out. (Variants: merge `c` and `d` into a new leaf `cd`, retargeting `σ` as step-4 reference checking then requires; or the same re-partition arrives as a foreign manifest edit, is quarantined, and is adopted as a governance-neutral delta, mechanically if policy so chooses under §21 item 12.)
3. Admission validates it as a well-formed authored structural change (§6.8 step 4). `scope(s)`, its bytes, its semantic declarations, its tenure and so `rev(s)` are unchanged; `s`'s acceptance stays current. But `rev(c)` changes, because `c`'s scope changed. In the merge variant `c` is no longer an effective unit at all.
4. `bears(a-)` now fails on the premise `(c, r_c)`: `cur(c) ≠ r_c`, and no machinery equivalence covers a scope change. In the merge variant no equivalence judgment can even be recorded, because equivalence “never relates different scopes”. So `adverse(s, e) = ∅`, `qual(s)` reads nothing (and in the merge variant `a-` is not “on a claim unit of `s`”), the adjudication obligation disappears, and the `disputed` label goes.
5. `X`'s passing assessment is non-current too, so `valid(s) = F` until the derived rerun obligation is met. The designated runner realizes `σ` on the new revision of `c`; it produces the same observation. Whichever assessor the Dispatcher assigns judges it. If that assessor reads the tolerance as `X` did, `ev(s, e) = T`, `qual(s) = T`, `valid(s) = T`, and §7.4 discharge is unqualified. `Y`'s competent dissent has been removed by a manifest edit plus the identity of the next assessor. No disposition was recorded, nothing names `a-`, and for a D1/D2 claim no R3 judgment occurred (the floor's human-attention item survives by existence, but validity and discharge are unqualified meanwhile). For a D3/D4 claim nothing at all remains open.

**What it violates.**

- The [evidence owner][evidence]: “Keep separate the **evidentiary target** (proposition/invariant evaluated) and **execution dependency**”; “A valid failing observation is evidence. A stale failing observation is not admissible evidence against **current authority**” (the current authority here is the same accepted revision of `s` the observation was made against); “Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position. When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement. An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.” “Do not suppress contradictory admissible observations to manufacture a pass”.
- The candidate's S4 (“failing evidence whose realization still bears on the claim keeps it qualified until disposed of”) and S10 (“Content identity, scope identity […] are distinct facts; no mechanism infers a later one from an earlier one”): `bears` infers a change of the evaluated target from a change of scope alone.
- The candidate's own §6.6 decision class (R3 to dispose of a D1/D2 disagreement), the §12.2 principle that byte-preserving structure “makes no semantic claim”, and the stated asymmetry that `bears` must *under*-approximate which moves remove adversity. A structural move is exactly the kind of change that currency may over-approximate (the passing side going stale is conservative) but `bears` must not.
- The closure claims of §0.1 and §27.22 (“retirement is not a disposition”, “`qual` ranges over the obligation each failing assessment named, an immutable fact”), which the merge variant defeats by co-moving the claim unit.

**Earliest owner.** D3 §6.6: the evidentiary-premise row of the role table and the definition of `bears` (with §10's realization target). Not Manual: whether a structural change of the claim's container ends adversity is a semantic decision about disagreement, and §22 currently *requires* the permissive outcome.

**Minimum repair direction.** Decide the claim-side (and, for consistency, the named-execution-side) evidentiary premise on the content the realization evaluated, not on the identity or scope of the unit that currently contains it. Either option keeps `bears` in S0, keeps S2 monotone and adds no record kind:

- *Byte-anchored premise.* Admission records each evidentiary premise with the content identity of the regions `scope(u)@r` covered. `bears` passes it while those bytes are present unchanged in `T_n` and lie inside the claim units of one effective subject (or are linked by an admitted equivalence, as now). Byte identity is already a machine decision (§6.7). Currency of the *passing* side may stay on unit revision, which is the asymmetry the candidate already states.
- *Structural moves are not evidentiary.* A structural change (re-partition, merge, boundary move) that alters the scope or identity of a unit named as an evidentiary premise of a bearing, undisposed failing assessment leaves that assessment bearing, as retirement of an obligation now does; only a content move or a disposition ends it.

Then correct the §22 “must not qualify” clause so that it speaks of content moves, and state the rule beside “retirement is not a disposition”.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers:

- a live disagreement, then a boundary move that grows the claim unit by an adjacent sentence with no content byte changed, then a passing rerun and assessment: the claim stays qualified and `disputed`, and the adjudication obligation stays open;
- the same with a merge into a new unit identity and the mandatory `σ` retarget;
- the same arriving as a foreign manifest edit adopted as a governance-neutral delta;
- the same on a D1/D2 claim: unqualified only after an R3 disposition;
- contrasts: a byte-preserving refinement (identity kept) keeps the claim qualified, as now; an edit of the claim's own bytes without equivalence ends bearing, as designed.

## 2. Non-blocking findings

### N1 — historical governing-version adoption remains partly evidenced

Unchanged from `644eb72` N1. The 2026-10-12 adoption instruction is still a paraphrase (§0.4; stakeholder record, Not covered). The handoff independently binds this Review to 7.2.1, and the release state names 7.2.1 accepted-current. Earliest owner: §0.4, pending stakeholder restatement.

### N2 — the never-lost salvage in §6.8 is narrower than §0.1 states

§0.1 says “A rejecting entry admits every such record a request carries”. §6.8 says it only for a request “routed to revalidation” (step 6) and for “the state of their task, contract revision or bound obligation” (step 7). A request rejected for another reason is not covered by the text: one whose claimed discharge predicate fails after its own records (§7.4 reads `ev`, which the request's own failing assessment caps), or a rejection at step 5 or step 8; and step 3 drops a request whose envelope was signed by an issue key rotated (not compromised) during the task. The intent (“so nothing reported or observed adversely is lost”) is explicit, and the natural request compositions of §7.8 rarely put a failing assessment in a request whose own discharge it defeats, so this is clarity, not a permissive defect today. Repair: one clause, “every rejection after authentication admits the never-lost records the request carries”, plus Manual item 14's key lifecycle keeping envelopes of retired, uncompromised keys verifiable for never-lost records; one §22 case (an assessment request claiming discharge whose own failing assessment defeats it). Earliest owner: §6.8 steps 6-7; Manual items 6 and 14.

### N3 — independence of R3 (human) dispositions is now load-bearing and undefined

Revision 14 put “`eff(d) = F`, `d` admitted as non-independent” into the equation (repairing `644eb72` N3). Step 3 defines independence only by lineage class (“only when its lineage class is `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` […] otherwise admitted as a non-independent judgment”), and lineage classes are defined for agent executions. Every disposition of a D1/D2 disagreement must be R3. Two readings follow, both unwanted at the edges: a human `decide` record with no lineage class fails closed, so no R3 disposition is ever effective; or human judgments are taken as independent, which says nothing about the human who authored the claim. In a single-human deployment where the stakeholder authored the D1/D2 claim, “every disposition […] must be independent of the claim's author” plus R3 makes the disagreement undisposable, although the evidence owner routes adjudication “to the governing claim/owner”. The effect is restrictive (the claim stays qualified; a risk override allows provisional continuation), so it is not a blocker. Repair: one D3 sentence defining independence for authenticated human judgments, reconciled with the owner's routing (for example, the claim's owner may adjudicate with the common-mode recorded, or policy names a second human). Earliest owner: §6.6 decision class and §6.8 step 3; Manual item 3.

### N4 — the D1/D2 floor is keyed per obligation, but `qual` disagreements can span obligations

The floor fires for a failing assessment “for an evidence obligation that also has an admitted passing assessment”. After a split or retarget (the very case `qual` now covers), the failing assessment is on `e` and the passing ones on its successor `e'`; if `e` had no passing assessment, no floor item exists. Validity stays qualified and any disposition is R3, so this loses A8's proactive attention, not safety. Repair: key the floor on a bearing failing assessment named by `qual` for a claim that has any admitted passing assessment. Earliest owner: Manual item 26 (§7.9 floor text).

### N5 — bearing of a rebased predecessor frame's records after integration

§6.9 says a frame-`X` record “counts for `X'` only if every one of its entries holds, in its role, in `D_n[X']`”, and gives the after-integration table for “the integrating admission `k`” of `X`. It does not say explicitly that `bears` of a frame-`X` failing assessment follows the same mapping after `X'` integrates. An implementer who reads “`X` never integrated” literally would drop the failing assessment while the passing frame-`X` records count for `X'`. The symmetric reading holds. Repair: one sentence and one §22 case (failing and passing assessments in frame `X`, clean rebase to `X'`, integration). Earliest owner: Manual item 5.

### N6 — the model check is honest and stronger, but its `MOVE` abstraction hides A

The extension closes most of `644eb72` N2: retirement (P7), challengeable equivalence and non-independent superseders are modelled, and the per-depth sensitivity claims are now accurate. What remains:

- **One abstract `MOVE`.** Every change of claim or execution content is a single event; the model cannot express a structural re-partition, so its expected value `T` for “non-equivalent move, passing rerun” encodes blocker A as correct.
- **The oracle still shares the partition** (only a non-equivalent `MOVE` ends bearing).
- **Idealizations.** Non-independent `IMMATERIALITY` and adjudications are not modelled; retirement is a global flag over one obligation, so successor obligations and the N4 floor case are outside it; Admission is outside it, as §22 says.

Earliest owner: §22 and the model check. Add A's discriminators to §22; extend the model only if cheap, for example a structural `REPART` event distinct from a content `MOVE` (PEM DS-001).

### N7 — failing assessments of obligations that never existed in admitted state

A failing assessment made in the frame of a never-integrated candidate that adds a specification naming only pre-existing code can bear in `D_n`, and `qual` then reads an obligation that never existed there. This is restrictive and arguably right (a valid failing observation is evidence), but it should be a stated, tested consequence. Earliest owner: §6.6 (one sentence); §22.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 644EB72

| Finding | Disposition | Basis |
|---|---|---|
| A1 — co-submitted stale record | **Closed** | §6.8 step 6: “the admission record that rejects it still admits every never-lost record it carries”; failing assessments are in the class |
| A2 — contract tightened during the task | **Closed** | Step 7: never-lost records “are admitted whatever the state of their task, contract revision or bound obligation” |
| A2 — obligation discharged first | **Closed** | Step 7: “including an obligation already discharged”; discharge is S3 and re-derives `OPEN` (or provisional); step 8 does not treat the assessment as regression |
| A — residual rejection routes | **Partly closed** | N2 above |
| B — obligation removed, split or retargeted | **Closed** on its trajectories | `qual(s)` in `valid` and §7.4; discriminator “644eb72 B” gives `P`, contrast `T` |
| B — claim-side sibling | **Open** | Blocker A |
| N1 adoption provenance | **Partly closed** | Unchanged (N1) |
| N2 model blind to A and B | **Partly closed** | P7 and new events added; numbers verified; Admission and structural moves outside (N6) |
| N3 independence in prose | **Closed** in the equation | `eff(d) = F` for non-independent; new residue N3 |
| N4 step-6 sentence | **Closed** | Rewritten: provenance sentence scoped to reports and challenges |
| N5 admissibility chosen by assessor | **Closed** | “decided against the specification revision the realization instantiated, which the realization record fixes” |
| N6 floor on later bearing | **Closed** | “has borne at some admitted position (immutable once true)” (§6.6, §7.9); residue N4 |
| N7 exercised but unnamed code | **Closed** | §26 routine-disagreement trigger names it |

### Earlier Reviews

The `644eb72..62c0b24` workplan diff touches §0, §0.1, the `valid` equation and Assessment disagreement in §6.6, §6.8 steps 6-7, §7.4, the §7.9 floor, §21 item 7, §22, §26, §27.22-§27.23 and §28. It touches no persistence, publication, frame, intake, migration, component or inheritance section. No `source/`, `dist/`, `orchestrator/`, release-state or PEM path changed.

- **4C35D92 A1, A2 and findings:** closed as recorded by `644eb72`; the role table, `bears` and the disposing relation are unchanged except for the admissibility anchor (closed above).
- **97E753F A, B1, B2: closed.** `ev`, `undisputed`, `disp` and `contested` are unchanged; `eff` gains only the S0 independence case. Discriminators give the expected values.
- **124B0B7 A: closed.** P1 and P2 are green to depth 5.
- **FB3E542 A: closed**; `bind(j)` unchanged. **FB3E542 B: partly closed**, through blocker A.
- **FFBAD17 A: closed**; P3 and P4 green to depth 5.
- **Strata.** `qual` ranges over a set fixed in S0 (record syntax and effective structure) and conjoins existing `undisputed` terms, which read dispositions only positively; non-independence is an admission-time S0 fact. S2 stays monotone with one least fixed point. The support graph gains edges to dispositions for any obligation, required or not, so the one-pass topological claim holds. The `f9d9de8` configuration and mutual-validity cycles remain rejected by step 5.

The remaining 730490D, AC71FA9, F3608F5 and FFBAD17 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Failing assessment co-submitted with stale task result and review judgment | Holds (salvage) |
| Failing assessment after contract tightening; after first discharge, both orders | Holds; order-independent |
| Failing assessment whose own request's discharge claim it defeats | Text silent (N2) |
| Envelope signed by a rotated, uncompromised issue key | Dropped at step 3 (N2) |
| Specification `EVIDENCES` removed, split, retargeted | Holds (`qual`) |
| Claim leaf boundary moved, no content byte changed, passing rerun | **Fails** (A) |
| Claim leaf merged into a new unit plus mandatory `σ` retarget | **Fails** (A; defeats the B repair) |
| Same re-partition as a foreign delta adopted as governance-neutral | **Fails** (A) |
| Byte-preserving refinement of the claim unit (identity kept as composite) | Holds: `rev(c)` unchanged |
| Carve-out of the disputed claim unit into its own subject | Holds: `qual` follows the claim unit to the new subject |
| Ruleset adoption renaming the obligation rule | Holds: `qual` reads the named obligation, restrictive |
| Non-independent superseder; independent superseder of it | Holds: first `eff = F`; second disposes through the chain |
| Failing superseder of a failing assessment admitted stale | Holds: stale superseder disposes nothing |
| R3 disposition of a D1/D2 disagreement by a human without lineage class | Ambiguous, restrictive (N3) |
| Split obligation with passing on the successor only | Validity qualified; floor missed (N4) |
| Frame-`X` failing and passing assessments, clean rebase to `X'`, integration | Holds on the symmetric reading (N5) |
| Frame-only specification naming only existing code | Restrictive anomaly (N7) |
| Failing realization's artifacts become unavailable | Holds: `bears` ignores availability; restrictive |
| Loss boundary with retained failing assessment and pre-boundary disposition | Holds (`cont`) |
| Workflow layer, publication, frame, intake and migration trajectories of earlier records | Hold as recorded; untouched by revision 14 |

## 5. Minimum architecture, capability transfer and inheritance

**Minimality.** Revision 14 adds one S2 term (`qual`, a conjunction of existing `undisputed` terms) and widens an existing class (never-lost) to the clause it was missing from. No primitive, record kind, store or component is added (§27.23). The repair of A needs one rule at §6.6 and no new mechanism.

**Convergence.** The [convergence owner][convergence] asks that review after recurrence shift “toward bounded sibling/family closure”. The `644eb72` Review asked for closure by enumeration. Revision 14 repaired the two named routes but did not enumerate (§27.22 lists trajectories). This Review's enumeration finds the routes now accountable except one: a move of the evidentiary premise's *identity or scope* that is not a move of the evaluated content. The family is “what counts as an evidentiary move”, and the candidate's own principle answers it: `bears` must under-approximate, so only content moves may end adversity. Practical minimality otherwise remains conditional on the empirical items of §26.

**Predecessor comparison.** Revision 14 did not touch §16.2 or §18. Blobs verified at the candidate:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The frozen Core profile resources `ssdp-protocol-6.0` through `6.6`, `7.0`, `7.1` and `7.2` (and `sdp-protocol-5.16`) are present at the candidate, consistent with PC-001 and §24. The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. The local tracking ref `origin/main` is `af0455753e20ee54a969c844872e29e270007211`, equal to the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. The uncovered later interval proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model check is green, and §22 requires the permissive outcome, while A holds; the single abstract MOVE event cannot distinguish a structural re-partition from a content move.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; present at the candidate; preserved by §24.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy; repair at the owning D3 rule (§6.6 evidentiary premise) and regenerate §0.1, §22, §27 and the check from it.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 14.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; remains applicable to later genesis and release.
```

**7.2.1 reconciliation.** The release state at the candidate names 7.2.1 accepted-current, with distinct public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff. The `644eb72..62c0b24` diff changes no `source/`, `dist/`, `orchestrator/`, release-state or PEM path, and no §0.4, §19 or §24 text, so the earlier owner comparison between `22f4bdba` and `aaeaf8b6`, the §0.4 obligation table and the §19 landing points stand. The place where the inherited evidence doctrine is not yet realized is A.

## 6. Qualification-program adequacy

§22's disagreement group now carries the `644eb72` discriminators (co-submitted stale records, contract tightening, discharged-first in both orders, obligation removal, split and retarget, with the disposition contrast), and requires `valid` and §7.4 to agree on every generated ledger. It cannot discriminate A. Worse, its “must not qualify the claim at all” clause requires the permissive outcome for any claim-revision move without equivalence, structural or not. The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 14 is such a concretization for A: every §22 case and every model-check property stays green. Add A's discriminators and narrow the clause to content moves; add the N2, N4 and N5 cases.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `2b4046b3…`. Extracted a `git archive` of the exact candidate into a scratch directory; later commits, including the handoff commit `290c373`, were excluded.
- **Owners read** at `aaeaf8b6` with `git show`: the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge); architecture (read first: admissibility, minimum justified complexity, “one authoritative representation/state”, D3 Review); evidence (target vs execution dependency; Applicability, immutable observation and superseding assessment; binding health; Assessment disagreement; Retirement); testing (smallest plausible wrong concretization); convergence (core progression, family reasoning); workflow (Review independence, Optional independent cognitive trajectories); the kernel's Challenge text.
- **Candidate read.** §0, §0.1, §2, §5, §6.1-§6.9, §7.1-§7.10, §9.1-§9.8, §10, §12.2, §15.6-§15.7, §21, §22 (workflow, conformance, escalation, disagreement and frame groups), §26, §27.20-§27.23; the full `644eb72..62c0b24` diff; the stakeholder record; the authority-index SSDS 8 diff (revision number and Review list only); the routing test; and the model check source.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures, 0.021 s**, Python **3.13.16**.
- **Whitespace.** `git diff --check 644eb726… 62c0b245…`: **exit 0**, no diagnostics.
- **Model check**, depth 4:
  - default mode (revision 14): **63 096 transitions, 0 failures, 21/21 discriminators as expected, exit 0**;
  - `REV13=1`: **9 674 failures (P7 748, Q 2 950, O 5 976)**; two discriminators differ; **exit 1**;
  - `REV12=1`: **10 497 failures (P5 78, P7 748, Q 3 284, O 6 387; P6 0)**; five differ; **exit 1**;
  - `REV11=1`: **10 458 failures (P7 748, Q 3 278, O 6 432)**; eight differ; **exit 1**;
  - `REV10=1`: **11 522 failures (P1 250, P7 748, Q 3 116, O 7 408)**; eight differ; **exit 1**.
- **Model check**, depth 5:
  - default mode: **1 535 515 transitions, 0 failures, 21/21 discriminators, exit 0** (about 108 s), matching §0.1;
  - `REV12=1` (additionally run to test §0.1's depth claim): **298 668 failures (P5 2 487, P6 16, P7 15 862, Q 90 072, O 190 231)**, confirming that P6 fails under `REV12` only from depth 5.

  Each sensitivity mode fails at least one owner-grounded property (P1-P7 or Q), not only the oracle. P7 fails in every earlier mode by construction, because retirement is the revision-14 delta.
- **A.** Deductive, from the quoted contract text (§6.1 revision and governance-neutral rule, §6.6 role table and `bears`, §6.7 and §12.2 equivalence scope, §15.7, §22). Not representable in the model's vocabulary, so no scratch reproduction was attempted.
- **Identities.** Verified the predecessor blobs, the release-state identities, the frozen-profile presence, the PEM blob identity, the stakeholder-record blob and the changed-path list above.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, admission, obligation, structural change, disagreement, disposition and closure. Materiality here is the ability to change support, closure or the next authorized action. No physical or numerical result is asserted. One pinned candidate was reviewed through multiple deductive trajectories; no variant search over scientific analyses was performed and no delegates were launched. The judgment relies on accepted engineering and evidence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation.** `source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, on the working-tree file whose blob equals the candidate's, failed with `UNAVAILABLE: repository revision is not resolvable as an immutable object` for historical evidence routes (`55c08526…`, `81375d81…`), which `git cat-file` cannot resolve. This checkout is a **shallow clone**. That is an environment limitation, not a PEM defect and not a pass.
- **Remote state.** `origin/main` is the local tracking ref. No fetch was performed and no remote-state claim is made.
- **Manual compositions.** A assumes that an implementer's write scope may include manifest entries of a claim's subject (§15.7 permits it; policy may narrow it) and that the passing rerun is assessed by an assessor who reads the observation as the passing assessor did. The boundary-move variant needs only the quoted D3 text; the merge variant also uses step 4's reference check. N2 assumes request compositions the Manual fixes (items 6, 14). N3 assumes the human `decide` record carries no lineage class, which the candidate does not state either way.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency: shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. In particular, the `644eb72` Review (same family) recorded “Byte-preserving restructure of the claim unit […] Holds as designed”, and this Review reached the opposite conclusion only by separating identity-keeping refinement from identity- or scope-changing re-partition; a different family might frame either differently.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require that for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need the owner adjudication and production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 10. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair of the §6.6 evidentiary-premise rule (A), with §0.1, §22, §27 and the model check regenerated from it, and a replacement immutable candidate. Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/62c0b24533f31b933f698c6f376a12ed689759f9/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md

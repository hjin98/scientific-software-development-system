# SSDS 8 Architecture Manual — Independent D3 Review, candidate f03b15e

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: f03b15e55de77fe230f404fcb0b3bf12b21b6a3d
    SCOPE: whole proposed Manual as durable D3 owner: (a) closure of workplan §21 and both §16.2 tables;
           (b) fidelity and refinements R1-R12; (c) adequacy (out-of-matrix); (d) inheritance, capability
           transfer and PEM HAS; (e) qualification design; (f) doctrine-realization map; (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 828222fd82b2034110d466bf2b4c11835b64091c
    CLOSURE MAP (aid, not authority): qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md,
           blob 6540eed8f79fc7d3b3a7527f3b857b070975db2d
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE: e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756),
           Phase B Review PASS (qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
           (both resolved from PROTOCOL-RELEASE-STATE.yaml)
    FROZEN ARCHITECTURE 1.6.0: orchestrator/docs/architecture.md, blob 39e6de727f6c35402962509d30d947962992eaad
    PRIOR REVIEWS (HYPOTHESES ONLY): Manual NO-PASS records 6FF4ED1, B595F2C, C6DA678, CC005DB, D837363,
           53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC, E9E6E9F, A18B544, 0B6C4FA,
           27EF339, 5C55D4B, 575DC78, F7419D5, B46C250 (same family), B46C250 (different family), F22B4DC,
           362AF9F and 61CD09B; Phase B PASS E23F142
    REVIEW METHOD: immutable-candidate reconstruction (git archive of the candidate), word-level diff
           61cd09b..f03b15e, read of Part 0, §1-§13, §16.6, §19, §22, §31.5-§31.6 and §32 in full and of the
           remaining sections by heading against the diff; deductive falsification of the two new mechanisms
           (the judgment key and the human cutover record) in both directions with family/sibling closure
           (convergence owner, "Review strategy after recurrence"); prior-finding regression; G1 document checks
    REVIEWER: Claude model family, the same family as the Manual's author; a fresh-context sub-agent
           launched by the authoring session, with none of the authoring conversation
    MUTATION: this record only; no commit, no push

All Manual section numbers refer to the candidate blob above. Governing owners are quoted at the public-source commit `aaeaf8b`.

## SERIOUS CHALLENGE

**None against accepted authority.** SSDP 7.2.1, the reviewed workplan contract, the frozen Architecture 1.6.0 and the stakeholder record are not shown to be false, contradictory or unrealizable. Both blockers below are defects of the proposed D3 Manual; the owners they violate are coherent and realizable.

Owner texts applied (public source `aaeaf8b`):

| Owner | Exact text |
|---|---|
| D3 role, Independent Review and Challenge | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| D3 role, design contract | "prefer cohesive ownership, direct flow, one authoritative representation/state" |
| Architecture, D3 formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| Architecture, D3 Review | "If D3 itself appears contradictory, materially ambiguous, impossible under simultaneous constraints, or incapable of preserving D2, raise Serious Challenge to D3." (applied to the proposed, not yet accepted D3, so reported as blockers) |
| Evidence, Assessment disagreement | "When a durable representation stores multiple assessments, supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement." |
| Workflow, Human gates | "The designated human authority is required where project/domain policy assigns ratification/adjudication. Orchestration may represent pending/accepted/rejected state but cannot self-approve it." |
| Convergence, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair** when evidence shows repeated patches around the same mechanism, patch-on-patch repair, ... duplicated/synchronized authoritative state, competing authorities" |
| Convergence, Review readiness | "Review sufficiency is not proof of zero conceivable defects." |

## Verdict

**NO-PASS.** Two blocking D3 defects survive. Both entered through the repairs of the `61cd09b` blockers.

- **B1 (judgment-disagreement and supersession-authority family; non-local recurrence, local defect).** The `61cd09b` B1 repair replaced "a record of the same kind **on the same target**" in Admission's supersession-authority rule (§8.3 step 3) with "the same **judgment key** (the key the kind's §5.5 `same` test reads ...)". It names `EVIDENCE_ASSESSMENT` explicitly as included, but §5.5 defines a `same` test only for the nine adverse-capable kinds and says "Failing evidence assessments are governed by §6, not here". So the key that authorizes an assessor's own reassessment or the owner's adjudicating supersession of a failing assessment — the reviewed disposition route of workplan §6.8 step 3 and Manual §6.7 — is undefined. The same holds for `IMMATERIALITY`, `LEGACY_ACCEPTANCE`, `EXTERNAL_ACCEPTANCE` and the other keyless support-tier kinds. Where a key is defined, it is not always a key: for `PLAN_ACCEPTANCE` it is an overlap relation, and for `EQUIVALENCE` the stated key ignores the class the veto reads. The repair's own claim that "the veto's reach and its relief's reach are therefore the same set of records" is false for both.
- **B2 (cutover realization; second round of `61cd09b` B2).** The repaired §19.5 makes the cutover `MODE_TRANSITION` a direct human record "once `X`'s `TASK_RESULT` is admitted", declaring frame `id(X)`, with conditions 1-6 checked only "at `X`'s integrating admission". Nothing bounds the record to the time before that integration, and the acting rule (§5.2) makes a record that declares an integrated enactment's frame act in the admitted state at once. The Dispatcher integrates `X` as soon as its item's discharge predicate holds, which does not depend on the cutover. A human recording the cutover after that integration therefore enacts a cutover that no Admission check ever examined: no owner acceptance, no `MIGRATION` equivalence, no quiescence attestation, no cutover gate. The head sentence still says the record is "admitted only with" conditions 1-6, which contradicts the new paragraph.

The `61cd09b` repairs otherwise close what they target:
- the gate and transformation-review relief across runs and enactments (`61cd09b` B1 trajectory and siblings (i)-(iv));
- the cutover carrier's admissibility, its per-domain carrier, its circular preconditions and the prospective-tenure test (`61cd09b` B2 along the pending path);
- `61cd09b` N1-N3 and N5.

The assessment-disagreement matching clause (§6.5-§6.6), the content-identity family and the D1-D3 change rule show no new defect; §6 is unchanged in this round.

This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — The judgment key that authorizes supersession is undefined for most kinds and is not a key for two

**Family and earliest owner.** Proposed D3, Manual §8.3 step 3 (supersession authority), §5.5 (`same`, adverse-judgment veto), §6.7 (disposition by supersession), §0.3 R8 and R9 and the §0.3 history sentence for `61cd09b`. These realize workplan §21 items 5 and 7 and the reviewed §6.8 step 3 rule ("a record may name `x` in `supersedes` only as `x`'s own assessor's reassessment or the owner's adjudication").

**Recurrence.** This is the thirteenth round of the gate and judgment-disagreement family and the second in which supersession identity and veto identity are defined in two places. The `61cd09b` Review's Option 1 asked for one key per adverse-capable kind. The realization instead redefined supersession authority for **every** support-tier kind by reference to a test that exists only for the adverse-capable ones. The defect is local in text but non-local in cause: "the same target" for supersession is now defined by a second owner (§5.5) that does not cover the kinds §8.3 step 3 applies it to.

**Contract text (candidate):**

- §8.3 step 3: "every other support-tier record, `EVIDENCE_ASSESSMENT` included, only by a record of the same kind with the same **judgment key** (the key the kind's §5.5 `same` test reads; for `EQUIVALENCE`, the same unit and endpoints) that is either `x`'s **own author's reassessment** (the same actor; for an assessment, its own assessor ...) or the **owner's adjudication** ... The veto's reach and its relief's reach are therefore the same set of records (61cd09b B1)"; "A record whose `supersedes` is not so authorized is **rejected**".
- §5.5: "Failing evidence assessments are governed by §6, not here." The `same` list covers `ACCEPTANCE`, `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS`, `GATE_DECISION`, `PRODUCT_SCOPE_ACCEPTANCE` and `INTAKE_DISPOSITION` only, then states "each kind's `same` test is its judgment key, which also decides supersession authority (§8.3 step 3)".
- §5.5 `same` for `PLAN_ACCEPTANCE`: "any item revision both name"; for `EQUIVALENCE`: "the same unit and endpoints, with `z`'s class covering `j⁻`'s class by the §4.4 rule".
- §6.7: "`d` supersedes `a⁻`, directly or through a chain of supersessions: an explicit reassessment of the realization by `a⁻`'s own assessor, or the owner's adjudication".
- §3.4: `EVIDENCE_ASSESSMENT` target "realization record, evidence obligation `e`, reading; mode".
- §0.3 history: "each kind has one judgment key, read both by the veto and by supersession authority".

**Trajectory 1 (assessment; restrictive, the literal reading).**

1. Assessor `A` (human, independent of the claim's authors) records `EVIDENCE_ASSESSMENT FAIL a⁻` of realization `R` for obligation `e` under the admitted reading. It counts (§6.4).
2. `A` re-examines the outcome and records `EVIDENCE_ASSESSMENT PASS a` of the same realization, obligation and reading, with `supersedes = [a⁻]`, as §6.7's first disposition route and workplan §6.8 step 3 allow.
3. Admission step 3 looks up the judgment key "the kind's §5.5 `same` test reads". `EVIDENCE_ASSESSMENT` has no `same` test, so no key matches and the supersession "is not so authorized": `a` is **rejected** (`AUTH_SUPERSEDES`). The owner's adjudicating supersession is rejected the same way.
4. The failure can now be disposed of only by an `IMMATERIALITY` or an upheld challenge. A reviewed disposition route is gone, and the inspector cannot show a resolved reassessment because none is admissible.

**Trajectory 2 (assessment; the permissive reading).** An implementer who instead takes §6.7's words ("a reassessment of the realization") as the key admits `A`'s `PASS` of `R` for a different obligation `e2`, or under a reading that is only in a pending candidate, as a superseder of `a⁻`. That record disposes of a failure under the admitted reading and obligation that nobody re-assessed. The ledger then shows the disagreement as resolved by a record about a different question. Assessments for different obligations "never conflict" (§6.2), yet one now withdraws the other.

**Siblings (one cause: supersession identity borrowed from the veto's comparison).**

- **(i) Other keyless kinds.** `IMMATERIALITY` (owner withdrawal of a disposition), `LEGACY_ACCEPTANCE`, `EXTERNAL_ACCEPTANCE`, `HUMAN_DECISION`, `LINEAGE_ATTESTATION`, `NON_AUTHORSHIP_ATTESTATION`, `INTAKE_CLASSIFICATION`, `RECONSTRUCTION_PROPOSAL` and `TASK_RESULT` have no `same` test, so their supersession authority is undefined. §6.7's "re-disposal ... a supersession of the fallen superseder" is an assessment supersession and inherits trajectory 1.
- **(ii) `PLAN_ACCEPTANCE` overlap (permissive).** Reviewer `R` records `REJECTED` naming item revisions `{A1, B1}`. The owner adjudicates with `ACCEPTED` naming `{A1}` only and `supersedes = [R's record]`. The two records share `A1`, so the key "matches". Before the repair, "the same target" required the same set and this was refused. Now `R`'s rejection of `B1` stops standing although no record judged `B1` again, and a peer's earlier `ACCEPTED {B1}` stops being vetoed. "Any item revision both name" is a non-transitive overlap, not a key.
- **(iii) `EQUIVALENCE` class (permissive).** The supersession key is stated as "the same unit and endpoints", without the class. The owner's `EQUIVALENT` of class `MIGRATION` may supersede a `NOT_EQUIVALENT` of class `CONSUMER:k` on the same endpoints. Afterwards a peer's `EQUIVALENT CONSUMER:k` is no longer vetoed and covers `CONSUMER:k` entries, so records relying on the old revision regain currency for consumer `k`, although no record addressed that class. Before the repair the target included the class. The relief's reach is now wider than the veto's, which reads class covering.
- **Held (no sibling).** `GATE_DECISION` (gate and triple, any run), `REVIEW`/`CONFORMANCE` of a transformation (item and changed-unit content, any enactment), `ACCEPTANCE`, `COMPLETENESS`, `PRODUCT_SCOPE_ACCEPTANCE` and `INTAKE_DISPOSITION`: each `same` is an equivalence on a well-defined key, and the `61cd09b` B1 trajectories now close (section 5).

**Violations.**
- For the assessment kind, §8.3 step 3 and §5.5 contradict each other on the rule that guards the S4 disposition route: one includes `EVIDENCE_ASSESSMENT` under a key the other never defines. An implementer must choose between refusing every assessment supersession, which is an unsurfaced semantic change to workplan §6.8 step 3 and §6.6's disposition list, and inventing a key, which in its natural form (§6.7's "the realization") lets a record about another obligation or reading dispose of a failure. That violates the evidence owner's "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement".
- The architecture owner's "define it before dependent invariants use it": the judgment key carries normative meaning in §8.3 and is undefined for most kinds it governs.
- Siblings (ii) and (iii) widen supersession authority beyond the reviewed and the previously stated target without listing the change in §0.3. They also falsify §8.3's "the veto's reach and its relief's reach are therefore the same set of records".

**Family assessment and options for the stakeholder.** The common cause is that one comparison is asked to serve as two things: the veto's reach (a relation, sometimes asymmetric or overlapping, defined only where an adverse outcome exists) and the supersession target (an identity every supersedable kind needs). A further latch per kind would be additive. Options:

- **Option 1 (recommended; narrowest).** Restore "the same target" as the supersession rule for every kind, and state the key exception only for the kinds whose `same` deliberately crosses targets: `GATE_DECISION` (gate and subject triple, any run) and `REVIEW`/`CONFORMANCE` of a transformation (item and changed-unit content, any enactment). `ACCEPTANCE`, `COMPLETENESS`, `PRODUCT_SCOPE_ACCEPTANCE` and `INTAKE_DISPOSITION` need no exception, because their `same` already equals their target. Delete the sentence claiming one key per kind, and say instead that for every adverse-capable kind the supersession target contains the veto's reach. This removes text rather than adding a mechanism.
- **Option 2 (one owner; restructures, adds a column).** Add a "judgment key" column to the §3.4 support-tier table, defined for every supersedable kind as an equivalence (the target where nothing else is stated), and make both §5.5 `same` and §8.3 step 3 read it. `PLAN_ACCEPTANCE` and `EQUIVALENCE` would then need their veto comparison restated over that key. This is cleaner ownership, but it rewrites the veto table, the surface on which the family keeps recurring.

I would put Option 1 versus Option 2 to the stakeholder. Neither SD-25, SD-26 nor any other SD chose a judgment key; this was the author's choice under item 19.

**Required discriminators (real owners: Admission → Derivation → inspector, nothing seeded resolved).**
- An assessor's own `PASS` reassessment of the same realization, obligation and reading, with `supersedes = [a⁻]`, is admitted and disposes of `a⁻` (`disp = T` in the states where it acts). The same holds for the owner's adjudicating assessment.
- A `PASS` of the same realization for another obligation, or under another reading, naming `a⁻` in `supersedes` is rejected (`AUTH_SUPERSEDES`).
- An owner's `PLAN_ACCEPTANCE ACCEPTED {A1}` naming a `REJECTED {A1, B1}` in `supersedes` is rejected, or else, under a stated rule, leaves the rejection of `B1` standing.
- An owner's `EQUIVALENT` of class `MIGRATION` naming a `NOT_EQUIVALENT` of class `CONSUMER:k` is rejected, or the `CONSUMER:k` veto survives.
- An implementation that keys assessment supersession on nothing, or on the realization alone, must fail.

### B2 — A cutover record admitted after its carrier's integration enacts an unchecked cutover

**Family and earliest owner.** Proposed D3, Manual §19.5 (head sentence and the carrier paragraph), §19.1, §5.2 (acting rule), §7.5, §7.6 enactment condition, §8.3 steps 2-4 and 7, §11.5 step 3. These realize workplan §21 item 13 (cutover, quiescence) and workplan §12.4 item 6 ("an admitted cutover record").

**Recurrence.** Second round of the cutover-realization defect (`61cd09b` B2). The repair fixed who submits the record and moved its conditions to the integration. It did not bound **when** the record may be admitted relative to that integration, and it did not re-derive the head sentence. This is a clean local defect inside a recurring family.

**Contract text (candidate):**

- §19.5 head: "A **cutover** of subject `s` from `LEGACY(p)` or `UNGOVERNED` to `NATIVE` is a `MODE_TRANSITION` admitted only with: 1. … 6."
- §19.5 carrier paragraph: "Once `X`'s `TASK_RESULT` is admitted, the actor policy designates records the cutover `MODE_TRANSITION` directly ..., declaring frame `id(X)`. It acts in that frame (§5.2) ... Conditions 1-6 are **enactment conditions**: Admission checks them at `X`'s integrating admission, with §7.6, and that integration enacts the transition."
- §5.2: "An admitted record **acts** in `G` iff it declares the admitted frame; or it declares a frame of an enactment that has integrated at or before `n`; or ...".
- §19.1: "Mode is ledger state, ... changed only by an admitted `MODE_TRANSITION` acting in the state (§5.2): a cutover's at the integration that carries it (§19.5), any other at its admission."
- §7.6: the enactment condition applies to "every promotion, restoration or cutover", that is, to an integration that carries one.
- §11.5 step 3: "Once the claimed obligation's discharge predicate would hold on the candidate — clean conformance, current review judgments, required gates — the Dispatcher submits an **integration request**".

**Trajectory (a natural race, no malice needed).**

1. `s` is a `LEGACY(p)` D4 subject (for a D1-D3 subject, the same with an `AUTHOR` carrier). A `MIGRATE` item `I` naming `s` is accepted. Task `t` submits `X`, which changes the representation; its `TASK_RESULT` is admitted.
2. Conformance is `CLEAN` and `REVIEW(X)` passes. No cutover `MODE_TRANSITION` acts in `X`'s frame yet, so no cutover obligation exists there, and `I`'s discharge predicate does not depend on the cutover. The Dispatcher submits the integration (R0). The enactment condition does not apply, because `X`'s integration carries no cutover. `X` integrates at `k` as an ordinary migration of a legacy subject.
3. The designated human `H` now records the cutover `MODE_TRANSITION`, declaring frame `id(X)` with its quiescence list, as §19.5 directs ("Once `X`'s `TASK_RESULT` is admitted"). Steps 1-3 pass: a human, a lifecycle record. No step checks conditions 1-6: they are enactment conditions of `X`'s integrating admission, which is already in the past, and step 7's integration rules do not apply to a records-only request. The record is admitted at `m > k`.
4. By §5.2 the record declares the frame of an enactment integrated at `k ≤ m`, so it acts in `D_m`. By §19.1 `s` is `NATIVE` in the admitted state from `m`: a new tenure starts, legacy-side edits become foreign changes, and Admission alone governs `s`. Yet:
   - there is no reconstruction check (condition 1);
   - there is no `MIGRATION` equivalence (condition 2);
   - there is no owner acceptance of the native revision (condition 3);
   - there is no `LEGACY_RELEASE` for a carve-out (condition 4);
   - no gate attested the quiescence list (condition 5);
   - there is no cutover gate decision (condition 6).

   In-flight legacy runs on `s` were never drained, pinned or migrated under a gate's attestation.

**Siblings.**

- **(i) Non-carrier frames.** The carrier condition ("an `AUTHOR` item for a D1-D3 subject ..., a `MIGRATE` item otherwise") is checked nowhere. Admission does not check it at the record's admission. At integration, the write set (§1.2) compares `Σ_n` with `Σ_n ⊕ Δ_Σ(X)`, and a mode change is not a declaration key, so it is not in `Δ_Σ(X)` (§8.3 step 3 itself distinguishes "`Σ_n ⊕ Δ_Σ(X)`" from "a cutover `MODE_TRANSITION` acting in `X`'s frame"). The stated reason "a mode change is a governance-signature change, §1.2, §13.2" therefore never brings `s` into the write set. A D2 cutover carried by a `MIGRATE`, `IMPLEMENT` or `DOCUMENT` transformation passes the domain rule and `BOUNDARY`. §31.6 (Q)'s expected "a `MIGRATE` carrier changing a D2 subject's mode is a `VIOLATION`" has no mechanism. Along the pending path, conditions 1-6 are still checked at integration, so this sibling alone loses only the `AUTHOR`-keyed duties of the carrier task; with (iii) it is unbounded.
- **(ii) Head sentence.** "A `MODE_TRANSITION` admitted only with" conditions 1-6 contradicts "enactment conditions ... checked at `X`'s integrating admission". Read as written, the head sentence restores the `61cd09b` B2 circularity, because condition 3 is a prospective acceptance that exists only once the record acts. Read the other way, the record's admission checks nothing, which permits the trajectory above.
- **(iii) Late record in an old frame.** The same late admission works with the frame of any long-integrated transformation that names `s`. Nothing ties the record to a pending carrier, so a cutover can be enacted at any later position by one human record.
- **(iv) Repeated records.** Two cutover records in one frame with different quiescence lists. Lifecycle records are never superseded, and the Manual does not say which list condition 5 reads. Minor; resolvable once (i)-(iii) are fixed.

**Violated text.** Workplan §12.4 item 6 and §21 item 13 (cutover conditions and quiescence) are not enforced on every route. M4 ("acceptance runs top-down") and M6 ("in-flight older-version work is drained, pinned or migrated") can be bypassed. The workflow owner's human-gate rule is also bypassed: the cutover gate is never decided. Finally, §19.5's head sentence and carrier paragraph contradict each other.

**Minimum repair direction (narrowing, no new record kind).**
1. Admission admits a cutover `MODE_TRANSITION` declaring `id(X)` only while `X`'s enactment has no admitted integration, and only if `X` is a transformation of an accepted carrier item of the stated kind that names `s`; otherwise it refuses the record (a reason code from the existing `OBLIGATION_*` or `ENACTMENT_*` families).
2. Restate the head sentence as "enacted only with" (or "an integration that carries a cutover is admitted only with").
3. Either state that the carrier's item kind is checked directly at the integrating admission, or make the write set's structure comparison read the frame's acting cutover, so that (i) is enforced by one stated mechanism.

**Option to put to the stakeholder.** After step 1 alone, the race leaves `X` integrated without the cutover, and the cutover needs a further iteration (`tree(C) = tree(B)`). That is a safe liveness cost, but `I` may already be discharged, so a new item may be needed. The alternative is an item-level cutover declaration so that the enactment condition requires the acting record and the race cannot happen. That **adds mechanism** (a contract field).

**Required discriminator.**
- `X` integrates before any cutover record exists. A human `MODE_TRANSITION` declaring `id(X)` afterwards is refused, and `s`'s mode in the admitted state is unchanged.
- A cutover record in the frame of a pending non-carrier transformation is refused, or the integration is refused, by one stated rule.
- Along the pending carrier path, the integration is refused until conditions 1-6 and §7.6 hold, and only that integration changes the mode.
- An implementation that admits the late record and lets it act must fail.

## 2. Non-blocking findings

**N1 — `OBLIGATION_ANSWERED` no longer says "bound to it" (B1 family; restrictive ambiguity).** Since `f22b4dc`, §8.3 step 7 reads "Once a judgment obligation is answered (§10.3) in the frame a passing judgment declares, Admission refuses that judgment". The `e2154ac` text said "any later passing judgment bound to it". Under §10.3 a judgment also answers when "recorded on its target by an authenticated human". So a human author's direct reassessing `ACCEPTANCE PASS`, or a human owner's direct adjudicating `REVIEW PASS`, on an obligation already answered by the adverse judgment can be read as refused. That would contradict §10.3's own "the next step is ... the adverse judgment's own author's reassessment, or the owner's adjudication". Gates are exempt, which is why the `61cd09b` discriminator (A) holds. §10.3 lets an implementer resolve this, so it is non-blocking. Repair: exempt a record whose supersession step 3 authorized, or restore "bound to it".

**N2 — Partition obligation identity can collide (repair of `61cd09b` N4).** §13.7 identifies each part's implementer obligation by "the item revision and the part's index in the decision". The decision's identity is not a parameter, so a later re-partition of the same item revision ("supersedes an earlier one only for obligations not yet discharged") derives part obligations whose identities equal the earlier partition's parts with the same index but a different share. Consequences:
- a discharged or in-flight earlier part shadows the new one: a duplicate discharge is refused, and a task bound under the old share claims an obligation whose share changed;
- the cost is liveness, not safety.

Repair: include the `PARTITION` record's identity in the parameters. This is a repair of a non-blocking finding that added a defect, the pattern the handoff asks to watch.

**N3 — A fenced cutover leaves a half state.** A cutover enacted by an integration that is then fenced or `OVERTAKEN` (R4) keeps `s` `NATIVE` (mode is ledger state), while the tree returns to the legacy bytes. `s` is visibly invalid there, so this fails closed. But §19.5's "interrupted migration leaves no half state" is then false. Disclose it in §19.5 and §32.2, with the human's options (re-apply as a new enactment, or a rollback `MODE_TRANSITION`).

**N4 — Residue in the newest text.**
- §19.5 says the carrier item "names `s` and its native revision", but the native revision is fixed by `X`, not by the item, except for a pure mode change.
- The §0.3 history sentence "each kind has one judgment key ... so a veto is always liftable where it bites" is false for keyless kinds (B1).
- Closure-map item 13 restates the carrier rule without the timing gap (B2).

Editorial, except where B1 and B2 make the statement false.

**N5 — Qualification gaps (DS-001).**
- §31.6 (P) exercises gate and transformation-review relief, but no case exercises assessment supersession authority after the key change, `PLAN_ACCEPTANCE` overlap or `EQUIVALENCE` class supersession (B1).
- No case integrates the carrier before the cutover record exists (B2).
- (Q)'s `VIOLATION` expectation has no stated mechanism (B2 (i)).
- No case records a direct human reassessment on an answered non-gate obligation (N1), and none re-partitions an item (N2).

A §31 implemented to the present expected values would encode both blockers. These are design-program omissions, not runtime demands at G1.

**N6 — Stakeholder-level trade-offs (reported as such, not blockers).**
- The author's `61cd09b` choice of a cross-run gate veto with relief in the later run (now realizable for gates and transformation reviews).
- SD-26's per-iteration acceptance and gate cost.
- R4's fence cost, now stated in full.
- SD-17's partial reversal.
- SD-24's narrowing.
- The exact-identity cost.
- SD-25's consequences.
- Phase B N1 (paraphrase-only adoption instruction, §32.2).

## 3. Closure audit: workplan §21 and §16.2

**Method.**
- The diff `61cd09b..f03b15e` changes only:
  - §0.3 (R4, R12, history);
  - §5.5 (one sentence in `same`);
  - §7.5;
  - §7.6 (enactment condition, rule 1);
  - §8.3 step 3 (prospective tenure; supersession authority);
  - §13.7 (part obligation identity);
  - §16.6 sections 1-2;
  - §19.5;
  - §22.3 (takeover wait);
  - §31.5 discriminators (O)-(Q);
  - §32.3 (one trigger);
  - closure-map rows 7 and 13 and §5.
- I located each changed or family-relevant §21 item's deciding section myself, using the closure map only to find text. For other items, I confirmed the cited text is unchanged since `61cd09b` and read the sections listed in the header.

**Not substantively resolved at this candidate:**

| §21 item | Clause | Gap |
|---|---|---|
| 13 | cutover, quiescence | Conditions 1-6 are checked only at a carrying integration, and the cutover record can be admitted after that integration and act at once. The carrier kind is not enforced by any stated mechanism, and the head sentence contradicts the carrier paragraph (B2) |
| 7 | obligation rules (adjudication and disposition) | Supersession authority is undefined for `EVIDENCE_ASSESSMENT` and other keyless kinds, and over-broad for `PLAN_ACCEPTANCE` and `EQUIVALENCE`. The `ADJUDICATE_DISAGREEMENT` route for a failing assessment (§6.10) depends on it (B1) |
| 5 | declared frame per kind | The frame a cutover record may declare is not bounded to a pending carrier (B2) |

**§16.2.** Both tables are resolved in §26.4, which is unchanged since `61cd09b`. The earlier full checks found every Deferred row resolved, and I found no hunk touching them.

**Material decision versus delegated choice.** B1 and B2 are under-specifications an implementer would have to decide architecturally. I found no new over-specification.

## 4. Refinements R1-R12

| # | Assessment |
|---|---|
| R1 | **Sound.** Unchanged. `on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction, and the guard keeps `on⁻` a function of the record and `K` |
| R2, R3 | Sound; unchanged |
| R4 | **Sound as a mechanism**, and its cost is now stated in full (`61cd09b` N2 closed). A fenced cutover's half state is undisclosed (N3) |
| R5, R6, R7 | Sound; unchanged |
| R8 | **Unsound as now realized.** Supersession authority "by the kind of `x`" is keyed on a judgment key defined only for adverse-capable kinds and is not a key for `PLAN_ACCEPTANCE` or `EQUIVALENCE` (B1). Because it widens two kinds' authority, the change needs listing even after repair |
| R9 | **Veto direction sound. Relief direction now realizable** for `GATE_DECISION`, `REVIEW` and `CONFORMANCE` across runs and enactments (`61cd09b` B1 closed). The claim "the veto's reach and its relief's reach are therefore the same set of records" is false for `PLAN_ACCEPTANCE` and `EQUIVALENCE` (B1 (ii)-(iii)). The direct-human relief route depends on reading N1 narrowly |
| R10 | **Sound for runs**, including the cutover's run, which is the carrying enactment and a ledger fact. The cutover's enactment is bypassable by a late record (B2) |
| R11 | **Sound.** `gterm`, `unq` and `elig` over acting records are unchanged |
| R12 | **Sound.** The why-column now states the liveness narrowing (`61cd09b` N3 closed) |

## 5. Previous findings re-derived

"Closed" means I re-derived that the present text excludes the named trajectory. It is not runtime evidence.

**Depth.**
- In full against the new text: `61cd09b` B1-B2 and N1-N7.
- For older records, I took the `61cd09b` record's dispositions as hypotheses. I confirmed that each family's governing text is unchanged except in the hunks listed in section 3, and I re-checked the mechanisms those hunks touch (R8/R9 supersession, §5.2 acting, §7.5-§7.6, §10.2 runs, §19.5) during the read. I did not re-read every older record's prose.

### 61CD09B

| ID | Disposition |
|---|---|
| B1 (gate veto relief across runs) | **Closed.** `H`'s or the owner's `ACCEPT` in `X2`'s frame naming `h⁻` has the same key (gate and triple), so it is authorized. It acts only in `X2`'s enactment: the veto stays in the admitted state while `X2` is pending and ends after integration. An `X1`-frame reassessment never acts in `D_n[X2]` |
| B1 siblings (i) absorbed revert, (ii) other item, (iii) re-cutover | **Closed** by the same key, recorded in the admitted frame (i) or the later frame (ii), (iii) |
| B1 sibling (iv) `REVIEW`/`CONFORMANCE` across enactments | **Closed** under the "bound to" reading of `OBLIGATION_ANSWERED` (an owner task bound to `ADJUDICATE_DISAGREEMENT`). A direct human record depends on N1 |
| B1 family | **Recurs as B1** for keyless and non-key kinds |
| B2 (cutover carrier inadmissible; circular preconditions; D1-D3 carrier; pure mode change) | **Closed along the pending path:** a human records the carrying-frame record; the carrier is `AUTHOR` for D1-D3; a pure mode change runs under such an item; conditions are checked at integration; step 3 reads the acting record. **Recurs as B2** (timing, carrier enforcement, head sentence) |
| N1 (gate core omits vetoing decisions) | **Closed** (§16.6 sections 1-2) |
| N2 (fence cost understated) | **Closed** (R4, §22.3, §32.3 trigger) |
| N3 (residue) | **Closed** for R12, §32.3 and closure-map row 7. New residue N4 |
| N4 (partition binding) | **Closed as stated; new defect N2** (identity collision on re-partition) |
| N5 (first submitter) | **Closed** (§7.6 rule 1 "whichever task resubmits it") |
| N6 (qualification) | **Partly closed**: (P), (Q) and the kept-fence case were added. New gaps N5 |
| N7 | Stakeholder; carried as N6 |

### 362AF9F, F22B4DC, B46C250 (both families)

| Review | IDs | Disposition |
|---|---|---|
| 362AF9F | B1-A and siblings | Closed (veto unchanged) |
| 362AF9F | B1-B (cutover run identity) | Identity closed; realization B2 |
| 362AF9F | N1-N5 | Closed |
| 362AF9F | N6 | Partly closed (N5) |
| 362AF9F | N7 | Stakeholder |
| F22B4DC | B1-A to B1-D, B1-F | Closed |
| F22B4DC | B1-E | Identity closed; realization B2 |
| F22B4DC | N1-N4 | Closed |
| F22B4DC | N5 | Partly closed (N5) |
| F22B4DC | N6 | Stakeholder |
| B46C250, different family | B1-A, B1-B (frame relief must not act in the admitted state) | Closed; the new key does not change where the relief acts |
| B46C250, different family | B1-C, B1-D | Closed |
| B46C250, different family | N1, N3, N6 | Closed |
| B46C250, different family | N2 | Disclosure |
| B46C250, different family | N4 | Partly closed (N5) |
| B46C250, different family | N5 | Stakeholder |
| B46C250, same family | B1 (i)-(iv) | Closed |
| B46C250, same family | N1, N3 | Closed |
| B46C250, same family | N2 | Disclosure |
| B46C250, same family | N4 | Partly closed |
| B46C250, same family | N5 | Stakeholder |

### F7419D5 to E2154AC

| Review | IDs | Disposition |
|---|---|---|
| F7419D5 | B1, N1-N3, N5 | Closed |
| F7419D5 | N4 | Partly closed (N5) |
| F7419D5 | N6 | Stakeholder |
| 575DC78 | B1, N1-N7 | Closed (`gterm` unchanged) |
| 5C55D4B | B1-B2, N1-N7 | Closed, apart from stakeholder items |
| 27EF339 | B1-B3, others | Closed. The gate family's later rounds are recorded above |
| 27EF339 | N2 | Stakeholder |
| 0B6C4FA | B1-B2, others | Closed |
| 0B6C4FA | N1 | Stakeholder |
| 0B6C4FA | N2 | Partly closed as before (author-accountable supersession while challenged) |
| A18B544 | B1-B2, N1-N5 | Closed |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1-B2, N1-N5 | Closed or superseded |
| E2154AC | B1, N1-N5 | Closed. Its N-level reading of `OBLIGATION_ANSWERED` ("bound to") is no longer the text (N1) |

### 3540D98 (GPT family), 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 3540D98 | B1 (exact identity), B2 (`ext`), B4 (equal regions) | Closed |
| 3540D98 | B3 | Closed for its trajectory; the family recurs as B1 here |
| 3540D98 | N1 | Run representation closed; cutover carrier B2 |
| 3540D98 | N2-N4 | Held as disclosures |
| 798B2B4 | B1-B4, N1-N8 | Closed. No D1/D2 revival on revert on any route. A late cutover starts a tenure with no acceptance, so nothing revives (B2 is a gate bypass, not a revival) |
| 71CF9B3 | B1-B2, N1-N8 | Closed. N4's cutover trigger is the frame derivation; its timing is B2 |
| 86AB683, 1FFBBF0 | B and N items | Closed (SD-18 class unchanged) |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | Stakeholder |
| D837363 | B1-B4, N1-N8 | Closed. B3's domain rule is intact, but it does not reach a mode change (B2 (i)) |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | IDs | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed |
| C6DA678 | B1-B3, N1-N12 | Closed. B2's veto is closed in both directions for gates and transformation reviews |
| B595F2C | B1-B3, N1-N8 | Closed |
| B595F2C | B4 (no resolution by re-dispatch, count or order) | **Closed in both directions** for the kinds `61cd09b` B1 named. For assessments, the reviewed own-assessor route is now ambiguous (B1) |
| 6FF4ED1 | B1-B4, N1, N3-N12 | Closed |
| 6FF4ED1 | N2 (R8 reconciliation of supersession authority) | **Reopened by B1**: R8's per-kind authority now reads an undefined key for most kinds |

### Phase B §3 closures and N1-N4 carry-forward

| Closure | Present reconstruction |
|---|---|
| Completeness polarity (Phase B N2), both directions | **Held.** §6 is unchanged. An alternate tree differing from `tree(a⁻)` only outside a recorded narrow basis carries a differing old-content run in (2) and a yielding present-content run in (4). Under a bounding judgment that becomes `P`, blocked, revoked or loss-withheld, both stay counted through `link⁻` (S0, no completeness read); losing the judgment only narrows (1) and (3) through `on⁺`. Restrictive direction: a stop is withdrawn only by a newly admitted narrow anchor linking a differing run. **Caveat:** B1 makes the supersession-disposal stop's authorization ambiguous; the staleness stop is unaffected |
| Support cycles fail closed; corrupt prefixes | Held: the §5.6 clamp and the §5.7 `INTEGRITY_HALT` are unchanged, and the judgment key and frame-acting record are S0/admission facts, adding no support edge |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (§6.8 unchanged) |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (§6.6 unchanged) |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; structure, quarantine, tenure; publication and fencing | Held. A fenced cutover's half state is disclosure N3 |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3 model limits) |
| Phase B N4 | Held (§32.3, with the R4 trigger added) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | `61cd09b` B1 gate trajectory: `H`'s `ACCEPT` in iteration 2's frame naming the run-1 `REJECT` | Held: authorized by key; ends the veto in that frame; vetoes in the admitted state while pending; lifted after integration |
| 2 | As 1, by the owner (`ADJUDICATE_DISAGREEMENT` holder) | Held; the obligation's trigger disappears where the relief acts |
| 3 | Run-`e1` `REJECT`, revert to the same revision by absorption (run `e3`), admitted-frame reassessment naming run `e3` | Held |
| 4 | Relief recorded in `X2`'s frame, evaluated in a third pending enactment `X3` that reaches the same revision | Held: does not act there, so the veto stands in `X3` |
| 5 | Holder's run-2 frame `UNQUALIFIED` superseding their run-1 `QUALIFIED` while run 1 is admitted | Held: acts only in the frame; admitted `gterm` stays `P` |
| 6 | Agent `NO_PASS` on `X1`; identical-content `X2`; owner's adjudicating `REVIEW PASS` in `X2`'s frame | Held under the "bound to" reading; a direct human record depends on N1 |
| 7 | Own assessor's `PASS` superseding their `FAIL` (same realization, obligation, reading) | **Fails: B1** (no key, so rejected as written) |
| 8 | Owner's or assessor's `PASS` of the same realization for another obligation or reading, naming `a⁻` | **Fails: B1** (admitted under the §6.7-words key) |
| 9 | `PLAN_ACCEPTANCE ACCEPTED {A1}` superseding `REJECTED {A1, B1}` | **Fails: B1 (ii)** |
| 10 | `EQUIVALENT MIGRATION` superseding `NOT_EQUIVALENT CONSUMER:k` | **Fails: B1 (iii)** |
| 11 | Owner withdraws an `IMMATERIALITY` by supersession | **Undefined: B1 (i)**; a challenge route exists |
| 12 | Cutover along the pending path: human record in `X`'s frame after the `TASK_RESULT`; `REVIEW(s, r)`, `ACCEPT` and gate derived from the ledger; integration checks 1-6 | Held |
| 13 | Agent submits the cutover `MODE_TRANSITION` with its `TASK_RESULT` | Held: refused (lifecycle record needs a human; not an implementer kind) |
| 14 | Carrier integrates first; the human records the cutover afterwards | **Fails: B2** |
| 15 | Cutover record in the frame of a long-integrated transformation | **Fails: B2 (iii)** |
| 16 | D2 cutover carried by a `MIGRATE` or `IMPLEMENT` transformation, pending | **Fails (non-blocking alone): B2 (i)**; conditions 1-6 still checked at integration |
| 17 | Fenced cutover integration | Fails closed; the "no half state" claim is false (N3) |
| 18 | Two cutover carriers for one subject in parallel | Held in substance: the second fails mode consistency after the first integrates (not stated explicitly) |
| 19 | Re-partition of an item revision after part 1 is discharged | Liveness defect (N2) |
| 20 | Fence kept: D1/D2 subjects at their earlier revisions in a new run | Held; now disclosed (R4, §22.3) |
| 21 | Direct human own-author `ACCEPTANCE PASS` after a `FAIL` answered `ACCEPT(s)` | Ambiguous (N1); §10.3 supports admission |
| 22 | Stratification and single-valuedness with the key-based authorization and the frame-acting cutover | Held: authorization is an admission fact; acting and mode are S0 |
| 23 | `D_n[X]` versus the post-integration state, with a frame-acting cutover | Held along the pending path; the late path (B2) has no frame-before-effect |
| 24 | `rid` of the cutover run: the carrying enactment, on the ledger before any record names it | Held |
| 25 | Phase B N2 polarity variants (section 5) | Held |
| 26 | Structure, `ignore` or analyzer change with `K` fixed | Held (guard unchanged) |
| 27 | `LEDGER_LOSS` over an enactment's integration; adverse records outside the acting rule | Held (unchanged) |

I stopped discovery in each family once its common cause and sibling list were characterized. Further siblings would be implementation-like:
- every remaining keyless kind's intended supersession semantics;
- every lifecycle kind's frame behaviour, though only `MODE_TRANSITION` declares a candidate frame.

Section 6 is a bounded negative result elsewhere, not a completeness claim.

## 7. Minimum architecture and capability transfer

- **What `f03b15e` changes.**
  - It replaces one identity (the supersession target) with a borrowed comparison.
  - It moves the cutover's conditions from the record's admission to the integration.
  - It names a carrier per domain.
  - It adds no component, store, record kind or tier.
- **The key repair (B1).** It was meant to remove the duplicated identity the `61cd09b` Review named. Instead it made one owner (§5.5 `same`) the definition for kinds that owner does not cover. Option 1 narrows it back; Option 2 restructures it.
- **Dropped capability (B1).** Under the literal reading, the reviewed own-assessor reassessment and the owner's adjudicating supersession of a failing assessment are lost. They are required by workplan §6.8 step 3 and by the evidence owner's supersession/adjudication sentence.
- **Withdrawn protection (B2).** The cutover's mechanical preconditions, which the workplan requires, are bypassable on the late-record route.
- **§30.** Accurate apart from the B1 claim of "one judgment key".
- **Architecture 1.6.0 supersession (PC-001).**
  - §26.4 preserves the version-bound Level 0 Core, the frozen profiles and the single composition root.
  - `orchestrator/docs/architecture.md` is byte-identical to `fad3ee4` (blob `39e6de7`).
  - Nothing under `source/` or `dist/` changed (section 10).
- **PEM Historical Applicability Set.** PEM was activated, because this is replacement of mature machinery under a memory-bound workplan. The PEM file at the candidate is blob `1561797`, equal to the checkout's, and schema-valid.

| Entry | Applicable | Disposition |
|---|---|---|
| PC-001 | yes | Held, as above |
| DS-001 | yes | Applied in N5: (P) and (Q) cannot discriminate B1 or B2 |
| FF-001 | yes, for genesis and cutover publication | Held for genesis (§19.9). B2 is a cutover enacted without its validation, the FF-001 shape in governance rather than publication |
| SP-001 | no | No source-to-package routing change |
| SP-002 | no | No immutable self-reference construction in this cycle |

I did not re-read the archived §18 inheritance workplans. The diff touches no inherited capability other than those noted.

## 8. Qualification-design adequacy

- **Status.** §31.1 correctly marks every runtime group `UNEXECUTED`. G1 needs only §31.10, which I ran (section 10).
- **Discrimination.** The real-owner requirement and the negative discriminators are adequate in form. (P) discriminates the `61cd09b` B1 cases and (Q) the pending-path cutover. But:
  - no case exercises assessment, `PLAN_ACCEPTANCE` or `EQUIVALENCE` supersession authority after the key change (B1);
  - no case integrates the carrier before the cutover record exists (B2);
  - (Q)'s `MIGRATE`-carrier `VIOLATION` expectation rests on a write-set effect the stated write set does not produce (B2 (i)).

  Per DS-001, a §31 implemented to the present expected values would encode both blockers.
- **Executed-evidence claims.** Nothing is claimed as executed beyond §31.10.
- **Diagnostic model.** Optional. I did not run it; it is unchanged and models none of the clauses at issue.

## 9. Doctrine-realization map and O1

- **Coverage.** All seven 7.2.1 entrypoints (four roles, three specialists) plus the scientific checks are mapped with E0-E3 levels. The diff does not touch §29.
- **§29.3, "durable authority mutation needs … human ratification where required" (E0).** It holds as presence. Under B2, a subject can enter native governance without the cutover gate on the late-record route. The map does not claim that case, but its presence claim depends on B2's repair.
- **Evidence-disagreement rows.** The rows claiming explicit supersession and adjudication of assessments depend on B1's repair.
- **Other rows.** No other row overclaims beyond the limits its E2/E3 level discloses.
- **O1 (§0.5).** Unchanged and adequate:
  - the realized record, readers, routine questions and realized-record architecture are stated;
  - product surfaces are marked within the deliverable;
  - **none** is marked beyond it.

  Product-scope acceptance remains with the stakeholder (S12). Technical Review accepts nothing.

## 10. What I verified and how; what I could not verify

**Verified.**

- Reviewed exactly `f03b15e55de77fe230f404fcb0b3bf12b21b6a3d` through a `git archive` snapshot in `$TMPDIR/ssds80-manual-review-f03b15e/`. Blobs confirmed: Manual `828222f…`, closure map `6540eed…`, workplan `91bde23…`.
- Diffed `61cd09b..f03b15e` by word for the Manual and the closure map (section 3).
- Read the Manual's Part 0, §1-§13, §16.6, §19, §22, §31.5-§31.6 and §32 in full, and the other sections' headings against the diff.
- Read the closure map §3-§5, the `61cd09b` Review in full, and the `OBLIGATION_ANSWERED` passages of the `e2154ac`, `b46c250` and `f22b4dc` records.
- Read workplan §6.8 step 3, checking for a fixed supersession target; it has none.
- Compared the `OBLIGATION_ANSWERED` sentence at `e2154ac`, `f22b4dc`, `61cd09b` and `f03b15e`.
- Read the governing owners at `aaeaf8b`:
  - the D3 role entrypoint;
  - architecture (formal-contract discipline, D3 Review);
  - evidence ("Assessment disagreement");
  - workflow (Review synthesis, "Human gates");
  - convergence (simplification trigger, review readiness, "Review strategy after recurrence").
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the candidate snapshot: **4 tests OK**.
- `git diff --check 61cd09b0b21a37cc4128e48afbd03998f3c65f85 f03b15e55de77fe230f404fcb0b3bf12b21b6a3d`: clean (exit 0).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 f03b15e55de77fe230f404fcb0b3bf12b21b6a3d`: 55 files. They are the Manual, `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`, and 53 files under `qualification/ssds80/`.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4` (empty diff; frozen blob `39e6de7`).
- PEM: `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` gave "PEM schema 1 valid: 5 families, 0 notices"; blob `1561797` at the candidate and in the checkout.

**Not verified or not established.**

- No production or runtime behaviour; none exists at G1.
- The diagnostic model was not run.
- I did not read §14-§15, §17-§18, §20-§21 and §23-§30 line by line; they are unchanged since `61cd09b`.
- I did not re-read every older Review record's prose or the archived §18 workplans. Section 5 states the depth.
- Both blockers are deductive from the Manual's own rules, and each premise is cited.
  - B1 depends on §5.5 defining `same` for exactly the nine kinds it lists, and on §8.3 step 3's "only by ... the same judgment key (the key the kind's §5.5 `same` test reads)".
  - B2 depends on the absence of any rule bounding a frame-`X` record to the time before `X`'s integration. I searched the candidate for one and found none. It also depends on §5.2's acting rule for integrated enactments.

## 11. Scientific-checks answers

- **Material findings.** None about scientific or numerical meaning. B1, B2 and N1-N6 are D3 findings about software that mediates scientific evidence:
  - B1 affects how a failing evidence assessment is disposed of by its assessor or owner, which decides whether a scientific claim stays visibly disputed;
  - B2 affects how a subject enters native governance.
- **Realized results.** I produced, ran and reviewed no realized scientific results. Null envelope: I examined the Manual's D3 text, the governing owners and prior Review records. Materially unexamined: any runtime evidence (none exists) and the diagnostic model.
- **Variants.**
  - Repair directions for B1: two, of kind D3 options. The criterion was to define supersession authority for every supersedable kind, keep the `61cd09b` B1 relief, and remove rather than add mechanism. Option 1 is recommended.
  - Repair directions for B2: one narrowing direction with three parts, plus one mechanism-adding option marked for the stakeholder.
  - Trajectories: 27, of kind out-of-matrix, chosen as high-information siblings of the two new mechanisms and of earlier families (section 6).
- **Reliance on accepted D1/D2 authority.** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was owed.
- **Gaps.** Runtime qualification (G2-G4), the unchanged sections not read line by line, the full prose of older records, and the archived §18 workplans.

## 12. Common-mode note

- **Family.** I am of the Claude family, the same as the Manual's author and as the reviewers of e2154ac, e9e6e9f, a18b544, 0b6c4fa, 27ef339, 5c55d4b, 575dc78, f7419d5, the same-family b46c250, f22b4dc, 362af9f and 61cd09b. The 3540d98, different-family b46c250 and Phase B reviewers were of the GPT family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session.
- **Shared dependencies.** Fresh context does not make me independent. I share:
  - the corpus;
  - the inherited workplan framing and its enactment, run, acting and key vocabulary;
  - the prior Review records, which I read and which shaped my attention to the newest clauses;
  - the toolchain;
  - the model family with the author and with most prior reviewers.
- **Provenance of the findings.** Both blockers were found by reconstruction from the candidate text, not from a prior record:
  - B1, by checking every kind §8.3 step 3 applies the new key to against the kinds §5.5 defines it for;
  - B2, by asking what bounds the cutover record's admission once its conditions moved to the integration.

  Both entered through repairs of the previous same-family Review's blocker directions. That repeats the pattern the handoff names and is evidence of shared-framing risk. A different-family review of the repairs would reduce it.

## 13. D4 statement

No SSDS 8 D4 is authorized. This Review accepts no architecture, product scope or proposed default. G1 remains open: it needs a repaired Manual candidate, an independent D3 Review with no surviving blocker, and explicit stakeholder acceptance. Shadow implementation additionally needs G2.

# SSDS 8 Architecture Manual — Independent D3 Review, candidate 0b6c4fa

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 0b6c4fa4ffb22313d3c791958ded1b7157350532
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: b5422602894fcc0e7c9920dbaf0ef49d428c1592 (checked)
    CLOSURE MAP BLOB: a1dce7ba56fd4cc63071ec0e664e0b1d41d77bd6 (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756, read for §6.6, §21 and the tenure text);
           blob at this candidate 91bde236465178f20c7348280e036d2884dfc216 (checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC,
           E9E6E9F, A18B544
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           clauses changed since a18b544, including the repairs of that round's non-blocking findings;
           prior-finding regression; required structural checks; no implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section references are to the exact candidate. The checkout HEAD was the later handoff commit `cc09ec61`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`:
- `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract and scientific checks);
- `architecture-and-design.md`;
- `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
- the cited sections of `evidence-evolution-and-dependencies.md`.

`abstraction-and-concretization.md` and the other concern owners were not loaded: no decision below turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** Both blockers are defects of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a gap between them, or between the Manual and a stakeholder direction, is not a challenge to accepted authority.

Baseline owner text applied:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- D3 owner, "Architecture design test": prefer "one authoritative representation/state".
- Evidence owner, "Applicability, immutable observation, and superseding assessment": "A stale passing observation is not admissible confirmation."
- Evidence owner, on positive guidance: "Do not suppress contradictory admissible observations to manufacture a pass".
- Evidence owner, on assessment disagreement: "When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence."
- Convergence owner, "Active simplification trigger": simplification is mandatory before another additive durable repair when evidence shows "repeated patches around the same mechanism, patch-on-patch repair", "duplicated/synchronized authoritative state, competing authorities".

## Verdict

**NO-PASS.** Two D3 blockers survive. Each is stated at family level, as method step 6a requires, and each entered through this round's repairs of the a18b544 record's own suggestions.

- **B1 (assessment-disagreement matching family, thirteenth finding; adverse side, permissive effect).**
  - The a18b544 B1 repair removed observed reads as a closure bound. Every execution without a current `COMPLETENESS(EXEC)` judgment now records the whole tree. That is every effective unit as a unit entry, plus a `{ prefix = "" }` entry over every tracked path.
  - The repair correctly closes the passing side: currency and `on⁺`.
  - But the same single record feeds `on⁻`. So for every unbounded execution, the adverse uses ((2), (4), `adm`, the floor and the class rule) now compare whole trees. An admitted change anywhere, even to a file no execution read, makes "the same content" different.
  - Consequences:
    - (2) and (4) lose differing and yielding runs;
    - a flaky failure is made stale by one flaky pass after an unrelated edit;
    - the reviewed Phase B N2 property fails when completeness is lost before a run is realized;
    - D1/D2 floor and class tests degenerate.
  - The Manual labels the change "a restrictive change". It keeps statements that are now false: R1's "granularity is the reviewed `on`'s"; §6.6's ignored-file example; §6.8's "both directions are therefore conservative"; §32.2's "bounded to representation-only differences".
  - Under the reviewed contract, a runner with complete observed reads had a narrow basis on both sides.
- **B2 (gate-decision family, fourth round).** The a18b544 B2 and N1 repairs key gate support on one standing decision per gate obligation, and add a tenure filter. But that filter sits only inside `valid`. Its escape "(or bound to it, §7.6)" is defined only for prospective *acceptances*. The GATE obligation's identity, its trigger, its answered state, discharge and the Admission standing-decision check do not read tenure. So:
  - **(a)** a new or promoted gated subject whose gate was decided on the candidate, as §11.5 requires, is permanently invalid after integration, while its obligation is discharged and nothing is re-derived;
  - **(b)** after a version rollback and re-cutover, or a demotion and restoration, of a gated non-D1/D2 subject at an unchanged triple, the earlier tenure's decision is excluded from `valid`. Yet it still answers the obligation and blocks every other holder's decision;
  - **(c)** discharge still counts the earlier tenure's decision.

Everything else this round targeted closes the trajectory it names:
- the a18b544 B1 trajectories A and B, siblings (i)-(iii) on the passing side, and the §31.2 discriminators A-D;
- a18b544 B2 (a1)-(a3), (b1), and (b2) for D1/D2 runs;
- N2-N5.

The D1-D3 change rule has no new blocker; one wording residue is N5. This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — The fail-closed whole-tree fallback, recorded once, is fail-open for every adverse use

**Earliest owner.** Manual §6.3 "executed content" and "Recorded execution basis" (refinement R1), read by §6.5 `on⁻`, §6.6 (2) and (4), and §6.8 `adm`, the floor and the class rule. These are workplan §21 item 4 (executed content: "execution basis, observed runner reads, whole-tree fallback") and item 5 (`on`, `stale`, discriminating readings). It is a D3 defect and asks no new D1/D2 rule.

**Owner and contract text.**
- Evidence owner (quoted above): preserve material disagreement; do not suppress contradictory admissible observations to manufacture a pass.
- Workplan §6.6, the reviewed contract, includes two clauses:
  - "Where no current completeness judgment bounds the closure and the runner's observed reads are not complete, the widening reaches the whole governed tree: missing dependency knowledge never proves that two executions read the same content."
  - "(1) and (2) need an identical second execution on the content `a-` read and no other outcome there, ever".
- Phase B Review N2 makes two points:
  - "applying fallback indiscriminately to both polarities would remove a differing old-content run or a yielding current-content run";
  - "Both the differing-old-run and yielding-current-run must continue qualifying the claim."
- Phase C handoff §5 adds two more:
  - "Losing completeness must not raise support by hiding either run";
  - "rewriting it to global fallback is a semantic regression, not clarification".
- Manual §6.3 now says: "Only a current completeness judgment bounds the closure …; observed reads add read entries and never bound it, so where no judgment bounds the closure the widening reaches the whole tree (a18b544 B1; refinement R1 drops the reviewed alternative bound "the runner's observed reads are complete", a restrictive change)".
- With no judgment, §4.6 sets `W := X_m` (every effective unit), and §6.3 records "unit entries: for every unit the closure reached" plus the whole-tree widened entry "over every tracked path, governed or ignored". So the record is the whole tree twice over. Removing the `{ prefix = "" }` entry alone would not narrow it.
- §6.5: "`on⁻(o, K)` ⇔ every recorded term (t, c) of a unit, read or widened entry of o's execution basis has cid(resolve_o(t, K)) = c".
- §6.6, "Nondeterminism goes to the owner": "(2) no other outcome on that content, ever". Its polarity bullet: "a run on content that differs from `tree(a⁻)` only in another span of a recorded file, in another unit's file or in an ignored file stays in (2), and a run on present content that differs only there stays in (4)."
- §6.8: "a candidate change outside the recorded regions leaves `adm(a⁻)` true. The floor uses `adm`, and the class rule uses `¬adm`; both directions are therefore conservative."
- §32.2: adverse narrowing "is bounded to representation-only differences".

**Trajectory (i): nondeterminism hidden and a live failure made stale.** This is the primary trajectory and is blocker-grade on its own.

1. A Dispatcher-controlled runner class whose harness records every in-tree file read (§4.2, §16.4). Specification `S`, declarative oracle, `l2_error`. The solver races, so it fails about half the time with no runner-supplied seed: unrecorded variation, §6.10. No `COMPLETENESS(EXEC)` judgment exists, which is the normal state of a newly adopted repository.
2. On `T1`, `o1` fails; it is `a⁻`, counted. The rerun obligation's reproduction `o2` on `T1` fails identically.
3. An admitted change edits `docs/notes.md`, which `S` never reads, giving `T2`.
   - Every record holds a unit entry for the docs unit and the whole-tree entry, so `o1` and `o2` are not `on⁻ T2`.
   - `a⁻` "counts again in G until one execution on the new content … shows it not yielded" (§6.6).
4. The rerun `o3` on `T2` passes. Its read entries equal `o1`'s.
5. Evaluate in `T2`:
   - (1) holds via `o2`.
   - (2) holds, because only `o1` and `o2` are `on⁻ T1`; `o3` differs in the docs entry.
   - (3) holds via `o3`: `ext` is equal, and `on⁺` holds through the same root tree.
   - (4) holds, because no yielding run is `on⁻ T2`.

   So `a⁻` is stale. With `o3`'s passing assessment, `ev` and `valid` reach `T`. For a D1/D2 claim the floor event "(2) has failed" never fires.

Under the reviewed contract, complete observed reads bounded `o1`-`o3` to `S`, its declared closure and the reads. Then `o1` is `on T2`, so (4) is false. And `o3` is `on T1` with another outcome, so (2) fails: "otherwise nondeterministic in fact", and the case goes to the owner and, for D1/D2, to the floor. The contradiction between `o1`/`o2` and `o3`, on content the runner recorded as identical, is suppressed by a difference nobody read.

**Siblings (same cause: the recorded basis width is chosen for the permissive polarity and read by the adverse one).**
- **(ii) Phase B N2, record-time variant.**
  - Setup: `a⁻` is recorded under a current judgment `c`. Then `c` becomes `P`, blocked, revoked or loss-withheld before the differing old-content run, or the yielding present-content run, is realized.
  - Effect: that run records the whole tree. It is `on⁻ tree(a⁻)` (or `on⁻ G`) only on an identical tree. On the alternate tree that differs only outside `a⁻`'s narrow basis, it leaves (2) or (4).
  - Losing completeness has therefore hidden the run and can raise `undisputed` to `T`. §31.3's "Completeness polarity" case records both runs while `c` is current, so it does not see this.
- **(iii) Floor and class.**
  - Setup: a flaky D1/D2 failure of admitted content is surfaced by the run of a candidate that changed only a document.
  - `adm(a⁻)` = `on⁻(real(a⁻), T_b)` is false, because the candidate tree differs from `T_b` somewhere and the basis is the whole tree. So the "`adm`" floor trigger never fires.
  - A base run `p` that passed on `T_b` gives `on⁺(p, T_b) ∧ ¬adm`, so a discriminating reading drops from R3 to R2 as "candidate-own".
  - §6.8's claim "both directions are therefore conservative" holds per basis. It fails when the basis width differs.
- **(iv) Pre-existing in the reviewed contract.** For runners whose observed reads were *not* complete, the reviewed contract already recorded the whole tree. So (i)-(iii) already applied to them, and no document discloses it. The candidate extends that cost to every unbounded execution and states the opposite polarity.

**Surfacing.** The change to workplan §6.6 is listed, but as "a restrictive change". It is restrictive for currency and `on⁺`, but permissive for (2), (4), `adm` and the floor. Four statements now contradict the mechanism:
- R1's "the granularity is the reviewed `on`'s, so a change outside the recorded regions (… another unit's file, an ignored file) changes neither predicate";
- §6.6's ignored-file and other-unit examples;
- §6.8's "both directions are therefore conservative";
- §32.2's "bounded to representation-only differences".

An implementer must choose between the mechanism and these statements. The stakeholder chose no repair direction for the a18b544 recurrence (N1). So nothing on record accepts this cost.

**Family assessment (convergence owner, "Review strategy after recurrence").** This is the fifth successive round in which a recorded execution basis does not serve both polarities:
- 3540d98 B1;
- e2154ac B1;
- e9e6e9f B1;
- a18b544 B1;
- now this.

It entered through the a18b544 record's own subtractive option (a). That option costed only the passing side ("Cost: more whole-tree fallbacks").

The shared cause is a two-polarity tension that no single recorded width can satisfy whenever the basis is not known to equal what was read:
- a wide basis is fail-closed for currency and `on⁺`, but fail-open for (2), (4) and `adm`;
- a narrow basis is the reverse: it would resurrect settled failures through runs on genuinely different content (workplan `ba7f738` U1b).

The reviewed contract resolved the tension only where reads were completely observed. The construction rule governs predicate polarity per record, never the polarity of the recorded width. This is a **non-local recurrence**. Further sibling search (tracer fidelity, partial bounds per closure step) would be implementation-like.

**Options for the stakeholder (Phase C handoff §5), not a single repair.**
- **(a) Adds mechanism.** Use an adverse-only exact core.
  - When a runner class declares complete in-tree read observation, qualified at G3 and including directory enumerations and absent-path probes as membership and absence entries, `on⁻`, `adm` and (2)/(4) compare only the declared-closure unit entries and the read entries. The widening enters only `on⁺`.
  - An over-narrow core keeps more runs counting, so a defective tracer costs only restrictively.
  - Currency and `on⁺` keep the whole-tree fallback, so a18b544 B1 stays closed.
- **(b) Subtractive.** Drop `on⁺`'s same-root-tree disjunct, so only an observation whose basis a current completeness judgment bounds serves (1) or (3).
  - Unbounded failures then go to the owner, as SD-18 failures do, and no unbounded stop can hide a contradiction.
  - Cost: red-then-green iterations need `COMPLETENESS(EXEC)` judgments.
- **(c) Subtractive, disclosure only.** Keep the mechanism and correct R1, §6.3, §6.6, §6.8 and §32.2. Add §31.3 cases and a §32.3 trigger. The stakeholder then explicitly accepts that, for unbounded executions, disagreement, nondeterminism and the admitted-content test hold only within one exact tree.
- **(d)** A different-family Review before repair (SD-22 already called for one).

**Required discriminators.** These run at the real Dispatcher → Admission → Derivation (`stale`, `adm`, floor, class) → discharge owners, with nothing seeded resolved:
- **(A)** Trajectory (i): `a⁻` is not stale in `T2`; the owner's adjudication obligation is derived; for a D1/D2 claim the floor fires.
- **(B)** Sibling (ii), with `c` becoming in turn `P`, blocked, revoked and loss-withheld *before* the alternate-tree run is realized: the claim stays qualified (`undisputed = P`).
- **(C)** Sibling (iii): the doc-only candidate's flaky D1/D2 failure keeps class R3 and reaches the floor.

The expected values depend on the option chosen. Under option (c), §31.3 must instead state and test the disclosed behavior, and the four contradicted statements must be gone. None of §31.2-§31.3 discriminates (A)-(C) today: the §31.2 "Closure bounding" cases test the passing side only.

### B2 — Gate tenure is a `valid`-only filter that every other gate consumer ignores, and frame-decided gates can never satisfy it

**Earliest owner.** Manual §5.5 (gate term, `standing h`, the tenure filter and "One standing gate decision"), with:
- §7.5 (declared frames), §7.6 (binding);
- §10.2 (`GATE(g)` trigger and parameters), §10.3 (answered obligations), §10.4 (discharge);
- §8.3 step 7 (standing-decision admission);
- §11.5 (integration flow);
- §19.4-§19.7 (restoration, cutover, rollback);
- R10 and R11.

These are workplan §21 items 3, 7, 10 and 13. It is a D3 defect.

**Owner and contract text.**
- Manual §5.5 makes three statements:
  - "standing h: the gate obligation's one passing decision not superseded";
  - "required-kind judgments j' and gate decisions h count only if admitted at or after τ(s) (or bound to it, §7.6)";
  - "The qualification follows its decision's obligation, so its run and tenure … a new run's or tenure's gate decides afresh".
- §7.6 defines binding only for acceptances: "A prospective acceptance `j` made in the frame of `X_0` counts for the tenure that `k` starts iff". §7.5 lists the frame-declaring records without `GATE_DECISION`.
- §11.5 step 3: integration is requested "Once the claimed obligation's discharge predicate would hold on the candidate — clean conformance, current review judgments, required gates". So required gates are decided on the candidate, before the tenure a new subject receives at integration.
- §10.2 makes two statements:
  - `GATE(g)` is triggered by "a required human gate without a current `ACCEPT`";
  - a gate decision "is in the run iff … it is a frame record of the transformation whose integrating admission is `run(s)`".

  Only `NATIVE` D1/D2 obligations carry `run(s)`.
- §10.3: "`ACCEPT` and `GATE`: the subject triple `(s, scope_id(s), cur(s))`"; "An answered obligation is never ready again".
- §10.4: "every human gate of o has a current standing authenticated ACCEPT". This has no tenure condition.
- §8.3 step 7: a passing `GATE_DECISION` on an obligation "that already has a standing passing decision … is admitted only as a supersession of that decision". §8.3 step 3 limits that supersession to the decision's own author or the owner.
- Workplan (reviewed): "even an admitted restoration starts a tenure that excludes every earlier judgment".
- R10: "derives a new revising review, acceptance and gate".

**Trajectory (a): a new gated subject can never be valid. Primary; blocker-grade on its own.**

1. A `PLAN` item of kind `AUTHOR` (authority D2), with `gates = ["d2-owner-review"]`, declares a new D2 subject `numerics.method2` over uncovered content (§13.2 permits this). Policy requires that human gate for D2.
2. In frame `X`, the following are admitted before integration:
   - review;
   - the AUTHOR task's revision-assessment record;
   - an R3 prospective `ACCEPTANCE`;
   - holder `H`'s `GATE_DECISION` `h`: `ACCEPT`, `ADEQUATE`, `UNQUALIFIED`, at position `p`. §10.2 derives `GATE` in a frame for a prospective tenure.
3. Integration `k` passes step 7: the discharge predicate reads `h` as current, with no tenure condition. `τ(s) = k`.
4. After `k`, the gate term is empty and `valid(s) = F`:
   - `ACC` holds the bound acceptance;
   - the required-kind human acceptance is bound;
   - but `h` was admitted at `p < k`, and nothing defines `h` as "bound".
5. Yet:
   - `h` is current: it is in the run, with base `T` and basis holding. So `GATE(g)` is not derived, and its obligation is answered anyway.
   - `REVALIDATE(h)` is not derived.
   - The AUTHOR obligation is `DISCHARGED`.
   - No inspector entry exists.
   - Every subject relying on `numerics.method2` through a `validity` entry is `F`.

   Only `H` or the owner can record a superseding decision after `k`, unprompted. Any other holder is refused (`AUTH_SUPERSEDES`).

The alternative reading, extending §7.6 binding to gate decisions by analogy, is an architectural choice the text does not make (§7.5 does not even list gate decisions as frame records). Either way, the implementer must choose between §5.5's filter and the §10.2/§11.5 flow.

**Trajectory (b): an earlier tenure's decision both excluded and blocking.**

1. A `NATIVE` D3 subject `s` has a policy-required human gate. `H1` accepts at `(s, σ, r)`.
2. A version rollback (§19.7) moves `s` to `LEGACY(p)`. A later re-cutover returns it to `NATIVE` at the same `r`: a new tenure.
3. Non-D1/D2 GATE obligations carry no run or tenure parameter. So `GATE(g)` on `(s, σ, r)` has the same identity and is already answered by `h1`.
4. Consequences:
   - `h1` is current, so `GATE(g)` is not derived;
   - `valid` excludes `h1` by tenure, so `valid(s) = F`;
   - the cutover's gate holder `H2`, or any holder other than `H1` and the owner, is refused on that obligation.

Demotion and restoration, a kind round trip, or a mode round trip at an unchanged triple give the same result.

**Sibling (c).** For a restored subject at an unchanged triple, §10.4 still counts the earlier tenure's `h` for any obligation carrying that gate. So the a18b544 N1 revival survives in discharge, while `valid` excludes it.

**Family assessment.** This is the fourth successive round in the gate-decision family:
- 3540d98 B3;
- e9e6e9f B2;
- a18b544 B2;
- now this.

It entered through this round's repair of a18b544 B2, together with the repair of N1 ("Filter both terms by τ(s)"); both were same-family suggestions. The shared cause is the one SD-22 removed for D1/D2 revisions: a condition stated in one consumer (`valid`) instead of in the record's target condition and the obligation's identity. That leaves the trigger, the answered state, discharge and Admission's standing-decision check reading a different key. The convergence owner names this "duplicated/synchronized authoritative state, competing authorities". It is a **non-local recurrence**.

**Options for the stakeholder.**
- **(a) Subtractive; reuses the SD-22 pattern.** Make tenure a target condition:
  - A `GATE_DECISION ACCEPT` (and a required-kind judgment) on `(s, σ, r)` is current only within `s`'s current tenure. That means admitted at or after `τ(s)`, or a frame record of the transformation whose integrating admission started `τ(s)` or of an earlier iteration or rebase of its enactment lineage. This is the §10.2 run-membership wording applied to tenure.
  - Parameterize `GATE(g)` by `τ(s)`.
  - Add `GATE_DECISION` to §7.5.
  - Delete the `valid`-only filter.

  Every consumer then reads one condition.
- **(b)** Revert the N1 repair. Accept the earlier tenure's gate revival for non-D1/D2 subjects as a disclosed residual, and narrow §19.4's lock statement.
- **(c)** Require gates after integration for new tenures. This changes §11.5's flow.
- **(d)** A different-family Review first.

**Required discriminators.** These run at Admission, Derivation (`valid`, triggers, discharge) and the inspector view:
- **(A)** Trajectory (a): after integration, `valid(s) = T` (`P` if the decision is `QUALIFIED`), and discharge and `valid` agree.
- **(B)** Trajectory (b), plus demotion and restoration: `GATE` is derived for the new tenure; any qualified holder may answer it; `valid(s) = T` after the answer; and the earlier tenure's decision neither counts nor blocks admission.
- **(C)** Sibling (c): discharge does not count an earlier tenure's decision.
- **(D)** In every case, `valid`, discharge, the `GATE` trigger, the answered state and step 7 agree on which decisions count.

§31.6 "One standing decision" tests a D1/D2 tenure restart only, where `run(s)` hides the defect. It does not test a frame-decided gate on a new subject or a non-D1/D2 restoration.

## 2. Non-blocking findings

- **N1 — Repair directions chosen without a recorded stakeholder decision (coordination; routed to the stakeholder).**
  - The a18b544 record classified both blockers as non-local recurrences and listed options for the stakeholder.
  - Phase C handoff §5 says "do not choose a new direction silently". The continuation handoff §3.1.4 says "present the options to the stakeholder first".
  - The stakeholder record ends at SD-24, and the candidate adopted option (a) for both. That includes dropping a Phase B-reviewed workplan clause (R1) and narrowing SD-24 further (N2).
  - The handoff says the stakeholder authorized continued work. Whether that authorization covers these choices is the stakeholder's to confirm. Both blockers entered through these choices.
- **N2 — The second holder's route is evadable, and SD-24's realization is narrowed further.**
  - A holder other than the standing decision's author can no longer record a `QUALIFIED` acceptance; it "raises a challenge against the standing decision instead" (§5.5).
  - Nothing stops the author from superseding a record under an open blocking challenge (§8.3 step 3). The new decision is unchallenged, so the gate returns to `T` while the challenge's `ADJUDICATE` stays open against a superseded record.
  - A challenge against the subject triple, or a gate `REJECT`, would not be evadable.
  - Either:
    - direct holders to those routes; or
    - refuse supersession of a record under an open blocking challenge (adds one Admission check).

    In both cases, surface to the stakeholder that SD-24's "until an unqualified gate decision" now admits only the first holder's qualification.
- **N3 — Revalidating a gate decision.**
  - A gate decision whose evidence core goes stale derives `REVALIDATE(h)`, held by "the role of x's kind", yet only `h`'s author or the owner may record its successor.
  - §3.5 does not require the policy adjudicator to be a qualified holder of that gate, so the obligation can be unanswerable.
  - Either state that floor or route `REVALIDATE` of a gate decision to its author or the owner.
- **N4 — The inspector entry's closing condition.** §16.8 keeps a `QUALIFIED` entry open "until an `UNQUALIFIED` decision supersedes it or its obligation stops being derived". `GATE(g)`'s trigger ("without a current `ACCEPT`") is false while the current `QUALIFIED` decision exists, so, read literally, the entry closes at once. Key it on the decision's target ceasing to be current instead. This is e2154ac N2(b) resurfacing.
- **N5 — Write-set attribution wording (D1-D3 change-rule family; entered through the a18b544 N3 repair).**
  - §1.2 and §14.5 now attribute a file's entry type and mode "to the innermost unit whose term resolves to it", read as exclusive.
  - Where top-level subjects of different kinds hold incomparable span terms in one file, "innermost" is undefined. An `IMPLEMENT` item's mode change could then be attributed to the D4 unit alone, while the D2 unit's `cid` (which hashes the mode) changes.
  - Validity and the revising duty still fail closed, because the revision and run change.
  - Fix: attribute the file to every unit a term of which resolves into it, and reserve "innermost" for byteless entries.
- **N6 — Whole-tree entry representation.**
  - §1.8 still says the empty prefix denotes "the whole governed tree".
  - The record uses the same term syntax `{ prefix = "" }` for "every tracked path, governed or ignored" (§6.3). Re-resolution under §1.3 and the recorded `ignore` would drop ignored files.
  - Give the whole-tree entry its own term kind. §31.2 (D) discriminates the failure.
- **N7 — Accounting.**
  - §30 counts neither the standing-decision admission rule nor the gate tenure filter.
  - §31.6 still says the supersession "lifts the cap".
  - Closure-map rows 3, 4 and 7 say DECIDED.
  - §29.3's E0 row "execution change derives rerun obligations" is now true. The §6 disagreement claims behind §29.4 and §29.7 rest on B1 and B2.

  The aid confers no authority.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly; the closure map was used only as an index. "Answered" means a substantive D3 answer exists; it is neither runtime evidence nor stakeholder acceptance.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | Answered; N5 and N6 are wording residues |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 6.8, 17.1; gate `adequacy` and `qualification` (§3.4, §5.5) | Vocabulary answered; gate support and tenure semantics carry **B2** |
| 4 | §§4.1-4.6, 6.3 | **Not substantively closed (B1)**: the one recorded basis is fail-open for adverse uses whenever no judgment bounds it |
| 5 | §§5-7, 17, 22.3 | `on`, `stale` and `adm` carry **B1**; strata and monotonicity hold (`unq` is an S0 constant) |
| 6 | §§8, 21-23 | Answered (R4 sound, as before) |
| 7 | §10 | **Not substantively closed (B2)**: discharge, triggers and the answered state disagree with `valid` on gate tenure |
| 8 | §11, §13.2, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered, except the §16.6/§16.8 Channel C realization of a qualified gate (B2; N2, N4) |
| 11 | §§17, 6.10 | Answered; runner declarations hold, and the adverse width is B1 under item 4 |
| 12 | §18 | Answered |
| 13 | §§19-20 | **Not substantively closed (B2)**: restoration, re-cutover and promotion of gated subjects |
| 14 | §§21-25 | Answered; runtime unexecuted |
| 15, 16 | §25.1-§25.3 | Answered |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered (submodule reachability disclosed) |
| 21 | §29.7 | Answered; the Channel C row depends on B2 |
| 22 | §30 | Present; N7 |
| 23 | §12, §1.2/§13.2 | Answered |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted; N5 for diff mapping |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; N7 |

**Workplan §16.2, both tables.** §26.4 is unchanged since e2154ac (diff). I re-read it against both workplan §16.2 tables. Every **Deferred** row has a final disposition: invariants 4, 9, 15, 17 and 26; §5 sub-rules; §6; §7 mappings; §12 configuration; §18 fitness. None is merely routed.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table remain correctly `[delegated]`. Two architectural decisions are left implicit:
- the polarity of recorded basis width (B1);
- whether gate decisions are frame records, and whether they bind to a tenure (B2).

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | The construction rule, the guard, `on⁺ ⇒ on⁻` and set-valued `ext` are sound per recorded basis. **The a18b544-round change of recorded width is a change needing different treatment (B1).** It is two-sided, not "restrictive", and three of R1's own claims no longer hold for unbounded executions |
| R2 | Sound. `unq` is S0, so "forcing only lowers values" holds |
| R3 | Sound; unchanged |
| R4 | Sound within its crash model; residuals disclosed; unchanged |
| R5 | Sound |
| R6 | Sound. Anchor lines in unclassified types are now recognized syntactically and kept in identity (a18b544 N2 closed) |
| R7 | Sound; unchanged |
| R8 | Sound. "Same target" for `GATE_DECISION` is now the obligation. Supersession of a record under an open blocking challenge is unconstrained (N2) |
| R9 | Sound; unchanged |
| R10 | Sound for D1/D2 runs. "Across tenures nothing revives" is realized only in `valid`, not in triggers, the answered state or discharge (B2) |
| R11 | **A change realized unsoundly (B2).** It also narrows SD-24 beyond R11's earlier listing: a second holder can no longer record a qualification (N2). No stakeholder decision records the choice (N1) |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence. Prior records were read as hypotheses.

The diff from a18b544 touches only §0.3, §1.2, §1.5, §2.6, §5.5, §6.3, §8.3 steps 3 and 7, §10.4, §14.5, §16.8, §31.2, §31.6, §32.2, §32.3 and closure-map rows 3, 4 and 7. For findings whose cited text lies elsewhere, I confirmed from the diff that the text is unchanged since a18b544, re-read it in the whole-Manual read, and give the basis tersely. I did not re-derive each of them from scratch (section 13).

### A18B544 (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Closed on the passing side.** (A) A data change makes `q` non-current (whole-tree entry). (B) `o3` is not `on⁺ T3`. (i) Enumeration and absence: tracked membership is in the whole-tree entry. (ii) Ignored tracked files are covered. (iii) Git-data reads are external reads, and passing currency is disclosed (§32.2). **The family reopens on the adverse side as B1 here** |
| B2 | (a1)-(a3) **closed**: a superseded decision never revives, and the standing one's challenge, block or loss lowers the gate term to `F`. (b1) **closed**: the target is the obligation. (b2) **closed for D1/D2** through `run(s)`; for non-D1/D2 tenure restarts the family reopens as **B2** here |
| N1 | **Partly closed.** `valid` now filters by tenure; triggers, the answered state and discharge do not, and frame decisions cannot pass the filter: **B2** |
| N2 | Closed (§1.5 syntactic recognition in unclassified types) |
| N3 | Closed for empty files and gitlinks. The new attribution wording leaves N5 |
| N4 | Closed (§32.2 LFS and submodule disclosure; §32.3 trigger) |
| N5 | Closed (§32.2 passing-side disclosure) |
| N6 | Partly closed: the history sentence is complete; the residue is N7 |

### E9E6E9F (same family)

| ID | Disposition and basis |
|---|---|
| B1 | Closed: A-E, with the E wording now in §1.2 and §14.5 (N5 residue) |
| B2 | Closed for its currency-lifting routes; the cap is now the standing decision's own qualification |
| N1 | Closed (`AUTH_ILL_FORMED`) |
| N2 | Closed |
| N3 | Closed |
| N4 | Superseded by the a18b544 B1 repair: closed permissively, adverse cost B1 |
| N5 | Closed |

### E2154AC (same family)

| ID | Disposition and basis |
|---|---|
| B1 | Closed for its trajectories |
| N1 | Closed |
| N2 | (a) and (c) closed; (b) **partly closed** (N4 here) |
| N3 | Closed |
| N4 | Closed |
| N5 | Closed |

### 3540D98 (different family)

| ID | Disposition and basis |
|---|---|
| B1 | Closed: binary, line-ending, mode and link identity |
| B2 | Closed: full `(locator, pin)` set |
| B3 | Closed for its trajectory (`QUALIFIED` gives `P`; `INADEQUATE` refused); family open as B2 here |
| B4 | Closed |
| N1 | Closed |
| N2 | Held as disclosure |
| N3 | Held as disclosure |
| N4 | Held as disclosure |

### 798B2B4, 71CF9B3, 86AB683

Text unchanged since a18b544; re-read.

| Review | ID | Disposition |
|---|---|---|
| 798B2B4 | B1-B3 | Closed: revision run as `tgt`; frames never integrated are in no run; predecessor display only |
| 798B2B4 | B4 | Closed: links recorded |
| 798B2B4 | N1-N8 | Closed |
| 71CF9B3 | B1-B2 | Closed: run start; S11/R10 restored |
| 71CF9B3 | N1-N8 | Closed |
| 86AB683 | B1 | Closed: the record counts in the run with standing |
| 86AB683 | N1-N7 | Closed |

### 1FFBBF0, 53669A5, D837363

| Review | ID | Disposition |
|---|---|---|
| 1FFBBF0 | B1 | Closed. The SD-18 flag again has only its out-of-tree meaning |
| 1FFBBF0 | B2 | Closed (§8.3 step 7 in every frame) |
| 1FFBBF0 | N1-N7 | Closed; N2's wording residue now N5 |
| 53669A5 | B1-B3 | Closed |
| 53669A5 | N1-N9 | Closed |
| D837363 | B1-B4 | Closed |
| D837363 | N1-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | ID | Disposition |
|---|---|---|
| CC005DB | B1-B3 | Closed |
| CC005DB | N1 | Closed: ignored tracked reads are now covered for currency |
| CC005DB | N2-N8 | Closed |
| C6DA678 | B1-B3 | Closed |
| C6DA678 | N1-N12 | Closed |
| B595F2C | B1-B4 | Closed |
| B595F2C | N1-N8 | Closed |
| 6FF4ED1 | B1-B4 | Closed: `on⁺ ⇒ on⁻` with frozen context; any prose change is R2; analyzer pinning; `AUTHOR`/`DOCUMENT` routes |
| 6FF4ED1 | N1-N2, N4-N12 | Closed |
| 6FF4ED1 | N3 | **Partly closed**: qualification propagates through the standing decision, but the tenure defect is B2 |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| Y1/Y2 coverage and candidate-own latch | Held (§6.6 coverage, §6.8). The class rule's `¬adm` degenerates for unbounded bases (B1 iii) |
| EF8445A/552AC01 N2: strata, completeness polarity | **Re-tested.** I used an alternate tree differing only outside a recorded narrow basis, with a differing old-content run and a yielding present-content run, both recorded while the judgment `c` was current. With `c` then `P`, blocked, revoked or loss-withheld, both runs stay in (2) and (4): **held**. **The record-time variant fails** (B1 ii): when `c` is lost before such a run is realized, the run records the whole tree and leaves (2) or (4) |
| Absorbed relaxation; identical-outcome floor; X1-X3 | Held |
| Promotion, refinement, enactment | Held for acceptances. Gate decisions on promoted or new subjects carry B2 |
| Adversity versus currency, challenge, loss | Held. A gate superseder's standing is now read through `current` (a18b544 B2 a closed) |
| Salvage, retirement, supersession authority; scope anchors, home, independence; start latch | Held |
| U1/U2/W1/W2 executed content | Held for currency. **The adverse side is B1** |
| Contrary-run retention, nondeterminism | **Fails for unbounded bases (B1 i)** |
| Fail-closed support cycles; corrupt prefixes | Held: no new S2 edges (`unq` is S0); `INTEGRITY_HALT` unchanged |
| Effective structure, quarantine, tenure | Held, except gate tenure (B2) |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N2 | As re-tested above |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held as reopen triggers (§32.3) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | Hermetic class, no in-tree tracing, no judgment; tracked data changes (a18b544 B1 A) | Held: non-current; `REALIZE` derived |
| 2 | a18b544 B1 B (`T1`/`T2`/`T3`) | Held: no stale without a run on `T3` |
| 3 | Glob picks up an added tracked file; probed absent file later added | Held |
| 4 | Ignored tracked input under the fallback | Held (§6.3); representation residue N6 |
| 5 | Version string derived from `.git` | Held as an unpinnable external read; passing currency disclosed |
| 6 | Tracing runner, unbounded, flaky test, unrelated doc edit, one flaky pass | **Violation (B1 i)**: stale; `ev = T`; no floor |
| 7 | Completeness lost before the alternate-tree differing or yielding run is realized | **Violation (B1 ii)** |
| 8 | Doc-only candidate surfaces a flaky D1/D2 admitted-content failure | **Violation (B1 iii)**: `¬adm`; no `adm` floor; class R2 |
| 9 | Phase B N2 with runs recorded under the current judgment | Held |
| 10 | `h_q`, then `h_u` by its author; `h_u` revoked, blocked or loss-withheld | Held: gate term `F` |
| 11 | Lifting decision rendered at a later head | Held: target is the obligation |
| 12 | D1/D2 revert or tenure restart after a `QUALIFIED` gate | Held: new run, any holder |
| 13 | New gated D2 subject by `AUTHOR` item; gate decided in the frame | **Violation (B2 a)**: `valid = F` forever; obligation discharged |
| 14 | Rollback and re-cutover, or restoration, of a gated D3 subject at the same triple | **Violation (B2 b)** |
| 15 | Discharge of an obligation gated on a restored subject | **Divergence (B2 c)** |
| 16 | Second holder challenges the standing decision; the author re-issues | Gate `T` with the challenge open (N2) |
| 17 | Stale evidence core; `REVALIDATE` by another holder | Refused; owner qualification not guaranteed (N3) |
| 18 | `QUALIFIED` entry while its decision is current | Entry closes on a literal reading (N4) |
| 19 | Mode change of a file hosting D2 and D4 spans | Attribution ambiguous; fail-closed for validity (N5) |
| 20 | Anchor-looking data line in YAML | Held: duplicate gives `ABSENT` plus integrity finding |
| 21 | Effect write set across concurrent `ignore` changes (d837363 B4) | Held; text unchanged |
| 22 | Support cycle via absorbed `about` or completeness edge; corrupt authenticated prefix | Held |
| 23 | Publication crash windows, fence chains, ABA | Held as previously reconstructed; text unchanged and not re-attacked in depth |

## 7. Minimum architecture and capability transfer

No primitive, component, persistent surface or record tier is added. The round removed one mechanism (observed-reads bounding) and one state (`qcap`). It added two rules:
- the standing-decision admission check;
- the `valid`-only tenure filter.

B2 entered through both added rules. The B1 cost entered through the removal. The recommended directions for B2 are subtractive. For B1, the options span added mechanism (a) to disclosure (c). §30 should count the two added rules (N7).

**Capability transfer.**
- The §26.4 tables are unchanged.
- Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS. PC-001 holds.
- PEM was activated, because this is mature-machinery replacement:
  - `PROJECT-ENGINEERING-MEMORY.md` is byte-identical on `main` and at the candidate (`15617971…`);
  - the validator reports "PEM schema 1 valid: 5 families, 0 notices";
  - `tests.test_protocol_63_engineering_memory` passes (28 tests).
- The five HAS entries (PC-001, SP-002, FF-001, DS-001, SP-001) remain applicable as in earlier records. DS-001 bears directly on section 8.
- Absence of a 7.x memory entry proves nothing.
- The workplan's "complete observed reads" bound is the one capability the round removed. B1 shows it carried an adverse-side property that no replacement preserves.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed.

Green fixtures could coexist with both blockers (DS-001):
- **B1**:
  - §31.2 "Closure bounding" tests only the passing side;
  - §31.3 "Completeness polarity" records both adverse runs while the judgment is current;
  - "Recording granularity" deliberately accepts that a widened run leaves (2);
  - no case runs a tracing runner unbounded, loses completeness before an adverse run is realized, or checks `adm` and the floor for a doc-only candidate.
- **B2**:
  - §31.6 tests a tenure restart only for D1/D2, where `run(s)` masks the defect;
  - no case integrates a new or promoted gated subject with a frame-decided gate, or restores or re-cuts-over a gated non-D1/D2 subject;
  - no case compares discharge against `valid`.

The diagnostic model was not run (optional); its file is unchanged since the Phase B candidate, and it models none of these clauses.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty.

§29.3's "execution change derives rerun obligations" is now true on the passing side. Two areas rest on the blockers:
- the E0 survival claims for disagreements and the D1/D2 floor (§29.4 findings, via §6) rest on B1;
- §29.7's Channel C realization and §29.4's revising-duty row ("a new record, acceptance and gate") rest on B2 for non-D1/D2 and new tenures.

§29.6's E3 list is adequate.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, and "Beyond the requested deliverable: **None**". I found no unmarked inspectability-driven product requirement. Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-0b6c4fa/`):**
- **Reading.**
  - The whole Manual, sections 0-33.
  - The word diff from a18b544 (Manual and closure map), and closure-map rows 1-5.
  - Workplan §6.6 executed content, `on`, `stale` and standing, the tenure and restoration text, and §21.
  - The stakeholder record (entries 1-18, SD-1 to SD-24).
  - Phase C handoff §5 and the continuation handoff §3-§5.
  - The a18b544 record in full; the Phase B record's N2 and §3 re-test table.
  - Governing owners as listed.
- **Blobs.** The Manual, closure-map and workplan blobs match the handoff.
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- **Whitespace.** `git diff --check a18b544… 0b6c4fa…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… 0b6c4fa…`: 35 files.
  - All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`.
  - The `qualification/ssds80/` files include `SESSION-CONTINUATION-HANDOFF-SSDS-8.0.md` (4 lines changed).
- **Frozen surfaces.** `git diff --quiet fad3ee4… 0b6c4fa… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **PEM.** Byte-identical to `main`; validator and 28 tests pass.

**Not verified:**
- any SSDS runtime behavior (none exists);
- real tracing-runner fidelity;
- G3 costs;
- the full prose of Review records before a18b544, beyond their findings tables;
- deep re-derivation of findings whose text is unchanged since a18b544, which I confirmed only by diff and re-reading;
- publication and fencing, which were not re-attacked;
- the diagnostic model, which was not run.

Family search stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.**
   - Blockers B1 and B2; non-blocking N1-N7.
   - All are D3 architecture or coordination findings.
   - I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings.
   - I launched no agents. None of the tools I ran (section 10) produced a finding beyond those stated.
2. **Realized results.** I produced, ran and reviewed no realized scientific results, and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM validator and the PEM tests are software checks on documents, not realized results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data.
   - **B1 repair options:** four, (a)-(d).
   - **B2 repair options:** four, (a)-(d).
   - **Selection criterion for the order and the leaning:** preserve the owner-required property with the least added mechanism (convergence owner). The choice is the stakeholder's; I make no single recommendation for either non-local recurrence.
   - **Clause readings, kept as findings rather than resolved:** two readings each of three clauses:
     - whether §7.6 binding extends to gate decisions (B2);
     - which unit is "innermost" for a multi-unit file (N5);
     - "its obligation stops being derived" (N4).

   No data, held-out set, earlier history or delegated search was involved.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment; no scientific or numerical formulation is accepted for the SSDS product. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, evidence, convergence);
   - the proposed workplan and Phase B record;
   - the stakeholder record and Phase C handoffs.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The following are shared dependencies:
- the corpus;
- the inherited workplan framing;
- the prior Review records (thirteen of the fourteen Manual Reviews same-family);
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT).

Both blockers entered through repairs that followed the a18b544 record, a same-family record:
- B1 through its subtractive option (a), whose stated cost covered only the passing side;
- B2 through its option (a) together with its N1 suggestion "Filter both terms by τ(s)".

This is the third consecutive round in which a same-family suggestion, adopted without a recorded stakeholder choice (N1), carried a defect forward. SD-22 already called for a different-family Review. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.

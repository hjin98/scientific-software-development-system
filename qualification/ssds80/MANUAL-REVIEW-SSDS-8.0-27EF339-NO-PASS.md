# SSDS 8 Architecture Manual — Independent D3 Review, candidate 27ef339

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 27ef3390317d48a81f49271207af963bec136224
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: 839d2d3a005974cc0df32aed378eb579fd221b22 (checked)
    CLOSURE MAP BLOB: 2cf0ba4b2b4ab4a4782e56fe168972a5567eaf3c (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756, read for §6.6, §6.9 declared frames, §12.2
           restoration locks, §16.2 and §21); blob at this candidate 91bde236465178f20c7348280e036d2884dfc216 (checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
           (both confirmed in PROTOCOL-RELEASE-STATE.yaml at the candidate, accepted_current 7.2.1)
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC,
           E9E6E9F, A18B544, 0B6C4FA
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           clauses changed since 0b6c4fa, including the repairs of that round's non-blocking findings;
           prior-finding regression; required structural checks; no implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section references are to the exact candidate. The checkout HEAD was the later handoff commit `5d2aa614`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`:

- `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract and scientific checks);
- `architecture-and-design.md`;
- `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
- the cited paragraphs of `evidence-evolution-and-dependencies.md`.

`abstraction-and-concretization.md` and the other concern owners were not loaded: no decision below turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** All three blockers are defects of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a gap between them, or between the Manual and a stakeholder direction, is not a challenge to accepted authority.

Owner text applied:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- D3 owner, "Architecture design test": prefer "one authoritative representation/state".
- D3 role entrypoint: "D3 contradictory/ambiguous/inadequate/unrealizable -> SERIOUS CHALLENGE to D3". Applied here to proposed D3, so it yields blockers, not a challenge to accepted authority.
- Evidence owner: "Do not suppress contradictory admissible observations to manufacture a pass or a positive project-learning pattern."
- Evidence owner: "When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence."
- Convergence owner, "Review strategy after recurrence": "Repeated related Review failures change the search strategy before another narrow repair/review loop. … A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign."

## Verdict

**NO-PASS.** Three D3 blockers survive, each stated at family level as method step 6a requires.

- **B1 — matching family (assessment disagreement, recorded execution basis); a non-local recurrence.** The 0b6c4fa B1 repair closes that record's trajectories (i) and (iii): an unbounded failure is never stopped, and it counts as admitted content. Its sibling (ii) is only disclosed, not closed. A differing or yielding run recorded **while no bounding completeness judgment was current** records the whole tree. It therefore never enters a bounded failure's (2) or (4), and stops resume once a judgment is current again. Live nondeterminism is hidden and support raised exactly as Phase C N2 forbids. The cause is the one the 0b6c4fa record named: one recorded width serves both polarities. Three statements call the change restrictive or claim Phase B N2 is preserved: §6.3, R1 and §31.2 (B). No stakeholder decision accepts the residual.
- **B2 — D1-D3 change-rule family (effect-keyed write set); a clean local defect that entered through the 0b6c4fa N5 repair.**
  - §14.5 and §1.2's parenthetical attribute a changed **byte** range to every unit with a term in the file.
  - §1.2's own "owned content by innermost ownership", its composite sentence, §1.4 rule 3, R5 and SD-14 attribute it only to the unit whose owned content changed.
  - Read literally, no agent item can change D4 code in any file that also holds a D1-D3 span. An implementer must choose between the two statements.
- **B3 — gate-decision family, fifth round; a clean local defect, pre-existing and now load-bearing.**
  - §7.5's closed list makes every `GATE_DECISION` an admitted-frame record.
  - §10.2, §11.5 step 3, §8.3 step 7 and the new §31.6 expectation ("a gate decided on a candidate frame is satisfied after integration") need gate decisions made in the candidate's frame.
  - Read literally, a pre-integration gate `ACCEPT` on changed content is refused as stale at step 6, so no gated change can integrate. For D1/D2, a gate decision admitted in the admitted frame is also never in the run that integration starts.

The 0b6c4fa-round repairs otherwise close what they target:
- trajectory (i) and sibling (iii) of 0b6c4fa B1;
- the tenure-filter divergences of 0b6c4fa B2 (b) and (c);
- the literal-reading defect of 0b6c4fa N4.

The other repaired non-blocking findings leave the residues listed below. This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — A run recorded without a current bound is invisible to every bounded failure's adverse conditions, so losing (or not yet having) completeness hides contradictory runs

**Earliest owner.** The following sections, which are workplan §21 items 4 and 5:
- Manual §6.3 "executed content" and "Recorded execution basis" (refinement R1);
- §6.5 `on⁻`;
- §6.6 conditions (2) and (4) and the "Bounded and unbounded bases" bullet.

It is a D3 defect and asks for no new D1/D2 rule.

**Owner and contract text.**
- Evidence owner (quoted above): do not suppress contradictory admissible observations to manufacture a pass; preserve material disagreement.
- Phase C handoff §5 (N2) makes two requirements:
  - "Losing completeness must not raise support by hiding either run";
  - "rewriting it to global fallback is a semantic regression, not clarification".
- Workplan §6.6 (reviewed): "Where no current completeness judgment bounds the closure and the runner's observed reads are not complete, the widening reaches the whole governed tree". Under that contract a runner with complete observed reads recorded a narrow basis even without a judgment.
- Manual §6.3: "Only a current completeness judgment bounds the closure …; observed reads add read entries and never bound it, so where no judgment bounds the closure the widening reaches the whole tree (a18b544 B1; refinement R1 drops the reviewed alternative bound "the runner's observed reads are complete", a restrictive change)."
- Manual §6.6, the new bullet: "The disclosed residual (§32.2): a differing or yielding run recorded unbounded, on a tree differing from the failing run's only outside a bounded failure's recorded content, is not in that failure's (2) or (4); it can matter only when the failure is later made stale through other runs bounded by a current judgment."
- Manual §17.4: a realization supports a claim only while its execution basis is satisfied "together with its bounding completeness judgments". So the loss of a bounding judgment itself derives `REALIZE` (§10.2), and the replacement runs are executed during the lapse, unbounded.

**Trajectory (primary; a lapse, then a restore).**

1. Dispatcher-controlled runner class (Python, image recorded, observes reads outside the tree).
   - Specification `S`: declarative oracle on `l2_error`, environment fixed, `EXECUTION_DEPENDS_ON kern`.
   - The solver has a data race, so it fails about half the time with no runner-supplied seed (unrecorded variation, §6.10).
   - The claim is D4, so no floor event intervenes.
   - Current reviewer judgments `c_S = COMPLETENESS({S}, EXEC)` and `c_k = COMPLETENESS({kern}, EXEC)`.
2. At `T1`, realization `a` is bounded by `c_S`, `c_k` and records unit entries for `S` and `kern`. It fails and is assessed `a⁻`, which counts.
3. A reviewer opens a blocking challenge against `c_k`, which is now `BLOCKED`. By §17.4 the obligation has no current realization, so `REALIZE` is derived. Meanwhile an unrelated admitted doc edit (`docs/notes.md`) gives `T2`.
4. The Dispatcher realizes `d` on `T2` during the lapse. Its closure reaches the fallback, so its record is `UNBOUNDED`: the whole tree. `d` passes.
   - In fact `d` ran on content identical to `a⁻`'s in every unit `S` reaches.
5. The challenge is dismissed and `c_k` is current again.
6. An `IMPLEMENT` item changes `kern` (a refactor that leaves the race), giving `T3`.
   - A reviewer or the analyzer re-attests `c_k3` on `kern@T3`.
   - The reruns produce:
     - a reproduction `r'` on `T1`, bounded by `c_k3`, which fails;
     - an evidence run `e` on `T3`, bounded by `c_k3`, which passes.
7. Evaluate in the admitted state at `T3`:
   - (1) holds via `r'`;
   - (2) holds, because the observations `on⁻ T1` are `a⁻`, the earlier reproduction and `r'`, all failing; `d`'s whole-tree entry differs at `docs/notes.md`, so `d` is excluded;
   - (3) holds via `e`;
   - (4) holds, because no observation `on⁻ T3` yields.

   So `a⁻` is stale, `ev` reaches `T` through `e`'s passing assessment, and the claim can be valid. The contradiction between `d` and `a⁻`/`r'` is suppressed by a difference nobody read. The current `c_k3`/`c_S` judgments show `d` read exactly the content `a⁻` read.

   Under the reviewed contract a tracing runner records `d` narrow, so (2) fails and the failure goes to the owner, which is what Phase C N2 requires.

**Siblings (same cause: a record's width is fixed by the completeness standing at record time and read by the adverse conditions).**
- **(ii-a) Judgment admitted later.** In a newly adopted repository the obligation's first passing realization `p` precedes any `COMPLETENESS(EXEC)` judgment, so it is recorded whole-tree. A later unrelated edit is followed by a judgment, then by a bounded flaky failure on the new tree, then by the steps of trajectory (6)-(7). `p` never counts in (2).
- **(ii-b) Analyzer upgrade.** An analyzer `RULESET_ADOPTION` makes every machinery completeness declaration non-current at once (§2.6, §5.2 `tgt`). Every bounded realization then becomes non-current and is rerun unbounded until the new analyzer re-declares. Every rerun in that gap is invisible to every bounded failure realized on a slightly different tree, whether as a differing run in (2) or a yielding run in (4).
- **(ii-c) Loss boundary or risk-overridden challenge.** The same as the primary trajectory, with `c_k` loss-withheld and then attested, or `P` and then dismissed.

**Surfacing.** §6.6 states the residual, and that statement is honest. Elsewhere the Manual contradicts or omits it:
- §6.3 still labels the change "a restrictive change". It is permissive for (2) and (4) whenever completeness was absent at record time.
- R1's property column claims the Phase B N2 property ("never removes an adverse recorded match"). That claim holds only for runs recorded while bounded.
- §31.2 (B) tests only "while the judgment is lost". A fixture written to it is green while this trajectory stands (DS-001).
- §32.2 says only "An unbounded basis matches adversely only an identical tree".
- The closure map's list of author choices for the stakeholder does not name this residual.
- No stakeholder decision accepts it. The 0b6c4fa record's disclosure option required explicit stakeholder acceptance.

**Family assessment.** This is the matching family's fourteenth round as the 0b6c4fa record counts. It is a **non-local recurrence**: no single recorded width serves both polarities while the record is also the currency basis (SD-11 "record once"). The 0b6c4fa round's option (b) moved the cost for unbounded *failures* but not for unbounded *witnesses*. Further sibling search (tracer fidelity, partial bounds per closure step) would be implementation-like.

**Options for the stakeholder (Phase C handoff §5), not a single repair.**
- **(a) Adds one existential, adverse-only, S0.**
  - In (2) and (4), let an observation count as "on the same content" also when another admitted observation of `conf(a⁻)` matches both trees: `∃ o' : on⁻(o', tree(a⁻)) ∧ on⁻(o', tree(o))` for (2), and `∃ o' : on⁻(o', G) ∧ on⁻(o', tree(o))` for (4).
  - `o' = real(a⁻)` covers the primary trajectory.
  - It reads only records and trees. It is compatible with SD-11, because every consumer still reads recorded bases. It keeps `on⁺ ⇒ on⁻`.
  - It only enlarges adverse matches, so it can only keep failures counting, and §5.6 monotonicity is unchanged.
- **(b) Subtractive, disclosure only.** The stakeholder explicitly accepts the residual. Then:
  - correct §6.3's label and R1's property claim;
  - state the residual and its three routes (lapse, record-before-judgment, analyzer upgrade) in §32.2;
  - replace §31.2 (B)'s expected value with the disclosed post-restoration behavior;
  - add a §32.3 trigger.
- **(c)** A different-family Review first (the stakeholder reserved this choice).

**Required discriminators.** These run at the real Dispatcher → Admission → Derivation (`stale`, `undisputed`) → discharge owners, with nothing seeded resolved:
- **(A)** The primary trajectory: after `c_k` is restored and `e` passes, `a⁻` is not stale and the owner's adjudication obligation is derived.
- **(B)** Sibling (ii-a).
- **(C)** Sibling (ii-b), with the gap reruns differing.

Under option (b), §31 must instead state and test the disclosed behavior, and the contradicting statements must be gone.

### B2 — The write set attributes changed bytes to every unit with a term in the file, contradicting innermost ownership, SD-14 and the composite rule; read literally, agents cannot edit D4 code that shares a file with D1-D3 spans

**Earliest owner.** The following sections, which are workplan §21 items 1, 23 and 25 (diff-to-unit mapping):
- Manual §1.2 "Write set [D3 decision; SD-14]";
- §14.5 "Language analyzers" (diff-to-unit mapping);
- as read by §13.2 (domain rule), §8.3 step 3 (`AUTH_WRITE_SCOPE`) and §14.3 `BOUNDARY.write_scope`.

**Text.**
- **§1.2** describes the set's members as follows:

  > every effective unit … for which any of these differs between the two: its owned content by innermost ownership (§1.4), in the §1.5 representation (the entry type, mode and bytes of every file a term of it resolves into, empty files and gitlinks included, attributed to every unit a term of which resolves into the file; innermost ownership applies only to byteless entries, empty files and gitlinks)

  It also says: "A composite whose revision changes only because a nested subject of another kind inside its scope changed is not in it by that change (the nested subject is)".
- **§14.5:** "diff-to-unit mapping (changed byte ranges, and a changed entry type or mode of a file, to every unit a term of which resolves into the file, innermost ownership applying only to byteless entries, §1.4, §1.5), one input to the effect-keyed write set".
- **§1.4 rule 3:** "A byte of governed content belongs to the innermost unit whose resolved region contains it." R5 says the same: "each byte belongs to the innermost declared region containing it".
- **SD-14** (stakeholder record item 11): "the write set is every unit whose owned content, declarations, regions, membership or signature actually differs between base and merged tree".
- **§13.2:** "an `IMPLEMENT`, `REPAIR`, `MIGRATE` or `DOCUMENT` write scope contains no `D1`, `D2` or `D3` unit, and its write set (§1.2) may contain none". An `AUTHOR` item's write scope "contains only units of that kind".

**Trajectory.**
1. Two top-level subjects share `src/solver/core.py`:
   - D2 `numerics.flux`, `{ file = "src/solver/core.py", symbol = "flux_limiter" }`;
   - D4 `impl.core`, `{ file = "src/solver/core.py", symbol = "write_output" }`.

   §1.4 rule 1 permits this, since neither qualified name is a prefix of the other.
2. An accepted `IMPLEMENT` item has `write_scope = ["impl.core"]` and changes bytes only inside `write_output`.
3. §14.5 maps the changed byte range to both units. So `numerics.flux` is in the write set:
   - `BOUNDARY.write_scope` gives a `VIOLATION`;
   - Admission rejects with `AUTH_WRITE_SCOPE`.
4. An `AUTHOR` item for D2 fails as well, because `impl.core` is in its write set. Only a human change can make the edit.

**Under the innermost reading.** `numerics.flux` owns none of the changed bytes and its `cid` is unchanged, so it is not in the set, as SD-14 and §1.2's opening clause say.

**Siblings.**
- §31.3 "Recording granularity": an `IMPLEMENT` item that changes only `helper` puts `kern.solve` and `kern` in its write set. Any write scope narrower than the composite fails.
- A D3 composite covering a Markdown file whole, with a nested D2 subject on one heading span:
  - a D2 edit puts the composite in the set, contradicting the composite sentence;
  - a D3 edit puts the D2 subject in the set.

  This extends d837363 N2's "no agent item route" from cross-kind *structural* changes to ordinary byte edits.

**Family and cause.** This is the D1-D3 change rule, write-set surface (SD-14). The 0b6c4fa N5 suggestion concerned only a file's entry type and mode. The repair carried "bytes" into the same clause. It is a **clean local defect**, not a recurrence of the revising-duty mechanism.

**Minimum repair (subtractive).**
- A changed byte belongs to the unit that owns it by §1.4 rule 3.
- A changed entry type or mode of a file belongs to every unit a term of which resolves into the file, because each such unit's `cid` hashes it.
- Delete "innermost ownership applies only to byteless entries" from §1.2 and §14.5, and make §14.5 match.

**Required discriminators** (at Admission step 3 and the conformance view):
- **(A)** The trajectory's item is `CLEAN` and admissible.
- **(B)** A mode change of `core.py` puts both units in the set and is a `VIOLATION` for an `IMPLEMENT` item.
- **(C)** The nested-subject cases follow §1.2's composite sentence.
- **(D)** A `kern.helper`-scoped item in the §31.3 trajectory is not refused.

### B3 — Gate decisions are admitted-frame records by §7.5, yet gates are derived, answered and required in candidate frames

**Earliest owner.** Manual §7.5 "Declared frame", with:
- §8.3 steps 6 and 7;
- §10.2 (`GATE(g)` "in a frame G", run membership);
- §11.5 step 3;
- §4.3 (`GATE_DECISION` basis);
- §31.6.

These are workplan §21 items 5 (declared frame per kind) and 7.

**Text.**
- **§7.5:** "A task result, a check execution, a realization on the candidate, and a review, conformance, assessment or acceptance judgment about a transformation declare frame `id(X)`. Every other record declares the admitted frame." This is the reviewed workplan's list, carried unchanged.
- **§4.3:** a `GATE_DECISION` has "`content` on the gated subject revision".
- **§8.3 step 6:** "every basis entry of every submitted support-tier record other than a report is satisfied, in its role, in that record's frame … Otherwise the record is classified stale and routed to revalidation, not admitted."
- **§11.5 step 3:** integration is requested once the discharge predicate would hold "on the candidate — clean conformance, current review judgments, required gates". §7.6 says the predicate "is evaluated in the post-admission state".
- **§10.2:** "A record, acceptance or gate decision is **in the run** iff it was admitted at or after `run(s)`, or it is a frame record of the transformation whose integrating admission is `run(s)` …"
- **§31.6 (new):** "a gate decided on a candidate frame is satisfied after integration."

**Trajectory.**
1. An `AUTHOR` item (or any item) carries a required human gate. Its candidate `X` changes subject `s` from `r_old` to `r`, or declares `s` new. `GATE(g)` is derived in `D_n[X]`.
2. Holder `H` records `GATE_DECISION ACCEPT`. By §7.5 it declares the admitted frame.
3. Step 6 evaluates its `content (s, r)` entry in the admitted state, where `cur(s) = r_old` or `s` does not exist. The decision is refused as stale (`STALE_BASIS`).
4. The integration request's step 7 needs "every human gate of o has a current standing authenticated ACCEPT" after admission, so it is refused.
5. The gate cannot be decided after integration, because integration needs it first. No gated change can integrate.

For a `NATIVE` D1/D2 subject there is a second route to the same result. Even an admitted-frame decision admitted before `k` is neither "admitted at or after `run(s)`" nor "a frame record", so it is outside the run.

The alternative reading, that a decision on a frame-derived gate declares that frame, is what §10.2, §11.5 and §31.6 presuppose. It contradicts §7.5's closed list, and an implementer must choose between them.

**Family and cause.** This is the gate-decision family's fifth round:
- 3540d98 B3;
- e9e6e9f B2;
- a18b544 B2;
- 0b6c4fa B2;
- now this.

The 0b6c4fa record's option (a) included "Add `GATE_DECISION` to §7.5". The round took option (b) and left §7.5 unchanged, while adding the §31.6 expectation that depends on it. The contradiction has existed since SD-19 put gate acceptance "in any frame". It is a **clean local defect**.

**Minimum repair.** Add to §7.5's frame-declaring kinds:
- a `GATE_DECISION` whose gate obligation is derived in frame `X`;
- a `PRODUCT_SCOPE_ACCEPTANCE` co-submitted with it.

The existing §7.3 and §7.5 rules then already make such a record "admitted but not current" in `D_n` until `X` integrates, and §10.2 places it in `X`'s prospective run. No new binding rule is needed.

**Required discriminators** (at Admission and Derivation):
- **(A)** A gated `AUTHOR` D2 revision and a new gated D3 subject each integrate after a frame gate decision, and the gate term is `T` after integration.
- **(B)** A frame gate decision of an abandoned candidate never becomes current in the admitted state, even when identical bytes arrive by absorption.
- **(C)** An admitted-frame gate decision recorded before integration on changed content is refused.

## 2. Non-blocking findings

- **N1 — Condition (1) now needs `bound`, which reads judgments about the frame's content, not the content the reproduction ran on.**
  - **Mechanism.** `bound(o)` requires "every `COMPLETENESS` judgment that bounded it is current … in the frame of evaluation".
  - **Effect after a fix.** Any fix inside a bounding judgment's scope (the usual case: the judgment has a `content` entry on the fixed unit) does two things:
    - every reproduction realized before the fix stops serving (1);
    - a fresh reproduction on `tree(a⁻)` is bounded by the post-fix judgment, which concerns other content (§4.6 reads currency at the head).
  - **Cost.** Every red-then-green iteration costs an extra reproduction.
  - **Under-statements.** §6.6 "Standing per frame", §31.3 "Red then green" and the 0b6c4fa round's §30 sentence ("so unbounded executions serve no stop") understate this. §31.3's contrast "(`on⁺` then needs another current bounding judgment)" does not apply to the same observation, whose bounding judgments are fixed.
  - **Narrowing option.** Let (1) also accept `tree(o) = tree(a⁻)` without `bound`. A run on the identical tree is a reproduction whatever its record's width, and (3) keeps `bound`, so 0b6c4fa B1 (i) stays closed. This option adds one disjunct back. Alternatively, state the cost.
- **N2 — SD-17 is partly reversed by an author choice; to put to the stakeholder.**
  - **What SD-17 rejected.** SD-17 withdrew SD-15's restriction "restoring red-then-green iterations". The stakeholder chose it after being told (item 13) its costs: "a failing candidate iteration against an admitted test permanently qualifies the admitted claim until the owner disposes of it, blocks the candidate's later green iteration, and for D1/D2 claims raises a floor item each time".
  - **What returns.** The bounded-only stop (0b6c4fa B1 option (b)) brings back exactly these costs for every closure no current judgment bounds.
  - **Why the cost is near-total.** Analyzer completeness is unavailable wherever an incompleteness marker exists (data read by path, runtime configuration; §2.6), which is typical of scientific code. Reviewer judgments lapse with every change in their scope, so each iteration needs re-attestation. §31.3's "an analyzer completeness declaration typically supplies it" is unsupported; §32.4 lists analyzer completeness for real scientific code as open.
  - **Surfacing.** The closure map lists the choice "to confirm or reverse" but does not say it partially reverses a stakeholder decision. It may be the right trade, but it is the stakeholder's to make.
- **N3 — Gate-tenure residue (entered through the 0b6c4fa B2 withdrawal).**
  - **Residue.** Four places conflict with §19.4's reuse of a gate decision on an unchanged triple across tenures for non-D1/D2 subjects:
    - §5.5 "a new run's or tenure's gate decides afresh";
    - §16.8's closing condition "(a new revision, revision run or tenure)";
    - R10's and S11's "across tenures nothing revives".

    For §16.8, a `QUALIFIED` decision reused across a tenure would close its inspector entry while still capping validity.
  - **Overclaim.** §19.4's "for a `NATIVE` D1/D2 subject the revision run excludes it" holds for `ACCEPTANCE` and `GATE_DECISION ACCEPT` (`tgt`, §5.2), not for a required-kind judgment of another kind.
  - **Surfacing.** Narrowing the reviewed workplan's lock "even an admitted restoration starts a tenure that excludes every earlier judgment" to acceptances follows the reviewed `valid` formula, but it is a choice between two reviewed statements. List it in §0.3.
- **N4 — `REVALIDATE` holder for a gate decision (0b6c4fa N3 repair).**
  - "Its author, or the owner where its author is unavailable" names no recorded predicate. S3 holder assignment must be a function of the ledger.
  - Fix: let the obligation be held by its author **or** the owner, whichever answers first.
- **N5 — The second holder's routes (0b6c4fa N2 repair).**
  - **Brief availability.** A `REJECT` needs a rendered core. When an `UNQUALIFIED` decision answered the obligation, no open inspector entry or gate brief exists for another holder.
  - **Evasion persists.** A challenge against the standing decision record is still permitted, and the author can still supersede around it.
  - **SD-24 narrowed.** A second holder can now only veto (`F`), never qualify (`P`). This narrows SD-24's "until a later unqualified gate decision". It is surfaced as an author choice; confirm it with the stakeholder.
- **N6 — Whole-tree entry (0b6c4fa N6, partly closed).**
  - `{ prefix = "" }` denotes the fallback, resolved with **no** `ignore` (§1.8, §6.3). A root-directory chain step (§4.5 "each ancestor directory") would record the same term under the frozen `ignore`.
  - Only the `UNBOUNDED` marker disambiguates them, and R1 and the §6.3 guard say every recorded term re-resolves under the record's own `ignore`.
  - Fix: give the fallback its own term kind, or state the disambiguation.
- **N7 — Accounting.**
  - §30's "The §6 family is unchanged in mechanism" omits the `UNBOUNDED` conjunct of `bound`, the `adm` disjunct and the new §6.9 clause.
  - The closure map's author-choice list omits B1's residual and N1's cost.
  - The map's row 5 "declared frame per kind … CARRIED" rests on B3.

  The aid confers no authority.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly; the closure map was used only as an index. "Answered" means a substantive D3 answer exists; it is neither runtime evidence nor stakeholder acceptance.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | **Write-set attribution contradicts itself (B2)**; N6 is a representation residue |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 6.8, 17.1 | Answered; gate qualification as N5 |
| 4 | §§4.1-4.6, 6.3 | **Not substantively closed (B1)**. Also unstated: which judgments bound a realization on a non-head tree (N1) |
| 5 | §§5-7, 17, 22.3 | `on⁻`/`stale` carry **B1**; the declared frame per kind carries **B3**; strata, single-valuedness and monotonicity hold (the new `bound` and `adm` terms read S0 or completeness positively) |
| 6 | §§8, 21-23 | Answered, except step 6 for gate decisions (B3) |
| 7 | §10 | **Gate discharge at integration is unreachable on the literal reading (B3)**; N4 |
| 8 | §11, §13.2, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered; N3 (§16.8), N5 |
| 11 | §§17, 6.10 | Answered |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered; N3 for §19.4 wording |
| 14-16 | §§21-25 | Answered; runtime unexecuted |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered |
| 21 | §29.7 | Answered; the Channel C row rests on B3 |
| 22 | §30 | Present; N7 |
| 23 | §12, §1.2, §13.2 | **Domain-rule input contradictory (B2)** |
| 24 | §13 | Answered |
| 25 | §14 | **Diff-to-unit mapping is B2**; the rest is answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; see section 9 |

**Workplan §16.2, both tables.** The diff since 0b6c4fa does not touch §26.4. I re-read it against the workplan's **Deferred** rows. Every one has a final disposition in §26.3-§26.4, and none is merely routed:
- invariants 4, 9, 15, 17 and 26;
- the §5 sub-rules;
- §6, §7 and §12;
- §18.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table remain correctly `[delegated]`. Three architectural decisions are left implicit or contradictory:
- the adverse width of runs recorded without a bound (B1);
- byte attribution in the write set (B2);
- the declared frame of a gate decision (B3).

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | The construction rule, the guard, `on⁺ ⇒ on⁻`, set-valued `ext` and the bounded-only permissive use are sound per record. The 0b6c4fa trajectories (i) and (iii) are closed. **The record-time adverse width is a change needing different treatment (B1)**, mislabeled "restrictive" in §6.3. N1 and N2 are its costs |
| R2 | Sound; unchanged. The new terms add no S2 edge of negative polarity |
| R3 | Sound; unchanged |
| R4 | Sound within its crash model; unchanged |
| R5 | Sound as a partition rule; **the write set now contradicts it (B2)** |
| R6, R7 | Sound; unchanged |
| R8 | Sound. A gate supersession targets the obligation. Challenge-route evasion remains (N5) |
| R9 | Sound. The second holder's `REJECT` uses the veto correctly (N5 covers availability) |
| R10 | Sound for D1/D2 runs. Its "across tenures nothing revives" overstates once gate decisions are reused (N3) |
| R11 | Sound as one standing decision with a `P` cap. It depends on B3 for frame-decided gates, and it narrows SD-24 for second holders (N5) |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence.

**Depth.** I re-derived the 0b6c4fa items in full. For the earlier records I read each record's findings list (titles and dispositions), treated the 0b6c4fa record's re-verification tables as hypotheses, and checked the cited text against the 0b6c4fa→27ef339 diff and my whole-Manual read.

That diff touches only these places:
- §0.3;
- §1.2 and §1.8;
- §5.5;
- §6.5, §6.6, §6.8 and §6.9;
- §10.2;
- §14.5;
- §16.8;
- §19.4;
- §30;
- §31.2, §31.3 and §31.6;
- §32.2 and §32.3;
- closure-map row 7 and the author-choice list;
- stakeholder record item 19.

I did not re-read earlier records' full prose (section 13).

### 0B6C4FA (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Partly closed.** (i): `o3` cannot serve (3), and the owner's adjudication obligation and the D1/D2 floor follow, so closed. (iii): `adm` holds for an unbounded basis and the class stays R3, so closed. (ii): open beyond the lapse window, now **B1** here. (iv): disclosed only within §6.6 |
| B2 | (b) and (c) **closed** by withdrawing the filter: one condition for `valid`, triggers, the answered state, discharge and step 7. (a) **partly closed**: it holds only if gate decisions are frame records, which §7.5 contradicts (**B3**) |
| N1 | **Partly closed.** The author choices are listed for the stakeholder, but no stakeholder decision is recorded and the list omits B1's residual (N2, N7) |
| N2 | **Partly closed** (N5) |
| N3 | **Partly closed** (N4) |
| N4 | Closed for the literal-reading defect; "or tenure" residue (N3) |
| N5 | **Repair introduced B2** |
| N6 | **Partly closed** (N6) |
| N7 | Partly closed (§30 and §31.6 updated); residue N7 |

### A18B544, E9E6E9F, E2154AC (same family)

| Review | ID | Disposition |
|---|---|---|
| A18B544 | B1 | Closed on the passing side; adverse side B1 here |
| A18B544 | B2 | Closed |
| A18B544 | N1 | Superseded by the withdrawal; residue N3 |
| A18B544 | N2 | Closed |
| A18B544 | N3 | The repair chain ends in B2 |
| A18B544 | N4, N5 | Closed |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, B2 | Closed |
| E9E6E9F | N1-N3, N5 | Closed |
| E9E6E9F | N4 | Superseded |
| E2154AC | B1 | Closed |
| E2154AC | N1, N3-N5 | Closed |
| E2154AC | N2 | Closed; the inspector residue is N3 |

### 3540D98 (different family)

| ID | Disposition |
|---|---|
| B1 | Closed: exact identity |
| B2 | Closed: full external-input set |
| B3 | Closed for its trajectory; the family continues as B3 |
| B4 | Closed: equal regions |
| N1 | Closed for acceptances (§10.2 prospective run); gate decisions B3 |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683

| Review | ID | Disposition |
|---|---|---|
| 798B2B4 | B1-B3 | Closed for acceptances (run as `tgt`); for gate decisions they rest on B3 |
| 798B2B4 | B4 | Closed |
| 798B2B4 | N1-N8 | Closed; N1's R10/S11 scope has the N3 residue |
| 71CF9B3 | B1, B2 | Closed |
| 71CF9B3 | N1-N8 | Closed |
| 86AB683 | B1 | Closed |
| 86AB683 | N1-N7 | Closed |

### 1FFBBF0, 53669A5, D837363

| Review | ID | Disposition |
|---|---|---|
| 1FFBBF0 | B1 | Closed |
| 1FFBBF0 | B2 | Closed for acceptances; gate refusal "in every frame" rests on B3 |
| 1FFBBF0 | N2 | Composite in the write set when only parts change; **reopened by B2** |
| 1FFBBF0 | N1, N3-N7 | Closed |
| 53669A5 | B1, B3 | Closed |
| 53669A5 | B2 | Closed for acceptances (B3 for gates) |
| 53669A5 | N1 | SD-15 withdrew reviewed stops; **reopened in a new form by the bounded-only stop** (N2) |
| 53669A5 | N2-N9 | Closed |
| D837363 | B1-B3 | Closed |
| D837363 | B4 | Closed as effect-keyed, but B2's byte attribution contradicts SD-14 |
| D837363 | N1 | Nested subjects of another domain; contradicted under B2 |
| D837363 | N2 | No agent route for cross-kind structure; **extended by B2 to byte edits** |
| D837363 | N3-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | ID | Disposition |
|---|---|---|
| CC005DB | B1-B3 | Closed |
| CC005DB | N1-N8 | Closed |
| C6DA678 | B1-B3 | Closed |
| C6DA678 | N1-N8, N10-N12 | Closed |
| C6DA678 | N9 | Empty prefix; **partly closed** (N6) |
| B595F2C | B1 | Closed for bounded bases; the adverse width of unbounded witnesses is B1 here |
| B595F2C | B2-B4 | Closed |
| B595F2C | N1-N8 | Closed |
| 6FF4ED1 | B1 | Closed: `on⁺ ⇒ on⁻` with frozen context |
| 6FF4ED1 | B2-B4 | Closed |
| 6FF4ED1 | N1-N12 | Closed; N3's gate-qualification line continues in B3, N3 and N5 |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| EF8445A/552AC01 N2: strata, completeness polarity | **Re-tested.** Runs recorded while `c` is current stay in (2) and (4) when `c` becomes `P`, blocked, revoked or loss-withheld: **held**. Runs recorded during a lapse or before any judgment: **B1** |
| Fail-closed support cycles; corrupt prefixes | Held. `bound`'s `UNBOUNDED` conjunct and `adm`'s disjunct are S0, completeness is read positively, and `INTEGRITY_HALT` is unchanged |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held; the class is conservative for unbounded bases |
| Contrary-run retention, nondeterminism | Held for bounded witnesses; **B1** for unbounded witnesses |
| U1/U2/W1/W2 executed content | Held for currency |
| Absorbed relaxation; adversity versus currency, challenge, loss; salvage; independence; start latch; effective structure, quarantine, tenure | Held. Gate tenure is now consistent; frame gates are B3 |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3) |
| Phase B N4 | Held as reopen triggers |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | 0b6c4fa B1 (i): racing solver, no judgment, unrelated doc edit, one flaky pass | Held: not stale; owner; D1/D2 floor |
| 2 | Doc-only candidate surfaces a flaky D1/D2 admitted-content failure (unbounded) | Held: `adm`, floor, R3 |
| 3 | Bounded failure; `c` lost before the alternate-tree run; `c` stays lost | Held: no stop |
| 4 | As 3, then `c` restored (dismissal, attestation) and a fix | **Violation (B1)** |
| 5 | First passing realization predates any judgment; later bounded flaky failure | **Violation (B1 ii-a)** |
| 6 | Analyzer `RULESET_ADOPTION` gap reruns | **Violation (B1 ii-b)** |
| 7 | Root-directory completeness judgment giving a "bounded" whole-governed-tree record | The reviewed `on` granularity accepts this: a change within a widened scope is new content. Noted, not a finding |
| 8 | Fix inside a bounding scope; earlier reproduction | Restrictive cost; extra reproduction (N1) |
| 9 | Candidate regression of a D1/D2 admitted test, unbounded | Floor item each time; claim `P` until owner (N2; the costs SD-17 rejected) |
| 10 | Bounded failure, `c` `P` / blocked / revoked / loss-withheld, runs recorded while `c` current | Held |
| 11 | Structure, `ignore`, analyzer or system-version change with the tree fixed | Held (`on⁻` unchanged) |
| 12 | `IMPLEMENT` edit of a D4 span sharing a file with a D2 span | **Contradiction (B2)** |
| 13 | Same-kind part edit (`kern.helper`) with a narrow write scope | **Contradiction (B2)** |
| 14 | Mode change of a mixed-kind file | Both units in the set; fail-closed (B2's repair keeps this) |
| 15 | Gated `AUTHOR` D2 revision; gate decided before integration | **Unintegrable on the §7.5 reading (B3)** |
| 16 | New gated D3 subject; frame gate | **B3** |
| 17 | Non-D1/D2 restoration or re-cutover at an unchanged triple with a standing gate | Held: reused, consistent across consumers; wording residue N3 |
| 18 | D1/D2 revert after a `QUALIFIED` gate | Held: new run; any holder |
| 19 | Second holder's `REJECT` against a standing `UNQUALIFIED` accept | Vetoes (`F`), owner adjudication; brief availability N5 |
| 20 | Author supersedes a gate decision under an open blocking challenge | Gate returns to `T` while the challenge stays open (N5) |
| 21 | `REVALIDATE` of a stale gate decision | Holder predicate undefined (N4) |
| 22 | Support cycle via absorbed `about` or a completeness edge; corrupt authenticated prefix | Held |
| 23 | Publication crash windows, fence chains, ABA | Text unchanged since 0b6c4fa; not re-attacked in depth |

## 7. Minimum architecture and capability transfer

No primitive, component, persistent surface or record tier is added. The round:
- removed the same-root-tree route and the gate tenure filter;
- added an `UNBOUNDED` conjunct to `bound`, a disjunct to `adm` and a scheduling clause;
- changed the write-set wording.

B2 entered through the wording change. B1's residual remains from the a18b544 removal of observed-reads bounding. B3 is pre-existing. The recommended repairs for B2 and B3 are local. For B1 the options range from one adverse-only existential to disclosure. §30 should count the round's added terms (N7).

**Capability transfer.**
- The §26.4 tables are unchanged and resolve every Deferred §16.2 row (section 3).
- Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS. PC-001 holds.
- PEM was activated, because this is mature-machinery replacement:
  - `PROJECT-ENGINEERING-MEMORY.md` is byte-identical on `main` and at the candidate (`15617971…`);
  - the validator, run from the checkout with `source/` unchanged from the candidate, reports "PEM schema 1 valid: 5 families, 0 notices";
  - `tests.test_protocol_63_engineering_memory` passes (28 tests).
- The HAS entries remain applicable as in earlier records: PC-001, SP-002, FF-001, DS-001 and SP-001. DS-001 bears directly on section 8. Absence of a 7.x memory entry proves nothing.
- The workplan's "complete observed reads" bound carried an adverse-side capability that no replacement preserves (B1).

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed.

Green fixtures could coexist with each blocker (DS-001):
- **B1:**
  - §31.2 (B)'s expected value is bounded to "while the judgment is lost";
  - §31.3 "Completeness polarity" records both adverse runs while `c` is current;
  - no case realizes a witness during a lapse or before a judgment and then restores the bound.
- **B2:**
  - §31.2 (C) and §31.5 test only mode changes and D1-D3 edits;
  - no case edits a D4 span sharing a file with a D1-D3 span, or a narrowly scoped part.
- **B3:**
  - §31.6 asserts "a gate decided on a candidate frame is satisfied after integration" without a case for the step-6 currency of the decision or for §7.5.

§31.3 "Red then green" also states a premise ("an analyzer completeness declaration typically supplies it") that is an open empirical question (§32.4). It omits N1's extra reproduction.

The diagnostic model was not run (optional). Its file is unchanged since the Phase B candidate, and it models none of these clauses.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty.

Three claims rest on the blockers:
- §29.2's routing row (E0 through the §13.2 domain rule) is over-enforced under B2's literal reading. It blocks legitimate D4 work in mixed-kind files rather than permitting silent mutation.
- §29.4's revising-duty row and §29.7's Channel C row rest on B3, since frame gates must be admissible.
- §29.4's disagreement survival claims (via §6) rest on B1.

§29.6's E3 list is adequate.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, and "Beyond the requested deliverable: **None**". I found no unmarked inspectability-driven product requirement. Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate** (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-27ef339/`):
- **Reading.**
  - The whole Manual, sections 0-33.
  - The diff from 0b6c4fa (Manual, closure map, stakeholder record), and closure-map rows 5-12 and the author-choice list.
  - Workplan §6.6 (executed content, `on`, `stale`, standing), the `valid` formula, the restoration locks, the §16.2 Deferred rows and §21.
  - The stakeholder record, entries 10-19 and SD-15 to SD-24.
  - Phase C handoff §5.
  - The 0b6c4fa record in full, and the findings lists of every earlier Manual Review.
  - Governing owners as listed.
- **Blobs.** The Manual, closure-map and workplan blobs match the handoff.
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- **Whitespace.** `git diff --check 0b6c4fa… 27ef339…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… 27ef339…`: 37 files. All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`.
- **Frozen surfaces.** `git diff --quiet fad3ee4… 27ef339… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **PEM.** As in section 7.

**Not verified:**
- any SSDS runtime behavior (none exists);
- tracer fidelity and G3 costs;
- the full prose of Review records before 0b6c4fa, beyond their findings lists;
- deep re-derivation of findings whose cited text is unchanged since 0b6c4fa;
- publication and fencing, which were not re-attacked;
- the diagnostic model, which was not run.

Family search stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence.

1. **Material findings.**
   - Blockers B1-B3 and non-blocking N1-N7, all D3 architecture or coordination findings.
   - I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings.
   - I launched no agents. The tools I ran (section 10) produced no finding beyond those stated.
2. **Realized results.** I produced, ran and reviewed no realized scientific results and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM validator and the PEM tests are software checks on documents, not realized results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data, and no data, held-out set, earlier history or delegated search was involved.
   - **Repair options:** three for B1, (a)-(c); one minimum direction each for B2 and B3.
   - **Clause readings, kept as findings rather than resolved:** two readings each of three clauses:
     - byte attribution (B2);
     - a gate decision's declared frame (B3);
     - which judgments bound a realization on a non-head tree (N1).
   - **Selection criterion:** preserve the owner-required property with the least added mechanism (convergence owner). The B1 choice is the stakeholder's.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment; no scientific or numerical formulation is accepted for the SSDS product. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, evidence, convergence);
   - the proposed workplan;
   - the stakeholder record and Phase C handoff.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The following are shared dependencies:
- the corpus;
- the inherited workplan framing;
- the prior Review records (fourteen of the fifteen Manual Reviews same-family);
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT).

Two of the three blockers trace to the previous same-family record:
- B2 entered through the repair of its N5 suggestion;
- B3 is the §7.5 clause its option (a) named and the round did not adopt.

B1 is the sibling that record's chosen option did not cover. Repair directions from candidate 13 onward were chosen by the author under the stakeholder's delegation (item 19), not by the stakeholder. N2 and B1 are the two I would put to the stakeholder before any further same-family round. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.

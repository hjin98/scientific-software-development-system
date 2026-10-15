# SSDS 8 Architecture Manual — Independent D3 Review, candidate a18b544

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: a18b544870cd597c89c5f4dd8e6649a7cbf17518
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: 7d221252f4510673c101f91294775ddfbdbfd56a (checked)
    CLOSURE MAP BLOB: d196bdacfeff15d0692f8941a9f730ca829f2e2a (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (word diff inspected: Review/lifecycle coordination text only)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC, E9E6E9F
    REVIEW METHOD: D3 role entered at the governing public source; whole-Manual read at the exact
           candidate (git archive snapshot); deductive counterexamples in both polarities; family-level
           search after recurrence (convergence owner; handoff method step 6a), attacking hardest the
           clauses changed since e9e6e9f, including the repairs of that round's non-blocking findings;
           prior-finding regression; required structural checks; optional diagnostic model; no
           implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section references are to the exact candidate. The checkout HEAD was the later handoff commit `7b206e93`, which differs from the candidate only by the handoff file. Governing owners were read at `aaeaf8b…`: `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md`; `source/shared/fragments/scientific-checks.md`; `architecture-and-design.md`; `abstraction-and-concretization.md`; `convergence-and-cycle-economy.md`; and the cited sections of `evidence-evolution-and-dependencies.md` and `workflow-and-workplans.md`. No other owner was loaded, because no decision below turned on one.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** Both blockers are defects of the proposed D3 concretization. The workplan and the Manual are proposed architecture, so a gap between them, or between the Manual and a stakeholder direction, is not a challenge to accepted authority.

Baseline owner text applied, unchanged:

- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- Kernel, "Verification and Challenge": "A child can perfectly satisfy a too-weak abstraction and still be wrong".
- Evidence owner, "Applicability, immutable observation, and superseding assessment": "A stale passing observation is not admissible confirmation." and "PASS/accepted/closed cannot depend on stale, rejected, unavailable-required or otherwise inadmissible evidence."
- Evidence owner, "Change impact and closure": "Restoring an old file does not restore old evidence validity by timestamp."
- Workflow owner, "Human gates and closeout learning": "The gate does not close unqualified when missing realized records could plausibly change its judgment." Under authority lifecycle: "Orchestration may represent pending/accepted/rejected state but cannot self-approve it."
- Convergence owner, "Active simplification trigger": simplification is mandatory before another additive durable repair when evidence shows "repeated patches around the same mechanism, patch-on-patch repair, wrappers/adapters/retries/fallbacks/special cases accumulating around one owner".

## Verdict

**NO-PASS.** Two D3 blockers survive. Each is stated at family level, as method step 6a requires, and each entered through this round's repairs.

- **B1 (executed-content family, fourth round; the §6 matching clause's twelfth finding, permissive side).** The repair of e9e6e9f N4 lets "complete observed reads" bound a realization's closure. It defines them as "a runner class declaring that it observes every read, §17.5". The only read-observation declaration in §17.5 covers reads **outside** the tree. So a hermetic runner that records no reads **inside** the tree bounds the closure, and the recorded execution basis omits tree content the execution read. Every consumer of that one record then treats changed content as unchanged:
  - realization currency: stale passing evidence discharges;
  - `on⁺`: a failure is made stale by an observation that never ran on the content in question.

  Siblings: directory enumeration and failed lookups are not "reads"; ignored tracked files lie outside the whole-tree widened entry. This is also an unsurfaced narrowing of workplan §6.6 ("the runner's observed reads are complete").
- **B2 (gate-qualification family, third round).** The repair of e9e6e9f B2 made the `QUALIFIED` cap (`qcap`) an S0 fact lifted only by supersession. Two problems follow.
  - **Permissive.** The lifting supersession is read as raw syntax. It need not stand, so an upheld or blocking challenge against the lifting decision, or loss-withholding of it, leaves the cap lifted. The subject then returns to `T` on an earlier, pre-limitation acceptance.
  - **Restrictive.** The cap reads the subject triple across runs and tenures. Its lift needs a supersession "on the same target", and that target is run-scoped and includes the exact rendered evidence core. After a D1/D2 revert or a tenure restart at the same revision, and on a literal reading even within a run, no admissible record can lift the cap. The §16.8 entry can then never close.

Everything else this round targeted closes the trajectory it names:
- the e9e6e9f B1 carve-outs: no non-exact runner fallback; submodule reads recorded as gitlink read entries; LFS objects read as pinned external reads; the comment classifier owned by the system version; byteless write-set entries, with a wording residue (N3);
- the e9e6e9f B2 currency-based lifting routes, the §10.4 restatement and §5.6 monotonicity;
- the `ABSENT` acceptance bar (e9e6e9f N1);
- the classifier precision (N2, with a new residue, N2 here);
- the set-valued `ext` (N3).

The D1-D3 change rule and the adverse side of the matching clause have no new finding. This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — "Complete observed reads" are keyed on the out-of-tree flag, so the one recorded basis can omit what the execution read

**Earliest owner.** Manual §6.3 "executed content" and "Recorded execution basis" (refinement R1), with §17.5's runner declaration and §4.6. These are workplan §21 item 4 ("the mechanical computation of each realization's executed content (execution basis, observed runner reads, whole-tree fallback)") and item 11 ("trusted-runner designation and custody"). It is a D3 defect and asks no new D1/D2 rule.

**Owner and contract text.**
- Evidence owner (quoted above): a stale passing observation is not admissible confirmation; restoring an old file does not restore old evidence validity.
- Workplan §6.6, the reviewed contract: executed content is "everything the realization's execution read". "Where no current completeness judgment bounds the closure and the runner's observed reads are not complete, the widening reaches the whole governed tree: missing dependency knowledge never proves that two executions read the same content." Workplan §32's reopen list names the fallback condition as "no completeness judgments, incomplete read recording".
- Manual §6.3 now says: "for an execution basis, and only there, complete observed reads (a runner class declaring that it observes every read, §17.5) bound the closure as a current completeness judgment would".
- Manual §17.5 declares only "whether the runner observes **every read outside the realization's tree** (files and network)". No other read-observation declaration exists anywhere in the Manual. §6.3 records "the declared attribute set and read-observation flag", one flag.
- Manual §2.6: "A marker never overrides … complete observed reads". So "data read by path" does not defeat the bound.
- Manual §17.4: "Stale passing evidence never discharges." R1: "one representation serves every consumer".

**Trajectory A — stale passing evidence discharges. Primary; blocker-grade on its own.**

1. Policy designates a Dispatcher-controlled class `hermetic` with no network, hermetic home and cache, and its image recorded as an environment component. This follows §17.5's own guidance. It truthfully declares that it observes every read outside the tree, since the only reads possible there are image files, which §20.1 excludes from external reads. It records no reads inside the tree; nothing in §17.5 or §4.2 requires that it do so.
2. Specification `S` (claim in a D2 unit) declares `EXECUTION_DEPENDS_ON kern`. The solver opens tracked `data/mesh.dat`, which belongs to unit `data` and lies outside the EXEC closure. No `COMPLETENESS(EXEC)` judgment exists.
3. Under §6.3 the class's flag bounds the closure. No widening happens, so the basis holds unit entries for `S` and `kern`, no read entries and no widened entry. `bound(o)` is vacuously `T`.
4. Realization `q` passes, is assessed, and discharges `S`'s obligation.
5. An admitted change edits `data/mesh.dat`. Every recorded entry re-resolves unchanged, so `sat(execution) = T` (§4.1) and `q` stays current. No `REALIZE` is derived (§10.2: "without a current admissible realization"). `ev` and `valid` rest on a passing observation of content the next execution would not read.

Before this candidate, §4.6 widened on the completeness judgment alone. The e9e6e9f record (N4) read that as the operative rule, under which the whole-tree widened entry changes and `q` goes non-current. This round resolved the ambiguity in the permissive direction, through the wrong flag.

**Trajectory B — a live failure is made stale without any run on the failing content (matching, permissive side). Same root cause.**

Same class and specification. The rows are trees with their content; each run is recorded with entries for `S` and the code units only.

| Tree | Code | `data/mesh.dat` | Event |
|---|---|---|---|
| `T1` | `c1` | `v1` | `a⁻` fails because of the `v1` data; a reproduction fails identically |
| `T2` | `c2` | `v2` | `o3` passes |
| `T3` | `c2` | `v1` | an admitted change restores only the data; no run happens on `T3` |

In `T3`:
- (3) holds through `o3`: its recorded entries match `T3`, `ext` matches, and `bound(o3)` is vacuous.
- (4) holds: `real(a⁻)` and its reproduction record `c1`, so they are not `on⁻ T3`, and `o3` does not yield.
- (1) and (2) hold on `T1`.

So `a⁻` is stale in `T3` although nothing ran on code `c2` with data `v1`. `o3` also stays current there as passing evidence. The adverse conditions (2) and (4) do not help, because the unrecorded difference lies on the side `on⁻` cannot see. This is a way "the content it read can change without matching noticing" (handoff step 5).

**Siblings (same cause: the recorded basis is allowed to be narrower than what was read).**
- **(i) Enumeration and absence.** Even a runner that traces every in-tree file read records "every file of the realization's tree the designated runner observed being read" (§6.3). A directory listing (`glob`) or a failed lookup (`exists`, import-path misses) reads no file. A later added file changes the execution while no recorded entry changes, whenever the directory lies in no recorded unit and the closure is bounded by observed reads.
- **(ii) Ignored tracked files.** Under the whole-tree fallback, the widened entry covers "the governed files under the frozen `ignore` patterns" (§6.3). With no in-tree read recording, a read of a tracked but ignored file is covered by nothing, whatever the bounding rule. This sibling is pre-existing (cc005db N1 classified such reads as read entries, which presumes observation).
- **(iii) Git object-database reads.** Content an execution obtains through Git plumbing (`git show`, an LFS fetch, version derivation from `.git`) is read from files absent from the tree. It is therefore an external, normally unpinnable read, which currency ignores. Under any bounded closure the tracked source of that content is not recorded.

**Surfacing.** Equating "the runner's observed reads are complete" (workplan) with the out-of-tree flag (SD-18) narrows the reviewed contract. It is neither listed in §0.3 nor named in the history paragraph's e9e6e9f sentence.

**Family assessment (convergence owner, "Review strategy after recurrence").** This is the fourth successive round in which realization currency, or matching, reads a recorded basis that does not denote what the execution read: 3540d98 B1, e2154ac B1, e9e6e9f B1, and now this. It entered, as the handoff warned, through the repair of a non-blocking finding (e9e6e9f N4). It is a **non-local recurrence**. Each round has accepted some declaration as proof that the recording is complete:
- runner byte-exactness, then a fallback class;
- the gitlink and the LFS transform;
- now the out-of-tree flag.

Each such proof has had a hole. Further sibling search (filesystem notification races, `mmap` without `open`, reads by child processes outside the trace) would be implementation-like.

**Minimum repair direction (subtractive).** Remove the observed-reads bounding clause. Only a current `COMPLETENESS` judgment bounds a closure (§4.6 governs every closure), and observed reads only add read entries. Make the whole-tree fallback entry cover every tracked path, governed or ignored, so that the fail-closed default denotes the whole tree the execution could read.
- Cost: more whole-tree fallbacks. That is already the §32.3 reopen trigger, and projects reduce it with `COMPLETENESS(EXEC)` judgments, which are challengeable.
- Effect: siblings (i)-(iii) close with the primary trajectory whenever no judgment bounds the closure. With a judgment, they are judgment errors, routed E3.

Options for the stakeholder (Phase C handoff §5), since this is a non-local recurrence:
- **(a)** the subtractive repair above;
- **(b)** keep observed-read bounding but add a separate runner-class guarantee, recorded by value, that it observes every in-tree read including directory enumerations and failed lookups, recorded as membership and absent-path entries. This adds mechanism and a hard-to-qualify runner contract;
- **(c)** restrict observed-read bounding to Dispatcher-controlled tracing runners qualified at G3 on real trajectories;
- **(d)** a different-family Review before repair.

**Required discriminators.** At the real Content Model → Dispatcher/runner → realization currency → discharge and matching owners:
- **(A)** Trajectory A under a class declaring out-of-tree observation with no in-tree tracing: after the data change, `q` is non-current and `REALIZE` is derived.
- **(B)** Trajectory B: `a⁻` is not stale in `T3`.
- **(C)** A tracing runner and a specification that globs `data/*.csv`: adding `data/new.csv` makes the passing realization non-current. The same holds for a probed absent file that is later added.
- **(D)** A non-tracing runner reading an ignored tracked file under the whole-tree fallback: changing that file makes the realization non-current.

None of §31.2-§31.3 discriminates A-D. §31.3 "Unobserved external inputs" tests only the out-of-tree side of the flag.

### B2 — The qualified-gate cap is keyed and lifted on identities other than the decision it qualifies

**Earliest owner.** Manual §5.5 (`qcap` and its paragraph), with:
- §8.3 step 3 (supersession authority);
- §3.4 (the `GATE_DECISION` target);
- §10.2 (run-parameterized `GATE` obligations);
- §10.4;
- §16.8 "Qualified gates";
- §0.3 R11.

These are workplan §21 items 3 (gate outcome vocabulary), 7 (three-valued discharge, provisional propagation) and 10 (gate templates meeting Channel C).

**Owner and contract text.**
- SD-24, verbatim: a `QUALIFIED` `GATE_DECISION ACCEPT` "supports validity and discharge only as `P` … until an unqualified gate decision on the same revision". Stakeholder entry 18: "until a later unqualified gate decision".
- Workflow owner (quoted above): no unqualified closure while missing realized records could plausibly change the judgment; orchestration cannot self-approve.
- Manual §5.5: "The cap is a fact about admitted records, like an adverse judgment's existence … It lifts only when the qualified acceptance is superseded by its own author's `UNQUALIFIED` `ACCEPT` … or by the owner's adjudication … in either case an authenticated human judgment (A8)".
- Manual §5.5 `stands⁻`, which disposes of an adverse judgment only when "the chain's last record must stand" (`¬superseded(d) ∧ status1(d) = CLEAR ∧ cont(d)`). Manual §6.1 standing clause: "a stop earned by supersession stands on immutable facts and its own record's standing".
- Manual §0.4 P5: across a loss boundary "retained permissive effects do not pass without requalification or accountable attestation".
- Manual §8.3 step 3: supersession "only by a record of the same kind on the same target".
- Manual §3.4: a `GATE_DECISION` targets "a gate obligation and the exact evidence core shown". §16.6 section 1: the core includes the "qualified head".
- Manual §10.2: "`ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` carry `run(s)` among their parameters".
- R10: a D1/D2 revert "derives a new revising review, acceptance and gate".

**Trajectory (a) — permissive: the lifting decision need not stand.** This reads "same target" as the gate obligation, the only reading under which any lift is possible (see (b)).

1. D2 subject `s` at revision `r` in its run, with a counting revision-assessment record and a required gate `g`.
2. Holder `H1` records `h_u`: `ACCEPT`, `ADEQUATE`, `UNQUALIFIED`. `valid(s) = T`.
3. A later realization shows a material limitation. Holder `H2` records `h_q`: `ACCEPT`, `ADEQUATE`, `QUALIFIED`, through `decide`. This is the §31.6 "cap persistence" set-up. Now `qcap(g) = P`, `valid(s) = P`, and the §16.8 entry is open.
4. `H2` records `h_u2`: `ACCEPT`, `ADEQUATE`, `UNQUALIFIED`, naming `h_q` in `supersedes` and claiming the limitation resolved. `qcap(g) = T`.
5. Any one of the following:
   - **(a1)** A qualified actor's blocking challenge against `h_u2` is upheld, because the adjudicator finds the limitation unresolved. `h_u2` is `REVOKED`.
   - **(a2)** The same challenge is merely open and blocking.
   - **(a3)** A `LEDGER_LOSS` follows `h_u2`, and a `CONTINUITY_ATTESTATION` (form `EXPLICIT`) holds `h_u` but not `h_u2`.
6. `qcap(g)` stays `T`, because `superseded(h_q)` is an S0 fact indifferent to `h_u2`'s standing. `h_u` is current, so the gate term, `valid(s)` and every descendant are `T`. The §16.8 entry stays closed, `GATE(g)` is not derived (a current `ACCEPT` exists), and nothing reopens.

Effects:
- The limitation is adjudicated live in (a1), and disputed in (a2). Yet the subject closes unqualified on an acceptance made before the limitation was known. That is contrary to SD-24 and to the Channel C rule.
- In (a3) the permissive effect of a withheld record passes the boundary unattested, contrary to P5. The Manual's own `stands⁻` would have refused all three.

**Trajectory (b) — restrictive: the lift is unreachable, so the cap and its human-attention entry can be permanent.**

- **(b1) Literal reading.** By §3.4 the target is the obligation *and* the exact core shown, and the core names the qualified head. Any later decision is rendered at a later head, so no record is ever "on the same target" as `h_q`. §8.3 step 3 then rejects every superseder (`AUTH_SUPERSEDES`). `qcap` can never lift, the §16.8 entry can never close, and no authenticated human judgment can discharge that attention.
- **(b2) Across runs and tenures, on any reading.**
  1. `h_q` caps `s` at `r0` in run `R1`.
  2. An admitted change starts `R2`, then a restore of `r0`'s bytes starts `R3`. This is the §31.5 revert case. A re-cutover after version rollback, or a kind round trip, gives the same triple in a new tenure.
  3. `qcap` ranges over "some admitted … `ACCEPT` for `g` on `(s, scope_id(s), cur(s))`", with no run or tenure condition, so `h_q` caps `R3`.
  4. `h_q`'s target is `R1`'s `GATE` obligation, which is no longer derived. Whether §8.3 step 2 ("every … obligation and target exists") admits a decision on it is undecided, and nothing derives, renders or prompts such a decision. A decision on `R3`'s obligation is not on `h_q`'s target.

  So the fresh, fully assessed `R3` gate cannot return `s` to `T` at `r0`. Where policy forbids provisional continuation, dependent obligations stay `OPEN` indefinitely. This contradicts SD-24 ("until an unqualified gate decision on the same revision") and R10 ("derives a new … gate").

**Family assessment.** This is the third successive round in the gate-qualification family:
- 3540d98 B3, closed by SD-24;
- e9e6e9f B2: the cap followed currency;
- now: the cap follows raw existence across all runs, while its lift follows run- and core-scoped supersession without standing.

Each repair moved the key of a **second qualification state**, kept beside the gate decision's own support, without unifying the two. The keys involved are:
- the subject triple (cap);
- the gate obligation (decision target, veto `same`, readiness);
- the run (`tgt`);
- standing (`stands⁻`).

That divergence is the shared cause. Since it recurs and accumulates special cases around one owner, this is a **non-local recurrence**, and the convergence owner's simplification trigger applies.

**Minimum repair direction (subtractive).** Delete `qcap` as a separate state:
- Define the target of a `GATE_DECISION` supersession as its gate obligation, not the rendered core.
- Admit a later passing `GATE_DECISION` on an answered `GATE` obligation only as its standing decision's author's reassessment, or the owner's adjudication, superseding it.
- Let the gate term read the one standing decision: `current(h)` capped at `P` when `h.qualification = QUALIFIED`.

Consequences:
- A qualification then follows its decision's run and tenure.
- Challenge, staleness or loss of the standing decision lowers the gate term, because no earlier unqualified decision remains to fall back on.
- A new run's gate decides afresh, with the earlier qualifying records rendered in its core as findings.
- `stands⁻`-style chain standing is needed only for adverse judgments, as now.

Options for the stakeholder:
- **(a)** the subtractive repair above;
- **(b)** a local repair keeping `qcap`: the lift requires the superseding chain's last record to stand (as `stands⁻`), the cap is scoped to the gate obligation (run and tenure) of the decision it qualifies, and "same target" for gate supersession is defined as the obligation;
- **(c)** the SD-24 alternative the stakeholder was offered in entry 18, "Refuse qualified accept", which removes the cap;
- **(d)** a different-family Review before repair.

**Required discriminators.** At Admission, Derivation (`valid`, discharge) and the inspector view:
- (a1), (a2) and (a3) each leave `valid(s) ≤ P`, discharge not `DISCHARGED`, and the §16.8 entry open.
- After a revert of a D1/D2 revision whose earlier-run gate was `QUALIFIED`, an `UNQUALIFIED` gate decision in the new run by any qualified holder lifts the cap, or the Manual states and displays the stakeholder-accepted alternative.
- Within a run, `H2`'s later `UNQUALIFIED` `ACCEPT` rendered at a later head is admissible as a superseder.
- An implementation that lifts on raw supersession, or keeps an unliftable cap, must fail.

The present §31.6 cases ("Qualified gates", "Cap persistence") discriminate none of these.

## 2. Non-blocking findings

- **N1 — Gate decisions and required-kind judgments are not tenure-filtered (pre-existing in the reviewed workplan; bears on B2).**
  - `valid` filters only `ACC` by `τ(s)`. The `⋁ j' passing, by q` term and the gate term read any current judgment on the same triple.
  - For a non-D1/D2 subject with a policy-required gate whose tenure ends and restarts at an unchanged triple (demotion then restoration, a mode round trip, a kind round trip), the earlier tenure's human gate `ACCEPT` satisfies the gate term again. `GATE(g)` is not derived.
  - §19.4's lock "an admitted restoration starts a tenure excluding every earlier judgment", and S11, therefore overstate what the formula does.
  - A new acceptance is still required, so this is not blocking. Filter both terms by `τ(s)`, or narrow the §19.4 statement and say whether a restored subject's human gate is re-asked.
- **N2 — Anchor recognition in file types without a classifier (entered through the e9e6e9f N2 repair).** §1.5 now says "anchor-term resolution (§1.3) uses the same classifier". §1.2 still gives comment leaders for TOML, YAML, shell and TeX, and §1.5 says those types "keep anchor lines in their identity", which implies anchors work there. Read literally, anchor terms in unclassified types never resolve, so §1.9 refuses them and the new `AUTH_ILL_FORMED` bar refuses acceptance. That is restrictive only. State that in a type without a classifier an anchor line is recognized syntactically and kept in identity.
- **N3 — Byteless write-set entries, wording residue (e9e6e9f B1 E).**
  - §1.2 includes "every file it owns bytes of or that a whole-file term of it names, empty files and gitlinks included".
  - §1.4 rule 1 uses "whole-file term" as distinct from `path` and `prefix`, so an empty file covered by a `prefix` or `path` term is included only by the parenthetical.
  - §14.5's diff-to-unit mapping ("owning bytes of it or naming it by a whole-file term") lacks the parenthetical.
  - Innermost ownership of a zero-byte entry under nested prefixes is undefined.

  The intent is clear and §31.2 tests it. Say "every file a term of it resolves into, attributed to the innermost unit whose term resolves to it", in both places.
- **N4 — Representation consequences not disclosed.**
  - Under §1.5 an LFS-tracked input is pointer text in the execution's tree. Evidence that needs LFS data must fetch the object as an observed, pinned external read, and a class that cannot observe such reads makes it unpinnable.
  - Submodule commits are not kept reachable by the ledger: §21.2 reachability covers this repository's commits. A reproduction on `tree(a⁻)` (§6.9) can therefore become impossible if the submodule's host drops the commit. §21.4's "always available to derivation" is true for derivation only.

  Disclose both in §32.2, and add a §32.3 trigger.
- **N5 — Passing evidence with an unpinnable read stays current (faithful to workplan §6.6; disclosure).** Currency reads only tree-resident entries. A passing realization that read an unpinnable network input, or ran under a class that does not observe outside reads, stays current while its tree-resident entries hold. §32.2 discloses only the failing side.
- **N6 — Accounting.**
  - Closure-map items 4 and 11 say DECIDED.
  - §29.3's E0 row "execution change derives rerun obligations" overstates until B1 is repaired, and §29.7's Channel C row until B2 is repaired.
  - The §0.3 history sentence for e9e6e9f omits the §6.3 bounding change and the `AUTH_ILL_FORMED` bar.

  The aid confers no authority.

## 3. Closure audit

Each workplan §21 item and clause was located in the Manual directly, using the closure map only as an index. "Answered" means a substantive D3 answer exists; it is not runtime evidence or stakeholder acceptance.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | Answered. N2 and N3 are wording residues |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 6.8, 17.1; gate `adequacy`/`qualification` (§3.4, §5.5) | Vocabulary answered; the qualification semantics carries **B2** |
| 4 | §§4.1-4.6, 6.3 | **Not substantively closed (B1)**: the observed-reads bound and the whole-tree fallback do not denote what was read |
| 5 | §§5-7, 17, 22.3 | Answered. Strata and monotonicity hold with `qcap` as an S0 constant |
| 6 | §§8, 21-23 | Answered (R4 replaces the write-ahead record; sound, as before) |
| 7 | §10 | **Not substantively closed (B2)**: the cap's lift is unrealizable or non-standing |
| 8 | §11, §13.2, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered, except that the §16.8 qualified-gate entry and Channel C realization carry **B2** |
| 11 | §§17, 6.10 | **Not substantively closed (B1)**: §17.5's single flag is used as an in-tree completeness guarantee |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered; N1 for §19.4's lock wording |
| 14 | §§21-25 | Answered; runtime unexecuted |
| 15, 16 | §25.1-§25.3 | Answered |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered; §27.3 now agrees with §1.5 on the classifier owner |
| 20 | §20 | Answered; N4 on submodule reachability |
| 21 | §29.7 | Answered; the Channel C row depends on B2 |
| 22 | §30 | Present; it does not count the §6.3 bounding route or `qcap` as added mechanism (N6) |
| 23 | §12, §1.2/§13.2 | Answered |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; the E0 claims named in N6 depend on B1 and B2 |

**Workplan §16.2, both tables.** §26.4 is unchanged since e2154ac (diff). I re-read it against both workplan §16.2 tables: all 26 product-invariant rows, and every frozen-surface row including §4 layout and namespace and §14 CLI. Every **Deferred** row has a final disposition (invariants 4, 9, 15, 17 and 26; §5 sub-rules; §6; §7 mappings; §12 configuration; §18 fitness). None is merely routed.

**Material decisions versus delegated D4.** Parsers, the diff implementation, checkpoint encoding, limit values and the file-type table extension are correctly `[delegated]`. Two architectural decisions are left implicit:
- whether in-tree read observation is a runner-class guarantee at all (B1);
- what "the same target" is for gate supersession (B2).

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | The construction rule is sound as a matching construction: `on⁺ ⇒ on⁻` holds by construction, the guard holds, and the set-valued `ext` is sound in both directions. **As now realized, the recorded basis it governs can omit in-tree content the execution read (B1).** "One representation serves every consumer" then propagates the omission to currency and to `on⁺` alike. Unsound until B1 is repaired |
| R2 | Sound. With `qcap` an S0 constant, `valid` is again monotone in every S2 input, so "forcing only lowers values" is true |
| R3 | Sound; unchanged |
| R4 | Sound within its crash model; residuals disclosed; unchanged |
| R5 | Sound. The `AUTH_ILL_FORMED` bar closes e9e6e9f N1 (an `ABSENT` composite cannot be accepted, so its blind revision supports nothing) |
| R6 | Sound for classified types. In unclassified types anchor refinement changes `rev`, as stated; anchor recognition there is N2 |
| R7 | Sound; unchanged |
| R8 | Sound as a supersession-authority rule. Its "same target" clause, applied to `GATE_DECISION`'s core-bearing, run-parameterized target, is what makes R11's lift unreachable (B2 b) |
| R9 | Sound; unchanged |
| R10 | Sound for acceptances and gate decisions. B2 (b2) shows the qualified-gate cap does not follow R10's run scoping |
| R11 | **A change realized unsoundly (B2).** The row narrows SD-24's "an unqualified gate decision on the same revision" to the qualified decision's own author or the owner. That narrowing is surfaced. But the lift it names is unreachable on a literal reading and across runs, and where reachable it ignores the superseder's standing. The stakeholder should see the narrowing's consequence after a revert, which contradicts SD-24's text |

## 5. Previous findings and Phase B closures

"Closed" means I re-derived that the present text excludes the named trajectory; it is not runtime evidence. Prior records were read as hypotheses.

The diff from e9e6e9f touches only:
- §0.3; §1.2; §1.5; §5.5; §6.3;
- §8.3 step 3; §10.4; §14.5;
- §16.8; §17.5; §30; §31.2; §31.6.

For findings whose cited text lies elsewhere, I re-read the cited present text in the whole-Manual read and give the basis. Rows are terse where the mechanism is unchanged and was confirmed present.

### E9E6E9F (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Partly closed.**<br>(A) Closed: a non-guaranteeing runner "cannot be designated" (§1.5, §17.5).<br>(B) Closed for observing runners: a submodule read is a gitlink read entry.<br>(C) Closed: LFS objects are external reads, so `filter=lfs` no longer selects what is presented.<br>(D) Closed: the classifier belongs to the system version, consistent with §27.3.<br>(E) Closed in intent, wording residue N3.<br>The family reopens as **B1** here, through the N4 repair. |
| B2 | **Partly closed.** The four currency-based lifting routes (a)-(d) are closed, because `qcap` reads existence. §10.4 now references `qcap` (b, closed). §5.6 monotonicity holds (c, closed). The family reopens as **B2** here. |
| N1 | Closed: `AUTH_ILL_FORMED` refuses acceptance of a revision with an `ABSENT` declared term (§8.3 step 3). |
| N2 | Closed for (i)-(iii). The (iii) wording introduced N2 here. |
| N3 | Closed: `ext` compares sets. A locator read under two pins still yields two pairs. |
| N4 | **Repaired unsoundly**: the bounding choice is B1. |
| N5 | Closed (§30, closure map). New accounting residue N6. |

### E2154AC (same family)

| ID | Disposition and basis |
|---|---|
| B1 | Closed for its own trajectories (byte-exact runners, data lines that look like anchors, mode changes, CRLF recognition, single pass). Family: B1 here. |
| N1 | Closed: single pass, no cascade (§1.4 rule 3). |
| N2 | (a) Closed: existence-based, order-independent. (b) **Partly closed**: the §16.8 entry prompts the lift, but per B2 (b) the entry may never close. (c) Closed. |
| N3 | Closed: R11 row; R5 row; §30; map item 7. |
| N4 | Closed: costs and guidance (§17.5, §32.2-§32.3); set comparison. |
| N5 | Closed as disclosure (§32.2, §32.3). |

### 3540D98 (different family)

| ID | Disposition and basis |
|---|---|
| B1 | Closed for binary, line-ending, mode and link identity (§1.5). Family open as B1 here. |
| B2 | Closed: `ext` compares the complete set of `(locator, pin)` pairs (§6.5); (2) and (4) use `on⁻` without pins. |
| B3 | **Partly closed**: `ADEQUATE` required; a `QUALIFIED` single acceptance gives `P`. Family open as B2 here. |
| B4 | Closed: equal regions resolve to `ABSENT` in one pass (§1.4). |
| N1 | Closed (§10.2 prospective run). |
| N2 | Closed as disclosure (§32.2). |
| N3 | Closed (aid). |
| N4 | Held (§32.2-§32.4). |

### 798B2B4, 71CF9B3, 86AB683

| Review | ID | Disposition and basis |
|---|---|---|
| 798B2B4 | B1-B3 | Closed: never-integrated frames are in no run; the run is `tgt`, read by `base`, `valid`, `ACC`, triggers and discharge; the predecessor is display only (§5.2, §10.2) |
| 798B2B4 | B4 | Closed: traversed links are recorded (§6.3); the gitlink analogue is now closed too |
| 798B2B4 | N1-N8 | Closed: `NATIVE` kind D1/D2 scope; `record` entry on the assessment record; envelope predecessor map; cutover `REVIEW`; disclosures; no `holds`; §31.5 coverage; aid |
| 71CF9B3 | B1-B2 | Closed: the run starts wherever `cur(s)` took its value; S11/R10 restored |
| 71CF9B3 | N1-N8 | Closed: display-only predecessor; counting record answers `REVIEW(s, r)`; §12.2/§13.5/§16.6/§30; cutover binding; randomness disclosure; links; §1.9/§2.6/§32.2 disclosures; aid |
| 86AB683 | B1 | Closed: counts only in the run, with `status1 ∉ {REVOKED, BLOCKED}` and `cont`, carried by the acceptance's `record` entry |
| 86AB683 | N1-N7 | Closed: cutover binding; randomness disclosure; flag and set recorded by value; disclosures; quarantine paths; one slot entry per subject; aid |

### 1FFBBF0, 53669A5, D837363

| Review | ID | Disposition and basis |
|---|---|---|
| 1FFBBF0 | B1 | Closed for its out-of-tree trajectory: a free seed is recorded; a non-observing class is unpinnable. **The SD-18 flag has since acquired a second, unsound meaning (B1 here).** |
| 1FFBBF0 | B2 | Closed: §8.3 step 7 refuses unassessed D1/D2 acceptances and gate `ACCEPT`s in every frame, human ones included |
| 1FFBBF0 | N1 | Closed (§1.9) |
| 1FFBBF0 | N2 | Closed in intent; N3 here |
| 1FFBBF0 | N3-N7 | Closed: predecessor display; quarantine paths; declared-set change disclosure (§17.5); environment-component exclusion (§20.1); aid |
| 53669A5 | B1-B3 | Closed: `ext` compares every recorded attribute; direct human acceptance refused before a counting record; the intake rule concerns targets |
| 53669A5 | N1-N9 | Closed: SD-17 red-then-green (§31.3); `NATIVE` scope; manifest in `AUTHOR` scope; cross-domain structural route; resolver purity; moved-out content disclosed; declaration-key conflicts; named statements; aid |
| D837363 | B1-B4 | Closed: free environment only in `on⁺`; pure resolvers and frozen context; target-keyed record; `T_n` versus `M_n(X)` write set |
| D837363 | N1-N8 | Closed: nested-kind revision; cross-kind route; `QUARANTINE` effect; re-identification disclosure (§27.3); manifest always in the write set; finding status and predecessor slot; aid |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | ID | Disposition and basis |
|---|---|---|
| CC005DB | B1-B3 | Closed: effect write set; system version in the resolution context; product-scope record kind |
| CC005DB | N1 | Closed as classification. Its dependence on read observation is B1 sibling (ii) |
| CC005DB | N2-N8 | Closed: incidental-read disclosure; no permissive frozen-analyzer fallback; term-level resolution; contrary-order mechanics; re-review policy; re-identification disclosure; aid |
| C6DA678 | B1-B3 | Closed: pins and unpinnable reads never narrow `on⁻`, (2), (4) or `adm`; `same` across item revisions; effect write set |
| C6DA678 | N1-N6 | Closed |
| C6DA678 | N7 | Closed: gitlink-selected reads are now gitlink read entries |
| C6DA678 | N8-N12 | Closed |
| B595F2C | B1-B4 | Closed: unit and term granularity; `ref` locality; `DOCUMENT` domain rule; R9 answered-once, symmetric veto, one `TASK_RESULT` |
| B595F2C | N1-N8 | Closed |
| 6FF4ED1 | B1-B4 | Closed: `on⁺ ⇒ on⁻` with frozen context; any prose change is R2; analyzer pinning; `AUTHOR`/`DOCUMENT` routes |
| 6FF4ED1 | N1, N2 | Closed |
| 6FF4ED1 | N3 | **Partly closed**: `qualification` propagates, via B2's defective cap |
| 6FF4ED1 | N4-N12 | Closed |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| Y1 identical-outcome coverage; Y2 candidate-own not re-escalated | Held (§6.5 coverage; §6.8 class) |
| EF8445A/552AC01 N2: strata, completeness polarity, class basis | **Re-tested.** I used an alternate tree differing from `tree(a⁻)` only outside a recorded narrow basis, with a differing old-content run and a yielding present-content run, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld. Both runs stay in (2) and (4), because `on⁻` reads no completeness and no S2 value. Held. A basis bounded by observed reads has no judgment to lose, and its defect lies on the permissive side (B1 B) |
| Absorbed assessor-read relaxation; identical-outcome floor; X1-X3 | Held (§6.5-§6.8) |
| Promotion, refinement, enactment | Held (§7.6, §19.3-§19.4) |
| Adversity versus currency, challenge, loss | Held for assessments and adverse judgments (§5.4, §6.7). **B2 (a) is the one place where a lifting supersession ignores standing** |
| Salvage, retirement, unauthorized supersession; scope anchors, home, independence; start latch | Held (§8.3 steps 3 and 6, §10.2, §6.4, §6.8) |
| U1/U2/W1/W2 executed content and reading | Held where the recorded basis denotes what was read; **B1** where the observed-reads bound applies |
| Contrary-run retention, nondeterminism | Held (§6.6 (2)/(4); §6.10) |
| Fail-closed support cycles | Held (§5.6 clamp; no new edges, since `qcap` is an S0 constant) |
| Corrupt prefixes | Held (§5.7 `INTEGRITY_HALT`) |
| Effective structure, quarantine, tenure | Held (§1.6, §8.3 step 4, §19.4); N1 on gate-term tenure filtering |
| Phase B N1 (adoption provenance) | Disclosed (§32.2, §32.4) |
| Phase B N2 (positive-only completeness) | Held, as re-tested above |
| Phase B N3 (diagnostic bounds) | Held (§31.3) |
| Phase B N4 (costs) | Held as reopen triggers (§32.3) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | Out-of-tree-observing hermetic class, no in-tree tracing, no completeness; tracked data read by path changes | **Violation (B1 A)**: passing evidence stays current |
| 2 | Same class; failure on `T1`, pass on `T2`, data restored in `T3` | **Violation (B1 B)**: stale in `T3` with no run there |
| 3 | Tracing runner; glob picks up an added file; probed absent file added | **Escape (B1 i)** where the closure is bounded by observed reads |
| 4 | Non-tracing runner, whole-tree fallback, ignored tracked input changes | **Escape (B1 ii)**; pre-existing |
| 5 | Content obtained through Git plumbing under a bounded closure | **Escape (B1 iii)** |
| 6 | `.gitattributes` `eol` change with a byte-exact designated runner | Held |
| 7 | Same with a runner that honors attributes | Held: not designatable; results are findings |
| 8 | Submodule bump with an observing runner; LFS `filter=lfs` removed | Held: gitlink read entry changes; pointer bytes always presented |
| 9 | Analyzer-set adoption changing Python tokenization | Held: the classifier is in the system version |
| 10 | Anchor line in a TOML or shell file | **Ambiguous (N2)**; restrictive only |
| 11 | `IMPLEMENT` mode change of an empty file under a D2 `prefix`; gitlink under a D2 prefix | Held by the §1.2 parenthetical; wording residue N3 |
| 12 | Acceptance of an `ABSENT` composite (e9e6e9f N1) | Held: `AUTH_ILL_FORMED` |
| 13 | `h_u`, `h_q`, then the author's lifting `h_u2`, which is revoked, blocked or loss-withheld while `h_u` is held | **Violation (B2 a)**: `valid = T` |
| 14 | `h_q` then `h_u2` rendered at a later head, read literally | **Unreachable lift (B2 b1)** |
| 15 | D1/D2 revert, or tenure restart at the same triple, after a `QUALIFIED` gate | **Permanent cap (B2 b2)** |
| 16 | `h_u` then `h_q`: challenge, staleness or loss of `h_q` | Held: the cap stays (§31.6) |
| 17 | `QUALIFIED` gate decision on a forced support cycle | Held: `qcap` is S0; clamping only lowers |
| 18 | Restoration of a non-D1/D2 gated subject at an unchanged triple | Old gate decision revives (N1) |
| 19 | Phase B N2 completeness polarity (`P`, blocked, revoked, loss-withheld) | Held |
| 20 | Support cycle through absorbed `about` or completeness edge; corrupt authenticated prefix | Held (§5.6, §5.7) |
| 21 | D1/D2 revert, mode churn, a merged revision, a frame never integrated: run and record conditions | Held: each value change starts a run; nothing revives |
| 22 | Set-valued `ext`: duplicate reads of one pin; one locator under two pins | Held both ways |
| 23 | Publication: crash windows, fence chains, ABA (unchanged sections) | Held as previously reconstructed; no text change |

## 7. Minimum architecture and capability transfer

No primitive, component, persistent surface or record tier is added this round. The round did add two mechanisms:
- an observed-reads bounding route in §6.3;
- a second qualification state (`qcap`) with its own lift rule beside the gate decision's support.

Each is where a blocker entered. Both recommended repairs are subtractive:
- B1 removes the bounding route;
- B2 removes `qcap` in favor of the standing decision's own qualification.

Subject to that, the §30 table remains the minimum justified set within this Review's evidence. §30's account should count the two mechanisms (N6).

**Capability transfer.**
- The §26.4 tables are unchanged and were re-read against workplan §16.2 and §18 rows.
- Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS (§26.2-§26.3). PC-001 holds.
- PEM was activated, because this is mature-machinery replacement. Accepted/base memory `PROJECT-ENGINEERING-MEMORY.md` is byte-identical on `main` and at the candidate (`15617971…`), and `tests.test_protocol_63_engineering_memory` passes (28 tests).
- The five workplan §0.3 HAS entries (PC-001, SP-002, FF-001, DS-001, SP-001) are the five PEM entries. Their dispositions are realized as in the e9e6e9f record.
- DS-001 bears directly on §8 below.
- The PEM coverage note (no 7.x memory write) means absence of an entry proves nothing.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed. The §31.2 "Representation" additions and the §31.6 "Cap persistence" case name negative discriminators for the e9e6e9f trajectories.

Green fixtures could coexist with this round's defects (DS-001):
- **B1**: no case runs a class that declares out-of-tree observation without in-tree tracing, enumeration, absent-file probes or ignored tracked inputs. §31.3 "Unobserved external inputs" tests only the outside side of the flag.
- **B2**: §31.6 challenges and stales only the *qualified* record. No case challenges, blocks or loss-withholds the *lifting* record, reverts a D1/D2 revision whose earlier-run gate was `QUALIFIED`, or lifts with a decision rendered at a later head.
- **N1**: no case restores a gated non-D1/D2 subject at an unchanged triple.

The diagnostic model ran in its default mode: `REV23`, 0 failures over 1,574,464 transitions, and the model file is unchanged since the Phase B candidate. It models none of these clauses, as §31.3 states.

## 9. Doctrine-realization map and O1

§29 is unchanged this round. I re-checked §29.2-§29.5 against:
- the 7.2.1 D3 entrypoint and its expanded entry contract;
- the role-contract rows;
- every scientific-checks duty: delegate questions, gaps, findings, realized results, variants, tensions, choices, retention, claims, before loss, resources, persistence, persisting tensions, inaccessible homes, product changes, revising duty, authority content.

Two E0 claims are false as realized until the blockers are repaired:
- §29.3 "D2, D4 … remap/rerun when machinery changes — E0 … execution change derives rerun obligations" fails under B1;
- §29.7's Channel C realization ("refusal of an unqualified accept with known missing evidence", with §16.6 and §5.5) relies on a cap that B2 shows can be lifted by a non-standing record, or never lifted.

§29.6's disclosed E3 list is adequate.

O1 (§0.5):
- It states the realized record, readers, routine questions and the realized-record architecture.
- It visibly marks the within-deliverable surfaces, including `sdp ssds export` and the tool-independent canonical-JSON ledger, with "Beyond the requested deliverable: **None**".
- I found no inspectability-driven product requirement left unmarked. N4's disclosures concern evidence operation, not a product surface.

Technical Review accepts no marked item; a marked item beyond the deliverable binds only after stakeholder or task acceptance.

## 10. What I verified and how; what I could not verify

**Verified at the exact candidate (`git archive` snapshot under `$TMPDIR/ssds80-manual-review-a18b544/`):**
- **Reading.**
  - The whole Manual.
  - The word diff from e9e6e9f (Manual and closure map), and closure-map rows 1, 3, 4, 7, 10 and 11.
  - Workplan §6.6 executed content and `on`, §7.4 `valid`, §16.2 (both tables), §19.4 lock text, §21 and the §0.3 HAS.
  - Stakeholder record entries 15-18 and SD-22 to SD-24.
  - The e9e6e9f record in full; the e2154ac and 3540d98 findings sections and tables; the earlier records through their findings tables, as hypotheses.
  - The governing owners named above.
- **Blobs.** The Manual, closure-map and workplan blobs match the handoff. The workplan differs from the Phase B blob only in coordination text (word diff).
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- **Whitespace.** `git diff --check e9e6e9f… a18b544…`: clean (exit 0).
- **Additions.** `git diff --stat fad3ee4… a18b544…`: 33 files.
  - All are under `qualification/ssds80/`, plus the Manual and two lines in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`.
  - The `qualification/ssds80/` files include `SESSION-CONTINUATION-HANDOFF-SSDS-8.0.md` (4 lines) and the stakeholder record (34 lines).
- **Frozen surfaces.** `git diff --quiet fad3ee4… a18b544… -- orchestrator/docs/architecture.md source dist`: exit 0.
- **Optional extras.**
  - `tests.test_protocol_63_engineering_memory`: 28 tests, OK.
  - PEM identical to `main`.
  - Diagnostic model: 0 failures; model unchanged since `e23f142`.

**Not verified:**
- any SSDS implementation or runtime behavior (none exists);
- the behavior of real tracing or sandbox runners: B1's premises rest on the Manual's text and on standard POSIX semantics, namely that directory listings and failed lookups are not file reads;
- Git LFS behavior (not installed);
- G3 costs;
- external or native issue homes;
- the full prose of Review records before e9e6e9f, beyond their findings tables;
- every filesystem or execution layer: the family search stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence. It produced, ran or reviewed no realized scientific results.

1. **Material findings.** My material findings are B1 and B2 (blockers) and N1-N6 (non-blocking), above. All are D3 architecture findings. I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings. I launched no agents. The tools I ran are listed in section 10, and none produced a finding beyond those stated.
2. **Realized results.** I produced, ran or reviewed none, and prepared no gate evidence, so no null envelope is owed. The unit tests, the PEM tests and the diagnostic model are software checks on documents and a model, not realized scientific results.
3. **Variants.** Yes, design and interpretation variants only. This was not result selection over data.
   - **B1 repair options:** four, (a)-(d).
   - **B2 repair options:** four, (a)-(d).
   - **Selection criterion for both recommendations:** preserve the owner-required property with the least added mechanism (convergence owner, "Active simplification trigger").
   - **Clause readings, kept as findings rather than resolved:** two readings each of four clauses:
     - which declaration "complete observed reads" names (B1);
     - "same target" with or without the rendered core (B2 b1);
     - whether a decision may target a no-longer-derived gate obligation (B2 b2);
     - anchor recognition in unclassified types (N2).
   - **Diagnostic model:** run once, default mode only.

   No data, held-out set or delegated search was involved. The recommendations are non-binding; the stakeholder chooses.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment; no scientific or numerical formulation is accepted for the SSDS product. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, kernel, convergence, evidence, workflow);
   - the proposed workplan;
   - the stakeholder record.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The following are shared dependencies:
- the corpus;
- the inherited workplan framing;
- the prior Review records (twelve of the thirteen Manual Reviews same-family);
- the diagnostic model;
- the toolchain.

The 3540d98 and Phase B reviewers were of another family (GPT). Fresh context does not establish epistemic independence.

Both blockers entered through repairs that followed the e9e6e9f record's own suggestions, a same-family record:
- B2's lifting rule adopted that record's direction ("not superseded by its own author's later `UNQUALIFIED` `ACCEPT`"), which omitted the superseder's standing and the target and run keys;
- B1 entered through its N4 request to "state once whether complete observed reads bound the closure".

Same-family suggestion and same-family repair have now carried a defect forward in two consecutive rounds. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.

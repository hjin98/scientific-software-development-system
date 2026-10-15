# SSDS 8 Architecture Manual — Independent D3 Review, candidate 362af9f

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: 362af9f4944aa3a04455884add03e969f2e7390a
    SCOPE: whole proposed Manual as durable D3 owner: (a) closure of workplan §21 and both §16.2 tables;
           (b) fidelity and refinements R1-R12; (c) adequacy (out-of-matrix); (d) inheritance, capability
           transfer and PEM HAS; (e) qualification design; (f) doctrine-realization map; (g) O1
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md, blob 17882cebaa908bd2b04239749e83e210b6b0ef65
    CLOSURE MAP (aid, not authority): qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md,
           blob d63d837fe8385eace7f4ec01bac05d999e06a2a5
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
           27EF339, 5C55D4B, 575DC78, F7419D5, B46C250 (same family), B46C250 (different family) and F22B4DC;
           Phase B PASS E23F142
    REVIEW METHOD: immutable-candidate reconstruction (git archive of the candidate), whole-Manual read,
           deductive falsification in both directions with family/sibling closure (convergence owner,
           "Review strategy after recurrence"), prior-finding regression, G1 document checks
    REVIEWER: Claude model family, the same family as the Manual's author; a fresh-context sub-agent
           launched by the authoring session, with none of the authoring conversation
    MUTATION: this record only; no commit, no push

All Manual section numbers refer to the candidate blob above. Governing owners are quoted at the public-source commit `aaeaf8b`.

## SERIOUS CHALLENGE

**None against accepted authority.** SSDP 7.2.1, the reviewed workplan contract, the frozen Architecture 1.6.0 and the stakeholder record are not shown to be false, contradictory or unrealizable. The blocker below is a defect in the proposed D3 Manual. The owners it violates are coherent and realizable.

Owner texts applied (public source `aaeaf8b`):

| Owner | Exact text |
|---|---|
| D3 role, Independent Review and Challenge | "Literal workplan compliance is insufficient when the workplan/architecture itself is too weak for the protected outcome." |
| Architecture, D3 formal-contract discipline | "When an architectural concept carries normative meaning, define it before dependent invariants use it" |
| Evidence, Assessment disagreement | "Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position." |
| Evidence, Assessment disagreement | "supersession/adjudication must be explicit enough to distinguish resolved reassessment from still-live disagreement" |
| Workflow, Human gates | "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." |
| Workflow, Review | "A synthesizer reconciles findings through evidence and owner adjudication; it cannot erase unresolved contradictory material evidence by vote." |
| Convergence, Active simplification trigger | "Active simplification/re-derivation is **mandatory before another additive durable repair**" under the stated recurrence triggers |
| Convergence, Review readiness | "Review sufficiency is not proof of zero conceivable defects." |

Manual texts the blocker shows the Manual itself violates (candidate):

- §0.4 C2: "same canonical inputs and ruleset give one derived state"; P3: "derived state is rebuildable; canonical records win".
- §3.1: "Purely operational facts — task issue, reservations, leases, worktree creation, agent launch, retries — live in the Dispatcher's private operator journal ... They influence scheduling, never derived workflow state."
- §5.1: "The ruleset and effective structure are read from `L_n`; nothing is supplied from outside."
- R9 (why column): "b595f2c B4: a review or acceptance disagreement is never resolved by re-dispatch, count or order."
- R12 (why column): "Only withholds support".
- §31.5: "The same cases run for `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS`, `GATE_DECISION` and `INTAKE_DISPOSITION`", after the case "a new candidate with identical changed-unit content and an independent `PASS`: the `PASS` is vetoed ... and nothing integrates (c6da678 B2)".

## Verdict

**NO-PASS.** One blocking D3 family survives: **B1**, the **revision-run identity as SD-26 realizes it**. It has two blocking cases:

- **B1-A (gate family, permissive).** SD-26 makes every enactment its own revision run. A `NATIVE` D1/D2 gate obligation carries the run, and the gate veto compares gate obligations. So a standing human gate `REJECT` no longer vetoes a later iteration's passing gate decision on **identical** content. A re-dispatch plus another holder's `ACCEPT` integrates the revision, and no adjudication obligation is ever derived. This regresses b595f2c B4 and c6da678 B2 for the gate kind, contradicts §31.5, and makes R12's "Only withholds support" false.
- **B1-B (cutover run identity, undefined).** A cutover's run is "the task issued to carry it out". Task issue is an operator-journal fact that the derivation never reads (§3.1). Yet the run must parameterize obligations and be checked by Admission (steps 2 and 3) before any record bound to that task exists. f22b4dc B1-E is therefore only partly closed.

One non-blocking sibling is in the same family (N1): the "one enactment, one integration" refusal contradicts the reviewed recovery route that re-applies an overtaken or fenced integration.

The SD-26 repair otherwise closes what it targets. f22b4dc B1-A, B1-B, B1-C, B1-D(i)-(ii) and B1-F are closed. B1-D(iii) is partly closed. Every f22b4dc non-blocking finding except N5 is closed, and N5 is partly closed. The assessment-disagreement matching clause (§6.5-§6.6) and the content-identity family have no new defect.

This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blocker by earliest owner

### B1 — SD-26's per-task revision run is not reconciled with every consumer of the run

**Family and earliest owner.** Proposed D3, Manual. The sections involved are:

- §5.2 (`rid` as an S0 fact, `tgt`);
- §5.5 (`same` for `GATE_DECISION`, `vetoed`, `elig`);
- §10.2 (revision run; obligations carry `rid`);
- §10.3-§10.4 (answering; `REFUSED`);
- §8.3 steps 2, 3 and 7;
- §19.5 item 3 (cutover);
- §0.3 R9, R10, R12;
- §31.5-§31.6.

These realize workplan §21 items 5 (frames, declared frame per kind), 7 (obligation rules, discharge) and 13 (cutover).

**Recurrence.** This is a **non-local recurrence**. It is the eleventh round of the gate-qualification and run-identity family (3540d98 B3 → … → b46c250 B1 → f22b4dc B1). Both cases arise from the f22b4dc repair: SD-26 made the run finer (one per producing task) without re-deriving the consumers that key on a run indirectly (through obligation identity) or that need the run's event identity to be a ledger fact before the event. B1-A has a latent precursor. Since SD-22/SD-25, a different item or an absorbed revert could already split the run and escape a gate `REJECT`. SD-26 makes the escape reachable by the cheapest route, a mechanical re-dispatch of the same obligation.

#### B1-A. Permissive: a re-dispatched iteration with identical content escapes a standing human gate `REJECT`

**Contract text the trajectory follows (Manual, candidate):**

- §10.2: "`ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` carry `rid_G(s)` among their parameters, so a new run derives new obligations".
- §10.2: for an integration, `ι` is "its enactment (the producing task, §5.2)", and "In a frame `D_n[X]` where `X` changes `cur(s)` ..., `ι` is `X`'s enactment".
- §5.2: "A later implementer iteration, a partition part (§13.7) and a re-dispatch of a reopened obligation are new tasks and so new enactments."
- §5.5 `same`: "`GATE_DECISION`, the same gate obligation and subject revision"; `elig` reads "the gate obligation `G` derives for `g` (its subject triple and, for a `NATIVE` D1/D2 subject, its run `rid_G(s)`)".
- §5.5 `same` for `ACCEPTANCE`, by contrast: "the same `(s, scope_id, rev)` in any frame or tenure", and for `REVIEW` of a transformation: "the same plan item at any of its revisions and the same candidate content".
- §16.6 section 2: earlier enactments' identical-content decisions are shown "as display only ... Such a decision supports nothing here".

**Setup.**
- `s` is a `NATIVE` D2 subject at `r0`, valid.
- Policy requires a D2 human gate `g`, and names two qualified gate holders `H` and `H2`.
- `I` is an accepted `AUTHOR` item (authority D2) with `gates = [g]`. Its obligation is `o = AUTHOR(I)`.

**Trajectory.**

1. **Iteration 1, gate `REJECT`.** Task `t1` submits `X1`, changing `s` from `r0` to `r1`.
   - Its `TASK_RESULT` holds the revision-assessment entry for `(s, r1)`, naming run `(s, t1)`.
   - `REVIEW(X1)` passes. The human acceptor's `ACCEPTANCE PASS j1` is admitted in `X1`'s frame.
   - On `GATE(g)` for `(s, σ, r1)` and run `(s, t1)`, holder `H` records `GATE_DECISION REJECT h⁻`. It is adverse, so it is admitted whatever the revision-assessment state (§8.3 step 7). It answers the gate obligation adversely (§10.3), and `gterm = F` in `X1`'s frame.
   - `o` stays undischarged and `X1` cannot integrate.
2. **Re-dispatch.** `o` is an implementer obligation. It is not a judgment obligation, so it has no answered latch. It is still `OPEN` and ready (§10.3), and the Dispatcher dispatches iteration 2 within budget (§13.7). The principal may equally decide `RESOLVE_LOCAL` on the routed adverse answer. Neither step needs a human.
3. **Iteration 2, identical content.** Task `t2` submits `X2`, a new commit with `s` at exactly `r1`. If an unrelated integration moved the base, even the same commit gives a new `id(X)`.
   - `X2` is a new enactment, so `rid_{D_n[X2]}(s) = (s, t2)`.
   - `t2`'s result carries the revision-assessment entry for `(s, r1)` in run `(s, t2)`.
   - `REVIEW(X2)` passes. Iteration 1's review does not act here, and no `REVIEW NO_PASS` exists.
   - The acceptor records `j2`. No `ACCEPTANCE FAIL` exists, so nothing vetoes it.
   - `GATE(g)` in `X2`'s frame is a **new obligation**, because its run parameter is `(s, t2)`. `H2` records `GATE_DECISION ACCEPT h2`, `UNQUALIFIED`. The gate core displays `h⁻` (§16.6 section 2).
   - `same(h⁻, h2)` is false because the gate obligations differ. So `vetoed(h2)` is false, `elig(g) = {h2}` and `gterm = T`. `REFUSED` (§10.4) does not apply, and `ADJUDICATE_DISAGREEMENT` (§10.2) is not derived, because no standing adverse judgment vetoes anything.
4. **Integration.** `X2` integrates, and `valid(s) = T`. `h⁻` stays admitted and standing, but it vetoes nothing.

**Violation.**

- A human gate holder's standing objection to exactly this D2 revision is set aside without the objector's reassessment, the owner's adjudication or an upheld challenge.
- The objection is set aside by a re-dispatch followed by a later decision of another holder. That is resolution by re-dispatch and by "latest-editor order", which the evidence owner forbids for disagreement, the workflow owner forbids for synthesis ("cannot erase unresolved contradictory material evidence by vote"), and R9 itself excludes: "a review or acceptance disagreement is never resolved by re-dispatch, count or order".
- The orchestration machinery (a mechanical re-dispatch, or an R1 principal decision) moves the decision from a disagreement owed to the owner into a fresh gate. That reaches the same outcome as letting orchestration choose which human's decision governs.
- The Manual contradicts itself. §31.5 requires the identical-content new-candidate veto for `GATE_DECISION` ("The same cases run for ... `GATE_DECISION`"), and R12 claims SD-26 "Only withholds support". The normative §5.5 and §10.2 give the opposite.
- The other judgment kinds keep the veto. An `ACCEPTANCE FAIL` vetoes the same triple in any frame or tenure, and a `REVIEW NO_PASS` vetoes the same item's identical content. So the D1/D2 gate, the highest-consequence human decision, is the only judgment kind that re-dispatch escapes.

**Siblings (one cause).**
- (i) The same escape through a different `AUTHOR` item reaching identical bytes. This existed under SD-25 as well (a different lineage was a different run).
- (ii) Through an absorbed revert `r1 → r2 → r1`, which gives a new run `(s, entry)`. This existed since SD-22.
- (iii) Through an identical-transformation resubmission, if an implementation takes the integrating task rather than the first submitter as the enactment (see N3).

SD-26 adds the same-obligation route, which needs no other item, no foreign change and no human.

#### B1-B. Undefined: a cutover's run is identified by a task-issue fact that the ledger does not hold when the run must be named

**Contract text (Manual, candidate):**

- §10.2: for a cutover, `ι` is "the task issued to carry it out (§19.5)". `rid` is "known before the event ... An S0 fact".
- §10.2 `REVIEW(s, r)` row: derived "in the admitted state, the native revision `r` of a subject whose cutover is requested (§19.5), for its prospective `NATIVE` tenure". Obligations "carry `rid_G(s)` among their parameters", and an obligation's identity is "deterministic from its derivation".
- §19.5 item 3: "`REVIEW(s, r)` is derived for that prospective tenure once the cutover is requested, by a `MIGRATE` item ... or by the cutover gate's derivation", and "the cutover is carried out by one task the Dispatcher issues for it once it is requested (bound to the `MIGRATE` obligation, or to the cutover gate's request), and the run it starts is identified by that task (§10.2), so the records made for it name that run before the cutover is admitted".
- §8.3 step 2: a run a record names must be, for a requested cutover, "the run that cutover's task starts". Step 3: "the envelope names an obligation existing at the request's base".
- §10.3: "A **task** is identified by a 128-bit random identity the Dispatcher issues in its envelope." §3.1 places task issue in the operator journal. §12.2: admitted records carry the binding, "so derivation and replay read it from the ledger alone". So a task's identity enters `L_n` only through a record bound to it.

**Trajectory (gate route, no `MIGRATE` item).**

1. A `LEGACY(p)` D2 subject `s` has its cutover requested through the cutover gate's derivation, with native revision `r`.
2. The Dispatcher issues cutover task `t_c`. Its identity is in the operator journal only.
3. Derivation must now derive `REVIEW(s, r)`, `ACCEPT(s)` and `GATE(g)` for the prospective native tenure, each with parameter `(s, t_c)`.
4. `L_n` holds no record bound to `t_c`. The records that must name the run all precede any record of `t_c`:
   - the revising reviewer's `TASK_RESULT` (a different task);
   - the owner's prospective acceptance (direct human);
   - the gate decision (direct human).

   §3.1 and §5.1 forbid derivation from reading `t_c` from the journal.
5. A conforming implementation therefore has three choices, and each is defective:
   - **(a) Derivation reads the Dispatcher's journal or envelope.** This violates §3.1, §5.1 and §26.1. Two hosts with the same `L_n` and different operator state derive different obligations, contrary to C2 and P3.
   - **(b) The obligations are not derived until a `t_c`-bound record appears.** Then the reviewer's envelope names no obligation existing at base (step 3 `AUTH_ENVELOPE`), and step 2 has nothing to check against. The cutover can never be prepared, so the G4 path is dead.
   - **(c) Step 2 accepts any run value.** Then the check §19.5 relies on is void.

**Gate-route self-reference.** On the gate route, the task is "bound to ... the cutover gate's request", whose obligation identity includes `rid`, which includes the task. The derivation cannot compute that obligation before the task exists. This is the f22b4dc B1-E self-reference in a new form.

**`MIGRATE` route.** When several `MIGRATE` iterations exist, or a cutover task ends `BLOCKED` and is re-issued, nothing says which task is "the" cutover task before one of them carries out the cutover. Records naming another task's run are admitted but never count. That is restrictive and silent.

**Uniqueness.** The premise of §10.2's uniqueness claim is not fully stated. Step 7 refuses a second integration of one enactment and a second cutover by one task, but not an integration by a task that already carried out a cutover, or the reverse. I found no harmful trajectory from this, because every later change still gets a fresh `ι`. It is listed because §10.2 asserts "no two events share `ι`" without that case.

**Violated text.**
- The architecture owner's "define it before dependent invariants use it".
- The Manual's own §3.1, §5.1, C2 and P3.
- Workplan §21 item 13 (cutover) remains unresolved for the identity that Admission steps 2 and 3 and the obligation identities depend on.

#### Family assessment and options for the stakeholder

**Common cause.** SD-26 put a run's identity on the producing task. Two kinds of consumer were not re-derived:

- consumers that see the run only through **obligation identity**: the gate veto's `same`, answering and `REFUSED`;
- consumers that need the event's identity **as a ledger fact before the event**: cutover obligations and step 2.

A third consumer, the reviewed re-application of an overtaken integration, collides with the new refusal (N1). This is not a clean local defect. But the repairs below remove or narrow mechanism rather than adding another per-consumer clause, as the convergence owner's simplification trigger requires.

**Option 1 (recommended; narrows mechanism).**
- **(a) Gate veto.** Key `same` for `GATE_DECISION` on the gate `g` and the subject triple, in any frame, tenure or run, exactly as `ACCEPTANCE` already is. Keep the run only in `tgt` and `elig`, which govern passing support.
  - This removes the run dependency from the veto, closes B1-A and siblings (i) and (ii), and makes §31.5 and R12 true.
  - Cost: a `REJECT` on revision `r` also vetoes later runs that reach `r` (reverts, other items) until its author or the owner lifts it, which is how `ACCEPTANCE FAIL` already behaves.
- **(b) Cutover.** Delete the separate cutover-task identity. A cutover rides on the integration of a transformation:
  - with a `MIGRATE` item, that item's iteration;
  - for a pure mode change, an empty-content transformation submitted by the cutover task's `TASK_RESULT`.

  Its `ι` is then that producing task, which is in `L_n` before any record names the run, exactly as for every integration. `REVIEW(s, r)`, `ACCEPT` and `GATE` for the native tenure are derived in that frame, and the admitted-state cutover clauses of §10.2 and §8.3 step 2 are deleted. This removes a special case. A records-only variant would need a task to submit its result before carrying out the cutover, which conflicts with "every task ends in exactly one `TASK_RESULT`", so the integration form is the narrower one.
- **(c)** Settle N1 by stating that re-application is a new task and a new run, listed as a narrowing.

**Option 2 (stakeholder-level).** Keep run-scoped gate obligations and declare that a D1/D2 gate judges one revision run (one change), not a revision. A `REJECT` then binds only its run, and a re-dispatched identical iteration is gated afresh, the earlier `REJECT` being display only.
- This must be listed as a narrowing of R9 and as part of R12, and §31.5 corrected.
- It accepts that mechanical re-dispatch can route a human gate disagreement to another holder without adjudication.
- I would not recommend it. It is the only option that keeps SD-26's per-iteration gate symmetry, so it belongs to the stakeholder.

**Option 3 (not recommended).** Key the veto on the obligation lineage while keeping runs per task. That reintroduces two notions of run identity, the per-consumer scoping the f22b4dc Review warned against.

**Provenance.** SD-26 chose "one task result plus its clean rebases is one enactment and one run". It did not decide the reach of adverse gate decisions or the cutover's ledger identity. Those realizations were the author's under item 19. I would put Option 1(a) versus Option 2 to the stakeholder.

#### Required discriminators

These run at real owners (Admission → Derivation → discharge → Dispatcher → inspector), with nothing seeded resolved.

- **(A) B1-A as written.** After `t2`'s identical-content iteration and `H2`'s `ACCEPT`:
  - `h2` is vetoed;
  - `GATE(g)` is `REFUSED`;
  - `ADJUDICATE_DISAGREEMENT(h⁻)` is derived;
  - `X2` does not integrate.

  The same holds for siblings (i) and (ii). Contrast: an iteration yielding `r2 ≠ r1` is not vetoed. An implementation keying the gate veto on the run-parameterized obligation identity must fail. Under Option 2 the expected values invert, and §31.5 must say so.
- **(B) B1-B, both routes.** Two derivation hosts with the same `L_n` and different Dispatcher journals derive identical cutover obligations and identical step-2 verdicts. Records for a cutover are admissible only after the ledger holds the task identity they name. A re-issued cutover task leaves no record of the first task counting. An implementation reading the journal must fail.

## 2. Non-blocking findings

**N1 — "One enactment, one integration" contradicts the reviewed re-application of an overtaken or fenced integration (B1 family sibling; unlisted narrowing).**

What the reviewed workplan says (§15.3):
- "An `OVERTAKEN` admission ... an obligation to revalidate its request is derived (§8.2)", where §8.2 means rebased, re-derived, "affected judgments re-requested";
- after a landed fence, "the choices are to re-apply `n` (an ordinary revalidated admission onto `F_n`)".

The Manual keeps both texts:
- §22.2: "until the revalidated request publishes and realigns";
- §22.3: "re-apply `n` (an ordinary revalidated admission onto the fence)";
- §9.1: "never rejected outright".

But a rebase of `n`'s transformation onto the fence is a clean rebase of the same enactment. §8.3 step 7 refuses it (`OBLIGATION_REENACTED`).

The only conforming route is a new task under `REVALIDATE_OVERTAKEN`. That means a new enactment, a new review of the new transformation and, for every `NATIVE` D1/D2 subject it changes, a new run with a new revising review, R3 acceptance and human gate.

Consequences:
- The route is restrictive and safe.
- It is not listed in §0.3. R12 lists only workplan §6.9, and closure map item 6 still says "CARRIED".
- It makes R4's stated cost ("costs a fence (and its human decision)") and §22.3's "loses nothing" understatements. A publisher crash inside a 300-second window now costs a full re-gating of every D1/D2 revision the admission carried.

Repair: state that re-application is a new task, and list the narrowing as R12 or R4. Alternatively, exempt the revalidation of an `OVERTAKEN` admission from step 7 with `ι` = the re-applying entry. That would add mechanism, so the listing is preferred.

**N2 — Partition claim bookkeeping (f22b4dc B1-D(iii), partly closed).** §13.7 now says "each part's integration claims only its own share of the item's obligations; each part is its own enactment". Acting and run identity no longer depend on the bound obligation, so the residual is bookkeeping. Two questions remain:
- Which derived obligation does each part's envelope name? The envelope has one `obligation_id` (§12.2).
- What does "claims its share" mean for §8.3 step 7's "its discharge predicate (§10.4) holds after the request's own records"? The item-level obligation discharges only when every part has integrated and the item-level review has passed.

State the binding. This is D4-resolvable once stated.

**N3 — Enactment of an identical transformation submitted by a later task.** §7.1 fixes `id(X)` "by the task result that first submits the candidate", so a later task resubmitting the same commit on the same base produces the same transformation. §5.2 defines an enactment as "the transformations of one producing task", which presumes one producer per transformation.

- If the first submitter is the enactment, an earlier iteration's frame records act after the later task's integration. That contradicts the literal R12 and §5.2 sentence "A record made in an earlier iteration's frame therefore never acts". It is harmless, because the content is identical.
- If the integrating task is the enactment, run identity splits again and sibling (iii) of B1-A opens.

State the first-submitter reading.

**N4 — Rebase registration.** Acting in `D_n[X']` and `rid_{D_n[X']}` need the derivation to know that a machinery rebase `X'` belongs to the producing task's enactment before integration (for example, for re-requested reviews). No admitted record is named for that. D4 can bind it through Dispatcher-submitted records under the task's envelope. State it.

**N5 — Residue of the lineage vocabulary.**
- §30 still says "a frame record of another pending lineage no longer supports", and lists neither SD-26 withdrawal: rule-1 later-iteration carry, and same-enactment re-application.
- §31.6 (G) and (H) still say "different lineage" and "another lineage".
- §6.1's family rule ("standing: a stop earned by supersession stands on immutable facts and its own record's standing") does not say that a supersession stops a failure only in states where it acts. §5.2 and §6.7 do say so.

This is editorial, and the governing text is unambiguous.

**N6 — Qualification gaps (DS-001).**
- §31.5 asserts the identical-content gate veto that §5.5 and §10.2 now deny (B1-A).
- §31.6 (L) "records naming the pending cutover's run pass step 2" cannot be implemented from the ledger (B1-B).
- No case re-applies a fenced or `OVERTAKEN` integration under SD-26 (N1).

A §31 transcribed from the present normative rules would fail §31.5, while one transcribed from §31.5 would contradict the rules. These are design-program omissions, not runtime demands at G1.

**N7 — Stakeholder-level trade-offs (reported as such, not blockers).**
- SD-17's partial reversal (stops need a bounded reproduction).
- SD-24's narrowing.
- The exact-identity cost.
- SD-25's consequences: cross-candidate support withdrawn, frame `REJECT` persistence, gate-member accumulation.
- SD-26's per-iteration acceptance and gate cost. Closure map §5 lists it, and §32.3 asks for it to be measured.
- Phase B N1 (paraphrase-only adoption instruction), still disclosed in §32.2.

Repair directions from candidate 13 onward are the author's under item 19. Option 1(a) versus Option 2 of B1 belongs with them.

## 3. Closure audit: workplan §21 and §16.2

**Method.** For every §21 item I located the deciding Manual section myself during a whole-Manual read, using the closure map only to find text faster, and checked the map's citations for the rows SD-26 touched (items 5, 6, 7, 13 and 24).

The diff `f22b4dc..362af9f` changes only these parts of the Manual:
- §0.3 (R12 and the history paragraph);
- §5.2;
- the §5.5 gate-term prose;
- §7.3, §7.5 and §7.6;
- §8.3 steps 2 and 7;
- §10.2 and §10.4;
- §13.7;
- §16.6;
- §19.5;
- §31.6;
- §32.3.

For the items whose text is unchanged since `f22b4dc` (1-4, 8-12, 14-23, 25-27), I spot-checked each section during the read and found nothing unresolved.

**Not substantively resolved at this candidate:**

| §21 item | Clause | Gap |
|---|---|---|
| 13 | cutover | The run a cutover starts is identified by an operator-journal fact that the derivation cannot read, while obligations and Admission steps 2 and 3 need it before any record of that task exists (B1-B) |
| 7 | obligation rules | The D1/D2 gate obligation's run parameter removes the veto from identical-content re-dispatch. The rule set is coherent only if Option 2 is adopted and listed (B1-A) |
| 6 | reconciliation procedure | Decided, but the reviewed re-application route is narrowed without a listing (N1, non-blocking); the closure map row still says CARRIED |
| 24 | task-partition checks | Decided; the claim bookkeeping is underspecified (N2, non-blocking) |

**§16.2.** Both tables are resolved in §26.4. I read §26.4 in full. Every invariant 1-26 and every frozen surface §3-§22 has a final disposition, and the workplan's **Deferred** rows have theirs:

| Deferred row | Resolved by |
|---|---|
| invariant 4 | single root |
| invariant 9 | benchmark fields |
| invariant 15 | harness-adapter verbs |
| invariant 17 | capability keys |
| invariant 26 | containment root |
| §5 | sub-rules adopted one by one |
| §6 | composition SPI |
| §7 | `CandidateRef` and `StageResultEnvelope` declined, the rest mapped |
| §9-§11 | function replacement |
| §12 | `[ssds]` configuration |
| §18 | §26.2 |

None is unresolved.

**Material decision versus delegated choice.** `[delegated]` marks remain on genuinely D4 choices: diff implementation, checkpoint encoding, parser libraries, mutation tool, limit values, reason-code members. B1-B is an under-specification that an implementer would have to decide architecturally. I found no new over-specification.

## 4. Refinements R1-R12

| # | Assessment |
|---|---|
| R1 | **Sound.** Unchanged since `f22b4dc`. `on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction, and the guard keeps `on⁻` a function of the record and `K`. The acting rule does not touch observations (§5.2 now says so). |
| R2 | **Sound.** The clamp is unchanged. `acts`, `superseded_G` and `rid` are S0 and add no support edge. |
| R3 | Sound. |
| R4 | **Sound as a mechanism.** Its stated cost is now understated: a fenced admission's re-application is a new task and, for D1/D2, a new run with a full re-gating (N1). |
| R5, R6, R7, R8 | Sound, unchanged. |
| R9 | **Core sound** for every kind except the `NATIVE` D1/D2 `GATE_DECISION`. There, the veto's `same` inherits SD-26's per-task run through the gate obligation, so re-dispatch escapes a standing `REJECT` (B1-A). This contradicts R9's own "never resolved by re-dispatch". The SD-25 clause ("a reassessment or adjudication ends it only in the states where that record acts") is now sound at enactment granularity: f22b4dc B1-B is closed. |
| R10 | **Sound for integrations, absorptions, adoptions and re-identification.** Every later change of `cur(s)` gets a fresh `ι`, so no D1/D2 revival on revert survives (f22b4dc B1-A closed). **Undefined for cutover** (B1-B). |
| R11 | **Sound.** `gterm` minimum, `unq` and the adequacy refusal are unchanged. `elig` over acting records closes f7419d5 B1 (vii) again. |
| R12 | **Sound in its support direction**, which matches SD-26: a later iteration records its own acceptance and gate, and a rejected iteration's or partition sibling's frame records never act. **Its claim "Only withholds support" is false.** SD-26 also narrows the adverse gate veto across runs (B1-A) and narrows the reviewed re-application route (N1). Both must be repaired or listed. |

## 5. Previous findings re-derived

"Closed" means I re-derived that the present text excludes the named trajectory. It is not runtime evidence.

**Depth.**
- In full against the new text: the `f22b4dc` blocker cases and N items, and both `b46c250` Reviews' blockers.
- For older records, I took the `f22b4dc` dispositions as hypotheses. I confirmed that the cited text is unchanged except for the hunks listed in section 3, and I re-checked each family's governing mechanism during the whole-Manual read:
  - SD-17/18 classes in §6.5 and §17.5;
  - `link⁻`;
  - the effect-keyed write set in §1.2;
  - the domain rule in §13.2;
  - R8 supersession authority;
  - the R9 veto table;
  - `ref` locality;
  - exact identity in §1.5;
  - `ext` in §6.5;
  - the §22.3 publication procedure.
- I did not re-read every older record's prose.

### F22B4DC

| ID | Disposition |
|---|---|
| B1-A (same-obligation restoration revives D2 validity) | **Closed.** A re-dispatch is a new task, so `rid = (s, t2)`. `j1`, `h1` and `t1`'s record are in no run. `ACCEPT`, `GATE` and `REVIEW(s, r1)` are derived. A second integration of `t1`'s transformation is refused. The livelock reading is gone, because §10.4 now states non-latching discharge and re-dispatch as a new task. |
| B1-B (rejected iteration's frame reassessment acts after a later iteration integrates) | **Closed.** `d` declares `X1`'s frame. `X1`'s enactment never integrates, so `d` never acts in `D_n` or in `D_n[X2]`. `f` keeps vetoing, and `ADJUDICATE_DISAGREEMENT(f)` stays derived. The gate variant keeps `P`, and the disposition variant keeps `undisputed = P`. |
| B1-C (earlier iteration's gate decision eligible when identical bytes arrive) | **Closed for passing decisions** (they never act). §31.6 (F) is now consistent with §5.5. The **adverse** counterpart, an earlier iteration's `REJECT` no longer vetoing, is B1-A. |
| B1-D (i) acting across partition parts, (ii) run identity | **Closed**: each part is its own task and enactment. |
| B1-D (iii) binding | **Partly closed** (N2). |
| B1-E (cutover run) | **Partly closed.** A second cutover by one task is refused, and a re-cutover is a new task. The identity is still not a ledger fact when it must be named (B1-B). |
| B1-F (re-identification `ι`) | **Closed**: the admitting entry. |
| N1 (§6.6 permissive reads outside the acting rule) | **Closed**: §5.2 states that observations and discriminating readings are outside the rule, and why. |
| N2 (unlisted narrowing) | **Closed** for the two §6.9 clauses (R12). A new unlisted narrowing is N1 here. |
| N3 (gate-term prose) | **Closed**: §5.5 now says a frame `REJECT` vetoes in the admitted state at once, and §32.3 states the pending effect. |
| N4 (non-latching implementer discharge) | **Closed** (§10.4, §32.3). |
| N5 (qualification gaps) | **Partly closed**: (I)-(M) are added and (F) is consistent. New gaps are in N6 here. |
| N6 (trade-offs) | Stakeholder matter; carried in N7. |

### B46C250 — different family (GPT)

| ID | Disposition |
|---|---|
| B1-A (frame supersession lifts admitted veto) | **Closed**, including through rejected iterations and partition siblings |
| B1-B (frame supersession drops admitted `P`) | **Closed**, with the same scope |
| B1-C (frame identity computable) | **Closed for integrations**: `rid = (s, task)` is known once the `TASK_RESULT` is admitted. For cutover, see B1-B here |
| B1-D (unchanged-subject run membership) | **Closed** |
| N1 | Closed |
| N2 | Closed as disclosure |
| N3 | Closed |
| N4 | Partly closed (N6) |
| N5 | Stakeholder matter |
| N6 | Closed |

### B46C250 — same family (Claude)

| ID | Disposition |
|---|---|
| B1 (i)-(ii) | Closed at enactment granularity |
| B1 (iii) identity | Closed except cutover (B1-B) |
| B1 (iv) | Closed |
| N1, N3 | Closed |
| N2 | Disclosure |
| N4 | Partly closed (N6) |
| N5 | Stakeholder |

### F7419D5

| ID | Disposition |
|---|---|
| B1 primary, (i)-(vi), qualified variant | Closed (state-relative `superseded_G`; `elig` over acting records; no hygiene rule) |
| **B1 (vii)** | **Closed again**: an abandoned or earlier iteration's decision never acts |
| N1-N3, N5 | Closed |
| N4 | Partly closed (N6) |
| N6 | Stakeholder |

### 575DC78, 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC

| Review | IDs | Disposition |
|---|---|---|
| 575DC78 | B1 | Closed (`gterm` minimum unchanged) |
| 575DC78 | N1-N7 | Closed |
| 5C55D4B | B1, B2 | Closed (bounded reproduction anchors `link⁻`; regions compared by content) |
| 5C55D4B | N1-N7 | Closed, apart from the stakeholder items |
| 27EF339 | B1, B2 | Closed |
| 27EF339 | B3 | Closed for its trajectory (frame gate decisions declare their frame); the family recurs as B1 |
| 27EF339 | N2 | Stakeholder |
| 27EF339 | others | Closed |
| 0B6C4FA | B1 | Closed |
| 0B6C4FA | B2 | Closed for its trajectory; family B1 |
| 0B6C4FA | N1 | Stakeholder |
| 0B6C4FA | N2 | Partly closed as before: an author may supersede its own decision while a blocking challenge is open; author-accountable |
| 0B6C4FA | others | Closed |
| A18B544 | B1, N1-N5 | Closed |
| A18B544 | B2 | Closed for its trajectory; family B1 |
| A18B544 | N6 | Superseded |
| E9E6E9F | B1, N1-N5 | Closed or superseded |
| E9E6E9F | B2 | Closed for its trajectory; family B1 |
| E2154AC | B1, N1-N5 | Closed |

### 3540D98 (GPT family)

| ID | Disposition |
|---|---|
| B1 | Closed (exact identity, §1.5) |
| B2 | Closed (complete external-input record) |
| B3 | Closed for its qualified-gate trajectory; the gate family recurs as B1-A |
| B4 | Closed (equal regions) |
| N1 | Prospective run representation closed for integrations; cutover open (B1-B) |
| N2-N4 | Held as disclosures |

### 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363

| Review | IDs | Disposition |
|---|---|---|
| 798B2B4 | B1-B3 | Closed. The protected property (no D1/D2 revival on revert) now holds on every integration and absorption route |
| 798B2B4 | B4, N1-N8 | Closed |
| 71CF9B3 | B1 | Closed |
| 71CF9B3 | B2 | Closed in text and in realization (R10), apart from cutover's undefined identity |
| 71CF9B3 | N1-N8 | Closed |
| 86AB683, 1FFBBF0 | B and N items | Closed (SD-18 class rule in §6.3, §6.5, §17.5 unchanged) |
| 53669A5 | B1-B3, N2-N9 | Closed |
| 53669A5 | N1 | Stakeholder |
| D837363 | B1-B4, N1-N8 | Closed |

### CC005DB, C6DA678, B595F2C, 6FF4ED1

| Review | IDs | Disposition |
|---|---|---|
| CC005DB | B1-B3, N1-N8 | Closed (`on⁻`'s frozen resolution context; effect-keyed write set; product-scope veto) |
| C6DA678 | B1, B3, N1-N12 | Closed |
| **C6DA678** | **B2** (identical-content new candidate escapes a veto) | **Closed for `REVIEW`, `CONFORMANCE` and every kind but one. Reopened for `NATIVE` D1/D2 `GATE_DECISION` (B1-A)** |
| B595F2C | B1-B3, N1-N8 | Closed |
| **B595F2C** | **B4** (disagreement resolved by re-dispatch, count or order) | **Closed except for the `NATIVE` D1/D2 gate across enactments (B1-A)** |
| 6FF4ED1 | B1-B4, N1-N12 | Closed (R1 guard; R8; plan-prose `ref` locality; the `AUTHOR` item) |

### Phase B §3 closures and N1-N4 carry-forward

| Closure | Present reconstruction |
|---|---|
| Completeness polarity (Phase B N2), both directions | **Held.** Consider an alternate tree differing only outside a recorded narrow basis, with a differing old-content run in (2) and a yielding present-content run in (4), under a bounding judgment that becomes `P`, blocked, revoked or loss-withheld. (2) and (4) read `link⁻`, which never reads completeness, so the claim stays `P`. Losing the judgment only narrows (1) and (3). Restrictive direction: a stop is withdrawn only by a newly admitted narrow anchor that links a differing run, which has a cause and is disclosed (§32.2). The acting rule touches neither observations nor discriminating readings. |
| Support cycles fail closed; corrupt prefixes | Held: the §5.6 clamp and the §5.7 `INTEGRITY_HALT` are unchanged |
| Y1/Y2, X1-X3, candidate-own latch, floor and class | Held (§6.8 unchanged) |
| Contrary-run retention, nondeterminism, U1/U2/W1/W2 | Held (§6.6 unchanged) |
| Absorbed relaxation; adversity vs currency, challenge, loss; salvage; independence; start latch; structure, quarantine, tenure; publication and fencing | Held. Dispositions read acting records at enactment granularity. Re-application after a fence is narrowed (N1) |
| Phase B N1 | Disclosed (§32.2, §32.4) |
| Phase B N3 | Held (§31.3 diagnostic-model limits) |
| Phase B N4 | Held (§32.3 reopen triggers, now including SD-26 costs) |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | D1/D2 gate `REJECT` in iteration 1; re-dispatched iteration 2 with identical content; peer holder `ACCEPT` | **Fails: B1-A** |
| 2 | As 1, but with an `ACCEPTANCE FAIL` instead of a gate `REJECT` | Held: vetoes across runs; `REFUSED`; adjudication derived |
| 3 | As 1, but with `REVIEW NO_PASS` on identical candidate content | Held (same item, same content) |
| 4 | Gate `REJECT` escaped by a different item reaching identical bytes, or by an absorbed revert | **Fails** (latent since SD-22/SD-25; B1-A siblings) |
| 5 | Cutover requested through the gate route: deriving `REVIEW(s, r)`, `ACCEPT`, `GATE`; step 2 and step 3 checks | **Undefined: B1-B** |
| 6 | Cutover through a `MIGRATE` item with two iterations, or a re-issued cutover task | **Ambiguous: B1-B** |
| 7 | One task carries out a cutover and an integration of the same subject | Uniqueness premise unstated; no harm found (B1-B note) |
| 8 | Fenced admission; the human chooses "re-apply `n`" | Refused by step 7; only a new task works (N1) |
| 9 | `OVERTAKEN` by a foreign push; "the revalidated request publishes and realigns" | As 8 (N1) |
| 10 | f22b4dc B1-A (same-obligation restoration) | Held |
| 11 | f22b4dc B1-B (rejected iteration's frame reassessment), all four variants | Held |
| 12 | f22b4dc B1-C (passing decisions); f7419d5 B1 (vii) | Held |
| 13 | Partition parts: acting and run identity | Held; bookkeeping is N2 |
| 14 | Analyzer re-identification and its reversal | Held (entry `ι`) |
| 15 | Identical transformation resubmitted by a later task | Enactment needs stating (N3) |
| 16 | `D_n[X]` versus the post-integration acting set and `rid` | Held: equal sets; equal `rid` (computable once the `TASK_RESULT` is admitted) |
| 17 | Machinery rebase `X'`: acting and `rid` before integration | Needs a stated ledger binding (N4) |
| 18 | A late record in an already-integrated enactment's frame after `s` changed | Held: every later change of `cur(s)` gets a fresh `ι`, so nothing re-enters an old run |
| 19 | Iteration-1 disposition versus an iteration-1 failing assessment counting in the lineage | Held restrictively: the failure counts in iteration 2; the disposition does not act. Disclosed (§32.3) |
| 20 | Discriminating reading in a rejected iteration's frame covering admitted outcomes | Held: coverage is outcome identity under the same reading; class unchanged |
| 21 | Stratification and single-valuedness with `acts`, `superseded_G`, `rid` | Held: all S0, positive in S2 |
| 22 | `LEDGER_LOSS` whose lost interval held an enactment's integration | Held: that enactment's frame records do not act on the retained chain |
| 23 | Phase B N2 polarity with structure, `ignore`, analyzer changes and `K` fixed | Held (guard) |
| 24 | Publication crash windows, fence chains, ABA (§22.3) | Held for safety; liveness narrowed (N1) |

I stopped discovery in B1's family once its common cause was characterized. Further siblings (inspector rendering of runs, other lifecycle events) would be implementation-like. Section 6 is a bounded negative result elsewhere, not a completeness claim.

## 7. Minimum architecture and capability transfer

- **What SD-26 changes.** It replaces the lineage unit by the producing task, adds one refusal (`OBLIGATION_REENACTED`) and one display (§16.6 section 2), and removes the later-iteration carry of prospective acceptances. It adds no component, store, record kind or tier.
- **Withdrawals.**
  - Later-iteration carry (rule 1) is withdrawn and listed (R12). No governing owner requires it.
  - Same-enactment re-application of an overtaken or fenced integration is withdrawn and unlisted (N1). No owner requires that exact route, but R4 and §22.3 claim it.
- **What B1's Option 1 would change.** It removes the run from one comparison and removes the separate cutover-task identity. Net mechanism goes down.
- **§30.** Still accurate apart from the stale SD-25 wording and the missing SD-26 withdrawals (N5).
- **Architecture 1.6.0 supersession (PC-001).** §26.4 preserves the version-bound Level 0 Core, frozen profiles and the single composition root. `orchestrator/docs/architecture.md` is byte-identical to `fad3ee4` (blob `39e6de7`), and nothing under `source/` or `dist/` changed (section 10).
- **PEM Historical Applicability Set.** PEM was activated, because this is replacement of mature machinery under a memory-bound workplan. The PEM file at the candidate is blob `1561797`, schema-valid.

| Entry | Applicable | Disposition |
|---|---|---|
| PC-001 | yes | Held, as above |
| DS-001 | yes | Applied in N6: §31.5 and the normative rule now disagree, and §31.6 (L) cannot be built from the ledger |
| FF-001 | yes, for genesis publication | Held: §19.9 publishes nothing before validation and quorum |
| SP-001 | no | No source-to-package routing change |
| SP-002 | no | No immutable self-reference construction in this cycle |

I did not re-read the archived §18 inheritance workplans. SD-26 touches no inherited capability other than those noted.

## 8. Qualification-design adequacy

- **Status.** §31.1 correctly marks every runtime group `UNEXECUTED`. G1 needs only §31.10, which I ran (section 10).
- **Discrimination.** The real-owner requirement and the negative discriminators are adequate in form. The SD-26 additions (I)-(M) discriminate the f22b4dc cases. But:
  - §31.5's `GATE_DECISION` clause contradicts the normative rule (B1-A);
  - §31.6 (L) presupposes a ledger-derivable cutover run (B1-B);
  - no case re-applies a fenced integration (N1).

  Per DS-001, a §31 implemented to the present expected values would either fail or encode a defect.
- **Executed-evidence claims.** Nothing is claimed as executed beyond §31.10.
- **Diagnostic model.** Optional. I did not run it; it is unchanged and models none of the clauses at issue.

## 9. Doctrine-realization map and O1

- **Coverage.** The map covers all seven 7.2.1 entrypoints: four roles (`source/roles/*`) and three specialists (`source/specialists/*`), plus the scientific checks, with E0-E3 levels and mechanisms.
- **§29.4 revising D1/D2 row.** Its claim "it is current only within that run, so a revert or any change of the revision needs a new record, acceptance and gate" is now true for integrations and absorptions, but undefined for cutover (B1-B).
- **§29.3 "durable authority mutation needs ... human ratification where required" (E0).** It holds as presence. It does not hold for disagreement between gate holders across iterations (B1-A), which the map does not claim.
- **Other rows.** No other row overclaims beyond what the rows' own E2/E3 limits disclose.
- **O1 (§0.5).** Unchanged and adequate:
  - the realized record, readers, routine questions and realized-record architecture are stated;
  - product surfaces are marked within the deliverable;
  - **none** is marked beyond it.

  Product-scope acceptance remains with the stakeholder (S12). Technical Review accepts nothing.

## 10. What I verified and how; what I could not verify

**Verified.**

- Reviewed exactly `362af9f4944aa3a04455884add03e969f2e7390a` through a `git archive` snapshot in scratch. Blobs confirmed: Manual `17882ce…`, closure map `d63d837…`, workplan `91bde23…`.
- Read the whole Manual (2701 lines). In the workplan I read §6.9, §7.8, §12.4, the §15.3 publication and settlement text, and §21.
- Read the f22b4dc Review record in full, the stakeholder record's item 21 and the SD-26 entry, and the closure-map diff.
- Read the governing owners at `aaeaf8b`:
  - the D3 role entrypoint;
  - the architecture owner;
  - the abstraction kernel;
  - convergence ("Active simplification trigger", "Review readiness", "Review strategy after recurrence");
  - evidence ("Assessment disagreement", revert text);
  - workflow ("Human gates", Review).
- Diffed the Manual `f22b4dc..362af9f` by hunk and word (the hunks are listed in section 3).
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at the candidate snapshot: **4 tests OK**.
- `git diff --check f22b4dc4c5cc56da962bee9eca843fa204af40bc 362af9f4944aa3a04455884add03e969f2e7390a`: clean (exit 0).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 362af9f4944aa3a04455884add03e969f2e7390a`: 51 files. They are the Manual, 49 files under `qualification/ssds80`, and `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`. The SSDS workplan blob is unchanged since `fad3ee4`.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4` (empty diff; frozen blob `39e6de7`).
- PEM: `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` gave "PEM schema 1 valid: 5 families, 0 notices". I ran it in the checkout, whose PEM blob `1561797` equals the candidate's.

**Not verified or not established.**

- No production or runtime behavior; none exists at G1.
- The diagnostic model was not run.
- I did not re-read every older Review record's prose, or the archived §18 workplans (section 5 states the depth).
- The B1 trajectories are deductive, from the Manual's own rules, and each premise is cited.
  - B1-A's "different holder" premise needs policy to name two qualified gate holders. §5.5 says "Any qualified holder may record a passing decision".
  - B1-B depends on reading §3.1 and §12.2 as excluding task issue from `L_n`, which they state.

## 11. Scientific-checks answers

- **Material findings.** None about scientific or numerical meaning. B1 and N1-N7 are D3 findings about software that mediates scientific evidence. B1-A affects how disagreement between human gate holders on a D1/D2 revision is resolved.
- **Realized results.** I produced, ran and reviewed no realized scientific results. Null envelope: I examined the Manual's D3 text, the governing owners and prior Review records. Materially unexamined: any runtime evidence (none exists) and the diagnostic model.
- **Variants.**
  - Repair directions: three, of kind D3 options. The criterion was to close both blocking cases, remove or narrow mechanism, and preserve reviewed contracts. Option 1 is recommended; Option 2 is a stakeholder-level alternative; Option 3 is rejected.
  - Trajectories: 24, of kind out-of-matrix, chosen as high-information siblings of the SD-26 clauses and of earlier families (section 6).
- **Reliance on accepted D1/D2 authority.** I relied on no accepted D1/D2 authority for a consequential judgment, so no tension search was owed.
- **Gaps.** Runtime qualification (G2-G4), the full prose of older records, and the archived §18 workplans.

## 12. Common-mode note

- **Family.** I am of the Claude family, the same as the Manual's author and as the reviewers of e2154ac, e9e6e9f, a18b544, 0b6c4fa, 27ef339, 5c55d4b, 575dc78, f7419d5, the same-family b46c250 and f22b4dc. The 3540d98, different-family b46c250 and Phase B reviewers were of the GPT family.
- **Engagement.** I was engaged as a fresh-context sub-agent launched by the authoring session.
- **Shared dependencies.** Fresh context does not make me independent. I share:
  - the corpus;
  - the inherited workplan framing and its run and enactment vocabulary;
  - the prior Review records, which I read and which shaped my attention to run identity;
  - the toolchain;
  - the model family with the author and with most prior reviewers.
- **Provenance of the findings.** Both B1 cases were found by reconstruction from the candidate text, not from a prior record:
  - B1-A, by testing whether adverse records keep their reach under the new run unit, as the handoff asked;
  - B1-B, by tracing where a task identity enters `L_n`.

  A different-family review of the B1 repair would reduce the shared-framing risk.

## 13. D4 statement

No SSDS 8 D4 is authorized. This Review accepts no architecture, product scope or proposed default. G1 remains open: it needs a repaired Manual candidate, an independent D3 Review with no surviving blocker, and explicit stakeholder acceptance. Shadow implementation additionally needs G2.

# Independent D3 Review — SSDS 8 Architecture Manual, candidate edabd81

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          edabd813838ee7703f6eb6d29496e5704517eba0
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        77f7ca8d2b454b55973723308fa995bc06543338 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   04504e86d82861826f9ee60ef1177316f71b8896 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 653e88c
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of the item-31
                        repairs in both directions; the handoff's six drift classes applied to every
                        place that states the dependence mode, the revalidation route and the
                        content-versus-identity reach; consumer-to-premise and staleness-to-route
                        traces; family-level recheck of earlier families; diagnostic model run in full
                        (parallel, all families and mutations); structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-edabd81/snap`. The later commit adding the handoff (`b767d5c3`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. The accepted SSDP owners, the reviewed workplan, and the stakeholder's SD-20/SD-22 and SD-35 directions can be realized together. Both blockers below are defects in how the proposed Manual states its own item-31 repairs: one repair is missing from the Admission owner, and one new clause removes a route the rest of the Manual relies on. No accepted authority is shown false, contradictory or unrealizable.

## Verdict

**NO-PASS.** Two blockers, both of the class the author named for item 31 ("two places computing one thing drift apart"):

- **B1**, D1-D3 change-rule / revising-duty family. The `standing` repair of 653e88c B1 is stated in §4.1, §4.3, §10.2, §16.6 and §29.4 but not in Admission. §8.3 step 7 still requires a `record` entry on the revision-assessment record, so 653e88c B1 stays open at the real Admission owner.
- **B2**, revalidation-routing / liveness family, gate and acceptance consumers. It enters through this round's new clause "`REVALIDATE` at the root of the staleness". A passing judgment whose premise is replaced rather than restored keeps an answered obligation and gets no revalidation. Gates and acceptances are then stranded for the rest of the run or revision. Three places state three different rules for this (§5.5, §10.2, §31.6 (Z)).

The other item-31 repairs hold for the trajectories that motivated them: `standing` itself, 653e88c N1's required-evidence premises, review evidence by currency, and the content-keyed acceptance and gate reach. The cases where they do not are B1, B2 and the non-blocking findings below. The diagnostic model is green on all five families and catches all 34 mutations. It cannot see B1 or B2 (§11 below).

## Blockers

### B1 — Admission still requires a `record` entry on the revision-assessment record, so the 653e88c B1 strand is unrepaired at the Admission owner

**Family:** D1-D3 change rule / revising duty (revision-assessment record, revision run). It is the 653e88c B1 mechanism itself, left in one of its owners. **Earliest owner:** proposed D3, Manual §8.3 step 7. **Status:** open, material. It is a clean local defect, a missed restatement inside a repair that is otherwise right.

**Exact rules at the candidate.**

- §4.1 line 545 defines `standing` for "the revision-assessment record an acceptance or gate decision relies on (§10.2)". Line 548: "where a readiness or admission condition reads a record's standing, the answering judgment's entry on that record is `standing`".
- §4.3 line 568 (`ACCEPTANCE`): "for a `NATIVE` D1/D2 subject, `standing` on the revision-assessment record it relies on". Line 578 (`GATE_DECISION`): "`standing` on the revision-assessment record section 3 rendered".
- §10.2 line 1285: "The accepting judgment carries a `standing` basis entry on that record (§4.1, §4.3) … An in-run re-acceptance after a governing change therefore reuses the record."
- **§8.3 step 7 line 1188**: "Admission refuses a passing `ACCEPTANCE` … and a `GATE_DECISION ACCEPT` on a `NATIVE` D1/D2 triple … unless a revision-assessment record for `(s, r)` already admitted counts for it (§10.2: in the run, and standing) **and the judgment carries a `record` entry on it** (`OBLIGATION_REVIEW_OPEN`)."
- §8.3 step 6 line 1187: "every basis entry of every submitted support-tier record … is satisfied … Otherwise the record is classified stale and routed to revalidation, not admitted"; §5.5: `sat(record x) = current(x)`.

**Trajectory.** This is exactly 653e88c B1's trajectory. `NATIVE` D1 `a`; `NATIVE` D2 `b` governed by it; `b`'s `AUTHOR` result `R` reads `a` and counts. Accept and gate `b`, then accept a real change `a1 -> a2`. `R` is no longer current (its `content`/`validity` on `a1` fail), but it still counts. A reviewer submits `ACCEPTANCE PASS` on unchanged `b`:

- with the §4.3 `standing` entry only: step 7 refuses it (`OBLIGATION_REVIEW_OPEN`), because it carries no `record` entry;
- with a `record` entry (alone or beside `standing`, which declared reliance allows): step 6 evaluates `current(R) = F` and refuses it as stale.

The gate is refused the same way. `REVIEW(b, r_b)` is not derived, because `R` counts. Siblings (a)-(e) of 653e88c B1 (item amendment, incidental read, revising-review result, gate, cutover) follow unchanged. With B2's root clause, the stale judgment's route now leads to `COORDINATE(plan)` for the stale task result. That re-plan can restore validity only by re-authoring `b` into a new run, against §10.2's "reuses its record".

**Violated owner text.** The reviewed early cutoff (workplan, restated at Manual §5.5): "If a re-review of `b` against the new `a` passes without changing `b`, `b` is valid again." The workflow owner (`aaeaf8b:source/shared/references/workflow-and-workplans.md`, "Authority lifecycle, mutation, and impact closure"): "acceptance -> bounded dependent impact -> reconcretization/revalidation". The architecture owner's "D3 formal-contract discipline": "define it before dependent invariants use it: … lifecycle states and transitions". And the Manual's own §10.2 and §31.6 (Z) ("an in-run re-acceptance and gate of unchanged `b` are admitted with the old revision-assessment record"). An Admission implementer must choose between §8.3 step 7 and §4.1/§4.3/§10.2. Workplan §21 items 4, 5 and 7, and the gate side of 10 and 26, stay partly open.

**Minimum repair direction (subtractive).** In §8.3 step 7, replace "carries a `record` entry on it" with "carries the `standing` entry §4.3 requires". Check that no other owner names the mode. A grep at this candidate finds no other one; §29.4 line 2539 and §16.6 agree.

**Required discriminator.** Run §31.6 (Z) through the real Admission step-6/step-7 owner, not only through derivation: the in-run re-acceptance and gate of unchanged `b`, carrying `standing`, must be admitted. A judgment that carries an additional declared `record` entry on the stale record must be refused at step 6. The diagnostic cannot do this: its gate family transcribes §4.3's mode assignment (`gate_basis`) and has no Admission step 7.

### B2 — "`REVALIDATE` at the root" removes the only route by which a stale gate decision or acceptance is replaced, while §5.5 and §31.6 still rely on it

**Family:** revalidation routing and liveness (a derived obligation or route must exist for every non-current judgment that something depends on). Consumers: the gate term (`gterm`, R11) and subject acceptance (`ACC`, `valid`). **Earliest owner:** proposed D3, §10.2 `REVALIDATE` trigger (line 1260) together with §4.1's route list (line 548). **Status:** open, material. It is non-local: it entered through this round's repair and crosses §4.1, §4.6, §5.5, §10.2, §10.3 and §31.6.

**Exact rules at the candidate.**

- §10.2 line 1260, `REVALIDATE(x)` trigger: "… **never for a judgment non-current only through a `record` entry on a record that is itself non-current**: the revalidation goes to the root of the staleness, or that record's own route applies (a rerun, a re-plan of a stale task result, §4.1)". Holder for a `GATE_DECISION`: "its author or the owner … (only they may supersede it, §5.10 (d))".
- §4.1 line 548, the routes when a `record` entry fails: "a completeness judgment that stops being current widens the closure (§4.6) and the next judgment takes the wider basis; a stale realization or assessment derives `REALIZE`, `RERUN` or `READING` (§6.9); a stale task result goes to `COORDINATE(plan)`; a non-current judgment derives `REVALIDATE` at the root of its staleness".
- §10.3 line 1299, answered obligations: an `ACCEPT` or `GATE` obligation "is answered … by the first judgment acting there of its kind on its target"; "An answered obligation is never ready again, so it is never dispatched again … A passing answer that later stops being current derives `REVALIDATE`, a separate obligation." The obligation's identity is rule, target and parameters (§10.2 line 1246), so an unchanged triple and run give the same obligation.
- §5.5 line 756 (gate term): "A non-current decision among them lowers the term **and derives `REVALIDATE` for it** in the state where it is eligible; nothing earlier remains to fall back on." `gterm(g)` is the minimum over every eligible unsuperseded passing decision. "Any qualified holder may record a passing decision … on an answered gate; each eligible one enters the minimum." Only the decision's author or the owner may supersede it (§8.3 step 3).
- §31.6 (Z), line 2689: "a judgment stale only through a stale record derives no `REVALIDATE` of its own **while its root's route is derived**". §32.2 line 2763 measures "the `REVALIDATE` work" stale gate members generate.
- `record` entries name one record, and "a superseded decision never becomes current again" (§5.5). A premise that is replaced (re-realized, re-assessed, superseded, revoked) therefore never makes the depender current again. Only a premise that is restored (an `EQUIVALENCE` covering its entry, a dismissed challenge) does.

**Decisive trajectory — a gate whose required assessment is replaced.** It holds for any subject kind; no D1/D2 condition is needed.

1. Subject `s` has required evidence obligation `e` and a required human gate `g`. Realization `R1` (execution basis includes test file `t` at `t1`) and passing assessment `A1` (`record R1`) are current. The core's required-evidence section marks `A1`. Holder `H` records `h = GATE_DECISION ACCEPT UNQUALIFIED` with `record A1` (§4.3 line 578). `gterm(g) = T` and `s` is valid. `GATE(g)` is answered by `h`.
2. An admitted change to `t` (outside `s`, not `s`'s authority) makes `R1` non-current (execution entry), so `A1` is non-current (`record R1`) and `h` is non-current only through `record A1`.
3. `REALIZE(spec, claim)` is derived (`e` has no current admissible realization). It yields `R2`; `ASSESS` yields a passing current `A2`. `ev(s, e) = T` again.
4. `gterm(g) = current(h) = F`: `h` is eligible and unsuperseded, and `A1` is non-current forever.
5. Routes. `GATE(g)` is answered by `h` and is never ready again. `REVALIDATE(h)` is never derived, because `h` is non-current only through a `record` entry on the non-current `A1` (§10.2). The root's route (`REALIZE`) was derived and has completed, and `A1` stays non-current permanently. A second holder's `ACCEPT h2` enters the minimum beside `h`, so `gterm` stays `F`. Only `H` or the owner can supersede `h`, and no obligation dispatches either of them.
6. `s` is invalid for the rest of the run, or forever for a subject outside the run regime until its bytes change. Every descendant whose support passes through `s` is `F`.

**Strongest sibling — no root route is derived at all.** In step 1, let two passing assessments `A1`, `A2` of `e` be current, so `h` carries `record A1` and `record A2` (§4.3: "several passing assessments of one obligation are each a premise, a conjunction stated as intended"; this is the 653e88c N1(ii) repair). Only `R1` goes stale. `ev(s, e)` stays `T` through `A2`, so no `REALIZE`, `RERUN` or `READING` is derived. `REVALIDATE(h)` is refused by the root clause. `h` is non-current with no derived route anywhere, and `gterm(g) = F`. Before this candidate, `REVALIDATE(h)` was derived and its answer (`record A2` only) was admissible.

**Further siblings (same cause, checked against the written rules).**

| Sibling | Trigger | Result |
|---|---|---|
| (a) acceptance via completeness | an `ACCEPTANCE j` has `record C` on the completeness judgment its closure used (§4.3 line 568). `C` stops being current while `j`'s own entries hold: `C` superseded by its author's reassessment or by the owner; `C` revoked by an upheld challenge, or vetoed and resolved against it; for a machinery declaration, a human-gated analyzer-set change that drops `C`'s analyzer identity (`tgt`, §5.2), whatever the output (in tension with §5.9's early-cutoff statement for analyzer changes) | `ACCEPT(s)` is answered by `j` and never ready again. `REVALIDATE(j)` is refused by the root clause. The §4.1 route, "the next judgment takes the wider basis", has no next judgment to dispatch. `valid(s) = F` for the rest of the tenure, or the run for `NATIVE` D1/D2. After an analyzer upgrade, every subject bounded by that machinery declaration is affected at once |
| (b) review via a check execution | a `REVIEW` of `X` has `record` on a current `CHECK_EXECUTION` (§4.3 line 569). A concurrent admission changes a file that the check read and the task did not, so the check is non-current in `D_n[X]`; the check is re-run | the review stays non-current through the old check. `REVIEW(X)` is answered and not ready. `REVALIDATE(review)` is refused. `X` cannot integrate in its enactment |
| (c) gate trigger | the `GATE(g)` trigger "a required human gate without a current `ACCEPT`" (§10.2) and "answered" do not read `gterm`'s minimum | with a stale `h` and a current `h2` the trigger is false while `gterm = F`. Before this round only `REVALIDATE(h)` covered this; now nothing does |
| control: premise restored | an `EQUIVALENCE` covering `R1`'s changed unit for `CONSUMER:REALIZATION`, or a dismissed blocking challenge against `A1` | `A1` and `h` are current again with no work. **Holds.** |
| control: stale task result | a review stale only through its task result (§4.1, §10.2 `COORDINATE(plan)`) | a route is derived (re-planning). **Holds** as a route, though §11.5 step 3 still says "review is re-requested" (N4) |

Shared cause: **the root clause assumes that repairing the root makes its dependers current again. That holds for a restored root but never for a replaced one, because a `record` entry names one record and a replaced record never returns.** The clause was meant to stop futile revalidations, where every answer is refused because the stale premise is still required. §10.3's new "no stranded obligation" rule already covers that case: show the obligation waiting and derive the premise's route. Discovery stops here; further variants re-derive the same composition.

**Violated owner text.** Workplan K1 (line 814): "A result is admitted only if everything it relied on is still current, or it is revalidated." Workplan concurrency (line 1759): "affected judgments re-requested". Workflow owner: "acceptance -> bounded dependent impact -> reconcretization/revalidation". Evidence owner (`aaeaf8b:…/evidence-evolution-and-dependencies.md`, "Durable evidence binding and binding health"): "withdraw unsupported positive guidance, and rerun/remap where required". Here no route remaps the gate onto `A2`. The Manual's own §10.3 invariant ("the route that restores it is derived instead") and §5.5 ("derives `REVALIDATE` for it") are also contradicted. An implementer must choose among §5.5 (always derive), §10.2 (never) and §31.6 (Z) (not *while* the root's route is derived). Under §10.2, the most specific statement, the trajectories above strand. Workplan §21 items 5 and 7 and the gate template (item 10) are partly open.

**Minimum repair direction (subtractive).** Delete the root clause from the `REVALIDATE` trigger. Rely on §10.3's rule instead: `REVALIDATE(x)` is derived for every acting, non-current judgment a current obligation depends on, and is **not ready** while every answer's mechanical minimum still needs the failing premise. During that time it is shown waiting on that premise, with the premise's §4.1 route derived. It becomes ready once a replacement premise exists (for the gate, `record A2`; for the acceptance, the widened closure). This is §31.6 (Z)'s "while" reading, and it removes mechanism. State the same in §4.1's route list, and make §5.5 line 756 point to it. Optionally have the `GATE(g)` trigger read `gterm < T` rather than "without a current `ACCEPT`" (sibling (c)); that is a one-predicate change, not new mechanism.

**Required discriminator.** At the real owners (Derivation `current`/`gterm` -> obligation derivation and readiness -> Dispatcher -> Admission):

- the gate trajectory above with one assessment: `REVALIDATE(h)` waits while `REALIZE`/`ASSESS` run, then becomes ready for `H` or the owner; its superseding `ACCEPT` with `record A2` is admitted and `gterm = T`;
- the two-assessment sibling: `REVALIDATE(h)` is ready at once;
- sibling (a) with each trigger (supersession, revocation, analyzer-set change): a re-acceptance with the wider or new closure is dispatched and admitted;
- sibling (b) in a frame;
- across every obligation kind, no acting non-current judgment that a current obligation depends on has neither a ready or waiting `REVALIDATE` nor a derived premise route.

Negative controls: a restored premise derives no `REVALIDATE` (the judgment is current again); a vetoed judgment still derives `ADJUDICATE_DISAGREEMENT` instead. The diagnostic cannot discriminate any of this. Its I10 checks only that a fresh decision `h2` is admissible and current. It does not check that `h2` raises `gterm` (it cannot without superseding `h`), and it models no obligation, "answered" state or `REVALIDATE` derivation.

## Non-blocking findings

### N1 — `standing` is said to read "exactly what counts reads"; the two lists differ

§4.1 defines `standing` as `base(x)`: acts, not superseded, `status1`, `cont`, `tgt`, not vetoed, not `nonind`. "Counts" (§10.2) is: in the run (acts and names `rid`), `status1`, `cont`. They agree for a `TASK_RESULT` in practice, since task results are never superseded, have no adverse kind and carry no independence requirement, and an out-of-run acceptance fails its own `tgt`. The "exactly" claim at line 1285 should say so, or `standing` should be defined as "counts". The gate row's "the revision-assessment record section 3 rendered" can be several records (§16.6 section 3: "every revision-assessment record that counts"). `standing` on each is a conjunction where readiness reads `∃`. It is liftable by `REVALIDATE` (not through a `record` entry, so not affected by B2), but it should be stated. The model's comment on `gate_basis` cites "SD-36", which does not exist; item 31 changes are author choices (closure map §5). Editorial.

### N2 — The content-keyed acceptance and gate reach: an ambiguous key, an incomplete cost disclosure, and tension with S10

§5.10 (a) and (b) (lines 821, 835, 842) extend `ACCEPTANCE` and `GATE_DECISION` reach to "every triple of any subject whose revision has the same content (every unit's bytes and semantic declarations, §1.5)". This is an author choice under item 31.

- **Key.** `rev` (§1.5) hashes `term_args`, which include paths, and `sem`, whose declarations name unit identities (SDG members, joint invariants, relation objects). Read as `rev` equality, copies at other paths are never reached, and a re-identification that renames self-referenced units escapes. Read as "bytes and declarations" without paths, distinct subjects at different paths with equal bytes are reached. The parenthetical supports both readings. State which one.
- **Cost.** Where two distinct subjects share the key, a correct `FAIL` on `s1` and a `PASS` on `s2` can never coexist. `ACCEPTANCE` and `GATE_DECISION` have no per-target relief. The only lifts (reassessment, owner adjudication, upheld challenge) withdraw the objection for `s1` too. A fresh `FAIL` superseding it reaches `s2` again. §32.2 line 2747 says such subjects "share … reach until its author or the owner ends it", but not that ending it ends it for both. In S10's words, "Content identity, scope identity, subject role and tenure … and acceptance are distinct facts", and §1.10 says acceptance never implies "anything about another subject". The reach narrows that for objections without saying so in §0.3 R9, which still says "on the same target".
- **Owner.** §5.10 (a) names the owner for reaches that "cross items or plans". A subject-crossing reach (possibly across domains) has no named owner.

**Stakeholder options:** keep the content key and disclose the coexistence cost; key subject-crossing reach on `renamed_from` lineage only (narrower); or add per-target relief for `ACCEPTANCE`/`GATE_DECISION` (**adds mechanism**).

### N3 — The history carry for relation-targeted kinds is narrower than §5.10 (a) says and has no mechanical trigger

§5.10 (a) says a re-identified named unit's standing objection is "carried as history into the next judge's brief (§16.5)". §16.5 line 1768 carries it only into "every review or acceptance brief". The next judge of an `INTAKE_DISPOSITION` (intake disposition step), of a `PRODUCT_SCOPE_ACCEPTANCE` (a human gate holder's brief) or of a stand-alone `EQUIVALENCE`/`COMPLETENESS` is not named. "A re-identification left outside their reach" is not defined mechanically. Lineage (`renamed_from`) can detect one; a remove-and-redeclare without lineage cannot. §32.2 should say so. Disclosure only; the veto is not weakened.

### N4 — Three statements of what happens to stale reviews and task results disagree with the new routes

- §11.5 step 3: after a clean rebase "review is re-requested only where the review's basis no longer holds". Under §4.1/§10.2, a review stale through its task result goes to `COORDINATE(plan)`, and a re-requested review would be refused at step 6.
- §12.3: the Implementer holds "`REVALIDATE` of its own result", against §4.1's "a stale task result goes to `COORDINATE(plan)`".
- §12.3: the Reviewer template does not list `REVALIDATE` among the obligation kinds it holds, although §10.2 gives `REVALIDATE` of an acceptance or review to "the role of `x`'s kind".

Also, §4.3's review row (line 569) cites §16.5 for the runs "the brief shows as the candidate's evidence", but §16.5 marks no such section (unlike §16.6's new required-evidence section). An implementer can infer "current at rendering", which suffices. Editorial, but repair it with B2.

### N5 — The "no stranded obligation" invariant covers dispatch only, and one case it names has no derived route

§10.3 constrains which obligations are *dispatched*. It does not require every non-current depended-on judgment to have a route (B2 is outside its text). The plan row (§5.10 (b), line 839) says an `ADJUDICATE_DISAGREEMENT` whose every owner answer is inadmissible is "shown waiting, not dispatched (§10.3)". Its only lift is an upheld challenge, and no rule derives one, so §10.3's "the route that restores it is derived instead" is false for it. The veto "blocks no work", so the harm is a permanent waiting entry. State the exception, or phrase the invariant as "ready obligations have an admissible answer; every non-current depended-on judgment has a ready or waiting route".

### N6 — The diagnostic was extended in ways that cannot see this round's risks

- The revision-assessment record's new basis (`rd`) is irrelevant under `standing` by construction.
- I10 tests admissibility of a fresh, non-superseding decision, not answerability of the gate. Under `gterm`'s minimum and the answered rule, it is the wrong liveness property (B2).
- The `acceptance_reach_same_subject` mutation and oracle encode content equality on abstract labels. They cannot test N2's key or cost.
- The model transcribes §4.3, not §8.3 step 7 (B1).

This is consistent with §5.10 (g)'s disclaimer and PEM DS-001. §31.6 (Z) is the right real-owner discriminator once it gains B1's Admission case and B2's cases.

### N7 — Noticed, not established: Admission step 8 versus post-integration review currency (carried from 653e88c)

Step 8 refuses any request that makes a discharged obligation undischarged, except an accepted change to a prerequisite authority. Discharge is not latched (§10.4). A transformation review keeps `record` on its task result and output-role `content`, both of which have "ordinary currency in the admitted state" after integration (§7.3). Read together, a later admitted change to code an earlier item implemented, or to a file its task read, might be refused as collateral regression. This is reviewed-workplan text (workplan line 1428), not this round's delta. I could not settle in budget whether "affected by the merged tree" and item issuability bound it. I make no finding; the author should check it with B2, since it is the same "what a `record` entry imports after integration" question.

## Closure audit

The closure map was used to navigate. I checked its claims against the workplan §21 items the delta and the blockers touch, and against the Manual sections they name. Other items were taken as dispositioned in the 653e88c record, unless a mechanism below reopens them. Subordinate clauses were spot-checked: the gate basis, the review basis, revision run identity, the revalidation trigger, discharge, readiness and answering.

| Item | Disposition at this candidate |
|---|---|
| 4 (basis composition and mode assignment per kind) | **partly closed (B1)**: §4.3's mode and §8.3 step 7's required mode disagree for the revision-assessment record; the gate's required premises are now defined by the core (653e88c N1, closed) |
| 5 (derivation) | **partly closed (B1, B2)**: in-run D1/D2 re-acceptance is contradictory at Admission; a stale gate member pins `gterm` with no route |
| 7 (obligation rules, readiness, discharge) | **partly closed (B2)**: `REVALIDATE` is withheld where it is the only route; three statements of it disagree |
| 10, 26 (gate template; decision/inspector templates) | gate consumer inherits B1 and B2 |
| 1-3, 6, 8, 9, 11-25, 27 | no unresolved architectural decision found in this bounded audit; unchanged by the delta |

§16.2 rows: unchanged by the delta; §26.4 keeps an explicit replacement, retirement or preserved boundary for every row. None found unresolved.

## Refinements R1-R14

| # | Assessment |
|---|---|
| R1 | Sound as stated; unchanged by the delta (Phase B N2 re-tested in text, below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4-R7 | Sound; unchanged and not re-derived beyond the text |
| R8, R9 | Sound locally. R9's "on the same target" wording now understates §5.10's content-keyed acceptance and gate reach (N2) |
| R10 | **Unsound in part (B1)**: within-run reuse of the revision-assessment record is stated in §10.2 but refused by §8.3 step 7 |
| R11 | **Unsound in part (B2)**: the minimum is sound only if every stale eligible member can be superseded, and the root clause removes the obligation that dispatches its superseders |
| R12, R13 | Sound; unchanged |
| R14 | Sound as the selected conservative reach policy. Its new identity sentence is coherent for the plan, review and relation kinds; the acceptance and gate extension is N2 |

The item-31 changes (`standing`, the route list, the root clause, the no-stranding invariant, the content-versus-identity statement) are D3 decisions inside §21 items 4, 5 and 7. They are listed in R14's text and in closure map §5 as author choices. The root clause also changes reviewed workplan K1 ("or it is revalidated") for the judgments it covers without a §0.3 row; B2's repair removes the need for one.

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design/disclosure closure with real-owner execution owed later; **R** retained, disclosed decision or stakeholder option; **P** partly closed. The delta since 653e88c touches §0.3 (R14 text, SD range), §4.1, §4.3 (acceptance, review and gate rows), §5.5 (`sat(standing)`), the §5.10 heading, (a) and (b), §10.2 (`REVALIDATE`, admission and readiness), §10.3 (invariant), §16.5, §16.6, §31.3, §31.6 and §32.2. I re-derived the mechanisms below independently. Earlier records' per-item closures are treated as unchanged unless a mechanism below reopens them; earlier Reviews were not replayed item by item.

**Mechanisms independently checked at this candidate:**

- **Revising duty (653e88c B1).** §4.1, §4.3, §5.5, §10.2, §16.6 and §29.4 now read standing, which closes the derivation side for siblings (a)-(e) and reuses the record in-run. Admission does not (B1). **P.**
- **Gate basis (SD-35; d94a293 B1; 653e88c N1).** Displayed challenges, reports, adverse and historical records, and stale or replaced records of a required obligation are `identity`. The required premises are the required-evidence section's assessments. **C** for display/support. The conjunction rule composes with B2 into a route-less strand (B2's strongest sibling).
- **Judgment disagreement (§5.10).** One reach rule over S0/S1 `asserts`; the plan closed form (same prose and fixed fields, `cur` unread) over chains, incomparable branches, joins, reverts, loosenings, R2 amendments and multi-item rejections; review reach on changed-unit content under any item or plan; relief and supersession admissibility; `nonind` in `base`; adjudication root and class at Admission; the acting rule for every permissive route. These are unchanged except the acceptance/gate content key (N2) and the plan row's "shown waiting" (N5). The model is green with all mutations caught. **C/R** as in 653e88c.
- **Matching (§6.3-§6.6).** Phase B N2 re-tested in text: an alternate tree differing only outside a recorded narrow basis, for a differing old-content run under (2) and a yielding present-content run under (4), with a completeness judgment that becomes `P`, blocked, revoked or loss-withheld. Only (1)/(3) narrow (`link⁻` anchored on the failing run's record). **C.** Support cycles (§5.6) and corrupt prefixes (§5.7) still fail closed. **C.** B2 does not reach `stale`, which reads completeness currency positively only.
- **Gate minimum and revalidation (575dc78, f7419d5, both b46c250, f22b4dc, 362af9f).** Their closures assume a stale eligible member derives `REVALIDATE` for its author or owner (§5.5 line 756, §31.6 (A)/(D), §32.2 line 2763). That assumption is false under the root clause for staleness through a `record` premise (B2). **P.**
- **Content identity, gate qualification (`unq`), equal-region partition.** Unchanged. **C.**

| Prior record | Disposition at this candidate |
|---|---|
| 653E88C (same family) | B1 **P** (B1 here: Admission); siblings (a)-(e) **C** in derivation, **P** at Admission; N1 (i) **C**, (ii) **C** as stated but composes into B2, (iii) **C** ("every other" keeps a required qualifying record `record`); N2 **C** (§0.3 and the §5.10 heading cite SD-35; §31.3 states the gate family's invariants), except that (g)'s case list still names the gate-basis case while (g) states no I9/I10 (editorial); N3 **P** (N6 here); N4 **R** |
| D94A293 (different family) | B1 **C**; N1 **C** wording / **R** stakeholder option; N2 **R** (cross-plan amended copy, §32.2); N3 **P** (N6) |
| 913DB8F | B1 **C** (changed-unit content key; plan-subject carries); N1-N8 as recorded by d94a293 and 653e88c, unchanged by the delta |
| 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows: blockers **C** (closed-form plan reach, content-keyed review reach, union composition, orientation-free equivalence authors, one reach rule); N items **C/R/D** as d94a293 records; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: **C** |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting/enactment, run identity, gate minimum: blockers **C** for which records act and count; the gate-minimum liveness they rely on is **P** under B2 |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap, partition: **C**, with R items unchanged. A18B544's "only a completeness judgment bounds a closure" now carries B2 sibling (a) for acceptances |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set). 86ab683's restrictive check and 798b2b4's run closures are **P** until B1's Admission sentence is fixed |
| Phase B closures, N1-N4 | matching-family closures re-verified (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Upstream D1 change, then in-run re-acceptance and re-gate of unchanged `NATIVE` D2 `b` through Admission | **B1** |
| The same evaluated in derivation only (§4.3 `standing`) | held: reuses the record, `b` valid again |
| Revision-assessment record revoked, blocked, risk-overridden or loss-withheld | held: `base` falls, the acceptance is non-current or `P`, the record stops counting, `REVIEW(s, r)` is derived |
| Gate with required assessment replaced after a rerun | **B2** |
| Gate with two current assessments, one going stale | **B2** (no route at all) |
| Acceptance whose completeness premise is superseded, revoked, vetoed-and-lost, or loses its analyzer identity | **B2** sibling (a) |
| Review whose check execution goes stale in its frame | **B2** sibling (b) |
| Stale premise restored by equivalence or dismissal | held |
| Re-identified subject with byte-identical content (same paths): peer `PASS` after a `FAIL` | held: vetoed and carried (§16.5); owner adjudication withdraws it for both |
| Two distinct subjects sharing the content key, one correctly failing | N2 (no coexisting state) |
| Re-identification of a named unit under `NOT_EQUIVALENT` / `INCOMPLETE` | held as disclosed: not reached, carried as history (N3 for briefs) |
| Gate core showing challenges, reports, other enactments' `REJECT`, stale non-required evidence, stale history of a required obligation | held (SD-35, N1 repair) |
| Review shown an earlier stale run beside the current one | held: `identity` on the earlier one |
| Plan rejection for infeasibility cured by a loosening; owner answer inadmissible on both bases | held as policy; N5 for the waiting entry |
| Composition, chain and union reach; review re-identification with a one-byte heading edit | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds one basis mode (`standing`), one trigger exclusion (the root clause) and one stated invariant. It adds no primitive, component, record kind or persistent surface. `standing` is the minimum mechanism that realizes SD-20's "stands" (653e88c option 1), and it is justified. The root clause is unnecessary given §10.3's invariant, and it drops a capability an owner requires (revalidation of affected judgments, workplan K1 and the workflow owner), so B2's repair removes it. B1's repair is one word.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (empty `git diff --stat`), so the version-bound Core and frozen profiles are preserved (PEM PC-001). Capability transfer was not re-derived beyond the delta.

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`; the PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository's validator (`source/project_engineering_memory.py`, run in the clone) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE (a green diagnostic coexists with B1 and B2).
- **SP-001**: evidence-only (one owner per rule; both blockers are two owners of one rule disagreeing).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.6 (Z) is a good real-owner discriminator for 653e88c B1, but:

- it states the in-run re-acceptance as admitted, which a faithful §8.3 step 7 refuses (B1);
- its sentence "derives no `REVALIDATE` of its own while its root's route is derived" contradicts §10.2's "never" (B2), and it has no case in which the root is replaced;
- §31.6 (A) and (D) assert `REVALIDATE` for stale gate decisions without saying through which entry they went stale.

The diagnostic (N6) shares claim definitions and helpers and transcribes §4.3's modes. It models no Admission step 7, no obligation answering, no `REVALIDATE` and no `gterm` recovery, so green runs coexist with B1 and B2 (DS-001).

## Doctrine-realization map and O1

§29 maps all seven entrypoints. The revising-duty row (line 2539) claims E0 "for presence and order … counts (in the revision run, standing)". That agrees with §10.2 and disagrees with §8.3 step 7, so the E0 mechanism as Admission would build it blocks legitimate reconcretization (B1). The D4 row's "reconcile every obligation" (line 2507) relies on revalidation routes that B2 removes for gates and acceptances. No other map claim depends on the delta.

O1 (§0.5) is unchanged: the realized record, readers, routine questions, retention and marked surfaces (all within the requested deliverable; none beyond) are stated. The gate brief's new required-evidence section is a within-deliverable surface. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate:

- Blob identities above (`git rev-parse` at the candidate); the model file's hash `5122ede7e83094081c9211d6d793b8e394d849e5` re-checked equal to the snapshot.
- `git diff --check 653e88c10f469c1da4b89b55cd09b4c5ff595b37 edabd813838ee7703f6eb6d29496e5704517eba0`: exit 0. The delta is 7 files (Manual 40 lines changed, closure map 7, model 58, stakeholder record, continuation handoff, previous handoff and Review record).
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… edabd813… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate: `--mutations` workload run in parallel by importing the unmodified module with `python3 -I` from a scratch driver under `$TMPDIR/ssds80-manual-review-edabd81/scripts/`. Each job ran in a fresh spawned process: `run_family` for each of the five families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`) with `MUT` cleared, then, for each of the 34 entries of `MUTATIONS`, `MUT = {m}` and `run_family` on each family that mutation names. That is 41 jobs on 28 workers; the job set was audited against the module's own lists (41/41, no omission or duplicate).
  - Base results, all with zero invariant failures: transformation-review/acceptance/gate 1,856,368 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 1,000.
  - All 34 mutations are caught. New ones: `revision_assessment_record_mode` (I1/I3, I10), `acceptance_reach_same_subject` (I1/I3). `plan_supersession_current_only` is caught by I4 only; `eq_authors_to_side_only` by I1/I3, I7 and I8.
  - Sum of per-job times: 10,967 s. I did not call `main()` itself; the driver calls the same functions in the same configuration.
- Governing owners read at `aaeaf8b`: `source/roles/software-design/SKILL.md`; `architecture-and-design.md` ("D3 formal-contract discipline"); `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure"); `evidence-evolution-and-dependencies.md` ("Durable evidence binding and binding health"); `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence"); `project-engineering-memory.md` (activation, HAS); `testing-and-validation.md` (proxy-proof, through PEM DS-001).
- Manual sections read in full: §0, §1.1-§1.11, §3.4, §4, §5, §7, §8, §10, §11.2-§11.5, §12.3, §13.6, §16.5-§16.8, §31.6, §32.2. Others were read by targeted search for the drift classes.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- The doctrine map was checked only for rows touching the delta and the blockers.
- Earlier Reviews' per-item closures were not replayed (stated above).
- N7 was not established.
- The six drift classes were applied by targeted search across the whole Manual, not by a line-by-line pairwise comparison of every concept. Further drift outside the searched concepts is possible.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations. Material findings: B1, B2 and N1-N7; none concerns a scientific observable, numerical method or realized scientific result.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, two submission variants (with and without a declared `record` entry) plus 653e88c's five siblings. For B2, two primary trajectories, three siblings and two controls. Seventeen out-of-matrix trajectory classes (overlapping, not independent trials). One diagnostic configuration with 5 base families and 34 mutations. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. It shares the corpus, the inherited workplan and handoff framing (including the handoff's six-class diagnosis, which directed the search), the prior Review records (read as hypotheses), the Git/Python toolchain and the diagnostic's claim definitions and helpers.

B1 was found by checking every owner that names the revision-assessment mode. B2 was found by asking, for each `record` premise, whether its §4.1 route makes the depender current again. Neither lies in the diagnostic's model. Shared-family blind spots remain possible; a different-family confirmation of the repairs is advisable.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Repair B1 (the one-word Admission restatement).
2. Repair B2: delete the root clause in favour of §10.3's waiting rule, and reconcile §4.1, §5.5, §10.2, §11.5, §12.3 and §31.6.
3. Consider N1-N7; N2's options are the stakeholder's.
4. Extend §31.6 (Z) to B1's Admission case and B2's replaced-root cases.
5. Freeze a replacement candidate and obtain an independent Review before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.

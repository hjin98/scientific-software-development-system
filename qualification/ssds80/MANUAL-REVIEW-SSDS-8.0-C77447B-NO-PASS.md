# Independent D3 Review — SSDS 8 Architecture Manual, candidate c77447b

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          c77447bcac18a626ff4668b72f463fc3e17e89d2
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        5b718a33ba7b04fb626dd5e9e9f8d96e77274287 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   e75aeaf7b39c7be27c134c5b4700d0f750423371 (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 095ce55
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of the restated
                        R15 (latch event, latched value, class, identity) in both directions, by evaluating
                        the written rule state by state across the publication reconciliation (§22.2,
                        §8.3 step 9), later content changes (own items, other items, absorptions),
                        revision runs, gates, evidence reruns, plan re-acceptance, fences, loss and
                        rollback; the handoff's drift classes applied to every statement of the latch
                        (R15 row, §10.4, §8.3 step 8, §22.2, §5.8, §31.4, §32.3, closure map); family-level
                        recheck of earlier families; diagnostic model run in full (parallel, every family
                        and mutation); structural checks of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-c77447b/snap`. The later commit adding the handoff (`408f39de`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. The accepted SSDP 7.2.1 owners, the reviewed workplan and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below is in R15, a refinement the author made under record item 31 and lists for the stakeholder (closure map §5). It is routed against the proposed D3 owner. Its repair options go to the stakeholder because R15 is stakeholder-visible and this is a non-local recurrence.

## Verdict

**NO-PASS.** One blocker, the fourth consecutive round in the obligation-lifecycle family (edabd81 N7, 82d618c B1, 095ce55 B1). It entered through the previous Review's recommended repair, which this candidate realizes nearly verbatim:

- **B1**, the latched value is not content-independent. R15 states a property: once latched, "a content change never does" lower an enacted obligation. It realizes that property with a formula: the ordinary discharge predicate, evaluated at a latch state after publication is reconciled, with `standing` substituted for some terms. Three parts of that formula still read current state. (a) Publication is reconciled only by the next entry, whose tree already holds that entry's change. (b) `standing` includes `tgt`, which for D1/D2 gate decisions and acceptances reads the current revision run. (c) The predicate's other terms (current-revision `status1`, `gterm` over the current gate obligation, `qual` and `undisputed` in the current state) also read the current state. Each part lets a later content change reopen an integrated item and re-dispatch its implementer against later code. That is the 82d618c B1 trajectory R15 exists to remove, and it contradicts §31.4's own R15 controls. A further sibling (d): the item-obligation key, "its accepted revision", is not single-valued.

The 095ce55 B1 siblings it targeted are closed in text: fenced and `OVERTAKEN` integrations, post-latch revocation, veto, risk override, loss and rollback, and the class instead of a list. Its N1, N3, N4, N5 and N6 are closed in text, and N2 is closed in the Manual. The diagnostic model is green on all five families and catches all 34 mutations. It models no obligation, latch, publication or integration, so it cannot see B1.

## Blockers

### B1 — R15's latched value re-reads current state; later content changes reopen integrated items

**Family:** obligation lifecycle after integration (82d618c B1, 095ce55 B1), now through the 095ce55 option-1 repair. **Earliest owner:** Manual §10.4 "Enacted obligations latch at publication, and are then read by standing" (line 1319), with the R15 row (line 100). Together they decide workplan §21 item 7 (obligation rules and discharge) and support item 6 (Admission step 8's "enacted obligations stay discharged", line 1190). **Status:** open, material, non-local: §4.1, §5.2 `tgt`, §5.5 `gterm`, §10.2, §10.4, §13.7, §22.2, §8.3 steps 8-9 and §31.4 each contribute.

**Exact rules at the candidate.**

- §10.4 (line 1319) latches an enacted obligation "in the first admitted state, at or after its enactment's integration is `PUBLISHED` (§22.3 …), in which its predicate holds with every discharging judgment acting there". The R15 row (line 100) says "the first admitted state **after** its enactment's integration is `PUBLISHED`". The closure map (line 87) says "the first admitted state after `PUBLISHED` integration".
- §22.2 (line 2107ff): "Publication of `n` is reconciled by the first later entry carrying `obs`", which may be "any entry, including the next admission". §8.3 step 9 (line 1191): the appended entry "also reconciles the previous admission's publication if that was pending". §22.4: Admission "appends `n+1` only after `n` is admitted". So `pub(k)` is `PENDING` in `D_k` and first `PUBLISHED` in `D_{k+1}`, whose tree is `C_{k+1}`.
- §10.4: "Once latched, the predicate is read with each discharging judgment, gate decision and passing evidence record by `standing` (§4.1), and every adverse record as always: a revocation, a veto, an owner's supersession, `nonind`, a loss boundary …, a failing assessment that counts against one of its evidence obligations, or a rollback … lowers it …; a content change never does". Also: "An absorbed foreign change re-dispatches no implementer".
- §4.1 (line 547) and §5.5 (line 734): `standing` is `base(x)`, which includes "`cont` and `tgt` hold". §5.2 (line 657) `tgt`: "for a passing `ACCEPTANCE` or `GATE_DECISION ACCEPT` on a `NATIVE` subject of kind D1 or D2, the judgment names the subject's current revision run in `G`".
- §5.5 (lines 751-752): `gterm(g) = ⋀_{h ∈ elig(g)} …, and F when elig(g) is empty`. `elig(g)` is the passing decisions "on the gate obligation `G` derives for `g` (its subject triple and, for a NATIVE D1/D2 subject, its run)".
- §10.4 predicate (lines 1305-1313) keeps "`status1` of `subject(o)`'s **current** revision", `ev(subject(o), e)` and `qual(subject(o))`. `subject(o)` is not defined for item obligations.
- §31.4 (line 2665), R15 controls: "two sequential accepted `IMPLEMENT` items editing one leaf unit both integrate, the first's obligations are not re-dispatched"; "a later `AUTHOR` revision of a D2 subject integrates with its own revision assessment, acceptance and gate"; "an absorbed foreign change … in both cases with no implementer re-dispatched".

**(a) Decisive trajectory: the latch state is after the reconciling entry.**

1. Items `I1` and `I2` (`IMPLEMENT`) edit disjoint lines of one leaf unit `s` and are reviewed concurrently. `I1`'s integration is admitted as entry `k`. Its discharge predicate holds in `D_k` (§7.6, line 1138). In `D_k`, `pub(k) = PENDING`.
2. The FIFO queue (§8.2) next admits `I2`'s integration, rebased cleanly onto `C_k`, as entry `k+1`, with `obs = C_k`. That entry reconciles `pub(k) = PUBLISHED` (step 9). Step 8 admits it: `I1`'s evidence still passes on the merged tree.
3. `D_{k+1}` is the first state in which `pub(k) = PUBLISHED`, so by the R15 row's "after", and by the plain S0 reading of §10.4's "at or after … is `PUBLISHED`", it is the latch candidate. Its tree has `cur(s) = r2`. `I1`'s review has an output-role `content` entry on `s@r1`, which after integration is "ordinary currency in the admitted state" (§7.3). So the review is not current, the predicate fails, and `IMPLEMENT(I1)` does not latch. It never will unless `s` returns to `r1` or an equivalence covers the change.
4. Before latching, an enacted obligation has only the ordinary predicate, so `IMPLEMENT(I1)` is `OPEN`. Its trigger, "an accepted, issuable item … with a contract", still holds, so it is ready and `I1`'s implementer is re-dispatched against `I2`'s code. Meanwhile `I2`'s step 8 relied on "enacted obligations stay discharged (§10.4)", which is false for `I1`.
5. The same happens when entry `k+1` is an absorption of a foreign push over `C_k` that touches `I1`'s outputs (§22.3 procedure, "anything else → append an absorption of `L`: `PUBLISHED` if `C_n` … is reachable"). An absorbed foreign change then re-dispatches `I1`'s implementer, contrary to §10.4 and §31.4.

Whether `I1` is re-dispatched depends on whether a records-only entry happened to come between the two integrations. That contradicts §8.2, "Any order is correct". A retroactive reading, latching in `D_k` once a later state shows `pub(k) = PUBLISHED`, avoids the trajectory. But the row, the closure map and the S0 definition of `pub` all point the other way. An implementer must choose, and one admissible choice reproduces 82d618c B1's decisive trajectory, which §31.4 lists as a passing control.

**(b) `standing` reads the current revision run.** Take `AUTHOR` item `I1` on a `NATIVE` D2 subject `b` (`r0 → r1`), with a required gate `g`. It integrates, publishes and latches. A later `AUTHOR` item `I2` revises `b` (`r1 → r2`) with its own revision assessment, acceptance and gate, the §31.4 control. Read the latch two ways:

- **"Discharging gate decision" means `I1`'s decision `h1`.** In `D_m` after `I2` integrates, `rid(b)` is `I2`'s enactment. So `tgt(h1) = F`, `base(h1) = F`, `standing` fails, and `AUTHOR(I1)` is lowered to `OPEN` and re-dispatched against `r2`. `I1`'s new candidate starts another run, which lowers `AUTHOR(I2)` the same way, so the two items reopen each other in turn until their budgets end in `COORDINATE`.
- **`gterm` is recomputed in the current state with `standing` for `current`.** Then `I2`'s decisions satisfy `elig(g)`. But a later foreign absorption of `b` starts a run with no gate decision, `elig(g)` is empty, `gterm = F`, and both `AUTHOR(I1)` and `AUTHOR(I2)` reopen. The same happens for any gated item on any subject, since a foreign change makes a new triple with no decision.

Either way a content change lowers a latched obligation, contrary to "a content change never does", to §31.4's `AUTHOR` and absorbed-change controls, and to R15's stated removal of "a second `AUTHOR` revision" (82d618c B1 (d)). The shared fact: `standing` was chosen as "the same mode as the revision-assessment dependence", but for a `TASK_RESULT` `tgt` is trivially `T`, while for a D1/D2 gate decision or acceptance it is a current-state run test.

**(c) The predicate's remaining terms are current-state.**

- **Evidence.** A foreign change breaks the evidence that `I1`'s acceptance criterion names. Evidence currency is current-state, so `REALIZE` is derived and the rerun fails. Its failing assessment "counts against one of its evidence obligations" (keyed on lineage, §10.2), so by §10.4's list it lowers the latched `IMPLEMENT(I1)`, which is then re-dispatched. §10.4's "An absorbed foreign change re-dispatches no implementer" and §31.4's "no implementer re-dispatched" are false for every foreign change that breaks evidence. The two statements cannot both be implemented.
- **`status1`.** The predicate still reads "`status1` of `subject(o)`'s current revision", so a blocking challenge against a later revision that a later item produced lowers an earlier item. And `subject(o)` is undefined for an item obligation.

**(d) Item-obligation identity is not single-valued.** §10.4 identifies an item obligation "by the item and its accepted revision so that a control tightening (R1) does not re-key it". §13.7 (line 1534) identifies parts "by the item revision". Trajectory: item `I` is accepted at `r` by `PA1`, integrated and latched. An R1 tightening gives `r'`, and `PA1` stays current through `PLAN_CONTROL`. The principal then adds item `K`, a topology change that "always need[s] whole-plan review" (§11.4), so `PA2` names every item at its current revision, `I@r'` included. `I` now has two accepted revisions. If "its accepted revision" is the latest, `IMPLEMENT(I, r')` is a new, undischarged identity, and integrated work is re-dispatched. This is the drift class "a mutable identity versus what was judged". §13.4 and the §5.10 plan row already define the R1-invariant content: same prose and fixed fields.

**Shared cause.** R15 states the latched value as a property ("content changes never reopen it, while revocation, veto, owner supersession, loss, a counted failing assessment and a rollback do") but computes it by re-evaluating the current-state predicate at a later state, with one mode substituted. Every term the substitution leaves untouched is a current-state read: the latch state's tree, `tgt`'s run test, `elig` over the current gate obligation, the current revision's `status1`, current-state `qual`, and the item key. This is the handoff's first drift class, "two places computing one thing": a row's claim versus its formula, re-entering at the obligation layer.

Discovery stops here. Further variants re-derive (a)-(c):

- `DOCUMENT` items gated on a D1/D2 subject;
- partition parts whose item-level review reads a later tree;
- `JOINT_INVARIANT` or `SPEC_REVIEW` answered in a frame when the reconciling entry is an in-scope change (this one is restrictive only: a fresh review is answerable).

**Controls that hold.**

- A fenced or `OVERTAKEN` integration leaves the item `OPEN`, and re-application claims it (step 7 is consistent).
- A post-latch upheld `NO_PASS`, an upheld challenge after a risk override, a loss boundary, and a rollback with re-cutover under the same `MIGRATE` item each lower the obligation. §5.10 (f)'s `REFUSED` agrees.
- The latch holds when the entry after the integration is records-only and no later change touches a D1/D2 run, a gated triple or evidence.
- `REVALIDATE_OVERTAKEN` is gone without residue: no reference remains.

**Violated owner text.**

- The Manual's own claims: §10.4 "a content change never does" and "An absorbed foreign change re-dispatches no implementer"; §8.3 step 8 "enacted obligations stay discharged"; §8.2 "Any order is correct"; §31.4's R15 controls. A conforming implementation must break one of them.
- Concurrency owner (`aaeaf8b:source/shared/references/concurrency-and-orchestration.md`, "Idempotency and publication"): "Prevent duplicate logical outputs from concurrent/retried attempts unless duplicates are intentional", and "Ensure a resumed stage can distinguish accepted work from partial/stale work". Re-dispatching integrated, published work against later code duplicates a logical output that has already been accepted.
- Architecture owner (`architecture-and-design.md`, "D3 formal-contract discipline"): "When an architectural concept carries normative meaning, define it before dependent invariants use it: … lifecycle states and transitions". The latched state's transition and its key (`subject(o)`, "accepted revision") are not defined so that the stated invariant holds.
- Unsurfaced semantic change: R15 presents the narrowing as "content changes never reopen it". As written it reopens on content changes in (a)-(d), so the row does not state what the rule does.

**Convergence assessment.** This is a non-local recurrence: the fourth consecutive round in this family, and the second to enter through the previous same-family Review's recommended option. Sibling (a) is in that option's own words ("latches in the first admitted state at or after its enactment's integration is `PUBLISHED` (S0 `pub`)"), and (b) is in its "read in the existing `standing` mode (`base`)". The convergence owner's active simplification trigger applies ("repeated patches around the same mechanism … patch-on-patch repair"). Another formula patch would add exceptions. The options below remove the re-evaluation instead. Options for the stakeholder (Phase C handoff §5):

1. **Recommended: make the latched value a record-level fact, not a re-evaluated predicate. Narrows; adds no record or mode.**
   - Latch in the integration's own post-admission state `D_k`, where §7.6 already evaluates the discharge predicate, and only while the current state has `pub(k) = PUBLISHED`. A records-only answer latches in its own admission's state.
   - Fix at the latch the set `L(o)` of records the predicate used: the discharging judgments, gate decisions and passing assessments.
   - Afterwards the latched value is the minimum, over `x ∈ L(o)`, of `x`'s run-free standing (`base` without `tgt`: acting, superseded, `status1`, `cont`, vetoed, `nonind`), and is lowered by a rollback of the cutover that enacted it. Nothing else of the predicate is read again: not the current revision's `status1`, the current gate obligation, current-state `ev`/`qual`, or the latch state's tree.
   - Key item obligations, and their parts, on the item plus its prose and fixed fields, the content key §13.4 and §5.10 already define, so neither an R1 tightening nor a re-acceptance re-keys them.
   - For evidence that fails after a later content change, choose and state one: (i) only failing assessments whose execution basis matches `D_k`'s content lower the obligation (`on⁻` against `tree(C_k)`), and drift reaches the subject's validity and a new `REPAIR` item; or (ii) every counting failure lowers it, in which case withdraw the "absorbed foreign change re-dispatches no implementer" claim and the §31.4 control for evidence-breaking drift, and disclose the re-dispatch in §32.2.
2. **Total latch at publication with a closed list of record events. Removes more.** As in option 1, but the only lowering events are revocation, an upheld veto, owner supersession, `nonind`, loss and rollback of a member of `L(o)`. Evidence failure after a later change never lowers; it goes to the subject's validity and a `REPAIR` item. Disclose the cost against the workflow owner's provisional discipline.
3. **Revert R15 to the reviewed §7.4 and narrow only step 8 (82d618c option 2).** This reintroduces the re-dispatch churn. Not recommended.

**Required discriminator.** At the real owners (Admission steps 7-9 → publication → Derivation discharge → obligation derivation → Dispatcher):

- two `IMPLEMENT` items on one leaf unit, where the second integration is the entry immediately after the first and reconciles its publication: the first is latched and never re-dispatched. The same holds when that entry is an absorption of a foreign push touching the first item's outputs. The result is identical with a records-only entry in between (order independence);
- two successive `AUTHOR` items on one `NATIVE` D2 subject, then a foreign absorption of that subject: no `AUTHOR` obligation reopens. The same holds for a gated `IMPLEMENT` item on a D4 subject after a foreign absorption;
- a foreign change that breaks a latched item's acceptance-criterion evidence follows the route the stakeholder chose, with no contradiction against any other statement;
- an R1 tightening followed by a whole-plan re-acceptance naming the tightened revision derives no new item obligation;
- negative controls, which must still lower the obligation: a post-latch `NO_PASS` upheld by the owner, an upheld challenge after a risk override, a loss boundary, a rollback, and a fenced integration (stays `OPEN`).

§31.4 has none of the positive cases above. A faithful implementation of R15 as written passes the §31.4 R15 cases whenever a records-only entry follows each integration (PEM DS-001).

## Non-blocking findings

### N1 — The class predicate captures run-keyed obligations the text calls current-state

The class is "one whose identity names an enactment, a change or an admission". But `ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` carry `rid_G(s) = (s, ι)` among their parameters, and `ι` is an enactment or an admitting entry (§10.2). `INTAKE(δ)` is keyed on an absorbed delta. §10.4 nevertheless names `ACCEPT`, `GATE` and `REVIEW(s, r)` as the current-state routes. Read literally, a latched `ACCEPT(s)` stays `DISCHARGED` by `standing` after a governing change within its run. Its consequence is small (an answered obligation is never ready again, and `REVALIDATE` still routes it), but the class needs a correct definition: say which parameter makes an obligation enacted (the item, transformation, change or specification revision it delivers), and say that a run parameter does not. This is a definition, not mechanism.

### N2 — A lowered latched item has no stated route other than ordinary readiness

Every lowering re-readies the item obligation, so its implementer is re-dispatched against current code. After a `LEDGER_LOSS` whose boundary withholds the pre-loss reviews, every integrated item is re-dispatched alongside `REQUALIFY` of its review. A veto re-dispatches before the owner's `ADJUDICATE_DISAGREEMENT` is answered. The reviewed §7.4 behaves the same way, so this is parity, not regression. Still, state the route: for example, wait while the discharging record's own `REQUALIFY` or `ADJUDICATE_DISAGREEMENT` is open. That reuses existing obligations and adds no mechanism.

### N3 — The joint-invariant review's mechanical minimum does not name the invariant's scope

§9.2 derives "a `REVIEW` of the integrated result against the invariant", and §4.3's `REVIEW` row carries `Δ(X)` and the governing closure. A `joint_invariant` declaration is not a relation (§1.7), so an unchanged scope unit `b` enters the basis only through recorded reads. Under a route whose reads are not observed, a frame-answered review stays current across a clean rebase over a concurrent change of `b`, and it latches. Then 095ce55 B1 (b) recurs, and §31.4's "made stale by a clean rebase" presumes a basis the minimum does not require. Adding ctx `content` on every unit of the invariant's scope to that review's minimum closes it. This adds one basis entry and is marked as mechanism.

### N4 — "Keep the fence" and an accepted late publication have no stated effect on the item

After a fence, the item obligation is `OPEN` and ready, so the Dispatcher may re-dispatch it before the human's keep-or-re-apply decision or the principal's `COORDINATE(plan)`, which makes "keep" ineffective for item work. Separately, an `OVERTAKEN` integration later found published (`late(n)`) and accepted by the human never latches by §10.4, so later changes reopen it as before R15. State both outcomes.

### N5 — Diagnostic and qualification scope

The model is unchanged since 095ce55 (blob `bd3ef8c…`). 095ce55 N2's point stands for the model: its `not superseded` filter is on both sides, so I8 is not independent of that clause. The Manual's (g)8 now matches (f). The model has no obligation, discharge, latch, publication or integration. §31.4 gained the 095ce55 discriminators but none for B1 here (DS-001).

### N6 — Editorial

- §10.3's route list names `REVALIDATE` twice ("`REVALIDATE`, `REVIEW(s, r)`, `REVALIDATE` or `COORDINATE(plan)`").
- §10.4's parenthetical "for an obligation answered by records only" leaves unclear whether `REVIEW(X)` and conformance (answered by records, enacted by an integration) latch at their answer or at the integration's publication. State it with B1's repair.

## Closure audit

The closure map was used to navigate. I checked its claims for every §21 item the delta or B1 touches, against the Manual sections they name. I evaluated every §10.2 obligation kind against the class predicate (N1), and every term of the §10.4 predicate under the latched reading (B1).

| Item | Disposition at this candidate |
|---|---|
| 7 (obligation rules, readiness, discharge) | **partly open (B1)**: latch state, latched value, item key; N1 (class) and N2 (route after lowering) |
| 6 (Admission validation order) | step 8 is sound in itself; its justification "enacted obligations stay discharged" depends on B1; step 7 is consistent with the fence rule |
| 9 (joint invariants) | N3 (scope not in the review's minimum) |
| 13 (publication), 18 (migration and cutover) | own rules consistent; they carry B1 (a) through the reconciliation rule |
| 1-5, 8, 10-12, 14-17, 19-27 | no unresolved architectural decision found in this bounded audit; unchanged by the delta |

§16.2 rows: unchanged by the delta. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row; none found unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1 | Sound; unchanged. Phase B N2 re-tested in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4 | Sound. Its fence cost is now consistent with R15 (a fenced item stays `OPEN`); N4 |
| R5-R8 | Sound; unchanged |
| R9 | Sound; `REFUSED` "whichever answered first" now agrees with R15's veto lowering |
| R10-R14 | Sound; unchanged. The plan row's closed form is a stakeholder-chosen conservative policy (SD-32 to SD-35), judged below |
| R15 | **Sound in direction, unsound as realized (B1).** Latching after publication and reading discharging records by standing keeps reviewed §7.4's consequences for revocation, veto, upheld challenge, risk override, loss and rollback, which 095ce55 B1 (c) lacked. As written, though, it re-reads current state through the latch state, `tgt` and the predicate's other terms, so it does not deliver "content changes never reopen it". It is an author choice under item 31; I would put B1's options 1-2 to the stakeholder |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design or disclosure closure, with real-owner execution owed later; **R** retained, as a disclosed decision or stakeholder option; **P** partly closed.

The delta since 095ce55 touches the R15 row, §4.1's stale-result route, §5.8, §5.10 (g)8, §8.3 step 8, the §10.2 `COORDINATE`, `SPEC_REVIEW` and `REVALIDATE_OVERTAKEN` rows, §10.4, §13.6, §22.2, §31.4 and §32.3 (word diff checked). I re-derived those mechanisms independently. Families the delta does not touch were re-checked at family level: by the model run, by reading their owner sections at the candidate (§5.2, §5.5, §5.10, §6.6, §7, §10.2 and §22), and by confirming the delta leaves them unchanged. I did not replay earlier records item by item.

**Mechanisms independently checked at this candidate:**

- **095ce55 B1.**
  - (a) fence or `OVERTAKEN`: §10.4 never latches; §22.2 says the item stays `OPEN`; step 7's re-application claims it. **C**, with N4's residue.
  - (b) frame-answered joint-invariant review across a clean rebase: the latch needs the predicate in the latch state. **C** where the reviewer's reads of the scope are recorded; **P** otherwise (N3).
  - (c) post-latch revocation, veto, override resolution, rollback and loss now lower the obligation. **C**.
  - (d) enumeration replaced by a class: **P**. The class over-captures (N1), and the item key is not single-valued (B1 (d)).
  - The repair opened B1 (a)-(c) here.
- **095ce55 N1-N7.**
  - N1: `SPEC_REVIEW(spec, r)`. **C**
  - N2: (g)8 restated. **C** in the Manual; the model side stands (N5)
  - N3: the return to accepted bytes is stated in §10.4, §31.4 and §32.3. **C**
  - N4: step 8 includes latched obligations. **C**
  - N5: the `COORDINATE` trigger is restated and the R1-tightening route is stated. **C**
  - N6: documentation freshness is disclosed in §32.3. **C**
  - N7: §31.4 gained fence, frame joint-invariant and post-latch cases. **P** (N5)
- **82d618c B1 and siblings.** Closed for content changes when a records-only entry follows each integration and no D1/D2 run, gated triple or evidence is involved. Reopened in those cases by B1 (a)-(c). **P**
- **Revising duty and liveness (653e88c, edabd81).** Unchanged: `standing` reads at §4.1, §4.3, §8.3 step 7, §10.2 and §16.6, and `REVALIDATE` for a gate whose assessment was replaced is answerable by its author's or the owner's superseder. B1 (b) is a new consequence of `tgt` inside `standing`, not a regression of that dependence. **C**
- **Judgment disagreement (§5.10).**
  - The per-kind table and the one reach rule are unchanged by the delta; only (g)8 changed.
  - I re-read every row against its claim. The plan row's closed form (same prose and fixed fields, the current revision not read, route-3 relief by the rejecter or owner, carry by plan subject) is a conservative resolution policy, stated as such and stakeholder-chosen. I found no tightening-order shape (chain, incomparable branch, join, revert, R2 amendment, multi-item rejection, objective revision) for which it supports what a standing rejection denies, nor a veto it cannot lift where it bites. Its restrictive cost (a cured looseness lifted only by the rejecter or owner) is disclosed.
  - The equivalence `authors` input covers both sides and re-producers. Unknown authorship needs an attestation or the owner, and cutover `MIGRATION` equivalences fall under the same rule.
  - **C/R** as in the earlier records.
- **Matching (§6.3-§6.6).** Phase B N2 re-tested in text (§6.6, line 1054). A differing old-content run under (2) and a yielding present-content run under (4) stay in through `link⁻`, an S0 test that reads no completeness, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld; only (1)/(3) narrow through `on⁺`. Support cycles (§5.6) and corrupt prefixes (§5.7) still fail closed. **C**
- **Content identity, gate qualification (`unq`), equal-region partition, run identity, acting rule.** Unchanged by the delta. **C**

| Prior record | Disposition at this candidate |
|---|---|
| 095CE55 (same family) | B1 (a) **C**, (b) **C/P** (N3), (c) **C**, (d) **P**; repair opened B1 here; N1 **C**; N2 **C**/model **P**; N3-N6 **C**; N7 **P** |
| 82D618C (same family) | B1 **P** (B1 (a)-(c) here); N1-N3 **C**; N4 **R**; N5-N7 **C** |
| EDABD81 (same family) | B1, B2 **C**; N1-N4 **C/R**; N5, N6 **C**; N7 settled in 82d618c, its lineage is B1 here |
| 653E88C (same family) | B1 **C**; N1-N2 **C**; N3 **P/R** (model limits); N4 **R** |
| D94A293 (different family) | B1 **C**; N1 **C/R**; N2 **R** (§32.2); N3 **P** (N5) |
| 913DB8F, 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows unchanged; blockers **C**; N items **C/R/D** as the edabd81, d94a293 and 095ce55 records give them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: **C** |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting and enactment, run identity, gate minimum, one integration per enactment: **C**; re-application now consistent with the latch |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap, partition: **C**, with R items unchanged |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set) |
| Phase B closures, N1-N4 | matching-family closures re-verified (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Two items on one leaf unit, second integration immediately after the first (reconciling entry) | **B1 (a)**: first never latches, re-dispatched |
| Same, with a records-only entry in between | held (latch at `D_{k+1}`), so the outcome is order-dependent |
| Foreign push absorbed as the reconciling entry, touching the integrated outputs | **B1 (a)** |
| Second `AUTHOR` revision of a `NATIVE` D2 subject after the first latched | **B1 (b)** (via `tgt`, or via `elig` after a foreign absorption) |
| Foreign change breaking a latched item's acceptance-criterion evidence | **B1 (c)** |
| Blocking challenge on a later revision of a latched item's subject | **B1 (c)** (`status1` of current revision) |
| R1 tightening, then whole-plan re-acceptance after a topology change | **B1 (d)** |
| Fenced integration, kept or re-applied; `OVERTAKEN` by a foreign push | held; N4 for "keep" and late publication |
| Post-latch upheld `NO_PASS`; risk override then upheld or dismissed challenge; rollback and re-cutover; loss boundary | held (lowering, `REFUSED` agrees); N2 for the route |
| Frame-answered joint-invariant review, clean rebase over a concurrent in-scope change | held with recorded reads; N3 otherwise |
| Second change to one specification | held (`SPEC_REVIEW(spec, r)`) |
| Later item that breaks an earlier item's required evidence | held: refused at step 8 (`REGRESSION`) |
| Composition, chain and union reach; review re-identification with a one-byte heading edit; plan closed form over every tightening shape | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, mode or persistent surface, and it deletes `REVALIDATE_OVERTAKEN`, removing mechanism. With the 095ce55 repair, R15 now keeps the capabilities the previous record named: distinguishing published from fenced work, provisional and challenged lifecycle states, P5 requalification, and re-review of joint behaviour after a rebase, subject to N3. What it does not yet deliver is the capability it exists for, stable discharge of integrated work against later content (B1). Option 1 delivers it by narrowing what the latched value reads, not by adding mechanism.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (empty `git diff --stat fad3ee41 c77447bc -- orchestrator/docs/architecture.md source dist`). The version-bound Core and frozen profiles are therefore preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator (`source/project_engineering_memory.py`, run in the clone, whose PEM file and validator equal the candidate's) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE (a green diagnostic and the §31.4 R15 cases coexist with B1).
- **SP-001**: evidence-only (one owner per rule; B1 is a property stated in one place and computed in another).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.4's R15 cases now discriminate 095ce55 B1 (fence, frame joint invariant, post-latch events), but not B1 here. Their two-item control passes whenever a records-only entry follows the first integration, and none of them runs a second D1/D2 revision past a latched `AUTHOR` item, a foreign absorption of a gated subject, an evidence-breaking foreign change, or a re-acceptance after an R1 tightening. A faithful implementation of R15 as written passes every listed case under favourable entry order. The diagnostic shares claim definitions and helpers with the rules it checks and models no obligations, so green runs say nothing about B1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. B1 touches one D4 row: "close each stage with affected regression; reconcile every obligation" relies on step 8 and on discharge staying stable, which B1 (a)-(c) breaks for content changes. This is the same defect seen from the map and needs no separate repair. No other map claim depends on the delta.

O1 (§0.5) is unchanged. The realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate:

- Blob identities above (`git rev-parse` at the candidate, and `git hash-object` of the snapshot files). The model file's blob is `bd3ef8c0449a1120a7fb4ba5e9aaa6983a1a8ce2`, last changed at `095ce557`.
- `git diff --check 095ce55704ab322208bb14ce9b2d0b7018befad2 c77447bcac18a626ff4668b72f463fc3e17e89d2`: exit 0. The delta is 5 files: the Manual (25 lines changed), the closure map (6), the continuation handoff, and the previous handoff and Review record added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… c77447bc… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate, with `--mutations` semantics, run in parallel. The driver was a scratch script under `$TMPDIR/ssds80-manual-review-c77447b/scripts/`, run with `python3 -I` (Python 3.10.12). It loaded the unmodified snapshot module by file path in each worker of a 28-worker `multiprocessing` pool, and cleared and set `MUT` at the start of every job.
  - It ran `run_family(name, verbose=False)` for each of the five families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`) with `MUT` empty. Then, for each of the 34 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names. That is 41 jobs, built from the module's own lists.
  - Base results, all with zero invariant failures: transformation-review/acceptance/gate 1,856,368 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 1,000.
  - All 34 mutations are caught. `plan_supersession_current_only` is caught by I4 only, `frame_acts_everywhere` by I5 only, `obligation_direct_only` by I8 only, and `eligibility_support_tier_only` and `challenged_record_authors` by I7 only.
  - `main()` itself was not called; the driver calls the same functions in the same configuration. The longest job took about 17 minutes.
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing, D3 design contract, Independent Review and Challenge);
  - `architecture-and-design.md` ("D3 formal-contract discipline");
  - `concurrency-and-orchestration.md` ("Idempotency and publication");
  - `workflow-and-workplans.md` (lifecycle states; the provisional discipline);
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review strategy after recurrence");
  - `project-engineering-memory.md` and `testing-and-validation.md`, applied through the validator, the HAS and DS-001.
- Reviewed-workplan text read at the candidate: §7.3, §7.4, §7.8.
- Manual sections read in full:
  - §0.3 (all rows), §4, §5.1-§5.10, §6.6, §7, §8, §9, §10;
  - §11, §13.4, §13.7, §17, §19.5-§19.8, §22.
  - The rest was read by targeted search for R15, latch, `PUBLISHED`, re-application, `REVALIDATE_OVERTAKEN`, `SPEC_REVIEW`, joint invariants and §31.4's R15 cases.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- B1 (a) rests on the S0 reading of `pub`. The retroactive reading avoids it; the Manual should state which applies (option 1 does).
- B1 (b) is shown under both readings of "each … gate decision … by standing", and each reading fails in a different case. I did not search for a third reading.
- The handoff asked for the six drift classes across the whole Manual. I applied them to every statement of R15, `standing`, `tgt`, the item key and step 8, and by targeted search elsewhere. I did not make a pairwise comparison of every concept the Manual states twice, so further drift outside those concepts is possible.
- Earlier records' per-item closures were not replayed.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations. Material findings: B1 and N1-N6. None concerns a scientific observable, numerical method or realized scientific result. B1 (b) concerns which D2 authority revision SSDS treats as delivered work and whose implementer it re-dispatches. That is a governance consequence, not a scientific judgment.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, four sibling classes:

- (a) two entry orders, plus an absorption variant;
- (b) two readings of the latched gate term, each with one decisive and one control case;
- (c) evidence and `status1` variants;
- (d) one identity trajectory;

and five negative controls. Fourteen out-of-matrix trajectory classes, overlapping rather than independent trials. One diagnostic configuration with 5 base families and 34 mutations. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. Shared dependencies:

- the corpus;
- the inherited workplan and handoff framing (including the handoff's drift-class diagnosis and its question about standing after publication, which directed the search);
- the prior Review records, read as hypotheses;
- the Git/Python toolchain;
- the diagnostic's claim definitions and helpers.

For the second consecutive round, this family's blocker entered through the previous same-family Review's recommended option, realized nearly verbatim. Same-family review of same-family repair directions is therefore a weak check here. A different-family check of B1 and of whichever option is chosen is advisable before G1.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Put B1's options to the stakeholder (option 1 recommended). Restate R15's latched value as a record-level fact over the records fixed at the latch, and reconcile:
   - the R15 row, §10.4, §8.3 step 8 and closure map line 87 (one latch state);
   - §4.1 and §5.2 (`standing` without `tgt` for latched use, or a named run-free standing);
   - §10.4 and §13.7 (item and part key);
   - §32.2 and §31.4 (the chosen evidence route and its disclosure).
2. Add B1's discriminator to §31.4.
3. Consider N1-N6. N1 and N2 are definitions the B1 repair touches anyway; N3 adds one basis entry (mechanism, marked).
4. Freeze a replacement candidate and obtain an independent Review, preferably a different-family one, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.

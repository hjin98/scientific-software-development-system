# Independent D3 Review — SSDS 8 Architecture Manual, candidate 095ce55

    GOVERNING SSDP:     7.2.1
    REPOSITORY:         hjin98/scientific-software-development-system
    BRANCH:             ssds-8.0-graph-native-architecture
    CANDIDATE:          095ce55704ab322208bb14ce9b2d0b7018befad2
    SCOPE:              the whole proposed Manual as durable D3 owner (handoff §1 (a)-(g));
                        technical evidence for G1 only
    MANUAL blob:        314138d5782376e751c07baa937c290874be2980 (orchestrator/docs/ssds-8.0-architecture.md)
    CLOSURE MAP blob:   361673e67ba9bfdf75362430a2473f8809b9aa6e (review aid, not authority)
    PARENT WORKPLAN:    workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
                        design revision 23; blob at candidate 91bde236465178f20c7348280e036d2884dfc216
    PHASE B CANDIDATE:  e23f14208be869e6a78cfd7b312e447254ee1851 (workplan blob 610f373b97fb8152d2a5742e17fa172e12204756)
    GOVERNING REFS:     public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
                        recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d (PROTOCOL-RELEASE-STATE.yaml)
    PRIOR REVIEWS:      Phase B and every Manual Review record through the same-family 82d618c
                        NO-PASS; hypotheses only, never authority
    REVIEW METHOD:      git-archive snapshot of the exact candidate; delta-first attack of refinement R15
                        in both directions, by asking, for every obligation the latch can touch, at which
                        event it latches, which inputs it freezes, and what happens to it on every route by
                        which an integration's effect or its discharging judgments can later fail (fence,
                        OVERTAKEN, clean rebase, revocation, veto, risk override, rollback, loss boundary);
                        the handoff's six drift classes applied to every statement of the latch, step 8,
                        "depends on" and the stale-result route; family-level recheck of earlier families;
                        diagnostic model run in full (parallel, every family and mutation); structural checks
                        of handoff §3 step 9
    REVIEWER:           Claude family (the Manual author's family); a fresh-context sub-agent launched
                        by the authoring session; did not author the candidate; no sub-agents used

Line numbers refer to the Manual blob above, extracted by `git archive` into `$TMPDIR/ssds80-manual-review-095ce55/snap`. The later commit adding the handoff (`a9d8403c`) was not substituted for the candidate. This is a deductive architecture review, not an observation of an SSDS implementation.

## SERIOUS CHALLENGE

None against accepted governing authority. The accepted SSDP 7.2.1 owners, the reviewed workplan and the stakeholder's recorded decisions (SD-1 to SD-35, record items 19 and 31) can be realized together. The blocker below is in R15, a refinement the author added under record item 31 and lists for the stakeholder (closure map §5); it is routed against the proposed D3 owner, and its repair options are put to the stakeholder because R15 itself is stakeholder-visible.

## Verdict

**NO-PASS.** One blocker, a non-local recurrence of the 82d618c B1 family (the obligation lifecycle after integration) that entered through that Review's recommended repair:

- **B1**, enacted-obligation latch. R15 latches an enacted obligation at the admission of the request that integrates it, or of the judgment that answers it, and then freezes every input of its discharge. So a latched discharge outlives the effect it records (a fenced or `OVERTAKEN` integration), is fixed before the integration whose result it judged (a joint-invariant review answered in the candidate's frame, then a clean rebase), and ignores later failure of the judgments it rests on (revocation, veto, a risk-overridden challenge upheld, rollback). The latch is realized by an enumerated list, so enactment-keyed obligations outside the list (`REVALIDATE_OVERTAKEN`, `INVESTIGATE`, a partitioned item's item-level review) fall to the current-state default and recreate 82d618c B1's re-dispatch.

R15's purpose holds for the trajectory that motivated it: two sequential items editing one file both integrate, step 8 refuses only evidence regression, and absorbed drift re-dispatches no implementer of a published integration (82d618c B1 and its siblings (a), (b), (d), (e) closed for content changes). The 82d618c non-blocking repairs hold except for one drift (N2). The diagnostic model is green on all five families and catches all 34 mutations. It models no obligation, discharge, latch or publication, so it cannot see B1.

## Blockers

### B1 — The R15 latch fixes discharge at the wrong event and over the wrong inputs

**Family:** obligation lifecycle after integration (82d618c B1), now through its repair. **Earliest owner:** Manual §10.4 "Enacted obligations latch" (line 1320) with the R15 row (line 100), deciding workplan §21 item 7 (obligation rules, discharge) and touching items 6 (Admission step 7) and 9 (joint invariants). **Status:** open, material, non-local (§10.2, §10.4, §5.10 (f), §8.3 step 7, §13.7, §19.5, §22.2-§22.3, §31.6 each contribute).

**Exact rules at the candidate.**

- §10.4 (line 1320): "An obligation keyed on an enactment or a change is discharged once: the item obligations (`IMPLEMENT`, `REPAIR`, `MIGRATE`, `AUTHOR`, `DOCUMENT`) of an item revision, and their partition parts, by the admission that integrates their enactment with the predicate above holding in its post-state; `REVIEW(X)` and the conformance of transformation `X`, `JOINT_INVARIANT(i, k)` of change `k` and `SPEC_REVIEW` of a specification change, by their answering judgment as above at its admission. Later content changes never reopen them. Every other obligation (`ACCEPT`, `GATE`, …, `REVALIDATE`, `PLAN_ACCEPT`, the report and attention obligations) is keyed on current state and is not latched".
- R15 row (line 100): "discharged once and never reopened by later content".
- §5.2 (line 656): "Acting is monotone along the admitted history (an integration is permanent)"; an `OVERTAKEN` or fenced integration stays an integration.
- §8.3 step 7 (line 1189): "an integration request whose enactment … already has an admitted integration is refused (`OBLIGATION_REENACTED`), even when that integration was `OVERTAKEN` or fenced; further work on the obligation, re-application included (§22.2-§22.3), is a new task (R12)"; and "Each obligation whose discharge the request claims is undischarged at the current head (a duplicate discharge is rejected and recorded)".
- §22.2-§22.3: a fence classifies `n` `OVERTAKEN` and restores `tree(B_n)`; `REVALIDATE_OVERTAKEN` is derived; "the human chooses to re-apply `n` … or keep the fence".
- §7.5: "Obligations in `D_n[X]` are derived in that state like any other, so they are the obligations `X`'s integration would produce"; review judgments about a transformation declare frame `id(X)`. §7.6 "Rebase": a frame-`X` record counts for `X'` only if its entries hold in `D_n[X']`.
- §5.10 (f) (line 879): an answered judgment obligation whose target carries a standing, unrelieved adverse judgment is `REFUSED`, "whichever answered first". §5.5: "A risk override never resolves a challenge".

**Decisive trajectory (a fenced integration).**

1. Item `I1` (`IMPLEMENT`, or `AUTHOR` of a `NATIVE` D2 subject `b`) produces `X1`. Review, conformance, evidence and gates hold. The integrating admission `n` is admitted. By §10.4, `IMPLEMENT(I1)` is latched `DISCHARGED`, its predicate holding in `D_n`.
2. The publisher crashes inside the publication window. A takeover appends a fencing absorption `k`. The tree returns to `tree(B_n)`, `n` is `OVERTAKEN`, and `REVALIDATE_OVERTAKEN(n)` is derived (§22.2-§22.3).
3. The fence is a later content change, so by §10.4 it "never reopen[s]" `IMPLEMENT(I1)`. The item reads `DISCHARGED`, while nothing it asked for is in the governed tree. Any evidence specification `X1` added is absent too, so no `REALIZE` or failing assessment surfaces the gap. A D4 subject is back at its earlier revision, which is valid because its earlier acceptance is reused by content identity (R10).
4. **Keep the fence.** The item stays discharged without its effect. No rule derives work for `I1`: the item is not ready, `REVALIDATE_OVERTAKEN` has no stated end after a keep decision, and intake covers only "content not produced by an admitted request" (§18.1): at most it shows drift, and no intake disposition redoes `I1`. For the `AUTHOR` variant, §22.3 and §31.6 (O) derive `REVIEW(b, r_old)`, `ACCEPT` and `GATE` for the *old* revision in a new run, so the stakeholder is asked to re-accept the D2 revision that `I1` was accepted to replace, while `I1` reads done.
5. **Re-apply.** Step 7 calls re-application "further work on the obligation". But the obligation, `IMPLEMENT(I1)`, is latched `DISCHARGED`, so a request claiming it is rejected as a duplicate discharge. If the implementer binds it instead to `REVALIDATE_OVERTAKEN(n)`, that obligation is keyed on an admission but is not in R15's list, so it is current-state (§10.4 "every other obligation"). Its trigger ("an `OVERTAKEN` admission") holds forever, so after the re-application integrates, any later change to its units makes its review non-current, reopens it, and re-dispatches the implementer against later code. That is 82d618c B1 sibling (e) again.

Under the reviewed workplan (§7.4, non-latched), step 3 makes `IMPLEMENT(I1)` `OPEN` at `k`, because its review's output entries no longer hold. Re-application then claims it, and keeping the fence leaves it to be redone. R15's row discloses neither the change nor the conflict with step 7.

**Siblings (same cause).**

| Sibling | Trajectory | Result |
|---|---|---|
| (b) latched before the result it judged exists | `X` changes unit `a` in joint invariant `i`'s scope `{a, b}`. By §7.5, `JOINT_INVARIANT(i, ·)` for `X`'s change is derived in `D_n[X]`, and a reviewer answers it there on `M_n(X)`. It latches at that judgment's admission. Concurrent `k'` changes `b` and integrates, and its own `JOINT_INVARIANT(i, k')` is reviewed on a tree without `X`. `X` rebases cleanly (disjoint files) and integrates | the joint behaviour of `a` and `b` is reviewed by nobody. Before R15, the frame review stops counting for `X'` (§7.6) and its own discharge predicate derives `REVALIDATE`. Under R15 the obligation is already discharged, so the write-skew class joint invariants exist for (K3, §9.1 "review of integrated results") passes unreviewed. `SPEC_REVIEW` answered in a frame is exposed the same way: failures counted after the frame review are made stale unseen. This depends on frame derivation of `JOINT_INVARIANT`, which §7.5's general rule implies and nothing excludes |
| (c) post-latch failure of the discharging judgments | (i) after `X1` integrates, a human records `NO_PASS` on `X1`. It vetoes `r1`, `ADJUDICATE_DISAGREEMENT` follows, and the owner sides with the `NO_PASS`. (ii) `X1` integrated `DISCHARGED_PROVISIONAL` under a `RISK_OVERRIDE` of a blocking challenge against `r1`, and the challenge is then upheld or dismissed. (iii) a version rollback ends a cutover subject's `NATIVE` tenure after the `MIGRATE` carrier integrated, and the stakeholder re-cuts over. (iv) a `LEDGER_LOSS` withholds `r1` | §10.4 says both "discharged once" and "Later content changes never reopen them", and none of these events is a content change. Total latch: (i) the item stays discharged on a judgment its owner has rejected, and no `COORDINATE` follows because the findings are in scope. (ii) the override has become a permanent waiver, or the item stays provisional forever, against §5.5 "A risk override never resolves a challenge" and the workflow owner's provisional discipline. (iii) §31.6 (L)'s "re-cutover after rollback under the same `MIGRATE` item" cannot claim the discharged `MIGRATE` obligation. (iv) item closure passes the boundary without requalification (P5). Content-only latch: §10.4 defines no evaluation of the predicate with frozen content but live S1 standing, and reopening would re-dispatch against later code. §5.10 (f)'s `REFUSED` "whichever answered first" also contradicts a latched `REVIEW(X)` when a `NO_PASS` arrives after the `PASS` |
| (d) enumeration instead of the class | `REVALIDATE_OVERTAKEN(k)` (keyed on an admission); `INVESTIGATE` items (item obligations with no integration; in neither list); a partitioned item's own discharge and its item-level review (§13.7: no obligation kind, no latch event); item-obligation identity under an R1 tightening (§13.7 parts are "identified by the item revision", while §10.4 says "a control tightening (R1) keeps the enacted obligation discharged") | each falls to the current-state default or is undefined. `REVALIDATE_OVERTAKEN` and `INVESTIGATE` reopen whenever a later change reaches what their judgments read, so their holders are re-dispatched (82d618c B1 (e)). The item-level review goes stale on any later change in the item's scope. A tightening that re-keys item obligations would derive a new, undischarged `IMPLEMENT` for integrated work |
| control | content changes after a *published* integration: two sequential items on one file, a read file, a second joint-invariant change, a second `AUTHOR` revision, an absorbed foreign change | **holds** (82d618c B1 closed for these) |

**Shared cause.** R15 names its class by a description ("keyed on an enactment or a change") but realizes it with a per-kind list. The latch event is the admission of a request (an intent; for judgments, possibly in a candidate's frame), not the enacted, published effect the obligation is about. It freezes every input, where 82d618c B1 needed only the content currency of the discharging judgments' entries frozen. One rule cannot do all three, so each sibling is a place where the frozen fact and the current fact differ. These are the handoff's drift classes "a mutable identity versus what was judged" and "readiness versus admissibility", re-entering at the obligation layer. Discovery stops here. Further variants (`DOCUMENT` items under a fence, partition parts under a fence, a cutover carrier fenced, §19.5) re-derive (a) or (c).

**Violated owner text.**

- Concurrency owner (`aaeaf8b:source/shared/references/concurrency-and-orchestration.md`, "Idempotency and publication"): "Ensure a resumed stage can distinguish accepted work from partial/stale work". A latched discharge cannot distinguish a published integration from a fenced one (sibling (a)). C4 (§0.4): "external effects follow intent, idempotent or reconcilable effect, observed outcome".
- The Manual's own §10.4: "A missing required check is an undischarged obligation; no rule turns it into a pass". The §29.3 D4 row claims E0 for "discharge requires every obligation".
- Workflow owner (`workflow-and-workplans.md`, "Authority lifecycle, mutation, and impact closure"): it distinguishes "challenged; risk-accepted/provisional; stale-dependent", and says "descendants must not reset that state to accepted-current or emit unqualified Pass/closure while the challenge remains unresolved" (sibling (c)). Evidence owner (`evidence-evolution-and-dependencies.md`, "Change impact and closure"): "Revert/restoration … reconciles present applicability … Restoring an old file does not restore old evidence validity by timestamp". Under (a), the fence's restoration of `tree(B_n)` is not reconciled with `I1`'s closure.
- K3 and §9.1 (joint validity "judgment: declared joint invariants, review of integrated results") for sibling (b).
- Architecture owner (`architecture-and-design.md`, "D3 formal-contract discipline"): "define it before dependent invariants use it: … lifecycle states and transitions". R15's latch transition is defined per listed kind and per request admission, not for the class it names (sibling (d)).
- Contradictions an implementer must resolve by choosing: §10.4 latch versus §8.3 step 7 ("further work on the obligation, re-application included" versus duplicate-discharge rejection); §10.4 versus §5.10 (f) `REFUSED` "whichever answered first"; §10.4 versus §31.6 (L); "discharged once" versus "Later content changes never reopen them". The R15 row presents the narrowing as "never reopened by later content". It does not surface the narrowing of reviewed §7.4 for fences, revocations, risk overrides, rollback or loss, so as written it is also an unsurfaced semantic change to the reviewed contract.

**Convergence assessment.** This is a non-local recurrence: the third consecutive round in the obligation-lifecycle family (edabd81 N7, 82d618c B1, here), entering through the previous round's recommended repair. A further per-sibling patch would add latch exceptions. Options for the stakeholder (Phase C handoff §5), each narrowing or replacing mechanism:

1. **Recommended: one rule, keyed on the effect and freezing only content currency (replaces R15's per-kind list).** An obligation whose target is an enactment, a change or an admission (defined as a class: item obligations and parts, a partitioned item's item-level review, `REVIEW(X)`, conformance, `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW` of a specification change, `REVALIDATE_OVERTAKEN(k)`, an `INVESTIGATE` item at its answering judgment) **latches in the first admitted state at or after its enactment's integration is `PUBLISHED`** (S0 `pub`), or, for a records-only target, its target's admission, **in which its predicate holds with every discharging judgment acting there**.
   - An `OVERTAKEN` or fenced integration never latches, so the item obligation is `OPEN` and re-application claims it. `REVALIDATE_OVERTAKEN` then becomes a pointer that may be deleted (removes mechanism).
   - A frame-answered joint-invariant or specification review latches only if it is still current at the integration.
   - Once latched, the discharging judgments are read in the existing `standing` mode (`base`), never for content currency. Revocation, a veto, a supersession by the owner, `nonind`, a loss boundary or a mode rollback lowers the obligation, and `P` follows the override. Where the obligation falls, route it as the reviewed contract did (ordinary readiness). Routing it instead to `COORDINATE(plan)` would add a trigger, which is mechanism; mark it so if chosen.
   - State the item-obligation identity as the item and its accepted revision, so an R1 tightening does not re-key it.
2. **Total latch, keyed on publication, disclosed.** Latch at `PUBLISHED` as in option 1, but keep every later event inert. Then state in R15 and §32.2 that revocation, veto, override resolution, rollback and loss after the latch reopen nothing and that a `REPAIR` item is the route. Restate §5.10 (f) `REFUSED` and §31.6 (L) to match, and keep (b)'s repair. This removes more mechanism, but it drops reviewed §7.4 consequences and P5 requalification of item closure. That needs the stakeholder's explicit acceptance against the workflow owner's provisional discipline. Not recommended.
3. **Revert R15 to non-latched discharge and narrow only step 8** (82d618c option 2). This reintroduces 82d618c B1 (e)'s re-dispatch churn and stranded revalidations. Not recommended.

**Required discriminator.** At the real owners (Admission steps 7-9 → publication → Derivation discharge → obligation derivation):

- a fenced `IMPLEMENT` integration leaves the item obligation `OPEN`; re-application claims it and integrates; keeping the fence never shows the item `DISCHARGED`; the same for an `AUTHOR` item of a `NATIVE` D2 subject and for an `OVERTAKEN` integration;
- after the re-application integrates, a later change to its units re-dispatches nobody;
- a joint-invariant review answered in `X`'s frame, followed by a clean rebase over a concurrent in-scope change, leaves `JOINT_INVARIANT` for `X`'s change undischarged until a review of the actual integrated result;
- a post-integration `NO_PASS` upheld by the owner, and an upheld challenge against the enacting review, lower the item obligation, and §5.10 (f)'s value agrees;
- an item integrated `DISCHARGED_PROVISIONAL` under a risk override becomes `DISCHARGED` when the challenge is dismissed and leaves discharge when it is upheld;
- §31.6 (L)'s re-cutover after rollback under the same `MIGRATE` item is admitted;
- an `INVESTIGATE` item whose investigator read a file that later changes re-dispatches nobody;
- negative controls (R15's current cases): two sequential items on one file both integrate; a candidate breaking another closure's required evidence is refused.

§31.4 and §31.6 have none of the positive cases above. A faithful implementation of R15 as written passes every R15 case listed there (PEM DS-001). The diagnostic model has no obligations, publication or integration transition.

## Non-blocking findings

### N1 — `SPEC_REVIEW` is keyed on the specification in §10.2 and on the change in R15

§10.2 (line 1270) writes `SPEC_REVIEW(spec)`, triggered by "a change to an evidence specification" (§17.1 likewise raises it on "a change to a specification unit"). R15 and §10.4 latch "`SPEC_REVIEW` of a specification change". If the identity's target is the specification, a second change of it derives an already-latched identity and is never reviewed, which is permissive. §10.3's general rule ("A judgment obligation's target is the exact thing judged … so a new revision … derives a new obligation") points to per-change keying. Write `SPEC_REVIEW(spec, r)` in the table. This is a definition, not mechanism.

### N2 — Invariant (g)8 did not follow the (f) repair, and the model changed both sides

§5.10 (f) now derives `ADJUDICATE_DISAGREEMENT` only for a vetoed passing judgment "acting in the state and not superseded there" (82d618c N3). Invariant (g)8 (line 892) still says "In every state where a standing objection vetoes a passing judgment acting there". `vetoed` does not test supersession, so the two now disagree for a superseded vetoed judgment. The model's delta adds the same `not superseded` filter to both `Ledger` (line 514) and `oracle_disagreement` (line 758). The I8 oracle is therefore not independent of this change: a wrong (f) would stay green. Restate (g)8.

### N3 — "An absorbed foreign change shows as an invalid subject" is false for a return to accepted bytes

The R15 row, §10.4, §32.3 and §31.4 ("an absorbed foreign change invalidates acceptance") say this. A foreign change that returns a subject other than a `NATIVE` D1/D2 subject to bytes an earlier acceptance in its tenure covers leaves the subject **valid** (R10, reuse by content identity). The signals are then intake (§18.1, "content differs from accepted revisions") and the display-only drift view. State this, and correct the §31.4 discriminator, which a correct implementation would fail for a revert.

### N4 — Step 8's scope over latched obligations' evidence is implicit

Step 8 protects "every other obligation whose required evidence the merged tree affects … the evidence terms it reads". A latched obligation reads no term. So evidence that only an item's acceptance criteria require, and no subject policy requires, is protected only if latched obligations count. §31.4 ("its required evidence is rerun on the merged tree") assumes they do. State it.

### N5 — The stale-result route still has one non-mechanical statement and a tightening case

§10.2's `COORDINATE` trigger still reads "stale result needing re-planning", while §4.1 now defines the route mechanically ("stale through its item revision or contract"). Also, an R1 control tightening changes the item revision. An in-flight `TASK_RESULT`'s `EXACT` entry on it then routes to `COORDINATE(plan)`, although the tightening only needs its new checks run. That is restrictive churn; state whether it is intended.

### N6 — Read-based reopening of documentation and investigation outputs is gone without disclosure

Under R15, a `DOCUMENT` item's recorded reads of code no longer reopen anything after integration. Only declared relations reach the document's acceptance. This is consistent with R15, but §32.2 should list it as a cost (documentation freshness rests on declared relations and the §9.4 residual). Whether `INVESTIGATE` follows the latch is B1 (d).

### N7 — Diagnostic and qualification scope

The model's delta is the two-sided `not superseded` filter (N2). It has no obligations, discharge, latch, publication, integration, rebase or rollback, so a green run coexists with B1 (DS-001). §31.4's R15 cases are all content-change controls, and the B1 discriminator should join them.

## Closure audit

The closure map was used to navigate. I checked its claims for every §21 item the delta or B1 touches, against the Manual sections they name. I swept every §10.2 obligation kind for its latch class, its latch event and its route after a fence, rebase, revocation, rollback and loss. Other items were taken as dispositioned in the 82d618c, edabd81 and 653e88c records unless a mechanism below reopens them.

| Item | Disposition at this candidate |
|---|---|
| 6 (Admission validation order) | step 8 closed for content changes (82d618c B1); **partly open (B1)**: step 7's re-application and duplicate-discharge rules contradict the latch after a fence or `OVERTAKEN` |
| 7 (obligation rules, readiness, discharge) | **partly open (B1)**: the latch event and inputs, and the latch class for unlisted enactment-keyed kinds; N1 (`SPEC_REVIEW` key) |
| 9 (joint invariants) | **partly open (B1 (b))**: frame-answered joint-invariant review across a clean rebase |
| 13 (publication), 18 (migration and cutover) | inherit B1 (a) and (c)(iii); their own rules are unchanged and consistent |
| 4, 5, 10, 26 | the delta's §4.1, §4.3, §5.9 and §16 statements are consistent; no open decision |
| 1-3, 8, 11-12, 14-17, 19-25, 27 | no unresolved architectural decision found in this bounded audit; unchanged by the delta |

§16.2 rows: unchanged by the delta. §26.4 keeps an explicit replacement, retirement or preserved boundary for every row; none found unresolved.

## Refinements R1-R15

| # | Assessment |
|---|---|
| R1 | Sound as stated; unchanged. Phase B N2 re-tested in text (below) |
| R2, R3 | Sound fail-closed SCC clamp and integrity halt; unchanged |
| R4 | Sound for publication itself; under R15 a fence also leaves enacted obligations latched (B1 (a)), which R4's cost statement omits |
| R5-R7 | Sound; unchanged and not re-derived beyond the text |
| R8, R9 | Sound. R9's `REFUSED` "whichever answered first" now conflicts with R15's latch of `REVIEW(X)` (B1 (c)) |
| R10 | Sound; it also makes N3's "invalid subject" claim false for reverts |
| R11-R14 | Sound; unchanged |
| R15 | **Sound in direction, unsound as realized.** Latching content currency after a published integration and reading only evidence regression at step 8 keep the workplan's purpose ("A D4 change that breaks another closure is a regression") for content changes and remove the drift re-dispatch. As written, the latch event (request admission), its inputs (all) and its class (an enumeration) narrow reviewed §7.4 beyond what the row states (B1). It is an author choice under item 31; I would put options 1-2 of B1 to the stakeholder |

## Re-verification of earlier findings (family level)

Key: **C** closed by the named current rule; **D** design or disclosure closure, with real-owner execution owed later; **R** retained, as a disclosed decision or stakeholder option; **P** partly closed. The delta since 82d618c touches the R15 row, §4.1, the §4.3 review row, §5.9, §5.10 (a) and (f), §8.3 step 8, the §10.2 `REVALIDATE` row and "counts", §10.3, §10.4, §13.7, §31.4, §31.6 and §32.3. I re-derived those mechanisms independently. Earlier records' per-item closures are treated as unchanged unless a mechanism below reopens them; earlier Reviews were not replayed item by item.

**Mechanisms independently checked at this candidate:**

- **82d618c B1 and siblings.** The decisive trajectory (two items, one file) holds: step 8 reads evidence terms only, and `IMPLEMENT(I1)` is latched. (a) read files, (b) a second joint-invariant change (each gets its own obligation), (d) a second `AUTHOR` revision and (e) absorbed drift without re-dispatch hold for content changes after a published integration. **C** for those; the repair opened B1 here.
- **82d618c N1-N7.**
  - N1: "depends on" is defined, with its end (line 1261). **C**
  - N2: §4.1 now says re-attest the same candidate, newest result, mechanical route. **C**; N5's residue
  - N3: §10.3 states the class and the owner's adverse superseder, and (f) tests supersession. **C**; N2's (g)8 drift
  - N4: listed for the stakeholder in closure map §5. **R**
  - N5: §4.1 and §31.6 (Z) wording. **C**
  - N6: "counts", `PRODUCT_SCOPE_ACCEPTANCE` and the §5.9 analyzer burden. **C**
  - N7: (Z) carries the additional-`record` refusal. **C**; diagnostic scope unchanged (N7 here)
- **Revising duty and liveness (653e88c, edabd81).** Unchanged: `standing` reads at §4.1, §4.3, §8.3 step 7, §10.2 and §16.6. `REVALIDATE` for a gate with a replaced assessment is still answerable by its author's or the owner's superseder. **C**
- **Judgment disagreement (§5.10).** The per-kind table and the reach rule are unchanged. The only edits are (a)'s naming of targeted kinds and (f)'s supersession filter. I did not find a composition, re-identification or plan shape the text mishandles, beyond what earlier records retain as policy. **C/R** as in edabd81 and d94a293.
- **Matching (§6.3-§6.6).** Phase B N2 re-tested in text (line 1054) with an alternate tree differing only outside a recorded narrow basis. A differing old-content run under (2) and a yielding present-content run under (4) stay in through `link⁻`, under a completeness judgment that becomes `P`, blocked, revoked or loss-withheld; only (1)/(3) narrow. Support cycles (§5.6) and corrupt prefixes (§5.7) still fail closed. **C**
- **Content identity, gate qualification (`unq`), equal-region partition, run identity.** Unchanged. **C**

| Prior record | Disposition at this candidate |
|---|---|
| 82D618C (same family) | B1 **C** for content changes; recurred through its repair as B1 here (fence, frame latch, standing, enumeration); N1 **C**; N2 **C**/**P** (N5); N3 **C**/**P** (N2); N4 **R**; N5 **C**; N6 **C**; N7 **C**/**P** (N7) |
| EDABD81 (same family) | B1 **C**; B2 **C**; N1-N4 **C/R**; N5 **C**; N6 **C**; N7 settled in 82d618c, its repair is B1 here |
| 653E88C (same family) | B1 **C**; N1-N2 **C**; N3 **P/R** (model limits); N4 **R** |
| D94A293 (different family) | B1 **C**; N1 **C/R**; N2 **R** (§32.2); N3 **P** (N7) |
| 913DB8F, 5895687, 4C52205 (SC-1 **R**), both E548472 (same-family SC-1 **R**), D6734C4, 83A82DF, 0D2B35E, 34803DF, BF23372, A6ED164 | plan, review, equivalence and completeness rows unchanged by the delta; blockers **C**; N items **C/R/D** as the edabd81 and d94a293 records give them; plan-policy items **R** |
| 6B986DE, 29DA56E, 51070E5, 9E5A763, 051CCE3, 63DDF91, F03B15E, 61CD09B | independence, adjudication eligibility, supersession targets and relief: **C** |
| 362AF9F, F22B4DC, both B46C250, F7419D5, 575DC78 | acting and enactment, run identity, gate minimum: **C**; the one-integration-per-enactment rule (SD-26) is sound in itself, but its re-application clause now conflicts with R15 (B1 (a)) |
| 5C55D4B, 27EF339, 0B6C4FA, A18B544, E9E6E9F, E2154AC, 3540D98 | matching, content identity, qualification cap, partition: **C**, with R items unchanged |
| 798B2B4, 71CF9B3, 86AB683, 1FFBBF0, 53669A5, D837363, CC005DB, C6DA678, B595F2C, 6FF4ED1 | **C** for each stated blocker (run-keyed counting, event-keyed run, `tgt` read by every consumer, frozen matching, effect-keyed write set) |
| Phase B closures, N1-N4 | matching-family closures re-verified (above); N1 **R** (§32.2); N2 **C/D**; N3 **R/D** (diagnostic limits); N4 **R** (empirical costs) |

## Out-of-matrix trajectories

| Trajectory | Outcome |
|---|---|
| Two sequential `IMPLEMENT` items editing one leaf unit; a later item editing a file an earlier reviewer read; a second change in a joint invariant's scope; a second `AUTHOR` revision of one D2 subject | held (step 8 evidence-only; latch) |
| A later item that breaks an earlier item's required evidence | held: refused (`REGRESSION`), subject to N4's scope statement |
| Absorbed foreign change after a published integration | held: no re-dispatch; intake follows; N3 on the "invalid subject" claim |
| Fenced integration, fence kept; fence re-applied; `OVERTAKEN` by a foreign push | **B1 (a)**; re-application via `REVALIDATE_OVERTAKEN` gives **B1 (d)** |
| Frame-answered joint-invariant review, clean rebase over a concurrent in-scope change | **B1 (b)** |
| Post-integration `NO_PASS` upheld; upheld challenge against the enacting review; risk-overridden challenge resolved after a provisional integration; rollback and re-cutover under one `MIGRATE` item; loss boundary withholding the enacting review | **B1 (c)** |
| `INVESTIGATE` item whose read file later changes; partitioned item after parts integrate and later changes; R1 tightening of a partly integrated item | **B1 (d)** |
| Second change to one evidence specification | held under §10.3's general rule; N1 under §10.2's literal key |
| Stale agent judgment replaced by a fresh one | held: `REVALIDATE` ends ("no longer depended on") |
| Stale pre-integration task result (governing change; item amendment; R1 tightening) | held as routes; N5 for the tightening case |
| `ACCEPTANCE` `FAIL`/`PASS` after the subject moved; plan disagreement after the item moved | held: §10.3's waiting class, lifted by route 4 or the owner's adverse superseder |
| Superseded vetoed passing judgment | held by (f); (g)8 disagrees (N2) |
| Composition, chain and union reach; review re-identification with a one-byte heading edit; plan closed form | held (unchanged; model green) |
| Completeness lapse under a narrow-basis failure (Phase B N2) | held |

## Minimum architecture and capability transfer

The delta adds no primitive, component, record kind, mode or persistent surface. R15 removes 82d618c's drift re-dispatch and judgment-currency protection at step 8. That removal is the minimum direction, but it also removes the reviewed reopening of enacted work after a fence, revocation, risk-override resolution, rollback or loss, without listing it (B1). The capabilities whose loss R15 must either avoid or state:

- distinguishing published from fenced work (concurrency owner);
- provisional and challenged lifecycle states for integrated work (workflow owner);
- requalification of closure across a loss boundary (P5);
- re-review of joint behaviour after a rebase (K3, §9.1).

B1 option 1 keeps them with one rule and lets `REVALIDATE_OVERTAKEN` be deleted.

Architecture 1.6.0 (`orchestrator/docs/architecture.md`, blob `39e6de727f6c35402962509d30d947962992eaad`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee41` (empty `git diff --stat`), so the version-bound Core and frozen profiles are preserved (PEM PC-001).

**PEM.** Activated: this is mature replacement and recurrence under a memory-bound workplan. `main` and `origin/main` both resolve to `af0455753e20ee54a969c844872e29e270007211`. The PEM blob there and at the candidate is `1561797125622f355f84eb27319f87e8fa4227d9`, so there is no overlay. The repository validator (`source/project_engineering_memory.py`, run in the clone on that blob) reports "PEM schema 1 valid: 5 families, 0 notices". Task-local HAS:

- **PC-001**: APPLICABLE (frozen profiles; preserved).
- **DS-001**: APPLICABLE (a green diagnostic and green §31.4 R15 cases coexist with B1).
- **SP-001**: evidence-only (one owner per rule; B1 is one rule realized per kind).
- **SP-002, FF-001**: evidence-only, not material.

Missing wider history does not prove absence.

## Qualification-design adequacy

§31 separates G1 document checks from G2-G4 runtime evidence and claims no execution it lacks. §31.4's R15 cases discriminate the 82d618c B1 trajectories, but not B1 here: they have no fence, `OVERTAKEN`, frame-answered joint invariant, post-latch revocation, override resolution, rollback or unlisted kind. §31.6 (L) and (O) presume a re-application or re-cutover under the original item obligation, which R15 makes impossible, so the qualification design contradicts the rule it would test. The diagnostic shares claim definitions and helpers, and its only delta changes model and oracle together (N2). It models no obligations, so green runs say nothing about B1.

## Doctrine-realization map and O1

§29 maps all seven entrypoints. Two D4 rows are affected by B1. "a required check that did not execute is not a pass … discharge requires every obligation" (E0) is not met by a latched discharge of fenced work. "close each stage with affected regression; reconcile every obligation" relies on step 8, which now matches the workplan's purpose for content changes. These are the same defect seen from the map and need no separate repair. No other map claim depends on the delta.

O1 (§0.5) is unchanged. The realized record, readers, routine questions, retention and marked surfaces are stated, all within the requested deliverable and none beyond it. Technical Review accepts no product-scope item.

## What I verified and how; what I could not verify

Executed against the extracted candidate:

- Blob identities above (`git rev-parse` at the candidate). The model file's blob is `bd3ef8c0449a1120a7fb4ba5e9aaa6983a1a8ce2`.
- `git diff --check 82d618cd26900f8cb7b0aaa6be7cac3d3a7c030c 095ce55704ab322208bb14ce9b2d0b7018befad2`: exit 0. The delta is 6 files: the Manual (29 lines changed), the closure map (5), the model (6), the continuation handoff, and the previous handoff and Review record added.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the snapshot: 4 tests OK (routing and lifecycle structure only).
- `git diff --stat fad3ee410ab9df0d94740cebb6969e161911b126 bf2337285dfdaba5d535e73cf76af3d5b78978f0`: 73 files, 23,269 insertions, 1 deletion (that historical comparison only).
- `git diff --stat fad3ee41… 095ce557… -- orchestrator/docs/architecture.md source dist`: empty.
- PEM validation as above.
- Diagnostic model at the candidate, re-checked equal to the snapshot with `git hash-object`. The `--mutations` workload was run in parallel by importing the unmodified module from a scratch driver under `$TMPDIR/ssds80-manual-review-095ce55/run/`. The driver used a 30-worker `multiprocessing` pool with forked workers, and cleared and set `MUT` at the start of every job. It ran `run_family` for each of the five families (`CORE`, the three in `FAMILIES`, `GATE_BASIS`) with `MUT` empty. Then, for each of the 34 entries of `MUTATIONS`, it set `MUT = {m}` and ran `run_family` on each family that mutation names. That is 41 jobs, built from the module's own lists.
  - That full run was started with plain `python3`, not `-I`. Its directory held only my driver, and the snapshot's `qualification/ssds80` was inserted on `sys.path`. A gate-basis-only rerun with `python3 -I` gave the same results.
  - A second full `-I` run was started, then abandoned as redundant; its results are not used.
  - Base results, all with zero invariant failures: transformation-review/acceptance/gate 1,856,368 scenarios; equivalence-chain 299,760; completeness-cover 37,600; plan-coverage 205,800; gate-basis 1,000.
  - All 34 mutations are caught. `plan_supersession_current_only` is caught by I4 only, `frame_acts_everywhere` by I5 only, `obligation_direct_only` by I8 only, and `eligibility_support_tier_only` and `challenged_record_authors` by I7 only.
  - I did not call `main()` itself; the driver calls the same functions in the same configuration.
- Governing owners read at `aaeaf8b`:
  - `source/roles/software-design/SKILL.md` (routing, D3 design contract, Independent Review and Challenge);
  - `architecture-and-design.md` ("D3 formal-contract discipline");
  - `workflow-and-workplans.md` ("Authority lifecycle, mutation, and impact closure"; "Evidence, stages, and impact closure");
  - `concurrency-and-orchestration.md` ("Idempotency and publication");
  - `evidence-evolution-and-dependencies.md` ("Change impact and closure");
  - `convergence-and-cycle-economy.md` ("Active simplification trigger", "Review readiness and independent review sufficiency", "Review strategy after recurrence");
  - `project-engineering-memory.md` and `testing-and-validation.md`, applied through the validator, the HAS and DS-001.
- Reviewed-workplan text read at the candidate: §6.8 step 8, §7.3, §7.4, §7.8, §15.3 (publication, fencing), §21.
- Manual sections read in full: §0.3 (R15 and neighbours), §0.4, §4, §5.2-§5.8, §5.10, §7, §8, §9, §10, §11, §13.4, §13.7, §17, §19.4-§19.8, §22, §23.6-§23.8, §29.3 (D4 rows), §31.10. The rest was read by targeted search for R15, "reopen", "drift", "re-dispatch", the latch's kinds, the fence and re-application clauses, and §31.4/§31.6's R15 cases.

Not verified:

- No production SSDS, real gate or runtime was exercised.
- B1 (b) depends on frame derivation of `JOINT_INVARIANT` for the candidate's own change. §7.5's general rule implies it and nothing excludes it, but no text says it explicitly.
- `REVALIDATE_OVERTAKEN`'s end after a keep-the-fence decision is not stated. B1 (a) holds whichever end is chosen.
- The doctrine map was checked only for rows touching the delta and B1. Earlier Reviews' per-item closures were not replayed.
- The six drift classes were applied by targeted search over the concepts named in REVIEW METHOD, not by a pairwise comparison of every concept in the Manual. Further drift outside them is possible.

## Scientific checks

Method: one pinned architecture candidate; deductive counterexamples bound to exact owner text; a family-level recheck; structural tests; and the candidate's diagnostic with its prescribed mutations. Material findings: B1 and N1-N7. None concerns a scientific observable, numerical method or realized scientific result. B1 (a)'s `AUTHOR` variant concerns which D2 authority revision SSDS records as accepted work. That is a governance consequence, not a scientific judgment.

**I produced, ran or reviewed no realized scientific results.**

Variants evaluated: one normative candidate. For B1, one decisive trajectory with two branches (keep, re-apply), three sibling classes with ten instances, and five controls, each checked against two readings of the latch's scope (total; content-only). Fourteen out-of-matrix trajectory classes (overlapping, not independent trials). One diagnostic configuration with 5 base families and 34 mutations. The criterion was to find a material counterexample, not to select a favourable result.

No accepted project D1/D2 scientific authority was relied on for a consequential judgment, so no tension search was triggered. Gaps: real-owner execution, reader adequacy and operating costs.

## Common-mode note

The reviewer is of the **Claude family**, the same family as the Manual's author and as most earlier Manual reviewers. The 3540d98, different-family b46c250, 9e5a763, a6ed164, d6734c4, e548472 and d94a293 Reviews and the Phase B Review were of the GPT family. This reviewer was engaged as a fresh-context sub-agent launched by the authoring session. It did not receive the authoring conversation, but fresh context is not epistemic independence. Shared dependencies:

- the corpus;
- the inherited workplan and handoff framing (including the handoff's drift-class diagnosis and its request to judge R15, which directed the search);
- the prior Review records, read as hypotheses;
- the Git/Python toolchain;
- the diagnostic's claim definitions and helpers.

B1 entered through the same-family 82d618c Review's recommended option 1, which R15 realized nearly verbatim. A same-family reviewer is therefore a weak check on it. A different-family check of B1 and of whichever repair is chosen is advisable.

## D4 statement

This Review authorizes **no D4**, cutover, architecture acceptance, product-scope extension or proposed default. The next steps are:

1. Put B1's options to the stakeholder (option 1 recommended), restate R15 as one rule over its class, and reconcile:
   - §8.3 step 7 (re-application, duplicate discharge);
   - §5.10 (f) and R9 (`REFUSED`);
   - §10.2 (`REVALIDATE_OVERTAKEN`, `SPEC_REVIEW`, item identity);
   - §13.7 (item-level review);
   - §19.5, §22.2-§22.3 and R4;
   - §31.4 and §31.6 (L), (O).
2. Add B1's discriminator to §31.4.
3. Consider N1-N7. N1, N3 and N4 are definitions the B1 repair will touch anyway.
4. Freeze a replacement candidate and obtain an independent Review, preferably a different-family one, before stakeholder G1 acceptance.

G2 still separately requires a reviewed shadow workplan and explicit stakeholder authorization.

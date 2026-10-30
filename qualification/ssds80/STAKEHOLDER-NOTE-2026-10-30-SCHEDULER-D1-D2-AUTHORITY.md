# SSDS Scheduler: D1/D2 Authority Before Level 3

Oct 30, 2026 · @Sam

**Before any Scheduler prediction, admission-sizing or AUTO-ranking work is designed or implemented, the workplan must establish and accept a D1 formulation and a D2 method for the predictor family, as its first stages.** The rest of the orchestrator keeps D3 as its top authority; only the Scheduler's prediction semantics need these upstream owners.

This note is addressed to whoever writes or executes the Scheduler workplan, or the parts of the SSDP 8.0 workplan that touch Scheduler state. It is a proposed planning instruction, not accepted authority: it binds once the project owner adopts it into the governing workplan.

## 1. Why the Scheduler Needs Upstream Owners

**Orchestrator Architecture 1.6.0 §11.6 already specifies a statistical predictor whose outputs gate consequential decisions, but it has no D1 or D2 owner.** Levels 0–2 (Core, Tracker, Adapters) are deterministic composition, tracking and routing, and need none.

| What §11.6 and §11.5 specify | Domain it belongs to | Why it is material |
| --- | --- | --- |
| Predicted distributions for runtime, per-ledger consumption, token categories, monetary cost | D1 estimand definitions; D2 estimators | Reservation sizing and admission depend on them; a biased estimate over- or under-admits work |
| Stage-quality completion probability, interruption probability, future repair rounds | D1 (what outcome counts); D2 (estimator, calibration) | "Quality completion" must mean canonical PASS, not agent PASS (SSDP 8.0 §19); the probabilities drive AUTO ranking |
| Interpretable priors by stage/role × model × effort × backend, project corrections | D2 | The prior structure and pooling rule set small-sample behavior, which is the normal regime early on |
| Empirical quantiles, EWMA, shrinkage, persisted calibration | D2 | Window, half-life and shrinkage strength decide how fast the predictor tracks model and pricing changes |
| Reservations of predicted capacity, uncertainty holds | D2 sizing rule, D3 mechanism | Which quantile is reserved determines the risk of exhausting quota mid-run |
| Protected future Review/Design reserve | D1 objective, D2 sizing | A miscalibrated predictor can starve Review capacity, which undermines independent falsification |
| Ranking over quality, interruption, capacity, cost, latency, diversity | D1 decision objective | The architecture forbids collapsing incompatible metrics into one scalar without a validated design; the ranking rule is exactly that design |

The existing architecture is consistent with this split: it says ordinary predictor churn does not reopen the parent architecture. That holds only if the predictor's semantics have their own owner.

## 2. Workplan Ordering

**The Scheduler workplan opens with two upstream stages, D1 then D2, each gated by ratification; only then do Scheduler D3 decisions and code proceed.** These stages run alongside SSDP 8.0 Phase B rather than blocking it.

&#91;embedded content: workplan ordering · four Scheduler stages beside the Protocol 8 phases\]

Required placement in the workplan:

1. **A first section, "Upstream authority stages",** ahead of the D3 obligations. It lists Stage 1 (D1 formulation, Section 3 below) and Stage 2 (D2 method, Section 4), each recorded with the change-plan template (`source/shared/templates/abstraction_concretization_change_plan_template.md`).
2. **A hard gate:** no Scheduler D3 decision that fixes a prediction-dependent rule, and no Scheduler implementation, before the D2 method is accepted. Stage 3 reconciles Architecture §11.4–§11.6 with the D2 handoff; Stage 4 implements it.
3. **No blocking of Phase B.** The SSDP 8.0 D3 reassessment may close Scheduler ownership, API and observation-boundary obligations (§30 items 1, 2, 13) without D1/D2, because predictions reach the reducer only as recorded observations (§12.2).
4. **If the Scheduler is inside the Protocol 8 cutover,** add accepted D1/D2 as a Phase G prerequisite for resource-governed runs, and add a §30 item: "Scheduler prediction semantics are owned by accepted D1/D2 authority; D3 encodes no predictor property beyond the D2 handoff."
5. **Implementation handoff stays not-authorized** for Scheduler work until Stages 1–3 close, consistent with the current SSDP 8.0 disposition.

## 3. D1: What the Formulation Must Define

**The D1 stage produces a short Scientific Method Paper for the predictor family** (template: `source/shared/templates/scientific_method_paper_template.md`). It defines meaning only and leaves estimators to D2.

1. **The decisions predictions serve.** Admission feasibility, reservation sizing, the protected Review/Design reserve, and AUTO ranking. For each, state what an error in each direction costs (over-admission versus needless blocking).
2. **Each estimand as a random variable.** For runtime, per-ledger consumption, token categories, cost, completion, interruption and repair rounds: the outcome, its unit, the conditioning features, and the population of runs it describes.
3. **The completion outcome.** Define "stage-quality completion" against canonical PASS after Review, not agent self-report. State how unresolved, abandoned and human-overridden runs count.
4. **Censoring and exclusions.** Interrupted runs truncate runtime and consumption; manual and unmetered routes may lack meters. State which runs are excluded, censored or imputed, and why.
5. **The ranking objective.** Which quantities are commensurable, which are constraints rather than terms in a score, and whether ranking is lexicographic, constrained, or a weighted utility. Weights themselves can stay configuration; the form of the objective is D1.
6. **Validity regime.** Non-stationarity (new model versions, pricing and quota changes), cold start, sparse cells in the stage × model × effort × backend grid. Name the conditions under which predictions must not be used and the conservative fallback.
7. **Uncertainty.** Separate outcome variability from estimation uncertainty and from drift, and say which ones reservations must cover.
8. **External adequacy.** What evidence would show the predictor is fit for its decisions: calibration of probabilities and interval coverage on later runs (a time-ordered holdout), and decision-level checks such as the Review reserve never being starved in replayed history.
9. **Inspectability (O1).** The realized record to retain (each prediction with its inputs, predictor version and the eventual outcome), the intended reader, and the routine questions ("why was this route chosen or blocked?"). Mark whether exposing these is within the requested deliverable; "persist calibration" in §11.6 suggests at least the record is.

The D1 paper must not prescribe estimators, window lengths or quantiles; those belong to D2.

## 4. D2: What the Method Must Define

**The D2 stage produces a Numerical & Algorithmic Method Paper that concretizes the accepted D1 estimands** (template: `source/shared/templates/numerical_algorithmic_method_paper_template.md`). It must be specific enough that two implementations cannot both conform while sizing reservations differently.

1. **Distribution representation** for each estimand: a fixed set of quantiles, a parametric family, or empirical samples, and the domain of each (non-negative, bounded probability).
2. **Prior structure and pooling.** How priors are set per stage/role × model × effort × backend cell, how sparse cells borrow from neighbors, and the shrinkage rule toward pooled estimates, with its strength as a governed parameter.
3. **Update rule.** EWMA half-life or window, quantile estimator, and how observations are ordered; updates must be deterministic given the recorded observation sequence.
4. **Censoring treatment** consistent with D1: how truncated runtime or consumption from interrupted runs enters the estimates.
5. **Reservation and hold sizing.** Which quantile, or what rule, sizes a reservation per ledger; how uncertainty holds are sized after a crash before the authoritative post-meter; and how the dependence between runtime and consumption is handled.
6. **Calibration.** The calibration procedure, its schedule, the metric and threshold that count as calibrated (for example interval coverage within a stated band; a proper score for probabilities), and what happens when calibration fails.
7. **Drift and reset.** How model-version, pricing or quota changes are detected, and which estimates reset to priors.
8. **Failure and fallback regimes.** Cold start, empty cells, stale data, missing meters. The fallback must be conservative and must defer to live meters and hard limits, which already outrank predictions (Architecture §11.5).
9. **Oracles and evidence,** defined before tuning: synthetic generators with known distributions, recovery and calibration tests, metamorphic checks (adding runs from an unrelated cell leaves a cell's estimate unchanged except through declared pooling), and a time-ordered holdout on real history.
10. **Governed defaults.** Every numeric parameter (half-life, shrinkage strength, reserve quantile, calibration band) is listed as family, instance and default, with its owning layer.

State numerical precision as "none material" unless a parameter makes it otherwise; the risk here is statistical, not floating-point.

## 5. What Stays in D3

**D3 keeps ownership, interfaces, persistence and the observation boundary; it must not encode any property of the predictor that D2 has not accepted.**

D3 may decide now, without waiting for D1/D2:

- Scheduler ownership and dependency direction relative to the reducer, Adapter, Core and Tracker (SSDP 8.0 §4, §30 items 1, 2 and 13);
- the `SchedulerAPI` surface (`predict`, `preview`, `admit`, `release`, `reconcile`) as typed boundaries;
- that every prediction and admission result reaches the reducer only as a recorded, provenance-bearing observation (SSDP 8.0 §12.2), carrying the predictor version and inputs;
- that live meters and hard limits outrank predictions, and feasibility precedes ranking (Architecture §11.5, §11.6);
- persistence of predictions and outcomes in Scheduler's namespaced Tracker tables (Architecture §11.7).

D3 must wait for the accepted D2 handoff before fixing:

- any reservation quantile, hold size, calibration threshold or reset rule;
- the shape of `UsagePrediction` beyond what the accepted distribution representation requires;
- the ranking rule's form, which follows the D1 objective.

If the D2 handoff cannot be satisfied inside the current Scheduler boundary, raise it against D3 rather than working around it in implementation.

## 6. Acceptance and Evidence

**Each upstream stage stays proposed until independent falsification and human ratification complete; agents may draft and check but may not self-accept.**

| Stage | Exit condition | Human gate | Evidence available at exit |
| --- | --- | --- | --- |
| D1 formulation | Independent review finds no unresolved Serious Challenge; every estimand, outcome and objective is defined before use | Project owner ratifies the decision objective and completion outcome | Definitions and a pre-declared adequacy plan; real calibration data may not exist yet |
| D2 method | Independent review attempts counterexamples (biased small-sample behavior, censoring errors, reserve starvation); oracles defined before tuning | Project owner ratifies reserve sizing and fallback, since they change admission guarantees | Synthetic recovery and calibration tests pass; time-ordered holdout on real history where it exists |
| D3 Scheduler reconciliation | Scheduler sections of the Architecture Manual consume the D2 handoff with no added predictor assumptions | Per the SSDP 8.0 D3 acceptance process | Ownership and observation-boundary checks |
| D4 implementation | Conformance to D2 on the defined oracles, plus replay tests that reuse recorded predictions | Per the normal implementation Review | Executed tests bound to the exact predictor version |

**Provisional acceptance is expected.** Before enough real runs exist, D1 and D2 can be accepted as provisional with a stated evidence trigger, for example re-evaluation after a declared number of completed runs per active cell. Until then, reservations use the conservative fallback.

**Variant disclosure.** When priors, half-lives or shrinkage strengths are tuned on real history, record how many variants were tried, the selection criterion, and whether held-out runs were reused. A setting chosen after seeing outcomes is reported as selected, not pre-specified.

## 7. Scope Limits and Open Questions

**This note adds two upstream stages for the Scheduler predictor and changes nothing else.** It does not alter Levels 0–2, the workflow reducer, the Scheduler's subordination to workflow intent, or the rule against combining incompatible benchmark metrics into one score. It does not make the Scheduler a workflow authority, and it does not reopen Architecture 1.6.0 beyond the Scheduler prediction, reservation and ranking sections.

Questions for the project owner before the workplan is revised:

- [ ] **Is the Scheduler inside the Protocol 8 cutover, or a later module?** If later, the D1/D2 stages gate only the Scheduler workplan, and SSDP 8.0 Phases C–G proceed without them. If inside, the Phase G cutover criteria should name accepted D1/D2 as a prerequisite for resource-governed runs.
- [ ] **Can the first Scheduler release drop completion and interruption probabilities?** Resource predictions alone (runtime, consumption, cost) would shrink both papers substantially; quality-aware ranking could follow once completion outcomes are defined and data exists.
- [ ] **Where do the two papers live?** Proposed: `orchestrator/docs/scheduler-prediction-formulation.md` (D1) and `orchestrator/docs/scheduler-prediction-method.md` (D2), referenced from the Architecture Manual's Scheduler section.
- [ ] **What run history may be used, with permission, for calibration and the holdout?** Its size decides how long acceptance stays provisional.
- [ ] **Who ratifies?** The note assumes the project owner for both human gates.

## Sources

Repository `hjin98/scientific-software-development-system`, commit `af0455753e20ee54a969c844872e29e270007211` (12 October 2026):

- [orchestrator/docs/architecture.md](https://github.com/hjin98/scientific-software-development-system/blob/af0455753e20ee54a969c844872e29e270007211/orchestrator/docs/architecture.md): Architecture 1.6.0, §2 invariants 8–10, §11.1–§11.8
- [workplans/active/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md](https://github.com/hjin98/scientific-software-development-system/blob/af0455753e20ee54a969c844872e29e270007211/workplans/active/SSDP-8.0-DETERMINISTIC-CONTROL-PLANE-AND-MANDATORY-ORCHESTRATOR-CONSOLIDATED.md): §3, §4, §12.2, §19, §20, §29, §30
- [source/shared/templates](https://github.com/hjin98/scientific-software-development-system/tree/af0455753e20ee54a969c844872e29e270007211/source/shared/templates): method paper and change-plan templates

Domain definitions follow the SSDP 7.2.1 `scientific-formulation`, `numerical-algorithm-design` and `software-design` skills.

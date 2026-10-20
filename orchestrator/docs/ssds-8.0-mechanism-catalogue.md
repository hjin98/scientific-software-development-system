---
kind: ssds-mechanism-catalogue
catalogue_id: SSDS-8.0-MECHANISM-CATALOGUE
status: proposed-non-authoritative
protocol_version: 7.2.1
target_system_version: 8.0.0
architecture_manual: orchestrator/docs/ssds-8.0-architecture.md
governing_workplan: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
governing_workplan_design_revision: 24
level_split: SD-47 (qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md item 43)
body_source: orchestrator/docs/ssds-8.0-architecture.md at 94316298ba0d40831560591c2d2385544b93ea42 (Manual candidate 61), Parts 0-X verbatim
consumer: the G2 shadow D3->D4 workplan (workplan §25 criterion 13)
d4: not-authorized
---

# SSDS 8 Mechanism Catalogue

```text
STATUS: PROPOSED MECHANISM MATERIAL. NON-AUTHORITATIVE. Binds no implementation. SSDS 8 D4 is NOT AUTHORIZED.
OWNER OF THE ARCHITECTURE: the SSDS 8 Architecture Manual (orchestrator/docs/ssds-8.0-architecture.md).
CONSUMER: the G2 shadow D3->D4 workplan, which accepts, replaces or drops each mechanism here against
          executable models and closes every residual-register entry (workplan §25 criterion 13).
NOT: a D4 specification, a second architecture owner, or G1 review evidence beyond realizability.
```

## C.1 What this file is and how to read it

The SSDS 8 Architecture Manual went through 61 Review rounds while it also held the exact mechanism (syntax, schemas, field lists, algorithms, validation orders, route tables, per-kind entry lists). Under SD-47 (stakeholder decision record item 43; workplan revision 24) the Manual now decides each §21 item at the architecture level, and the mechanism moved here. This file keeps that mechanism without loss, so that nothing the earlier candidates worked out is dropped, and so that the G2 workplan can test it against executable models instead of re-deriving it.

Reading rules:

1. **Body.** Part 0 to Part X below are the Manual candidate 61 text (`94316298`), verbatim. In the body, "this Manual" reads "this catalogue body", "D3 decision" reads "proposed mechanism", and a section reference `§n` is to the body. The body's front matter, title and status block are not reproduced; the Manual's are current.
2. **Correspondence.** Body §n realizes Manual §n. The Manual owns every architecture decision, invariant and authority boundary that a body clause realizes.
3. **Conflict.** Where a body clause disagrees with the Manual, the Manual governs, and the disagreement is a residual-register entry (C.2) until G2 reconciles it. A body clause never supplies a second current meaning. Known disagreements are listed in C.2; an unlisted one found later is added there.
4. **Status of choices.** The body's stakeholder decisions SD-36 to SD-45 and its refinements R1-R15 are the current proposed realization. SD-47 keeps them as material, not as accepted mechanism: G2 may keep, replace or drop each, against an executable model, provided the Manual's decisions and invariants hold. A choice the stakeholder made at the architecture level is carried into the Manual and keeps its force there.
5. **Evidence.** `qualification/ssds80/judgment_disagreement_model_check.py` and `qualification/ssds80/item_review_history_probe.py` are diagnostics of this mechanism, not adequacy evidence (DS-001). The 61 Manual Review records in `qualification/ssds80/` are G2 input: every mechanism-level finding not closed at the architecture level is to be replayed against the executable models (register entry RR-9).

## C.2 Residual register

Each entry is a known open question about a mechanism here. It is closed only under workplan §25 criterion 13, against an executable model, at the same no-blocker bar a G1 blocker meets. An entry that turns out to show a Manual invariant unrealizable, an architectural contradiction or an inadequate Manual decision is not a register entry: it reopens G1 (workplan §25 criterion 11).

| # | Entry | Source | Manual owner | Discriminator required at G2 |
|---|---|---|---|---|
| RR-1 | **Item-level review judged content.** Body §4.3 and §13.7 name the parts' latest integrated changes as the item-level review's output entries, so an output kept by an empty or partial re-dispatch, by a part a re-partition replaced after it integrated, or by a copy under the same prose and fixed fields loses its producer from the independence test. The Manual's one judged-content rule (§5.10) covers all of the item revision's work in its write scope at the integrated result. | `MANUAL-REVIEW-SSDS-8.0-9431629-DIFFERENT-FAMILY-NO-PASS.md` B1 (a)-(d); the SD-46 history diagnostic (re-partition, copy) | §5.10, §13 | item-level entries and reviewer exclusion derived from integration histories: empty, partial and all-empty re-dispatch; kept part after re-partition; replaced part; copy; repaired content (its earlier producer not excluded); a same-key item in another scope (its producer not excluded). `item_review_history_probe.py` is a seed |
| RR-2 | **Transformation judged scope.** Body §5.10 (a) defines `J` over `Δ(X) ∪ U_X`, with `U_X` every unit any same-key enactment changed, in any scope, recorded in the task envelope at issue (`retained`), checked at Admission step 2, and protected at integration by `STALE_RETAINED` (step 7). The Manual's rule reads the work's content in the task's write scope at the candidate, a fact of `id(X)`; whether the envelope field, the step-2 check and the step-7 refusal remain needed, or reduce to the transformation's own identity and the existing rebase staleness, is open. | SD-42 to SD-45; 9431629 N3 | §5.10, §8 | reach, relief and independence over the scoped judged content on the review-scope cases, plus same-key integrations in and outside the scope between issue and integration; and (f044820 register note) two producing tasks proposing the same `(B, C, A)` with different scopes or work histories, which must resolve to one producing context or be prevented from reuse |
| RR-3 | **Review target typing.** Body §3.4 lists `REVIEW` targets as a transformation or a subject triple; body §13.7 adds an item revision's integrated result; body §4.3's row is headed "on `X`" and says its output entries carry `J` for reviews §5.10 (a) gives no `J`; a joint-invariant or high-consequence review's target collides with the transformation's own review. The Manual fixes three target types (§3). | 9431629 N2; e810508 N4 | §3, §5.10 | a target schema with distinct identities per type, and the reach, answer and `REFUSED` rules per type |
| RR-4 | Routing residual (a): an item obligation's identity under an R2 amendment that leaves its prose and fixed fields unchanged. | SD-41; body §32.3 | §10 | real-owner routing replay (body §31.5) |
| RR-5 | Routing residual (b): a spent-budget or out-of-scope `COORDINATE(plan)` answered by an identity-keeping amendment, after which no route is derived. | SD-41 | §10, §15 | as RR-4 |
| RR-6 | Routing residual (c): an item-level review whose findings name no part. | SD-41 | §10, §13 | as RR-4 |
| RR-7 | Routing residual (d): a pending candidate that never ends. | SD-41 | §10 | as RR-4 |
| RR-8 | Routing residual (e): an out-of-scope NO-PASS on a non-latest integrated enactment, or on the latest while a pending candidate masks it. | SD-43 | §10, §29 | as RR-4 |
| RR-9 | **Historical findings.** The B and N findings of the 61 Manual Review records that concern mechanism and were not closed at the architecture level have not been replayed one by one. | 9431629 N4 | — | replay each against the executable models; a finding that bears on a Manual decision is routed to G1 |
| RR-10 | **Diagnostic construction.** `judgment_disagreement_model_check.py` transcribes the body rules into hand-chosen tables and shares helpers and claims with its oracle, so a green run cannot qualify a rule's adequacy (R6/R7 hold largely by construction; the routing family's section claims enter only under mutations; its core actor table treats the owner as an independent human and its invariant I4 inserts that owner as the lifting record, so it cannot show the owner exception safe or model a policy with no eligible resolver, RR-11). | 9431629 N1; b365947 N1; 47b9f77 N1 | §31 | executable models derived from the Manual's decisions and from recorded histories, independent of the rules under test |
| RR-11 | **Owner exception scope.** Body §5.10 (a) states the owner exception for every record with an independence requirement, and body §8.3 step 3 and §6.8 read it so; the Manual narrows it to an authenticated owner's disposition of a failing assessment and makes an obligation with no eligible independent judge wait on human attention (SD-48). | `MANUAL-REVIEW-SSDS-8.0-F044820-DIFFERENT-FAMILY-NO-PASS.md` B1 | §5.10, §10.3 | with known authorship and a policy naming no qualified outside human: the content author cannot satisfy or relieve a transformation review, a subject-triple review, an item-level or joint-invariant review, a conformance or a plan acceptance as independent; the owner's disposition of a failing assessment is admitted with its class and common-mode record; a non-author human and an unknown-lineage agent behave as before; the waiting obligation derives human attention; and (8c1f2f2 register note) a standing objection whose only qualified resolvers authored the content keeps vetoing a current independent pass, is shown waiting on the named missing judge with human attention (Manual §5.10 (h)(4), SD-49), and is relieved by ordinary exact-target relief once policy names a non-author resolver |

Costs the body discloses (same-key coupling, `STALE_RETAINED` serialization, independence breadth, re-dispatch churn) are measurement items at G3 (Manual §31), not register entries.

## Part 0. Orientation

### 0.1 Authority and binding

| Question | Answer |
|---|---|
| What does this Manual own once accepted? | Every material current architecture claim about SSDS 8 for SSDS-governed scopes. Each such claim has exactly one statement here. |
| What does it not own? | Scientific meaning (D1), numerical-method meaning (D2), D4 code, SSDP doctrine, project policy values, release identities (`PROTOCOL-RELEASE-STATE.yaml`), and the behavior of the frozen Level 0 Core for version-bound work (§26.4). |
| What happens to the workplan's contract sections on acceptance? | Workplan §1.4, §2 and §5-§26 are superseded as the statement of current architecture by this Manual. They stay the reviewed cycle record. Where this Manual refines them, §0.3 lists each refinement; there is no other intended difference. |
| What does acceptance require? | G1: workplan §25 criteria 1-8, 11 and 12. Criterion 2 is this Manual resolving every §21 item; `qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md` is the review aid that maps each item to its section. The map is not a second owner. |
| What does acceptance not do? | It authorizes no D4. Shadow implementation needs G2 (a reviewed shadow D3->D4 workplan derived from this Manual, and explicit stakeholder authorization). Runtime acceptance is G3; native authority over a subject is G4 for that subject. |

**Normative language.** "Must", "never" and "only" state architecture. A section marked **[D3 decision]** fixes a choice the workplan left to the Manual. A clause marked **[delegated]** names a choice left to D4 within the stated contract; D4 may choose any concretization that meets it. Formulas are normative where they appear in code blocks introduced as definitions; examples are not.

**Decision status.** Every [D3 decision] here is a proposal until G1. A decision marked **[proposed default]** is a parameter value the stakeholder may change at G1 or later through the owning lifecycle record without reopening the architecture.

### 0.2 Architecture in one page

SSDS 8 coordinates reasoning agents and humans over evolving scientific software. Wherever an answer is mechanically decidable it is answered mechanically; where machinery can answer only conservatively it over-approximates and a recorded judgment narrows; a judgment already made is reused while its basis holds.

Four primitives carry everything:

1. **Unit** — a governed region of repository content with a stable identity and a content-addressed revision. Leaf units partition the governed content. Composite units group leaves into one acceptance **subject**. Structure takes effect only as admitted (§1).
2. **Relation** — a typed, directed fact between units with a closed semantic role and cycle class (§2).
3. **Record** — an immutable entry in one append-only ledger: a judgment, an observation, an admission or a lifecycle record (§3).
4. **Basis** — the exact typed set of unit revisions and records a record relied on (§4).

Everything else — validity, currency, obligations, readiness, impact, context, conformance, routing, briefs, views — is a pure, stratified **derivation** over the ledger and the content its records name (§5-§7). One **Admission** component is the sole ledger writer (§8). The ledger is an authenticated Git commit chain on one authoritative ref, appended by single-ref compare-and-swap, admitted only when a witness quorum holds the new head, and published to the product integration ref as an effect whose outcome the next entry records (§21-§23). A known loss of admitted history is a ledger fact that withholds every retained permissive effect until requalified or accountably attested (§23.6).

Agents act in typed **workflow roles** whose authority Admission enforces from authenticated task envelopes, never from instruction text. Each plan item carries a machine-readable **work contract**; **conformance verification** is a derived classification that can reject, return or point but never pass what a judgment must pass; every report that can change what happens next is a typed record routed deterministically, and material findings reach the human through obligations no agent can close (§10-§16).

Six separations carry the design:

| Separation | Rule | Failure class it excludes |
|---|---|---|
| observed repository state vs admitted governance state | content proposes; admitted records enact (§1.6, §8) | authority, routing or acceptance arising from repository presence, foreign pushes, restores or merges |
| definitional vs warrant dependency | cycles legal only among definitional edges inside a declared simultaneous-definition group (§2.4) | circular warrant, authority, evidence, provenance or lineage |
| appended vs current-qualified ledger state | only quorum-witnessed heads are asserted current (§23) | a historical prefix or unwitnessed append presented as current |
| retained vs known-lost admitted history | a recorded loss boundary withholds pre-loss permissive effects (§23.6) | authority reviving across lost history, even after a stale-consistent restore |
| authority envelope vs instruction | Admission checks role, write scope and record kinds against the signed task envelope (§12) | an agent mutating plans, contracts, verifiers or out-of-scope content because a prompt was misread or absent |
| mechanical conformance vs semantic acceptance | verification is necessary, never sufficient (§14) | a passing check or an agent's own claim standing in for a reviewer's judgment |

### 0.3 Refinements of the reviewed workplan

The Phase B Review passed workplan revision 23. This Manual resolves the §21 items that revision delegated to it. The following clauses go beyond filling a delegated detail: each narrows or makes explicit a reviewed contract. None adds a persistent record kind, latch or exception to the assessment-disagreement family; each is listed so that Review can check it rather than find it.

| # | Reviewed contract (workplan) | This Manual | Why; property preserved |
|---|---|---|---|
| R1 | §6.6 `on`, the clause "standing (permissive use only)", and "a passing realization's currency reads the same execution basis" | The execution basis is recorded **once**, at realization, at the reviewed granularity: the declared scope terms of every unit the closure reached with the content identities of their resolved regions, observed reads as whole-file entries, a widened directory or the whole tree (every tracked path) only where no completeness judgment bounds the closure; observed reads never bound it, external pins, and the value of every execution attribute its runner class records (environment components, backend, precision, device and host or hardware attributes, §17.5); the record also carries its **resolution context** by value (the system ruleset, so the system version, the `ignore` patterns and the analyzer set in force where its terms were hashed), and every scope-term resolver is a pure function of file bytes (§6.3). Realization currency, both matching predicates, conditions (1)-(4), the floor and the class rule all read that one record (§6.5, §6.8, §17.2). One construction rule governs both predicates: `on⁻` (adverse use) compares only the tree-resident recorded terms, re-resolved and hashed in `K` under the record's own resolution context (its system version, `ignore` patterns and analyzer set), so it is a function of the record and `K`'s bytes alone and reads no S2 value and no input outside the tree; every other dimension is stated as a class, never a list: whatever can distinguish two executions of one configuration without being tree-resident recorded content (every external input, and every recorded execution attribute the specification leaves free), and whatever bounds the recorded basis (a current bounding completeness judgment), appears only in `on⁺` (permissive use), which is `on⁻` conjoined with "no unpinnable read, the failing realization's complete set of external locators with the same pins (SD-23), and its value for every recorded execution attribute", and "a bounded basis whose every bounding completeness judgment holds for the content matched" (§6.5 as amended by SD-58; an `UNBOUNDED` basis serves no permissive use). Each use site of §6.6 names which it uses. Runner classes declare the execution attributes they record and whether they observe every read outside the tree; a free seed is a recorded attribute, and an execution whose class does not observe such reads counts as having an unpinnable read (SD-18); variation in an attribute no runner class records is a disclosed residual (§17.5, §32.2) | SD-11, SD-12, SD-13, SD-15, SD-17, SD-18: `on⁺ ⇒ on⁻` holds by construction, so losing completeness or changing structure, `ignore` or an analyzer can only narrow permissive matches and never removes an adverse recorded match; for a bounded basis the granularity is the reviewed `on`'s, so a change outside the recorded regions (another span of the same file, another unit's file, an ignored file) changes neither predicate, while an unbounded basis records the whole tree and serves no permissive use, every unfixed external input and every free recorded execution attribute (backend, precision, environment, hardware, seed) is execution variation adversely and a difference permissively, an input the runner cannot observe fails closed as the reviewed contract requires, so a run that differs from the failing one only there neither reproduces it nor shows it not yielded, one representation serves every consumer, and the class statement leaves no named dimension for a later one to escape, the surface on which the matching clause kept recurring |
| R2 | §6.6 support-graph cycle clause ("evaluates to `F` and raises a finding") | Before any value is presented, every non-trivial strongly connected component of the instantiated support graph is forced to `F` as a whole, then the rest is evaluated (§5.6) | The promised `F` is applied explicitly, not left to whatever a permissive provisional value would give |
| R3 | §6.6 "derivation is defined for every authenticated prefix"; integrity defects "raise an obligation" | An authenticated entry that violates the closed schema, the entry-shape rule or a record kind's syntactic constraints puts every position at or after it into `INTEGRITY_HALT`: no current assertion, Admission halted, recovery only by a human-gated lifecycle record (§5.7) | Fail-closed handling of corrupt prefixes before any current assertion |
| R4 | §15.3 publisher's durable write-ahead attempt log; intactness left to the Manual | The publisher of entry `n` is the Admission **process incarnation** that appended `n`, identified in the entry. Only that incarnation, in that incarnation's lifetime, may perform `B_n -> C_n`; any restart, other process or other host fences. No durable attempt log exists (§22.3) | Removes the intactness problem instead of specifying it: an in-memory "I have not attempted" is exact within one incarnation. Preserves at-most-once execution and decision-after-settlement; costs a fence (and its human decision) after a crash inside the publication window; the fence restores `tree(B_n)`, so every `NATIVE` D1/D2 subject `n` changed is back at its earlier revision in a new run (§10.2) and needs a new revising review, acceptance and gate whichever way the human decides, and re-applying `n` is a new enactment needing them again for `n`'s revision (R12); the same holds for an `OVERTAKEN` admission |
| R5 | §6.1 coverage partition "checked at every admission" | Partition holds by construction for every tree: siblings are statically disjoint by declaration, each byte belongs to the innermost declared region containing it, and every composite owns an implicit residual part (§1.4) | Foreign bytes can no longer create overlapping leaves, so no S0 case is left undefined; equal or partially overlapping dynamic regions of units not nested by membership resolve to `ABSENT`, in one pass |
| R6 | §6.1 `scope_id` "identifies the set of regions independently of their bytes" | `scope_id(s)` is the hash of the scope expression declared on the subject itself; parts must partition it (§1.5) | Byte-preserving refinement keeps `scope_id`, revision and tenure exactly as the workplan requires |
| R7 | §6.2 vocabulary listed `CHALLENGES` only as a record-level relation | An authored `CHALLENGES` type (role `EVIDENTIAL`, never a validity or warrant prerequisite) lets an in-repository tension home bind its implicated authorities with inquiry status (§2.2); it is excluded from cycle legality and well-formedness (§2.4-§2.5) | 7.2.1 tension binding and inquiry status on `CHALLENGES`; it can affect no subject's validity, so it adds no S2 input |
| R8 | §6.8 step 3: "a record may name `x` in `supersedes` only as `x`'s own assessor's reassessment or the owner's adjudication" (stated for assessments, read literally for every kind) | Supersession authority by the kind of `x`: reports by their raiser; consultations by Admission's mandatory supersession; coordination records by the principal of the same plan; every other support-tier record, assessments included, only by its own author's reassessment or the owner's adjudication on the same target, the exact thing judged (for a `GATE_DECISION`, the gate and subject triple in any run, so a gate veto that reaches across runs can be lifted where it bites); a transformation review's veto, which reaches other item revisions and bases, is lifted per reached target by its author's or the owner's own passing judgment of that target (§5.10 `relieved`), never by supersession across targets; challenge-tier, observation, admission and lifecycle records never (§8.3 step 3) | Reconciles the workplan's own §7.9 raiser supersession, §11.4 consultation supersession and §13.7 re-partition with step 3. Every judgment kind keeps the reviewed assessment rule; there is no peer supersession |
| R9 | §7.4 discharge ("∃ current judgment … with outcome in passing(o)"); iteration counting; the workflow owner's "cannot erase unresolved contradictory material evidence by vote" | Every task ends in exactly one `TASK_RESULT` carrying its slots, reviewer and principal tasks included, and that result counts its iteration; result-only `HARD` templates run at admission, and a passing judgment submitted with a non-clean result is refused (§8.3 step 7). A judgment obligation is answered by its first judgment acting in the state (§5.2) and is never dispatched again; one answered on a target carrying a standing adverse judgment is `REFUSED`, a fourth discharge value (§10.3-§10.4). An **adverse judgment** (§5.10) is never-lost and, while it stands, vetoes every passing judgment of its kind on the same target, whatever their order; it stops standing only through its own author's reassessment (a human's; an agent's task has ended), the owner's adjudication, or an upheld challenge (§5.10), each counting only if independent (`nonind` false for a judgment, admission for an adjudication, as the reviewed rule requires of an assessment's dispositions), and only in the states where that record acts (§5.2; SD-25). For a transformation's `REVIEW` and `CONFORMANCE`, whose veto reaches other item revisions and bases, the author or the owner lifts it per reached target by passing that target (`relieved`, §5.10). Changed judged content or a new subject revision is a new target, which the adverse judgment does not reach unless its judged scope still contains the rejected content (an amendment of the item revision with unchanged judged content is reached, and so is a re-dispatch keeping the rejected content, §5.10 (a), SD-42); the re-review brief carries the earlier unresolved findings (§16.5). A passing and an adverse judgment on one target derive the owner's adjudication obligation (§10.2) | A review or acceptance disagreement is never resolved by re-dispatch, count or order. Applies the reviewed assessment rule (a failure counts by existence until disposed of) to every judgment kind with an adverse outcome, on that judgment's exact target. The veto reads only S0/S1 facts, so S2 stays monotone |
| R10 | §2 S11: "An acceptance belongs to one subject tenure and never revives once that tenure ends; restoring old bytes or old declarations restores no validity" | Restated with its scope: across tenures no acceptance revives (a gate decision or required-kind judgment on an unchanged triple of a subject that is not `NATIVE` D1/D2 is reused, as the reviewed `valid` formula reads it; this resolves the reviewed lock "a restoration starts a tenure that excludes every earlier judgment" in favour of that formula); within one tenure a subject that is not a `NATIVE` subject of kind D1 or D2 has its acceptance reused by content identity (the reviewed early cutoff), while a `NATIVE` subject of kind D1 or D2 has its acceptance and gate decision current only within the revision run in which they were made, a run identified by the event that started it (§10.2), so restoring an earlier revision's bytes restores no D1/D2 validity and derives a new revising review, acceptance and gate (SD-21, SD-22) | The reviewed clause had been dropped from §0.4 without a listing; it is restored, and its within-tenure meaning stated per kind |
| R11 | §7.4 discharge: "every human gate of o is discharged by a current authenticated human judgment" | A gate `ACCEPT` requires `adequacy = ADEQUATE`; the gate term is the minimum over every eligible unsuperseded passing decision, each capped at `P` when `QUALIFIED`, so a qualification lifts only when its own decision is superseded (`gterm`, `unq`, §5.5, §10.4; SD-24) | A human's bounded, qualified decision stays visibly provisional instead of closing as unqualified, without a second qualification state; reuses the existing `P` value, supersession and provisional-continuation rules |
| R12 | §6.9 rule 1 ("`k` integrates a transformation produced for the same bound obligation as `X_0` …: `X_0` itself, a later iteration or a rebase") and §6.9's "a `record` entry on a record of a different transformation is satisfied only if that record's basis holds in this frame" | The unit of enactment is the transformation of one producing task together with its clean rebases (§5.2). A record acts, and so supports, supersedes, relieves a veto, disposes, answers or belongs to a run, only in the admitted state, in the frames of its own enactment, and in admitted states after that enactment integrates (§5.2, §7.3, §7.5). A prospective acceptance counts only for its own enactment's integration (§7.6 rule 1); a later iteration records its own; a record in another pending enactment's frame supports nothing; an enactment integrates at most once, so the re-application of an `OVERTAKEN` or fenced admission (workplan §15.3) is a new task and enactment (§22.2-§22.3). A gate `REJECT` still vetoes the same gate and subject triple in every run (§5.10), so a replacement enactment never escapes it. A revision run is identified by the event that starts it, an integration by its enactment (§10.2) | SD-25, SD-26: a frame record could otherwise take effect in a state that never contained its grounds (an abandoned candidate, a rejected iteration replaced by another, a partition sibling), lifting a veto or a qualification or reviving an earlier run's acceptance. Withholds support and narrows liveness: a fresh acceptance and gate per replacement iteration and per re-applied admission, the gate core showing earlier identical-content decisions (§16.6, §32.3). The cross-run reach of a gate `REJECT` and the matching supersession target are R8's and R9's (§5.10) |
| R13 | §5.3/§6.1 challenge tier: "**Judgment** (challenge tier) \| qualified actors per policy \| … adjudication …"; §6.6 `valid`/`ACC`, which read no independence fact; §6.6's unknown-authorship rule, stated for dispositions | Every `ADJUDICATION` is admitted only if independent of the authors of its challenge chain's root content and of a class not lower than the highest in the chain, or it is refused (§8.3 step 3); a support-tier judgment of a kind with an independence requirement supports nothing if admitted as non-independent (`nonind`, read in `base`, §5.10); independence is measured against one function `authors(x)`, the unknown-authorship rule applies to every record with a requirement, curable by `NON_AUTHORSHIP_ATTESTATION` (§3.4), and machinery records and imports carry none (§5.10 (a)); every non-machinery `EQUIVALENCE` and `COMPLETENESS` carries the requirement whatever request carries it, measured against the authors of the change it judges or of its members (SD-29) | The reviewed rule requires independence of every disposition that ends a failing assessment's dispute, and A5/A9 forbid acting on one's own work; R9 extended the veto to every judgment kind, so the same floor applies to every record that can end an objection or support a judgment, at two enforcement points instead of a list of routes. Restrictive: a non-independent adjudication is refused; a non-independent judgment is kept and supports nothing. Workplan §6.8 step 3 says "independence requirements for equivalence/completeness about the request's own change"; §6.7 says "the author of a change cannot be the sole qualifier of an equivalence or completeness judgment about that change", and A5 and the threat rows say the same. Read literally, step 3 would exempt every such judgment recorded in a later request, since integration requests carry none (§11.5); this Manual follows §6.7 and A5 (SD-29) |
| R14 | §6.6 `sat(content (u, r, k))`, "⋁ over paths r = r_0 -> … -> r_m = cur(u) of ⋀_i current(q_i) over EQUIVALENCE judgments q_i on u, class k", and its `PLAN_CONTROL` case (§7.9 tightening coverage); §6.6 `closure` by the smallest complete scope; the evidence owner's "an unresolved material disagreement keeps dependent present guidance/closure visibly qualified" | Composition is kept, and a standing objection reaches what a composition claims. **One reach rule** (§5.10 (a), SD-29): an adverse judgment vetoes every passing judgment of its kind that, alone or with other judgments of that kind asserting in the state, claims what it denies and is needed for that claim; each kind's row says what its passing judgments claim and how they compose (§5.10 (b)). Equivalences compose into every pair of revisions they connect, read in either direction, within a covering class; boundary-completeness judgments compose by union of sub-scopes (§2.6), the analyzer identity being a currency condition, not compared; a plan rejection denies the revision it names and every tighter revision, and an acceptance claims the revision it names and every tighter one (workplan §7.9), so they contradict exactly when the two revisions have the same prose and fixed fields; the current revision is not read; acceptances do not compose; only the rejecter or the owner relieves a reached acceptance (route 3, SD-30, SD-32). A judgment **asserts** exactly when `base` would leave it above `F` but for vetoes, so a `PROVISIONAL` one asserts. A vetoed hop is not current, so no path through it counts; a vetoed completeness judgment bounds no closure, which then widens to the next complete scope or the whole tree; the owner's adjudication is derived for every vetoed judgment (§5.10 (f)) | SD-28: with the veto reaching only the same endpoints, two passing hops `r0 -> r1 -> r2` restored a consumer around a standing `NOT_EQUIVALENT(r0, r2)` with no adjudication derived. SD-29: per-kind clauses still missed completeness composed by union (a standing `INCOMPLETE` on a subject's scope was bypassed by complete singleton judgments), an analyzer declaration the reach compared by its identity, and provisional hops the chain clause did not count; a plan clause reaching every tighter revision kept a correct rejection vetoing an acceptance after the rejected tightening was reverted (SD-31 restores that reach, since route 3 now lifts it with one record by the rejecter or the owner), while one reaching only the current revision let a further tightening escape a standing rejection; a path rule (`r ⊑ r* ⊑ cur`) still let an acceptance of a revision incomparable with the rejected one carry a later tightening past it. The plan row therefore states its claim (a tightening is taken to keep what was rejected, a conservative resolution policy rather than a claim about the rejection's ground, and an acceptance claims every tighter revision, workplan §7.9) and derives the reach from it; SD-31 dropped a revert exemption that let the plan's author release a standing rejection by reverting or loosening, and SD-32 replaced the remaining test that read the current revision, which still released a rejection of a revision incomparable with the accepted one after a loosening below their join, by its closed form: the two revisions have a common tightening, that is, the same prose and fixed fields; SD-33 then keyed the plan and transformation-review reaches, and both brief carries, on what was judged rather than on the plan item's identity, which a re-identification or copy of an item with byte-identical content had escaped; SD-34 then keyed the transformation-review reach on the changed-unit content alone and the plan-acceptance and re-review carries on the plan subject, because a re-identification with any amendment still escaped a key that read the item or its prose, and SD-42 on one judged scope `J` used on both sides of the comparison and for independence, because a re-dispatched review over `out(o)` that kept the rejected content escaped the changed-unit key, and SD-41's wording, reading the adverse side's changed units, made an empty transformation's objection reach every review; and, after the 653e88c Review, one statement in §5.10 (a) states which kinds are keyed on content and which on a subject or named units (S10 keeps acceptance and gate decisions on their subject), and §4.1 makes each basis entry say what it relies on (a `standing` mode for the revision-assessment record) with a route when it fails (item 31); an exemption for an acceptance of a tighter revision, whoever its judge, let a peer override a standing rejection, so judging that an amendment cured a rejection is the rejecter's or the owner's (per-target relief, SD-30). The equivalence `authors` input covers both sides of the change, since the claim and the reach are orientation-free, and `sat` hops keep their recorded direction (§4.4). Restrictive only against the reviewed text: it removes support and adds none; it reads S0 and S1 facts, so `base` stays an S2 constant and §5.6's monotonicity holds. Cost: one objection blocks every judgment a contradicting composition needs, including compositions no consumer uses and judgments whose own basis is stale, until its author, the owner or an upheld challenge ends it; an `INCOMPLETE` on a large scope widens every closure inside it; a plan rejection reaches every acceptance of a revision with the same prose and fixed fields, a fresh one and one on a control-only branch never joined with the rejected revision included, until the rejecter or the owner relieves or supersedes it or a challenge is upheld; and since `sat` hops keep their recorded direction, an independent equivalence recorded the other way, or judged before a revert for consumers on the other side, serves no path in that direction |
| R15 | §6.8 step 8: "every obligation discharged at the current head and affected by the merged tree stays discharged, with affected evidence rerun"; the workplan's "A D4 change that breaks another closure is a regression and is not admitted" | Admission step 8 reads only the evidence terms of the obligations the merged tree affects: a request that makes a passing `ev` or `qual` fail is refused (`REGRESSION`); a judgment the request's content makes non-current is not a regression, and the obligation it supported is then reopened in current state, an item obligation taking the one route §10.4 gives it, a judgment obligation never re-dispatched (§8.3 step 8, §10.4). Discharge is not latched: every obligation keeps reviewed workplan §7.4's current-state discharge (SD-36), and event-keyed judgment obligations end in current state (SD-37), with one key `out(o)` per item obligation (SD-38) and one route statement in §10.4 (SD-39), with no post-integration revalidation of an item obligation's review or task result (SD-40; acceptances and gate decisions keep their `REVALIDATE`) | Read with exact-content output entries, step 8 had refused every later item that edited a unit an earlier item changed or read, every second change in a joint invariant's scope, and a second `AUTHOR` revision. The narrowing keeps the workplan's purpose (a D4 change breaking another closure's evidence is refused). Latching enacted obligations to avoid the resulting drift re-dispatch was tried in candidates 46-51 and failed eight Reviews at successive couplings; the stakeholder withdrew it and accepted the drift re-dispatch (SD-36, stakeholder record item 32), then limited it to output changes and gave event-keyed judgment obligations a current-state end (SD-37, item 33), keyed every post-integration route on `out(o)` with an adverse revalidation as a NO-PASS iteration (SD-38, item 34), put the routes in one ordered statement (SD-39, item 35), and withdrew post-integration revalidation so every reopened integrated item is re-dispatched (SD-40, item 36) |

Every other clause restates the reviewed contract or decides a §21 item inside it. Which Review motivated each refinement, and the order in which the refinements were made, are recorded in the closure map (`qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md` §7); they are provenance, not part of this Manual's normative content. Repair directions from candidate 13 onward were chosen by the author under the stakeholder's delegation (stakeholder record item 19); the stakeholder decisions SD-11 to SD-45 are cited where they apply.

### 0.4 Governing invariants

These invariants are the parents every section below concretizes. Their sources are the accepted SSDP 7.2.1 owners, the consolidated Protocol 8 proposal and the stakeholder's SSDS objectives, as tagged in workplan §2; the tags show provenance only.

**Semantic.**
- **S1** D1-D4 semantic authority, one current owner per material normative claim, acyclic current ownership, a layered DAG rather than a waterfall; mutual definition only through an explicit simultaneous-definition declaration; no definition, definitional dependency or condensation warrants a claim; circular warrant, authority, evidence, provenance or lineage is invalid.
- **S2** Concretization fidelity and abstraction adequacy are distinct; a Serious Challenge stops counterfeit closure; a risk override leaves dependents visibly provisional.
- **S3** Authority mutation is proposal, independent falsification where required, human ratification where required, acceptance, bounded impact, reconcretization. Repository presence promotes nothing.
- **S4** Evidence is specification, realization, observation, assessment; observations are immutable and assessments supersede only explicitly; stale passing evidence never confirms and stale failing evidence never refutes; a failing assessment that counts keeps its claim qualified until a judgment addressing it, or discriminating evidence, disposes of it; binding health is tracked separately from historical existence.
- **S5** Absence of a relation establishes independence only inside a scope judged complete for that relation class.
- **S6** Specialized inference needs the exact canonical meaning; definitions establish no truth; conflicting simultaneous meanings go to their owner.
- **S7** Version-bound interpretation; no retroactive reinterpretation; no self-adoption.
- **S8** Project Engineering Memory is non-authoritative; a Historical Applicability Set is task-local.
- **S9** No machine vocabulary converts a semantic judgment into a deterministic fact; an agent PASS is a recommendation.
- **S10** Acceptance attaches to one exact semantic subject, in one tenure, at one exact scope and revision. Content identity, scope identity, subject role and tenure, lineage, dependency coverage, semantic equivalence and acceptance are distinct facts.
- **S11** Effective governance is admitted, never observed. An acceptance belongs to one subject tenure and never revives once that tenure ends; restoring old bytes or old declarations restores no validity: across tenures no acceptance revives (gate decisions and required-kind judgments on an unchanged triple of a subject that is not `NATIVE` D1/D2 are reused, R10), and within one tenure only a subject that is not a `NATIVE` subject of kind D1 or D2 has its acceptance reused by content identity (refinement R10).
- **S12** Gate evidence is decision-sufficient with a separable non-narrative core; its adequacy is a semantic judgment. A marked product inspectability surface beyond the requested deliverable is accepted only by the product-scope owner.
- **S13** A persisted finding has one canonical home; a tension's home is a project evidence record or native issue, never accepted authority text; no universal discovery database.

**Control.** **C1** one serialization point per ledger. **C2** same canonical inputs and ruleset give one derived state. **C3** time, filesystem, Git remotes, resources, model output and human judgment enter only as recorded typed records. **C4** external effects follow intent, idempotent or reconcilable effect, observed outcome; ambiguity is reconciled before retry. **C5** unknown required semantics fail closed. **C6** disagreement between semantic content and its control representation blocks dependent transitions. **C7** control data is the minimum needed to select, validate, serialize, replay or audit. **C8** the derivation is well-founded: one value per predicate for every admitted input, no self-supporting acceptance, no negation through recursion.

**Concurrency.** **K1** a result is admitted only if everything it relied on is current, or it is revalidated. **K2** no two mutating executions share a working tree. **K3** a clean textual merge is not semantic orthogonality. **K4** correctness never depends on predictions.

**Provenance and replay.** **P1** every canonical change records what, who, against which basis, under which rules. **P2** historical decisions are never recomputed under newer rules. **P3** derived state is rebuildable; canonical records win. **P4** currentness is asserted only for durably witnessed state, under the declared witness model, with no lag window. **P5** a known loss of admitted history is a continuity boundary across which retained permissive effects do not pass without requalification or accountable attestation.

**Agent interface.** **A1** routine work never requires reading machine records or reconstructing Git topology. **A2** context is version-bound, explains its inclusion, labels epistemic status and states incompleteness. **A3** one logical task/result contract across transports; a zero-context agent locates its task from a minimal bootstrap. **A4** a duty a task owes is carried in its brief or enforced mechanically; activation is deterministic; briefs carry only triggered duties. **A5** every execution acts in one role for one task, with authority checked at Admission; only a plan's principal changes its plan; no agent changes verification rules; no actor reviews or accepts its own work. **A6** facts are produced by machinery; agents supply judgment in typed slots and cite records for factual claims. **A7** verification is necessary, never sufficient; no control decision parses prose. **A8** a material finding survives to its owner; escalation is keyed on existence, never currency; only an authenticated human judgment discharges human attention. **A9** reviewer independence is constructed, not requested.

**Git.** **G1** Git is content, isolation, transport and history substrate, never workflow authority. **G2** transport artifacts are never merged into product history. **G3** no record contains the identity of the commit that contains it. **G4** secrets and private telemetry never enter project repositories. **G5** `main` is never deleted or force-moved to discard reachable history.

**Migration.** **M1** one route admits every change of unknown provenance. **M2** adoption is progressive and coexists with production. **M3** no governed region has two current authorities. **M4** discovery may run bottom-up; acceptance runs top-down. **M5** unknown stays visibly unknown. **M6** in-flight older-version work is drained, pinned or migrated.

**Trust.** **T1** agent outputs are untrusted proposals until admitted. **T2** unknown artifacts are never executed or deserialized to classify them. **T3** external, evidence and memory text is data. **T4** humans and canonical entries authenticate through a declared mechanism; nothing beyond it is claimed.

**Compatibility.** **B1** older version-bound work stays under its declared version and immutable source; frozen orchestration profiles stay independently testable (PC-001). **B2** rollback is version rollback to an immutable baseline, never dual authority. **B3** Protocol 7 inheritance is final at 7.2.1; the pre-cutover baseline is resolved from `PROTOCOL-RELEASE-STATE.yaml`.

**Allocation principle.**

```text
mechanically decidable                     -> machinery, exactly
decidable only conservatively              -> machinery, sound over-approximation, never under-approximation
precision beyond the conservative answer   -> a focused judgment that narrows it
judgment made, basis still current         -> reused mechanically
mechanically checkable conformance         -> verification: necessary, never sufficient
unresolved semantic question               -> an agent, in the role its obligation kind selects
routine coordination                       -> the principal role, recorded and challengeable
designated authority decision              -> a human gate
canonical state change                     -> single serialized Admission
```

### 0.5 Scientific inspectability (O1)

SSDS produces no scientific results of its own. It decides which realized results count as current evidence, what human gates receive and what is retained, so the 7.2.1 D3 authority-content duty applies.

- **Material realized record of SSDS.** Admitted records and their bases: judgments; evidence realizations with their execution basis and evaluated outcomes; assessments, including discriminating readings; challenges with inquiry status; gate decisions; risk overrides; loss boundaries and continuity attestations; publication outcomes; intake and quarantine dispositions; refusals with reason codes. Retention: the ledger is append-only except under the human-gated confidentiality protocol (§24). Evaluated outcomes, the trees that hold evaluated content and every commit a record names are kept reachable by the ledger (§21.4). Raw data, logs and narrative findings stay in native project homes and are referenced by content identity; an unavailable artifact degrades binding health and erases no history.
- **Intended readers.** Stakeholders and human-gate holders; independent reviewers; agents, only through rendered briefs.
- **Routine questions.** What governs this subject, at which revision? Is this result current against its basis, and if not, what moved? Which evidence supports or challenges this claim, and which is stale, disputed or unavailable? What did a gate decide, on which evidence core, with which findings and tensions visible? What is withheld by quarantine or a loss boundary, and why? What did each agent do, in which role and within which boundaries; what did verification find; and which findings were escalated, merged or downgraded, by whom?
- **Product inspectability surfaces (marked).**
  - *Within the requested deliverable (this architecture):* `ask`/`read` answers naming their qualified head (§16.2); task briefs with incompleteness notices (§16.3); gate briefs led by a separable non-narrative core (§16.6); the conformance view of each result (§14.6); the inspector view and digest (§16.8); historical views at any ledger position (§5.8); `sdp ssds export`, a snapshot of the ledger and derived views at a named qualified head in canonical JSON (§26.3); the canonical-JSON ledger itself, readable with Git and a JSON reader without SSDS code or an AI (§21.2), which is the tool-independent route.
  - *Beyond the requested deliverable:* **None.** Projection of a project's own scientific records, exploration interfaces and discovery stores stay with project products. SSDS references their homes and adds no universal observation database.
- **Realized-record architecture.** Canonical source: the ledger plus the content it names. Derived projections: every view, regenerated, never edited (§5.8). Drill-down identity: record identity, unit identity plus revision, scope identity, ledger position and qualified head. Streaming and interim exposure: a long execution's progress is operator state; its realized outcome enters only as an admitted observation, and the inspector shows pending executions as pending. Restart continuity: the ledger and Git content; derived state rebuilds. Privacy and security: §24-§25; inspection and export views are trust boundaries that give the strongest safe aggregate and state the limitation.

## Part I. Primitives

### 1. Units, scopes, subjects and the manifest

#### 1.1 Unit

A **unit** `u` has a stable logical identity `id(u)`; a **kind** and owning **domain**; a **scope** (the repository regions it covers); a declaration source; and a **role**, leaf or composite. Every unit is either a **subject** (default) or a declared **part** of its enclosing composite.

**Identity grammar [D3 decision].** `id := segment ("." segment)*`, `segment := [a-z0-9][a-z0-9_-]{0,62}`, at most 255 bytes. Identities are opaque: no meaning is inferred from their text. The prefix `ssds.` is reserved for system units (§1.8). A residual part (§1.4) has the derived identity `<id>.~`, which no declaration may use.

**Kinds [D3 decision].** The kind fixes the owning domain and the acceptance contract that applies.

| Kind | Domain | Meaning |
|---|---|---|
| `D1` | D1 | scientific/mathematical formulation |
| `D2` | D2 | algorithm and numerical method |
| `D3` | D3 | software architecture |
| `D4` | D4 | specification and implementation, including tests that are not evidence specifications |
| `EVIDENCE_SPEC` | the domain of the claims it `EVIDENCES` (§2.2); acceptance by that domain's contract | an evidence specification |
| `EVIDENCE_RECORD` | none (non-authority) | an in-repository finding, tension or evidence home; never authority text (S13) |
| `PLAN` | plan | a change-plan unit (§11) |
| `GENERATED` | the domain of its generator | content reproduced by regeneration (§9.3) |
| `EXTERNAL` | external | an immutable external pin (§20) |
| `POLICY` | governance | the project policy unit; protected (§25.3) |
| `MANIFEST` | governance | the unit manifest; content edits are ordinary, effect only by admission |
| `UNCLASSIFIED` | none | content whose kind is not yet judged |

A subject's kind and domain are declared on the subject. A part inherits them; a part declaring a different kind is a static error (§1.9). A region that needs another domain must be its own (nested) subject.

#### 1.2 The unit manifest

**Location and format [D3 decision].** Structural declarations live only in the repository-owned unit manifest at the path genesis declares, default `.ssds/manifest.toml`. It is TOML 1.0, parsed by a data-only parser; parsing never instantiates objects or executes content (T2). A manifest that does not parse is, for every declaration key, a quarantined delta against `Σ` (§1.6): governance continues on `Σ`, and the parse failure is an intake obligation.

```toml
schema = 1                                    # manifest grammar version

[governed]
ignore = ["build/", "*.pyc"]                  # governed-content boundary: excluded path patterns

[[unit]]
id       = "numerics.solver"                  # identity grammar §1.1
kind     = "D2"                               # required on every subject; forbidden on parts
role     = "composite"                        # "leaf" | "composite"
subject  = true                               # default true; false declares a part
part_of  = "numerics"                         # optional: the enclosing composite (membership)
scope    = [ { file = "docs/solver.md" } ]    # ordered list of scope terms (§1.3)
renamed_from = ["numerics.method"]            # optional identity lineage

[unit.semantic]                               # semantic declarations (§1.7); part of the revision
defines   = ["solver.timestep-rule"]
relations = [ { type = "USES_DEFINITION", object = "physics.units" } ]
sdg       = [ { id = "solver-core", members = ["numerics.solver.a", "numerics.solver.b"] } ]
joint_invariants = [ { id = "flux-conservation", units = ["numerics.solver", "kernels.flux"] } ]
```

Keys other than these are a static error for the grammar version. The `[unit.semantic]` table is semantic content of that unit and is part of its revision (§1.5); every other key is structural.

**Declaration keys.** `decl(T)` is the map from **declaration key** to value parsed from tree `T`. The keys are `(id, "kind")`, `(id, "role")`, `(id, "subject")`, `(id, "part_of")`, `(id, "scope")`, `(id, "renamed_from")` for each declared `id`, and `("governed", "ignore")`. A key absent from `T` has value `⊥`. Removing a unit is the change of each of its keys to `⊥`.

**Write set [D3 decision; SD-14].** The **write set** of a request is keyed on effect and computed at the admitted head `n` where each check runs (Admission, and conformance in `D_n[X]`): it compares the current observed tree `T_n` under `Σ_n` with the merged tree `M_n(X)` under `Σ_n ⊕ Δ_Σ(X)` (§7.2), so changes admitted concurrently since the request's base never enter it, and an effect that arises only when its change meets them does. It contains every effective unit, in either structure, for which any of these differs between the two: its owned content by innermost ownership (§1.4), in the §1.5 representation: the bytes it owns by innermost ownership (§1.4), and the entry type and mode of every file a term of it resolves into, empty files and gitlinks included; any declaration key of it (§1.2: kind, role, subject, `part_of`, scope, `renamed_from`) or semantic declaration it or any of its parts carries; its resolved regions, compared by content and never by position: a region differs only when a term's resolution status changes (resolved or `ABSENT`) or bytes enter or leave it under the pinned diff alignment (§7.2), so a length-changing edit elsewhere in the file that only shifts it leaves it unchanged; its membership (its `part_of` and its members); its governance signature. A newly declared unit is in it with its effective kind (a new part with its composite's kind), a removed unit with its former kind, and a unit whose kind differs between the two structures under both. `ssds.manifest` is in it whenever the manifest's bytes change. A composite whose revision changes only because a nested subject of another kind inside its scope changed is not in it by that change (the nested subject is); its revision still changes, and its gate core says so (§16.6). The set is computed like the governance-affecting classification (§1.6), never from changed bytes or keys alone, so a change that reaches a unit only through the governed boundary, a new or moved part, or another unit's declarations still counts against it. Every write-scope check, the domain rule (§13.2) and every trigger keyed on the kind or domain of a changed unit read this write set. Identity lineage is a fold over admitted history: removing a `renamed_from` declaration never removes lineage already admitted (§1.11).

**Inline anchors [D3 decision].** An anchor only delimits a leaf span inside a file that a manifest scope term names (`anchor` term, §1.3). It never declares role, membership, kind, domain or scope. Syntax: a line whose content after the file's comment leader is `ssds:begin <name>` or `ssds:end <name>`, with `<name>` in the segment grammar. Comment leaders are fixed by file type: `<!-- … -->` for Markdown and HTML, `#` for Python, TOML, YAML and shell, `//` for C, C++ and similar, `%` for TeX. **[delegated]** The file-type table and its extension within the same rule. Anchor lines are pure structural boundary markers; they are removed from identity only where §1.5's comment classifier applies. Immutable or version-pinned artifacts are never rewritten to acquire anchors; their spans use `heading` or `symbol` terms, or whole-file scopes.

#### 1.3 Scope terms and resolution

A unit's scope is an ordered list of scope terms. **[D3 decision]** The term grammar is closed:

| Term | Denotes, in tree `T` |
|---|---|
| `{ path = "a/b.py" }` | the whole file at that exact path |
| `{ prefix = "src/solver/" }` | every governed file whose path starts with the prefix (must end in `/`, or be empty for the whole governed tree, §1.8) |
| `{ file = "f", heading = ["A", "B"] }` | in Markdown file `f`, the span from the ATX heading path `A > B` to the next heading of the same or higher level, or end of file |
| `{ file = "f", symbol = "pkg.mod.Class.method" }` | the source span of that definition, as resolved by the language analyzer of the file as a pure function of that file's bytes under the pinned analyzer identity and configuration, never reading host inputs (§14.5) |
| `{ file = "f", anchor = "name" }` | the lines strictly between the matching `ssds:begin name` and `ssds:end name` |
| `{ file = "f" }` | the whole file, used inside a composite whose parts section it |

**Resolution.** `resolve(t, T)` returns the region the term denotes in `T`'s bytes, or `ABSENT` when it does not resolve: the file is missing; the heading path, symbol or anchor does not occur; it occurs more than once; or anchors are unbalanced, crossed or nested under one name. `ABSENT` is a value, not an error: the unit's content identity records it, so a unit whose region vanishes changes revision and every reliance on it becomes non-current. An ambiguous or malformed anchor additionally raises an S3 integrity finding.

**Governed content.** The governed content of `T` is every tracked path not matched by an effective `ignore` pattern. `ignore` patterns use Git wildcard semantics (`fnmatch` with `**`), decided once by the system version.

#### 1.4 Partition by construction

**[D3 decision]** Leaves partition the governed content of every tree by construction, so no observed bytes can produce an overlap:

1. **Static sibling disjointness.** Within one composite, and among top-level units, no two units' scope terms may be nested or equal by declaration: two `prefix`/`path` terms where one is a prefix of the other; two span terms on one file where one heading path is a prefix of the other, one qualified symbol name is a prefix of the other, or the anchor names are equal; a whole-file term and any term on the same file; a `prefix` or `path` term and a span term on a file it covers. Such a declaration is a static error (§1.9). A unit that should sit inside another is declared a member of it (`part_of`), never a sibling.
2. **Containment.** Every member's terms must denote regions inside its composite's declared terms: a member `path`/`prefix` lies under a composite `prefix` or equals a composite `path`; a member span term names a file the composite covers whole or a span nested in a composite span. Static error otherwise.
3. **Innermost ownership.** A byte of governed content belongs to the innermost unit whose resolved region contains it. Resolution can still nest, cross or coincide regions dynamically (anchors moved by an edit): a region strictly nested in a sibling's is the inner owner of its bytes; two resolved regions of distinct units, neither a member (transitively) of the other, that partially overlap (neither contains the other) or are equal both resolve to `ABSENT`, as does a member region that falls outside its composite's resolved region, and each case raises an S3 integrity finding. These tests are evaluated once, over the §1.3 resolutions of every term, never over regions already set to `ABSENT`, and do not cascade: a member of a composite set to `ABSENT` keeps its own resolution unless a test applies to it directly. **Precedence.** Ownership is decided first, by this innermost rule, over every unit's region that did not resolve to `ABSENT`, whether or not the units are related by membership; the residual part and the uncovered region receive only bytes still unowned. Within a composite, bytes of the composite's regions that no other unit owns by this rule (a member, or a unit whose region resolution nested inside the composite's without membership) belong to the composite's **residual part** `<id>.~`, an implicit leaf part of that composite.
4. **Uncovered region.** Governed bytes that no unit owns by rule 3 and no residual part receives (no unit's non-`ABSENT` region contains them) belong to the reserved **uncovered region**, status `UNCLASSIFIED` (§18); this includes the bytes of a composite set to `ABSENT` that none of its surviving members owns.

So a new foreign file under a declared prefix belongs to that prefix's innermost owner; a vanished or conflicting span's bytes fall to the enclosing residual; nothing is ever owned twice. Composites form a laminar family because membership is a forest (each unit has at most one `part_of`, and membership is acyclic).

#### 1.5 Revision, content identity and scope identity

**Normalization [D3 decision].** Content identity is exact. It hashes every byte, and for every file a term resolves into, the file's Git entry type and mode (regular, executable, symbolic link, gitlink), so a binary byte change, a line-ending change, an executable-bit change or the replacement of a file by a link with the same bytes each change identity. **The representation [D3 decision].** The one representation of content, for identity and for every comparison of owned content (the write set and the diff-to-unit mapping, §1.2, §14.5; currency; matching), is the Git tree entry: its type, mode and blob bytes; a gitlink's bytes are the commit identity it records. The tree is exactly what a designated runner presents to the execution, with no exception: no end-of-line or encoding conversion, no clean, smudge, `ident` or LFS filter, no sparse or skip-worktree divergence, whatever `.gitattributes` or Git configuration say. A runner that cannot guarantee this cannot be designated (§17.5). What lies outside the tree is read as an external read: a Git LFS object is read by its pointer's object identity, its pin (§20.1); a read inside a submodule is recorded as a read entry on the gitlink's path, whose identity is the commit the tree records, so a submodule change changes it as any tracked file would; the runner materializes the submodule at exactly that commit under the same rule, recursively. Exactly one normalization applies, as the workplan requires of pure structural boundary markers, fixed by the system version and never by policy: an **anchor line** is removed only where the system version's fixed lexical **comment classifier** for the file's type classifies that line as a comment: a Python comment token, a C or C++ comment, or a Markdown line that is an HTML comment and not inside fenced or indented code. The classifier belongs to the system version, not to the analyzer set, and in a classified type anchor-term resolution (§1.3) uses the same classifier, so an anchor-looking data line neither delimits nor is removed. In a file type without a classifier, an anchor line is recognized syntactically and kept in identity, so an anchor refinement there changes the revision. Adding or moving anchor delimiters in a classified type (byte-preserving refinement, §19.3) leaves identity unchanged. Nothing else is normalized: line endings, trailing whitespace, encoding and Unicode form are content. For recognizing anchor and heading lines only, a line ends at LF and one trailing CR is ignored; identity keeps every byte. A span term in a file that is not a regular or executable file resolves to `ABSENT`. A future normalization is a system-version change (§27).

```text
cid(t, T)     = sha256( "ssds.cid.v1" ‖ term_kind ‖ term_args ‖ entry type and mode of the file
                          ‖ normalized bytes of resolve(t, T) )
                ("ABSENT" in place of the bytes when the term does not resolve; a prefix term hashes its
                 files in bytewise path order, each as path ‖ entry type and mode ‖ length ‖ bytes)
content(u, T) = sha256( "ssds.content.v1" ‖ cid(t_1, T) ‖ … ‖ cid(t_k, T) )   -- u's declared term order
sem(u, T)     = sha256( JCS( sorted semantic declarations of u and of every unit inside scope(u) ) )
rev(u, T)     = sha256( "ssds.rev.v1" ‖ content(u, T) ‖ sem(u, T) )
cur(u)        = rev(u, T_n)
```

`JCS` is RFC 8785 canonical JSON. Semantic declarations include those in manifest `[unit.semantic]` tables and inline semantic markers (§1.7) inside the unit's regions.

**Scope identity [D3 decision; refinement R6].** `scope_id(s) = sha256("ssds.scope.v1" ‖ JCS(declared terms of s))`, over the terms declared **on the subject itself**, independent of bytes and of how parts partition them. Parts must partition exactly the subject's declared terms (§1.4 rule 2 plus the residual). Byte-preserving structural refinement therefore leaves `scope_id`, `content`, `sem` (unless relations are redirected) and `rev` unchanged, which is what makes a refinement leave acceptance valid (§19.3). A change to the subject's own terms is a scope change and ends its tenure (§1.6).

Revisions are computed from Git content on demand and memoized by key (§5.9); no separate hash graph is stored.

#### 1.6 Effective structure, quarantine and tenure

**Effective structure** `Σ_n` is the map of structural declarations in force at ledger position `n`: genesis admits `Σ_0`; an ordinary or intake admission changes `Σ` exactly by the structural changes it authored or explicitly adopted (§8.3 step 4); an absorption never changes it; a governance-mode transition changes only the mode. `Σ_n` is a fold over admitted entries and the trees they name; it is never stored as a second copy. Derived from it: units, leaves, composites, residual parts, `scope_id`, `subj`, kind and domain, governed boundary, and tenure.

- `subj(u)` is `u` if `u` is a subject, else the nearest enclosing composite that is a subject; unique by laminarity.
- **Resolution** of effective scopes is against the bytes of the observed tree `T_n` (§5.2).
- **Quarantine.** `Q_n = { k : decl(T_n)[k] ≠ Σ_n[k] }`.
- **Governance-affecting classification [D3 decision: algorithm].** For each `k ∈ Q_n` compute the derived structure `Σ_n[k := decl(T_n)[k]]` on `T_n`. The delta is **governance-affecting** iff, compared with `Σ_n` on `T_n`, some unit's identity, kind, domain, role or enclosing composite differs; some subject's `scope_id`, or the set of governed byte regions it covers, differs; or the governed boundary differs. Otherwise it is **governance-neutral**: a re-partition of leaves inside one subject's unchanged regions into parts of that subject. A delta whose single-key override is statically invalid (§1.9) is governance-affecting. The classification is fixed by the system version, never by policy.
- **Affected subjects.** `aff(Q_n)` compares `Σ_n` with `Σ_n` overridden by every key of `decl(T_n)` (all deltas together), on `T_n`. It contains every effective subject that is, or contains, a unit named by a governance-affecting quarantined delta, and every effective subject whose signature or covered regions the override would change. A foreign declaration that would carve a part out of `P` as a nested subject affects `P`.
- **Governance signature** of subject `s`: `(role = subject, scope_id(s), kind/domain, governance mode)`. **Tenure** `τ(s)` is the first ledger position of the current uninterrupted run over which `s` has been an effective subject with an unchanged signature. A tenure ends when `s` is demoted to a part, its `scope_id` changes, its kind or domain changes, or its governance mode changes; a later restoration starts a new tenure. Byte-preserving refinement and carve-out promotion of one of its parts leave `s`'s tenure unchanged. Acceptance belongs to a tenure (§5.5 `ACC`); challenges, revocations and supersessions target exact triples and records and survive tenure changes.

**Content proposes; admitted records enact.** Acceptance, governance mode, reconstruction status, lifecycle and effective structure are derived from records, never from fields in unit content.

#### 1.7 Semantic declarations

Semantic declarations are authored in the manifest's `[unit.semantic]` table of the unit they belong to, or inline inside the unit's regions [D3 decision: inline syntax]: a line whose content after the comment leader is one of

```text
ssds:rel <TYPE> <object-unit-id> [key=value ...]
ssds:defines <object-name>
ssds:sdg <group-id> <member-unit-id> <member-unit-id> ...
ssds:joint-invariant <invariant-id> <unit-id> <unit-id> ...
```

Inline semantic markers are content: they are not normalized away, and editing one changes the unit's revision. Semantic declarations are: authored relations (§2), defined-object declarations, simultaneous-definition group declarations (§2.4) and joint-invariant declarations (§9.2).

**Single definer.** A unit may declare that it defines a named semantic object (`defines`). Two units current in one tree defining the same object name is an integrity conflict: both are ill-formed (§2.5) until the owner adjudicates by removing one declaration.

#### 1.8 System units and genesis structure

Genesis declares three reserved leaves: `ssds.manifest` (kind `MANIFEST`, the manifest file), `ssds.policy` (kind `POLICY`, the project policy file at the path genesis names, default `.ssds/policy.toml`) and, optionally, `ssds.unclassified` (kind `UNCLASSIFIED`), a catch-all that genesis may use instead of declaring units. Its scope is the only declaration using the empty prefix `prefix = ""` (a recorded execution basis's whole-tree fallback uses its own record-only entry instead, §6.3); it is not a sibling of the other top-level units but the outermost owner: it owns exactly the governed bytes that no other top-level unit's region contains, so with it declared the uncovered region is empty. Their identities are reserved; the policy unit is a protected surface (§25.3).

#### 1.9 Static structural checks

These checks run on every admission over the merged tree (§8.3 step 4) and define part of `well_formed` (§2.5): identity grammar and uniqueness; kind present on every subject and absent on parts; membership a forest; static sibling disjointness and containment (§1.4); scope conservation for a refinement (the parts partition the subject's declared terms); every scope term well formed, and every `symbol` term in a language whose pinned analyzer resolves terms as a pure function of file bytes (§1.3, §14.5). The check concerns the resolver, never a later result: a term that comes to resolve to `ABSENT` stays well formed (§1.3), but every term naming a file or a span within one (`path`, `file`, `heading`, `symbol` or `anchor`; `prefix` terms are exempt) that an admission newly declares or changes, authored or adopted, must resolve in the merged tree at that admission to a present file, which may be empty, or a found span (a realignment back to `Σ`'s value declares nothing new), so no file or span unit is declared over nothing (a typo, or a definition its analyzer cannot resolve, §14.5); a misspelled `prefix` is not caught by this check; no `renamed_from` cycle; residual identities never declared.

#### 1.10 What each identity establishes

| Fact | Established by | Never implies |
|---|---|---|
| content identity | hashing (mechanical) | any fact below |
| scope identity | the subject's admitted scope declaration | that bytes or meaning are unchanged |
| subject role and tenure | effective structure, changed only by admission | acceptance; a past tenure's acceptance |
| lineage | `renamed_from`, refinement history, ledger history, Git rename history | acceptance or equivalence |
| simultaneous definition | an SDG declaration accepted with its subject's revision | warrant of any member claim |
| dependency and completeness coverage | relations; `COMPLETENESS` judgments; analyzer completeness declarations | equivalence or acceptance; widening only adds context |
| semantic equivalence | an `EQUIVALENCE` judgment by a qualified actor (machinery decides only byte identity and §1.5 normalization) | acceptance of any new subject |
| acceptance | a passing acceptance judgment on exact `(subject, scope_id, rev)` in the current tenure | anything about another subject, scope or tenure |

#### 1.11 Locating an authority from a tension search key [D3 decision; §19.1 mapping]

The 7.2.1 tension search keys map onto unit structure as follows; the query is `ask(locate)` (§16.2).

| 7.2.1 key | SSDS resolution |
|---|---|
| owner/path plus heading, anchor or object ID | the unit that owns that region in `Σ` at the position asked (innermost ownership, §1.4); an object ID resolves through `defines` |
| exact revision | `(id, rev)` at that position, with the ledger position(s) at which it was current |
| claim or locator | the unit plus the byte span within it |
| earlier revisions | the unit's revision history over ledger positions |
| former names or paths | `renamed_from` lineage, transitively, as a fold over every admitted structure (a removed declaration never removes admitted lineage); Git rename-following history for paths |
| recorded predecessors | `SUPERSEDES`/`REPLACES` relations and refinement/promotion history in the ledger |

A tension home binds every implicated authority by unit identity (in-repository homes use `CHALLENGES`, §2.2; native issues carry the identities in searchable text). A move plus substantial rewriting that neither `renamed_from` nor Git rename detection reveals is a stated limitation, not a further rule.

### 2. Relations

#### 2.1 Relation and provenance class

A **relation** is `(subject, type, object, class, provenance)`, stored in the direction subject -> prerequisite; reverse traversal is impact analysis, never a second relation.

- **Authored** relations are semantic declarations inside the subject's scope or manifest semantic table (§1.7). They are part of every enclosing subject's revision, take effect when that subject's revision is accepted, and change only by changing content.
- **Derived** relations are computed by a versioned analyzer from content (§14.5) and cached under their derivation key; never edited, never canonical.
- **Proposed** relations are records awaiting acceptance; one is accepted only by an admitted content change to the subject's authored relations.
- **Record-level relations** (challenge targets, adjudication, supersession) are fields of records (§3), never edits to their targets.

#### 2.2 Vocabulary [D3 decision]

The vocabulary is part of the ruleset in force `ρ_n` (§5.2). It is closed and versioned. The system ruleset `ssds-rules/1` defines:

| Type | Role | Cycle class | Classes permitted | Layer constraint | Completeness class |
|---|---|---|---|---|---|
| `USES_DEFINITION` | `DEFINITIONAL` | `SIMULTANEOUS` | authored, proposed | non-ascending | `DEF` |
| `DERIVED_FROM` | `WARRANT` | `ACYCLIC` | authored, proposed | non-ascending | `WARRANT` |
| `ASSUMES` | `WARRANT` | `ACYCLIC` | authored, proposed | non-ascending | `WARRANT` |
| `DEPENDS_ON` | `WARRANT` | `ACYCLIC` | authored, proposed | non-ascending | `WARRANT` |
| `CONCRETIZES` | `GOVERNING` | `ACYCLIC` | authored, proposed | non-ascending | `GOVERNING` |
| `CONSTRAINED_BY` | `GOVERNING` | `ACYCLIC` | authored, proposed | non-ascending | `GOVERNING` |
| `EVIDENCES` | `EVIDENTIAL` | `ACYCLIC` | authored | subject kind `EVIDENCE_SPEC` | none |
| `EXECUTION_DEPENDS_ON` | `EVIDENTIAL` | `ACYCLIC` | authored, derived | subject kind `EVIDENCE_SPEC` or `D4` | `EXEC` |
| `CHALLENGES` | `EVIDENTIAL` | `ACYCLIC` | authored | subject kind `EVIDENCE_RECORD`; attribute `inquiry` ∈ {`EXPLORATORY`, `CONFIRMATORY`} required | none |
| `GENERATED_FROM` | `PROVENANCE` | `ACYCLIC` | authored, derived | subject kind `GENERATED` | `EXEC` |
| `SUPERSEDES` | `LINEAGE` | `ACYCLIC` | authored | same kind | none |
| `REPLACES` | `LINEAGE` | `ACYCLIC` | authored | same kind | none |
| `IMPORTS` | `STRUCTURAL` | `NEUTRAL` | derived | none | `STRUCT` |
| `CALLS` | `STRUCTURAL` | `NEUTRAL` | derived | none | `STRUCT` |
| `BUILD_DEPENDS` | `STRUCTURAL` | `NEUTRAL` | derived | none | `STRUCT` |
| `TESTS` | `STRUCTURAL` | `NEUTRAL` | derived | none | `STRUCT` |

**Layer order.** `D1 < D2 < D3 < D4` from higher abstraction to lower concretization; `PLAN`, `EVIDENCE_SPEC`, `GENERATED` take the layer of their domain; `EVIDENCE_RECORD`, `EXTERNAL`, `POLICY`, `MANIFEST` and `UNCLASSIFIED` are layer-free. **Non-ascending** means `layer(object) ≤ layer(subject)`: a unit may rely on its own or a higher abstraction, never on a lower concretization. Plan item dependencies follow the layer of each item's governing subject.

What each role can do: `DEFINITIONAL` fixes meaning and never warrants; `WARRANT` carries claim support or prerequisite order; `GOVERNING` carries authority; `EVIDENTIAL` binds evidence to target, execution and challenged authority; `PROVENANCE` orders regeneration; `LINEAGE` records replacement; `STRUCTURAL` supplies context, impact and widening only. `CHALLENGES` and `EVIDENCES` never appear as validity or warrant prerequisites in any rule (§2.3).

A generic "related-to" type does not exist and supports no closure (S5).

#### 2.3 Vocabulary adoption checks

A ruleset adoption (§27.1) is rejected unless: every type has every attribute; `SIMULTANEOUS` only on `DEFINITIONAL` types; `NEUTRAL` only on derived `STRUCTURAL` types and on no authored type; no rule names a `NEUTRAL` type, `CHALLENGES` or `EVIDENCES` as a validity-mode or warrant prerequisite; and every layer constraint is one of the closed forms above. An adoption that removes, renames or reclassifies a type declares, for existing uses, `READ` (alias to a defined type), `MIGRATE` (ordinary content changes through Admission) or `REJECT`; the adoption gate is shown the subjects that would become ill-formed. Historical views keep the vocabulary in force at their position. A type absent from `ρ_n` has unknown required semantics: Admission rejects any authored relation of that type, and in absorbed content it makes its subject ill-formed.

#### 2.4 Simultaneous-definition groups and cycle legality

An **SDG** is a semantic declaration (§1.7) naming units whose meanings are defined together. It is part of the enclosing subject's revision, so adding, removing or changing it needs acceptance. Rules: all members have one common `subj`, and the declaration lies inside that subject's scope; an SDG never contains a subject; SDGs are laminar; no relation is a self-relation.

**Cycle legality.** Let `E` be every authored relation other than `CHALLENGES` and every derived relation whose cycle class is not `NEUTRAL`, over effective units in the observed tree. `E` is legal iff every cycle of `E` lies inside the member set of one SDG and uses only `SIMULTANEOUS` edges. Consequences: a `DERIVED_FROM` or `DEPENDS_ON` cycle is illegal, even inside one subject or SDG; a mixed cycle is illegal; a cycle spanning two sibling SDGs is illegal unless an enclosing SDG is declared; nested SDGs are permitted. Contracting each SDG yields the acyclic order used for layer checks, ordering and impact; the contraction is a representation, never a warrant. Every claim inside an SDG still needs `ACYCLIC`-class warrant and its subject's acceptance.

Code recursion (mutual imports, recursive calls) is derived `STRUCTURAL` and `NEUTRAL`: legal, inert, traversed by widening, never warrant.

#### 2.5 Well-formedness

`well_formed(s)` (S0) is false when any unit of `s`: fails a static structural check of §1.9 in the effective structure as resolved; lies on an illegal cycle; carries an authored relation of a type unknown to `ρ_n` or one violating its layer constraint or subject-kind constraint; belongs to a malformed SDG; or conflicts under the single-definer rule. Admission rejects any request whose merged tree would make an affected subject ill-formed (§8.3 step 4(c)); a violation reaching the tree without Admission (absorption, a ruleset reclassification) makes every involved subject invalid in S2 through `ok` (§5.5).

Machinery checks declared relations only. Circular reasoning stated only in prose is a semantic defect for acceptance review and Challenge (§32).

#### 2.6 Completeness

`COMPLETENESS(X, R)` asserts, for a scope `X` (a set of effective units) and a completeness class `R`, that every `R`-prerequisite of a unit in `X` lying outside `X` is declared (boundary completeness). For `{u}` it is the outgoing completeness of `u`, typically attested during `u`'s acceptance review. Its mechanical minimum basis is a `content` entry on every unit of `X` plus the identity of `X`'s membership (`scope_id` of each member and the member set), so adding, removing or editing a member makes it non-current. Completeness never transfers through refinement or scope change.

**Analyzer completeness declarations [D3 decision].** An analyzer version declares, per language and configuration, the constructs for which its derived relations of a class are complete, and the **incompleteness markers** it detects: reflection, plugin loading, dynamic registration or import, generated code, runtime configuration, data read by path, build flags, external consumers. An analyzer may supply boundary completeness for a derived class only for a scope in which it detected no marker, no unit of which has a term resolving to `ABSENT`, and only within its declared constructs; it does so as an ordinary `COMPLETENESS` record with actor class `MACHINERY` (R0), whose basis is `content` on the scope's units and which also names the analyzer identity, a currency condition, not part of what is judged (§5.10 (b)); its target condition holds only while that identity is in the analyzer set of `ρ_n` (§5.2), so it is current only while its content holds and its analyzer is pinned, challengeable like any judgment, and the only form in which analyzer completeness narrows a closure (§4.6) or a recorded basis (§6.5). A marker never overrides a qualified actor's `COMPLETENESS` judgment; observed reads never bound a closure (§6.3).

### 3. Records and the ledger schema

#### 3.1 The ledger

The **ledger** is the single canonical store of everything not derivable from content: append-only, totally ordered by position, authenticated (§23.2), serialized in one closed versioned schema. Every record enters through Admission. A ledger entry is *provisional* when appended and *admitted* when a witness quorum holds its head (§22); a record is *recorded* when its entry is admitted; whether it is *current* is derived (§5.5). Rejections and refusals are recorded, so provenance includes what was refused and why.

Purely operational facts — task issue, reservations, leases, worktree creation, agent launch, retries — live in the Dispatcher's private operator journal under intent -> effect -> observed outcome (C4). They influence scheduling, never derived workflow state. Execution provenance that matters for audit travels inside submitted records.

#### 3.2 Common record envelope [D3 decision]

Every record is a canonical JSON object (RFC 8785, UTF-8). Field values are only: identifiers in declared grammars, enumerations, `sha256:` digests, integers, booleans, recorded UTC timestamps (RFC 3339, informational), validated repository-relative paths, and content-identity references. There are no free-text fields (C7, §24.1).

| Field | Type | Meaning |
|---|---|---|
| `id` | digest | `sha256` of JCS of the record without `id` |
| `kind` | enum §3.4 | fixes tier, schema and polarity |
| `schema` | integer | ledger schema version; `1` for SSDS 8.0 |
| `ruleset` | `{system, policy, analyzers}` | system ruleset id (e.g. `ssds-rules/1`), policy content digest and analyzer-set digest in force when submitted |
| `actor`, `actor_class` | actor id §25.1; `HUMAN` \| `AGENT` \| `MACHINERY` \| `ADMISSION` | who asserts it |
| `frame` | `ADMITTED` \| `{transformation: id(X)}` | the derivation it is evaluated in (§7) |
| `target` | typed reference(s) per kind | what it is about |
| `basis` | list of basis entries §4 | what it relied on |
| `outcome` | per-kind enumeration | its conclusion |
| `reason` | list of enumerated reason codes | why, where the kind requires |
| `supersedes` | list of record ids | explicit supersession, authorized at Admission (§8.3) |
| `binding` | task binding §12.2 | the signed envelope, its signature and the execution's lineage class, for every record submitted for a task |
| `governs` | `{mode: NATIVE, ruleset}` \| `{mode: LEGACY, protocol}` | the governing version the record declares; must equal its envelope's (§16.9) |
| `provenance` | `{route, harness, model_family, model, attempt, toolchain}` | execution provenance; replayed as recorded fact |
| `refs` | list of content references | report artifacts, evaluated outcomes, narrative homes, by content identity |
| `recorded_at` | timestamp | informational; never read by derivation (C3) |

A **content reference** is `{store, digest, media_type, locator?}` where `store` is `LEDGER` (an object in the ledger repository, §21.4), `REPO` (a blob in a commit the ledger keeps reachable), `HOME` (a native project home: issue tracker, evidence store, with a stable locator) or `RUNNER` (an external custody store). Derivation reads only `LEDGER`-store objects (evaluated outcomes, §17.3); every other reference is for drill-down and binding health.

#### 3.3 Tiers

| Tier | Kinds | Read by |
|---|---|---|
| **support** (judgments) | every judgment kind not in the challenge tier | S2 support (currency) |
| **challenge** | `CHALLENGE`, `ADJUDICATION`, `WITHDRAWAL`, `RISK_OVERRIDE`, `CONTINUITY_ATTESTATION` | S1 |
| **observation** | `REALIZATION`, `CHECK_EXECUTION`, `EXTERNAL_CONSULTATION`, `ANALYZER_OUTPUT`, `AVAILABILITY`, `CUSTODY_ENUMERATION` | S0 (as facts), S2 (as `record` premises) |
| **admission** | `ADMISSION`, `ABSORPTION` | S0 |
| **lifecycle** | §3.4 lifecycle rows | S0 |

Each kind has exactly one tier.

#### 3.4 Record kinds [D3 decision]

Decision classes R0-R3 are defined in §12.4; "S1 role" is the syntactic polarity of §5.3; "after a loss boundary" is the treatment of §23.6. A support-tier record's **target** is the exact thing it judges, so supersession on the same target (§8.3 step 3) never reaches content the superseder did not judge; the one exception is a `GATE_DECISION`, superseded on its gate and subject triple in any run (§8.3 step 3). The frame a record declares is where it resolves, not part of its target.

**Support tier.**

| Kind | Target | Outcomes | Producer and class | S1 role | After a loss boundary |
|---|---|---|---|---|---|
| `ACCEPTANCE` | `(s, scope_id, rev)`, resolved in its declared frame | `PASS`, `FAIL` | qualified actor for `s`'s domain under policy; R2, or R3 where policy requires (D1/D2 by default) | — | withheld |
| `REVIEW` | transformation `id(X)` or subject triple | `PASS`, `NO_PASS` | reviewer; R2 | — | withheld |
| `CONFORMANCE` | transformation `id(X)` and contract item revision | `CONFORMANT`, `NONCONFORMANT` | reviewer; R2 | — | withheld |
| `EQUIVALENCE` | `(u, r_from, r_to, consumption_class)` | `EQUIVALENT`, `NOT_EQUIVALENT` | qualified actor; R2; independent of `authors` of the change it judges (§5.10 (a)) | — | withheld |
| `COMPLETENESS` | `(X, R, membership)` at the revisions of `X`'s members its `content` basis names; a machinery record also names its analyzer identity, a `tgt` condition (§5.5), not part of what is judged | `COMPLETE`, `INCOMPLETE` | qualified actor, R2; or machinery, R0, for an analyzer completeness declaration (§2.6) | — | withheld |
| `EVIDENCE_ASSESSMENT` | realization record, evidence obligation `e`, reading; mode `ORDINARY` or `DISCRIMINATING` (§6.6) | `PASS`, `FAIL`, `INCONCLUSIVE`; `failing_outputs`; for `DISCRIMINATING`, a pair of `(observation, reading, verdict)` items | assessor; R2, or R3 per §6.8 | — | withheld; a failing assessment's adversity is unchanged (§6) |
| `IMMATERIALITY` | failing assessment(s) | `IMMATERIAL` | owner's qualified actor; R2, R3 for D1/D2 (§6.8) | — | withheld as disposition |
| `PLAN_ACCEPTANCE` | the plan objective section's revision and the item revisions | `ACCEPTED`, `REJECTED` | reviewer independent of the contract's author; R2 | — | withheld |
| `INTAKE_CLASSIFICATION` | observed path set or quarantined delta | proposed kind/domain/class | investigator, or the static classifier (machinery, §18.2); advisory, enacts nothing | — | withheld |
| `INTAKE_DISPOSITION` | quarantined delta or observed content | §18.3 vocabulary | reviewer, R2, independent by §8.3 step 3; a governance-neutral `ABSORB` may be machinery R0 where policy permits (§18.4) | — | withheld |
| `LEGACY_ACCEPTANCE` | `(s, scope_id, rev)` plus cited legacy evidence | `IMPORTED` | qualified actor; R2, R3 where policy requires | — | withheld |
| `EXTERNAL_ACCEPTANCE` | external unit pin plus consultation record | `IMPORTED` | qualified actor; R2 | — | withheld |
| `RECONSTRUCTION_PROPOSAL` | proposed unit or relation | `PROPOSED`, `PROVISIONAL`, `UNKNOWN` | investigator; enacts nothing | — | withheld |
| `TASK_RESULT` | task; for a candidate, the candidate commit and `id(X)` | the task's allowed outcomes (§12.3); typed slots (§13.5) | the bound role; exactly one per task, which ends the task (§8.3 step 7) | — | withheld (requalified by a new iteration) |
| `FINDING`, `AMENDMENT_REQUEST`, `BLOCKER`, `HUMAN_QUESTION` | target units or records | materiality, blocking flag, reason | any role | — | unchanged (never-lost; §15.2) |
| `COORDINATION_DECISION` | report(s) or item; `PARTITION` names tasks | `RESOLVE_LOCAL`, `AMEND`, `CHALLENGE`, `ESCALATE`, `DECLINE`, `PARTITION` | principal; R1 | — | not in force; the report's obligation reopens |
| `MATERIALITY_RECLASSIFICATION` | a non-floor report | `ROUTINE` | principal; R1 | — | not in force |
| `HUMAN_DECISION` | a human-attention obligation | `ACKNOWLEDGE`, `ANSWER`, `ACCEPT`, `REJECT`, `REDIRECT`, `MOOT` | authenticated human; R3 | — | not in force; attention reopens |
| `GATE_DECISION` | a gate obligation and the exact evidence core shown | `ACCEPT`, `REJECT`; `adequacy` ∈ {`ADEQUATE`, `INADEQUATE`}; `qualification` ∈ {`UNQUALIFIED`, `QUALIFIED`} with references to the qualifying records (§16.6); an `ACCEPT` requires `adequacy = ADEQUATE`, and a `QUALIFIED` `ACCEPT` supports only provisionally (§5.5) | authenticated gate holder; R3 | — | withheld |
| `PRODUCT_SCOPE_ACCEPTANCE` | a marked product-surface item in an authority unit at a revision | `ACCEPTED`, `REJECTED` | stakeholder or task authority; R3 | — | withheld |
| `LINEAGE_ATTESTATION` | a judgment record | `HUMAN_ATTESTED_FRESH` | authenticated human; R3 | — | withheld |
| `NON_AUTHORSHIP_ATTESTATION` | a record §8.3 step 3 classifies for independence and the content it judges | `NOT_AUTHOR` | the authenticated human who made that record; R3 | — | withheld |

The column "after a loss boundary" concerns support. An adverse outcome of these kinds (§5.10) keeps its veto across a loss boundary, because adversity follows existence.

**Challenge tier.**

| Kind | Target | Fields | Producer and class | S1 role |
|---|---|---|---|---|
| `CHALLENGE` | a support-tier record, a subject triple, an adjudication, a risk override or a continuity attestation; never another challenge, except that a challenge of a restrictive adjudication is a counter-challenge (§5.3) | `blocking`; `serious` (always blocking); `inquiry` ∈ {`EXPLORATORY`, `CONFIRMATORY`}; `locus` (the part, when raised against a part); materiality | any qualified actor per policy | restrictive, or counter |
| `ADJUDICATION` | a challenge | `UPHELD`, `DISMISSED` | the qualified actor policy names; R2, or R3 (Serious Challenge, D1/D2 claims); eligible only by §5.10 (e) (independence from `authors(root)` and the chain's class), whatever its outcome | restrictive (`UPHELD` of ordinary) or relaxer |
| `WITHDRAWAL` | the raiser's own challenge | — | the raiser | relaxer |
| `RISK_OVERRIDE` | a challenge | declared continuation scope (§10.5) | authenticated human; R3 | relaxer |
| `CONTINUITY_ATTESTATION` | a `LEDGER_LOSS` | scope form `COMPLEMENT` or `EXPLICIT` (§23.7); evidence references | designated human; R3 | relaxer |

**Observation tier** (produced by machinery through the Dispatcher; class R0).

| Kind | Target | Content |
|---|---|---|
| `REALIZATION` | evidence specification revision and claim content | execution basis, configuration, evaluated outcome reference or `INCOMPLETE` (§17.2) |
| `CHECK_EXECUTION` | contract obligation and candidate | template, parameters, result class per finding, tool version (§14) |
| `EXTERNAL_CONSULTATION` | external unit or external ledger | consulted qualified head, checkpoints, status read (§20) |
| `ANALYZER_OUTPUT` | analyzer identity, version, configuration, input revisions | output digest (only for nondeterministic or expensive analyzers, §14.5) |
| `AVAILABILITY` | a content reference | `AVAILABLE`, `UNAVAILABLE` |
| `CUSTODY_ENUMERATION` | an external custody runner and configuration | the complete list of runs of the configuration it performed (§17.5) |

**Admission tier.** `ADMISSION` (request identity, decision `ACCEPT`/`REJECT`, reason codes, validated basis summary, base commit, admitted commit, adopted deltas, the admitted records, salvaged never-lost records and refused records by identity and reason). `ABSORPTION` (plain, or fencing with its fence effect `B_n -> F_n`). Both carry `obs` (§22.1).

**Lifecycle tier** (Admission appends; human-gated unless stated).

| Kind | Effect |
|---|---|
| `GENESIS` | project identity, ledger id and location, authoritative replica, trust roots, witness set and quorums, ruleset, initial `Σ_0`, baseline commit, deployment class |
| `RULESET_ADOPTION` | system ruleset version, policy digest and analyzer set from position on (§27.1) |
| `SCHEMA_MIGRATION` | ledger schema version change with READ/MIGRATE/REJECT (§27.2) |
| `MODE_TRANSITION` | a subject's governance mode change, including cutover and version rollback (§19) |
| `LEGACY_RELEASE` | the legacy process owner releases a scope from the legacy process (§19.6) |
| `KEY_LIFECYCLE` | register, rotate or retire an Admission host key or Dispatcher issue key; a retirement lists the outstanding envelopes (§25.2) |
| `TRUST_MECHANISM_CHANGE` | change of human authentication mechanism or human key registry |
| `PROJECT_FORK` | new project identity |
| `REPLICA_REDESIGNATION`, `WITNESS_SET_REDESIGNATION` | §23.8 |
| `LEDGER_LOSS`, `FORK_RESOLUTION` | §23.6 |
| `LINEAGE_MIGRATION`, `LINEAGE_RETIREMENT`, `REDACTION_NOTICE` | §24 |

#### 3.5 Actor qualifications

Project policy (§25.3) maps each judgment kind × target domain × outcome to a required actor class and qualification, within system floors that policy may raise and never lower:

- D1 and D2 `ACCEPTANCE`, every `GATE_DECISION`, `RISK_OVERRIDE`, Serious Challenge adjudication, an adjudication in a challenge chain that contains an R3 human record (§8.3 step 3), `CONTINUITY_ATTESTATION`, `PRODUCT_SCOPE_ACCEPTANCE`, `HUMAN_DECISION`, `LINEAGE_ATTESTATION`, `NON_AUTHORSHIP_ATTESTATION` and every lifecycle record need an authenticated human.
- `PRODUCT_SCOPE_ACCEPTANCE` needs the stakeholder or task authority designated in policy for product scope; an applicable D1/D2 human gate whose evidence core showed the marked surface may accept it too, recorded as the gate holder's own `PRODUCT_SCOPE_ACCEPTANCE` co-submitted with the `GATE_DECISION`, so every acceptance or rejection of a surface is a record of one kind and the same-kind veto and adjudication apply to the surface alone (§5.10), never to the gate's decision on the revision. Technical D3 review of any kind never accepts it (S12).
- No actor reviews, accepts, conforms or plan-accepts its own work (A5; independence §8.3 step 3, §12.2).

#### 3.6 Compatibility contract [D3 decision]

The schema is **closed**: Admission rejects a record with an unknown kind, an unknown field, a missing required field or a value outside its grammar (C5). A system version declares the set of ledger schema versions it reads. A reader that meets an authenticated entry of an unreadable schema version presents historical views up to the entry before it and makes no current assertion (it is not compatible); this is not an integrity defect. New optional semantics never enter a schema version silently: any change to a kind, field or enumeration is a new schema version adopted by `SCHEMA_MIGRATION` (§27.2). Admission never re-adjudicates a record under a newer schema or ruleset (P2).

### 4. Basis

#### 4.1 Basis entries and modes

A **basis entry** is `(mode, target, consumption_class, role?)`. The mode is fixed by the rule for the record's kind at admission and never inferred at evaluation.

| Mode | Target | Satisfied when (§5.5) | Used for |
|---|---|---|---|
| `content` | `(u, r)` | evaluated in the state at hand (§5.5) and, for a frame record, in the entry's role (§7.3): `cur(u) = r`; or an equivalence path from `r` to `cur(u)` for the entry's consumption class; or, for class `PLAN_CONTROL` only, `cur(u)` reached from `r` by the control-tightening order (§13.4) | everything the actor saw: the judged revision, context supplied or read, change base, content behind evidence; prerequisites inside the record's own subject |
| `validity` | `(u, r)` | the content condition holds and `subj(u)` is valid | direct `GOVERNING` or `WARRANT` prerequisites in another subject only; never a `NEUTRAL`, `CHALLENGES` or `EVIDENCES` relation |
| `execution` | a realization's recorded execution basis (§6.3) | evaluated like `content`, in the state at hand and the entry's role: every unit entry `(u, r_u, terms)` has each recorded term re-resolve under the frozen context to its recorded content identity, or has an equivalence path from `r_u` to `cur(u)` for the entry's consumption class; every read and widened entry re-resolves to its recorded content identity | the execution part of a `REALIZATION` only, so its currency reads the same record that matching reads |
| `record` | record `x` | `x` is current | premises whose conclusion the depender relies on holding now: completeness, realization, assessment, plan acceptance, consultation, a task result reviewed |
| `standing` | record `x` | `x` stands: `base(x)` (it acts, is not superseded, its `status1` is neither `REVOKED` nor `BLOCKED`, `cont` and `tgt` hold, it is not vetoed or `nonind`), with `P` when `base(x) = P` | premises the depender relies on only as made and standing, not on their own basis still holding: the revision-assessment record an acceptance or gate decision relies on (§10.2) |
| `identity` | a record, or `(subject, scope_id, rev)` | always | targets of challenge-tier records, supersessions and dispositions; equivalence endpoints |

**A dependence states what it relies on [D3 decision; stakeholder record item 31].** A `record` entry imports the named record's currency, so it fails whenever anything that record relies on moves; a `standing` entry imports only that the record stands; an `identity` entry only that it exists. Each entry of §4.3 takes the mode its depender's conclusion needs, and where a readiness or admission condition reads a record's standing, the answering judgment's entry on that record is `standing`, so the dependence reads exactly what the condition reads. Each `record` entry also has a route when it fails: a completeness judgment that stops being current widens the closure (§4.6) and the next judgment takes the wider basis; a stale realization or assessment derives `REALIZE`, `RERUN` or `READING` (§6.9); a stale task result of a pending candidate derives `REVALIDATE` of that result for its implementer or investigator (§12.3), which re-attests the same candidate (a content change is a new iteration), one stale only through an R1 tightening being revalidated with the new checks run, and an integrated enactment's task result derives none (§10.4, SD-40); an R2 amendment derives a new obligation instead (§10.4); a review whose `record` entry on the task result fails is shown waiting on that revalidation (§10.3); a non-current judgment that a current obligation depends on derives `REVALIDATE` (§10.2), whose answer is admissible once its premises hold again or are replaced (a gate decision's answer, by a fresh decision on the current core: only its author's or the owner's decision naming it in `supersedes` raises `gterm`). No obligation is ready whose answer's mechanical minimum cannot hold without one of these routes being derived (§10.3).

**Subject boundary.** Let `S_x` be the subject of a record's target. A governing or warrant prerequisite `v` with `subj(v) ≠ S_x` gets a `validity` entry where the rule requires validity; one with `subj(v) = S_x` gets a `content` entry. A record never holds a `validity` entry on its own subject: no acceptance supports itself, warrant is acyclic inside and across subjects, an edit to the relied-on part makes the record stale through its `content` entry, and an `EQUIVALENCE` on that part for the record's class restores it without re-review. Modes are fixed at admission: after a part is promoted, records admitted earlier keep their `content` entries (exactly as strong, because the former subject's frozen scope still covers the promoted bytes); records admitted afterwards use `validity` on the new subject. Transitive governing authority is reached through validity of direct prerequisites, not listed separately.

#### 4.2 Composition

The basis of a record is the union of:

- the **mechanical minimum** for its kind (§4.3);
- **recorded reads**: every `read` through the interface during the task (§16.4), and every read a harness adapter or designated runner observed;
- **declared reliance** the actor adds at submission.

An actor can add to the mechanical minimum, never remove from it. A read of a file absent from the realization's tree is recorded by content identity where it can be pinned (§20.1); a read of a tracked file is recorded by its identity in the tree, governed or not (§6.3); an unpinnable read is recorded as such and keeps the record out of every permissive comparison of executed content (§6.5).

#### 4.3 Mechanical minimum per kind [D3 decision]

`gov(u)` is the set of direct `GOVERNING` and `WARRANT` prerequisites of `u`; `closure(S, R)` is §4.6 over class set `R`. "ctx" entries take consumption class `CONSUMER:<kind>`; target entries take `EXACT`.

| Kind | Mechanical minimum |
|---|---|
| `ACCEPTANCE` of `(s, σ, r)` | `content (s, r, EXACT)`; `validity` on each `v ∈ gov(u)` for units `u` of `s` with `subj(v) ≠ s`; ctx `content` on every unit of `closure(units(s), {GOVERNING, WARRANT, DEF})` outside `s`; `record` on each completeness judgment the closure used; for a `NATIVE` D1/D2 subject, `standing` on the revision-assessment record it relies on (§10.2) |
| `REVIEW`, `CONFORMANCE` on `X` | frame-role `content` on every unit of `Δ(X)` (before-image and output, §7.3) and on the contract item revision (`EXACT`); for a review or conformance judgment of a transformation `X` with retained units `U_X` (§5.10 (a)), `content` on every unit of `U_X`; for an item-level review of a partitioned item (§13.7), output `content` on every unit the parts' latest integrated enactments changed; the output entries and these retained-unit entries carry its judged scope `J`, the other entries of this row do not; for a review answering `JOINT_INVARIANT(i, k)` (or a high-consequence surface's review), the output `content` entries and the `validity` and governing-closure entries only for the units of `Δ(X)` inside `i`'s scope (or on the marked surface), and ctx `content` on every unit of that scope (§9.2); `validity` on `gov` of each changed unit across subjects; ctx `content` on the governing closure; `record` on the candidate's current task result (after a revalidation, the newest one for the same candidate; `identity` instead for a review answering `JOINT_INVARIANT(i, k)` or a high-consequence review, which judges the integrated result, not the attestation) and on each current `CHECK_EXECUTION`/`REALIZATION` of the exact candidate that the brief's evidence section marks (§16.5); `identity` on every other one shown (earlier, superseded or stale runs, history), since being shown is not being relied on (item 31) |
| `EQUIVALENCE` of `(u, r_1, r_2, k)` | `identity` on `(u, r_1)` and `(u, r_2)`; `validity` on `gov(u)` across subjects; never a `validity` entry on any consumer of `u` (§8.5) |
| `COMPLETENESS` of `(X, R, m)` | `content` on every unit of `X`; its target `m` is the membership digest `sha256(sorted (id, scope_id) of X's members)` and is part of its currency (§5.5) |
| `EVIDENCE_ASSESSMENT` | `record` on the realization; `content` on the specification revision applied (the reading) and on the claim content read; for `DISCRIMINATING`, both observations' realizations as `record` and both readings as `content` |
| `IMMATERIALITY` | `identity` on the failing assessments; `content`/`validity` on the governing state its conclusion is about (the specification or claim revision now in force) |
| `PLAN_ACCEPTANCE` | `content` on the plan objective section and each accepted item revision, class `PLAN_CONTROL` for items (§13.4), `EXACT` for the objective |
| `TASK_RESULT` | `content` on the item revision (`EXACT`); frame-role `content` on reads and on `Δ(X)`; `validity` on governing units across subjects |
| `INTAKE_DISPOSITION` | `identity` on the absorption entry and delta key; `content` on affected units |
| `LEGACY_ACCEPTANCE`, `EXTERNAL_ACCEPTANCE` | `content (s, r, EXACT)`; `record` on the consultation observation (external); `identity` on cited legacy evidence |
| `GATE_DECISION` | `content` on the gated subject revision; `record` only on its required supporting premises, the passing admissible assessments through which the core's required-evidence section shows each required evidence obligation holding at the rendering head (§16.6; their realizations are reached through the assessments' own entries, and several passing assessments of one obligation are each a premise, a conjunction stated as intended); `standing` on each counting revision-assessment record section 3 rendered, for a D1/D2 revision (a conjunction where readiness reads `∃`, stated as intended: one that stops standing derives `REVALIDATE`); `identity` on every other record of the evidence core shown (challenges, reports and findings, adverse and historical judgments, other enactments' decisions, non-required evidence, qualifying records), so the core stays exact while only the support the decision relies on can make it non-current (SD-35). Being shown is not being relied on: no displayed record's currency, and no challenge-tier record, enters the decision's `current` |
| `COORDINATION_DECISION` | `identity` on the reports it resolves; `content` on the plan items it names |
| `REALIZATION` | target `content` on claim content (`EXACT`); one `execution` entry on its recorded execution basis (§6.3), class `CONSUMER:REALIZATION`; `record` on each completeness judgment that bounded it |
| reports, challenges | provenance only; never checked for currency and never consumed by any rule (§8.3 step 6) |

#### 4.4 Consumption classes and equivalence paths [D3 decision]

Classes: `EXACT` (no equivalence coverage), `EDITORIAL`, `REPRESENTATION`, `MIGRATION`, `CONSUMER:<kind>`, `PLAN_CONTROL`. An `EQUIVALENCE` judgment of class `c` covers an entry of class `k` iff `k ≠ EXACT`, `k ≠ PLAN_CONTROL`, and `c = k`, or `c ∈ {EDITORIAL, REPRESENTATION}` (a meaning-preserving change affects no consumer). `MIGRATION` covers only `MIGRATION` entries and the cutover condition (§19.5).

```text
sat(content (u, r, k)) = T                              if cur(u) = r, or k = PLAN_CONTROL and r ⊑ cur(u)
                       = ⋁_{paths r = r_0 -> … -> r_m = cur(u)} ⋀_i current(q_i)
                                                        over passing EQUIVALENCE judgments q_i on u covering class k
```

A path composes judgments of covering classes, visits no revision twice, and every hop must be current; a step from `r_{i-1}` to `r_i` uses only a judgment with `r_from = r_{i-1}` and `r_to = r_i`, so hops keep their recorded direction (the reach reads them in either direction, §5.10 (b)). A hop that a standing `NOT_EQUIVALENT` on `u` vetoes is not current, and a `NOT_EQUIVALENT` vetoes every passing judgment that a composition connecting its two revisions needs, not only one on its own endpoints (§5.10 (a), (b); R14), so no path counts through a comparison under unresolved objection. The static support graph over-approximates coverage by including every equivalence judgment on `u` reachable from `r` (§5.6). The author of a change cannot be the sole qualifier of an equivalence or completeness judgment about that change, whatever request carries the judgment: every non-machinery one carries the independence requirement (§5.10 (a)), and a self-declared one is admitted as non-independent and covers nothing.

#### 4.5 Conservative widening

Widening addresses dependency uncertainty only. It never establishes equivalence, completeness or acceptance, and a widened basis never makes a part valid.

**Enclosing-scope chain.** For a unit `u`, built from `Σ_n` only (never from quarantined declarations):

```text
X_0 = {u}
then each effective composite containing u, smallest first      (laminar, so nested)
then the directory of u's declaration source, then each ancestor directory
X_m = every effective unit in the governed tree, plus the uncovered region
each step: X_{i+1} = X_i ∪ units(next scope); steps adding nothing are skipped
```

#### 4.6 Closure

```text
closure(S, R):                                     -- R a set of completeness classes
  reached := S; queue := S
  while queue not empty:
    u := pop(queue)                                -- order irrelevant to the result
    for v in declared R-prerequisites(u), authored and derived: enqueue v if new   -- enqueue adds v to reached
    if no X_i in chain(u) has a COMPLETENESS(X_i, c) with outcome COMPLETE, current with value T, for every c ∈ R:
        W := X_m                                   -- whole governed tree; brief marks UNBOUNDED
    else:
        W := the smallest such X_i
    for v in W: enqueue v if new
  return reached                                   -- least fixed point; finite; order-independent
```

Exact closure needs a current singleton completeness judgment on every reached unit. With no judgment anywhere in the chain the result is the whole governed tree, marked `UNBOUNDED`, with declared external units listed and undeclared external dependencies stated as unenumerable. Missing dependency knowledge never proves independence (S5).

## Part II. Derivation

### 5. The derivation and its strata

#### 5.1 Function

```text
derive(L_n, content of the trees L_n names) -> exactly one derived state D_n
```

`L_n` is the authenticated ledger prefix through position `n`. The ruleset and effective structure are read from `L_n`; nothing is supplied from outside. Derivation is a pure function. Which prefix may be presented as current is decided outside it, by currentness qualification (§23), so witness reads, live refs, wall clock, operator state and search indexes never enter `D_n`. A transformation frame `D_n[X]` is the same function over a hypothetical tree and structure fixed by `id(X)` (§7).

Four strata, each reading only lower strata; recursion only inside S1 and S2 in the forms proved unique below.

**Fixed predicate templates.** The SSDS system version fixes every derivation predicate. Project policy (§25.3) only parameterizes these templates: judgment kinds in use and their passing outcomes; actor qualifications (above the floors of §3.5); additions to the mechanical minimum; consumption classes per entry role; required judgment kinds, actor classes and human gates per subject domain; evidence obligations per claim kind; obligation triggers; the report routing table and escalation floors (raise only); role narrowing; enabled check templates; default budgets and time bounds. There is no rule language and no executable policy.

**Adoption-time stratification check [D3 decision].** A ruleset adoption is rejected if any parameter would make: S0 read anything but syntax, admitted structure, observed content and recorded facts; polarity depend on anything but kind, outcome and target; S1 read S2 or S3; S2 read S3 (readiness, discharge, obligations, routing, conformance, materiality, rank); or `stale` read an S2 value other than the currency of a record that a bounding completeness judgment cites, positively (§6.5, §6.6, SD-58). Every template declares its stratum, and the check is a comparison of declared strata, not an analysis of policy text.

#### 5.2 S0 — observed content, effective structure and ledger syntax

- **Ruleset in force** `ρ_n`: the latest admitted `RULESET_ADOPTION` at or before `n` (genesis's ruleset before any), naming a system ruleset version, a policy digest and the **analyzer set**: for each analyzer, its identity, version, configuration digest and the identities of the parsers it uses.
- **Expected integration head** `E_n`: genesis's baseline commit; `C_k` after an admission `k` (`C_k = B_k` for a records-only request); `obs_k` after a plain absorption `k`; `F_k` after a fencing absorption `k` (whose tree equals `obs_k`'s); unchanged after any other entry. **Observed tree** `T_n = tree(E_n)`.
- **Publication classification** `pub(k)` ∈ {`PENDING`, `PUBLISHED`, `OVERTAKEN`} and `late(k)`: §22.2.
- **Loss boundaries.** Every admitted `LEDGER_LOSS` is a boundary at its own position. `exposed(x, X)`, for a record `x` before the boundary and a set `X` of subjects and records, holds if `x ∈ X`, `x` targets a member of `X`, or `x` targets an exposed record; subjects resolve in `Σ` at the boundary.
- **Effective structure** `Σ_n`, and from it units, leaves, residual parts, composites, `scope_id`, `subj`, kind, domain, governed boundary, governance mode and tenure `τ(s)` (§1.6).
- **Quarantine** `Q_n` and `aff(Q_n)` (§1.6).
- **Revisions** `rev(u, T)`, `cur(u)` over effective scopes resolved in observed bytes (§1.5).
- **Relations and well-formedness**: authored and derived relations of `T_n`; `well_formed(s)` (§2.5).
- **Acting records [D3 decision; SD-25, SD-26].** Every S0, S2 and S3 rule is evaluated in one **state** `G`: the admitted state `D_n`, or a frame `D_n[X]` (§7.2). The **enactment** of a transformation is that transformation together with every clean machinery rebase of it (§11.5 step 3): the transformations of one producing task, whose identity is the enactment's; a transformation belongs to the enactment of the task whose result first submitted it (§7.1), so a later task resubmitting an identical transformation joins that enactment. A later implementer iteration, a partition part (§13.7) and a re-dispatch of a reopened obligation are new tasks and so new enactments. An admitted record **acts** in `G` iff it declares the admitted frame; or it declares a frame of an enactment that has integrated at or before `n`; or `G = D_n[X]` and it declares a frame of `X`'s own enactment. A record made in an earlier iteration's frame therefore never acts in the admitted state or in a later iteration's frame. This is the one rule for which records a state reads permissively: support (`base`, §5.5), withdrawal (`superseded`), relief of a veto (`stands⁻`, §5.10), disposition (§6.7), gate eligibility (§5.5), answering (§10.3) and run membership (§10.2) all read only records acting in `G`. Adverse records are outside this rule, whatever their frame: an adverse judgment vetoes in every state (§5.10), and a failing assessment counts wherever §6.4's start latch puts it. Acting is monotone along the admitted history (an integration is permanent), a record of an enactment that never integrates never acts in an admitted state, and `D_n[X]` reads exactly the records that act after `X`'s integration at head `n`. Observations and discriminating readings (§6.5-§6.8) are also outside this rule: they report outcomes on recorded trees under a reading, not judgments of a candidate, and §6 places each by its matching predicates and its own standing.
- **Record syntax**: targets; `superseded_G(x)` ⇔ some record acting in `G` names `x` in `supersedes` (authorization was checked at admission); **target conditions** `tgt(x)`: for `COMPLETENESS`, the membership digest of `X` under `Σ_n` equals the recorded one and, for a machinery record, its analyzer identity is in the analyzer set of `ρ_n`; for a passing `ACCEPTANCE` or `GATE_DECISION ACCEPT` on a `NATIVE` subject of kind D1 or D2, the judgment names the subject's current revision run in `G` (`rid_G(s)`, §10.2, an S0 fact); `T` for other kinds.
- **Adverse scope facts** of each failing assessment (§6.4): recorded anchors, assessed content, `home`, `about`, `starts`; the matching predicates `on⁺`/`on⁻` inputs (§6.5); the observations and discriminating readings `stale` reads.

**Content proposes; admitted records enact.** The policy unit is ordinary content whose edits take effect only through a human-gated `RULESET_ADOPTION` validated under the previous ruleset. A structural declaration takes effect only through an admission that authored or adopted it. S0 never reads a derived acceptance or validity.

#### 5.3 S1 — challenge tier

Kinds: `CHALLENGE`, `ADJUDICATION`, `WITHDRAWAL`, `RISK_OVERRIDE`, `CONTINUITY_ATTESTATION` (§3.4). Targets carry no tenure, so a challenge or revocation on a triple binds every tenure in which that triple recurs. A challenge against a part targets its subject's current revision and records the part as `locus`. Every target is strictly earlier (§8.5).

**Polarity** is syntactic, by kind, outcome and target:

```text
restrictive(a)   ⇔ a ∈ ADJUDICATION ∧ a.outcome = UPHELD ∧ ¬counter(a.target)
counter(c)       ⇔ c ∈ CHALLENGE ∧ restrictive(c.target)
relaxer(y)       ⇔ y ∈ WITHDRAWAL ∪ RISK_OVERRIDE ∪ CONTINUITY_ATTESTATION
                   ∨ (y ∈ ADJUDICATION ∧ y.outcome = DISMISSED ∧ ¬counter(y.target))
                   ∨ (y ∈ ADJUDICATION ∧ y.outcome = UPHELD ∧ counter(y.target))
                   -- each refers only to strictly earlier records: syntactic and well-founded

held(x, b)       ⇔ ∃ a ∈ CONTINUITY_ATTESTATION : a.target = b ∧ in_force(a) ∧ a holds x      (§23.7)
cont(x)          ⇔ ⋀ { held(x, b) : b a loss boundary with pos(x) < pos(b) }               -- T if none

gate(y)          = cont(y) if relaxer(y); T otherwise        -- every admitted adjudication is independent (§5.10 (e))
in_force(y), y ∈ ADJUDICATION ∪ WITHDRAWAL ∪ RISK_OVERRIDE ∪ CONTINUITY_ATTESTATION
                 ⇔ gate(y) ∧ ¬∃ c ∈ CHALLENGE : c.target = y
                                  ∧ (upheld(c) ∨ (c.blocking ∧ open(c) ∧ ¬counter(c)))
open(c)          ⇔ ¬∃ y ∈ ADJUDICATION ∪ WITHDRAWAL : y.target = c ∧ in_force(y)
upheld(c)        ⇔ ∃ a ∈ ADJUDICATION : a.target = c ∧ a.outcome = UPHELD ∧ in_force(a)
overridden(c)    ⇔ open(c) ∧ ∃ o ∈ RISK_OVERRIDE : o.target = c ∧ in_force(o)

status1(z) = REVOKED      if ∃ c : c.target = z ∧ upheld(c)
             BLOCKED      else if ∃ c : c.target = z ∧ c.blocking ∧ open(c) ∧ ¬overridden(c)
             PROVISIONAL  else if ∃ c : c.target = z ∧ c.blocking ∧ open(c)
             CLEAR        otherwise
```

**Uniqueness.** Polarity is computed first by recursion on strictly earlier targets. In the force and continuity predicates every right-hand side refers only to records at strictly greater positions than the left (a resolver is later than what it resolves; a challenge is later than its target; a boundary is later than every record it covers; an attestation is later than its boundary). The definitions are a recursion on a finite strictly increasing chain of positions, evaluated once in decreasing ledger order; each value is unique although negation appears. Non-blocking challenges have no S1 effect while open; they create S3 obligations.

Effects are conservative in both directions: an open blocking challenge against any relaxer suspends it while open, and an upheld one removes its force permanently; a counter-challenge has no effect while open, whatever its `blocking` flag; a revocation ends only when a counter-challenge is upheld, and that upholding is itself a relaxer (challengeable, suspended by an open blocking challenge, withheld by a later loss boundary). Repair of a revoked triple therefore needs a new revision and acceptance, or a successful challenge of the upholding.

**Loss boundary in S1.** `cont(x)` is false for a record before a `LEDGER_LOSS` unless an in-force attestation of that boundary holds it. It gates exactly the permissive effects: a relaxer before the boundary loses force (`gate`), and a record before it cannot be current (S2 `base`). Ordinary challenges, counter-challenges, restrictive adjudications (so revocations), supersessions and every S0 fact are not gated. Withholding a relaxer at any depth of a challenge chain can only restore a block or a revocation, never lift one. A disposition of an assessment disagreement is permissive for the claim; S2 reads it through `eff`, which includes `cont` (§6.7). With no `LEDGER_LOSS`, `cont` is identically `T`.

#### 5.4 Record polarity summary (every kind)

| Kinds | S1 effect | Effect in S2 | After a loss boundary |
|---|---|---|---|
| support-tier judgments other than reports and coordination records | none | support through `current` | withheld (`base = F`) until requalified or held |
| reports (`FINDING`, `AMENDMENT_REQUEST`, `BLOCKER`, `HUMAN_QUESTION`) | none | none (S3 obligations keyed on existence) | unchanged |
| `COORDINATION_DECISION`, `MATERIALITY_RECLASSIFICATION`, `HUMAN_DECISION` (as resolving records) | none | none (S3) | not in force; obligations reopen |
| failing `EVIDENCE_ASSESSMENT` | none | adverse through `adverse`/`qual` (§6) | unchanged (adversity follows existence) |
| adverse support-tier judgments (§5.10) | none | veto through `base` of passing judgments of their kind in their reach | unchanged (adversity follows existence); a disposing supersession from before the boundary is withheld |
| supersession, upheld adjudication, `IMMATERIALITY` as **dispositions** | — | permissive through `eff` | withheld as dispositions; other effects (removal from support, revocation) survive |
| `CHALLENGE` (ordinary, counter) | restrictive / counter | via `base` | unchanged |
| `ADJUDICATION` `UPHELD` of ordinary | restrictive (revocation) | via `base` | unchanged |
| `ADJUDICATION` `DISMISSED` of ordinary; `UPHELD` of counter; `WITHDRAWAL`; `RISK_OVERRIDE`; `CONTINUITY_ATTESTATION` | relaxer | via `base` | not in force |
| `ADJUDICATION` `DISMISSED` of counter | none | none | unchanged |
| observations | none | `record` premises; staleness evidence (§6) | permissive use withheld (`cont`); adverse use unchanged |
| admission and absorption entries, `Σ`, tenure, quarantine, trees | none | S0 constants | unchanged |
| lifecycle records | none | S0 constants | as re-established by the `LEDGER_LOSS` (§23.6) |

#### 5.5 S2 — support tier

Values lie in the lattice `F < P < T` (non-current/invalid < provisional < current/valid), `∧ = min`, `∨ = max`, empty `∨ = F`, empty `∧ = T`. S0 and S1 are constants here. Every term is evaluated in the state at hand `G` (§5.2): `acts` and `superseded` are those of `G`, and every basis entry of an acting record is evaluated against `G`'s tree and structure, in its role for a frame record (§7.3), whatever frame the record declares.

```text
base(z)  = F  if ¬acts(z) ∨ superseded(z) ∨ status1(z) ∈ {REVOKED, BLOCKED} ∨ ¬cont(z) ∨ ¬tgt(z) ∨ vetoed(z)
                 ∨ nonind(z)                                                -- §5.10 (a), (e)
           P  if status1(z) = PROVISIONAL
           T  otherwise                       (acts = cont = tgt = T for a subject-revision triple z)

current(x) = base(x) ∧ ⋀_{e ∈ basis(x)} sat(e)          -- x a support-tier or observation record

sat(content (u, r, k))   per §4.4
sat(execution E)         = per §4.1: each unit entry as a content entry whose identity test re-resolves the
                           recorded terms; each read and widened entry by its recorded content identity
sat(validity (u, r, k))  = sat(content (u, r, k)) ∧ valid(subj(u))
sat(record x)            = current(x)
sat(standing x)          = base(x)                     -- S0/S1 only, so an S2 constant (§4.1)
sat(identity z)          = T

ok(s)    = T if well_formed(s) ∧ s ∉ aff(Q_n) ∧ no unit of s is under a standing QUARANTINE
               disposition (§18.4), else F                               -- S0/S1 constant

valid(s) = base((s, scope_id(s), cur(s))) ∧ ok(s)
           ∧ ⋁_{j ∈ ACC(s)} ( current(j)
                              ∧ ⋀_{required kind/actor q of ρ_n for s} ⋁_{j' passing, by q, on the same triple} current(j')
                              ∧ ⋀_{required human gate g} gterm(g)
                              ∧ ⋀_{required evidence obligation e} ev(s, e) )
           ∧ qual(s)
  ACC(s) = admitted passing ACCEPTANCE (or LEGACY_ACCEPTANCE, EXTERNAL_ACCEPTANCE per mode) on exactly
           (s, scope_id(s), cur(s)), admitted at or after τ(s), or prospective acceptances j with bind(j) = τ(s) (§7.6),
           by actors qualified for them (for a NATIVE D1/D2 subject, current only within its revision run: tgt, §5.2, §10.2)

unq(h)   = T if h.qualification = UNQUALIFIED, P if QUALIFIED                    -- S0 constant; SD-24
gterm(g) = ⋀_{h ∈ elig(g)} ( current(h) ∧ unq(h) ), and F when elig(g) is empty    -- min, never max
  elig(g) = every authenticated passing GATE_DECISION acting in G, not superseded in G, on the gate obligation
            G derives for g (its subject triple and, for a NATIVE D1/D2 subject, its run rid_G(s), §10.2)

valid(part u) is not a variable: every use routes to valid(subj(u)).

**Gate term [D3 decision; SD-24, SD-25].** The gate term reads one state, through the one acting rule (§5.2), so it needs no rule of its own for frames: a decision, and a supersession of one, has effect exactly in the states where it acts. Consequences: a passing frame decision or a frame supersession has no effect in the admitted state until its enactment integrates, and none ever if that enactment is abandoned or replaced by a later iteration, so no pending, abandoned or replaced candidate raises or lowers the admitted gate term through them; a frame `REJECT`, being adverse, vetoes in the admitted state at once (§5.10, §32.3); and because `D_n[X]` reads exactly the records and runs that act after `X`'s integration at head `n` (§5.2, §10.2), every gate predicate in the frame (answered, eligible, superseded, `gterm`, `REVALIDATE`, the §16.8 entry) equals its value after that integration, so every decision that can affect the gate term in some state is visible, revalidatable and inspectable in a state that precedes that effect. `gterm` takes the minimum over the eligible decisions, so no order of admission or integration between holders or candidate frames decides between them, and a qualification lifts only when its own decision is superseded, by its author's reassessment or the owner's adjudication (§8.3 step 3), whatever another holder or frame decided. A non-current decision among them lowers the term and derives `REVALIDATE` for it in the state where it is eligible; nothing earlier remains to fall back on, and a superseded decision never becomes current again. Any qualified holder may record a passing decision, `QUALIFIED` or not, on an answered gate; each eligible one enters the minimum. A holder who sees a limitation can also challenge the subject triple or record a gate `REJECT` (an adverse judgment that vetoes passing decisions and derives the owner's adjudication, §5.10) on a core `decide(gate)` renders for it (§16.1). A holder who accepts with a stated material limitation lets work continue only visibly provisionally, and only where policy permits provisional continuation: the subject and every descendant whose support passes through it are `P` (min-propagation), and discharge is `DISCHARGED_PROVISIONAL` where policy permits it for the obligation's kind, otherwise `OPEN` (§10.4). A new revision run's gate (`NATIVE` D1/D2) decides afresh, while for any other subject a decision on an unchanged triple is reused across a tenure restart (§19.4). While a `QUALIFIED` decision is eligible in a state, the inspector view keeps an entry open for it there, naming the qualifying records (§16.8). `acts`, `unq` and `elig` read only S0 facts, so §5.6's monotonicity argument is unchanged.

ev(s, e)         = ( ⋁_{passing assessment a admissible for e} current(a) ) ∧ undisputed(s, e)
undisputed(s, e) = ⋀_{a⁻ ∈ adverse(s, e)} ( P ∨ disp(a⁻) )       -- T when adverse(s, e) is empty
qual(s)          = ⋀_{e named by a failing assessment a⁻ with starts(a⁻) ∧ about(a⁻, s)} undisputed(s, e)
                                                                 -- whether or not e is still required
```

`adverse`, `starts`, `about`, `stale` and `disp` are defined in §6, evaluated in the frame at hand.

**Adverse judgments and the veto.** Which outcomes object, how far they reach, what ends an objection and who may end it, and the predicates `vetoed`, `stands⁻`, `relieved` and `nonind` that `base` reads, are owned by §5.10.

**Supersession and risk override.** A record superseded in a state never becomes current again there or in any later admitted state, even if its superseder later goes stale; supersession withdraws a record without reversing its admitted history. A risk override never resolves a challenge: it turns `BLOCKED` into `PROVISIONAL` for the challenged target, `P` propagates by `min`, and S3 permits provisional discharge only inside the override's declared scope (§10.5). An upheld challenge on a subject revision revokes it permanently.

**Early cutoff.** When upstream subject `a` changes, subject `b` whose acceptance relied on `a` in `validity` mode becomes invalid, and records relying on `b` become non-current. If a re-review of `b` against the new `a` passes without changing `b`, `b` is valid again, and every record whose basis named `b`'s unchanged revision, and did not itself see `a`'s text, is current again with no further work. Equivalence is semantic unless trivial: machinery decides only byte identity and §1.5 normalization; the `PLAN_CONTROL` order is an order, not a sameness claim; derived interface fingerprints serve only consumers of derived structure, never behavioral conformance, evidence or acceptance.

#### 5.6 Uniqueness and support cycles [refinement R2]

S2's right-hand sides are built from `min` and `max` over S2 variables and constants. `about`, `starts`, the S1 predicates, `base` (including its veto, §5.10) and `base` inside `eff` are constants. `current(d)` of an `IMMATERIALITY` judgment enters `undisputed` only positively. `stale` reads S2 values only through the completeness judgments that bound an observation's basis, and only positively, through `on⁺` (§6.5): the currency of the records such a judgment cites (SD-58; its standing and its content entries are S1 and S0 facts); a holding bound can only make a failure stale, and a stale failure can only raise `undisputed`. The system is therefore monotone on a finite lattice and has exactly one least fixed point.

**Static support graph.** Nodes: `valid(s)` and `current(x)`. Edges, all fixed by admitted records and S0 facts:

1. each basis entry;
2. each subject to every acceptance, gate and assessment judgment naming it, and to every record disposing of a failing assessment about it (for any obligation, required or not; over-approximated through `home` and specification-derived obligations);
3. for each `content` entry `(u, r)` and each unit entry `(u, r_u, …)` of an `execution` entry, every equivalence judgment on `u` reachable from the recorded revision;
4. each subject to every completeness judgment that bounds the execution basis of an observation of a configuration whose failing assessments are about it, and to every record such a judgment cites (SD-58).

Admission keeps this graph acyclic (§8.3 step 5). Two terms of `about` (content-follow and obligation lineage) and the completeness edge of item 4 can acquire a cycle through absorbed content without a new record.

**Evaluation order, explicit fail-closed rule.** Derivation (i) instantiates the graph for the frame; (ii) computes its strongly connected components; (iii) assigns `F` to every node of every non-trivial component (more than one node, or a self-edge), before evaluating anything else; (iv) evaluates the remaining nodes once in topological order, reading the forced values; (v) raises one S3 finding per forced component: an ordinary finding when the cycle passes through an absorption-extensible `about` term or a completeness edge, else an **integrity** obligation, because any other cycle can arise only from corrupted input. Forcing only lowers values, so the result is the least fixed point of the system with those nodes clamped to `F`: no acceptance can ever support itself, and a cycle is never presented at `P` or `T`. For the mutual-acceptance configuration (`current(j_a)` ← `valid(b)` ← `current(j_b)` ← `valid(a)` ← `current(j_a)`) every node is `F`, and Admission also rejects it on two independent grounds (support cycle; illegal warrant cycle, §2.4).

#### 5.7 Corrupt prefixes [refinement R3]

The Ledger Store rejects any chain containing an unauthenticated entry before derivation runs (§23.2). An **authenticated** entry `k` that nonetheless violates the closed schema (§3.6), the entry-shape rule (§22.1), or a record kind's syntactic constraints (target tier, strictly earlier target, self-supersession, unknown kind) puts every position `≥ k` into **`INTEGRITY_HALT`**:

- derivation of positions `< k` is unaffected and available as historical views;
- no current assertion is made at or after `k`; Admission appends nothing except a human-gated `FORK_RESOLUTION` or `LEDGER_LOSS` that abandons the chain from `k` (a boundary if `k` was admitted, §23.6);
- an S3 integrity obligation with `CRITICAL` human attention is raised in every view.

An unreadable schema version is not corruption (§3.6). Integrity checks that run on every derivation: authentication and hash chain; closed schema; entry shape; static structure of `Σ` (§1.9); relation vocabulary and cycle legality; single definer; support-graph cycles (§5.6); observed-versus-effective comparison.

#### 5.8 S3 — consequence tier and views

Non-monotone functions of S0-S2 that nothing below reads: open obligations, including intake of each quarantined delta, the re-application of each `OVERTAKEN` admission's still-open item obligation, and requalification of each record or relaxer withheld by a loss boundary that was in effect at the retained head (computed by comparing derivation at the retained head with derivation now); discharge (§10.4); readiness (§10.3); blockers; **drift** (`cur(s)` differs from `acc(s)`, the latest revision with a passing acceptance — a display view only); impact sets for hypothetical changes; context answers; briefs; conformance (§14); routing, escalation and coordination obligations, decision and amendment classes (§12-§15); graph, diff and history views; integrity findings. Provisional values and risk-override scopes are interpreted here. S3 explains and schedules quarantine and ill-formedness; it never enforces them, because S2 already did.

**Historical views.** Derivation at any position `m ≤ n` is `derive(L_m, …)`, reproducible with the ruleset in force at `m`; it is labeled historical and claims no currentness.

#### 5.9 Determinism, analyzers, caching and checkpoints

**Determinism.** For every authenticated `(L_n, content)`: S0 is a function; S1 is a well-founded recursion; S2 is the unique least fixed point with the §5.6 clamp; S3 is a function. The same holds for each frame `D_n[X]`. `D_n` is single-valued and independent of evaluation order, wall clock, live refs, witness reachability, operator state and search indexes (C2, C3, C8).

**Analyzer contract [D3 decision: pinning].** Derivation at position `m` runs exactly the analyzer set pinned by `ρ_m`, never the analyzers a host happens to have installed. Matching re-resolves a recorded `symbol` term with the analyzer set its execution basis froze (§6.3), so a host must also hold every analyzer set named by a recorded execution basis it matches. A host that lacks a required analyzer makes no current assertion and offers historical views only at positions whose analyzer sets it has, as for an unreadable schema (§3.6). Analyzers produce derived relations keyed by `(analyzer id, version, configuration, input revisions)`. A deterministic analyzer's output is cache. An analyzer whose output is nondeterministic, expensive, or dependent on any input that key does not name (host headers, compilers, the build environment) has its output recorded as an `ANALYZER_OUTPUT` observation, and replay uses the recorded output. Changing the analyzer set is a human-gated `RULESET_ADOPTION` (§27.3): derivation from that position uses the new set, historical views keep the set of their position, and judgments whose basis named analyzer output become non-current only if the output changed (early cutoff); a machinery `COMPLETENESS` declaration's `tgt` requires its analyzer identity in the set, so an analyzer-set change makes every acceptance bounded by such a declaration non-current whatever the output, and its re-acceptance burden is shown in the adoption gate (§27.3).

**Caching.** Memoization keyed by inputs; nothing is cached without its content key, so no dirty state exists. Incremental derivation must equal from-scratch derivation (§31).

**Derivation checkpoints and recovery time [D3 decision].** A derivation checkpoint caches the complete derived state at a position, keyed by `(ledger position, entry digest, ruleset including its analyzer set, schema, system version)`, in the private derived index. It is verified before use by recomputing its key from the ledger, carries no currentness, and is unrelated to witness checkpoints. Restart derives from the latest verified checkpoint forward. **[proposed default]** A checkpoint is written at least every 1,000 entries and at every lifecycle entry, so that restart replays at most 1,000 entries; the recovery-time objective is that current state is derivable after restart without replaying unbounded history. **[delegated]** Checkpoint encoding and storage engine.

#### 5.10 Judgment disagreement [D3 decision; owner; refinements R8, R9, R12, R13, R14; SD-24 to SD-35, SD-41 to SD-45]

This section is the **one owner** of judgment disagreement: which outcomes object, how far an objection reaches, what ends it, who may end it, how independence is measured, and what follows in S3. Every other section that touches these rules points here (§3.4, §5.3, §5.5, §6.7, §6.8, §8.3 steps 3 and 7, §10.2-§10.4, §16.6, §16.8); where one restates a consequence, this section governs. Failing evidence assessments keep §6 for start, adverse scope, matching and staleness; their dispositions and the independence of those dispositions are governed here.

**(a) Definitions.**

- **Adverse outcomes**: `ACCEPTANCE` `FAIL`, `REVIEW` `NO_PASS`, `CONFORMANCE` `NONCONFORMANT`, `PLAN_ACCEPTANCE` `REJECTED`, `EQUIVALENCE` `NOT_EQUIVALENT`, `COMPLETENESS` `INCOMPLETE`, `GATE_DECISION` `REJECT`, `PRODUCT_SCOPE_ACCEPTANCE` `REJECTED`, and every `INTAKE_DISPOSITION` other than `ABSORB`. A failing `EVIDENCE_ASSESSMENT` is adverse under §6.
- **Target**: the exact thing a record judges (§3.4). The frame a record declares is where it resolves, not part of its target.
- **What was judged, not who names it** (stakeholder record items 28-29, 31). A reach compares what a judgment judged. A transformation review's or conformance judgment's **judged scope** `J` is an S0 fact of `X`: the post-state content `(u, rev(u, C))` of every unit of `Δ(X) ∪ U_X`, where `X`'s **retained units** `U_X` are recorded once, in the envelope of the task that produces `X` (§12.2), as `rid` is: every unit an integrated enactment changed for an item revision with the same prose and fixed fields as the revision that task was issued for (in any item or plan, §13.4), empty when there is none. So every judgment of `X` carries the same `J`, whenever it is admitted; the `J` of the first enactment for a new prose and fixed fields is its change; an empty transformation's is its retained content; and an R2 amendment of other fields, a re-identification, a copy into another plan or a re-partition keeps the retained content (SD-42 to SD-44). Of the `content` entries §4.3 requires, those carrying `J` are the output entries of `Δ(X)` and the entries on the units of `U_X` outside `Δ(X)` (context by §7.3); before-images, the contract item revision, the governing closure and a joint invariant's scope context are outside it. A joint-invariant, high-consequence or item-level review has no `J`: it reaches, and is reached, by its exact target only, and its independence is measured over the content its output entries name (SD-44); a plan item revision's judged content is its prose and fixed fields: they reach the same content under any item or plan, so re-identifying or copying an item does not escape them. An acceptance or gate decision judges a subject: by S10, acceptance attaches to one exact subject and content identity never transfers it, so their objections stay on the same subject triple. The kinds with named targets (`EQUIVALENCE` between two revisions of a unit, `COMPLETENESS` of a scope, `INTAKE_DISPOSITION` of a delta, `PRODUCT_SCOPE_ACCEPTANCE` of an item at a revision) stay on what they name. A re-identification of a subject or unit is a new target for these kinds; where a declared lineage (`renamed_from`, §1.2) links the new identity to the old one, the standing objection is carried into the next judge's brief (§16.5), and a remove-and-redeclare without lineage is not detected (§32.2).
- **Asserts.** A passing judgment **asserts** in a state when `base` would leave it above `F` but for vetoes: it acts there (§5.2), is not superseded, its `status1` is neither `REVOKED` nor `BLOCKED` (a `PROVISIONAL` one asserts), it has `cont` and `tgt`, and it is not `nonind`. This reads only S0 and S1 facts, the same ones `base` reads, so a judgment asserts whether or not its basis is current.
- **Reach** (one rule; R14, SD-29): `same(j⁻, z)`, the set of passing judgments an adverse judgment `j⁻` objects to in a state, is every passing judgment `z` of `j⁻`'s kind for which some set `S` of judgments of that kind asserting in that state, together with `z`, **claims** what `j⁻` denies, while `S` alone does not. What a set of passing judgments claims is the table's third column: a kind whose judgments compose (`EQUIVALENCE`, `COMPLETENESS`) states how they compose, and every other kind states what one judgment claims, so for it `S` is empty and `z` alone decides. `z`'s own standing is not part of the test (`base` handles it). Every reach contains the target; reaching further is what keeps amendment, rebase, re-dispatch, a new run or a composition of judgments from escaping an objection. The test reads only S0 and S1 facts.
- **Owner** of a target: the actor policy names to adjudicate disagreements over that target's domain (§10.2 `ADJUDICATE_DISAGREEMENT`); for an agent, the execution bound to that adverse judgment's `ADJUDICATE_DISAGREEMENT` obligation, never a peer holding the same qualification. Where a reach crosses items or plans (§5.10 (b)), the owner is the owner of the adverse judgment's target, and the reached judgment's own owner is shown on the obligation.
- **`authors(x)`**, for a record or subject triple `x`: the actors whose admitted records authored the repository content `x` ultimately judges, unknown where any of that content has no admitted authoring record (absorbed pushes, legacy imports, restores, manual merges). For content or a subject triple, that revision's content; for an `EQUIVALENCE`, the content that differs between its two endpoints, on either side (the change it judges, whichever way it is recorded); for a `COMPLETENESS`, its members' content at their revisions; for a transformation's `REVIEW` or `CONFORMANCE`, the content in its judged scope `J` (§5.10 (a)), retained units included; for a joint-invariant, high-consequence or item-level review, the content its output entries name; for an observation, the content it ran on; for an `EVIDENCE_ASSESSMENT`, its claim content; for a disposition (`IMMATERIALITY`, a superseding assessment, an upheld adjudication of a challenge against an assessment), the claim content of the assessments it covers; for a revision-assessment `TASK_RESULT`, the assessed revision; for any other record, `authors` of its target, recursively, or its own author where its target is not a record or content. The authors of content at a revision are every actor whose admitted record produced that content at that revision, the author of a revert, restore or re-application that re-produced it included.
- **Requirement.** These records carry an independence requirement: every `EQUIVALENCE` and every `COMPLETENESS` that is not a machinery record, whatever request carries it (SD-29); every review, conformance, acceptance and plan-acceptance judgment; every disposition of a failing assessment; every `INTAKE_DISPOSITION` a reviewer records. Machinery records (R0) never do: their warrant is determinism (§2.6). Imports (`LEGACY_ACCEPTANCE`, `EXTERNAL_ACCEPTANCE`) never do: they record a fact about another process's acceptance, not a judgment by SSDS (§19.2, §20.2). A `GATE_DECISION` and a `PRODUCT_SCOPE_ACCEPTANCE` are human R3 decisions with no independence requirement; their gate holders are fixed by policy (§3.5).
- **Independence test.** A record with a requirement is independent only when its lineage class is `ATTESTED_FRESH` or `HUMAN_ATTESTED_FRESH` and its lineage is disjoint from `authors(x)` for its target `x`; for an authenticated human, when the human is not in `authors(x)` or presents a `NON_AUTHORSHIP_ATTESTATION`. Unknown authorship is never disjoint from an agent's lineage. **Owner exception**: where policy names no qualified human other than a member of `authors(x)`, that member may act as owner, admitted as independent with the common-mode dependency recorded and shown in the inspector view. The classification is fixed at admission from the binding and any co-submitted attestation; a later attestation does not change it.
- **`nonind(z)`**: the S0 fact that `z` had a requirement at admission and was not independent. A record without a requirement is never `nonind`.
- **Root and class of a challenge chain.** From an `ADJUDICATION`'s challenge, follow targets through challenge-tier records to the first record or subject triple that is not challenge-tier: the **root**. The chain's **class** is the highest decision class of any support-tier or adjudication record in it; challenges carry no class.

**(b) Per-kind table.** One row per kind that can object; a kind not in the table supersedes only on its target (§3.4). "Supersession target" is what a superseder must judge (§8.3 step 3 admits a supersession only on it); "per-target relief" ends the veto for one reached target without superseding.

| Kind | Target | What passing judgments claim, alone or composed (reach, `same`) | Supersession target | Per-target relief | Requirement; `authors` of | Passing aggregation |
|---|---|---|---|---|---|---|
| `ACCEPTANCE` | `(s, scope_id, rev)` | the same triple, in any frame or tenure | the target | — | yes; the revision | ∃ over `ACC(s)` (§5.5) |
| `REVIEW` of a subject triple | the triple | the same triple | the target | — | yes; the revision | ∃ (§10.4) |
| `REVIEW` of a transformation | `id(X)` | every transformation whose judgment's judged scope `J` (§5.10 (a)) contains the adverse judgment's `J` at the same content, under any item, revision or plan, when that `J` is nonempty; only its own target when it is empty (SD-34, SD-42): what a review judged is its `J`, so neither an amendment of fields other than the prose and fixed fields nor a re-identification or copy of the item changes the reach (an amendment of the prose or fixed fields starts a new key, whose first transformation retains nothing, its earlier findings reaching it only through the same-plan re-review carry, §16.5), a re-dispatch that keeps rejected content (partially or with an empty change) is reached, and one that changes it, or a review of unrelated content, is not | the target | the adverse judgment's own author's or the owner's independent passing judgment on that exact target | yes; the content in `J` | ∃ (§10.4) |
| `CONFORMANCE` | `id(X)` and the contract item revision | as `REVIEW` of a transformation | the target | as `REVIEW` of a transformation | yes; the content in `J` | ∃ (§10.4) |
| `PLAN_ACCEPTANCE` | the objective section's revision and the item revisions | a rejection of item revision `r*`, under any objective revision, denies `r*` and every tighter revision (§13.4). This is a conservative resolution policy, not a claim about why the plan was rejected: a tightening is taken to keep what was rejected whatever the ground, since a rejection for looseness or infeasibility that a later amendment cures is for its rejecter or the owner to judge cured (route 3), never a peer (SD-35); one acceptance naming `r` claims `r` and every revision tighter than `r` (its conclusion "still applies under tighter controls", workplan §7.9, §13.4), the item's current revision among them when it covers it. The two contradict exactly when `r` and `r*` have a common tightening, which by §13.4 is when their item prose is byte-identical and every field `⊑` holds fixed has the same value: every field §13.4 marks "unchanged" and every field outside its whitelist (such as `affected`), the `item` key excepted because it names the item rather than what was judged (each control field then has a tighter value common to both). Read across items or plans, the same test asks whether two item revisions, whatever item names them, judged the same content: the meet is computed over that content, not over one item's revisions. So a rejection of `r*` reaches every acceptance naming an item revision, in any item or plan, with the same prose and fixed fields, whoever recorded it and whenever (SD-32, SD-33); the item's current revision is not read, so no revert, loosening or tightening releases or creates a veto. A rejection denies each item revision it names; acceptances do not compose | the target, admitted while its basis holds (Admission step 6: the objective section at its revision, an `EXACT` entry, and each named item revision `⊑ cur`); otherwise only an upheld challenge lifts it | the rejecter's or the owner's independent passing acceptance on that exact target (SD-30), so judging that an amendment cured a rejection is theirs, never a peer's; relieving an acceptance of `r` also clears its coverage of every tightening of `r`, those it shares with the rejected revision included, and the reliever's brief says so; relief is admitted only while the relieved acceptance's own basis holds (`r ⊑ cur`, §8.3 step 6), and where it does not, that acceptance covers nothing issuable, so its veto blocks no work and the obligation it derives ends by supersession of the rejection while its basis holds, or otherwise by an upheld challenge; while no answer of the owner is admissible the obligation is shown waiting, not dispatched (§10.3) (where neither the relieved acceptance's basis nor the rejection's holds, an upheld challenge is the only lift) | yes; the plan units | ∃ over coverage (§11.2) |
| `EQUIVALENCE` | `(u, r_from, r_to, consumption_class)` | judgments on the same unit of classes covering `j⁻`'s (§4.4), each read in either direction, claim that every two revisions they connect are equivalent for `j⁻`'s class: so `z` is reached when it lies on a chain of asserting judgments joining `j⁻`'s two revisions, and, alone, when it has those two revisions | the target (exact class) | — | yes, unless machinery; the change between the endpoints | ∃ path (§4.4), through unvetoed hops only |
| `COMPLETENESS` | `(X, R, membership)` at its members' revisions (a machinery record's analyzer identity is its `tgt` condition, §5.5, not part of the target) | judgments of `j⁻`'s class on scopes inside `j⁻`'s scope, at the same member revisions, claim complete every scope their union covers (boundary completeness composes by union, §2.6): so `z` is reached when it is needed in such a union covering `j⁻`'s scope, and, alone, when it has that scope; a machinery record and a judgment are compared alike | the target | — | yes, never machinery; the members | per closure (§4.6) |
| `GATE_DECISION` | the gate and subject triple, in any run | the same gate and triple, in any frame, tenure or run | the gate and triple, in any run | — | none (R3 holder) | minimum `gterm` (§5.5), so a superseder's own decision stays in it |
| `PRODUCT_SCOPE_ACCEPTANCE` | the item at a revision | the same item at the same revision | the target | — | none (R3) | ∃ |
| `INTAKE_DISPOSITION` | the quarantined delta or observed content | the same | the target | — | a reviewer's yes; machinery none; the delta | ∃ |
| failing `EVIDENCE_ASSESSMENT` | realization, obligation, reading | §6.4 adverse scope | the target, by its own assessor or the owner (§6.7) | — | yes; the claim content | §6 (`undisputed`) |

**(c) Objection.** An adverse judgment counts by existence: it is never-lost (§8.3 step 6), its own currency is irrelevant, a loss boundary does not withhold it, and it needs no independence (independence is required to support, never for an adverse judgment to object). It objects in every state, whatever its frame (§5.2), to every passing judgment in its reach, admitted before or after it.

**(d) What ends an objection, and who.** Exactly four routes, each counting only from a record that is independent by (a):

1. **Reassessment**: a record by the adverse judgment's own author (a human; an agent's task has ended) naming it in `supersedes`, on the supersession target.
2. **Adjudication by the owner**: the owner's record naming it in `supersedes`, on the supersession target.
3. **Per-target relief** (transformation `REVIEW` and `CONFORMANCE`, and `PLAN_ACCEPTANCE`, SD-30, only): the author's or the owner's passing judgment on a reached target, which exempts that target without superseding anything, so a judgment about one item revision or base never lifts the objection for another. A relieved plan acceptance covers what it covered before, so relieving an acceptance of `r` clears its coverage of every tightening of `r`, those it shares with the rejected revision included; the plan-acceptance brief of the reliever states this.
4. **Upheld challenge**: an `ADJUDICATION` upholding a challenge against the adverse judgment.

No qualified peer supersedes another actor's judgment; a contrary peer judgment is a disagreement. These routes end an adverse judgment; a failing assessment's dispositions are §6.7's (supersession by its assessor or the owner, `IMMATERIALITY`, an upheld adjudication), each counting only when independent by (a), and its staleness is §6.6's. Each route has effect only in the states where its record acts (§5.2): a reassessment in a candidate's frame ends the objection there and, after that enactment integrates, in the admitted state, never in the admitted state while it is pending or after it is abandoned or replaced.

**(e) Independence is enforced at two points.** *Admission*: every `ADJUDICATION`, of any outcome, at any depth of a chain and whatever its target tier, is admitted only if it is independent of `authors(root)` by (a) and its class is not lower than the chain's class (§12.4: a decision moves up, never down); otherwise it alone is refused (`AUTH_ACTOR`), the rest of its request, its `TASK_RESULT` included, is admitted, it answers nothing and `ADJUDICATE(c)` stays dispatchable; a supersession not authorized by (b) and (d) is rejected (`AUTH_SUPERSEDES`). *Derivation*: a record with `nonind` has `base = F` (§5.5), so it supports, supersedes, relieves and disposes of nothing and is kept as data. S1 therefore needs no independence fact.

```text
stands⁻(j⁻) ⇔ ¬∃ d : d supersedes j⁻, directly or through a chain of supersessions, each acting in G,
                     ∧ acts(d) ∧ ¬superseded(d) ∧ status1(d) = CLEAR ∧ cont(d) ∧ ¬nonind(d)   -- routes 1-2;
                                                                        -- the chain's last record must stand, as in §6.7
             ∧ ¬∃ a ∈ ADJUDICATION : a.target is a challenge targeting j⁻ ∧ a.outcome = UPHELD
                     ∧ in_force(a) ∧ cont(a) ∧ ¬contested(a)          -- route 4; contested as in §6.7
vetoed(z)   ⇔ z has a passing outcome ∧ ∃ admitted adverse j⁻ : kind(j⁻) = kind(z) ∧ same(j⁻, z) ∧ stands⁻(j⁻)
                                                   ∧ ¬relieved(j⁻, z)            -- same: (a), (b), evaluated in G
relieved(j⁻, z) ⇔ j⁻ is a REVIEW or CONFORMANCE of a transformation, or a PLAN_ACCEPTANCE ∧ ∃ y passing, of kind(j⁻), on z's exact
                  target, by j⁻'s own author or the owner
                  : acts(y) ∧ ¬superseded(y) ∧ status1(y) = CLEAR ∧ cont(y) ∧ ¬nonind(y)   -- route 3; F for every other kind
```

`stands⁻`, `vetoed` and `relieved` read only S0 and S1 facts, so `base` stays a constant in S2 and §5.6's monotonicity argument holds.

**(f) Consequences in S3.**

- A standing adverse judgment that vetoes a passing judgment of its kind acting in the state and not superseded there derives `ADJUDICATE_DISAGREEMENT` for the owner (§10.2); a passing judgment vetoed this way derives no `REVALIDATE`. For a composing kind this includes every judgment a composition needs, so a disagreement carried by composition is routed exactly like a direct one, and the inspector shows the composition. A vetoed passing judgment with `nonind` also derives it: it supports nothing, but the contrary claim it states is shown to the owner.
- An answered judgment obligation whose target carries a standing, unrelieved adverse judgment in its reach is `REFUSED` (§10.4), whichever answered first.
- A passing judgment with `nonind` does not answer an obligation whose discharge requires independence, so that obligation stays dispatchable (§10.3).
- The gate brief lists every standing adverse judgment whose reach includes the decision asked (§16.6).

**(g) Invariants.** The rules above are written to satisfy these properties. `qualification/ssds80/judgment_disagreement_model_check.py` checks them only on the cases it models (§31.3): transformation `REVIEW`, `ACCEPTANCE` and `GATE_DECISION`; `EQUIVALENCE` chains on one unit; `COMPLETENESS` covers of three units, an analyzer declaration among them; and `PLAN_ACCEPTANCE` coverage of three items; a gate decision's basis built from its evidence core; with risk-overridden (`PROVISIONAL`) records, fixed authorship, at most one resolving record, challenge chains of depth two, and admission order sampled over two reference-respecting permutations per case. Its oracle restates the protected properties but shares the model's helpers for acting, supersession, S1 status and the independence test, so a mistake in those can agree on both sides; and it reads what each kind claims and denies from the same table column (b) states, so an error in that column is green by construction: the model tests how claims compose and are enforced, never whether a row states the right claim. It models no other kind, no qualified gate value, integration transition, loss boundary or changing authorship. It is a diagnostic of these written rules, never adequacy or production evidence (DS-001).

1. **No unresolved support.** A passing judgment in the reach of an adverse judgment supports nothing while that objection stands and is unrelieved for its target; no path or other composition of judgments supports a conclusion that a standing objection denies.
2. **Every route is independent.** No record with `nonind`, and no adjudication refused by (e), ends an objection, supports, supersedes, relieves or disposes.
3. **Relief stays inside what was judged.** A superseder ends an objection only by judging the objection's own supersession target, and then withdraws it wherever it reaches (the objector's reassessment, or the owner's adjudication, of the very thing objected to); a reliever ends it only for its own exact target. No record ends an objection by judging some other target in its reach.
4. **Liftable where it bites.** For every state in which a standing objection vetoes a passing judgment, some admissible independent record of routes 1-4 would end it there.
5. **State locality.** A permissive record (a passing, superseding or relieving one) of a pending, abandoned or replaced enactment changes no admitted value. An adverse judgment is the stated exception: it objects in every state, whatever its frame ((c), §5.2).
6. **Order independence.** For the same set of admitted records, every derived value is the same whatever order they were admitted in; where admission itself depends on order (a reference not yet present, or an Admission check that reads the state at the request's position, such as a supersession's or relief's basis or a cutover's carrier), the admitted set, and with it the derived values, can differ by order; the invariant is over the admitted set. (The model samples two reference-respecting orders per case; it does not prove this.)
7. **Class.** No adjudication below its chain's class is admitted.
8. **Routed.** In every state where a standing objection vetoes a passing judgment acting there and not superseded there, directly or through a chain, the owner's `ADJUDICATE_DISAGREEMENT` is derived.

### 6. Assessment disagreement

#### 6.1 Owner requirements realized here

The 7.2.1 evidence owner requires: "A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority. A stale passing observation is not admissible confirmation"; `review-required` when applicability is uncertain; "an unresolved material disagreement keeps dependent present guidance/closure visibly qualified"; supersession and adjudication "explicit enough to distinguish resolved reassessment from still-live disagreement"; no resolution by vote, count, latest editor or serialized record position; and no suppression of contradictory admissible observations to manufacture a pass. This section is the D3 concretization of those requirements.

**No mechanical lapse.** A failing assessment, once it counts, counts against the claim until a disposition stands or discriminating observations show it stale in the frame. No content change, structural change, specification change, frame outcome, challenge or ledger order ends it by itself. Staleness is not refutation: a failing assessment never makes validity `F`; it caps it at `P`, and reassessment decides.

**The family rule.** Every input to `adverse`, `qual`, `disp` and `eff` obeys three clauses:

- **start**: machinery may make a failing assessment start counting only on an admitted fact or in its own lineage; once started in the admitted state it never stops there by machinery;
- **stop**: only a judgment that addresses it, or evidence that discriminates in the observations, stops it;
- **standing**: a stop earned by supersession stands on immutable facts and its own record's standing, in the states where that record acts (§5.2), never on the currency of the content it ran on; a stop by discriminating observations holds in each frame exactly while that frame's observations show it.

#### 6.2 Applicability dimensions

| Owner dimension | Role here |
|---|---|
| protocol obligation | the evidence obligation `e`. Assessments for different obligations never conflict. An obligation that stops being required keeps its disagreement in `qual`: retirement is not a disposition |
| input/validity regime; every environment, backend, precision or configuration attribute the specification **fixes** | **admissibility** (§17.4), against the specification revision the realization instantiated: an assessment outside them is inadmissible for `e` and enters neither side |
| stochastic replicate identity; every execution attribute the specification leaves **free** (backend, precision, environment components, device, host or hardware attributes) | **execution variation**: admissible assessments differing only here conflict; every permissive use treats a difference in a recorded one as a difference (§6.5) |
| everything the execution read; the claim content and the oracle and tolerance semantics applied | **assessed content** (§6.3): decides the rerun obligation and `stale`; never decides whether a failing assessment starts counting |
| subject/candidate | **frame**: a failing assessment counts in its own lineage's frames from its admission, and in the admitted state and other lineages' frames once its obligation is required there (`starts`) |
| everything else in the basis | **provenance**: can end the assessment's currency, never its adversity |

#### 6.3 Assessed content

A failing assessment's **assessed content** is recorded at admission as content identities and never changes:

- **executed content**: everything the realization's execution read — the specification unit; the closure of execution content under declared and derived `EXECUTION_DEPENDS_ON` (class `EXEC`) widened by §4.6; and every read the designated runner observed. Only a current completeness judgment bounds the closure (§4.6 governs every closure); observed reads add read entries and never bound it, so where no judgment bounds the closure the widening reaches the whole tree (refinement R1 drops the reviewed alternative bound "the runner's observed reads are complete", a restrictive change). A read of Git data other than the realization's tree (another commit, the index, the object store) is an external read. Every **execution attribute** the runner class records (§17.5), whether environment components (interpreter, standard and system libraries, compilers, toolchain) or backend, precision, device and host or hardware attributes, is recorded as an attribute entry (below), never treated as configuration unless the specification fixes it (§17.1); files the execution itself wrote are outputs, not inputs. Any other read of a file absent from the realization's tree, or of a network resource, is an **external read**, recorded by content identity where it can be pinned (§20.1) and otherwise as unpinnable; an unpinnable read keeps the observation out of every permissive use (§6.5), so it supports no mechanical stop, while its adverse uses are unchanged. An external read the runner did not observe is recorded nowhere, so absence of a recorded external read counts only for an execution whose runner class declares that it observes every read outside the realization's tree (§17.5); every other execution is recorded as having an unpinnable read (SD-18);
- **reading**: the specification revision whose oracle and tolerance semantics it applied, and the claim content it read.

**Recorded execution basis [D3 decision; refinement R1].** The executed content is recorded **once**, in the `REALIZATION` record, at the granularity the closure and the runner reached. Every consumer reads this one record: the realization's own currency (§4.1, §17.4), both matching predicates (§6.5), conditions (1)-(4), the floor and the class rule (§6.8). It holds:

- **unit entries**: for every unit the closure reached, including the specification unit, `(u, r_u, [(t_1, c_1), …, (t_k, c_k)])`: `u`'s identity, its revision `r_u` in the realization's tree, and each of `u`'s declared scope terms `t_i` in the structure the execution ran under (`Σ` at its position, or `Σ_n ⊕ Δ_Σ(X)` for a realization in the frame of `X`) with `c_i = cid(t_i, tree)` (§1.5), the content identity of its resolved region (`ABSENT` included). A residual part `<id>.~` is recorded by its composite's terms together with the terms of every unit that owns bytes inside the composite's regions at the realization by §1.4 rule 3 (its members, and any unit nested there by resolution), and denotes the composite's resolved regions minus those units' resolved regions; its content identity is `cid` (§1.5) over the denoted bytes in path and offset order;
- **read entries**: for every file of the realization's tree the designated runner observed being read, `({ path = p }, cid)` with `cid` over that file in the tree, whether or not the file is governed; a read through symbolic links records every link the resolution traversed, as `({ path = link }, cid)` over the link entry itself, and its resolved target, as a read entry when the target is a file of the tree and as an external read otherwise; a read inside a submodule is recorded as a read entry on the gitlink's path, whose identity is the recorded commit (§1.5); a read of any other file absent from the tree is an external read (pin entries);
- **widened entries**: only where the closure widened (§4.6). A composite step is recorded through the composite's own unit entry. For each directory step `d` of the chain, `({ prefix = d }, cid)` over the governed files under the frozen `ignore` patterns; for the whole-tree fallback, a record-only entry `({ tracked = "*" }, cid)` (not a manifest scope term) over **every tracked path, governed or ignored**, resolved without `ignore` patterns, each with its entry type and mode, so the fail-closed default denotes the whole tree the execution could read. Each entry fixes that scope's membership and content;
- **pin entries**: `(locator, pin)` for every external read pinned by the §20.1 grammar; an unpinnable external read is recorded as such;
- **attribute entries**: `(attribute, value)` for every execution attribute the runner class declares it records (§17.5), fixed or free: environment components (interpreter, libraries, compilers, toolchain, runner image) at the granularity the class declares, and backend, precision, device and host or hardware attributes; and its seed or replicate identity where the runner supplied one, which every runner class records (SD-18). An execution that does not record a declared attribute, or a seed the runner supplied, is treated as having an unpinnable read. Whether an execution counts as having an unpinnable read, and the declared attribute set and read-observation flag of its runner class, are decided at realization under the policy in force there and recorded by value in this basis, so a later policy change never changes `ext` for it;
- **resolution context**, recorded by value inside the execution basis and computed together with its terms at the execution's start position, never inferred from the record's envelope `ruleset`: the system ruleset identity in force there (and so the SSDS system version, which fixes normalization, the scope-term grammar and its resolution, wildcard semantics and the content-identity encoding, §1.3, §1.5, §27.3), the `ignore` patterns of `Σ`, and the analyzer set of `ρ`;
- the completeness judgments that bounded the closure, or `UNBOUNDED`.

**Re-resolution.** `resolve_o(t, K)` re-resolves a recorded term in content `K`, and `cid` hashes it, entirely under `o`'s recorded resolution context: its system version's semantics, its `ignore` patterns and its analyzer set, never the current system version, `Σ`, `ignore`, analyzers or policy. Resolution is term-level (§1.3): the overlap rule of §1.4 rule 3, which depends on other units' terms, is not applied to recorded terms. **Guard [refinement R1]:** `on⁻(o, K)` is a function of `o`'s record and `K`'s bytes alone; every semantics used to resolve and hash a recorded term is the one named in `o`'s record, so no ledger-named input adopted later (ruleset, system version, policy, structure, analyzer set, completeness standing, loss boundary) can change it. Effective structure, the governed boundary and analyzers were used to *choose* what to record; afterwards nothing current changes what the record denotes. A derivation host must hold every system version and analyzer set a recorded execution basis it matches names, as it already must for historical views (§5.8, §27.3); a host lacking one makes no current assertion (§5.9). Every scope-term resolver is a pure function of file bytes under its pinned identity (§1.3, §14.5), so re-resolution never needs a host input or a later record. Any future classification of what an execution read is stated only through this guard and the construction rule of §6.5. Regions the closure did not reach are not recorded, so a change outside them (another span of the same file, another unit's file outside every widened entry, an ignored file that no read entry names) changes no comparison with this record.

The **realization's tree** `tree(o)` is the commit the execution ran on; the ledger keeps it reachable (§21.4).

#### 6.4 Start: anchors, home, about, starts

Admission records each failing assessment's **anchors** in two sets that never change: its **admitted anchors** (every subject whose scope contained the evaluated target in the admitted state at the request's base) and, for a frame record, its **frame anchors** (every subject whose scope contains the target in its frame). Nested subjects are included in both. A frame record's **lineage** is that of the transformation it was made in: the bound obligation for which that transformation was produced, as its signed result envelope records (§7). The lineage's frames are those of every transformation produced for that obligation, iterations and rebases included; never the reviewer's or assessor's own task obligation. A record made in the admitted state has no frame lineage.

**Admitted**, for the start latch, means present in the observed tree, or required, in the admitted state at some ledger position, by any route: integration, absorption or adoption. Every question about which reading or check governed a failure asks what was **in force at its base**: present in the admitted state at the base position, never merely "ever admitted". A failure's **base** is the admitted state its frame was merged onto, or its own position for a record made in the admitted state.

Every formula below is evaluated in one frame `G`: the admitted state `D_n` or a frame `D_n[X]`. The subscript is dropped where clear.

```text
anchors_G(a⁻) = admitted anchors ∪ (frame anchors, if G is a frame of a⁻'s lineage)
home_G(a⁻)    = succ*(anchors_G(a⁻)): those anchors and every effective subject that received regions of a
                subject in home_G(a⁻) by an admitted structural change since a⁻'s base position   -- S0 fold
about_G(a⁻, s) ⇔ s ∈ home_G(a⁻)
               ∨ s has a required evidence obligation in G in the lineage of the obligation a⁻ names
                 (its retargets, splits and renames)
               ∨ the evaluated target lies within scope(s) in G and within no scope of home_G(a⁻)   -- additions only
starts_G(a⁻)  ⇔ G is a frame of a⁻'s lineage
               ∨ the obligation a⁻ names, or one in its lineage, is required in the admitted state at some
                 position ≤ n                                                   -- monotone latch over positions
               ∨ G is a frame and that obligation, or one in its lineage, is required in G
adverse_G(s, e) = { failing assessments a⁻ admissible for e : starts_G(a⁻) ∧ about_G(a⁻, s) ∧ ¬stale_G(a⁻) }
```

`starts` and `about` read only record syntax, the admitted history of effective structure, the observed trees and the frame's fixed identity, so they are S0.

**Guarantee: `home` is never shed.** Nothing removes a subject from `home`, so no change outside a disposition sheds a dispute from the subjects that held the claim when it was disputed. The other two terms of `about` are best-effort additions: they follow the obligation's lineage and, while no home subject still contains the evaluated content, the content itself. A claim moved and also edited, with its obligation replaced rather than retargeted, is not followed and stays disputed at home; byte-identical copies elsewhere attach nothing while the claim is at home. This bounded clone-tracking is a disclosed limit (§32), not a guarantee.

**Where counting starts.** A failing assessment counts in every frame of its own lineage from its admission. In the admitted state and in other lineages' frames it starts at the first position at which its obligation, or one in that obligation's lineage, is required there: at once for an obligation already admitted (including a candidate's failure of an admitted test); for an obligation the frame introduced, at the integration, absorption or adoption that first admits it, by any route. From then on it counts in the admitted state at every later position whatever happens to the content. A failing test-first specification in a rejected or abandoned iteration therefore costs nothing outside its lineage; a claim revised inside an existing evidenced unit, or a check tightened inside an existing specification, belongs to an admitted obligation and counts at once.

#### 6.5 Matching: configuration, outcome and the two matching predicates [refinement R1]

**Configuration.** A realization's configuration is its specification unit identity, regime, parameter instance, and every execution attribute the specification fixes (§17.1), a seed or seed policy it fixes included. This is the only definition. A realization's observed values of the attributes the specification leaves free, a free seed or replicate identity included (SD-18), are its recorded execution attributes (§6.3, §17.2), never part of its configuration: "of `conf(a⁻)`" in (1)-(4) includes runs that differ from `real(a⁻)` in a free attribute, and only `ext`, in permissive uses, separates them.

**Evaluated outcome.** The part of an observation the specification's oracle reads, recorded by content identity as a canonical outcome object (§17.3). Logs, timestamps, host names, paths and line numbers are never part of it unless the specification names them. A specification that declares no evaluated outcome supports no mechanical stop; its failures go to the assessor or owner. A failing assessment records `failing_outputs`, the declared outputs it found failing (a mechanical oracle reports them; an assessor names them); one naming none found every declared output failing. Below, `F(a⁻)` is that set and `out(o)|F` the restriction of observation `o`'s outcome to it.

**Output identity across specification revisions [D3 decision].** An output's identity is `(specification unit id, output name)`. A specification revision that renames an output declares the mapping in its `output_renames` field (§17.1); without one, the old output is "not evaluated" by the new reading.

**Matching predicates.** For an observation `o` and content `K` (a tree, or a frame's content):

```text
on⁻(o, K)  ⇔ every recorded term (t, c) of a unit, read or widened entry of o's execution basis has
             cid(resolve_o(t, K)) = c                                   -- tree-resident terms only
ext(o, x)  ⇔ neither o nor x recorded an unpinnable read
             ∧ o and x record the same set of (external locator, pin) pairs                -- SD-23
             ∧ o and x record the same value for every execution attribute either records (§6.3)
bound(o, K) ⇔ o's recorded basis is not UNBOUNDED (its closure never reached the whole-tree fallback, §4.6)
             ∧ every judgment c that bounded it is a COMPLETENESS judgment with outcome COMPLETE
               that holds for K (SD-58, Manual A8):
                 c stands (acts, unsuperseded, CLEAR, held, independent, not vetoed),
                 c's membership digest and every content entry of c's basis are those of K,
                 and every other basis entry of c holds in the frame of evaluation
                 (a cited record current at T; a standing entry at base T; a machinery c's analyzer
                 in the analyzer set; a validity or execution entry fails closed)
on⁺(o, K)  ⇔ on⁻(o, K) ∧ ext(o, real(a⁻)) ∧ bound(o, K)    -- a judgment-bounded basis only
             -- every permissive use concerns one failing assessment a⁻
```

**Construction rule for the family [refinement R1].** `on⁻` compares only tree-resident recorded terms (unit, read and widened entries), re-resolved under the frozen context. Every other dimension of "the same content" is stated as a class, never a list: **whatever can distinguish two executions of one configuration and is not tree-resident recorded content** (every external input, by its pins or an unpinnable read, and every recorded execution attribute the specification leaves free: backend, precision, environment components, device, host or hardware attributes, whatever the runner class records, and a free seed or replicate identity; an external read the runner could not observe counts as unpinnable, §6.3), together with whatever bounds the recorded basis (a bounding completeness judgment that holds for the content matched; an `UNBOUNDED` basis serves no permissive use), appears only in `on⁺`'s further conjuncts, and `ext` requires identity with the failing realization over the whole class: the same complete set of external locators and pins (an observation that read a different, smaller or larger set never serves a permissive use; SD-23) and the same value for every recorded execution attribute. An attribute a runner class records later is in the class by definition and needs no new clause. Variation in an attribute no runner class records is invisible to both predicates and is a disclosed residual (§17.5, §32.2). An attribute the specification fixes is equal for every admissible realization (§17.4), so comparing every recorded attribute compares exactly the free ones; a recorded attribute that a fixed declaration does not determine (a host-mounted driver under a fixed image) is free (§17.1). So `on⁻` reads no S2 value, no current system version, structure, `ignore` or analyzer, and no input outside the tree (the guard of §6.3), and its granularity is the reviewed `on`'s: the content identity and membership of every unit and widened scope `o` recorded, never whole files that merely contain a recorded region. An unfixed external input or a free execution attribute is execution variation (§6.2): two runs on the same tree that read different pins, that differ in a recorded free attribute (a CUDA and a CPU node; `float32` and `float64`; seed 17 and seed 42), or where either read an unpinnable input, are on the same content adversely, so a differing outcome between them defeats (2) and a yielding one keeps (4) false; permissively they are not, so neither reproduces the other in (1), and a run observed in `G` stands for (3) only if it read the failing realization's pins and recorded its value for every recorded execution attribute. `on⁺` is `on⁻` with further conjuncts, and `on⁻(o, K) ⇒ link⁻(o, K)`, so **`on⁺ ⇒ on⁻ ⇒ link⁻` holds by construction** for every `o`, `K`, `Σ`, `ignore`, analyzer set, external input and execution attribute. The completeness conjunct reads completeness positively only (a holding judgment can only enlarge the set of permissive matches), so losing completeness (a judgment provisional, blocked, revoked, superseded, vetoed, withheld by a loss boundary, over a membership that is not the matched content's, or with a cited record no longer current) can only shrink permissive matches; it can never remove an adverse match, and no structural change can make an observation usable permissively while excluding it adversely. **Every use below names its predicate. Permissive uses — those that can make a failure stale or lower a decision class — use `on⁺`. Adverse uses — those that keep a failure counting — use `on⁻`, and conditions (2) and (4) use `link⁻` (§6.6), which contains it.** `link⁻` links an observation to content through any admitted observation of the configuration whose recorded basis matches both trees, so a run recorded at a different width than the failing run is never hidden from the adverse conditions by the width alone. An observation with an unpinnable read satisfies `on⁺` for no failure; its adverse uses are those of any observation.

**Verdict functions per reading [D3 decision].** A mechanical oracle is one of:

- **declarative**: a fixed check template over declared outputs (`EXACT`, `ABS_TOL`, `REL_TOL`, `ULP_TOL`, `RANGE`, `SET_EQUAL`, `MONOTONE`, §14.3), parameterized by the specification revision. Its verdict `verdict(ρ, o, x)` under any reading `ρ` is recomputed by Derivation from `o`'s stored outcome; deterministic and memoized;
- **embedded**: the execution itself produces per-output verdicts (a test runner's per-test results). The verdict under the reading the execution ran is the recorded one; under any other reading it is **not computable**.

Where a verdict is needed on an output `x` that `G`'s reading evaluates and it is not computable, the failure is treated as yielded on `x` (fail closed). An output that `G`'s reading does not evaluate is governed by the "either" clause of §6.6, never by computability.

#### 6.6 Stop: staleness by discriminating observations

```text
stale_G(a⁻) ⇔
    (1) reproduced                     [permissive: standing, on⁺]
        some standing admitted observation o ≠ real(a⁻) of conf(a⁻) with on⁺(o, tree(a⁻))
        has out(o)|F = out(a⁻)|F
  ∧ (2) never differed                 [adverse: any standing, link⁻]
        every admitted observation o of conf(a⁻) with link⁻(o, tree(a⁻)), whatever its standing,
        has out(o)|F = out(a⁻)|F                    -- otherwise nondeterministic in fact
  ∧ (3) observed here                  [permissive: standing, on⁺]
        some standing admitted observation o of conf(a⁻) has on⁺(o, G)
  ∧ (4) not yielded here               [adverse: any standing, link⁻]
        no admitted observation o of conf(a⁻) with link⁻(o, G), standing or not, yields a⁻'s failure
        on any x ∈ F(a⁻) under G's reading

link⁻(o, K) ⇔ ∃ admitted observation o' of conf(a⁻) : on⁻(o', K) ∧ on⁻(o', tree(o))      -- adverse only; S0
              (o' = o gives on⁻(o, K); o' = real(a⁻), or the bounded reproduction (1) requires, links any run on a
               tree that agrees with K on that record's content, whatever the width o itself recorded;
               o' ranges over every admitted observation of conf(a⁻), INCOMPLETE ones and those of never-integrated frames
               included, whatever its standing; a partially recorded basis only links more)

Invariant: every stop rests on a narrow record of the failing run's content: (1) needs a bounded
reproduction on tree(a⁻), and that record anchors link⁻ in (2) and (4).

yields a⁻'s failure on x under G's reading:
  mechanical oracle    the verdict on x under G's reading is FAIL, or not computable; where the admitted state
                       holds G's specification revision only by absorption, the verdict is also taken under the
                       last revision an admission integrated, and the failure is yielded if either fails
  assessor-read oracle no standing discriminating reading of a⁻ covers o under G's reading
  either               o lacks x, or G's reading does not evaluate x, while a⁻'s check on x was in force in the
                       admitted state at a⁻'s base

standing (permissive uses only; the adverse conditions read observations whatever their standing):
  an observation stands iff cont holds for it, its realization has no upheld challenge and no open blocking
  challenge (overridden or not: a risk override never resolves a challenge), and it is not INCOMPLETE;
  completeness standing enters only through on⁺
```

`INCOMPLETE` observations have no evaluated outcome and enter none of (1)-(4).

**Discriminating reading (assessor-read oracles).** One `EVIDENCE_ASSESSMENT` in mode `DISCRIMINATING`, by a qualified assessor independent of the claim's authors, of an execution of `conf(a⁻)`, recording in one record `PASS` for that execution's outcome under the reading in force there and `FAIL` for `a⁻`'s reproduced outcome under `a⁻`'s reading, both on `F(a⁻)`. Where its two readings differ, it names the material difference between them by a reason code and a content reference. Admission refuses it where the two readings are the same and the two outcomes on `F(a⁻)` are identical: one outcome cannot be read both ways under one reading.

**Coverage.** A standing discriminating reading `d` of `a⁻` covers, in any frame `G`, every observation whose evaluated outcome on `F(a⁻)` is identical to the outcome `d` read `PASS`, while `G`'s reading is the one `d` read under. Content identity plays no part: what the oracle reads is the outcome under a reading. A reading under a specification or claim revision that the admitted state holds only by absorption covers nothing there until an admission integrates that revision. `d` stands iff `cont(d)`, it is not superseded, `status1(d) ∉ {REVOKED, BLOCKED}`, and the realizations of both observations it reads stand.

**What the four conditions keep.**

- **Discrimination, not repetition.** For a mechanical oracle (4) reads each outcome's verdict. For an assessor-read oracle a value alone discriminates nothing, so (4) needs one record reading both outcomes: a rerun yielding the failing outcome, or an outcome perturbed in low bits that still shows the defect, never makes the failure stale, and a later assessor's ordinary `PASS` of a new outcome never settles it by being later. Interpretive disagreement over one outcome under one reading goes to `a⁻`'s assessor, the owner's adjudication or `IMMATERIALITY`.
- **Nondeterminism goes to the owner.** (1) needs an identical second execution on the content `a⁻` read, with its pins and recorded execution attributes, and (2) no other outcome on that content, ever, under any free attribute.
- **Standing per frame, without lapse by change.** After a change of `G`'s executed content, `a⁻` counts again in `G` until one execution on the new content with `real(a⁻)`'s pins and recorded execution attributes (normally the same execution that refreshes the obligation's passing evidence, which is stale too, when it ran with them; otherwise the rerun obligation of §6.9) shows it not yielded; a revert yields it again. For an assessor-read oracle an outcome identical to one a standing reading read `PASS` is covered with no new reading, whatever else changed; only a genuinely new outcome needs one new reading.
- **One reading per frame.** A mechanical verdict is computed under `G`'s reading, so a candidate's tightened tolerance or test-first case is stale in the admitted state as soon as the admitted reading passes the admitted outcome in runs that satisfy (1) and (3); an output shift the admitted reading still passes keeps it stale; an editorial reading variant gives the same verdict and never makes a real failure stale.
- **Removing a check.** An output `G` no longer evaluates makes nothing stale when `a⁻`'s check on it was in force at `a⁻`'s base: removing a check is a specification change the owner disposes of. When the check was the candidate's own addition, its absence from the admitted reading is why the failure does not apply there.
- **Accepted change of the admitted reading.** Under a declarative mechanical oracle, an admitted specification revision that the admitted outcome passes makes an earlier mechanical failure stale; the review brief of every specification change lists, as a required item, the counted failures it would make stale and the discriminating readings it would stop covering (§16.5). Under an assessor-read oracle an admitted reading change raises reassessment or a discriminating reading under the new reading.
- **Bounded and unbounded bases.** Only an observation whose basis a current completeness judgment bounds serves (1), (3) or the class rule's candidate-own test (`on⁺` needs `bound`), so a failure whose stop would need an unbounded run goes to the owner. An unbounded basis records the whole tree (§6.3): it is fail-closed for currency and for every permissive use, and it is not used to stop anything; its own `on⁻` matches only an identical tree, although through `link⁻` an unbounded run is still linked to any tree that agrees with a narrow anchor. A differing or yielding run recorded unbounded (because no judgment was current when it ran: a lapse later restored, a judgment admitted after the run, an analyzer upgrade) on a tree that differs from the failing run's only outside a bounded failure's recorded content is still in that failure's (2) or (4), through `link⁻` with `o' = real(a⁻)`.
- **Completeness and structure polarity.** Losing a completeness judgment never removes a differing old-content run from (2) or a yielding present-content run from (4), whatever width that run recorded, because both use `link⁻`; it only stops a narrow-basis observation from serving (1) or (3). A change of effective structure, of the governed boundary or of an analyzer never changes `on⁻` at all, because the recorded execution basis carries its own resolution context (§6.3); it can only make a bounding completeness judgment stop holding (a cited record no longer current, a machinery judgment's analyzer no longer in the set; its membership and content entries are read on the matched content, SD-58), which again only narrows (1) and (3). A change outside the recorded regions never changes `on⁻` either: a run on content that differs from `tree(a⁻)` only in another span of a recorded file, in another unit's file or in an ignored file stays in (2), and a run on present content that differs only there stays in (4). A claim is never made less qualified by discarding an observation or by making an unrelated passing assessment stale.

#### 6.7 Stop: effective disposition

A record `d` **disposes of** `a⁻` when:

- `d` supersedes `a⁻`, directly or through a chain of supersessions: an explicit reassessment of the realization by `a⁻`'s own assessor, or the owner's adjudication;
- `d` is an `UPHELD` adjudication of a challenge targeting `a⁻` or its realization `real(a⁻)` (the only premises whose revocation discredits the observation); an upheld challenge against any other premise disposes of nothing;
- `d` is an `IMMATERIALITY` judgment covering `a⁻`.

```text
eff(d, a⁻) = F                                  nonind(d) (§5.10 (a))
           = base(d)                            otherwise, d a supersession; S1 constants only
           = current(d)                         otherwise, d an IMMATERIALITY judgment
           = T if in_force(d) ∧ cont(d) ∧ ¬contested(d), else F      otherwise, d an UPHELD adjudication
contested(d) ⇔ ∃ c ∈ CHALLENGE : c.target = d ∧ c.blocking ∧ open(c)       -- counter-challenge or not
disp(a⁻)     = ⋁_{d disposing a⁻} eff(d, a⁻)
```

A supersession stands, in the states where it acts (§5.2), on immutable facts: not superseded, not revoked or blocked, held across any boundary; an open blocking challenge removes it and a risk override caps it at `P`. `IMMATERIALITY` stands at its own currency, since its premise is about the current governing state. An upholding stands while in force, held and uncontested; an open blocking challenge against it suspends its disposing effect while its revocation stays (each effect keeps its own polarity). A disposition names `a⁻` in `identity` mode, so a challenge against `a⁻` never changes the disposition's currency.

**What does not end a disagreement:** an open challenge against `a⁻`, overridden or not; a loss boundary (the disposition is withheld and observations from before it make nothing stale); a positive-only requalification or attestation; any content or structural change; a passing assessment of another realization or configuration, or a passing rerun that yields `a⁻`'s outcome; the rejection, abandonment or integration of `a⁻`'s candidate; an upheld challenge against another premise; retirement, split or retargeting of the obligation; an unauthorized later passing assessment; an `IMMATERIALITY` whose basis moved; a fallen superseder; ledger order.

**Re-disposal** after a disposition stops standing uses existing records: a new `IMMATERIALITY`, a further supersession of `a⁻` (a record may have several superseders), or a supersession of the fallen superseder. Staleness needs no re-disposal: it is read afresh in every frame.

#### 6.8 Decision class, independence and floor events

Staleness is not a decision: it is derived from designated-runner observations (R0) and, for an assessor-read oracle, a recorded discriminating reading.

**Admitted-content test.** `adm(a⁻)` ⇔ `a⁻`'s reading (specification revision and claim content) was in force in the admitted state at its base, and either `on⁻(real(a⁻), T_b)`, where `T_b` is the admitted observed tree at `a⁻`'s base, or `real(a⁻)`'s basis is `UNBOUNDED` (its closure reached the whole-tree fallback, §4.6, §6.3). For a bounded basis it reads the one recorded execution basis at its recorded granularity, so a candidate change outside the recorded regions leaves `adm(a⁻)` true; an unbounded basis, which records the whole tree, cannot separate the candidate's change from the admitted content, so it is taken as admitted content. The floor uses `adm`, and the class rule uses `¬adm` together with `on⁺`, which needs a bounded basis; both directions are therefore conservative.

- **Independence.** Every judgment disposition, the failing assessor's own reassessment included, carries an independence requirement against `authors` of the claim content, with the owner exception and the common-mode record; `authors`, the test and the exception are defined once in §5.10 (a). A disposition with `nonind` has `eff = F`.
- **Class.** `IMMATERIALITY` judgments, and supersessions or adjudications disposing of another actor's failing assessment, are R2; R3 where any subject `a⁻` is about is, or has been, D1 or D2 authority. A discriminating reading is R2; it is R3 where any such subject is or has been D1/D2, **unless the failure is shown to be the candidate's own**: either this reading's passing observation `p` has `on⁺(p, T_b)` and `¬adm(a⁻)`, or a standing reading has already shown that. A reading of later admitted content may carry a fix of a failure the base already had, so it is R3 unless already shown candidate-own. Admission checks the class from S0 facts and bounding completeness (through `on⁺`, §6.5); the highest class reached latches. An adjudication obligation that no available agent can make independently is routed to a human mechanically.
- **Floor event (D1/D2).** Where any subject a failing assessment is about is, or has been, D1 or D2 authority, a failing assessment that counts in the admitted state, for any obligation `qual` reads, on a claim having any admitted passing assessment, becomes a **floor item** at the first position at which, with no disposition standing and while not stale there, one of these holds: `adm(a⁻)`; for a mechanical oracle, an admitted observation `o` with `link⁻(o, T_m)`, at a position `m` where the failure counts in the admitted state, yields it under the admitted reading; for an assessor-read oracle, an admitted observation of admitted content has `a⁻`'s identical outcome under `a⁻`'s reading (so no reading can be admitted), or its reading obligation is answered by a failing assessment of the admitted outcome, closes into the owner's adjudication, or needs an R3 reading; (2) has failed; or an execution scheduled for it ended `INCOMPLETE`. The event is evaluated once, latches, and creates human attention keyed on the failing assessment's existence, closed only by an authenticated human judgment (which may record it `MOOT`). The inspector digest shows the failure before the event.

#### 6.9 Scheduling

When `a⁻` counts in `G` with no disposition standing and it is not stale there, S3 derives a **rerun obligation** for what (1) or (3) lacks: one reproduction on `tree(a⁻)`, and one execution of the configuration on `G`'s content (which `G`'s own affected-evidence rerun supplies when it ran with them), each with `real(a⁻)`'s pins and recorded execution attributes, since no other run can serve (1) or (3) (§6.5). Whether a runner of the class with those attributes is available is the Dispatcher's operational decision (§10.3); while none is, no run serves (1) or (3) and the failure stays with the owner (§6.10). For an assessor-read oracle whose observed outcome in `G` no standing reading covers, it derives one **reading obligation**, held by an independent reviewer at the class above: read `a⁻`'s reproduced outcome and `G`'s observed outcome in one assessment, recording a discriminating reading or a failing assessment of `G`'s outcome. A reviewer who disagrees with `a⁻` over one outcome under one reading can record neither; the reading obligation then closes into the owner's adjudication obligation. Where (2) has failed, or no current completeness judgment bounds the configuration's execution closure (so no run could serve (1) or (3)), nothing is scheduled: the failure is the owner's.

The Dispatcher keeps at most one outstanding execution per configuration, required execution attributes and frame, on the frame's latest content. Every designated-runner execution it starts ends in an admitted, never-lost observation: complete, or `INCOMPLETE` when the execution fails, cannot start or exceeds its time bound. **[D3 decision]** The specification declares the time bound; the system caps it at **168 hours** of wall-clock time from start for Dispatcher-run executions. Longer realizations run under external custody (§17.5). Observations hosted by a policy-designated external custody runner make nothing stale unless its `CUSTODY_ENUMERATION` lists every run of the configuration it performed; every enumerated run counts for (2) and (4). A run admitted late is read when it arrives, so no run can be hidden from (2) or (4).

#### 6.10 Effects and uniqueness

A live disagreement makes `undisputed(s, e) = P`, so `ev`, validity and discharge are visibly provisional (§10.4), and briefs and gate views label the evidence `disputed`. S3 derives an adjudication obligation for each adverse assessment with no standing disposition, routed to the claim's owner; the inspector view shows which observations make each failure stale, so resolved reassessment stays distinguishable from live disagreement. `stale`, `adverse`, `qual` and `disp` preserve the monotonicity argument of §5.6.

**Stochastic specifications.** For a specification with free stochastic attributes, the assessed unit is the declared assessment granularity (§17.3): an ensemble specification's realization is the whole ensemble and its evaluated outcome is the declared ensemble statistic in canonical form; replicate variation inside one realization is not disagreement. Ensemble assessments of the configuration still disagree when they differ. A free seed is a recorded free attribute (§6.5): (1) and (3) need runs with `a⁻`'s seed, which replays it as a fixed seed policy would, while every run on `a⁻`'s content under another seed enters (2) and (4), so a seed-dependent failure goes to the owner as soon as another seed has been observed there; a runner that cannot replay a recorded seed supplies no run for (1) or (3), and the failure goes to the owner. Randomness the runner does not supply (a generator the code seeds from the clock or the operating system) and scheduling nondeterminism have no recorded seed: they are unrecorded variation, caught only when a differing run on the same content is observed and defeats (2) (§32.2). Acceptance never depends on the latest single replicate: a later passing ensemble neither supersedes nor disposes of a counted failing one, so edit-and-rerun is not a route to a pass.

### 7. Transformation frames

#### 7.1 Transformation identity

A **transformation** is `X = (B, C, A)`: `B` the recorded base (an admitted integration commit); `C` an immutable candidate commit on an isolated ref; `A` the exact set of quarantined structural deltas its producing request adopts by `ABSORB` dispositions (§18), possibly empty. `id(X) = sha256("ssds.transformation.v1" ‖ B ‖ C ‖ JCS(sorted A))`. `id(X)` is fixed by the task result that first submits the candidate; no later request changes what that result's transformation adopts. `Δ(X)` is the set of effective units whose revision in `tree(C)` differs from `B`; `Δ_Σ(X)` is the set of structural-declaration changes `C` authors relative to `B`, together with `A`.

#### 7.2 Frame state and the fixed merge

At admitted head `n`, the frame `D_n[X]` is `derive` over the same `L_n` with the observed tree replaced by `M_n(X)` and effective structure replaced by `Σ_n ⊕ Δ_Σ(X)`.

**The three-way merge [D3 decision].** `M_n(X)` is the merge of `tree(C)` onto `T_n` with merge base `tree(B)`, computed by the system version's pinned implementation with these semantics: path-level three-way merge with no rename or copy detection; a path changed on one side only takes that side; a path changed identically on both sides takes it; a text path changed differently on both sides is merged line-wise by the diff3 rule with a fixed diff algorithm and succeeds only when no hunk overlaps; any other both-sides change (binary content, file mode, symlink target, delete versus modify, add versus add with different bytes) is a conflict. A declaration key (§1.2) whose value `tree(C)` and `T_n` both change relative to `tree(B)`, to different values, is also a conflict, even where the manifest's lines merge cleanly; so every key of `Δ_Σ(X)` has in `M_n(X)` the value `C` gave it, and `Σ_n ⊕ Δ_Σ(X)` is exactly the structure integration enacts (§8.3 step 4(a)). Repository attributes, custom merge drivers and rerere never apply. A conflict means the frame does not exist (§7.4). The implementation is part of the system version: changing it is a system version change (§27.3), never a configuration. **[delegated]** The diff implementation, within the pinned determinism requirement.

In the frame, the declarations in `Δ_Σ(X)` are not quarantined (they are the proposal under judgment); every other quarantined delta stays quarantined.

#### 7.3 Basis-entry roles

Every `content` entry `(u, r)` of a frame-`X` record, and every unit entry `(u, r_u, …)` of an `execution` entry, has exactly one role, computed mechanically from `B`, `C` and the entry (for a unit entry, "has `r`" means its recorded terms re-resolve to their recorded identities):

| Role | When | Satisfied before integration (in `D_n[X]`) | After the integrating admission `k` |
|---|---|---|---|
| **before-image** | `u ∈ Δ(X)` and `r = rev(u, B)` | while the live head still has it: `rev(u, T_n) = r`; otherwise rebase or re-review | a fixed fact about what `k` transformed: satisfied, like `identity` |
| **output** | `u ∈ Δ(X)` and `r = rev(u, C)` | `rev(u, M_n(X)) = r` (a unit changed on both sides is judged at its merged revision) | ordinary currency in the admitted state |
| **context** | `u ∉ Δ(X)` | ordinary currency in `D_n[X]` | ordinary currency in the admitted state |
| — | `u ∈ Δ(X)` and `r` neither | never | — |

`validity`, `record`, challenge-tier and loss-boundary facts are evaluated in `D_n[X]` before integration and in the admitted state after. A `record` entry is satisfied only by a record that acts in the state at hand (§5.2) and is current there: in `D_n[X]`, an admitted-frame record, a record of an integrated enactment or one of `X`'s own enactment; a frame record of another pending enactment, an earlier iteration of `X`'s obligation included, supports nothing (R12). An admitted-frame record evaluated in `D_n[X]` is evaluated against `M_n(X)`, exactly as it will be after `X`'s integration. No frame designation transfers currency.

#### 7.4 Existence: inspection, not enactment

The frame exists when the merge is clean and `Δ_Σ(X)` is **well-formed**: every structural check of §8.3 step 4 except the enactment condition — leaf coverage, laminarity and scope conservation (§1.9); governance-mode consistency; source and destination challenge freezes; SDG integrity; release by the old domain owner for a domain change; relation and cycle legality; and a cutover record acting in the frame has `s`'s admitted mode as its source mode (§19.5). In the frame, a subject that `Δ_Σ(X)` creates or restores exists in a **prospective tenure** and is simply not yet valid. Without a clean merge or well-formedness there is no frame, no record in it can be current, and §11 routes a new iteration: machinery never resolves a conflict (K3). `D_n[X]` is never presented as current state, and nothing in `D_n` reads it.

#### 7.5 Declared frame and what frames decide

A task result, a check execution, a realization on the candidate, a review, conformance, assessment or acceptance judgment about a transformation, and a `GATE_DECISION` answering a gate obligation derived in `D_n[X]` for a subject whose revision `X` changes or that `X`'s item requires, with any `PRODUCT_SCOPE_ACCEPTANCE` co-submitted with it, and a cutover `MODE_TRANSITION` that `X` carries (recorded by a human, §19.5), declare frame `id(X)`. Every other record declares the admitted frame. Obligations in `D_n[X]` are derived in that state like any other, so they are the obligations `X`'s integration would produce: the subject triple at `M_n(X)` and, for a `NATIVE` D1/D2 subject, the run `rid` of the frame (§10.2), which is the run that integration starts or the admitted run it leaves unchanged. What a frame record supports, supersedes or relieves has effect only where it acts (§5.2): in the frames of its own enactment, and in the admitted state only once that enactment integrates; an adverse record counts as §5.10 and §6.4 state, whatever its frame. No other frame rule exists (SD-25). An acceptance in frame `X` must name a subject effective in `Σ_n ⊕ Δ_Σ(X)` at its frame `scope_id` and revision; it is a **prospective acceptance**. Evaluated in `D_n[X]`: the conformance of `C` (§14); the readiness and discharge of review, acceptance and gate obligations on `X`; Admission step 6 for frame-`X` records. Nothing evaluated in a frame changes the admitted state: in `D_n` a review, prospective acceptance, gate decision or supersession recorded in `X`'s frame is admitted but does not act (§5.2), and a proposed promotion is still quarantined.

#### 7.6 Integration enacts; prospective acceptance binds once

The integrating admission `k` of `X` admits exactly `M_n(X)` as the observed tree and `Σ_n ⊕ Δ_Σ(X)` as effective structure, in one entry, after the full §8.3 step 4 validation including the **enactment condition**: every promotion, restoration or cutover carries a prospective acceptance that counts for the tenure it starts, and a cutover also meets its conditions 1-6 (§19.5). Its discharge predicate is evaluated in the post-admission state, where before-image entries are fixed facts and output and context entries hold exactly as they held in the frame.

A prospective acceptance `j` made in the frame of `X_0` counts for the tenure that `k` starts iff:

1. **Same enactment**: `k` integrates `X_0` itself, whichever task resubmits it, or a clean rebase of it (§5.2, §7.1). A later iteration is a new enactment and needs its own prospective acceptance (R12, SD-26). A restoration after a demotion is new work under a new obligation.
2. **Same structure**: `Δ_Σ(X) = Δ_Σ(X_0)`.
3. **Basis holds**: `j`'s basis holds, in its roles, in `D_n[X]` at `k`.
4. **First enactment**: `j` has not counted for any earlier tenure. `bind(j)`, the first admission at which 1-3 held and that started a tenure, is a function of the ledger.

`j` therefore counts for at most one tenure; when it ends, `j` leaves `ACC` permanently. Promotion and acceptance take effect together in `k`; the integration request carries no new judgment.

**Rebase.** A rebase produces `X' = (B', C', A')` for the same task, in the same enactment. A frame-`X` record counts for `X'` only if every one of its entries holds, in its role, in `D_n[X']`; a record about structure (a prospective acceptance, a structural review) additionally needs `Δ_Σ(X') = Δ_Σ(X)`. Records never move between frames by assertion. A frame-`X` failing assessment counts in every frame of its lineage, `X'` included, from its admission (§6.4).

## Part III. Admission and concurrency

### 8. Admission

#### 8.1 Admission requests

An **admission request** is the typed result of `submit` (§16.1), built by machinery. It contains: a **request identity**; its **task binding** (the authenticated envelope of the task that produced it, §12.2), which fixes bound obligation, role and contract revision; the obligations whose discharge it claims, possibly none; the base admitted position and base commit; candidate commit(s) on isolated refs, or none for a records-only request; any quarantined structural deltas it adopts; and the records it submits. The admission record that accepts or rejects it carries the request identity, decision, reason codes, the admitted records and the resulting admitted commit. That is the complete identity and audit trail of a change; no change primitive exists.

**Request identity and idempotency [D3 decision].** `request_id = sha256("ssds.request.v1" ‖ JCS(request without request_id))`. A repeated identical request returns the recorded decision and appends nothing. A request with the same task binding and different content is a different request. The Dispatcher retains the request bytes in its journal until the decision is recorded, so a provisional entry lost before admission is resubmitted by identity (§22.4).

Admission is the **sole ledger writer**. Other actors can still move the integration ref (legacy-scope pushes, an external merge button, a force-push, a restore). Such movement has no admitted status: Admission observes it before its next append and absorbs it (§8.6).

#### 8.2 Queue order

Admission processes requests one at a time against the admitted head it holds, as a merge queue. **[D3 decision]** Order is arrival order at Admission (FIFO), except that a request carrying only never-lost records is never delayed behind a request that may need revalidation. Any order is correct, because each request is validated against the head it is appended on (serializable by validation, §9.1); FIFO bounds starvation. **[delegated]** Speculative batching, which must preserve the serial order and revalidate each request at its actual head.

#### 8.3 Validation order

Admission validates, in order, against the admitted head it holds after reconciling the integration head (step 9), and either appends or rejects with recorded reasons:

1. **schema** — every record well-formed under the closed schema (§3.6); bounded secret and sensitive-value checks (§24.1); unknown required semantics fail closed.
2. **reference** — every identity, revision, task, obligation and target exists and matches; a run a record names is its subject's `rid` in the record's declared frame (§10.2); a task envelope's `retained` field equals the retained units `U_X` recomputed at its `issued_at_position` (§5.10 (a)); a record declaring the frame of a rebase `X'` carries `X'`'s `(B', C', A')` and the transformation it rebases, and Admission checks that `tree(C')` is the pinned merge (§7.2) of that transformation onto `B'` and `A' = A`, so derivation knows `X'`'s enactment from the ledger.
3. **authorization**:
   - actor class qualified for each judgment kind (§3.5);
   - acceptance judgments only on subjects effective in the record's frame: in their current tenure (after the request's own structural changes), or for a frame-`X` acceptance in the prospective tenure of `Σ_n ⊕ Δ_Σ(X)` or of a cutover `MODE_TRANSITION` acting in `X`'s frame (§19.5); never on parts, never on a `REVOKED` triple, never on an ill-formed revision, never on a revision any of whose subject's declared terms resolves to `ABSENT` (`AUTH_ILL_FORMED`);
   - the task binding verifies against a Dispatcher issue key in force (§25.2); or, for never-lost records (step 6), against a retired, never-compromised issue key whose retirement record lists the envelope among its outstanding envelopes. A never-lost record under an unlisted envelope is refused, its bytes retained by content identity with the refusal (inert: S0 never reads them), and a re-issue obligation is raised; the Dispatcher resubmits it mechanically (R0) under the re-issued task's envelope with the refusal as provenance, keeping its original actor and lineage class;
   - the envelope names an obligation existing at the request's base and was issued for the role `role(kind(o))` under `ρ_n`;
   - the record's declared `governs` equals its envelope's (§16.9);
   - **independence and adjudication eligibility**: Admission classifies each record with an independence requirement as independent or `nonind` at admission, and admits an `ADJUDICATION` only if it is eligible, both exactly as §5.10 (a) and (e) define; a refused adjudication is refused alone (§5.10 (e));
   - **supersession authority, by the kind of `x` [D3 decision; refinements R8, R9]**: a report only by its raiser (§15.2); an `EXTERNAL_CONSULTATION` only by Admission's mandatory supersession on an adverse consultation (§20.2); a `COORDINATION_DECISION` or `MATERIALITY_RECLASSIFICATION` only by a record of the same kind by the principal of the same plan (principal executions are interchangeable, §12.5; a re-partition per §13.7); every other support-tier record, `EVIDENCE_ASSESSMENT` included, only by a record of the same kind on its supersession target (§5.10 (b)) that is the record's own author's reassessment or the owner's adjudication (§5.10 (a), (d)), independent by §5.10 (a). No qualified peer supersedes another actor's judgment: a contrary judgment by a peer is a disagreement (§5.10). Challenge-tier, observation, admission and lifecycle records are never superseded (S1 resolves challenge-tier records). A record whose `supersedes` is not so authorized is **rejected**, its refusal recorded, and it is never admitted;
   - a discriminating reading is refused where it reads one outcome both ways under one reading, and admitted only at its class (§6.8);
   - the bound role permits each record kind and outcome (§12.3); the request's write set (§1.2, effect-keyed) lies within the bound contract's write scope, and plan units, contracts and verification rules lie outside every role's scope except as §12.3 assigns them; protected surfaces are untouched without their own authority (§25.3).
4. **structure** — on the merged tree `M`:
   - **(a) effective-structure delta.** For every declaration key `k`: if `k ∉ Q_n`, `Σ_{n+1}[k] := decl(M)[k]` (authored change, or none); if `k ∈ Q_n` and `decl(M)[k] = Σ_n[k]`, the request **realigns** and `Σ` is unchanged; if `k ∈ Q_n` and the request carries an `ABSORB` disposition adopting `k`, `Σ_{n+1}[k] := decl(M)[k]`, validated exactly as if authored; if `k ∈ Q_n` and `decl(M)[k] = decl(T_n)[k]`, the quarantine is carried unchanged; any other value routes the request to revalidation. Authored and adopted changes are validated together by the **well-formedness** checks: §1.9; no membership change mixing governance modes without its `MODE_TRANSITION` (§19.1); SDG members never separated; no change of a unit's kind or owning domain without a judgment by an actor qualified for its *current* domain (release by the old owner). An integrating admission must also meet the **enactment condition** (§7.6). Admission never creates quarantine, and repository presence never enters `Σ` except through an adopting disposition.
   - **(b) challenge freeze.** No change to the signature, scope, regions or membership of any subject is admitted, whether it would lose or gain units, while its current revision carries an unresolved blocking challenge (overridden or not) or is `REVOKED`; the freeze applies at source and destination.
   - **(c) semantic structure.** Known relation types of `ρ_n`; direction, layer and subject-kind constraints; cycle legality and SDG rules; single definer (§2).
5. **dependency well-formedness** — challenge-tier targets strictly earlier and of permitted kinds; no `validity` entry on the record's own subject or a part of it; after adding the request's edges (basis entries, equivalence coverage, the edges of existing records whose `validity` endpoints the request's structural changes re-route through `subj`, and the disposition edges that a successor added by the request's structural changes acquires) the static support graph (§5.6) gains no new non-trivial strongly connected component and no existing one grows (a cycle that absorbed content already created is reported, §5.6, and does not block unrelated requests); no equivalence judgment's `validity` entries depend on a consumer of its unit.
6. **currency** — every basis entry of every submitted support-tier record other than a report is satisfied, in its role, in that record's frame at the current admitted head (the admitted state, or `D_n[X]` for a record about `X`). A request carrying content or structural changes is evaluated as a frame record of its own transformation. Otherwise the record is classified stale and routed to revalidation, not admitted. **Never-lost records are exempt**: reports, challenges, failing assessments, adverse judgments (§5.10) and the observations of designated-runner executions. A report's or challenge's basis is provenance, never checked for currency and never consumed by any rule. A failing assessment counts until a disposition stands, and an adverse judgment vetoes while it stands, never according to its context's currency. Never-lost records are checked record by record: whenever Admission rejects a request after authenticating its task binding, for any reason at any step, the rejecting admission record still admits each never-lost record that passes its **own** schema, reference and step-3 checks (a failing assessment's co-submitted realization is salvaged with it when that realization passes its own checks). A never-lost record failing its own checks is recorded as refused, by identity and reason, and S0 never reads it.
7. **legality** — the bound obligation exists at the current head. **Task results [D3 decision; refinement R9]**: every task the Dispatcher issues to an agent role ends with exactly one request carrying its one `TASK_RESULT`, together with whatever judgments, decisions or reports the task submits (mid-task report requests carry none and claim nothing); a second `TASK_RESULT` for one task is rejected. The `HARD` templates that read only the result and its contract (`slots_filled`, `outcome_consistent`, `citations_support`, §14.3) are evaluated at admission; when any yields `INCOMPLETE` or `DISCREPANCY`, every passing judgment and every principal decision record in the request is refused (`CONFORMANCE_RESULT`), while the `TASK_RESULT`, adverse judgments and other never-lost records are admitted and the iteration counts. **Stale retained units [SD-45]**: an integration request is refused (`STALE_RETAINED`) when an enactment for an item revision with the same prose and fixed fields as the one its task was issued for integrated after that task's issue, so its review's judged scope lacks those outputs; the item takes a new iteration whose task records fresh retained units (§10.4, §13.7), as a stale `rid` makes a new run. **One enactment, one integration [SD-26]**: an integration request whose enactment (§5.2) already has an admitted integration is refused (`OBLIGATION_REENACTED`), even when that integration was `OVERTAKEN` or fenced; further work on the obligation, re-application included (§22.2-§22.3), is a new task (R12). Once a judgment obligation is answered (§10.3) in the frame a passing judgment declares, Admission refuses any later passing judgment bound to it there (`OBLIGATION_ANSWERED`); a supersession step 3 authorizes (the author's reassessment, the owner's adjudication) is not refused; a passing `GATE_DECISION` is exempt from that refusal (any qualified holder may add one; each eligible one enters `gterm`'s minimum, §5.5). **Revision assessments first [SD-16, SD-19, SD-22]**: in every frame, Admission refuses a passing `ACCEPTANCE`, prospective or not, and a `GATE_DECISION ACCEPT` on a `NATIVE` D1/D2 triple `(s, σ, r)`, whether bound to a task or recorded directly by an authenticated human, unless a revision-assessment record for `(s, r)` already admitted counts for it (§10.2: in the run, and standing) and the judgment carries a `standing` entry on it (§4.1, §4.3; `OBLIGATION_REVIEW_OPEN`); adverse judgments on it are admitted as always. No override of this order exists. A task result or discharge claim bound to an already-discharged obligation or a non-current contract revision is recorded with that classification and routed to revalidation. Never-lost records are admitted whatever the state of their task. A human decision on a fenced admission is admissible only once that admission is **settled** (§22.3). Each obligation whose discharge the request claims is undischarged at the current head (a duplicate discharge is rejected and recorded), and its discharge predicate (§10.4) holds after the request's own records, including affected evidence rerun on the merged tree. For a claimed task obligation with a work contract, the derived conformance of the exact candidate has no `VIOLATION`, `INCOMPLETE` or `DISCREPANCY` (§14.6), and an integrating request claims it only together with its current review judgments (§11.5).
8. **no collateral regression [refinement R15]** — for every other obligation whose required evidence the merged tree affects (its realizations' execution bases or readings read a unit the request changes), the evidence terms it requires stay passing: no `ev` or `qual` that passes at the current head falls on the merged tree (a fall from `T` to `P` counts as failing), with the affected evidence rerun; a request that makes one fail is refused (`REGRESSION`). The only legal way to make another closure's evidence fail is an accepted change to a prerequisite authority, whose derived impact obligations are the intended consequence: a request that carries or references, in its frame, a current prospective acceptance (and every required gate decision) of the D1-D3 revision it integrates, exempt only for the obligations whose subjects depend on that authority. A judgment that the request's content makes non-current (an earlier transformation's review or task result, an acceptance of a changed subject) is not a regression: the obligation it supported is reopened in current state, an item obligation taking the one route §10.4 gives it (SD-36 to SD-40), and the changed subjects reach their consumers through their own obligations. This step concerns the request's content and structural changes: an admitted assessment, adverse judgment, report or challenge that qualifies another closure is evidence, never collateral regression.
9. **commit and admit** — Admission reads the live integration head `obs`. The request is appended only if `obs` is the head entry's expected head `E` or an equivalent publication of it (§22.2); otherwise Admission first appends an absorption of `obs` and revalidates the request at the new head. One entry carrying `obs` and all records is appended by single-ref compare-and-swap (§21.3); it also reconciles the previous admission's publication if that was pending. The entry is provisional until a witness quorum holds it (§22.4); only then is the request reported admitted, the integration ref published, work dispatched from the new state and the next entry appended.

#### 8.4 Reason codes [D3 decision]

Rejections and refusals carry enumerated codes, one per failed check, grouped by step: `SCHEMA_*`, `SECRET_DETECTED`, `REF_*`, `AUTH_ACTOR`, `AUTH_TARGET_PART`, `AUTH_TARGET_REVOKED`, `AUTH_ILL_FORMED`, `AUTH_ENVELOPE`, `AUTH_ROLE_KIND`, `AUTH_WRITE_SCOPE`, `AUTH_PROTECTED`, `AUTH_SUPERSEDES`, `AUTH_VERSION`, `READING_CONTRADICTION`, `STRUCT_*`, `FREEZE_SOURCE`, `FREEZE_DESTINATION`, `ENACTMENT_MISSING`, `RELATION_*`, `CYCLE_SUPPORT`, `CYCLE_WARRANT`, `STALE_BASIS`, `STALE_RETAINED`, `OBLIGATION_*`, `CONFORMANCE_*`, `REGRESSION`, `HEAD_MOVED`, `NOT_SETTLED`. **[delegated]** The exact member list of each `*` family, which is closed per schema version.

#### 8.5 Dependency rules restated for authors

A challenge-tier record targets only strictly earlier records; a challenge never targets a challenge except as a counter-challenge of a restrictive adjudication. A judgment about part `u` never holds `validity` on `subj(u)`. An equivalence judgment relates two revisions of one unit and never relies on a consumer of that unit.

#### 8.6 Absorption

Absorption of a foreign change already on the integration ref records what happened, so it cannot be stale or illegal. It skips steps 1-8 and is appended and admitted like any entry. It is a pure integration observation: its only content is `obs` and, for a fencing absorption, the fence effect `obs -> F` (§22.3). An entry whose `obs` differs from its expected head must be an absorption carrying no submitted records; Admission rejects any other shape, and derivation treats a violating entry as corrupt (§5.7). Absorption sets the observed tree and changes nothing else. Consequences, all in S0/S2: foreign structural declarations become quarantined deltas; foreign semantic content changes revisions, so acceptances and reliance on it stop being current; foreign relation violations make the involved subjects ill-formed. The S3 obligations that follow — intake, drift, broken closures, integrity findings — only schedule and explain (§18).

#### 8.7 Self-reference and agent PASS

Records reference the candidate commit; they are never stored inside it. Task and result envelopes on run branches are transport, ingested into the ledger, never merged (G2, G3). An admitted `PASS` judgment is a recorded fact about what the actor concluded; closure is a derived discharge (§10.4).

### 9. Concurrency, serialization and joint invariants

#### 9.1 What is decided where

| When | What can be established | Mechanism |
|---|---|---|
| before issue (prediction) | probable footprint: intended affected units, impact closure, serialization surfaces | Dispatcher avoids overlapping work; advisory only (K4) |
| before issue (authorization) | the work contract's write scope | enforced in conformance and at Admission (§13, §8.3 step 3) |
| at admission (proof) | everything relied on is current; actual write set; structural validity of the merged tree; dependency well-formedness | basis currency, diff mapped to units, structural checks |
| after merge (evidence) | behavior of the combined tree | evidence currency recomputed; affected realizations rerun |
| never mechanically | joint validity of independently valid changes where no relation, invariant or evidence covers the interaction | judgment: declared joint invariants, review of integrated results, stated residual risk |

**Optimistic admission.** Concurrent tasks work from recorded bases in isolated workspaces (K2: one mutating execution per worktree, enforced by the Dispatcher's lease keyed by physical worktree identity). Two requests conflict when one modifies a unit or record in the other's basis; this catches write-skew among recorded reliances across disjoint files. A request whose basis was overtaken is revalidated — rebased, re-derived, affected judgments re-requested — never rejected outright and never silently admitted. A losing compare-and-swap between two Admission hosts is the same case. A very late result whose basis is still current is admissible regardless of age; a fresh result with a stale basis is not. Lease expiry affects scheduling, never correctness.

#### 9.2 Serialization surfaces and joint invariants [D3 decision]

- **Serialization surfaces.** Project policy may declare units (by identity) as serialization surfaces: shared schemas and public contracts, build configuration, D1-D3 subjects in one dependency neighborhood, generated outputs. The Dispatcher then issues at most one mutating task whose write scope intersects such a unit at a time. Every change plan is a serialization surface for coordination: at most one coordination task per plan at a time (§12.5). Serialization is scheduling, never correctness.
- **Joint invariants.** A semantic declaration `joint_invariant` (§1.7) names an invariant identity and the units whose joint behavior it constrains. Any admitted change touching the scope of any named unit derives a joint-invariant obligation: a `REVIEW` of the integrated result against the invariant, by a reviewer in the R2 class, plus any evidence specifications that `EVIDENCES` the invariant's unit. Each change derives its own; an earlier change's obligation ends when a later admitted change in the same scope derives one, unless it is `REFUSED` (§10.2, SD-37). Policy may mark further surfaces high-consequence, which derives the same integrated-result review for every change to them, ending when a later change to the same marked surface derives its own.

#### 9.3 Generated units

A `GENERATED` unit declares `GENERATED_FROM` its generator and inputs. It is never hand-merged and never hand-edited: a boundary check (§14.3) flags any diff to it not produced by regeneration, and a conflict is resolved by regenerating. Its acceptance is that of its generator's subject plus a regeneration-parity check execution.

#### 9.4 Residual risk disclosure

Semantic dependencies an agent uses without machinery observing them cannot be captured. Mitigation is layered: the mechanical minimum includes the governing closure; integration reruns affected evidence; joint invariants re-derive their obligations; integrated-result reviews run on high-consequence surfaces. Every brief whose basis includes unobservable reads (manual and Git-envelope routes) states "reads not observed"; every review record and gate brief over integrated work states the residual: "joint validity is reviewed only where a relation, joint invariant or evidence covers the interaction".

## Part IV. Work, workflow and verification

### 10. Obligations, readiness and discharge

#### 10.1 Two sources of work

- **Derived obligations** follow from rules and state; they are never authored and appear and disappear as derivation changes (S3).
- **Authored intents** carry creative direction (implement this, investigate that, migrate this region). They live in change-plan **items** (§11).

#### 10.2 Obligation kinds [D3 decision]

An obligation's identity is `sha256("ssds.obligation.v1" ‖ rule id ‖ JCS(target) ‖ JCS(parameters))`, deterministic from its derivation. The system ruleset's obligation kinds, their triggers and holders:

| Kind | Trigger (S3) | Holder role (§12.3) |
|---|---|---|
| `IMPLEMENT`, `REPAIR`, `MIGRATE` | an accepted, issuable item of that kind with a contract | implementer |
| `AUTHOR` | an accepted, issuable `AUTHOR` item (authoring or materially revising D1, D2 or D3 authority) with a contract | implementer, under the authoring write-scope rule (§13.2) |
| `DOCUMENT` | an accepted, issuable `DOCUMENT` item with a contract | implementer, under the documentation write-scope rule (§13.2) |
| `INVESTIGATE` | an accepted investigation item; an intake classification need | investigator |
| `CONTRACT` | an accepted item revision lacking a lint-clean contract | principal |
| `COORDINATE(plan)` | a decision owed on the plan: a routed report, an adverse answer to an acceptance or plan-acceptance obligation of its items (§10.3), detected recurrence, a `COORDINATE(plan)` route §10.4 gives an item obligation of its items (a kept fence, a spent budget, an out-of-scope NO-PASS finding or a `DISCREPANCY`, an adverse item-level review naming no part), each condition one obligation, and a `REFUSED` `JOINT_INVARIANT`, `SPEC_REVIEW` or high-consequence review obligation derived from an enactment of its items until a coordination decision answers it (§10.4) | principal of the plan |
| `PLAN_ACCEPT(items)` | an item revision not covered by a current plan acceptance | reviewer |
| `REVIEW(X)` | a task result whose conformance is `CLEAN`, while `X` is unintegrated (after integration the item obligation's discharge reads the review, §10.4; SD-37) | reviewer |
| `REVIEW(s, r)` (revising review) | in a frame `G`, `ACCEPT(s)` or a `GATE(g)` on `(s, scope_id(s), r)` derived for a `NATIVE` subject `s` of kind D1 or D2 at revision `r` (in its current or a prospective tenure), with no revision-assessment record for `(s, r)` that counts (below; SD-16, SD-19, SD-22), including in a cutover's frame for the subject's prospective `NATIVE` tenure (§19.5). Its brief carries the revising and tension-search duties and the machinery-computed predecessor; its result requires `revision_assessments` | reviewer |
| `ACCEPT(s)` | a subject without a valid acceptance whose work is ready for acceptance; for a `NATIVE` D1/D2 subject at revision `r`, ready only while a revision-assessment record for `(s, r)` counts (below), and current only within its revision run | reviewer (R2) or human (R3 by domain) |
| `REVALIDATE(x)` | a judgment acting in the state (§5.2), no longer current there, that a current obligation depends on: one whose discharge predicate needs `x`'s currency because no other judgment satisfies the term `x` is in (an `∃` term another current judgment satisfies does not depend on `x`; a minimum such as `gterm` depends on each member); it ends when `x` is current again, superseded, or no longer depended on; for an item obligation's review or task result, only where §10.4's routes give it; never for a judgment that is non-current because a standing adverse judgment vetoes it (§5.10 (f)), whose disagreement goes to `ADJUDICATE_DISAGREEMENT` | the role of `x`'s kind; for a `GATE_DECISION`, its author or the owner, whichever answers first (only they may supersede it, §5.10 (d)) |
| `REALIZE(spec, claim)` | an evidence obligation without a current admissible realization in the frame | Dispatcher (R0 execution) |
| `ASSESS(realization)` | an admitted realization without an assessment for its obligation | reviewer (assessor) |
| `RERUN(a⁻, G)`, `READING(a⁻, G)` | §6.9 | Dispatcher; reviewer at the §6.8 class |
| `ADJUDICATE(c)` | an open challenge | the actor policy names (R2/R3) |
| `ADJUDICATE_DISAGREEMENT(x)` | an adverse assessment `x` with no standing disposition (§6.10); or a standing adverse judgment `x` that vetoes a passing judgment of its kind acting in the state (§5.10 (f)) | the owner of the claim or target (§5.10 (a); R2/R3) |
| `GATE(g)` | a required human gate without a current `ACCEPT`; for a gate on a `NATIVE` D1/D2 subject `s` at revision `r`, ready only while a revision-assessment record for `(s, r)` counts (below); a gate decision is current only within the revision run | human |
| `HUMAN_ATTENTION(r)` | a report or floor event routed to the human (§15) | human |
| `INTAKE(δ)` | each quarantined delta; each uncovered or foreign observed change | investigator, then a disposition reviewer |
| `SPEC_REVIEW(spec, r)` | a change of an evidence specification to revision `r` (each change its own obligation), while the specification is at `r`, or while `REFUSED` (SD-37) | the specification's owner (reviewer of its domain) |
| `JOINT_INVARIANT(i, k)` | an admitted change touching a joint invariant's scope (§9.2), except an `OVERTAKEN` or fenced one, whose re-application derives its own, until a later admitted change in the same scope derives `JOINT_INVARIANT(i, k')`, or while `REFUSED` (SD-37); for a late publication the human accepts (`late(n)`, §22.3), the absorption that reaches `C_n` derives it | reviewer |
| `REQUALIFY(x)` | a permissive record or relaxer in effect at the retained head and withheld by a loss boundary | the role of `x`'s kind |
| `INTEGRITY(f)` | an integrity finding (§5.6-§5.7) | human, plus the standing principal |
| `REISSUE(envelope)` | a refused never-lost record under an unlisted retired envelope (§8.3) | Dispatcher (R0) |
| `RECONSULT(external)` | a newer external revision observed (advisory, never blocking) | Dispatcher |

Obligations belonging to no plan are held by the role their kind names; a decision owed on them goes to the principal of the plan policy designates as **standing**, or to the human where policy names none (§12.5).

**Revision assessments and the revision run [D3 decision; SD-16, SD-19, SD-22, SD-25].** These rules apply to every `NATIVE` subject of kind D1 or D2 (its declared kind; an `EVIDENCE_SPEC` or `GENERATED` unit in a D1/D2 domain is not one).

- A **revision-assessment record** for `(s, r)` is an admitted `TASK_RESULT` whose `revision_assessments` slot is complete (`slots_filled`, §14.3) and holds an entry naming exactly subject `s` and revision `r` (one entry per subject the task revised): the result of an `AUTHOR` task whose candidate yields `r`, or of a task answering `REVIEW(s, r)`, whether an agent or an authenticated human executed it. How `r` was produced plays no part: an `AUTHOR` item, a human change, an absorption, an adoption, a clean merge of several, a promotion, a nested change, a re-identification and a revert are treated alike, so an `AUTHOR` item's assessments cover only the revision its own candidate yields.
- The **revision run** of `s` in state `G` (§5.2) is identified by `rid_G(s) = (s, ι)`, where `ι` identifies the event at which `cur(s)` took its current value in `G` (an integration, an absorption, an adopting disposition, or the start of `s`'s tenure, a cutover included; a byte-preserving refinement changes no revision, R6): for an integration, its enactment (the producing task, §5.2), a cutover included, since a cutover is carried by an integration (§19.5); for every other event (an absorption, a machinery `ABSORB` request, which has no producing task, a ruleset adoption that re-identifies a revision, §27.3), the admitting entry's identity. In a frame `D_n[X]` where `X` changes `cur(s)` or starts `s`'s tenure, `ι` is `X`'s enactment, the event its integration would be; where `X` changes neither, `rid_{D_n[X]}(s) = rid_{D_n}(s)`. Admission refuses a second integration of one enactment (§8.3 step 7), and entry identities are unique, so no two events share `ι` (SD-26). `rid` is therefore known before the event, unchanged by intervening unrelated admissions, and equal in the frame and after the integration, with no mapping between them (SD-25); a later change of `cur(s)`, including a return to earlier bytes, is a new event and a new run. An S0 fact.
- A passing `ACCEPTANCE`, a `GATE_DECISION ACCEPT` and each `revision_assessments` entry on `s` **name** a run: `rid` of `s` in the frame the record declares, at its admission; machinery fills the field and Admission checks it (step 2). Such a record is **in the run** of `s` in `G` iff it acts in `G` (§5.2) and names `rid_G(s)`. A record of an enactment that never integrates is in no run of an admitted state, and a frame record of `X` on a subject `X` leaves unchanged is in the admitted run once `X` integrates, exactly as it was in the frame.
- **Currency [SD-22].** A passing `ACCEPTANCE` (prospective or not) or `GATE_DECISION ACCEPT` on `(s, σ, cur(s))` is current only if it is in the run: this is a target condition (`tgt`, §5.2), so `base`, `valid`, `ACC`, discharge (§10.4), the `ACCEPT` and `GATE` triggers and every other consumer read it. A revert to an earlier accepted revision, or any other change of `cur(s)`, therefore starts a new run in which no earlier acceptance or gate decision is current; `ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` are derived for the new run. Re-accepting an unchanged revision within its run reuses its record.
- **Admission and readiness.** A passing `ACCEPTANCE` or `GATE_DECISION ACCEPT` on `(s, σ, r)` is admissible only while a revision-assessment record for `(s, r)` **counts**: it is in the run in the state where the judgment is evaluated (in a frame `D_n[X]`, the run `rid_{D_n[X]}(s)`) and it stands there, `base ≠ F` (it acts, is not superseded, `status1 ∉ {REVOKED, BLOCKED}`, `cont` and `tgt` hold, it is not vetoed or `nonind`; for a `TASK_RESULT` the last three hold trivially; §8.3 step 7). The accepting judgment carries a `standing` basis entry on that record (§4.1, §4.3), so the record's later revocation, block, risk override (`P`) or loss withholding reaches the acceptance through the record's `base`, which is what "counts" reads (the run part of "counts" is the acceptance's own `tgt`); the record's own basis (what the reviser read, its governing context, its item revision) does not, since the acceptance carries its own `content` and `validity` entries (stakeholder record item 31). An in-run re-acceptance after a governing change therefore reuses the record. `ACCEPT` and `GATE` readiness read the same condition.
- **Predecessor (display) [SD-22].** Machinery computes the **predecessor** of `(s, r)` and shows it in the revising brief, the record's slot and the gate core: the last revision of `s` whose acceptance was current in the admitted state before the run started, in this or an earlier tenure, together with declared lineage (`renamed_from`, the source subjects of a promotion, split or merge) and the earlier subjects that owned the bytes `s` covers at its tenure's start. The reviser may extend it in the slot with further predecessors and a reason. It is an input to the revising and tension-search duties and to the gate's judgment, never an equality condition on counting or currency. A tension recorded after the record does not make it stop counting; the gate core's section 1 shows every tension the relying search finds (§16.6; SD-20).
- **Obligations.** `ACCEPT(s)`, `GATE(g)` and `REVIEW(s, r)` carry `rid_G(s)` among their parameters, so a new run derives new obligations, and a frame derives the obligations its integration produces, with the same identities. `ACCEPT` and `GATE` are answered only by a judgment in the run, and `REVIEW(s, r)` only by a counting record (§10.3).

**Evidence obligations under change [D3 decision].** An evidence obligation is `(claim unit lineage, specification unit lineage)`. Its **lineage** follows retargets (an `EVIDENCES` relation moved to a successor claim unit), splits (one obligation becoming several, each in the lineage) and renames (`renamed_from`). Retirement (the specification or relation removed), split or retargeting never disposes of a failing assessment: `qual` keeps reading it through the lineage, and the owner disposes explicitly, typically by `IMMATERIALITY` (§6.7).

#### 10.3 Readiness

**No stranded obligation [D3 decision; stakeholder record item 31].** In every state, a judgment obligation is dispatched only while an answer of its kind with its mechanical minimum basis (§4.3) can hold at Admission step 6; where an entry of that minimum cannot hold, the obligation is shown as waiting on that entry and the route that restores it is derived instead (§4.1: a wider closure, `REALIZE`/`RERUN`/`READING`, `REVALIDATE` (for an item obligation's review or task result, only of a pending candidate, §10.4), `REVIEW(s, r)`). A ready obligation whose every answer Admission must refuse is a defect, and so is a non-current judgment that a current obligation depends on with neither a ready nor a waiting route; §31.6 (Z) tests for both. One class waits by design: an `ADJUDICATE_DISAGREEMENT` for which neither the owner's supersession nor relief is admissible because the bases they need no longer hold (a plan rejection and its vetoed acceptance after the item moved; an acceptance `FAIL`/`PASS` pair after the subject moved to a new revision; a transformation review whose frame no longer exists) waits on an upheld challenge, which the owner or any qualified actor may raise, or on the owner's adverse record superseding the vetoed passing judgment, which is never-lost and exempt from step 6; the vetoed record then blocks no work.

An obligation is **ready** when every prerequisite it names is valid (or provisional, where an in-force risk override's scope or policy permits provisional continuation; the result is then provisional) and its plan item, if any, is covered by a current plan acceptance. Readiness is derived from the ledger and content alone (S3); it replaces any freeze frontier. Whether a ready obligation is dispatched now is the Dispatcher's operational decision (resources, routes, serialization surfaces held) and never feeds back into derived state.

**Iterations and attempts [D3 decision].** An **iteration** of obligation `o` is identified by `(o, k)`, where `k` counts the admitted `TASK_RESULT` records bound to `o`; every task ends in exactly one (§8.3 step 7), reviewer and principal tasks included. A NO-PASS of an implementer's candidate leaves that implementer obligation undischarged and its next task is iteration `k+1`, on a new candidate.

**Answered judgment obligations [D3 decision; refinement R9].** An obligation whose answer is a judgment (`REVIEW` other than the revising review, which only a counting revision-assessment record answers (§10.2), `ACCEPT`, `PLAN_ACCEPT`, `ASSESS`, `READING`, `SPEC_REVIEW`, `JOINT_INVARIANT`, `ADJUDICATE`, `ADJUDICATE_DISAGREEMENT`, `GATE`, and the disposition step of `INTAKE`) is **answered** in a state by the first judgment acting there (§5.2) of its kind on its target that is bound to it or recorded on its target by an authenticated human, so a judgment in a pending or abandoned candidate's frame answers nothing in the admitted state; a passing judgment with `nonind` does not answer an obligation whose discharge requires independence, so that obligation stays dispatchable (§5.10 (f)). For a `NATIVE` D1/D2 subject, an `ACCEPT` or `GATE` obligation is answered only by a judgment in its revision run (§10.2). A judgment obligation's target is the exact thing judged (`ACCEPT` and `GATE`: the subject triple `(s, scope_id(s), cur(s))`; `REVIEW`: the transformation; `PLAN_ACCEPT`: the item revisions), so a new revision or candidate derives a new obligation. An answered obligation is never ready again, so it is never dispatched again. A passing answer discharges it per §10.4. An adverse answer (§5.10) closes it undischarged: the next step is a new candidate or revision (a new target, hence a new obligation), the adverse judgment's own author's reassessment, or the owner's adjudication. A passing answer that later stops being current derives `REVALIDATE`, a separate obligation. A judgment obligation stays unanswered, and may be dispatched again within its budget, only when its task ended without an admitted judgment (a `BLOCKED` result, or every judgment it submitted refused at admission, an adjudication included). A **task** is identified by a 128-bit random identity the Dispatcher issues in its envelope. An **attempt** is one execution of one task, `(task, j)`, recorded only in the operator journal; a failed attempt never touches derived workflow state and spends no iteration budget.

#### 10.4 Discharge

Discharge is an S3 classification with four values: `DISCHARGED`, `DISCHARGED_PROVISIONAL`, `OPEN`, and `REFUSED` for an answered judgment obligation whose target carries a standing, unrelieved adverse judgment of its kind in its reach (§5.10 (f)), whichever answered first.

```text
discharged(o) ⇔ ∃ current judgment j of kind(o) on subject(o) by an actor qualified for kind(o),
                  with outcome in passing(o), satisfying any independence requirement (§8.3)
              ∧ status1 of subject(o)'s current revision ∉ {BLOCKED, REVOKED}
              ∧ ev(subject(o), e) for every evidence obligation e of o              -- §5.5, the same term valid reads
              ∧ qual(subject(o))                                                    -- §5.5
              ∧ gterm(g) for every human gate g of o (§5.5: the minimum over every eligible unsuperseded passing decision)
value is DISCHARGED_PROVISIONAL when any input above is P; that value is permitted only inside the declared
scope of an in-force risk override, or where policy permits provisional continuation for o's kind;
otherwise the obligation stays OPEN.
```

A passing judgment vetoed by a standing adverse judgment of its kind is not current (§5.10), so ∃ a passing judgment never discharges against a standing objection, in either order of admission.

Discharge is not latched (SD-36): an obligation discharged at one head is `OPEN` at a later one whose state no longer satisfies the predicate. For an item obligation, `subject(o)` in the predicate above is the union of the subjects every integrated enactment of `o` changed, so a re-dispatch never narrows what its terms read (SD-37). Admission step 8 refuses only a request that makes another obligation's passing required evidence fail (refinement R15); a later admitted request that changes content an obligation's judgments read, and an absorbed foreign change, can reopen it. **Routes of an item obligation [D3 decision; SD-37 to SD-40].** This paragraph is the one owner of an item obligation's route; every other section points here. An item obligation's identity is its item and the prose and fixed fields of its accepted revision (§13.4): an R1 tightening keeps it, and an R2 amendment derives a new obligation, so the old one is no longer derived and a candidate bound to it is refused at integration (§8.3 step 7). For an item obligation `o` (implementer or investigator), `out(o)` is the set of units its integrated enactments changed, with their revisions just after `o`'s latest integration; `out(o)` has **moved** while some of its units' current revision differs from that revision (a state, so a revert restores it). An obligation is **integrated** once some enactment of it has integrated; for a findings-only investigation, the admission of its reviewed result counts as that integration, with `out(o)` empty. After integration `o` relies only on its latest integrated enactment's review, the review of a re-dispatched enactment carrying `content` on every retained unit, which include `out(o)` (§4.3, §5.10 (a)), and no `REVALIDATE` is derived for an integrated enactment's review or task result (SD-40). A **pending candidate** of `o` is the candidate of a task result admitted for it and neither integrated nor refused.

Before integration, and for a pending candidate after it, `o` has the ordinary routes: it is dispatched while ready; a rebase over a change to one of the candidate's own changed units, or an integration refused for stale retained units (§8.3 step 7), is a new iteration (§11.5, K3); a clean rebase that makes the candidate's task result or review non-current derives its `REVALIDATE` (the task result's first, §4.1); a `PARTIAL`, `INFEASIBLE` or `INCOMPLETE` result or a NO-PASS whose findings lie within the item's write scope and obligations is the next iteration within budget, otherwise `COORDINATE(plan)`; a `BLOCKED` result is a blocker report (§15.3); a NO-PASS finding outside the item or a `DISCREPANCY` is `COORDINATE(plan)` (§13.7). After integration, the first of these that applies is `o`'s only route:

1. a fence of its latest integration awaiting the human's decision: that decision (§22.3); a fence the human kept, until a coordination decision answers it: `COORDINATE(plan)`, answered by `AMEND` (amend or withdraw the item) or by `DECLINE`, after which the routes below follow, so a re-application is drift;
2. the predicate holds: none, `o` is discharged;
3. a pending candidate of `o`: that candidate's ordinary routes above, so it is never discarded by a re-dispatch;
4. a standing adverse review of the latest integrated enactment (its author's or the owner's adverse review, or a peer's or human's whose veto the owner upheld, §5.10) whose findings lie outside the item's write scope or obligations, or, for a partitioned item, an adverse item-level review whose findings name no part: `COORDINATE(plan)`;
5. the budget is spent: `COORDINATE(plan)` (§13.7);
6. otherwise: re-dispatch, a new task and enactment (§8.6): drift when `out(o)` has moved, the next iteration after an adverse review, and a fresh enactment after a change only to what its implementer or reviewer read, a governing change or an R1 tightening.

An adverse item-level review of a partitioned item is a standing adverse review of each part whose outputs its findings name, so each such part's predicate fails and the list above is that part's route. A disagreement's own obligations (`ADJUDICATE_DISAGREEMENT` for a peer's veto of an integrated review) are not item routes: they stay derived on that review, answerable as §10.3 states, while the item takes its route above. A drift task's brief names the admitted change that moved its outputs and the item or absorption that made it, and states that later accepted changes are preserved (a conflict with one is an amendment request to the principal, §15.5); a drift candidate that changes nothing, because the current content already meets the contract, is reviewed and integrated as an empty transformation (`C_n = B_n`) claiming the obligation. Its re-dispatch is a new task, so a new enactment and, for a `NATIVE` D1/D2 subject it changes, a new revision run (§5.2, §10.2). A judgment obligation keyed on a past event (`REVIEW(X)` and conformance, `JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`, a partitioned item's item-level review) is derived only while what it judged can still be current (§10.2, §13.7), so none waits on a revalidation that no admissible answer can satisfy; one whose answer is a standing adverse judgment (`REFUSED`) stays derived, even when that answer is admitted after its successor was derived (a never-lost record from a task in flight re-derives it as `REFUSED`), so a finding is never retired by a later obligation whose judge did not see it. A `REFUSED` obligation of a kind with no mechanical iteration (`JOINT_INVARIANT(i, k)`, `SPEC_REVIEW(spec, r)`, a high-consequence review) derives a decision, `COORDINATE(plan)` for the plan of the item whose enactment derived it or §12.5's route outside a plan, until a coordination decision answers it (§15.5); a `REFUSED` `REVIEW(X)`, conformance or item-level review is handled by the item's own route above.

Impact on other subjects is not a discharge condition: those are separate obligations, and Admission step 8 forbids collateral regression. A missing required check is an undischarged obligation; no rule turns it into a pass.

#### 10.5 Provisional propagation and risk-override scope [D3 decision]

A `RISK_OVERRIDE` declares its continuation scope as a closed set: the subjects and items covered (identities), the obligation kinds allowed to discharge provisionally, and whether descendants created after the override inherit it (default no). It never covers `GATE`, `HUMAN_ATTENTION`, `ADJUDICATE` or `INTEGRITY` obligations. Inside the scope, `P` inputs discharge as `DISCHARGED_PROVISIONAL`; outside it they stay `OPEN`. Every view, brief and gate core labels provisional values with the override and the challenge it overrides; descendants whose support passes through a `P` value are `P` (min-propagation) and can never emit unqualified closure.

### 11. Change plans, plan acceptance and integration flow

#### 11.1 Plan structure [D3 decision]

A change plan is a `PLAN`-kind subject: a Markdown document whose manifest declaration sections it into parts. The **objective** part is the section headed `Objective`. Each **item** is a section whose heading path the manifest declares as a part, containing exactly one fenced code block with info string `ssds-item`, a TOML document:

```toml
item     = "solver-timestep"                 # item id, unique in the plan
kind     = "IMPLEMENT"                       # IMPLEMENT | REPAIR | MIGRATE | INVESTIGATE | AUTHOR | DOCUMENT
# authority = "D2"                           # AUTHOR items only: the one authority domain authored (§13.2)
# specialist = "MAINTENANCE_AUDIT"           # INVESTIGATE items only: MAINTENANCE_AUDIT | REPOSITORY_HYGIENE (§16.3)
objective = { ref = "#objective-of-item" }   # the prose objective for judgment is the item's own text
governing = ["numerics.solver@rev:…"]        # governing units at revisions
acceptance_criteria = [ { id = "ac1", evidence = "tests.solver-convergence" } ]
affected  = ["src/solver/"]                  # intended affected units or patterns
gates     = ["d2-owner-review"]              # required gates
depends_on = ["other-item"]                  # item dependencies (acyclic, layer-respecting)
[contract]                                   # the work contract (§13.1)
```

Plan lifecycle fields in document prose (`status:`, `active/`, `archive/` placement) are non-authoritative or generated, and a manual edit to them enacts nothing (§19.8).

#### 11.2 Plan acceptance

A `PLAN_ACCEPTANCE` judgment (R2, by an execution other than the contract's author) names the objective section and the item revisions it accepts, the items with consumption class `PLAN_CONTROL`. An item is **issuable** only while a current plan acceptance covers its current revision. Item-level revisions give locality: an amendment is an ordinary change to the plan unit; tasks whose basis names a changed item become non-current; tasks on unchanged items continue. Running tasks remain bound to their basis; no revision pretends an old task saw new requirements.

#### 11.3 Plan invariants

Rechecked mechanically on every plan-unit change, as part of contract lint (§13.2): referenced units exist in `Σ`; item dependencies are acyclic and respect layer order; gates policy requires for the item kinds and domains are present; acceptance criteria name resolvable evidence specifications or `REVIEW`; every changed contract passes lint. A plan that fails is admitted as content (the principal's change is recorded) but its changed items are not issuable.

#### 11.4 Amendment policy [D3 decision]

An amendment's class is computed by lint from the diff between the accepted item revision and the current one (§13.4): control tightening keeps the existing plan acceptance current (R1); every other amendment needs independent plan acceptance (R2). The plan's policy section declares, per plan, whether an R2 amendment may be accepted by **scoped review** of the changed items plus their derived impact set, or needs whole-plan review. Changes to the plan objective, acceptance criteria, item topology (`depends_on`, added or removed items) or gates always need whole-plan review. A scoped reviewer always receives the whole-plan objective and may escalate to whole-plan review. There is no global planning or working phase and no global stop: an unaccepted amendment only makes its own items non-issuable.

#### 11.5 Results, review and integration

Implementation work enters canonical state through two ordinary admissions.

1. **Result.** `submit` by an implementer or investigator produces a records-only request bound to its task and claiming no discharge: a `TASK_RESULT` (outcome, typed slots, claim references, reports) naming the candidate commit and the contract revision. It fixes `X = (B, C, A)`. Machinery attaches the factual part: diff mapped to units, touched relations, reads (A6). The candidate is not merged. The Dispatcher then runs the contract's required executions on the exact candidate through a designated runner and submits them as observations. Conformance is derived (§14.6).
2. **Review.** Once conformance is `CLEAN`, `REVIEW(X)` becomes ready (R0). Result, executions, review and conformance judgments declare frame `id(X)`. A reviewer task submits its judgments together with its `TASK_RESULT` (carrying the required slots) as one records-only request claiming discharge of the review obligation only; the first admitted judgment answers it (§10.3). When the candidate promotes, restores or adopts a subject, a qualified reviewer also records the prospective acceptance in the frame (§7.6).
3. **Integration.** Once the claimed obligation's discharge predicate would hold on the candidate — clean conformance, current review judgments, required gates — the Dispatcher submits an **integration request**: the candidate plus references to those admitted records, bound to the producing task and claiming its obligation, carrying no new judgment. Admission validates it through steps 1-9. If the head moved, the candidate is rebased; a rebase that does not apply cleanly routes to a new implementer iteration (K3); a clean rebase has its conformance re-derived, and review is re-requested only where the review's basis no longer holds, by the routes §10.4 gives a pending candidate.

Every other request follows the same split: a mid-task report is bound to its task and claims nothing (a blocking report suspends that task, §15); a coordination request is bound to its `COORDINATE` obligation and claims discharge of the decision obligations it resolves. A rejected candidate stays recorded with its conformance view and reports. Records-only work (reviews, investigations whose output is findings) has no integration step.

### 12. Workflow roles and decision classes

#### 12.1 Role and domain

A **workflow role** is an authority envelope: what an execution may write, which record kinds and outcomes it may submit, which decisions it may make. It is distinct from SSDP's D1-D4 domain roles, which are content: the epistemic procedure a brief carries for its subject's domain (§16.3). A brief composes the two. No agent role is a principal in the authentication sense of §25.1: its records are proposals attributed to an execution identity.

#### 12.2 Authenticated task binding and lineage

The Dispatcher issues every task as an **envelope**, signed with a Dispatcher **issue key** registered as a trust root (§25.2):

```text
envelope = { task_id, obligation_id, role, contract_revision (item unit, rev) | system contract id,
             governs (§16.9), route, lineage_class, input_sessions, issued_at_position, issue_key_id,
             predecessors (revision-assessing tasks only: a map from each subject the task may revise
             to its machinery-computed predecessor, for display, §10.2),
             retained (implementer and investigator tasks: the retained units U_X of the
             transformation it produces, machinery-computed at issue, §5.10 (a)) }
binding  = { envelope, signature, lineage_class }        -- carried by every submitted record
```

Admission verifies the signature and checks role, write scope and record kinds against the envelope (§8.3 step 3); admitted records carry the binding, so derivation and replay read it from the ledger alone. Binding and discharge are separate: every request is bound to one task; only some claim discharge.

**Lineage classes and context-lineage provenance [D3 decision].** On a route where the Dispatcher's harness adapter launches the execution, it starts a new harness session for the task, hands that session alone a per-task submission credential, and signs a **launch attestation** naming the session identity and the sessions of the task's inputs (the authoring task of a candidate under review; the author of a contract under plan acceptance). Requests authenticated by that credential carry lineage class `ATTESTED_FRESH`. On manual and Git-envelope routes the Dispatcher cannot observe the session: a judgment from such a route is `UNKNOWN` unless an authenticated human attests that it ran in a fresh context that did not receive the author's conclusions (`HUMAN_ATTESTED_FRESH`, a `LINEAGE_ATTESTATION`). Anyone holding an envelope may submit within its role and contract; independence is credited only to positively attested lineage. Two lineages are **disjoint** iff no session in one's attestation closure appears in the other's. Execution provenance records lineage class, route, harness, model family and model, and toolchain.

#### 12.3 System role templates [D3 decision]

| Role | Obligation kinds held | Operations | Record kinds and outcomes it may submit | Write-scope rule | Decision class | May not |
|---|---|---|---|---|---|---|
| **Principal** | `COORDINATE`, `CONTRACT` | `open`, `ask`, `read`, `report`, `submit` | `TASK_RESULT` with outcomes `COMPLETE`, `BLOCKED`; `COORDINATION_DECISION` (outcomes per §15.5), `MATERIALITY_RECLASSIFICATION`, reports, challenges; plan-unit candidate | its plan's units only | R1 | write product, authority or evidence units; submit review, conformance, acceptance, plan-acceptance or human judgments; any judgment keeping its own amendment covered; change verification rules |
| **Implementer** | `IMPLEMENT`, `REPAIR`, `MIGRATE`, `AUTHOR`, `DOCUMENT`, `REVALIDATE` of its own result | all six except `decide`; `ask(verify)` | `TASK_RESULT` with outcomes `COMPLETE`, `PARTIAL`, `BLOCKED`, `INFEASIBLE`; reports; challenges | its contract's `write_scope`, plus `evidence_specs` it names | — | edit plan units, contracts, evidence specifications its contract does not name, verification rules or protected surfaces; judge its own work |
| **Reviewer** | `REVIEW`, `ACCEPT` (R2), `PLAN_ACCEPT`, `ASSESS`, `READING`, `ADJUDICATE` (R2), `ADJUDICATE_DISAGREEMENT` (R2), `SPEC_REVIEW`, `JOINT_INVARIANT`, `INTAKE` dispositions, `REVALIDATE` of a judgment of those kinds | `open`, `ask`, `read`, `report`, `submit` | `TASK_RESULT` with outcomes `COMPLETE`, `BLOCKED`; `REVIEW`, `CONFORMANCE`, `ACCEPTANCE`, `PLAN_ACCEPTANCE`, `EVIDENCE_ASSESSMENT`, `EQUIVALENCE`, `COMPLETENESS`, `IMMATERIALITY`, `ADJUDICATION`, `INTAKE_DISPOSITION`, reports, challenges | none (records only) | R2 | write content; judge work or a contract its own execution or lineage authored; receive the author's narrative or conclusions |
| **Investigator** | `INVESTIGATE`, `INTAKE` classification | `open`, `ask`, `read`, `report`, `submit` | `TASK_RESULT` (findings outcomes `FOUND`, `NONE_FOUND`, `INCONCLUSIVE`), `INTAKE_CLASSIFICATION`, `RECONSTRUCTION_PROPOSAL`, reports, challenges, proposed relations | scratch workspaces and the native finding/evidence homes its contract names (`homes`) | — | write product or authority units; submit acceptance |
| **Human** | `GATE`, `HUMAN_ATTENTION`, every R3 decision | `decide`, plus all operations | every R3 kind; any content as ordinary change that enacts nothing until admitted or accepted | any, as ordinary change | R3 | — |

Every role may submit reports (§15) and challenges, because those are never-lost. Every execution the Dispatcher launches runs in a fresh context for one task.

**Separation constraints.** No execution holds principal and reviewer roles; no reviewer reviews a transformation, contract or record its own lineage authored; a plan acceptance is never by the contract's author lineage; an `ACCEPTANCE`, `REVIEW`, `CONFORMANCE` or disposition by a lineage not disjoint from the author's is non-independent (§8.3). The obligation kind determines the role (A4): no agent selects its role.

**Policy extension limits.** Project policy may add roles only by narrowing a system template (fewer obligation kinds, operations, record kinds, outcomes or write scope). It may not widen a template, combine principal and reviewer in one execution, give an agent role any R3 decision, or let any role edit roles, check templates, routing, floors or decision classes.

#### 12.4 Decision classes

The class of every decision is a function of its kind, target domain and policy; no agent selects it. An agent may move a decision up by escalating, never down.

| Class | Decided by | Decisions | Recorded as |
|---|---|---|---|
| **R0** | machinery | readiness; dispatch, suspension, resumption; staleness; evidence and check executions; iteration retry within budget; report routing; integration requests; recurrence detection; re-issue | derived state or operator journal; never a judgment |
| **R1** | principal | task partitions and ordering; responses to findings inside an item's scope; local resolutions in delegated space; control-tightening amendments; merging, upgrading, framing; downgrading non-floor materiality | coordination decision or plan-unit change; challengeable; never acceptance |
| **R2** | an independent agent or human reviewer (A9) | plan acceptance of new contracts and every non-tightening amendment; review, conformance and acceptance judgments policy assigns to agents; adjudications assigned to agents; dispositions of a disagreement (§6.8) | support- or challenge-tier judgment |
| **R3** | authenticated human | gates; D1/D2 acceptance where policy requires; Serious Challenge adjudication; risk overrides; product-scope acceptance; continuity attestations; human attention; dispositions of a D1/D2 disagreement, including discriminating readings of a failure that may belong to admitted content | authenticated human judgment |

#### 12.5 The principal is an obligation holder; standing plans

`COORDINATE(plan)` obligations are derived whenever a decision is owed on a plan. Each coordination task is a fresh execution whose decision brief (§16.7) is rendered from derived state; nothing a principal execution remembers is canonical, so any execution can replace it at any decision point and context compaction loses no workflow state. Each plan is a serialization surface for coordination: at most one coordination task per plan at a time, and the Dispatcher batches the plan's pending decisions into it.

**Standing-plan designation [D3 decision].** Project policy names one plan as **standing** (`standing_plan = "<plan subject id>"`). Decisions owed on obligations that belong to no plan (intake, integrity, requalification, re-issue) route to its principal; with no standing plan they route to the human. The standing plan is an ordinary plan with ordinary acceptance; it has no extra authority.

### 13. Work contracts

#### 13.1 Schema [D3 decision]

A **work contract** is the `[contract]` table of an item (§11.1): plan content authored by the plan's principal, revisioned with the item, accepted by the item's `PLAN_ACCEPTANCE`, and bound into every task's basis through the item revision. Obligations that belong to no item receive the **system contract** of their kind (§13.6), so every task has exactly one contract.

```toml
[contract]
scientific   = "APPLIES"                      # APPLIES | NOT_APPLIES: the 7.2.1 scientific-checks predicate
budget       = 3                              # iterations before mechanical retry yields to the principal
[contract.boundaries]
write_scope  = ["src/solver/", "tests/solver/"]   # unit ids or scope terms, resolved in Σ
frozen       = ["pkg.solver.step", "pkg.solver.Solver.run"]   # public symbols, by language analyzer
dependencies = { python = ["numpy>=1.26"] }   # permitted additions to declared dependency manifests
evidence_specs = []                           # evidence-specification units the item may change (default none)
homes        = []                             # investigator only: finding/evidence homes it may write
[[contract.obligations]]
id        = "o1"
statement = { ref = "#o1" }                   # prose in the item section, for judgment
verifier  = { check = "OBLIGATION.required_evidence", params = { spec = "tests.solver-convergence" } }
          # or { evidence = "<spec unit>", runner = "<runner class>" } or "REVIEW"
secondary = [ { check = "TEST_INTEGRITY.no_skips" } ]   # optional secondary HARD checks
[contract.expectations]
artifacts = ["src/solver/timestep.py"]
evidence  = ["tests.solver-convergence"]
slots     = ["findings", "choices", "retention", "claims"]   # required result slots (§13.5)
[contract.escalation]
triggers  = ["SCOPE_DEVIATION", "D1_D2_TOUCH"]
```

Unknown keys are a lint error (closed schema, C5).

#### 13.2 Lint

Lint is mechanical and runs at every admission of a plan-unit change, with the plan invariants (§11.3):

- fields typed under the schema; units and scope terms resolve in `Σ_n`;
- **ref locality [D3 decision]**: every `ref` in an item (objective, obligation statements and any other prose field) is resolved only inside that item's own part and the plan's `Objective` part, which every plan acceptance names `EXACT` (§4.3); an anchor or heading of the same name elsewhere is never consulted. A `ref` that does not resolve there to exactly one span is a lint error, so all prose an item relies on is either in its own revision or covered by its plan acceptance;
- the write scope lies within the item's `affected` units and contains no protected surface, no plan unit and no evidence-specification unit outside `evidence_specs`;
- **domain rule [D3 decision]**: an `IMPLEMENT`, `REPAIR`, `MIGRATE` or `DOCUMENT` write scope contains no `D1`, `D2` or `D3` unit, and its write set (§1.2) may contain none, so no change to a D1-D3 unit's owned content, semantic declarations, regions, membership or signature, by whatever route (its text, the manifest, the governed boundary, a new or moved part), can happen except through an `AUTHOR` item, whose duties, slots and minimum coverage are keyed on its kind (§13.3, §13.5, §16.3); an `AUTHOR` item declares one authority domain (`authority = "D1" | "D2" | "D3"`) and its write scope contains only units of that kind, `ssds.manifest`, `EVIDENCE_RECORD` homes and the evidence specifications its `evidence_specs` names. A structural change across domains (nesting a unit of one kind in a subject of another, carving a D1-D3 subject out of other content) has no agent item route, because its write set holds units of two kinds: it is a human's ordinary change or an adoption under an R2 intake disposition (§18.4); a change of a unit's kind or owning domain also needs release by an actor qualified for its current domain (§8.3 step 4), and every D1/D2 subject the change revises needs its revision-assessment record before acceptance (§10.2). Declaring a new unit of the item's own domain over uncovered content is an `AUTHOR` item's change like any other, with its duties and acceptance;
- every obligation names exactly one primary verifier; every `check` names a `HARD` template of `ρ_n` with valid parameters (a `HEURISTIC` template cannot be a primary or secondary verifier); every `evidence` names an existing specification and a designated runner class;
- the required slots include every slot the obligation kind, subject domain and `scientific` flag trigger (§13.5);
- policy-declared minimum verifier coverage holds (§13.3);
- a budget is present and within the system cap (§13.7).

Lint establishes form only. Whether the contract captures the item — the right obligations, a sufficient verifier for each, a boundary neither too narrow nor too loose, the right `scientific` flag — is judged in `PLAN_ACCEPTANCE` by an execution other than the contract's author. A strong verifier over a weak contract proves only what the contract asked.

#### 13.3 Minimum verifier coverage per item kind [D3 decision; policy may raise]

| Item kind | Minimum |
|---|---|
| `IMPLEMENT`, `REPAIR` changing `D4` units | at least one `EVIDENCE` obligation; at least one `REVIEW` obligation |
| any item whose write scope contains a `D4` or `EVIDENCE_SPEC` unit (whatever its kind) | `TEST_INTEGRITY` and `BOUNDARY` families as secondary checks on every obligation |
| `REPAIR` | additionally an `EVIDENCE` obligation whose specification failed before the repair (a regression oracle) or a `REVIEW` stating why none exists |
| `MIGRATE` | a `REVIEW` obligation whose judgment is a `MIGRATION`-class equivalence (§19.5) |
| `AUTHOR` (D1-D3 authority) | a `REVIEW` obligation, an `ACCEPT` obligation at the domain's class, and the `o1_content` slot (§13.5) |
| `INVESTIGATE`, `DOCUMENT` | a `REVIEW` obligation; for `specialist = "MAINTENANCE_AUDIT"`, the `audit_conclusion` slot |

#### 13.4 Control tightening: the closed whitelist and its order

An amendment is **control tightening** (R1) iff every field of the item and its contract is unchanged or moved only in its tightening direction, and the item's prose is byte-identical; every other change, including any prose change, is R2. Prose carries meaning a reviewer judges, so machinery never classifies a prose change as tightening.

| Field | Tightening direction |
|---|---|
| `write_scope`, `dependencies` allowance, `evidence_specs`, `homes` | subset (resolved in `Σ` at the comparison) |
| `frozen` | superset |
| each obligation | `id`, `statement` and primary `verifier` unchanged; `secondary` may gain `HARD` checks |
| `expectations.slots`, `escalation.triggers` | superset |
| `budget` | not greater |
| `scientific` | `NOT_APPLIES` to `APPLIES` only |
| `kind`, `authority`, `specialist`, `objective`, `governing`, `acceptance_criteria`, the obligation set, `expectations.artifacts`, `expectations.evidence`, `gates`, `depends_on` | unchanged |
| item prose: every byte of the item's part outside its `ssds-item` block, including every span a `ref` names (objective, obligation statements, constraints, non-goals) | byte-identical to the accepted revision |
| any other field, including fields later schema versions add | not in the whitelist: R2 |

The relation `r ⊑ r'` holds iff the item prose is byte-identical and every field of `r'` is reached from `r` by its direction; it is reflexive and transitive and is always checked against the **accepted** revision, so tightening then loosening is caught. It is the only rule-defined coverage order (`PLAN_CONTROL`, §4.4). It claims only that the acceptance's conclusion about what is asked still applies under tighter controls, so a standing rejection of a revision reaches every acceptance of a revision with the same prose and fixed fields, in any item or plan, which has a tightening in common with it, whatever the current revision is, and only the rejecter or the owner relieves it (§5.10 (b)); feasibility is not claimed, and a scope narrowed too far surfaces as an `INFEASIBLE_CRITERION` or `SCOPE_DEVIATION` request. Adding an obligation narrows what is admissible and is therefore R2.

#### 13.5 Result slots [D3 decision; §19.2 delegation schema]

The delegation request is the work contract; the return is the `TASK_RESULT` with typed slots. Each slot holds a typed value, or `NONE` with an enumerated reason, or a content reference to a narrative home. An empty required slot without a typed reason is `INCOMPLETE` (§14.4).

| Slot | Content | Triggered by |
|---|---|---|
| `deviations` | declared boundary deviations (units, reason codes) | every implementer task |
| `unverified_assumptions` | assumptions with targets | every implementer and investigator task |
| `claims` | each factual claim with the record ids establishing it | every task |
| `findings` | material findings (target identities, materiality, inquiry status, home reference, and for a re-review the status `OPEN` or `RESOLVED` of each earlier finding by its reference) or `NONE` | `scientific = APPLIES`; every investigator task |
| `null_envelope` | examined and materially unexamined areas, materiality basis | tasks that produce, run or review realized results or prepare gate evidence |
| `variant_search` | count and kind, selection criterion and data (including held-out reuse), lineage, known lower bound where history is missing | tasks that may select among analysis, pipeline, preprocessing, model or parameter variants |
| `tension_search` | searched scopes, unreachable places, each tension with entries, binding and asserter | tasks relying on accepted D1/D2 authority for a consequential judgment |
| `choices` | consequential choice, effective value, origin, chooser, binding or `PROPOSED` | tasks building or changing a scientific pipeline, analysis or report |
| `retention` | what the change retains, projects and omits, with proposed defaults marked | the same tasks, unless accepted authority states the realized record |
| `delegate_returns` | each delegate's findings, null and variant answers, or the gap | tasks that delegate under `scientific = APPLIES` |
| `bidirectional` | reverse-direction finding, or "no reverse-direction finding survives" | review tasks on scientific subjects (§16.5) |
| `o1_content` | realized record, reader, routine questions, marked product surfaces | `AUTHOR` items for D1-D3 authority over scientific software |
| `revision_assessments` | one entry per subject revised: the subject and revision assessed `(s, r)` and the run it is made in (machinery-filled, §10.2); the machinery-computed predecessor, which the reviser may extend with a reason (§10.2); per found tension: applicable / inapplicable with reason / review-required, asserter; proposed until the revision is accepted | `AUTHOR` items revising D1/D2 authority, for the revision their candidate yields; the revising review `REVIEW(s, r)` (§10.2) |
| `audit_conclusion` | `HEALTHY`, `WATCH` or `ACTION_REQUIRED`, with each finding's scope and expected improvement | `INVESTIGATE` items with `specialist = "MAINTENANCE_AUDIT"` |

#### 13.6 System contracts

| Obligation kind | System contract |
|---|---|
| `REVIEW`, `PLAN_ACCEPT`, `ACCEPT`, `ASSESS`, `READING`, `SPEC_REVIEW`, `JOINT_INVARIANT`, `ADJUDICATE*` | write scope empty; required slots `claims`, `findings`, `bidirectional` for scientific subjects, and `revision_assessments` for a revising review `REVIEW(s, r)` (§10.2), carried on the task's `TASK_RESULT`; the default budget (§13.7), spent only while the obligation is unanswered (§10.3); escalation triggers per §15.4 |
| `INVESTIGATE` from intake, `INTAKE` | write scope empty; `homes` from policy; slots `claims`, `findings`, `unverified_assumptions` |
| `COORDINATE`, `CONTRACT` | write scope the plan's units; slots `claims` |
| `REVALIDATE`, `REQUALIFY` | the contract of the original record's task where it has one, else the kind's contract above |

#### 13.7 Task partition and budgets

A `PARTITION` coordination decision splits the **execution** of one item revision into tasks, never the item: their obligation sets partition the item's obligations exactly (for a re-partition, its undischarged obligations); their write scopes are pairwise disjoint subsets of the item's; their order is acyclic. Lint checks all three, a re-partition against the item's obligations undischarged at its admission; a superseded `PARTITION`'s part obligations that were discharged at the later partition's admission stay derived from it and stay among the item's required obligations, so one that reopens by drift (§10.4) is still its part's and is ready again when its outputs moved; its parts that were then undischarged are replaced by the later partition's and are no longer required (they stay as history). Example: `P1` has parts `a` (integrated) and `b` (pending); `P2` re-partitions `b` into `b1` and `b2`; the item is discharged when `a`, `b1`, `b2` and the item-level review are; if a later change moves `a`'s outputs, `a` reopens and is dispatched; `b` is never required again, and a request from `b`'s in-flight task is rejected at step 7 (its bound obligation is no longer required), its never-lost records salvaged. Each task's contract is the item contract restricted mechanically to its share, each part's task is bound to its share's implementer obligation, which the decision derives per part (an obligation of the item's kind identified by the item revision, the `PARTITION` record's identity and the part's index in it), and its integration claims that obligation and the rest of its share; each part is its own enactment (§5.2). The item, its plan acceptance and its scope are unchanged. The item is discharged when every part is and an item-level review of the integrated result has passed, because separately reviewed parts can violate a joint property; an adverse item-level review is a standing adverse review of each part whose outputs its findings name (§10.4); the item-level review's target is the item revision's integrated result, its output `content` entries naming the parts' latest integrated outputs, over whose authors its independence is measured and its reviewer selected (§5.10 (a), §16.5); it is derived over the parts' latest integrations, waits on a part's re-dispatch while that part's outputs have moved, and is derived anew when a part integrates again (SD-37); policy may waive the item-level review only for named item kinds. A later partition supersedes an earlier one only for obligations not yet discharged: it partitions only the item's undischarged obligations, and the superseded `PARTITION`'s discharged part obligations stay as they are.

**Budgets [D3 decision].** **[proposed default]** 3 iterations; system cap 10. Within budget, an `INCOMPLETE` result or a NO-PASS whose findings all lie within the item's write scope and obligations starts the next iteration mechanically (R0), in the order §10.4 gives, whose brief carries the conformance view and review findings as data, not the previous attempt's narrative. Budget exhaustion, a NO-PASS finding outside the item, and every `DISCREPANCY` are `COORDINATE(plan)` routes as §10.4 and the §10.2 row state them. An operational failure is a Dispatcher retry and spends no iteration.

### 14. Conformance verification and the check library

#### 14.1 Conformance

**Conformance** of a task result is an S3 classification evaluated in the candidate's frame: a pure function of the contract at the task's basis, the base and candidate trees, the result record and the observations recorded for that exact candidate. It is never stored. For a result without a candidate (reviewer, principal and records-only investigator results), conformance is the same function over the result record and its contract alone, and its result-only templates are also enforced at admission (§8.3 step 7). Expensive or nondeterministic checks (test execution, mutation testing, static analyzers) run on the exact candidate by a designated runner and are recorded as `CHECK_EXECUTION` observations; deterministic checks are memoized like analyzers. No component is added: Derivation evaluates, the Dispatcher executes, Admission enforces (§8.3 steps 3 and 7).

#### 14.2 Templates and force

Check templates are fixed, versioned functions of `ρ_n`. A contract only parameterizes them and never carries executable check code. A project-specific template enters only by human-gated ruleset adoption after qualification (§14.7). Each template declares one **force**: `HARD` templates may yield `VIOLATION`, `INCOMPLETE` or `DISCREPANCY`; `HEURISTIC` templates yield `SIGNAL` only. Every template that reads prose is `HEURISTIC` by system rule, so no control decision parses prose (A7). A model's verdict is never a template: it is an R2 judgment.

#### 14.3 The library [D3 decision]

| Family | Template | Parameters | Force |
|---|---|---|---|
| `BOUNDARY` | `write_scope` (effect-keyed write set, §1.2, ⊆ write scope; for `IMPLEMENT`, `REPAIR`, `MIGRATE` and `DOCUMENT`, no D1-D3 unit in the write set) | — | `HARD` |
| | `protected_surfaces` | — | `HARD` |
| | `frozen_interface` (public symbols and signatures, by language analyzer) | symbol set | `HARD` |
| | `dependency_allowance` (manifest additions ⊆ allowance) | allowance | `HARD` |
| | `generated_untouched` (no hand edit of `GENERATED` units) | — | `HARD` |
| | `credential_values` (known patterns, high entropy, in content) | policy pattern set | `HARD` |
| `TEST_INTEGRITY` | `no_deletions`, `no_skips`, `no_xfail` (tests deleted, skipped or marked expected-to-fail) | test selectors | `HARD` |
| | `evidence_specs_untouched` (outside `evidence_specs`) | — | `HARD` |
| | `fewer_assertions`, `widened_tolerance` | — | `HEURISTIC` |
| `OBLIGATION` | `required_artifact` (present and linked by derived `TESTS` relation) | artifact | `HARD` |
| | `required_evidence` (realized by the designated runner on the exact candidate, passing) | specification | `HARD` |
| | `evidence_basis_fields` (regime, precision, backend, seed, replicate match the specification) | — | `HARD` |
| | `slots_filled` (required slots filled or `NONE` with reason) | — | `HARD` |
| | `no_new_stubs` (placeholder bodies, `NotImplementedError`, `TODO` stubs in written units) | language | `HARD` |
| | `mutation_strength` (§14.5) | threshold | `HARD` |
| `FAITHFULNESS` | `outcome_consistent` (`COMPLETE` with an unmet obligation) | — | `HARD` |
| | `deviations_declared` (declared deviations equal detected breaches) | — | `HARD` |
| | `citations_support` (every cited record exists and supports its slot; a failing realization cited as passing) | — | `HARD` |
| | `governing_at_basis` (cited governing units at their basis revisions) | — | `HARD` |
| | `prose_numbers`, `certainty_vocabulary` | — | `HEURISTIC` |
| `DOMAIN` | `dimensional_consistency` (annotated quantities, §14.5) | — | `HARD` |
| | `tolerance_declared` (numerical claims in annotated units carry tolerance and precision) | — | `HARD` |
| | `layer_direction` (declared references respect layer order) | — | `HARD` |
| | `unit_inference` (unannotated quantities) | — | `HEURISTIC` |
| `ORACLE` (declarative mechanical oracles, §6.5) | `EXACT`, `ABS_TOL`, `REL_TOL`, `ULP_TOL`, `RANGE`, `SET_EQUAL`, `MONOTONE` | tolerance, range, order | `HARD` (as oracles, not contract checks) |

Each template has exactly one force. Removing every `HEURISTIC` template must leave every admission decision and every discharge unchanged (§31).

#### 14.4 Classes and set-valued aggregation

| Class | Meaning | Routing (R0) |
|---|---|---|
| `VIOLATION` | a `HARD` boundary or test-integrity check failed | the candidate is never integrated; a disclosed breach becomes an amendment request; an undisclosed breach is also an integrity finding to the principal, shown to the reviewer of any later attempt |
| `INCOMPLETE` | a `HARD` obligation check failed, or a required execution is missing | next implementer iteration within budget; beyond it, the principal |
| `DISCREPANCY` | a `HARD` faithfulness check failed | integrity finding to the principal and the reviewer; repetition by one route is recurrence (§15.7) |
| `SIGNAL` | a `HEURISTIC` hit | a labeled pointer in the review brief; changes no disposition |
| `CLEAN` | none of the first three (signals may be present) | `REVIEW(X)` becomes ready |

Conformance is a **set**: every failed `HARD` template contributes its class and finding, every routing of every contributed class applies, and no class takes precedence. An undisclosed breach is both `VIOLATION` and `DISCREPANCY`.

**A clean conformance view discharges nothing.** `REVIEW`-verified obligations stay open until a current review judgment, and every task obligation still needs the review its kind requires (A7). **Disclosed vs undisclosed breaches**: a disclosed breach is a request for more scope, decided by the principal; an undisclosed one is a faithfulness failure and a finding against the route that produced it; neither is integrated. **Advisory pre-flight**: `ask(verify)` runs the pure templates and workspace-local executions before submission, labeled advisory; it never stands in for the designated runner, and an agent's report of it is a finding, never evidence.

#### 14.5 Language analyzers, mutation testing and unit annotation [D3 decision]

- **Language analyzers.** For Python and C++, an analyzer version provides: diff-to-unit mapping (changed byte ranges, and a changed entry type or mode of a file, changed bytes to their innermost owner and a changed entry type or mode to every unit a term of which resolves into the file, empty files and gitlinks included, §1.4, §1.5), one input to the effect-keyed write set (§1.2); public interface extraction (Python: module-level names not prefixed `_` and their signatures, `__all__` where declared; C++: declarations in public headers the policy names, with signatures after preprocessing under the declared build configuration, which reads host headers and is therefore recorded as `ANALYZER_OUTPUT`, §5.9); symbol span resolution for `symbol` scope terms, which must be a pure function of the file's bytes under the pinned analyzer identity and configuration (C++ spans are resolved from the source text without preprocessing; a definition whose span cannot be so resolved cannot be named by a `symbol` term and uses an `anchor`, `heading` or whole-file term instead); derived `IMPORTS`, `CALLS` (static, best-effort), `BUILD_DEPENDS` (from declared build manifests) and `TESTS` (test-to-code, by import and call reachability from test entry points); and completeness declarations with incompleteness markers (§2.6). **[delegated]** The choice of parser libraries and versions; once chosen they are part of the analyzer identity that the ruleset pins (§5.9).
- **Mutation testing.** Seeded mutation over the candidate's changed lines only, with the system operator set (arithmetic, relational, logical and boolean operators, constants, return values, removed calls), executed by the designated runner with a recorded tool identity and seed. The score is killed mutants over non-equivalent generated mutants; mutants the tool marks equivalent and timeouts are reported separately. The contract parameter `threshold` is a fraction; **[proposed default]** 0.70; below it the check is `INCOMPLETE`. **[delegated]** The mutation tool per language.
- **Unit annotations.** Two forms are read: `typing.Annotated[<type>, Unit("<expr>")]` in Python, and the comment form `ssds:unit <name> = <expr>` in any language with a comment leader (§1.2). Unit expressions use UCUM syntax. Unannotated quantities are inferred only by the `HEURISTIC` template.

#### 14.6 The conformance view

The conformance view of a result lists, per obligation: verifier, template results with classes and findings, the observations used (by record id, with their runner and custody), and the set-valued class. It is rendered deterministically from derived state and shown to the reviewer and the principal; it is never a judgment.

#### 14.7 Qualifying a template as `HARD` [D3 decision; proposed defaults]

A template is adopted as `HARD` only after qualification on real trajectories, with thresholds and samples frozen before the runs: detection on seeded violations inserted into real trajectories, at least 200 seeded violations across at least 20 trajectories, with a Wilson 95% lower bound on the detection rate of at least 0.95; and false positives on clean real trajectories, at least 300 trajectories, with a Wilson 95% upper bound on the false-positive rate of at most 0.01. A template that misses either stays `HEURISTIC`. The thresholds are **[proposed default]** values; changing them is a ruleset adoption (human-gated). A template later found defective is corrected only by ruleset adoption; admissions are never re-adjudicated, and current conformance is re-derived (§27.1).

### 15. Reports, escalation and coordination

#### 15.1 Report kinds and vocabulary [D3 decision]

Every communication from an agent that can change what happens next is a typed report record, not a message. Narrative stays in its canonical home (the project evidence record or native issue for a finding or tension, the result envelope for a task report); the record carries kind, subject, raiser and role, declared materiality, blocking flag, inquiry status for a challenge, reason and a content reference to the home.

| Kind | Tier | Reasons | Can block |
|---|---|---|---|
| `CHALLENGE`, `CHALLENGE` with `serious = true` | challenge | `AUTHORITY_DEFECT`, `EVIDENCE_DEFECT`, `CONFORMANCE_DEFECT`, `STRUCTURE_DEFECT` | yes (if blocking; serious always) |
| `FINDING` | support | `TENSION`, `ANOMALY`, `OPPORTUNITY`, `DEFECT`, `INSPECTABILITY_GAP` | no |
| `AMENDMENT_REQUEST` | support | `SCOPE_DEVIATION`, `MISSING_PREREQUISITE`, `INFEASIBLE_CRITERION`, `CONTRACT_DEFECT`, `AUTHORITY_DEFECT` | the raising task (if blocking) |
| `BLOCKER` | support | `PREREQUISITE_UNAVAILABLE`, `ENVIRONMENT`, `AMBIGUITY` | the raising task |
| `HUMAN_QUESTION` | support | `DECISION_NEEDED`, `CLARIFICATION` | the raising task (if blocking) |

**Materiality**: `ROUTINE` < `MATERIAL` < `CRITICAL`, declared by the raiser and raised, never lowered, by the floors.

#### 15.2 Persistence

Every obligation derived from a report or challenge (human attention, coordination, adjudication) is keyed on that record's existence and identity. It opens when the record is admitted and closes only when a **resolving record** targets the report by `identity` and stays in force: not superseded, not `REVOKED` or `BLOCKED`, not withheld by a later loss boundary. The report's own currency never closes it. When its target or basis moves, the obligation stays open and its entry is annotated "target changed since raised", so the decider can answer `MOOT` explicitly. Only the raiser may supersede or withdraw its own report; withdrawal or supersession of a floor item leaves human attention open with "withdrawn by raiser" shown; for a non-floor item it moves the entry to the digest. A resolving record from before a loss boundary is withheld, so the obligation reopens. Reports inside an abandoned interval are lost with it, and the `LEDGER_LOSS` gate brief states that open human-attention items there cannot be enumerated.

#### 15.3 Routing table

The routing table is a ruleset parameter mapping `(kind, reason, materiality, target domain)` to derived S3 obligations:

| Report | Derived obligation | Holder |
|---|---|---|
| amendment request, blocker (including a disclosed breach) | `COORDINATE` decision | the plan's principal |
| any blocking report | the raising task is suspended, workspace and basis preserved; it resumes as a new attempt after the decision | Dispatcher |
| challenge | `ADJUDICATE` | the qualified actor policy names |
| Serious Challenge | `ADJUDICATE` and `HUMAN_ATTENTION` | human |
| human question | `HUMAN_ATTENTION` | human |
| `MATERIAL` or `CRITICAL` report | `HUMAN_ATTENTION`, plus `COORDINATE` if it bears on the plan | human; principal |
| `ROUTINE` finding | recorded; `COORDINATE` only if it names a unit of an open item | principal |

#### 15.4 Escalation floors

System semantics fix the floors; policy may raise them, never lower them.

- **`CRITICAL`, always human attention**: a Serious Challenge; a tension or challenge against accepted D1 or D2 authority; a human question; an amendment changing a plan's objective or changing or removing an existing acceptance criterion (computed from the plan diff); an authority-defect request targeting D1 or D2; an admission fenced after an ambiguous publication (raised when the fence is admitted, decidable once it settles) and every `LATE_PUBLICATION` (§22.3); every integrity halt or forced support cycle of integrity type (§5.6-§5.7); any decision R3 owns.
- **Domain floor**: every report whose target includes a D1 or D2 unit is at least `MATERIAL`, computed from the target's effective kind and domain.
- **Disagreement floor**: the floor events of §6.8.
- **Delegate floor**: when a task's contract has `scientific = APPLIES`, every material finding in its E2 slots creates human attention, so material delegated findings survive to the human by mechanism rather than by each intermediate agent's compliance.

#### 15.5 Principal decisions

A coordination task decides each routed report with a `COORDINATION_DECISION`. The allowed outcomes are a function of the report's kind, reason and target domain:

| Outcome | Meaning | Allowed for |
|---|---|---|
| `RESOLVE_LOCAL` | decided inside the item's delegated space; the raising task resumes | blockers, scope questions, routine findings; never an authority-defect or contract-defect request |
| `AMEND` | a plan-unit change follows | amendment requests; blockers; contract defects |
| `CHALLENGE` | a challenge-tier record against the earliest affected owner | any; required for an authority-defect request targeting D3 or D4 |
| `ESCALATE` | human attention | any |
| `DECLINE` | no action, with a reason code; the raising task resumes or ends | non-floor reports only; a report that already created human attention keeps it |
| `PARTITION` | §13.7 | items |

A decision owed with no report behind it allows, for a route §10.4 gives an item obligation (a kept fence, a spent budget, an out-of-scope NO-PASS, a `DISCREPANCY`, an adverse item-level review naming no part), `AMEND`, `PARTITION` and `ESCALATE`, and for a kept fence also `DECLINE`, which resumes the item's own route; `ESCALATE` does not answer it, so the principal's later `AMEND`, `PARTITION` or `DECLINE` does; for detected recurrence or a `REFUSED` joint-invariant, specification or high-consequence review it allows `AMEND`, `DECLINE` with a reason (outside the floors, §15.4), `CHALLENGE` and `ESCALATE`; the `COORDINATE(plan)` obligation for it is answered by the first admitted `COORDINATION_DECISION` naming it, like the answered judgment obligations of §10.3.

An `AMEND` decision is followed by a plan-unit change authored by the principal in the same coordination request; Admission checks binding and role, runs lint with the plan invariants, and integrates the plan-unit change, which enacts nothing by itself. Whether each changed item stays issuable is derived from its plan acceptance and the computed amendment class (§13.4).

#### 15.6 Annotate, merge, upgrade, downgrade

The principal may annotate any human-attention obligation; its framing is Channel A interpretation, rendered apart from the evidence core. It may merge duplicates (the merged entry lists every member, and one human judgment may answer it as a whole), upgrade materiality, and reclassify a non-floor `MATERIAL` report to `ROUTINE` by a `MATERIALITY_RECLASSIFICATION`, which counts only while in force, moves the item to the digest, is challengeable (an upheld challenge or a later loss boundary returns it), and is never a discharge. Floor items cannot be reclassified. Human attention is discharged only by an authenticated human judgment (A8).

#### 15.7 Recurrence

Recurrence is detected mechanically: the same `HARD` template failing on the same obligation across iterations; the same finding family (template, target unit or relation family) across items; repeated discrepancies by one route. Detection creates a `COORDINATE` decision whose brief carries the convergence duty: consider the shared owner and simplification before another local repair, and route a challenge where the contract or its governing authority may be at fault. Detection is mechanical; the response is judgment.

## Part V. Interface

### 16. Agent and human interface

#### 16.1 Logical operations

The interface is defined independently of transport (`ssds.api.v1`, §28).

| Operation | Purpose |
|---|---|
| `open(task)` | the task brief (§16.3) and workspace locator |
| `ask(query)` | typed queries (§16.2), answered at the task's basis |
| `read(ref)` | content by unit identity or path; recorded into the basis (§16.4) |
| `report(item)` | a typed report (§15.1) or a proposed relation |
| `submit(result)` | outcome from the task's allowed set, the contract's required slots, plus the workspace. Machinery builds the admission request and supplies the facts: diff, touched units, changed authored relations, reads, basis, derived consequences (A6). The response is `PROVISIONAL` until the entry is admitted, then `ADMITTED` or `REJECTED` with reason codes; for a candidate it then reports conformance as derived |
| `decide(gate)` | human only: a gate brief or inspector entry and an authenticated decision |

Within a task, `ask` and `read` answer at the task's basis (snapshot isolation); `ask(changed)` reports admitted changes since the basis that intersect the task. The agent never declares write claims, revisions, edges (except by writing authored relations as semantic content), subject roles, plan patches, lifecycle states, reconciliation steps, its own conformance or any decision class. A principal changes a plan by editing its plan unit; reviewers and principals submit judgments and decisions through `submit`.

#### 16.2 Query classes [D3 decision]

| Query | Answers |
|---|---|
| `governs(x)` | the governing units of `x` with revisions, validity and inclusion path |
| `depends(x, class, direction)` | prerequisites or dependents per completeness class, with widening state (`EXACT`, widened scope, `UNBOUNDED`) |
| `explain(x)` | a unit, record or obligation: kind, status, basis, why current or not |
| `evidence(claim)` | evidence for a claim: realizations, assessments, disagreement state (`disputed`, `stale` with the discriminating observations), binding health |
| `blocked(x)` / `stale(x)` | why: the basis entries, challenges, quarantine, loss withholding or integrity state responsible |
| `impact(diff)` | the derived impact set of a workspace diff or proposed edit |
| `verify` | advisory pre-flight against the task's contract (§14.4) |
| `locate(locator)` | §1.11 resolution of a tension or authority locator |
| `tensions(authority)` | in-repository `CHALLENGES` relations and recorded challenges bound to the authority's identity, earlier revisions and predecessors; native homes listed as searchable-elsewhere with their identities |
| `history(x)` | ledger history of `x`; offered only when the PEM predicate fires or on explicit request (`HISTORICAL`) |
| `search(text)` | text or semantic search; results are `CANDIDATE` only |
| `changed` | admitted changes since the task's basis intersecting the task |

Every answer names the qualified ledger head it was derived at (§23.4); with no qualified head, answers are labeled `UNQUALIFIED` (historical) and claim no currentness. Answers are deterministic for identical basis, query and policy version; search indexes record their versions, and nondeterministic search contributes only `CANDIDATE` items outside the determinism guarantee.

**Epistemic labels.** Every context item carries one class and its acceptance status and inclusion path:

| Class | Meaning |
|---|---|
| `GOVERNING` | authority the task's subject concretizes or is constrained by; mandatory |
| `IMPLIED` | reached by accepted authored relations inside a judged-complete scope |
| `ADJACENT` | reached by derived structural relations; completeness per analyzer declaration |
| `EVIDENTIAL` | evidence for the subject's claims, with current, stale, disputed or unavailable status |
| `HISTORICAL` | PEM entries and Git history; offered only when the PEM predicate fires or on explicit request |
| `CANDIDATE` | search or embedding hits and unaccepted proposals; never authority, never closure support |

Acceptance statuses: `valid`, `provisional`, `disputed`, `challenged`, `stale`, `drift`, `quarantined`, `ill-formed`, `loss-withheld`, `unclassified`.

#### 16.3 Task briefs and duty compilation [D3 decision; §19.2 activation and injection]

A drift task's brief also carries what §10.4 requires: the change that moved `out(o)`, the item or absorption that made it, and the later accepted changes it preserves. A task brief contains, in order: (1) objective, obligation kind and workflow role; (2) allowed outcomes; (3) governing content inline — the exact text of governing units at the basis revisions; (4) the contract's boundaries, constraints, non-goals and delegated space; (5) obligations with verifier class, acceptance criteria, required evidence and required slots; (6) open challenges, findings and provisional states touching the subject, and for a later iteration the previous conformance view and review findings as data; (7) **incompleteness notices**: widened or `UNBOUNDED` bases, incomplete analyzers, proposed-only relations, parts whose validity comes from a coarser subject, quarantine, loss-withheld records, a pending publication outcome, unobservable reads on this route, and the qualified head; (8) the governing version (§16.9); (9) escalation triggers, budget, workspace and submission instructions.

Briefs are rendered deterministically from derived state by version-bound templates; no model translates machine state. **The duties a brief carries are compiled, never selected by wording** (A4):

```text
duties(task) = role_core(role)                                -- the role's authority and prohibitions (§12.3)
             ∪ domain_core(domain(subject))                   -- the governing SSDP role entrypoint's contract
             ∪ kind_duties(obligation kind)                   -- e.g. review: Challenge Pass, out-of-matrix pass
             ∪ slot_duties(required slots, §13.5)             -- each owed question, inline, as a typed slot
             ∪ injected(events)                               -- owner depth at the situations it matters
```

**Domain cores** are the version-bound text of the SSDP role entrypoint for the subject's domain (D1 scientific-formulation, D2 numerical-algorithm-design, D3 software-design, D4 software-implementation), including its entry contract and its scientific checks, at the protocol source the ruleset pins. Specialist cores apply by item: the documentation core to `DOCUMENT` items; the maintenance-audit or repository-hygiene core to `INVESTIGATE` items by their `specialist` field.

**Injection events.** Owner depth that the 7.2.1 entrypoints load conditionally is injected mechanically when its predicate is a recorded or derived event:

| Event (derived) | Owner text injected (version-bound) |
|---|---|
| obligation is `ACCEPT`, `REVIEW` or `AUTHOR` on a subject of domain D1/D2/D3/D4 | that domain's reference owner (scientific formulation, numerical algorithm design, architecture and design, specification and implementation) |
| `ASSESS`, `READING`, `ADJUDICATE_DISAGREEMENT`, `SPEC_REVIEW` | evidence owner: applicability, assessment disagreement |
| the subject or its governing closure declares `defines`, a parameter family, or an external import | semantic-definition owner |
| recurrence detection; budget exhaustion; a repeated finding family | convergence owner, active simplification |
| PEM predicate: the item kind is `MIGRATE`, or the task replaces mature machinery (policy-tagged units), or recurrence detection | PEM owner, plus `HISTORICAL` items |
| `GATE` preparation; a `scientific = APPLIES` review | workflow Channel C; scientific-inspectability owner as optional depth |
| `AUTHOR` revising D1/D2 authority; the revising review `REVIEW(s, r)` (§10.2) | the revising duty and tension-search duty |
| a Serious Challenge raised or adjudicated | kernel Challenge rules |
| subject in `LEGACY(p)`, or a declared version mismatch | versioning owner; the brief renders under `p`'s profile |
| write scope intersects units tagged by policy with a concern (`security`, `storage`, `concurrency`, `performance`, `configuration`, `release`) | that concern owner |

A duty that is not triggered is not carried, because surplus duty text causes narration nobody owed.

#### 16.4 Read recording

`read` records `(u, r)` or the path's content identity into the task's basis. Harness adapters that can observe file reads add them as observed reads. On routes where reads cannot be observed (manual, Git-envelope), the basis is the mechanical minimum plus `read` calls plus declared reliance, and the brief and the result's provenance state "reads not observed" (§9.4). No consumed-package ledger exists beyond read recording **[D3 decision; §19.2]**: the rendered brief is recorded by content identity in the task's envelope, so the doctrine text an agent was given is recoverable exactly; finer package-access accounting would be provenance the decision does not need (the 7.1 package-access ledger stays retired).

**Typed control facts versus narrative [D3 decision; §19.2].** Typed control facts in records: kinds, outcomes, targets, bases, reason codes, materiality, inquiry status, slot structures (identities, counts, enumerations, record references). Narrative in native homes by content reference: rationale, interpretation, finding prose, review argument, gate commentary. A slot that needs prose holds a content reference; its presence is checked (E2) and its content is judged (E3).

#### 16.5 Review briefs and constructed independence

A review brief **contains**: the governing content inline; the contract; the candidate diff and machine-produced facts; the conformance view with every `SIGNAL` as a labeled pointer; the evidence with status, including, for a candidate changing a specification, the counted failures the change would make stale (mechanical) or whose discriminating readings it would stop covering (assessor-read), as a required review item; the result's disclosure slots, labeled as the author's claims to test; for a scientific subject, the 7.2.1 bidirectional Review question as the required `bidirectional` slot (an explicit "no reverse-direction finding survives" is valid; an empty slot is `INCOMPLETE`); for a substantial authority review, the out-of-matrix abstraction-adequacy duty.

It **excludes**: the author's outcome classification, rationale and narrative; commit messages and transcripts; the principal's annotations and expectations; any earlier conclusion by the author. An acceptance or gate brief carries every standing adverse judgment whose reach includes the triple asked, and, as history, every standing objection on a subject or unit that a declared lineage (`renamed_from`) links to the one asked (§5.10 (a)); the same carry applies to the brief of the next judge of an equivalence, completeness, intake disposition or product-scope acceptance. A review brief's **evidence section** marks the current check executions and realizations of the exact candidate, which the review relies on (§4.3); earlier, superseded or stale runs are history. In a review, every standing transformation `NO_PASS` or `NONCONFORMANT` whose reach includes the candidate (§5.10 (b): a review whose judged scope contains the vetoed review's at the same content, under any item, revision or plan, SD-34, SD-42) is supplied by default, labeled as another reviewer's. In a re-review, the review findings of earlier transformations on the same plan subject that no later judgment resolved, removed and re-identified items included (a finding is resolved when a later review of a transformation on that plan subject, admitted as independent, acting and not vetoed, records it `RESOLVED` in its `findings` slot, §13.5, or the owner's adjudication disposes of it; SD-34) are supplied by default, labeled as another reviewer's; policy may withhold them only where independence of the re-review requires it, and the brief then says so. A plan-acceptance brief (`PLAN_ACCEPT`) likewise carries by default, labeled as another reviewer's, every standing `PLAN_ACCEPTANCE` rejection that names any item of the plan subject being accepted, at any revision (the one asked included) and under any objective revision, removed and re-identified items included (SD-34), or that names an item revision in another plan with the same prose and fixed fields as a revision asked about, whether or not it reaches the revision asked: an amendment of an item's prose or fixed fields, or of the objective alone, makes a new target that the rejection may not reach or whose earlier acceptance it vetoed. A rejection naming several items is carried whole when it names any one of them. It stays carried until a later plan acceptance of that plan subject, admitted as independent, acting in the state (§5.2) and not vetoed, records it `RESOLVED` in its `findings` slot, or the owner's adjudication disposes of it (SD-30, SD-31, SD-34); a `RESOLVED` entry in a non-independent, superseded, non-acting or vetoed record ends nothing.

The Dispatcher launches every review in a fresh context distinct from the authoring task's and the contract author's, and selects a transformation reviewer independent of `authors(J)` (§5.10 (a)) so that Admission's `nonind` check is not spent on predictable refusals, and records lineage class, model family, route and toolchain. Independence fails closed (§12.2). Where a claim relies on independence, the review judgment records material common-mode dependencies (shared model family, source corpus, toolchain, oracle); policy may require a different model family or a distinct evidence route for high-consequence surfaces. *Residual:* the artifact under review can carry its author's framing in comments and docstrings; that is content to review and cannot be stripped.

#### 16.6 Gate briefs (Channel C) [D3 decision: template obligations]

A gate brief is rendered at a named qualified head, in this order, each section a deterministic projection of records:

1. **Evidence core (non-narrative, separable, first).** Gate identity and the decision asked; subject identities, revisions and scope; qualified head; coverage (denominators; included, excluded, missing, failed counts; selection rule; complete, sampled or thresholded); key data and trajectories as records, tables and links to canonical artifacts; findings as data — every standing adverse judgment whose reach includes the decision asked (§5.10), from any frame, run, enactment or item, which vetoes a passing decision until its author reassesses or the owner adjudicates; open challenges, disputed evidence with the observations that keep it counting, stale and unavailable evidence, provisional and risk-overridden states, integrity and quarantine states; tensions found by the relying search with every recorded entry, binding and native asserter; variant-search disclosures from the slots; known missing realized records, each classified (non-material limitation, material uncertainty, blocker, provisional continuation, prospective-retention trigger). The core's **required-evidence section** marks, for each evidence obligation the gate requires, the passing admissible assessments through which the core shows it holding at the rendering head (or that it does not hold: `UNAVAILABLE`, stale, disputed); these, and for a D1/D2 revision the revision-assessment record, are the decision's supporting premises (§4.3). Every other evidence record shown, stale or replaced records of a required obligation included, is history, referenced by identity.
2. **Consequential-decision disclosure.** Anomalies, uncertainty, alternatives considered, unresolved findings, each linked to its record; and every gate decision and acceptance recorded in an earlier enactment of the same obligation whose subject content was identical, with its outcome and qualification, so a replacement iteration's human decision can be made against what was already decided (SD-26). A passing one supports nothing here (§5.2); an adverse one vetoes (section 1).
3. **For a gate accepting a D1/D2 revision**: from every revision-assessment record that counts for exactly that revision (§10.2), the machinery-computed predecessor with any extension the reviser recorded, and the tension applicability assessments, including those marked inapplicable, with their asserters, marked proposed, and the route that produced the revision; where the revision changed only because a nested subject of another kind changed (§1.2), that statement.
4. **Interpretation (Channel A)**, labeled: the preparing agent's and principal's framing.
5. **Allowed outcomes**, and the required `adequacy` and `qualification` fields of the `GATE_DECISION`.

Rules: agents and machinery may request a gate and prepare its interpretation; they cannot synthesize a human judgment. Admission refuses an `ACCEPT` with `adequacy = INADEQUATE`, and an `ACCEPT` with `qualification = UNQUALIFIED` while the evidence core lists required evidence that is `UNAVAILABLE`, `disputed` or stale, or a missing record classified material uncertainty or blocker; whether other missing records could plausibly change the judgment is the human's semantic judgment, recorded in `adequacy` and challengeable. A gate on a `NATIVE` D1/D2 revision without a counting revision-assessment record for it is not ready, and its `ACCEPT` is refused (§10.2, §8.3 step 7), so section 3 always has a counting record. Every gate is an inspector entry (§16.8).

#### 16.7 Decision briefs

A coordination task receives a decision brief rendered at the qualified head: the plan objective and each item with its state (awaiting contract, ready, running, suspended, under review, discharged, open); the decision obligations owed, each led by the report's record core, the target identities and revisions, and the relevant conformance and review outcomes, followed by the allowed outcomes (§15.5); budgets, recurrence detections and discrepancies; the plan's open human-attention items; what changed since the previous coordination. Narrative reports are reached by reference. The decision brief *is* the plan's working state: derived, version-bound and reproducible, so the principal keeps no memory between invocations.

#### 16.8 The inspector view and digest

The human interface for everything R3 owns is the **inspector view**, an S3 view rendered deterministically.

- **Ordering [D3 decision].** Open human-attention obligations sort by the key `(−w, c, p, id)`: `w` the number of obligations whose readiness or discharge waits on this one (transitively through readiness prerequisites); `c` the consequence class, `CRITICAL` before `MATERIAL` before `ROUTINE`; `p` the ledger position at which the obligation opened (older first); `id` the obligation identity.
- **Each entry, in order**: the evidence core (the report or floor record, target identities and revisions, conformance and review outcomes, cited evidence with status); the principal's framing labeled as interpretation; the allowed outcomes. Merged entries list their members.
- **Answering.** `decide` records an authenticated `HUMAN_DECISION` or `GATE_DECISION`; its effects propagate mechanically (suspended tasks resume, amendments follow, obligations discharge or reopen).
- **Qualified gates.** A `QUALIFIED` gate `ACCEPT` keeps an entry open in every state where it is eligible, naming its qualifying records, until it is superseded in that state (§5.5 `elig`, SD-24, SD-25); a decision reused across a tenure restart keeps its entry open while it caps validity.
- **Digest.** Below the open entries, a cold digest of what agents settled since the human's last acknowledgment: R1 decisions, materiality downgrades, declined reports, discrepancies, recurrences, and failures counted but not yet at a floor event. Every digest item is challengeable; reading it is never required for work to proceed.
- **Trust boundary.** Where content is confidential the view gives the strongest safe aggregate and states the limitation. Human unavailability leaves human-attention obligations open; dependent work stays not ready, independent work proceeds.

#### 16.9 Version binding [D3 decision; §19.2 in-loop version routing]

Each issued envelope carries `governs`: for a `NATIVE` subject, the ruleset in force, which pins the SSDP doctrine version and its immutable public-source identity used for domain cores and injected owner text; for a `LEGACY(p)` subject, protocol `p`, and the brief is rendered through `p`'s frozen Core profile. The brief states the governing version in its first lines. Admission rejects a record whose `governs` differs from its envelope's (`AUTH_VERSION`). No agent record can adopt a version: adoption is a human-gated `RULESET_ADOPTION` (doctrine pin) or `MODE_TRANSITION`. This realizes the version step and self-adoption guard at E0 for native work.

#### 16.10 Transports, harnesses and bootstrap [D3 decision]

Three transports expose the same operations: an MCP server; the CLI (`sdp ssds <operation>`, §26.3); and a **Git-envelope** transport for zero-context web agents: an immutable signed task envelope `task.json` plus the rendered brief on an isolated run ref `refs/heads/ssds/run/<task-id>`, a result envelope `result.json` plus candidate commits written back to that ref, and polling-first fetch of that specific ref. Run refs are transport: never merged, retired by policy, regenerable from the ledger and obligations. Harness adapters only map operations and launch, observe and cancel executions (admit, start, events, control response, cancel, terminal result, §26.4). The bootstrap is `Execute SSDS task <task-id>` plus the minimum locator the environment does not already bind (repository, run ref, envelope path, protocol source). It fails truthfully when protocol material cannot be resolved. Transport and process success never imply evidence admissibility or task success. Local and Git-envelope transports give identical admissions for identical submissions.

## Part VI. Evidence and intake

### 17. Evidence

| SSDP evidence concept | SSDS 8 representation |
|---|---|
| specification | an `EVIDENCE_SPEC` unit with `EVIDENCES` -> the unit holding the claim, declared or derived `EXECUTION_DEPENDS_ON`, and its specification declaration (§17.1) |
| realization | a `REALIZATION` observation whose basis has a **target** part (the claim's content) and an **execution** part (executed content, §6.3) plus the configuration fields (§17.2) |
| observation | the realization's evaluated outcome, by content identity, plus references to native artifacts (logs, data) |
| assessment | an `EVIDENCE_ASSESSMENT` judgment; a reassessment replaces an earlier one only by authorized supersession (§8.3); a counting failing assessment and a passing assessment for one obligation are a disagreement (§6) |

#### 17.1 Specification declaration [D3 decision]

Every `EVIDENCE_SPEC` unit carries exactly one specification declaration, a TOML document in a fenced `ssds-spec` block (Markdown) or a file `*.ssds-spec.toml` inside the unit's scope. It is semantic content: part of the unit's revision and of every reading.

```toml
oracle      = "DECLARATIVE"          # DECLARATIVE | EMBEDDED | ASSESSOR_READ (§6.5)
runner      = "ci-linux-x86_64"      # designated runner class (§17.5)
time_bound_hours = 24                # ≤ 168 for Dispatcher-run executions (§6.9)
outputs     = [ { name = "l2_error", type = "float64", canonical = "binary64-hex" },
                { name = "converged", type = "bool" } ]
verdicts    = [ { output = "l2_error", template = "ABS_TOL", params = { reference = 0.0, tol = 1e-8 } } ]
fixed       = { regime = "re<2000", parameters = "configs/case3.toml", backend = "cpu",
                precision = "float64", environment = "image:sha256:…" }   # an environment identity (§6.3)
granularity = { mode = "SINGLE" }    # or { mode = "ENSEMBLE", replicates = 32,
                                     #      statistic = "mean_and_ci95", seed_policy = "FIXED_SEQUENCE" }
output_renames = {}                  # old output name -> new name (§6.5)
```

`fixed` attributes are **claim-defining**: a realization differing in one is inadmissible for the specification's obligation. Every execution attribute the declaration does not fix is **free** (execution variation): admissible assessments differing only there conflict. What each kind fixes by default **[D3 decision]**: `DECLARATIVE` and `EMBEDDED` specifications fix nothing beyond what they declare; an `ENSEMBLE` granularity fixes the replicate count, statistic and seed policy; every specification's runner class is fixed. Precision, backend and environment are fixed only when declared, and the D2 owner of the claim decides which are claim-defining; the default (free) is the conservative one for disagreement: a free attribute's recorded value separates runs in every permissive use and in no adverse one (§6.5). A fixed `environment` names an environment identity (a runner image or an equivalent content-addressed environment); a lockfile of language packages alone does not fix the environment. A recorded attribute the fixed identity does not determine (a host-mounted driver, a CPU kernel selected at run time) stays free and is compared by `ext` like any other.

A change to a specification unit raises `SPEC_REVIEW` for its owner (a reviewer of the claim's domain), whose brief lists the counted failures the change would make stale and the readings it would stop covering (§16.5).

#### 17.2 Realization basis fields

A `REALIZATION` records: specification unit and revision; claim units and revisions (target); the **recorded execution basis** (§6.3) — unit, read, widened, pin and attribute entries, the recorded resolution context, and the bounding completeness judgments or `UNBOUNDED` — recorded once and read by every consumer (its own currency, §17.4; matching, the floor and the class rule, §6.5-§6.8); unpinnable reads, if any; its **configuration** in the one sense of §6.5 (regime, parameter instance, and each fixed attribute's value, a fixed seed or seed policy included); its **recorded execution attributes**, which are the basis's attribute entries (§6.3), never a second field: the observed value of every attribute its runner class records, fixed or free, and a free seed or replicate identity; runner identity; the tree it ran on; start and end positions; and either a `LEDGER` reference to its evaluated outcome, or `INCOMPLETE` with an enumerated reason (`FAILED_TO_START`, `CRASHED`, `TIME_BOUND`, `MALFORMED_OUTPUT`, `CANCELLED`). Logs and data go to native artifacts by content reference.

A realization with incomplete or malformed evidence is `INCOMPLETE` and cannot enter a `PASS`/`FAIL` assessment. Process exit or harness success is never evidence admissibility.

#### 17.3 Evaluated outcomes [D3 decision]

The evaluated outcome is a canonical JSON object `{output name: value}` over the declared outputs, stored as a `LEDGER`-store object (§21.4). Canonical forms: `binary64-hex` (IEEE-754 bit pattern, exact), `decimal-shortest` (round-trip shortest decimal), `rounded:<n>` (declared rounding to `n` significant digits, a D2 decision of the specification's owner), integers, booleans, enumerations, and `digest` (a content identity of a large output artifact). An `ENSEMBLE` outcome is the declared statistic over the replicates plus the replicate count; replicate-level outputs are native artifacts. Identity of outcomes on failing outputs (§6.6) is byte equality of canonical values.

#### 17.4 Admissibility and currency

An assessment is **admissible** for obligation `e` iff its realization instantiated the specification revision `e` names (or a revision in its lineage under the reading rules of §6.6), every fixed attribute matches that revision's declaration, and the realization is complete. A realization supports a claim at revision `c` only while its recorded execution basis is satisfied (`execution` mode, §4.1: the recorded regions unchanged, or an equivalence judgment of class `CONSUMER:REALIZATION` covering each changed unit) together with its bounding completeness judgments, and its target is `c`. An execution-dependency change triggers a rerun obligation, including the configuration of every failing assessment counted against the claim (§6.9); a target change triggers an assessment-review obligation. Stale passing evidence never discharges. Failing evidence is never dropped by a change (§6).

**Binding health.** `AVAILABILITY` observations record when a referenced artifact becomes unavailable: the historical record survives, and present use becomes `UNAVAILABLE` (an evidence term that needs it is not `T`). Raw data stays in native stores; the ledger stores identities and bounded classifications.

**Realized-record/observation boundary.** A realized-record item is an observation only when an evidence realization produced it; retaining it neither assesses nor re-identifies it. A `CHALLENGE` carries the finding's inquiry status (`EXPLORATORY` or `CONFIRMATORY`) as its own attribute, separate from evidence strength, applicability and disposition. Findings and tensions keep their one canonical home in project evidence records or native issues; the ledger references that home by identity and never becomes it (S13).

#### 17.5 Who may realize evidence: runners and custody [D3 decision]

A realization can discharge an evidence obligation only when a **designated runner** for the specification's runner class executed or reproduced it. Project policy designates runner classes, each as one of:

- **Dispatcher-controlled**: the Dispatcher runs the execution on the exact candidate or merged tree, materialized in the §1.5 representation, in an isolated workspace it owns, with a runner identity key registered in policy; the realization is submitted by the Dispatcher;
- **external custody**: an external runner (HPC scheduler, CI service, laboratory system) designated with its custody identity. Its realization records name the custody evidence (job identifiers, scheduler accounting, signed run manifests) by content reference. A `CUSTODY_ENUMERATION` from that runner must list every run of the configuration it performed before any of its observations can make a failure stale (§6.9).

**Recorded execution attributes and read observation [D3 decision; SD-17, SD-18].** Each runner class's policy designation declares the execution attributes its realizations record (§6.3): environment components at a stated granularity, and backend, precision, device and host or hardware attributes as far as the runner can observe them; every class records a seed or replicate identity it supplies to an execution. It also declares whether the runner observes **every read outside the realization's tree** (files and network); an execution of a class that does not is recorded as having an unpinnable read (§6.3), so its failures support no mechanical stop and go to the owner, red-then-green iterations included. A realization that does not record a declared attribute is treated as having an unpinnable read. Every designated runner materializes the tree in the §1.5 representation, ignoring `.gitattributes` and Git configuration transforms; a runner that cannot is not designated, and its results are findings (below). Because `ext` compares the complete external-input record (SD-23), classes should declare host files as environment components and run with hermetic home and cache directories, so incidental reads do not prevent stops. Declared attributes should be ones the Dispatcher can request: one it cannot request (a node identity) leaves (1) and (3) unobtainable for every failure of the class. A change of a class's declared set makes every failure recorded under the other set unmatchable for (1) and (3), since `ext` compares every attribute either records; the policy change that makes it shows those failures, as §27.3 does for re-identification. Variation in an attribute the class does not declare (for example a run-time CPU-kernel selection under a class that records only its image) is invisible to matching, so a failure caused by it can be made stale by a run that differs only there. That is a disclosed residual (§32.2), not a mechanism; a project that needs such failures to stay counted declares the attribute for the class or fixes it in the specification.

Results an agent reports from its own workspace are findings: useful for direction, never admissible for discharge. A `CHECK_EXECUTION` (§14) is evidence for a scientific claim only where an evidence specification names it.

### 18. Intake: one route for every change of unknown provenance

#### 18.1 Detection

Intake is a set of derivation rules plus judgment kinds over any content not produced by an admitted request. Recorded facts detect it: the live integration ref moved away from the expected head (observed by Admission before every append; a Dispatcher census that notices it requests an absorption); a submitted workspace contains changes outside its reported result; an external branch is offered for import; content differs from accepted revisions (drift); observed structural declarations differ from `Σ` (quarantine); a scheduled census finds untracked or unexpected material.

Two entry paths share one rule set. Content **already on the integration ref** is absorbed (§8.6): the observed tree advances, nothing governing changes, and consequences become obligations. Content **offered as a candidate** (an external or foreign-agent branch, agent work outside its result) is a change whose basis is computed conservatively from its merge base (mechanical minimum plus widening) and reaches the integration ref only through ordinary Admission after its intake obligations are discharged.

#### 18.2 Processing and static classification [D3 decision]

```text
preserve exact identity (commit, ref, tree; nothing executed or deserialized)
 -> diff against the last admitted observed tree; map changed paths to effective leaves (§1.4)
 -> structural declarations: each key of decl(T_n) ≠ Σ_n is a quarantined delta, classified (§1.6)
 -> uncovered paths: proposed new units, statically classified
 -> mechanical consequences (S0/S2): changed revisions make dependent records non-current; aff(Q) and
    ill-formed subjects are invalid
 -> obligations (S3): INTAKE per delta and per uncovered or foreign change
```

**Static classifier.** A versioned machinery function proposing `(kind, domain, class)` for an uncovered path from: path and extension; content-type sniffing by fixed magic bytes and text/binary detection (never parsing beyond a bounded size, never executing, importing or deserializing); Git history (authors, rename history, producing commits); known producers (`GENERATED_FROM` declarations, build manifests naming outputs); parsers of declared manifest formats in data-only mode. Its output is an advisory `INTAKE_CLASSIFICATION` proposal (R0 machinery, enacting nothing). **Opaque active content** — binaries, archives, notebooks with outputs, executables, serialized objects, unknown formats — is proposed `QUARANTINE`.

#### 18.3 Dispositions

| Disposition | Meaning |
|---|---|
| `ABSORB` | accept the content as it stands; for a quarantined structural delta, **adopt** it (§18.4) |
| `RECONCILE` | needs rework; an item or obligation follows |
| `SPLIT` | divide into separately classified parts |
| `ARCHIVE` | keep as historical material |
| `RETAIN_AS_EVIDENCE` | keep as evidence, not authority (`EVIDENCE_RECORD` kind) |
| `MARK_GENERATED` | declare `GENERATED`; regenerate rather than edit |
| `QUARANTINE` | isolate untrusted or opaque content: it stays in the tree but is excluded from governing context, evidence and acceptance basis |
| `REJECT` | revert by an ordinary change; for a structural delta, **realign** the declaration with `Σ` |
| `DISPOSABLE` | classification only; deletion is a separate authorized change |

#### 18.4 Structural intake, adoption and realignment

A quarantined delta becomes effective in exactly one way: an admission request carries an `ABSORB` `INTAKE_DISPOSITION` adopting it, which makes the delta part of its transformation's identity `A` (§7.1), and Admission validates the adopted change exactly as if the requester authored it now (§8.3 step 4): challenge freezes at source and destination, a prospective acceptance bound to the same admission for any promotion, mode consistency, SDG integrity. Adoption is re-authoring under current rules and authority, never ratification of presence, validated under the ruleset in force when admitted. A ruleset adoption never changes `Σ` or `Q`. **Realignment** is an ordinary change that makes `decl(T)[k] = Σ[k]`.

**Contrary dispositions.** An `ABSORB` enacts at its admission (S0), so a later standing adverse disposition of the same delta (§5.10) vetoes the `ABSORB` record's support but does not undo the enactment: it derives the owner's adjudication obligation, and where the owner upholds the adverse disposition, a realignment obligation follows (an ordinary change). A `QUARANTINE` disposition names observed paths; a subject is **under** it while it owns any byte of those paths in the observed tree (innermost ownership, §1.4). Such subjects are treated as `UNCLASSIFIED` for governing use: they have `ok = F` (§5.5) and supply no governing context, evidence or acceptance basis while the disposition stands (§5.10 `stands⁻`), that is, until its own author's reassessment or the owner's adjudication supersedes it, or an upheld challenge disposes of it. A `QUARANTINE` follows paths, not content: content that a later change moves out of the named paths leaves it (§32.2). Admission admits an `INTAKE_DISPOSITION` only on an intake object for which an `INTAKE` obligation has been derived at some position (a quarantined delta, or an uncovered or foreign observed change), and a `QUARANTINE` only naming paths of that object: for an uncovered or foreign change, the paths it changed or added; for a quarantined structural delta, the files its declared terms resolve to before and after the delta, and for the `("governed", "ignore")` key the paths whose governed status the delta changes. The rule concerns targets, never timing: it applies alike to a later contrary disposition, the owner's adjudication and the author's reassessment after an `ABSORB` has enacted the delta. Admission refuses an `ABSORB` of a delta on which an adverse disposition already stands, so neither order lets enactment outrun a standing objection.

**Mechanical adoption of governance-neutral deltas [D3 decision].** Where project policy sets `intake.neutral_auto = true` (default `false`), the Dispatcher may submit an `ABSORB` adoption of a governance-neutral delta as an R0 machinery disposition; it still passes §8.3 step 4 and is recorded and challengeable. A governance-affecting delta always needs an R2 disposition.

#### 18.5 Effect on governance and inspectability

Foreign content affects governance only through lower-stratum facts: changed bytes or semantic declarations change revisions (S2); changed structural declarations are quarantined, and every subject in `aff(Q)` has `ok = F` and cannot serve as validity prerequisite, governing context or acceptance basis until adopted or realigned, while routing (`subj`, scope, tenure) follows admitted structure; uncovered content is `UNCLASSIFIED` and excluded from governing use; illegal relation structure makes its subjects ill-formed. The S3 intake obligations only schedule and explain. Unqualified authority cannot arise from repository presence, because no S0 input that S2 consumes changes by presence alone.

Foreign content is never hidden or discarded: the observed tree is the product and stays buildable and releasable; views show each quarantined delta beside its effective value with the absorption entry that introduced it; every disposition is an ordinary admitted change a later admitted change can reverse. Production is never blocked; what stays open is governance closure. Agent overstep, manual edits, collaborator branches, foreign-agent work, repository restores, manual merges, legacy import and corruption repair all use this one route.

## Part VII. Migration and external units

### 19. Governance modes, migration and cutover

#### 19.1 Governance modes

Every subject is in exactly one governance mode at any ledger position; its parts share it (M3).

| Mode | Meaning |
|---|---|
| `NATIVE` | SSDS-governed: acceptance, conformance and evidence obligations derived and enforced by Admission |
| `LEGACY(p)` | governed by a declared legacy process bound to protocol version `p`; SSDS records and derives but never adjudicates or reinterprets |
| `UNGOVERNED` | production content with no authority system yet; changes recorded, mechanical consequences derived, no conformance claims |
| `UNCLASSIFIED` | unknown content; excluded from governing context, evidence and acceptance basis until classified |

Mode is ledger state, set at genesis per subject and changed only by an admitted `MODE_TRANSITION` acting in the state (§5.2): a cutover's at the integration that carries it (§19.5; a cutover record declaring the admitted frame is refused), any other at its admission. It ends the subject's tenure. A membership change that would move a unit between subjects of different modes is a mode transition for that unit and needs its record (§8.3 step 4); neither an ordinary request nor an adopted foreign declaration can do it silently. A change touching subjects in several modes receives the union of their obligations. Changes confined to `LEGACY(p)` or `UNGOVERNED` subjects may arrive as ordinary commits; they are absorbed and derive only intake classification for uncovered paths plus whatever the mode's policy requires.

#### 19.2 Relying on legacy authority

A `LEGACY_ACCEPTANCE` imports the fact that the legacy process accepted an exact revision of an exact scope: it cites the legacy process's acceptance evidence (for SSDP source, the `PROTOCOL-RELEASE-STATE.yaml` entry and its Review and ratification records at their immutable identities) and supplies the acceptance for that `(subject, scope_id, rev)` without claiming SSDS reviewed it. The imported scope is the scope the legacy process actually accepted: a whole-document or release acceptance cannot be imported onto a section. Native work relying on a legacy subject without an imported acceptance is provisional.

#### 19.3 Reconstruction status and structural refinement

Authority-bearing subjects carry a reconstruction status, `OPAQUE`, `PARTIAL` or `RECONSTRUCTED`, recorded by admitted `RECONSTRUCTION_PROPOSAL` judgments accepted through the subject's owner (proposals alone enact nothing).

**Structural refinement** is an admitted change that partitions a leaf's scope into new leaves declared as parts of the original unit, which becomes or remains a composite subject. Scope conservation is checked mechanically (§1.9). Refinement makes no semantic claim. A byte-preserving refinement leaves `scope_id`, content identity, signature and tenure unchanged, and semantic declarations unchanged unless relations are redirected; the revision is unchanged and the acceptance stays valid; nothing is copied. Parts hold no acceptance of their own: every `validity` reliance on a part routes to the subject; `content` reliance on a part is local to its bytes. Coarse relations stay on the subject until redirected to parts by authored relations, which is a semantic change needing a new accepted subject revision.

#### 19.4 Promotion, demotion, restoration and carve-out

**Promotion** makes a part `A` of subject `P` its own subject. It needs both an admitted declaration change marking `A` a subject (authored, or adopted from a quarantined declaration), which starts `A`'s tenure; and an acceptance on `(A, scope_id(A), rev(A))` in that tenure, by an actor qualified for `A`'s domain, recorded beforehand as a prospective acceptance in the promoting candidate's frame by an independent reviewer and bound to the integrating admission (§7.6). If the request also changes `A`'s domain, the old domain's owner must release it too. The judgment's basis names `P`'s acceptance (`record`) and widens to `P`'s former scope until a completeness judgment narrows it. Promotion is rejected while `P` or `A` carries an unresolved blocking challenge or a revoked revision. The reviewer may conclude `A` is not self-standing; then `A` stays a part or the owner first makes the coupling explicit (`A USES_DEFINITION B`). SDG members are promoted together, as one composite whose scope contains the SDG declaration, or not at all. Neither widening, byte identity nor an unchanged relation set substitutes for the judgment. For a `LEGACY(p)` subject only the legacy process can accept `A` separately.

**Demotion** of `A` into a part of `P` ends `A`'s tenure; `A`'s acceptances leave `ACC(A)` permanently and stay as history. **Restoration** of `A` is a promotion: a new tenure, a new acceptance bound to the same admission; it may cite the earlier tenure's records by `identity`, and prior evidence counts only where currently admissible.

An old acceptance cannot become current again because structure changed. Three independent locks: repository presence never changes `Σ`; an admitted restoration starts a tenure excluding every earlier acceptance (a gate decision or required-kind judgment on the unchanged triple is reused, as the reviewed workplan's `valid` reads it; for a `NATIVE` D1/D2 subject the revision run excludes its acceptances and gate decisions, §10.2, §5.2); after a recorded loss, every earlier acceptance is withheld until requalified or attested (§23.6). Challenges and revocations target triples without tenure, so they bind a restored subject exactly as before, and every signature change is frozen while an affected subject is under unresolved blocking challenge or revoked.

**After promotion** `P` keeps its frozen scope, which still includes `A`'s bytes, and its tenure. Reliance on `P`'s remaining parts stays valid only while that whole scope is byte-identical to `P`'s accepted revision; once `A` evolves it needs a scoped `EQUIVALENCE` for their consumers, acceptance of a residual subject (a new scope), or, for `LEGACY(p)`, a new legacy acceptance. A **carve-out** is a promotion after which `A` leaves `P`'s governance mode (§19.6); the same rule applies. An equivalence relates revisions of one unit and never different scopes; acceptance moves to a new scope only by acceptance of that scope.

#### 19.5 Discovery bottom-up, acceptance top-down; cutover

Agents may propose candidate D3, D2 and D1 units reconstructed from D4 behavior, papers, comments, tests and history. A proposed upstream unit is accepted only through its owner's acceptance (human-gated where policy requires); until then descendants relying on it are provisional, and no D4 behavior creates accepted authority. Reconstruction that cannot recover intent records `PROVISIONAL` or `UNKNOWN` explicitly (M5).

A **cutover** of subject `s` from `LEGACY(p)` or `UNGOVERNED` to `NATIVE` is a `MODE_TRANSITION` enacted only by an integration that carries it (below) and meets:

1. reconstruction status at least the policy minimum (**[proposed default]** `RECONSTRUCTED` for D1-D3, `PARTIAL` for D4);
2. a current `EQUIVALENCE` of class `MIGRATION` stating that representation changed and behavior and meaning did not, or a separately governed change if they did;
3. owner acceptance of the native revision `r` of that exact subject, as a prospective acceptance in the carrying frame (below), bound at integration;
4. for a carve-out from a legacy subject: the subject promoted first, and a `LEGACY_RELEASE` by the legacy process owner (§19.6);
5. the **quiescence record**: the cutover record lists every known in-flight legacy run on `s` (open workplans, branches and tasks bound to `p` that touch `s`) with its disposition `DRAINED`, `PINNED` (continuing in an isolated workspace under `p`) or `MIGRATED` (explicitly re-bound by its owning authority), and the human gate attests the list complete to its knowledge (M6);
6. the human-gated cutover decision.

**A cutover is carried by an integration [D3 decision].** The carrier is a transformation `X` of an accepted item that names `s`: an `AUTHOR` item for a D1-D3 subject (a mode change of D1-D3 authority belongs to its authoring route, §13.2), a `MIGRATE` item otherwise; for a mode change with no content change, an iteration of such an item whose transformation has `tree(C) = tree(B)`. The native revision is `X`'s. Once `X`'s `TASK_RESULT` is admitted, the actor policy designates records the cutover `MODE_TRANSITION` directly (a lifecycle record, so an authenticated human, §3.5), with its quiescence list (condition 5), declaring frame `id(X)`. Admission admits it only while `X`'s enactment has no admitted integration, only if `X`'s item is of the carrier kind stated here and names `s`, and only if no cutover record of `s` is already admitted in that enactment's frames; otherwise it is refused (`ENACTMENT_*`). The integrating admission also requires `s`'s admitted mode to be the record's source mode; once another carrier has cut `s` over, a pending carrier whose frames hold a cutover record has no frame (§7.4) and never integrates, and the work needs a new iteration. A record therefore cannot act after its carrier integrated, and no cutover is enacted except through the integration that checks conditions 1-6. If the carrier integrates first, the cutover needs a further iteration of the item (or a new item, if the item is discharged). It acts in that frame (§5.2), where `s` exists in its prospective `NATIVE` tenure, so `REVIEW(s, r)`, `ACCEPT(s)` and the cutover gate are derived there like any frame obligation and the owner's prospective acceptance is admissible there (§8.3 step 3). Conditions 1-6 are **enactment conditions**: Admission checks them at `X`'s integrating admission, with §7.6, and that integration enacts the transition. The run the cutover starts is `X`'s enactment (§10.2), on the ledger with its task's result before any record names it. A re-cutover after rollback is a new task, so a new enactment and run.

After cutover only Admission governs `s`; legacy-side edits are foreign changes (§18); the legacy representation is historical. A part cannot cut over apart from its subject. Each refinement, promotion and cutover is one admission, so interrupted migration leaves no half state, with one disclosed exception: a cutover whose carrying integration is then fenced or `OVERTAKEN` (§22.2-§22.3) leaves `s` `NATIVE` (mode is ledger state) while the tree returns to the legacy bytes; `s` is then invalid in its native tenure (fail-closed), and the human either re-applies the carrier as a new enactment with fresh acceptance and gate or records a rollback `MODE_TRANSITION` (§32.2). A re-application is an ordinary `NATIVE` change, so conditions 1-6 are not re-checked; legacy work resumed while the legacy bytes were back arrives as foreign changes and goes to intake (§18).

#### 19.6 Carve-out release

A `LEGACY_RELEASE` is a human-gated lifecycle record by the actor policy designates as the legacy process owner for `p`, naming the exact scope released from the legacy process. It is required before a carve-out cutover and enacts nothing else.

#### 19.7 Version rollback

Rollback is version rollback to the immutable pre-cutover baseline (B2): stop Admission for the affected scope, resume the pinned baseline process there (resolved from `PROTOCOL-RELEASE-STATE.yaml`, never guessed), repair SSDS separately. The `MODE_TRANSITION` back to `LEGACY(p)` ends each affected subject's tenure, so pre-cutover legacy imports never revive; a fresh `LEGACY_ACCEPTANCE` is needed. Ledger rollback (§23) is an integrity incident, not a version rollback; an unrecoverable admitted loss adds a boundary, which composes with a later version rollback because the mode change ends tenure and the boundary withholds every pre-loss import independently. A cutover lost inside an abandoned interval leaves the retained mode in force, with every retained import withheld until requalified.

#### 19.8 Documents, workplans and skills after cutover

Change plans and authority documents remain semantic artifacts. In natively governed documents, lifecycle fields (`status:`) and directory placement (`active/`, `archive/`) are removed or generated from derived state and marked non-authoritative; a manual edit to them enacts nothing. Skills remain epistemic procedures and stop owning workflow transitions represented by rules. Historical pre-cutover workplans and records stay immutable under their original semantics.

#### 19.9 Genesis and deployment cases [D3 decision: genesis procedure]

Genesis records project identity, ledger id and location, authoritative replica, trust roots (Admission host keys, Dispatcher issue keys, human authentication mechanism and keys), witness set and quorums with deployment class, ruleset, `Σ_0` and per-subject modes, and the baseline commit. **Procedure (FF-001):** build the genesis entry and `Σ_0` in an isolated workspace; validate every declaration, static check, trust root and witness reachability; obtain the human gate; append and admit it under its own quorum; only then publish any identity or begin derivation as current. A genesis that fails validation publishes nothing.

| Case | Entry | Special |
|---|---|---|
| A native project | genesis with fine subjects, all `NATIVE` | none |
| B SSDP 7 or earlier documents | the manifest declares section-level parts of each legacy subject (the scope its process accepted: a document or a release tree) without rewriting files; mode `LEGACY(p)`; heuristically extracted relations are proposed | version-pinned workplans stay governed by their protocol; section locality serves reading and context; validity routes to the legacy subject; promotion and carve-out cutover per §19.4-§19.6 |
| C mature repository without authority | a few coarse `UNGOVERNED`, `OPAQUE` subjects by top-level region, or `ssds.unclassified`; analyzers give derived structure early | bottom-up proposals, top-down acceptance; production continues |
| D live partial migration | mixed modes | a production edit makes non-current exactly the reconstruction judgments whose basis named it |
| E external or foreign-agent branch | intake of a change with unknown basis (§18) | provenance recorded; obligations from touched units |
| F drift or corruption | intake; derived state rebuilt; ledger integrity and qualification checked | §23 |

**Shadow genesis.** A shadow deployment (G2-G3) runs genesis with every subject in mode `LEGACY(p)` or `UNGOVERNED`, so SSDS derives, renders and records but holds no authority over any subject. Moving any subject to `NATIVE` is a cutover under G4.

### 20. External units and the cross-repository boundary

#### 20.1 External units and pins [D3 decision: pin grammar]

SSDS governs one ledger per project and provides no atomic admission across repositories. Cross-repository projects couple through immutable pins. An `EXTERNAL` unit's scope is one pin:

```text
{ git = "<repository identity>", commit = "<full hash>", path = "<region>" }
{ package = "<ecosystem>:<name>", version = "<exact>", digest = "sha256:…" }
{ dataset = "sha256:…", locator = "<url or DOI>" }
{ doi = "<DOI>", variant = "<edition/version>", locator = "<section/table/page>" }
```

Its content never changes, so `content` entries on it never go stale. A change of pin is an ordinary local content change whose impact is derived locally. A read of a file absent from the realization's tree, other than a file of an environment component the runner class records as an attribute, is an external read: pinned by the same grammar where possible, otherwise unpinnable; a class that cannot observe such reads makes every execution unpinnable (§6.3, §17.5).

#### 20.2 External acceptance and consultation

An `EXTERNAL_ACCEPTANCE` imports the fact that the external project's own process accepted that exact revision and scope, citing its evidence; its basis names, in `record` mode, the `EXTERNAL_CONSULTATION` it relied on. Without one, native reliance on the external unit is provisional. External status is only as fresh as the latest consultation; re-consultation is an advisory Dispatcher obligation, and briefs show the consulted position.

**Supersession by consultation.** When a later consultation observes that the pinned triple is no longer accepted by its owner, or finds the external ledger `FORK`, `ROLLBACK` or retired, Admission admits it with **mandatory supersession** of the earlier consultation, so every import relying on that consultation becomes non-current mechanically. A merely unreachable (`UNQUALIFIED`) external ledger supersedes nothing, which keeps network loss from flapping imports. A qualified actor may additionally challenge the importing subject. An external correction or retraction of a cited source is a binding event under the semantic-definition owner.

#### 20.3 Another SSDS ledger

Another project's SSDS ledger may be consulted read-only. The consultation qualifies that ledger's head under its own witness model (§23); an unqualified or retired head is never imported. The observation records the qualified head consulted, the checkpoints used and the derived status read. The external ledger is never written, merged or treated as local authority.

#### 20.4 Multi-repository change

A multi-repository change is a sequence of admissions: the producer first, then the consumer pinning the producer's admitted commit. Intermediate states are visible and legitimate: the consumer stays on its older pin until its own admission. A newer external revision observed by the Dispatcher creates an advisory obligation, never a block. **Supported class:** coupling through immutable pins (submodules, lock files, package versions, dataset hashes, DOIs). Scopes that must co-evolve atomically belong in one repository and one ledger; otherwise their transient inconsistency is visible as provisional or advisory state, never hidden.

## Part VIII. Persistence, publication, trust and security

### 21. Ledger storage realization

#### 21.1 Stores

| Store | Content | Canonical? | Location | Sole writer | Recovery |
|---|---|---|---|---|---|
| content store | all repository content including authored relations, the manifest, anchors and the policy file (the observed state) | yes, for meaning; structural declarations and policy are proposals until admitted | the project's Git repository | humans and tools through Git; Admission only by publication compare-and-swap | Git replication; foreign movement absorbed; referenced commits kept reachable by the ledger |
| ledger | entries (§21.2) under the closed schema | yes, for everything not derivable | one authoritative ref (§21.5) | Admission | any replica extending the highest observed checkpoint; else human-gated `LEDGER_LOSS` |
| witness checkpoints | authenticated checkpoints and retirement statements; digests only | no; evidence that admits entries and detects rollback | declared witnesses outside the authoritative replica's administrative control | Admission; any participant may relay an existing authenticated checkpoint | redundancy by quorum; loss beyond the fault bound by human-gated redesignation |
| derived index | derived state, effective structure, derivation checkpoints, analyzer caches | no | private, local, rebuildable | Derivation | discard and re-derive |
| operator state | leases, reservations, account and quota telemetry, harness sessions, raw prompts and transcripts, signing keys and secret references, high-water marks, the operator journal | no project authority | private user-local root outside repositories (owner-only permissions) | Dispatcher (journal); each participant's Ledger Store (its high-water mark); Admission (its keys) | journal rebuilt by observing harnesses and workspaces; high-water mark by qualification; keys by trust-root lifecycle |
| transport | task and result envelopes, rendered briefs and candidate commits on run refs | no | `refs/heads/ssds/run/<task-id>` in the project repository | Dispatcher and Interface (envelopes, briefs); agents (results, candidates) | regenerated from the ledger and obligations; results enter only through Admission |

There is no publication-attempt log (§22.3, refinement R4).

#### 21.2 Entry format [D3 decision]

Each ledger entry is one Git commit on the authoritative ledger ref. Its tree contains exactly:

```text
entry.json             RFC 8785 canonical JSON of the entry
entry.sig              Ed25519 signature by the appending Admission host key over
                       "ssds.entry.v1" ‖ sha256(entry.json)
objects/<sha256>.json  LEDGER-store objects this entry introduces (evaluated outcomes, refused record bytes)
```

```text
entry = { ledger_id, position, schema,
          prev: sha256 of the previous entry's (entry.json ‖ entry.sig)      -- null for genesis
          entry_kind: ADMISSION | ABSORPTION | LIFECYCLE,
          host_key_id, incarnation_id,                                       -- the publisher (§22.3)
          obs: commit | null,                                                -- null only for recovery lifecycle entries
          admission: { request_id, decision, reasons, base_commit, admitted_commit,
                       adopted_deltas, refused: [ {record_id, reasons, object} ] } | null,
          absorption: { fence: {base, fence_commit} | null } | null,
          lifecycle: <lifecycle record> | null,
          records: [ … ] }
entry_digest(n) = sha256(entry.json ‖ entry.sig)
```

The authenticated chain is the SHA-256 `prev` chain plus signatures; Git's commit chain is transport and must agree with it (a mismatch is corruption, §5.7). Commit metadata is fixed (author and committer `ssds-admission`, message `ssds ledger <ledger_id> #<position>`) and is never read.

**Reachability.** An entry commit's first parent is the previous entry commit; its further parents are every commit the entry newly references that is not already reachable from earlier entry commits: base, admitted, observed and candidate commits, fence commits, and the trees realizations ran on. So the ledger keeps every content commit it references reachable, and product-ref force-pushes or deletions cannot make history underivable. In a dedicated ledger repository those objects are pushed with the entry.

#### 21.3 Append and durability [D3 decision]

The append is a compare-and-swap of the single ledger ref from the expected previous entry commit to the new one:

- **local authoritative repository**: a Git reference transaction with an expected old value, with object and reference fsync enabled (`core.fsync` including `objects` and `reference`, `core.fsyncMethod = fsync`), sufficient for the declared crash model: process crash and operating-system crash or power loss of the authoritative host;
- **remote authoritative replica**: a push of the single ledger ref with an explicit expected old value (`--force-with-lease=<ref>:<expected>`), which the server rejects if the ref moved. No multi-ref capability is needed. The server's own durability is assumed; loss of the server is covered by the witness quorum (§23).

A losing writer re-validates against the new head (§9.1).

#### 21.4 Retention of referenced objects and evaluated content

The ledger retains every entry, every `LEDGER`-store object, and reachability of every referenced commit for its lifetime. Evaluated outcomes and the trees on which failing and reproducing executions ran are therefore always available to derivation (§6). Native artifacts referenced by `REPO`, `HOME` or `RUNNER` references are not retained by the ledger; their unavailability is a binding-health event (§17.4). Nothing referenced is purged except under the confidentiality protocol (§24.2), which weighs later scientific judgment before any irreversible purge.

#### 21.5 Location options [D3 decision]

Genesis chooses one: (i) the reserved ref `refs/ssds/ledger/<ledger_id>` in the project repository; or (ii) a dedicated ledger repository (for example private, when governance records must be more private than the product), on the ref `refs/ssds/ledger/<ledger_id>`. Semantics are identical. Genesis names the **authoritative replica** (repository URL and ref); a change is a human-gated `REPLICA_REDESIGNATION`.

#### 21.6 Derived index and operator-state boundary

The derived index holds only derived state, keyed caches and derivation checkpoints (§5.9); it is never authority and is discarded and rebuilt on any doubt. Operator state never enters the ledger, the content store or transport, except as record provenance fields (route, harness, model family and model, attempt, toolchain). **[delegated]** Index and journal storage engines.

### 22. Publication

#### 22.1 The integration observation and the entry-shape rule

Every entry carries `obs`, the live integration head Admission read immediately before appending it (for an admission, `obs = B`). The exception is a human-gated recovery lifecycle entry (`LEDGER_LOSS`, `FORK_RESOLUTION`, `WITNESS_SET_REDESIGNATION`, `REPLICA_REDESIGNATION`, `LINEAGE_RETIREMENT`), which carries `obs = null`, so recovery never waits for the integration host. **Entry-shape rule**: an entry whose `obs` differs from its expected head `E` must be an absorption carrying no submitted records. An **equivalent publication** of admission `n` is a commit reachable from `obs` (or equal to it) that descends from `B_n` and has `C_n`'s tree.

#### 22.2 Publication classification

An admission entry `n` names `C_n` and `B_n`; it is the complete admitted **intent** of the effect `B_n -> C_n` (C4). A records-only request has `C_n = B_n` and no effect. Publication starts only after `n` is admitted. Publication of `n` is reconciled by the first later entry carrying `obs`:

| `obs` of the first later entry | That entry may be | `pub(n)` |
|---|---|---|
| none yet | — | `PENDING` |
| `C_n`, or an equivalent publication equal to `obs` | any entry, including the next admission; `E` becomes `obs` (same tree) | `PUBLISHED` |
| anything else | only an absorption of `obs` | `PUBLISHED` if `C_n` or an equivalent publication is reachable from `obs`, else `OVERTAKEN` |

`late(n)` holds when `pub(n) = OVERTAKEN` and a later `obs` newly reaches `C_n` or an equivalent publication: a `LATE_PUBLICATION` integrity finding with `CRITICAL` attention. An `OVERTAKEN` admission keeps `C_n` recorded and reachable; its records are re-evaluated against the absorbed tree; its item obligation stays `OPEN` (unless the absorbed history already carries its outputs and the predicate holds, when a re-application is a duplicate discharge and is rejected), and its re-application is a new task, so a new enactment (§5.2, R12): every `NATIVE` D1/D2 subject the admission changed gets a new run, with its own revising review, acceptance and gate; its structural changes, already in `Σ` but absent from the absorbed tree, appear as quarantine until the revalidated request publishes and realigns.

#### 22.3 The publisher, fencing and settlement [refinement R4]

**Publisher.** Each Admission process generates a random 128-bit **incarnation identity** when it starts and records it in every entry it appends, with its host key. The publisher of admission `n` is the incarnation named in entry `n`. Only that incarnation, during its lifetime, performs `B_n -> C_n`, at most once, tracked in its own memory. A restarted process is a new incarnation; a different process or host is never the publisher. No durable attempt log exists: within one incarnation, "I have not attempted `n`" is exact, so no log intactness question arises (copied, restored, shared or inherited operator state cannot authorize a publication). Two processes holding the same host key are distinct incarnations and cannot both be `n`'s publisher.

**Fencing.** A fence commit `F_k` for admission `n`, created by entry `k`, has `tree(B_n)`, parent `B_n` and message `ssds fence <ledger_id> #<n> by #<k>`; it changes no content, and distinct fences have distinct identities. Any Admission incarnation that finds `L = B_n` with `pub(n) = PENDING` and is not `n`'s publisher in its first attempt appends, after the operational takeover wait, a **fencing absorption** `k`: an absorption of `B_n` (`obs_k = B_n`, classifying `n` as `OVERTAKEN`) carrying the effect `B_n -> F_k`, performed by `k`'s own publisher. Exactly one compare-and-swap from `B_n` can succeed: if the fence lands, `n`'s effect can never apply from this ref state; if `C_n` lands first, the next entry observes it.

**Takeover wait [D3 decision; proposed default].** 300 seconds after `n` is admitted with no successor, policy-configurable; a liveness choice only. A publisher that crashes inside the window is always fenced, which costs a human decision (below) and loses no record; the fence restores `tree(B_n)`, so every `NATIVE` D1/D2 subject `n` changed starts a new run at its earlier revision and needs a new revising review, acceptance and gate even if the fence is kept, and re-applying `n` is a new task (§8.3 step 7) that needs them again for `n`'s revision (R4, R12).

**Settlement.** Admission `n` is **settled** iff some later admitted entry's `obs` is not `B_n`. Human attention for an ambiguous `n` is raised when the first fencing absorption of `n` is admitted; a human decision on it is admissible only once `n` is settled (§8.3 step 7). Across a chain of fences the rule is the same: a later fencing absorption may classify an earlier fence `OVERTAKEN` while the ref still shows `B_n`; only an observation away from `B_n` proves that no outstanding effect from `B_n` can still apply. If a fence landed, the human chooses to re-apply `n` (an ordinary revalidated admission onto the fence) or keep the fence; no outstanding effect can reverse either. If `C_n` landed first, `n` was published late; the human chooses, with the product showing `C_n`, to accept it or revert by an ordinary admission.

**ABA policy.** A foreign reset of the integration ref to exactly `B_n` after a successful compare-and-swap is indistinguishable from a publication not yet applied. Every `L = B_n` that is not the publisher's first attempt is fenced, and the human decides after settlement. After a fence, a foreign writer returning the ref to exactly `B_n` while a stale publisher resumes is outside SSDS's control: detected as `LATE_PUBLICATION`, never prevented — a disclosed residual.

**Procedure** at an admitted head `n` with `pub(n) = PENDING` (Admission reads only the qualified ledger, the live ref and its own memory):

```text
read L
L = B_n and this incarnation is n's publisher and has not attempted n
                       -> compare-and-swap B_n -> C_n; mark attempted; read L again
L = B_n otherwise      -> after the takeover wait, append a fencing absorption of B_n with effect B_n -> F_k;
                          once admitted, its publisher performs it; read L again
L = C_n, or an equivalent publication equal to L
                       -> append the next entry with obs = L (the next ready admission, or an absorption
                          recording PUBLISHED)
anything else          -> append an absorption of L: PUBLISHED if C_n or an equivalent publication is
                          reachable from L, else OVERTAKEN
```

Recording an idle outcome is optional: a canonical `PENDING` with no successor is truthful, because the governed tree is already `T_n`.

**Every failure point.** Crash before the compare-and-swap: the publisher is gone; a takeover fences. Compare-and-swap loses to a foreign push: the successor is an absorption, `OVERTAKEN` unless the foreign history contains `C_n`. Compare-and-swap succeeds, then crash: restart reads `L`; `C_n` gives a consistent successor; later foreign movement gives an absorption classified by reachability. Successor appended but not admitted: it is the single provisional entry; restart completes its anchoring; if it vanished and is proved never admitted, read `L` again and append a new successor. Successor admitted, response lost: `submit` by request identity returns the recorded decision. Two hosts racing to reconcile: the ledger compare-and-swap admits one; the loser re-derives from the winner's `obs`. Publisher paused, takeover fences, human decides, publisher resumes: its compare-and-swap from `B_n` fails against `F_k`. Fence publisher paused: another incarnation fences again with a new fence commit.

**Idempotency and replay.** The effect identity `(ledger_id, n, B_n, C_n)` is fixed by entry `n`; a compare-and-swap from the exact predecessor is idempotent and never overwrites foreign work. Classification reads only `B_n`, `C_n`, `obs` and the commits reachable from `obs`, which the ledger keeps reachable, never the live ref; replay explains from the ledger alone which entry resolved each publication. There is no hidden cycle: `n` admitted -> effect -> read `L` -> append `n+1` -> admit `n+1`, and nothing on that chain waits for `n+1`.

#### 22.4 Commit point: provisional and admitted entries

```text
append (CAS, durable)                              -> PROVISIONAL
checkpoint acknowledged by q_a witnesses           -> ADMITTED (current-qualified; the commit point)
then: submit response ADMITTED; integration-ref publication; dispatch from the new state;
      current-state answers at the new head; the next append
```

Admission keeps **at most one provisional entry**: it appends `n+1` only after `n` is admitted. The single exception is a human-gated `WITNESS_SET_REDESIGNATION`, which may be appended over a provisional entry and whose admission settles that prefix. The head Admission validates against is therefore always admitted, and no provisional entry influences derivation anyone relies on. After a crash, request identity tells Admission what happened: no entry carries it -> retry; a provisional entry carries it -> complete checkpoint distribution (nothing else could append in between, so validation still holds); an admitted entry carries it -> proceed to publication. A provisional entry whose every copy is lost is resubmitted by identity when qualification proves it never admitted (§23.6); otherwise its loss is a `LEDGER_LOSS`.

If the authoritative replica, the integration host or a witness read quorum is unreachable, appends stop (fail closed) while production continues; recovery lifecycle entries need only the replica and witnesses. Each admission costs one entry and one quorum round in ordinary operation, because the next admission carries its predecessor's outcome.

### 23. Currentness qualification, witnesses and known loss

#### 23.1 Contract (P4)

Currentness is asserted only for durably witnessed state. A head is **current-qualified** only when a witness quorum holds its exact identity and it extends every checkpoint and high-water mark the evaluator observes. Every current-state assertion names its qualified head. The guarantee holds without exception under the declared witness model; there is no lag window.

#### 23.2 Authentication [D3 decision]

Every entry is signed (§21.2) by an Admission host key registered as a trust root in genesis or a `KEY_LIFECYCLE` record; keys are Ed25519, held only in private operator state, non-exportable where the platform provides it. Derivation rejects any chain containing an entry with a missing or invalid signature, a key not in force at that position, or a `prev` mismatch: this detects direct pushes of crafted entries. Entries are signed in every deployment class, including single-user local trust.

#### 23.3 Witness model, kinds and formats [D3 decision]

Genesis declares `N` witnesses outside the authoritative replica's administrative control, an admission quorum `q_a`, a read quorum `r` and a fault bound `f`, with

```text
q_a + r > N + f        (any admission quorum and any read quorum share more than f witnesses)
```

A faulty witness may be lost, rolled back or adversarial. Genesis and every redesignation reject parameters violating the inequality.

| Deployment class | `(N, q_a, r, f)` | Premise stated in status views |
|---|---|---|
| `LOCAL_TRUST` | `(1, 1, 1, 0)` | the single witness is on another medium under the same user and is not rolled back together with the replica |
| `TEAM` | `(3, 2, 2, 0)` | witnesses under three administrative controls |
| `HARDENED` | `(4, 3, 3, 1)` | one witness may be faulty |

Witness kinds: **Git witness**, a repository on a host under separate administrative control, holding checkpoints as files on an append-only ref (`refs/ssds/witness/<ledger_id>`) with force-push and deletion disabled by the host; **file witness**, an append-only directory on another medium (local-trust only); **log service**, an append-only transparency log. Acknowledgment means the witness durably retained the checkpoint: for a Git witness, the successful push of a commit adding it; for a file witness, the fsynced write; for a log service, its signed inclusion receipt. **[delegated]** Additional witness kinds that meet the same append-only and acknowledgment contract.

```text
checkpoint  = { ledger_id, position, entry_digest, entry_commit, host_key_id, signature }   -- Admission-signed
retirement  = { ledger_id, kind: RETIREMENT, last_position, last_entry_digest,
                successor_ledger_id, successor_genesis_digest, signatures }               -- human-gated (§24.2)
```

Witnesses retain every checkpoint they receive, append-only per ledger id. Any participant may relay an authenticated checkpoint it has seen to further witnesses (**read repair**); relaying can complete a quorum but cannot forge one.

#### 23.4 Qualification procedure and states

Every participant that presents current state (Admission, Dispatcher, Interface hosts, clones) keeps a **high-water mark**: the last head it qualified, in private operator state. An evaluator with authoritative-replica head `A` and high-water mark `W` collects checkpoint sets from at least `r` witnesses (after read repair where possible), then classifies:

- `FORK` — two observed checkpoints, or `A` and an observed checkpoint, lie on conflicting chains with no authenticated human-gated resolution in `A`'s chain naming the abandoned side;
- `ROLLBACK` — `A` is a strict ancestor of an observed checkpoint or of `W`, with no admitted abandonment record in `A`'s chain naming it; for a non-authoritative copy that can fetch the missing suffix, `BEHIND`: fetch, then re-qualify;
- otherwise the **qualified head** `H*` is the highest entry of `A`'s chain observed held by `q_a` witnesses that extends every observed checkpoint and `W`; `A` is `H*` or `H*`'s single provisional successor, labeled `PROVISIONAL` and never presented as current;
- `UNQUALIFIED` — fewer than `r` witnesses respond, or no head is confirmable at `q_a`: historical views only, no current assertion, Admission does not append;
- `RETIRED` — the witnesses hold a retirement statement for the ledger id: historical views only, from any mirror (§24.2);
- `INTEGRITY_HALT` — §5.7.

A chain carrying more than one entry beyond `H*` cannot come from a conforming Admission, except a human-gated `WITNESS_SET_REDESIGNATION` appended over a provisional entry (§22.4). Qualification, not derivation, checks this (provisional versus admitted is witness state): such a chain makes no assertion beyond `H*` and raises an integrity obligation with `CRITICAL` attention.

Every current-state answer, task brief, dispatch readiness decision, snapshot export, external consultation and publication is bound to a named `H*`. Admission's own validation uses the head it holds by compare-and-swap, admitted by construction. Nothing irreversible depends on a non-Admission participant's notion of currency: results are revalidated at Admission (K4).

**Why the contract is sound.** An admitted head is held by `q_a` witnesses; any `r` responses include more than `f` of them, so at least one honest holder; every qualifying evaluator therefore observes every admitted head, and an older prefix cannot qualify. An entry that never reached `q_a` was never relied on. If every copy and checkpoint of such an entry disappears, nothing distinguishes it from never having been appended, and no architecture can infer it; SSDS needs no such inference because it never granted that entry currentness, and its request is resubmitted by identity.

#### 23.5 Fresh-clone procedure

A fresh clone, with or without a historical prefix, has no high-water mark: it qualifies against a read quorum; fetches a missing admitted suffix (`BEHIND`) or reports `ROLLBACK`; with no read quorum its views are `UNQUALIFIED` and Admission refuses to append from it. It then sets its high-water mark to `H*`.

#### 23.6 Known loss of admitted history (P5)

**Abandonment versus loss.** A human-gated record may abandon a head not in the retained chain; whether that abandons admitted history is decided from witness reports, never asserted. Let `h` be the number of responding witnesses holding the abandoned checkpoint and `m` the number not responding; up to `f` responders may deny a checkpoint they hold. The entry is **proved never admitted** iff `h + m + f < q_a`; **known admitted** iff `h ≥ q_a`; otherwise **possibly admitted**. Abandoning only proved-never-admitted entries is a `FORK_RESOLUTION` with no boundary. Abandoning a known or possibly admitted head is a `LEDGER_LOSS`, whichever lifecycle record carries it. When the bound is inconclusive because witnesses are unreachable, waiting is always an alternative to a boundary.

**`LEDGER_LOSS` names** the retained head `R` (position and digest of the highest entry of the retained authenticated chain from genesis); every abandoned head known from witnesses, replicas or high-water marks, with position, digest and witnessed admission status (the lost interval is at least `(R, h_max]`); the content reference of the qualification report gathering those reports; the **global control facts** re-established from its position — witness model and set, trust roots, ruleset (each may equal its retained value; the gate re-establishes them because the lost interval may have changed any, and their effect is project-wide); and the human gate's decision. It is appended at `R + 1`, carries `obs = null`, and is admitted under the quorum it re-establishes (and the old one where reachable). Once admitted, qualification classifies the named heads as abandoned. A lineage whose old witnesses hold a retirement statement cannot take a `LEDGER_LOSS`; recovery continues in the successor lineage.

**The boundary** is the S1 predicate `cont` (§5.3): a record admitted before it has no permissive effect after it unless held. Polarity decides (§5.4): acceptances, conformance, plan acceptances, completeness, equivalence, assessments, imports, reconstruction and intake judgments, realizations, consultations, task results and check executions are not current until requalified or held; relaxers lose force, so their challenges reopen, their blocks return, and a revocation lifted by a counter-challenge returns; ordinary challenges, counter-challenges, restrictive adjudications, revocations and supersessions are unchanged; reports and their obligations are unchanged; failing assessments and their disagreements are unchanged, while their dispositions are withheld as dispositions; coordination decisions, reclassifications and human decisions that resolved a report are not in force, so the report's obligation reopens; `Σ`, tenure, quarantine, trees and content are unchanged; availability degradations and adverse consultations are unchanged; derivation at earlier positions is unchanged.

**Requalification** uses existing kinds only: a fresh acceptance, review, gate decision, adjudication, assessment, realization, import or consultation after the boundary, whose basis may cite withheld records by `identity`. S3 derives one `REQUALIFY` obligation per permissive record or relaxer in effect at `R` and withheld now, so recovery work is enumerated, and readiness orders it top-down.

**Why a stale-consistent restore cannot resurrect authority.** While any read quorum shows a later checkpoint, qualification refuses the stale ledger (`ROLLBACK`). Continuing needs an admitted `LEDGER_LOSS`, a ledger fact independent of product content; the boundary reads only ledger records, so agreement between a restored tree and the retained ledger is irrelevant: `Q` may be empty and nothing revives. At every position at or after the boundary, `current(x) ≤ base(x) ≤ cont(x)` for every earlier record, and every earlier relaxer is in force only if `cont` holds.

#### 23.7 Continuity attestation [D3 decision: grammar]

The only narrowing is accountable. A `CONTINUITY_ATTESTATION` is a human-gated challenge-tier judgment by an actor policy designates for the purpose:

```text
{ target: <LEDGER_LOSS record id>,
  scope: { form: COMPLEMENT, possibly_affected: [subject ids, record ids] }
       | { form: EXPLICIT,   held: [subject ids, record ids] },
  evidence: [ content references: hosting audit logs, notifications, CI artifacts, operator journals,
              a surfaced abandoned chain ] }
holds(a, x) ⇔ (form = EXPLICIT ∧ exposed(x, held)) ∨ (form = COMPLEMENT ∧ ¬exposed(x, possibly_affected))
```

`exposed` is the S0 predicate of §5.2. While in force it holds what it covers, and dependents follow through S2. Any qualified actor may challenge it; an upheld challenge withdraws it permanently; a later boundary withholds it like any relaxer unless that boundary's attestation holds it. It is the only way a pre-boundary record becomes current again without a fresh record, and it is an accountable act, never an inference from agreement between product and ledger.

#### 23.8 Recovery

| Situation | Recognized by | Response | Boundary |
|---|---|---|---|
| ledger ref rewound, suffix recoverable | `ROLLBACK`/`BEHIND`; some replica or clone holds the suffix | restore it; Admission halted until then | none |
| stale product restore, ledger intact | the next entry's `obs` differs from `E` | absorption, drift, quarantine | none |
| ledger truncated, newer product observable | `ROLLBACK`; suffix unrecoverable | `LEDGER_LOSS`; the next entry also absorbs the newer product | yes |
| ledger and product restored to one stale snapshot | `ROLLBACK` from a witnessed later checkpoint; `Q` empty | `LEDGER_LOSS` | yes; the boundary alone protects |
| only proved-never-admitted entries lost | non-admission bound holds | `FORK_RESOLUTION`; request resubmitted by identity | none |
| fork, or witnesses on conflicting chains | `FORK` | human-gated `FORK_RESOLUTION` choosing one lineage and naming the abandoned head; key rotation if compromise is suspected; never auto-merged | if the abandoned side holds admitted entries |
| crash after append, before admission | provisional entry | complete anchoring (idempotent) | none |
| witnesses below read quorum | `UNQUALIFIED` | historical views only; Admission halted; production continues; read repair when witnesses return | none |
| witnesses lost beyond the fault bound, ledger intact | `UNQUALIFIED` | human-gated `WITNESS_SET_REDESIGNATION` continuing from the intact head when every reachable checkpoint, replica and high-water mark ends there; the record states that continuity rests on that evidence (an assumption beyond the fault model); any evidence of a later head not proved never admitted makes it a `LEDGER_LOSS` | conditional |
| ledger objects lost, witness checkpoints intact | `ROLLBACK` | `LEDGER_LOSS` naming retained and abandoned heads | yes |
| authoritative replica lost | unreachable or empty | restore from a replica extending the highest observed checkpoint; `REPLICA_REDESIGNATION`; if none extends it, `LEDGER_LOSS` | conditional |
| abandoned entries later surface | an authenticated chain conflicting with an admitted abandonment | never merged; evidence with an integrity obligation; may ground a challenge to an attestation | the boundary stays |
| lost local store, intact repository | absent operator state | ledger is in Git; journal rebuilt from harnesses and workspaces; stale leases released; high-water mark re-established by qualification | none |
| corrupted derived state | integrity checks; mismatch with re-derivation | discard and re-derive | none |
| content objects referenced by the ledger unavailable | object lookup | `UNAVAILABLE` binding health; fail closed for dependent closure; restore from any replica | none |

**Witness lifecycle.** The witness set and quorums change only through a human-gated `WITNESS_SET_REDESIGNATION`, admitted under both old and new quorums where the old is reachable. Where it is not, the gate gathers every reachable checkpoint, replica head and high-water mark and names the head the new set continues from; any evidence of a later head not proved never admitted makes the record carry a `LEDGER_LOSS`. Witness admission latency on the Admission critical path is a reopen trigger (§32), not a reason to restore a lag window.

**Where information runs out.** If every copy, checkpoint and high-water mark of an admitted head is lost (more than `f` witnesses failing with every replica) and the product is restored stale as well, nothing distinguishes that world from one where the head never existed. A continuity attestation can be wrong: it is accountable and challengeable, not infallible. A holder of recovery authority who abandons a recoverable suffix can withhold admitted history from continuity until the abandoned chain surfaces; it is then evidence, never silently merged.

### 24. Confidentiality

#### 24.1 Prevention [D3 decision]

1. **Closed, reference-oriented schema** (§3.2): no free text; reasons are codes; rationale and reports are referenced by content identity and live under ordinary repository hygiene or in a private store.
2. **Bounded Admission checks** over every string-valued record field and every `LEDGER`-store object: grammar validation; known-credential patterns (a system list of provider token formats, private-key headers and connection-string forms, which policy may extend and never shrink); high-entropy detection (**[proposed default]** Shannon entropy at least 4.5 bits per character over any token of at least 20 characters, outside fields whose grammar is a digest or identity). Where policy enables it, the same scan runs over the candidate diff (the `credential_values` boundary check). A hit rejects with `SECRET_DETECTED`. These are preventive help, not a confidentiality guarantee.
3. **Operator secrets** (signing keys, tokens, prompts, transcripts, account telemetry) live only in private operator state.
4. **Visibility separation**: a dedicated private ledger repository when governance records must be more private than the product (§21.5).

#### 24.2 Breach protocol

Applies when a sensitive value is found in a replicated ledger entry or in product content the ledger pins.

1. A human-gated security incident under the security owner; Admission halts for the affected ledger.
2. **Rotate or revoke** every exposed credential immediately; rotation does not wait for any purge.
3. **Inventory replicas**: authoritative replica, remotes, clones, mirrors, forks, CI and harness caches, hosting retention and backups. Checkpoints contain digests only.
4. **Weigh retention before loss.** Before any irreversible purge, the incident record states which realized records and evidence the purge would make irrecoverable, which later scientific judgments may need them, and the substitute retained (digests, the private mapping, a redacted re-encoding), under the storage and scientific-inspectability owners.
5. **Choose remediation by confidentiality need** (human decision):
   - *Rotation suffices*: keep history; append a `REDACTION_NOTICE`; no guarantee yields.
   - *Confidentiality required*: a replacement lineage. Settle the old head (admit or prove-never-admitted any provisional entry). Re-encode records with sensitive fields replaced; map commit identities if product history moves; hold any pseudonym mapping privately. Bind the new genesis to the old lineage's last admitted head digest by a `LINEAGE_MIGRATION` record, and qualify that the replacement derives the same state, effective structure included, up to the renaming. Publish an authenticated **retirement statement** to the old witnesses, held by `q_a` of them, so every read quorum observes it and treats the old lineage as `RETIRED`; retire participants' high-water marks for it. Purge the old ledger ref and objects on every controlled replica only with explicit operation-specific authorization (G5); declare old clones invalid for SSDS use; request host garbage collection and backup purge. If the value sits in protected `main` history, confidentiality requires a new repository with the old one archived or access-restricted, never an in-place rewrite. Publish the replacement only after it validates (FF-001).
6. **Disclose what yields** in the incident record: append-only continuity (the old lineage is abandoned or purged); reproducibility of the affected records (only digests and the private mapping survive); checkpoint continuity (the new lineage starts new checkpoints); confidentiality of copies outside controlled replicas (cannot be guaranteed). A new lineage never removes leaked data, and SSDS never claims it does.

### 25. Actors, authentication, protected surfaces and self-governance

#### 25.1 Actor identity [D3 decision]

| Actor class | Identity | Authentication |
|---|---|---|
| `HUMAN` | `human:<key fingerprint>` | a signature by a registered human key in the SSH signature format with namespace `ssds`, or, in `LOCAL_TRUST`, the declared single-user mechanism (operating-system account plus a local key) |
| `AGENT` | `agent:<task id>/<attempt>` | the signed task envelope plus, on harness routes, the per-task submission credential; provenance names harness, model family and model, route and toolchain |
| `MACHINERY` | `machinery:<component>@<host key id>` | the component's registered key (Dispatcher issue key for envelopes and Dispatcher-submitted observations; runner keys for designated runners) |
| `ADMISSION` | `admission:<host key id>` | the Admission host key |

Agents are never principals with authority: their records are proposals attributed to an execution identity and bound to an envelope. No guarantee beyond the implemented mechanism is claimed (T4).

#### 25.2 Trust roots and key lifecycle

Trust roots are declared in genesis and change only through human-gated lifecycle records: Admission host keys (per host; every entry names its host and incarnation), Dispatcher issue keys, designated runner keys, human keys and the human authentication mechanism (`TRUST_MECHANISM_CHANGE`). A `KEY_LIFECYCLE` record registers, rotates or retires a key. A retirement of an issue key lists every outstanding envelope (compiled from run refs and the Dispatcher's journal) so that never-lost records under them stay verifiable (§8.3 step 3). A key declared **compromised** names the position from which its signatures are untrusted: envelopes it signed from there are refused; entries it signed from there make the chain `FORK` or `INTEGRITY_HALT` until a human-gated resolution. A compromised issue key or harness adapter can forge bindings and lineage; that is outside the declared trust model, and its remedy is rotation through this lifecycle.

#### 25.3 Protected surfaces and self-governance [D3 decision]

Agents cannot modify: the ledger; the **rules registry** (system ruleset versions shipped with the SSDS system, never in a project repository); the **project policy** unit `ssds.policy`; schemas; trust roots; witness configuration; unit governance state; issued envelopes. The policy file (TOML, closed schema) holds: actor qualifications above the floors; required judgment kinds, actors and gates per domain; evidence obligations per claim kind; routing table additions and raised floors; role narrowing; enabled check templates and their thresholds; default budgets and time bounds; serialization surfaces and concern tags; runner-class designations; standing plan; product-scope owner; intake options; witness and deployment parameters are **not** policy (they are genesis and lifecycle facts).

Self-governance: a policy edit is ordinary content that enacts nothing; it takes effect only through a human-gated `RULESET_ADOPTION` validated under the previous ruleset (stratification check §5.1, vocabulary checks §2.3) and shown its derived impact (subjects becoming ill-formed, obligations reopening). Schema changes take effect only by `SCHEMA_MIGRATION`; trust roots and witnesses only by their lifecycle records; every one of these needs a human gate. Admission detects any touch of a protected surface in a candidate (`AUTH_PROTECTED`). Agents may propose structural declarations in the manifest as ordinary content; they take effect only through Admission.

#### 25.4 Untrusted input

Agent branches, result envelopes and records are untrusted until validated (T1). Malformed or adversarial records cannot inject actions; agent-reported test results are never admissible evidence. Unknown executable or binary content is classified statically and never executed or deserialized to classify it (T2). Paths are repository-contained, validated relative paths. Evidence, memory and external text are data (T3). Inspection and export views over realized records, and tension or disposition homes that non-owners can write, are data-exposure and trust boundaries: views give the strongest safe aggregate and state the limitation, and content written to such a home stays a claim by its native asserter. Input sizes are bounded at every boundary (record count per request, field lengths, object sizes, outcome object sizes) by system limits. **[delegated]** The limit values.

## Part IX. Components, evolution and versions

### 26. Components, deployment and the Architecture 1.6.0 supersession

#### 26.1 Components

| Component | Owns | Never does |
|---|---|---|
| **Content Model** | parsing the manifest, anchors and semantic declarations; resolving effective scopes against observed bytes; authored relation extraction; revisions and scope identities | store status; decide which structure is effective |
| **Analyzers** | derived relations, interface extraction, diff-to-unit mapping, completeness declarations (§14.5) | claim completeness they do not have |
| **Ledger Store** | ledger persistence, authentication and chain verification, currentness qualification (read quorum, read repair, high-water marks, `FORK`/`ROLLBACK`/`BEHIND`/`UNQUALIFIED`/`RETIRED`), the non-admission bound, replica restore | interpret records; present a provisional or unqualified head as current; decide what was lost |
| **Derivation Engine** | the four strata and every query over them, including S0 structure, quarantine, tenure, well-formedness, expected head and publication classification, S1 continuity, S2 support with the cycle clamp, and S3 obligations, conformance, routing, escalation and decision and amendment classes | write canonical state; choose which prefix is current; read the live integration ref |
| **Admission** | validation; the integration-head observation before every append and publication reconciliation; the only ledger appends; admission by witness quorum; canonical publication effects by the entry's publisher incarnation; fencing absorptions and fence commits; enforcement of task binding, role, write scope, lineage-based independence, version binding and conformance | judge semantics, including what a lost interval contained; perform agent work; publish or report before admission |
| **Dispatcher** | scheduling among obligations ready at the qualified head (route selection, resources, reservations, serialization surfaces); workspaces and worktree leases; harness adapters; execution effects, including designated-runner realizations and check executions; signed task envelopes; launches in fresh sessions with per-task credentials and launch attestations; suspension and resumption; mechanical iteration retry; integration requests; the operator journal; route recommendation from benchmark evidence | decide readiness, conformance or completion; choose a decision class; act as a second admission; move canonical refs; dispatch from a provisional head |
| **Interface** | logical operations, transports, version-bound rendering of task, review, decision and gate briefs and of the inspector view and digest, advisory `ask(verify)` | hold state of its own |

**Dependency direction.** `Content Model, Analyzers <- Derivation <- {Admission, Interface, Dispatcher}`. The Ledger Store is read by Derivation and written only by Admission; its qualification is consulted by Admission, Interface and Dispatcher before anything is presented as current; Derivation never consults witnesses. Admission and the Dispatcher never depend on each other's internals: the Dispatcher submits through the same request path as every actor, and Admission never schedules. Scheduling decisions never influence derived workflow state; their provenance travels in submitted records and is replayed as recorded fact.

#### 26.2 Executable architecture fitness [D3 decision; replaces 1.6.0 §18 for SSDS]

Static checks on the SSDS source distribution, run in repository acceptance:

```text
ssds.content, ssds.analyzers    import only Core public API/SPI and each other's public module
ssds.derivation                 imports content, analyzers, ledger (read API) only
ssds.ledger                     imports Core public API/SPI only; exposes read and qualification APIs and an
                                append API whose only importer is ssds.admission
ssds.admission                  imports derivation, ledger; never ssds.dispatcher or ssds.interface
ssds.dispatcher                 imports derivation, ledger (qualification only), interface rendering; never
                                ssds.admission internals, and never the ledger append API
ssds.interface                  imports derivation, ledger (qualification only); submits only through the
                                admission request API
Core (sdp_orchestrator.core)    imports nothing from ssds
```

Also enforced: no derivation module reads the clock, the network, environment variables or the live integration ref (an import allowlist); every SSDS file lives under `orchestrator/`; one extension registration; no private cross-module imports. Fitness checks are sensors of the dependency rule, not architecture truth.

#### 26.3 Deployment and composition [D3 decision]

- **One composition root.** SSDS is a Core extension, `sdp.ssds`, registered through Core's single entry-point group `sdp_orchestrator.extensions.v1`. The `sdp` CLI and Core composition root stay the only root per installation; SSDS adds the command group `sdp ssds` (`open`, `ask`, `read`, `report`, `submit`, `decide`, `status`, `inspect`, `admission serve`, `dispatcher serve`, `mcp serve`, `genesis`, `qualify`, `export`). Core never imports SSDS; Core's standalone acceptance never depends on it (1.6.0 invariant 12, PC-001).
- **Packaging.** Distribution `sdp-orchestrator-ssds`, depending on `sdp-orchestrator-core`, under `orchestrator/` (containment root unchanged), native namespace package `sdp_orchestrator.ssds` with subpackages per component. Public surfaces `sdp_orchestrator.ssds.api.v1` (logical operations and records) and `sdp_orchestrator.ssds.spi.v1` (harness adapter, runner, witness and analyzer provider contracts).
- **Processes.** Admission and the Dispatcher run as long-lived local processes started through `sdp ssds … serve`; Interface hosts (CLI, MCP) are short-lived or long-lived; Derivation is a library. Multiple Admission hosts may exist; correctness comes from the ledger compare-and-swap and witness quorum, not from leader election.
- **Configuration ownership.** Core's configuration owner (defaults -> config/profile -> environment allowlist -> explicit CLI/API) holds operator-local SSDS settings in a namespaced `[ssds]` section: repository and ledger locations, key references, harness routes, runner endpoints, witness endpoints. Secrets are references, never values. Project policy is not configuration: it is governed content adopted by the ledger (§25.3).

#### 26.4 Executed supersession of Architecture 1.6.0 for SSDS-governed scopes [D3 decision]

On acceptance of this Manual, `orchestrator/docs/architecture.md` (Architecture 1.6.0, frozen) is superseded **for SSDS-governed scopes only**. For version-bound older work, the implemented Level 0 Core keeps its accepted behavior unchanged: one composition root, version/profile-separated source resolution, frozen historical profiles, versioned JSON records, no cross-version substitution (PC-001). The frozen document is not edited. The Tracker, Adapter and Scheduler levels were never implemented, so no Level 1-3 data migrates; their functions are preserved below.

| # | 1.6.0 product invariant | Final disposition for SSDS scopes |
|---|---|---|
| 1 | progressive usefulness; Core alone complete | **Replaced**: staged usefulness (read-only derivation and interface useful without Admission); document-only operation is not complete for native scopes (§19). **Preserved** for version-bound work through Core prompt mode |
| 2 | `core <- tracker <- adapters <- scheduler` | **Retired** with the ladder; **replaced** by §26.1-§26.2 dependency direction |
| 3 | graceful degradation without silent policy bypass | **Replaced**: degradation is truthful non-closure plus read-only derivation, labeled `UNQUALIFIED` or historical; no-silent-bypass **preserved** |
| 4 | one CLI and one composition root; extensions via versioned SPIs | **Preserved and closed**: SSDS is a Core extension under the single `sdp` root (§26.3); no second root |
| 5 | versioned public boundaries | **Preserved**: `sdp_orchestrator.ssds.api.v1`, `…spi.v1` |
| 6 | no duplicated workflow authority | **Replaced**: ledger plus Admission is the single workflow authority for native scopes; workplans and profiles keep transitions only for `LEGACY(p)` |
| 7 | manual operation is first-class | **Replaced in part**: manual invocation and the Git-envelope route stay first-class; manual results enter by admission; manual document control is not complete for native scopes |
| 8 | capability recommendation precedes resource scheduling | **Retired** as a module boundary (both in the Dispatcher); substance **preserved**: recommendation evidence never acts as quota or resource authority |
| 9 | benchmark observations preserve context | **Preserved and closed**: the Dispatcher's route-recommendation evidence keeps source, benchmark and version, model identity, effort, harness and configuration, value with uncertainty, generated and fetched time, freshness and identity-match quality (`EXACT_CONFIG_MATCH`, `MODEL_EFFORT_PROXY`, `MODEL_ONLY_PROXY`, `UNRESOLVED`), in operator state; never derived workflow state; incompatible metrics are never combined into one scalar |
| 10 | scheduler subordinate to workflow intent | **Preserved and strengthened**: the Dispatcher acts only on derived-ready obligations and cannot affect derived state |
| 11 | private state outside project repositories | **Replaced in part**: operator state private; the closed-schema ledger in a Git repository designated at genesis, which may be private |
| 12 | subset acceptance is permanent | **Preserved** for Core; **retired** as a ladder rule for SSDS components, which are accepted as one system (G3) |
| 13 | stable IDs cross modules; implementation objects do not | **Preserved** |
| 14 | read-only query and durable mutation visibly distinct | **Preserved**: `ask`/`read` and Derivation are pure; only Admission mutates canonical state |
| 15 | long-running execution is explicit | **Preserved and closed**: the harness-adapter SPI has `admit` (route admission), `start`, `events` (cursor-paged, normalized), `respond` (control and permission responses with stable request identity), `cancel` (idempotent) and `wait` (terminal result without destroying the run); one active execution per attempt; an ambiguous start reconciles before retry; process status and workflow semantics stay separate |
| 16 | manual and direct routes share one route vocabulary | **Preserved**: `ExecutionRoute` vocabulary (backend, account, transport, model, effort, delivery `direct`/`manual_handoff`, prompt context `local`/`web`, repository access, mutability) |
| 17 | capability identity independent of API version | **Preserved and closed**: SSDS capability keys `ssds.derive`, `ssds.query`, `ssds.admit`, `ssds.ledger`, `ssds.qualify`, `ssds.dispatch`, `ssds.render`, `ssds.transport.cli`, `ssds.transport.mcp`, `ssds.transport.git-envelope`, `ssds.harness.<family>`, `ssds.runner.<class>`, `ssds.witness.<kind>`, `ssds.analyzer.<language>` |
| 18 | explicit route choice is not an admission bypass | **Preserved** in the Dispatcher's resource admission (distinct from SSDS Admission) |
| 19 | route admission precedes final prompt rendering | **Preserved**: the route is selected before route-specific brief rendering (privacy differs by route) |
| 20 | run identity precedes scheduling and rendering | **Preserved**: task and attempt identity precede dispatch and travel in records |
| 21 | manual result tracking has a structured seam | **Replaced and strengthened** by the typed admission request |
| 22 | protocol version binding is explicit | **Preserved** (§16.9, B1) |
| 23 | one mutating run owns one local worktree | **Preserved** (K2; Dispatcher lease keyed by worktree identity) |
| 24 | workflow routing authority is profile-owned | **Replaced** by the rules registry for native scopes; profiles remain for version-bound rendering |
| 25 | uncertain routing remains uncertain | **Preserved**: ambiguity surfaces as explicit S3 states or fails closed |
| 26 | orchestrator code contained under `orchestrator/` | **Preserved and closed**: SSDS keeps `orchestrator/` as its containment root; no change |

| 1.6.0 frozen surface | Final disposition for SSDS scopes |
|---|---|
| §3 capability ladder and distributions | **Retired**; Level 0 Core **preserved** for version-bound work; SSDS is one additional distribution (§26.3) |
| §4 repository layout, Python packaging and namespace | **Preserved and closed**: native PEP 420 namespace, no root `__init__.py`; SSDS adds `sdp_orchestrator.ssds` with `api.v1`/`spi.v1` under `orchestrator/` (§26.3); cross-module imports only through public API/SPI |
| §5.1 API versus SPI | **Adopted** |
| §5.2 compatibility | **Adopted**: a public major is a semantic contract; persisted schema, ledger schema, ruleset, interface and profile versions are independent dimensions (§28) |
| §5.3 public records | **Adopted** with SSDS canonical JSON (RFC 8785) for records; timestamps UTC; IDs opaque; digests carry algorithm, scheme and value; unsupported required semantics fail; records never hold live objects |
| §5.4 pagination | **Adopted** for `ask` results, history and inspector listings |
| §5.5 problems/errors | **Adopted**: `Problem{code, message, retryable, details}`, codes namespaced `ssds.*`, Admission reason codes carried in `details`; callers never parse messages; redaction per owning boundary |
| §5.6 idempotency/mutation | **Adopted**: `ask`/`read`/render are read-only; `submit` idempotent by request identity; `decide` idempotent by the decision record's identity; Dispatcher start idempotent per attempt |
| §5.7 sync/async boundary | **Adopted**: `ask`, `read`, `report` and `decide` synchronous; `submit` returns `PROVISIONAL` and the outcome is observed by request identity; harness execution through handles |
| §5.8 two-stage API freeze | **Superseded**: the SSDS API v1 is frozen once, at the G3 implementation review, for the whole system |
| §6 Core composition SPI | **Preserved**; SSDS registers through it |
| §7 Core shared records | **Mapped**: `ProjectKey` -> genesis project identity; `WorktreeKey` reused for K2 leases; `RunId` retained for Core prompt mode only (SSDS uses task and attempt identity); `DigestRef` reused; `ProtocolProfileRef` reused for `LEGACY(p)` rendering; `WorkplanRef` not reused (plans are units); `CandidateRef` **declined** (transformation identity `(B, C, A)` replaces it, §7.1); `StageResultEnvelope` **declined** (the typed `TASK_RESULT` and admission request replace it); `EventEnvelope` remains Core's non-durable event; SSDS never derives state from events |
| §8 Core/Prompt module | **Preserved** for version-bound work |
| §9 Tracker | **Retired** as a module; functions **replaced**: history and projection by Ledger and Derivation (historical views, §5.8); status and next action by obligations and readiness; manual result ingestion by the Git-envelope result and `submit`; retention and export by the ledger and `sdp ssds export`; the storage/lease SPI by the Dispatcher's operator journal and worktree leases |
| §10 Adapters | **Retired** as a module; functions **replaced** by the Dispatcher: routes and identities, manual and direct delivery, pre-render route admission, worktree lease, execution lifecycle (invariant 15), benchmark sources, cache and identity resolver, static recommendation |
| §11 Scheduler | **Retired** as a module; functions **replaced** by the Dispatcher: account and resource ledgers and meters (operator state, never workflow), reservations, prediction, AUTO route selection, future-stage reserves, failover; a configured-required resource policy that is unavailable fails closed |
| §12 configuration ownership; secrets as references | **Preserved and closed** (§26.3) |
| §13 persistence/event ownership | **Replaced** by §21 stores; "persisted state is not repository authority" **retired** for native scopes, where the ledger is authority |
| §14 CLI capability behavior | **Preserved** for Core commands; **replaced** for SSDS by the `sdp ssds` command group (§26.3); Tracker/Adapter/Scheduler command sets retired with their modules |
| §15 failure/degradation | **Replaced** by §23.8 and §19.7 |
| §16 security/privacy | **Preserved** (§24-§25): untrusted pasted output, no tokens in prompts, caches, events, logs or repositories, no local paths or telemetry in web context, no transcript auto-injection, restrictive permissions |
| §17 benchmark integrity | **Preserved** for Dispatcher recommendation |
| §18 executable architecture fitness | **Replaced and closed** by §26.2 |
| §19-§20 module acceptance ladder; module-workplan derivation | **Retired**; replaced by gates G2-G4 and Manual-derived D4 workplans |
| §21 versioning/evolution | **Preserved** principle; SSDS versions per §28 |
| §22 active simplicity/reopen triggers | **Preserved** where applicable: separate mutable workflow authority, duplicated resolution, hidden preview writes, private objects in public API, process execution outside its owner |

### 27. Evolution

#### 27.1 Ruleset evolution

A ruleset adoption is a human-gated `RULESET_ADOPTION` naming a system ruleset version, a policy digest and an analyzer set, validated under the previous ruleset by the stratification check (§5.1) and vocabulary checks (§2.3), and shown its derived impact. Admissions are never re-adjudicated (P2): current derivation uses the adopted ruleset; a previously discharged obligation the new ruleset no longer considers discharged becomes open, never rewritten history; a relation reclassification that makes accepted structure illegal makes its subjects ill-formed until repaired; `Σ` and `Q` are unchanged; historical views reproduce with the ruleset in force at their position. A corrected check template enters the same way; a candidate wrongly blocked becomes integrable, and an integrated result the corrected template would flag gets an integrity obligation, never a silent revocation.

#### 27.2 Schema evolution

A ledger schema change is a human-gated `SCHEMA_MIGRATION` declaring, per kind and field, `READ` (the new reader reads old records as stated), `MIGRATE` (old records are re-encoded only in a replacement lineage, never in place) or `REJECT` (records of that shape are inadmissible from the position on). Old records are retained. The manifest grammar version (§1.2) and specification declaration grammar evolve the same way through the ruleset.

#### 27.3 System version evolution

Derivation semantics, normalizations (§1.5), the merge implementation (§7.2), check-template functions and the canonical encodings belong to the SSDS system version; the analyzer set belongs to the ruleset (§5.9). Both are therefore inputs named by the ledger, never by a host's installation. A system version change that alters any of them is adopted by `RULESET_ADOPTION` naming a ruleset of the new system version, so historical views keep the semantics of their position, and every recorded execution basis keeps being re-resolved under the system version it names (§6.3). A change of normalization or of revision hashing re-identifies revisions: every `content` entry and acceptance over affected units becomes non-current (each re-identified D1/D2 revision also needs its revision-assessment record before re-acceptance, §10.2), so the adoption gate is shown that re-acceptance burden, including D1/D2 human gates, and the discriminating readings whose coverage it ends (readings are compared by revision identity, §6.6), before it is adopted.

#### 27.4 Successor migration

The ledger is self-describing and versioned. An SSDS successor either reads it compatibly (declaring the schema versions it reads, §3.6) or starts a new lineage whose genesis carries a `LINEAGE_MIGRATION` record naming the SSDS 8 last admitted head digest; admissions are never reinterpreted, and the old lineage stays readable as history.

### 28. Versions

| Dimension | Identity | Changes by |
|---|---|---|
| SSDS system version | semantic version (`8.0.0`) | release of the SSDS system |
| Manual (architecture) version | `manual_version` of this document (`1.0.0`) | accepted D3 change through its acceptance process |
| ledger schema version | integer in every record and entry (`1`) | `SCHEMA_MIGRATION` |
| ruleset version | `{system ruleset id, policy digest, analyzer set}` | `RULESET_ADOPTION` |
| manifest and specification grammar versions | integers in the files | ruleset |
| interface version | `ssds.api.v1`, `ssds.spi.v1` | public-major change per §26.4 |
| doctrine version for native briefs | SSDP version and immutable public-source identity pinned by the ruleset | `RULESET_ADOPTION` |
| protocol and profile versions | SSDP protocol versions and Core profiles (`ssdp-protocol-7.2`, …), resolved from `PROTOCOL-RELEASE-STATE.yaml` | SSDP release process; never by SSDS |

No dimension is inferred from another, and none is conflated with SSDP protocol semantic version. Every supported orchestration profile through `ssdp-protocol-7.2` stays frozen and independently testable (PC-001).

## Part X. Assurance

### 29. Doctrine realization

#### 29.1 Levels

| Level | Realization | What it guarantees | What it cannot |
|---|---|---|---|
| **E0** | enforced mechanically; no agent action needed | the mechanical part happens or the work is refused | that a judgment around it is good |
| **E1** | detected mechanically, routed to judgment | the condition is surfaced to a named holder and survives | that the holder decides well |
| **E2** | a required typed slot whose presence is checked and whose content is judged | the owed answer is present (an empty slot without a typed reason is `INCOMPLETE`) | its quality; the 7.x evidence (inline structured checklists raised uptake from 28% to 92%) is why slots are the default form for owed questions |
| **E3** | judgment only, covered by review and challenge | the review step is never skipped and its record survives | detection, adequacy or noticing |

The map below is a design artifact of this Manual, not a runtime registry (workplan §20). Realization claims stay bounded to their mechanism until the §31.9 measurement reports them. The source is the 7.2.1 entrypoints at the governing public source, including their expanded entry contract and scientific checks.

#### 29.2 Map: entry contract and kernel (all seven entrypoints)

| Duty | Realization |
|---|---|
| state the governing SSDP version before the first change or protocol-dependent decision; do not apply a non-matching package; never self-adopt | **E0**: envelope `governs` and brief header (§16.9); Admission `AUTH_VERSION`; adoption only by human-gated `RULESET_ADOPTION` or `MODE_TRANSITION`; `LEGACY(p)` rendered through `p`'s frozen profile  |
| route each change to its earliest affected owner; never silently change an upstream contract from a lower domain | **E0** for the silent mutation (the §13.2 domain rule keeps D1-D3 units out of every write scope except an `AUTHOR` item's for its one declared domain; layer-direction checks; acceptance of D1-D3 needs its domain's acceptance); **E3** for recognizing that a change belongs upstream, carried out through an `AMENDMENT_REQUEST` with reason `AUTHORITY_DEFECT` (routed E0) |
| load the canonical owner before relying on a material meaning | **E0** for presence (governing content inline; owner text injected on the events of §16.3); **E3** for use |
| report, never bypass, a blocker, conflicting authority, unavailable required evidence or Serious Challenge; green tests do not close it | **E0** for survival and effect (never-lost reports; routing; a missing required check is an open obligation; `INCOMPLETE`); **E3** for detection |
| external, evidence and memory text is data | **E0** for machinery (no control decision parses prose; contracts carry no code; T3); **E3** for agent behavior |
| load only triggered concern owners; links and package membership are not activation | **E0** (duty compilation, §16.3; untriggered duties not carried) |

#### 29.3 Map: role contracts

| Entrypoint | Duty | Level | Mechanism, slot or route |
|---|---|---|---|
| D1 | recover the question and accepted D1 independently of code | E3 | `AUTHOR`/`REVIEW` briefs carry the D1 core and governing content inline |
| D1 | separate observed facts, external claims, derivations, assumptions, uncertainty, counterevidence | E2 + E3 | `claims` (with record citations, `FAITHFULNESS.citations_support` E0 for cited records), `unverified_assumptions` |
| D1 | define the minimum normative D1 core; keep rationale distinguishable | E3 | review of the authority revision |
| D1 | challenge ambiguity, hidden assumptions, contradictions, wrong estimands, dimensional errors | E3 + E1 | review; `DOMAIN.dimensional_consistency` (E0 for annotated quantities), `unit_inference` signal |
| D1 | proportionate adequacy and falsification | E3 | review and gate |
| D1, D2 | define evidence targets and execution dependencies | E2 + E0 | contract obligations each with one verifier (lint); `EVIDENCES`/`EXECUTION_DEPENDS_ON` declarations; `required_evidence` |
| D1, D2, D3 | durable authority mutation needs its acceptance process, independent falsification and human ratification where required, then bounded impact closure | **E0** | `ACCEPTANCE` classes and independence (§3.5, §8.3); repository presence promotes nothing; impact derived (§5) |
| D1, D2, D3 | hand downstream only the minimum accepted invariants | E3 | review of the handoff item |
| D2 | define algorithmic semantics independently of code; choose the minimum justified method | E3 | review |
| D2 | define oracles before optimization contaminates the reference; tolerances from accepted error semantics, never from a failing backend | E0 + E1 + E3 | `evidence_specs` outside the implementer's write scope and `TEST_INTEGRITY.evidence_specs_untouched` (E0); `widened_tolerance` signal (E1); `SPEC_REVIEW` (E3) |
| D2 | bound whether numerical uncertainty can change the decision before escalating | E3 | review |
| D2, D4 | distinguish evidentiary target from execution dependency; remap/rerun when machinery changes | **E0** | realization basis target/execution parts; execution change derives rerun obligations (§17.4) |
| D3 | classify the earliest affected domain and side constraints | E3 | review |
| D3 | reconstruct accepted D3 independently of implementation | E3 | review brief excludes author narrative (§16.5) |
| D3 | test D3 adequacy against D2 | E3 | review |
| D3 | compare admissible architectures; prefer minimum justified complexity | E3 | review; §30 |
| D3 | freeze only material decisions; delegate machinery | E3 | review |
| D3 | define D4 acceptance at real owner and consumer boundaries | E2 + E3 | contract verifiers; review of the contract in `PLAN_ACCEPTANCE` |
| D3, D4 | a first clean local defect stays local; recurrence triggers simplification before additive repair | E1 + E3 | recurrence detection creates a `COORDINATE` decision carrying the convergence duty (§15.7) |
| D4 | reconstruct the accepted contract; prefer the simplest admissible repair | E3 | brief |
| D4 | an equivalent local concretization is reconciliation; reopen upstream only when the abstraction must change; never change a D1/D2 meaning, default or tolerance for convenience | **E0** + E3 | write scope and protected evidence specifications enforce the edit boundary; the judgment is reviewed |
| D4 | close each stage with affected regression; reconcile every obligation; rerun evidence whose owner changed; real-boundary integration | **E0** | `required_evidence` on the exact candidate by a designated runner; integration reruns affected evidence; no collateral regression (§8.3 step 8) |
| D4 | a required check that did not execute is not a pass; green tests do not prove omitted obligations | **E0** | `INCOMPLETE`; open obligations; discharge requires every obligation |
| D4 | name each claim's real owner; test doubles never replace it | E3 | review; qualification design (§31) |
| D4 | never weaken tests, tolerances or specifications or discard contradictory evidence | **E0** + E1 | `no_deletions`, `no_skips`, `no_xfail`, `evidence_specs_untouched` (E0), required on every item whose write scope contains a `D4` or `EVIDENCE_SPEC` unit (§13.3); `fewer_assertions`, `widened_tolerance` (E1); failing evidence never dropped (§6) |
| all roles | Review/Challenge: reconstruct, attempt falsification, Serious Challenge before ordinary findings | E3 + E2 | review brief kind duties; `bidirectional` slot for scientific subjects on the reviewer's `TASK_RESULT`, whose emptiness refuses the review's passing judgments at admission (§8.3 step 7); Serious Challenge routing and human attention (E0) |
| all roles | completion report: governing parents, state, evidence applicability, blockers, Challenge first | E2 + E3 | `TASK_RESULT` outcome and slots; machine-produced facts (A6) |
| D1, D2 | important claims use independent evidence routes where they reduce common-mode risk; tests sharing an expected-value generator, fixture, dataset defect or reference are correlated | E3 | review; review judgments record common-mode dependencies (§16.5) |
| D3 | priority changes investigation effort, not the pass threshold; Stabilization asks whether the architecture would still be chosen | E3 | review; §30 |
| D4 | inspect obsolete, bypassed or duplicate ownership; reconcile documentation and dependency impact | E3 + E1 | review; derived impact sets (§5.8) |
| documentation | identify the intended reader; define new terminology and abbreviations before use | E3 | `DOCUMENT` briefs carry the documentation core |
| maintenance audit | conclude `HEALTHY`, `WATCH` or `ACTION REQUIRED` with per-finding scope and expected improvement | E2 + E3 | the `audit_conclusion` and `findings` slots of an `INVESTIGATE` item with `specialist = "MAINTENANCE_AUDIT"` (§13.5) |
| every entrypoint | every other duty of the entrypoint text | E3 | carried inline in the brief's domain core (§16.3); judged in review |

#### 29.4 Map: scientific checks

| Duty | Realization |
|---|---|
| when delegating, ask the findings, realized-results, variant and tension questions in the request itself | **E0** for SSDS-dispatched delegation (the delegate's contract requires the triggered slots, §13.5); **E2** (`delegate_returns`) for delegation outside SSDS |
| report each unanswered part as a gap, never a null | **E0** for emptiness (empty slot without typed reason -> `INCOMPLETE`); E3 for truthfulness |
| findings, including delegates' and out-of-scope ones; inspectability gaps | E2 (`findings`) + **E0** survival (delegate floor, §15.4, for `scientific = APPLIES` contracts) + E3 detection; an out-of-scope NO-PASS on an earlier integrated enactment is a named G2 reopen trigger (§32.3), not E0 |
| realized-results inquiry with null envelope and materiality basis | E2 (`null_envelope`) |
| variant-search disclosure | E2 (`variant_search`) |
| tension search before relying on accepted D1/D2 for a consequential judgment; report entries, bindings, asserters | E2 (`tension_search`) + E1 (`ask(tensions)` over in-repository `CHALLENGES` and recorded challenges) + E3 |
| consequential choices with origin, chooser and binding | E2 (`choices`) |
| retention, projection and omission statement | E2 (`retention`) |
| claims no stronger than evidence | **E0** for cited records (`citations_support`, `outcome_consistent`) + E1 (`prose_numbers`, `certainty_vocabulary`) + E3 |
| look for findings before discarding or irreversibly aggregating realized results or retained evidence | **E0** for the ledger (append-only; purge only through §24.2 with retention weighing); E3 for project data |
| probe within the declared resource budget | **E0** for Dispatcher-run executions (time bound, runner classes); E3 inside an agent's workspace |
| persist a finding or human decision in one authorized home with its required content | **E0** for records and human decisions (ledger); E2 + **E0** for homes (`homes` in the contract, enforced as write scope); E3 for content |
| persist a tension bound to every plausibly implicated authority and its subject, with asserter | E2 + E0 (`CHALLENGES` requires an inquiry attribute; schema) + E3 for breadth |
| inaccessible homes: named limit; qualify or block only on the stated conditions | E2 (`tension_search`) + E3 |
| product changes need accepted authority, instruction or contract; a marked surface beyond the deliverable binds only after stakeholder/task acceptance | **E0** for acceptance (`PRODUCT_SCOPE_ACCEPTANCE` is R3; technical review cannot accept it, §3.5); E3 for whether a code change is an unrequested product change |
| revising D1/D2: search tensions bound to accepted concretizations; record predecessor identity and revision-scoped assessments, asserter, proposed until accepted | E2 (`revision_assessments`) + **E0** for presence and order: in every frame, a passing acceptance or gate `ACCEPT` of a `NATIVE` D1/D2 revision is refused unless a revision-assessment record for exactly that revision counts (in the revision run, standing), however the revision was produced, and it is current only within that run, so a revert or any change of the revision needs a new record, acceptance and gate (§10.2, §8.3 step 7, §5.2); the revising review is derived wherever one is missing, and the gate core renders the record (§16.6); an agent can change what a D1-D3 unit itself owns only through an `AUTHOR` item (§1.2, §13.2). E3 for the assessments' quality |
| authority content (O1) when authoring or materially revising D1-D3; check it when reviewing | E2 (`o1_content`) + E3 |

#### 29.5 Map: specialists

| Entrypoint | Duty | Level | Mechanism |
|---|---|---|---|
| documentation | classify a disagreement before editing; route to its owner | E3 | `DOCUMENT` briefs carry the classification table |
| documentation | never self-approve semantic changes or promote observations into doctrine | **E0** | a `DOCUMENT` write scope and its effect-keyed write set contain no D1-D3 unit (§1.2, §13.2); an agent changes authority text only through `AUTHOR`, whose revision needs its domain's acceptance; every `NATIVE` D1/D2 revision, however produced, needs a counting revision-assessment record before acceptance and for validity (§10.2) |
| documentation | edit canonical sources and regenerate derivatives | **E0** | `generated_untouched` (HARD) |
| documentation | preserve evidence distinctions; truthful current documents | E3 | review |
| maintenance audit | sense risk; route each finding to its smallest owner; no redesign inside the audit | E2 + **E0** + E3 | `findings` and `audit_conclusion` slots; the investigator role cannot write product or authority units; review |
| maintenance audit | no PEM admission or authority by assertion | **E0** + E3 | an audit execution accepts no authority (R2 reviewer roles accept only the kinds policy assigns them, §12.3); PEM admission stays with its owner |
| repository hygiene | hard boundaries: never delete or force-move `main` or protected refs, never rewrite history, delete only with positive proof | E3 | ref operations are outside SSDS's governed content and G5 relies on Git host protection; SSDS itself never deletes refs and purges only through §24.2 |
| repository hygiene | classify, retain ambiguous, report | E2 + E3 | `findings` and `claims` slots; review |

#### 29.6 Disclosed E3 duties

These stay judgment only, and SSDS claims nothing more for them than that the review step runs and its record survives: **detection** (noticing anomalies, tensions, upstream defects; the 7.x study found detection did not respond to protocol text in any arm, and enforcement is not expected to change it); adequacy of authority, contracts, evidence and gate evidence; semantic equivalence and completeness; scientific and numerical interpretation; materiality; whether a Serious Challenge is warranted; the quality of discriminating readings (a lenient but formally consistent reader); the adequacy of a tension search; real-owner versus proxy judgments; whether a change belongs upstream; reliance on reads machinery cannot observe; behavior inside an agent's own workspace; hygiene operations on Git refs.

#### 29.7 Protocol 7 inputs: Manual decisions (§21 item 21)

| Input (workplan §19) | Decision | Section |
|---|---|---|
| gate-evidence template obligations (Channel C) | gate brief order, core contents, refusal of an unqualified accept with known missing evidence, adequacy field | §16.6 |
| tension search keys to unit identity | locator resolution, lineage, `CHALLENGES` binding | §1.11, §2.2, §16.2 |
| product-scope acceptance actor | `PRODUCT_SCOPE_ACCEPTANCE`, R3, policy-designated owner; D1/D2 gate naming the surface | §3.4-§3.5 |
| realized-record/observation overlap; inquiry status | §17.4; `CHALLENGE.inquiry`; `CHALLENGES.inquiry` | §17.4, §2.2 |
| inspection/export and writable homes as trust boundaries | strongest safe aggregate with the limitation stated; content written to such a home stays a claim by its native asserter | §25.4, §16.8 |
| mandatory activation and selection | obligation kind selects role; duty compilation tables | §12.3, §16.3 |
| event-triggered owner injection | injection event table | §16.3 |
| typed delegation request and return | the contract and the slot vocabulary | §13.1, §13.5 |
| mechanical write-scope and persistence-home enforcement | `write_scope`, `homes`, boundary checks; scope term syntax and analyzers | §13.1, §14.3, §1.3, §14.5 |
| in-loop version routing and self-adoption guard | `governs`, `AUTH_VERSION`, adoption only by lifecycle records | §16.9 |
| typed choice-provenance and claim records | control facts versus narrative; `choices`, `claims` | §16.4, §13.5 |
| exact package-access provenance | no consumed-package ledger beyond read recording and recorded brief identity | §16.4 |
| pre-cutover baseline | resolved from `PROTOCOL-RELEASE-STATE.yaml`, currently 7.2.1; public fallback and recovery distinct | §19.7 |

### 30. Minimum-justified-architecture reassessment (§21 item 22)

Against the accepted baseline (document-controlled SSDP 7.2.1 with the frozen Level 0 Core), each primitive, component and persistent surface is kept only if removing it drops a capability some governing invariant requires and no simpler equivalent exists.

| Element | Capability it alone carries | Simpler equivalent considered | Verdict |
|---|---|---|---|
| unit | locality of acceptance, context and staleness below file and above byte | files (too coarse for long authority documents), Git blobs (no semantic grouping) | keep |
| subject/part split | one acceptance per holistic meaning while reading and context stay local | per-leaf acceptance (needs false semantic claims at refinement) | keep |
| relation | declared authority, warrant, definition and evidence structure with cycle classes | prose links (no mechanical impact or cycle legality) | keep |
| record and one ledger | everything not derivable from content, append-only and replayable | status in documents (H3, rejected: anyone can push a PASS file) | keep |
| basis | per-record staleness, the single mechanism replacing epochs, plan binding, context staleness, evidence staleness and dirty tracking | global epochs (H0, rejected: global coupling) | keep |
| Content Model, Analyzers | revisions and derived relations | — | keep; distinct inputs |
| Derivation Engine | the only interpreter of records | logic in Admission (would duplicate interpretation for queries) | keep |
| Admission | the single serialization point (C1) | Git merge rules (not semantic) | keep |
| Dispatcher | execution effects, designated runners, envelopes, launch attestations | agents launching themselves (no lineage attestation, no runner custody) | keep |
| Interface | one transport-neutral contract over three transports | per-transport logic (would duplicate rendering) | keep |
| Ledger Store with qualification | currentness only for witnessed state (P4) | trusting the replica (cannot detect its own rollback) | keep |
| witness checkpoints | rollback and stale-restore detection | none: a replica cannot prove its own currentness; `LOCAL_TRUST` is the minimal instance | keep |
| derived index | bounded restart cost | re-derive from genesis every time (violates the recovery-time objective) | keep, as cache only |
| operator state | private keys, leases, transcripts, high-water marks | in-repository state (violates G4) | keep |
| transport run refs | zero-context web agents | — | keep; regenerable |
| publication-attempt log | (formerly: evidence of "no attempt" across restarts) | **in-memory per incarnation (R4)** | **removed** in this Manual |
| partition validity check over observed bytes | (formerly: detection of overlapping leaves) | **partition by construction (R5)** | **removed** as a dynamic check; static checks remain |
| frames, transformation identity | pre-integration review with defined currency | reviewing only after merge (loses K1 for review) | keep |
| roles, envelopes, contracts, conformance, reports, inspector | stakeholder-directed enforcement layer (SD-1-SD-6) | instruction text (the 7.x evidence: compliance with text is probabilistic) | keep |
| fences | revocation of a stale publisher's effect authority | ledger checks before CAS (a paused publisher outlives them) | keep |

No new primitive, component, persistent surface or record tier is added by this Manual; two mechanisms are removed (R4, R5). The §6 family is unchanged in its record kinds and components; its predicates changed as follows: R1 fixes how the reviewed execution basis is recorded (once, in the existing `REALIZATION` record, at the reviewed granularity, with its resolution context frozen), names which of two predicates each existing use reads, states one construction rule and one guard for them (the adverse predicate compares only tree-resident terms under the record's own resolution context; every other dimension, external inputs and the environment included, enters only the permissive one), and states that permissive conjunct over the class of every recorded execution attribute the specification leaves free (SD-17, which withdrew SD-15's restriction of mechanical staleness to fixed-environment specifications), and R2 makes an existing fail-closed promise explicit. R1's recorded context adds one operational duty, keeping every system version and analyzer set a recorded basis names (a reopen trigger, §32.3); hosts already keep historical system versions for historical views. SD-14 replaced the write-attribution rule by the existing `Δ(X)` and structure comparison. SD-16 and SD-19 add one admissibility condition keyed on the acceptance target (a revision-assessment record for exactly the accepted revision) and one obligation trigger that supplies it where missing (§10.2, §8.3 step 7); they add no record kind, since the record is an existing `TASK_RESULT` carrying the existing `revision_assessments` slot, and SD-19 removed the producing-admission classification and the `AUTHOR` exemption. SD-22 then replaced SD-20's predecessor comparison and SD-21's `holds` predicate by one S0 target condition, the revision run, which every consumer reads through `base`; the predecessor is a display. SD-24's qualified-gate cap (R11) reuses the existing `P` value and its provisional-continuation rules, realized as the minimum over every eligible unsuperseded passing decision (`gterm`). SD-25 replaced the prospective frame clauses by one S0 rule for which records act in a state, read by every permissive consumer, and identified a revision run by the event that starts it rather than its ledger position; this adds a run field to three existing record kinds and removes the per-consumer frame exceptions, and withdraws capabilities, listed as R12: a frame record of another pending enactment no longer supports a record in a candidate's frame (§7.3), a prospective acceptance no longer carries to a later iteration (SD-26), and the re-application of an overtaken or fenced admission is a new enactment; a cutover is carried by an integration instead of a separate admission (§19.5); `on⁺` lost its same-root-tree route, so unbounded executions serve no permissive use; `bound` excludes `UNBOUNDED` bases, `adm` treats them as admitted content, §6.9 schedules nothing for them, and conditions (2) and (4) read `link⁻`, one existential over admitted observations that only enlarges adverse matches. Content identity became exact: the line-ending normalization is removed, Git entry type and mode are hashed, anchor removal is limited to classified comment lines, and runners must materialize exactly that representation with no exception (a runner that cannot is not designated; LFS objects are external reads; submodule reads are read entries on the gitlink); partition rule 3 also covers equal regions. R9 adds one rule outside §6, the veto of passing judgments by a standing adverse judgment of the same kind on the same target, with the derived `answered` state and `REFUSED` discharge value, which extends the reviewed assessment rule to the other judgment kinds instead of adding a separate mechanism per kind, and makes reviewer and principal tasks end in the existing `TASK_RESULT` instead of leaving their slots without a carrier. Practical costs remain reopen triggers (§32.3), not grounds to claim burden reduction.

**Stabilization question.** Would this architecture still be deliberately chosen today for the same governing contract? Within the evidence available at Phase C, yes: each element carries a capability an invariant requires. The answer is design rationale, not evidence of adequacy; independent Review and the G3 measurements decide.

### 31. Qualification design

#### 31.1 Principles

Qualification binds every claim to the property its method can discriminate (DS-001). Synthetic fixtures and model cases establish mechanical properties only; semantic adequacy (promotion, equivalence, completeness, gate adequacy, reading quality) needs real-owner cases and independent Review. Persistence and recovery claims use deterministic failpoints with the production owner executing. Every negative discriminator below is a case a shallow or proxy implementation would pass and a correct one fails. **No executable SSDS evidence exists at G1.** Every runtime group below is **UNEXECUTED**; G1 needs only the document-level checks of §31.10. A missing required check is never a pass.

| Gate | Evidence it needs from this section |
|---|---|
| G1 | §31.10 document checks; independent D3 Review of this Manual; stakeholder acceptance |
| G2 | a shadow D3->D4 workplan that carries §31.2-§31.9 as its acceptance program, independently reviewed |
| G3 | §31.2-§31.9 executed against production owners, with independent implementation Review |
| G4 | per subject: §19.5 cutover conditions, demonstrated rollback (§19.7), human and project approval |

#### 31.2 Derivation, structure and relations

Real owner: the Derivation Engine and Content Model, consumed by Admission and the Interface.

- **One input, one state.** Property-based generation of admissible ledgers and trees; identical derived state across evaluation orders, incremental and from-scratch evaluation, repeated runs and hosts. Discriminators: an implementation memoizing without the full key diverges under an analyzer-version change; **analyzer pinning**: two derivation hosts with different installed analyzer versions over the same `L_n` give identical `D_n`, or the host lacking the pinned set refuses current assertions; a historical view at `m` is byte-identical before and after an analyzer `RULESET_ADOPTION`; an implementation deriving with the installed analyzer must fail.
- **Partition by construction (R5).** Generated manifests and trees, including foreign files under prefixes, vanished spans, malformed and crossed anchors, duplicate headings: every governed byte has exactly one owner or lies in the uncovered region; scope identity and revision unchanged by byte-preserving refinement; sibling-overlap declarations rejected statically. Discriminator: overlapping prefix siblings accepted, or a vanished span's bytes double-owned. **Equal regions:** sibling `symbol` and `anchor` parts on one Python file, initially disjoint; an absorbed edit moves the anchors exactly around the function: both resolve to `ABSENT` with an integrity finding, independent of declaration order; a member region equal to its composite's stays the member's. **Exact identity:** a one-byte binary change `0d` to `0a`, a CRLF-to-LF change, an executable-bit change, and a regular file replaced by a symbolic link with the same bytes each change `cid`, make dependent passing evidence non-current and derive its rerun; adding comment anchor lines to a Markdown or Python unit leaves `rev` unchanged. **Representation:** (A) an absorbed `.gitattributes` change to `eol` or `working-tree-encoding` with the read blob unchanged leaves the realization current only because the runner provably read blob bytes; a runner honoring the attributes cannot be designated, and no fallback admits its results as evidence; a submodule bump changes the gitlink read entry and makes the realization non-current; an LFS-tracked input is read as an external read pinned by its object identity; a mode change of an empty D2 file is in the write set; (B) an anchor-syntax line inside a Python string and inside a Markdown fenced block changes `cid`, while a genuine comment anchor does not; (C) an `IMPLEMENT` item changing only the mode of a D2 file is a `VIOLATION`, while one changing only bytes that a D4 symbol span owns, in a file that also holds a D2 span, is not, even when the edit changes the file's length above the D2 span; a part-scoped item whose edit shifts a following sibling or residual part, and a nested D2 edit inside a D3 whole-file composite, follow §1.2's composite sentence; a `kern.helper`-scoped item in the §31.3 granularity trajectory is not refused; an `IMPLEMENT` item that moves a D2 unit's anchors so that it owns different bytes is a `VIOLATION`; and in isolation, an edit to a D4-owned line between two unchanged D2 regions of one file leaves the D2 unit out of the write set while an edit to one byte the D2 unit owns puts it in, so region comparison by content is tested apart from offset shift; (D) a CRLF file and an LF file give the same anchor and heading resolution; (E) partition rule 3 in one pass: a composite partially overlapping a sibling is `ABSENT` while its member equal to a top-level anchor's region is `ABSENT` with it; (F) precedence: a top-level anchor unit whose anchors an edit moves inside a method of class composite `A`, without becoming its member, owns those bytes, which leave `A.~` and `A.~`'s execution-basis subtraction; a member that survives its composite becoming `ABSENT` keeps its bytes and the composite's other bytes become uncovered. Discriminator: an implementation that normalizes line endings, ignores entry type and mode, removes data lines that look like anchors, cascades rule 3, or computes a residual by subtracting members only, must fail. **Closure bounding:** (A) under a runner class that observes reads outside the tree but traces none inside it, with no `COMPLETENESS(EXEC)` judgment, a change to a tracked data file the execution read makes the passing realization non-current and derives `REALIZE`; (B) the corresponding failure is not made stale by a run that never read the failing content; (C) a specification that globs `data/*.csv`, with no judgment: adding `data/new.csv` makes the realization non-current, as does adding a probed absent file; (D) changing an ignored tracked file under the whole-tree fallback makes the realization non-current. Discriminator: an implementation that lets observed reads bound a closure, or computes the whole-tree fallback under `ignore`, must fail. **Unbounded bases serve no stop:** (A) a racing solver, no `COMPLETENESS(EXEC)`: `o1` fails on `T1`, `o2` reproduces it, an unrelated admitted doc edit gives `T2`, and `o3` passes there: `a⁻` is not stale (`o3` is unbounded and cannot serve (3)), the owner's adjudication obligation is derived, and for a D1/D2 claim the floor fires (`adm` holds for an unbounded basis); (B) a bounded failure whose bounding judgment becomes `P`, blocked, revoked or loss-withheld before a differing alternate-tree run is realized: that run cannot help a stop, and the failure cannot become stale while the judgment is lost; (C) a doc-only candidate's flaky D1/D2 failure keeps class R3 and reaches the floor. Discriminator: an implementation that lets an unbounded run serve (3) or the candidate-own test, or (1) on a non-identical tree, must fail. **Width-independent adverse matching:** a bounded failure `a⁻` under judgment `c_k`; `c_k` lapses (or is admitted only after a run, or an analyzer upgrade intervenes) and a differing run `d` is recorded unbounded on an alternate tree that differs from `tree(a⁻)` only outside `a⁻`'s recorded content; `c_k` is restored and a passing bounded run `e` on present content follows. Expected: `d` is in (2) through `link⁻` with `o' = real(a⁻)`, so `a⁻` is not stale and the owner's adjudication obligation is derived; likewise a yielding unbounded run keeps (4) false. Discriminator: an implementation that compares only the observation's own recorded basis in (2) or (4) must fail. **No stop without a narrow anchor:** an `UNBOUNDED` failure whose only reproductions are `UNBOUNDED` runs on its own tree (a second evidence obligation, a CI retry): no reproduction serves (1), so `a⁻` is never stale mechanically, and a differing run after an unrelated doc edit cannot be hidden by a later bounded pass. Discriminator: an implementation that accepts an unbounded reproduction in (1) must fail.
- **Manifest handling.** An unparsable manifest quarantines every key while governance continues on `Σ`; anchors never declare structure; inline semantic markers change revisions.
- **Illegal positive recursion.** The mutual-acceptance configuration of §5.6 rejected at Admission; a fixture-injected ledger evaluates to all-`F` with an integrity obligation.
- **Support-cycle clamp (R2).** Injected cycles through absorption-extensible `about` terms, through a completeness edge, and through corruption: every node of every non-trivial component is `F` before any presentation, never `P` or `T`; an ordinary finding or integrity obligation as classified. Discriminator: an implementation evaluating only the least fixed point from a permissive provisional start shows `P` on a cycle node.
- **Corrupt prefixes (R3).** Authenticated entries violating schema, shape, target tier or strictly-earlier targets: `INTEGRITY_HALT` at and after the entry; historical views before it unchanged; Admission appends only the human-gated resolution. An unreadable newer schema version yields historical views, not a halt.
- **Challenge recursion and counter-challenges.** The workplan §22 cases: chain uniqueness; challenged dismissal restores the block permanently once upheld; counter-challenges inert while open; revocation lifted only by an upheld counter-challenge; polarity table to depth four.
- **Relation-cycle legality.** Valid SDG recursion; same-subject `DERIVED_FROM` and `DEPENDS_ON` cycles; mixed cycles; unknown future types; undeclared simultaneity; nested and sibling groups; group boundaries; code recursion legal and inert; self-relations; legitimate intra-subject warrant with `content` entries; re-routed support edges; condensation carries no warrant; ruleset reclassification; vocabulary adoption rejections including `CHALLENGES`/`EVIDENCES` as validity prerequisites.
- **Structural intake and tenure.** The required counterexample of workplan §22 (accept, demote, accept composite, challenge, foreign re-declaration, adoption only with fresh prospective acceptance; risk-override and revocation variants) and its siblings: part-to-subject, subject-to-part, membership mutation, boundary mutation, kind and governed-boundary changes, reparenting under challenge, destination freeze, rewind and manual conflict resolution, ledger truncation with newer product, lawful demotion then restoration, ruleset evolution during quarantine, overtaken admission, deleted manifest.
- **Currency and widening.** Exactly the reliant records go non-current; re-review without content change backdates descendants that did not see upstream text; equivalence scoped by class (§4.4 covering rules, including `EXACT` never covered); falsified completeness invalidates its inferences; chain determinism; `UNBOUNDED` fallback; membership change invalidates completeness; widened bases never make parts valid.
- **Determinism and replay.** Independence from wall clock and live state (with the §26.2 import allowlist); checkpoint corruption detected; schema-evolution fixtures; admissions never re-adjudicated.

#### 31.3 Assessment disagreement

Real owners: Admission, Derivation, discharge (§10.4) and the inspector view, end to end, with nothing seeded resolved. The workplan §22 assessment-disagreement program is carried in full (no lapse under every content, structural, relocation, frame and rerun variant; admission salvage; independence; the cases that must remove qualification; standing; start; content and reading U1/U2/W1/W2; X1-X3; Y1-Y2 and N4; floor and class; the cases that must not qualify; `valid` and discharge agreeing on `ev`; ledger-order and evaluation-order invariance). This Manual adds:

- **Completeness polarity (R1).** A failing assessment `a⁻` with a recorded narrow execution basis bounded by a completeness judgment `c`. Variants of `c`: current `T`; `P` (an open overridden blocking challenge); blocked; revoked; superseded; withheld by a loss boundary. In each variant, two adverse runs exist: (i) a **differing old-content run** — an observation of `conf(a⁻)` whose recorded narrow basis matches `tree(a⁻)` with another outcome on `F(a⁻)`, made on an alternate tree that differs from `tree(a⁻)` only outside the recorded regions, including in another span of a recorded file; (ii) a **yielding present-content run** — an observation whose recorded narrow basis matches the frame with an outcome yielding the failure. Expected in every variant: the claim stays qualified (`undisputed = P`); losing `c` never raises support by removing either run, because (2) and (4) use `link⁻`, which rests on `on⁻` and never on completeness (§6.6). Contrast: with `c` lost, a narrow-basis reproduction and a non-yielding current observation no longer make the failure stale (`on⁺` then needs another current bounding judgment). Negative discriminators: (a) an implementation applying whole-tree fallback to both polarities raises `ev` from `P` to `T` when `c` is lost — must fail; (b) an implementation that "repairs" (a) by discarding the observation or by making the claim's unrelated exact passing assessment stale — must fail, since the expected value is reached with every observation retained and the passing assessment current.
- **Structure changes with an unchanged tree.** The trajectory: a narrow-basis failure of admitted content, a reproduction on its tree, and then, with the tree unchanged, the adoption of a quarantined delta — a byte-preserving refinement adding parts inside the bounded scope (adopted by an R0 machinery disposition and, separately, by an R2 reviewer), an `ignore` change excluding a file the execution read, and a governance-affecting re-scope. Expected: `on⁻` of every recorded observation is unchanged; the failure keeps counting (`undisputed = P`) unless a non-yielding observation stands with `on⁺`, which after the bounding judgment loses currency needs another current bounding judgment; differing old-content runs stay in (2). Negative discriminators: an implementation that evaluates the recorded basis as unit revisions or membership under the current `Σ`, or whose permissive predicate is not conjoined with the adverse one, must fail.
- **Recording granularity (SD-11).** The trajectory: `src/kern/f.py` holds `solve` and `helper`; composite `kern` has parts `kern.solve` and `kern.helper` (`symbol` terms); specification `S` (declarative oracle, thread scheduling free) declares `EXECUTION_DEPENDS_ON kern.solve`; current singleton `COMPLETENESS(EXEC)` on `{S}` and `{kern.solve}`; no observed reads; `solve` races and fails `l2_error` about half the time. A realization `p` at `T0` passes; an `IMPLEMENT` item changes only `helper`; the run on candidate `C` fails and is assessed `a⁻`, which counts at once; a reproduction on `C` fails. Expected: `on⁻(p, tree(a⁻))` holds, because `kern.solve` and `S` are unchanged at the recorded granularity, so `p` stays in (2) with another outcome, (2) fails, `undisputed = P`, the owner's adjudication obligation is derived, and for a D1/D2 claim `adm(a⁻)` holds and the floor fires at the first position. Variants with the same expectation: the item changes another unit's file in the same directory while the closure is bounded (no widened entry is recorded); the closure widened to the directory and the item changes only an ignored tracked file under it (the widened entry, computed under the frozen `ignore` patterns, is unchanged). Contrast: the closure widened to the directory and the item changes a governed file under it; the widened entry differs, so `p` leaves (2), as the reviewed `on` requires for content the execution may have read. Restrictive variant: a non-widened `prefix` unit in the basis gains a file; its recorded term's content identity changes, so an old yielding run no longer keeps (4) false on the new content, and a standing non-yielding run there satisfies (3) and (4). Negative discriminators: an implementation that compares whole files or Git trees containing a recorded region, that keeps separate recordings for realization currency and for matching, or that re-resolves recorded terms with the current `ignore` or analyzer, must fail.
- **External inputs (SD-12).** The trajectory: specification `S` reads a dataset through locator `L`, which its `fixed` table does not fix; `p` on `T0` reads pin `P1` and passes; `L` then serves `P2`; a run on `T0` reads `P2` and fails (`a⁻`), and its reproduction `r` on `tree(a⁻)` reads `P2` and fails; an item changes a recorded region and integrates `T1`, whose rerun `q` reads `P1` and passes. Expected: `p` is `on⁻` `tree(a⁻)` with another outcome, so (2) fails, `undisputed = P`, the owner's adjudication obligation is derived, and for a D1/D2 claim the floor fires; independently, `q` cannot serve (3) because `ext(q, real(a⁻))` fails. Variants: a passing run on `tree(a⁻)` that differs only by an unpinnable read keeps (2) failing; a D1/D2 failure whose realization has an unpinnable read and whose candidate changed no recorded region has `adm(a⁻)` and is not candidate-own (R3); a reproduction under a different pin does not satisfy (1). Negative discriminators: an implementation that compares pins in `on⁻`, or excludes unpinnable-read observations from (2), (4) or `adm`, must fail.
- **Matching guard (SD-13).** With `K` held fixed, adopt in turn each ledger-named input: a ruleset of a new system version that changes normalization; one that extends the anchor file-type table; a policy change; a structural adoption; an analyzer-set change; loss of a bounding completeness judgment; a loss boundary. Expected: `on⁻` of every recorded observation is unchanged in every case. The trajectory: `p` passes on `T0`; a racing run fails (`a⁻`), so (2) fails and the owner's adjudication obligation is derived; then the system-version adoption. Expected: `p` stays `on⁻ tree(a⁻)`, (2) keeps failing, `undisputed = P`, the obligation stays derived, and for a D1/D2 claim `adm(a⁻)`, the R3 class and the floor clause are unchanged. Negative discriminator: an implementation that re-resolves or hashes recorded terms under the current system version must fail.
- **Environment and pure resolvers (SD-15, SD-17).** A failure under runner image `b1` of a specification that leaves its environment free: a passing run under `b2` on `tree(a⁻)` defeats (2); a non-yielding run under `b2` on later content cannot serve (3); a reproduction and a non-yielding run under `b1` can. The same specification with a fixed environment: a run under another image is inadmissible, and only runs whose attribute entries equal `real(a⁻)`'s serve (1) or (3). A `symbol` term in a language whose analyzer would need host headers is a static error (§1.9) and that analyzer fails qualification; two hosts with different header sets give the same `on⁻` and `rev` for every admitted term; a realization that straddles a system-version adoption keeps `on⁻(p, tree(p))`. Negative discriminators: an implementation that keeps a free environment out of `on⁺`, infers the resolution context from the envelope `ruleset`, or lets a later record change `on⁻`, must fail.
- **Free execution attributes (SD-17).** Specification `S` fixes regime, parameters and environment image `I` and leaves backend and precision free; its runner class records backend, precision and CPU instruction set. At `T0`, `r0` runs on a CUDA node and fails `l2_error` through a CUDA-only defect (`a⁻`, counted); its reproduction `r1` on a CUDA node fails identically; an `IMPLEMENT` item changes another recorded region and integrates `T1`, whose rerun `q` lands on a CPU node and passes. Expected: `q` cannot serve (3), because `ext(q, real(a⁻))` fails on backend; `a⁻` keeps counting, `undisputed = P`, the owner's adjudication obligation stays derived, the rerun obligation asks for a CUDA execution on `T1`, and a passing CUDA run on `T1` can serve (3). A passing CPU run on `T0` is `on⁻` `tree(a⁻)` with another outcome and defeats (2). Variants with the same expectations: `float32` versus `float64`; an AVX-512 failure and an AVX2 pass under one image, with the instruction set recorded. Residual contrast: the AVX variant under a class that records only its image makes `a⁻` stale, as §17.5 and §32.2 disclose. For a D1/D2 claim the floor fires at the first position as before. Negative discriminators: an implementation that ignores a recorded free backend, precision or host attribute in a permissive use, or that reads the §17.2 recorded attributes as the configuration (so a passing CPU run on `T0` no longer defeats (2)), must fail.
- **Red then green under a free environment (SD-17).** A candidate's iteration 1 adds a test-first case to an admitted specification that leaves its environment free and fails it; iteration 2 fixes the code; a current `COMPLETENESS(EXEC)` judgment bounds the closure (an analyzer completeness declaration where no incompleteness marker exists, §2.6, or a reviewer's judgment, which lapses with changes in its scope). Expected: once a reproduction of the iteration-1 run and a non-yielding run on the iteration-2 content, both with its recorded execution attributes, stand, the iteration-1 failure is stale in the lineage's frame and, under the admitted reading, in the admitted state; it then neither blocks the lineage's integration nor raises a floor item for a D1/D2 claim. A candidate's tightened tolerance behaves the same. Discriminator: an implementation that keeps every free-environment failure counting until an owner disposition must fail. Contrast: with no bounding judgment, the iteration-1 failure goes to the owner; (1) needs a bounded reproduction, so a fix inside the bounding judgment's scope can cost a fresh reproduction bounded by the current judgment (an identical-tree shortcut is not a stop). Cost disclosure: in scientific code with incompleteness markers (data read by path, runtime configuration), most closures are unbounded, so this partially reverses SD-17's red-then-green restoration; it is listed for the stakeholder (closure map §5).
- **Reads through symbolic links.** `S` declares `EXECUTION_DEPENDS_ON kern` with current completeness; the solver opens `data/current`, a tracked symbolic link in an ignored directory pointing to `data/mesh_v1.dat`; `q` passes; an admitted change repoints the link to `data/mesh_v2.dat`. Expected: `q`'s recorded link entry no longer matches, so `q` is not current, `REALIZE` is derived and `q` cannot serve (3). A link to a file outside the tree is an external read. Contrast: changing an unrelated ignored file changes nothing. Negative discriminator: an implementation that records only the resolved target must fail.
- **Unobserved external inputs (SD-18).** A specification of an external-custody class that does not declare observation of reads outside the tree; the solver reads a mesh by absolute path outside the repository; `r0` fails under mesh `M2` and its reproduction fails identically; after the mesh reverts to `M1`, a passing rerun on new content. Expected: every execution of the class is recorded as having an unpinnable read, so (1) and (3) never hold, `a⁻` keeps counting, `undisputed = P` and the owner's adjudication obligation is derived. The same trajectory under a class that declares complete observation records the reads and pins, and the rerun under `M1` cannot serve (3). Negative discriminator: an implementation that treats an execution with no recorded external read as having read none, whatever its class declares, must fail.
- **Free seed (SD-18).** A `SINGLE` Monte Carlo specification leaves its seed free; on `T0`, seed 17 fails and seed 42 passes; a seed-17 reproduction fails identically; an item changes a recorded region and a seed-17 run on `T1` passes. Expected: the seed-42 run is of `conf(a⁻)` and `on⁻` `tree(a⁻)` with another outcome, so (2) fails, `a⁻` is never stale mechanically, `undisputed = P`, the adjudication obligation is derived, and for a D1/D2 claim the floor fires when (2) fails. Contrast: with only seed-17 runs on `T0`, a seed-17 pass on `T1` serves (3), as a fixed seed would; a seed-42 pass on `T1` cannot. Negative discriminator: an implementation that limits (2) or (4) to runs with `a⁻`'s seed, or lets another seed's run serve (1) or (3), must fail.
- **Complete external-input record (SD-23).** `real(a⁻)` reads `(L_bad, P_bad)` and fails; a reproduction reads the same and fails; a rerun on later content reads `(L_good, P_good)` and passes. Expected: the rerun cannot serve (3), since the locator sets differ; `a⁻` keeps counting. Variants with the same expectation: a run recording none of `a⁻`'s locators, a proper subset, a proper superset, an alias without a warranted correspondence. Contrast: a fixed run that reads exactly `a⁻`'s locators and pins and passes can serve (3). Every such run on `tree(a⁻)` with another outcome still defeats (2). Negative discriminator: an implementation comparing only shared locators must fail.
- **Class decision polarity.** A discriminating reading's R2-versus-R3 class for a D1/D2 claim uses `on⁺(p, T_b)` and `¬adm(a⁻)`: with the bounding completeness lost, a candidate-own showing that depended on the narrow basis no longer lowers the class, and a candidate change outside the recorded regions never makes `a⁻` candidate-own.
- **Embedded oracles.** A failure under an embedded oracle whose admitted reading is held only by absorption: verdict not computable under the integrated reading -> yielded -> not stale.
- **Outcome identity.** Canonical-form equality on failing outputs; `output_renames`; an output not evaluated by a new reading with the check in force at the base keeps the failure counting.
- **Time bound.** A scheduled execution exceeding its bound, or the 168-hour cap, ends `INCOMPLETE`; for a D1/D2 claim it creates the floor item.
- **Ensembles.** Replicate variation inside one ensemble realization creates no disagreement; two ensemble assessments differing do; a later passing ensemble never disposes of a counted failing one; a recorded, replayable free seed allows mechanical stops as a fixed seed policy would (§6.10), and randomness the runner does not supply allows them only until a differing run on the same content is observed.
- **Diagnostic model.** `qualification/ssds80/s1_disagreement_model_check.py` stays green in its default mode and keeps its sensitivity modes failing owner-grounded properties. It is a diagnostic transcription (DS-001), never a production test; it does not model `about`, frames other than the admitted state, lineages, Admission classes and floors, per-observation completeness polarity, structural scopes, witnesses, publication, external custody or real assessors, and it enumerates honest readings only. The R1 polarity cases above therefore run at the real owners; extending the model to them is optional diagnostic work, not a substitute.
- **Judgment-disagreement model.** `qualification/ssds80/judgment_disagreement_model_check.py` enumerates the §5.10 rules in four families, with a fifth for the gate decision's basis and a sixth for obligation routing after integration (§10.4, SD-36 to SD-41), and a seventh for a transformation review's judged scope (SD-42). The first covers a transformation `REVIEW` (with an amended item revision and two re-identified ones, one with a one-byte heading change), an `ACCEPTANCE` (with a subject re-identified with identical content, which its objection does not reach, S10) and a `GATE_DECISION` over actors of every independence and class, admitted, pending and abandoned frames, supersession, per-target relief, and challenge chains of depth two (counter-challenges and challenged dismissals included). The second covers `EQUIVALENCE` chains on one unit with four revisions: every subset of six passing judgments of three classes (one of them variously non-independent, self-declared by the author, in a pending frame, or risk-overridden to `PROVISIONAL`, alone or with a second), a `NOT_EQUIVALENT` on every ordered pair of revisions and class, and its reassessment, owner adjudication, peer or wrong-class supersession attempts, and challenges; it checks the vetoes, five consumers' three-valued `sat` and the adjudication obligation. The third covers `COMPLETENESS` on three units and five scopes (singletons, the subject, the tree): every subset of six passing judgments, one an analyzer declaration and one of another class, variously self-declared, pending or provisional, an `INCOMPLETE` on four scopes and the same resolutions; it checks each unit's closure bound. The fourth covers `PLAN_ACCEPTANCE` coverage of an item whose revisions are field values (prose, budget, write scope), ordered as §13.4 orders them: seven revisions, among them tightenings, a loosening, an R2 amendment incomparable with the accepted one, a revision joining both and a prose edit, every one of them also as the current revision, of a second item, and of a re-identified item whose revision is byte-identical to one of the first's: acceptances of each, a rejection of each, the item's current revision, the same resolutions and a fresh acceptance of the current revision by each kind of actor; it checks issuability. The brief carry of §16.5 is not modelled. The model computes the composing kinds' reach by the one generic rule of §5.10 (a); its oracle states each kind's composition separately but reads the same claims, so the claims column is a shared definition it cannot test (§5.10 (g)). The equivalence family gives each revision's differing content an author and includes an author's reversed-endpoint judgment; the plan family has three items (one a re-identification of another, with a byte-identical revision), field-value revisions and two-item rejections; its plan oracle builds the common tightening of an accepted and a rejected revision from their field values and tests it against both, rather than reading the row's formula (same prose and fixed fields), so a formula that disagrees with the claim fails. For the review row the claim and the formula coincide (one judged scope containing the other's, with re-dispatched reviews over `out(o)` that keep or re-do the rejected content), so its oracle restates the row; a seventh family (`review-scope`) transcribes §4.3's transformation-review entries (before-images, outputs, retained units, contract and governing entries) and selects `J` from them by role, independently of the reach rule but not of the Manual author's reading of `J`, with copies and amendments sharing prose and fixed fields (as hand-chosen shapes: the key itself is not computed), judgments of one transformation admitted at different times, integrated-result reviews including an item-level review over the parts' latest outputs, an integration whose retained units went stale after issue and Admission's check of the envelope's retained field, over first enactments, partial and empty re-dispatches and unrelated and repaired content on both the adverse and the passing side, and checks R1 `J` equals the post-state the review is asked to judge, R2 continuity, R3 specificity, R4 an empty `J` reaching only its own target, R5 independence over the authors of `J`, R6 one `J` for every judgment of a transformation, R7 an integrated-result review's independence over its output-entry content, R8 a stale retained part refused at integration and R9 the retained field checked at Admission (R6 and R7 hold largely by construction of the shapes); the re-identified item revisions test that no item condition survives in the model's rule. The fifth builds a gate decision's basis from an evidence core showing its required evidence (current or not), a revision-assessment record, a non-required realization, open challenges and a standing gate rejection from this or an abandoned enactment, superseded or not, and checks that the decision's `current` reads only its required premises and never a challenge-tier record (SD-35). The sixth evaluates §10.4's route list, as the model transcribes it, over an integrated `IMPLEMENT` item, a two-part partitioned item modelled as one obligation and a first candidate, with output and read-only changes, adverse reviews in and outside scope, a peer veto, R1 and R2 amendments (every R2 retiring the obligation), re-dispatches whose single candidate stays pending, that candidate's clean, NO-PASS, `INCOMPLETE`, `DISCREPANCY` and rebase outcomes, its revalidation and integration, a fence kept or re-applied, the principal's `AMEND` (always retiring) and `DECLINE`, and adverse item-level reviews naming a part or none, every sequence of up to three events with a budget of three, and checks I13 every open obligation has a route, I14 exactly one, I15 no `REVALIDATE` of an integrated review or task result and every reopened integrated item re-dispatched within budget unless a fence, a pending candidate or a decision comes first, and I18 a pending candidate never discarded, a kept fence's route ending once decided, and an adverse item-level review naming a part never leaving the item discharged. It does **not** check the list against the other sections' current text: their route claims enter only through the mutations that re-introduce earlier rounds' defects, so an unmutated run compares the list with itself (b365947 N1). It does not model an identity-keeping amendment, an R2 amendment with unchanged prose and fixed fields, separate part obligations, two candidates, a revert, an answered decision other than a fence's, the joint-invariant and specification-review obligations (unchanged since candidate 55, whose routing family checked them), several-subject evidence, or a decision's effect beyond its route; the residual §32.3 names lies there. The four judgment families check §5.10 (g) 1-8 against the oracle as (g) states it, and the gate-basis family checks I1/I3, I9 and a liveness invariant I10 (a ready gate obligation has an admissible answer), and the routing family I13-I15 and I18, and the review-scope family R1-R5, which bounds what a green run shows; `--mutations` re-introduces earlier defects (non-independent relief, cross-target review supersession, tier-limited and challenged-record adjudication eligibility, a run-keyed gate veto, frame records acting in the admitted state, `base` ignoring `nonind`, no class check, an endpoint-only equivalence veto, chains read only in their recorded direction, chains ignoring class, a blocked chain deriving no adjudication, a plan rejection or a review veto reaching only the same plan item, a review veto reaching re-identified items only with identical prose and contract, a review veto reaching only the same changed content rather than a re-dispatched review's judged scope, `J` read as §7.3's output-role entries only or as every entry §4.3 requires, the retained part read at each judgment's admission or keyed on the obligation, an integrated-result review with no authors, an item-level review with no entries, a stale retained part admitted, an unchecked retained field, the adverse side read as its changed units (an empty change vetoing every review), independence measured over the change only; the core family's objector stays a first enactment, so relief and supersession for an objection to a re-dispatched review are not modelled, a gate basis with `record` on every record shown, or with `identity` on its required premises too, a decision importing the revision assessment's currency rather than its standing, an acceptance veto keyed on content across subjects (against S10), a plan rejection reaching only acceptances that name its revision, every tighter revision, only the current one or only one below it on the path to the current one, a plan supersession admitted only while its revisions are current, an exemption for acceptances of a tighter revision, no per-target plan relief, a revert exemption, the current-revision join of SD-31, a rejection denying its named set only as a whole, equivalence authors measured on one side, `asserts` stricter than `base`, a completeness reach by the same scope only or comparing the analyzer identity, and the equivalence and completeness requirement keyed on the request; and, for routing, `REVALIDATE` of an integrated review or task result, an R2 amendment routed to the principal instead, a pending candidate of an integrated obligation re-dispatched over or ignored, a kept fence's route outliving its decision, an adverse item-level review iterating parts that stay discharged, and a `DECLINE` answering an item obligation's decision) and each must be caught, re-running only the families its code touches. It models no evidence assessment, plan objective section, intake, loss boundary, qualified gate value or request structure, and integration only in the routing family's abstract events, and it shares the Manual author's reading of §5.10; the real-owner cases of §31.5-§31.6 remain required.

#### 31.4 Admission, publication, currentness and loss

Real owners: Admission and the Ledger Store with real witnesses, deterministic failpoints with the production owner executing, and **ledger-only replay** (integration host disconnected) as the oracle for every publication classification.

- **Admission and concurrency.** Disjoint bases admit concurrently; intersecting bases revalidate; write-skew across disjoint files caught; a clean Git merge with a semantic conflict blocked; stale, duplicate, partial and very late results; protected-surface edits and modified envelopes rejected; duplicate discharge rejected; collateral regression rejected while accepted upstream change reopens dependents; Admission step 8 reads evidence only and discharge is not latched (R15, SD-36, SD-40): two sequential accepted `IMPLEMENT` items editing one leaf unit both integrate with the first's required evidence rerun on the merged tree, and the first item's obligation, whose outputs the second moved, reopens and is re-dispatched (a new task and enactment); a later item changing only a file the first item's reviewer read, or a governing unit, also re-dispatches it and derives no `REVALIDATE` of its integrated review or task result; an R1 tightening after integration re-dispatches it, whether or not the integrated content already meets it, while an R2 amendment derives a new obligation and a candidate of the old one is refused at integration; a candidate that makes another obligation's passing required evidence fail is refused (`REGRESSION`); while a re-dispatched candidate is pending, a clean rebase over a read-only change derives that candidate's `REVALIDATE` and never a second re-dispatch, and its NO-PASS within scope iterates within budget; at a spent budget, `COORDINATE(plan)` is the only route; a fence awaiting its decision is the only route; a kept fence derives `COORDINATE(plan)` until answered, an `AMEND` withdrawing or amending the item and a `DECLINE` resuming its route (drift); an adverse item-level review naming part `p1` reopens `p1`, which is re-dispatched, and one naming no part derives `COORDINATE(plan)`; a `DECLINE` is refused for any other decision on an item obligation; two successive changes `k1`, `k2` in a joint invariant's scope both integrate, `JOINT_INVARIANT(i, k1)` ends when `JOINT_INVARIANT(i, k2)` is derived unless it is `REFUSED`, which stays and derives a decision that lapses once answered; a second revision of an evidence specification ends the first revision's `SPEC_REVIEW` the same way; a change `k1` touching units inside and outside a joint invariant's scope, then a change only outside it, leaves `JOINT_INVARIANT(i, k1)`'s review current; a re-dispatch that integrates no change, or changes only another subject, leaves the item undischarged while its original subject's required evidence fails (`subject(o)` is the union over its enactments); a fenced or `OVERTAKEN` integration leaves its item obligation `OPEN` and its re-application claims it; an absorbed change that breaks evidence reaches the claim's subject; live-ref movement absorbed without blocking production; self-declared equivalence backdates nothing; compare-and-swap losers revalidate; FIFO queue under revalidation.
- **Crash windows.** Clean synchronous admission; crash before append; crash before admission (provisional survives, anchoring completes); crash after admission; witness admission failure (appends halt, answers stay at the previous head); admitted-pending publication; foreign push and force-push in the window; integration host unreachable; equivalent publication by squash, rebase or merge button; no configuration publishes a provisional entry.
- **Publication reconciliation and the incarnation publisher (R4).** Compare-and-swap succeeds then crash: before restart ledger-only replay gives `PENDING`; after restart the **new incarnation is not the publisher** and fences if the ref shows `B_n`, or records `PUBLISHED` if it shows `C_n`. Two processes sharing one host key: only the appending incarnation publishes; the other fences. A copied or restored operator-state directory confers no publication right. Publisher paused, takeover fences, human decides "keep", publisher resumes: its compare-and-swap fails. Publisher's compare-and-swap released before the fence: the fence fails, `C_n` observed, human decision admissible only after that observation. Human decision while a fence is pending: rejected (`NOT_SETTLED`). Two fence publishers paused in turn: the second classifies the first `OVERTAKEN` while the ref shows `B_n`, and a decision stays inadmissible until an entry observes the ref away from `B_n`. Foreign return to exactly `B_n` after a fence, then a stale publisher resumes: `LATE_PUBLICATION`, `CRITICAL` (detected, never asserted impossible). Barrier discriminators: an admission whose `obs` differs from `E`, or an absorption carrying records, is rejected, and a fixture-injected one halts derivation (R3). Recovery entries carry no `obs` and leave `pub = PENDING`.
- **Currentness and recovery.** With `(3, 2, 2, 0)`, `(4, 3, 3, 1)` and `LOCAL_TRUST`: the L99/L100 world (`ROLLBACK`); total loss of an unadmitted newest entry (L99 current, resubmission); sub-quorum trace (`FORK` until resolution, no boundary when proved never admitted); fresh clone `BEHIND`; fork plus witness disagreement; malicious rewind with a compromised push credential; witness loss below read quorum; `f` faulty witnesses cannot hide an admitted head; backup older than the admitted head; unauthenticated entry rejected; replica loss; missing content objects `UNAVAILABLE`; derived checkpoints never served as current; external SSDS ledger consultation qualifies its head; retired lineage reads `RETIRED`.
- **Known loss.** The workplan §22 known-loss program in full (demotion, demotion then restoration, challenge or revocation, ruleset change, evidence invalidation, external import, attestation in both scope forms, counter-challenge across the boundary, escalation across the boundary, product newer, historical visibility, exact requalification set, version rollback after loss, retired lineage, surfaced abandoned chain, provisional-only contrast with the non-admission bound, witness loss beyond `f`).
- **Confidentiality.** Credential-like and high-entropy values rejected; the incident drill (settle, rotate, re-encode, equal derived state up to renaming, retirement statement, stale mirror reads `RETIRED`, purge only with operation-specific authorization, retention weighing recorded); a value in `main` history routed to a new repository.

#### 31.5 Workflow, contracts and conformance

Real owners: Admission (step 3, step 7), Derivation (S3 conformance, routing), Dispatcher (envelopes, launches), Interface (briefs). The obligation-routing residual named in §32.3 (SD-41) is exercised at the real owners before G2: an R2 amendment with unchanged prose and fixed fields, an identity-keeping answer to a spent-budget or out-of-scope decision, an item-level review naming no part, a rejected earlier candidate beside a later one, and an out-of-scope NO-PASS on an earlier integrated enactment after a later one integrated.

- **Roles and binding.** Every role attempts every record kind, outcome and write outside its template: rejected. Phase-1 results and mid-task blocking reports bound and claiming nothing; forged, absent, revoked-key and compromised-key envelopes rejected; requests bound to discharged obligations or non-current contracts routed to revalidation; ledger-only replay reproduces every binding; retired-key envelope salvage only when listed.
- **Fail-closed independence.** A review bootstrap pasted into the authoring session, a Git-envelope review without lineage attestation, and a launch attestation naming the author's session each yield a non-independent judgment that discharges nothing; an `ATTESTED_FRESH` review from a disjoint session does.
- **Version binding.** A record declaring a `governs` different from its envelope is rejected; no agent record adopts a version; a `LEGACY(p)` brief renders through `p`'s profile.
- **Contracts.** Lint rejections (no verifier, heuristic verifier, protected or plan unit in scope, unnamed evidence specification, a D1-D3 unit in an `IMPLEMENT`/`REPAIR`/`MIGRATE` scope, an `AUTHOR` scope outside its declared domain, missing triggered slots, missing minimum coverage per §13.3, missing budget); control-tightening classification on generated diffs over every field, including tighten-then-loosen and fields injected by a newer schema, and on prose-only amendments with byte-identical TOML (R2: the item becomes non-issuable, an independent `PLAN_ACCEPT` is derived; a field-only comparator must fail); partition checks.
- **Revision assessments and the revision run (SD-16, SD-19, SD-22, SD-25).** A human-authored D2 revision and an absorbed one each derive a revising review whose brief carries the revising and tension-search duties and the machinery-computed predecessor; neither `ACCEPT` nor `GATE(g)` is ready until a revision-assessment record for exactly that revision counts; an authenticated `GATE_DECISION ACCEPT` and a direct human `ACCEPTANCE PASS` submitted before then are refused (`OBLIGATION_REVIEW_OPEN`), while an adverse gate decision is admitted; the gate core section 3 renders the record. **Adopted promotion:** a human push edits part `numerics.method` and declares it a subject; in the adopting request's frame the owner's prospective `ACCEPTANCE PASS` on `(numerics.method, σ_A, r_A)` is refused until `REVIEW(numerics.method, r_A)`, derived in that frame, is answered by a record naming `r_A`, displaying `numerics`' last accepted revision as predecessor; bound at integration, the acceptance is in the new run. **Revert:** `r0` accepted and gate-accepted, a tension `t` recorded, `r2` accepted with its record, then a restore of `r0`'s bytes by a foreign push, by an `AUTHOR` item, or while `r2`'s acceptance is revoked: a new run starts, `j0` and its gate decision are not current, `valid(s)` is not `T`, and `ACCEPT`, `GATE` and `REVIEW(s, r0)` are derived for the new run, the brief displaying `r2` and carrying `t`; `j0` answers nothing; the gate trigger and discharge see the same currency. A draft `r1` assessed but never accepted and later restored needs a new record, since its old record lies in an earlier run. **Frames that never integrate:** an acceptance recorded on a pending, abandoned or concurrent candidate changes no admitted currency and no displayed predecessor; the accepted subject stays valid while its candidate is accepted in the frame. **Tenure starts:** a rename with `renamed_from` plus a file move, a split into new files, a replacement at a new path, a kind or domain change and a re-cutover after rollback each start a new run that needs a new record; the displayed predecessor comes from declared lineage and prior byte ownership, and the reviser may extend it. **Records:** a revoked record, or one withheld by a loss boundary, makes the acceptance that names it non-current; an overridden challenge on it makes the acceptance `P`; re-acceptance of an unchanged revision after `REVALIDATE` within its run reuses its record. **Merged revision:** an `AUTHOR` item's candidate yields `r_C` with its assessments; a human edit to another section of the same file is absorbed; the frame's merged revision `r_m ≠ r_C` derives `REVIEW(s, r_m)` in the frame, and an acceptance of `r_m` is refused until it is answered. **Answers without the slot:** a `REVIEW NO_PASS` whose `revision_assessments` slot is empty, and a human's `REVIEW` judgment recorded with no `TASK_RESULT`, leave `REVIEW(s, r)` unanswered and the gate not ready. A D2 composite whose revision changed only through a nested D4 subject needs its record like any other revision, and its gate core says the change was nested. Contrast: a D4 subject reverted within its tenure is valid again through its old acceptance. Discriminators: an implementation that derives the review from the producing admission only, exempts revisions of `AUTHOR` integrations, accepts a prospective acceptance without the record, treats an adverse empty-slot answer or a slotless judgment as answering it, lets an acceptance from an earlier run or a never-integrated frame be current, or applies the run only at admission and readiness but not in `tgt`, must fail.
- **Plan prose behind a `ref`.** An item whose statement `ref` resolves outside its own part and outside the plan `Objective` is rejected at lint; an edit to the `Objective` makes every covered item non-issuable and derives `PLAN_ACCEPT`. Discriminator: an implementation that computes plan-acceptance coverage from the item part's revision alone while accepting out-of-part `ref` targets must fail.
- **Authoring and documentation items.** An accepted `AUTHOR` item for a D2 unit derives exactly one `AUTHOR` obligation held by the implementer role; its brief carries the D2 core, the revising and tension-search duties and the `o1_content` and `revision_assessments` slots; the authored revision cannot be accepted, reviewed or plan-accepted by the authoring lineage; a role outside the template, or an `IMPLEMENT` task, writing the D2 unit is rejected. A `DOCUMENT` item whose write scope contains a D1, D2 or D3 unit is rejected at lint. An `IMPLEMENT` or `DOCUMENT` item with `ssds.manifest` in scope that edits a D2 unit's semantic table, scope or membership, declares a new D2 unit, changes `ignore` so that a D2 `prefix` unit gains or loses a file, declares a new part of a D2 composite (with or without a semantic table), or moves a D4 unit into a D2 composite, is a `VIOLATION`; an `AUTHOR` item for that D2 unit, with `ssds.manifest` in its write scope (§1.2, §13.2), may edit those declarations, and its brief carries the revising and tension-search duties. Discriminators: an implementation that keys the revising duties on item kind while letting a `DOCUMENT` scope contain D1-D3 units, or that computes the write set from changed bytes and keys rather than effect, must fail. Concurrency: an admission outside an `IMPLEMENT` item's scope made after its base never enters that item's write set, and its result is admitted or revalidated, never refused with `AUTH_WRITE_SCOPE`; two items that each change `ignore` and add ignored files under a D2 prefix are a `VIOLATION` for whichever integrates second; an `IMPLEMENT` item changing only a D2 unit's `renamed_from` is a `VIOLATION`. A `DOCUMENT` or `MIGRATE` item whose scope contains a `D4` test or `EVIDENCE_SPEC` unit fails lint without `TEST_INTEGRITY` and `BOUNDARY` secondary checks.
- **Judgment disagreement and task results (R9).** `REVIEW NO_PASS` on `X` followed by an independent `PASS` on the same candidate content does not discharge `REVIEW(X)` or integrate `X` without the owner's adjudication, in either order of admission; `ACCEPTANCE FAIL` then `PASS` on one triple, and `PASS` then `FAIL`, leave `s` invalid until the owner adjudicates or the `FAIL` is withdrawn by its own author's reassessment or disposed by an upheld challenge whose adjudication was admitted as independent (and, against a human R3 `FAIL`, by an R3 human); a peer's `FAIL` naming an earlier `PASS` in `supersedes` is rejected (`AUTH_SUPERSEDES`); an answered review obligation is never dispatched again, and a second passing judgment bound to it is refused; a reviewer request without its `TASK_RESULT`, or with an empty `bidirectional` slot on a scientific subject, has its passing judgments refused while an adverse judgment in it is admitted; every reviewer task counts one iteration. A `NO_PASS` under item revision `i1`, an R1 tightening to `i2`, a new candidate with identical changed-unit content and an independent `PASS`: the `PASS` is vetoed, `REVIEW(X')` is `REFUSED`, the owner's adjudication obligation is derived and nothing integrates; the same for `CONFORMANCE`. The same cases run for `PLAN_ACCEPTANCE`, `EQUIVALENCE`, `COMPLETENESS`, `GATE_DECISION` and `INTAKE_DISPOSITION`. Product scope: a `PRODUCT_SCOPE_ACCEPTANCE REJECTED` of surface `m` and a gate holder's `PRODUCT_SCOPE_ACCEPTANCE ACCEPTED` of `m` co-submitted with a D1 `GATE_DECISION ACCEPT`, in both orders: `m` does not bind, the owner's adjudication obligation is derived, and the gate's acceptance of the D1 revision is unaffected. Discriminators: an implementation that discharges on ∃ `PASS`, that re-dispatches an answered review, that compares item revisions by equality in the veto, or that lets the later of two contrary judgments win, must fail.
- **Conformance.** Each `HARD` template qualified per §14.7 on real trajectories; signal inertness (removing every `HEURISTIC` template changes no admission or discharge on a replayed corpus); never sufficient (clean conformance without review never integrates); disclosed versus undisclosed breach; faithfulness discrepancies; test integrity; mutation-strength shortfall `INCOMPLETE`; advisory pre-flight never enters discharge; determinism across hosts.
- **Duty compilation.** Same brief for the same basis, query and policy; every triggered duty and slot present and no untriggered one; every injection event of §16.3 fires exactly on its derived predicate. Discriminator: wording variants of identical structured content change nothing.

#### 31.6 Escalation and the inspector

Persistence after target amendment, basis staleness and a loss boundary; floor items never closed by any principal operation; raiser withdrawal of a floor item leaves attention open; reclassification moves only non-floor items and returns them on an upheld challenge; domain floor raises `ROUTINE` reports on D1/D2 units; authority-defect requests cannot be resolved locally; blocking reports suspend exactly the raising task; deterministic inspector ranking per §16.8; the delegate floor carries a material E2 finding through any number of intermediate roles; a gate `ACCEPT` marked unqualified is refused while the core lists required unavailable, disputed or stale evidence. **Qualified gates (SD-24):** with the subject, bases and outcomes fixed and a known material missing record outside the required evidence, an `ACCEPT` with `adequacy = INADEQUATE` is refused; a `QUALIFIED` `ACCEPT` makes `valid(s) = P`, its descendants `P`, and the obligation `DISCHARGED_PROVISIONAL` only where policy permits provisional continuation, otherwise `OPEN`; only a supersession by its own author's `UNQUALIFIED` `ACCEPT` or the owner's adjudication ends the qualification. **Minimum over eligible decisions:** a second holder's `QUALIFIED` decision on an answered gate, in any frame, enters the minimum; (A) a rebase whose earlier frame decision is stale: `REVALIDATE` is derived in the rebased frame before integration, and the frame's gate term equals Admission's post-admission one; (B) an earlier iteration's `QUALIFIED` or `UNQUALIFIED` decision is not eligible in a later iteration's frame or after it integrates, and the later iteration's gate core displays it when the subject content is identical (SD-26); (C) a `QUALIFIED` D1/D2 frame decision, integrated, is superseded by its author's `UNQUALIFIED` reassessment and the gate term becomes `T`; (D) one state rule (SD-25; B1-B): a candidate `Z` whose frame reassessment by holder H supersedes H's admitted gate `REJECT`, while a peer's admitted `ACCEPT` stands: with `Z` pending and after `Z` is abandoned, the admitted gate term stays `F`, the veto and the owner's adjudication obligation remain, and in `Z`'s frame the reassessment ends the veto; an admitted `QUALIFIED` decision superseded by its author's `UNQUALIFIED` reassessment in `Z`'s frame leaves the admitted term exactly `P` (not `F`, not `T`), its inspector entry open and permitted provisional work continuing, while the frame's term is `T`; an admitted `UNQUALIFIED` decision whose basis is stale only in `Z` keeps the admitted `T` while `REVALIDATE` is derived in the frame; when `Z` integrates, the admitted term equals the frame's; (E) a single frame with one `UNQUALIFIED` decision has gate term `T` and integrates; (F) an earlier iteration's decision on a revision its enactment never integrated never counts, when a later iteration of the same obligation integrates or when identical bytes arrive later by absorption or another candidate; two candidates that change a gated D3 subject (or a D2-domain evidence specification) to the same revision each record a gate decision in their frame, one `UNQUALIFIED`, one `QUALIFIED`, and both integrate in either order: the gate term is `P` until the `QUALIFIED` decision is superseded; for a D1/D2 subject, a clean rebase's frame decision is eligible after the rebased transformation integrates, and an earlier iteration's is not; after an `UNQUALIFIED` decision supersedes a `QUALIFIED` one, an upheld or open blocking challenge against it, or a loss boundary withholding it, leaves the gate term below `T` (no earlier decision revives); after a D1/D2 revert or a tenure restart at the same revision, the new run's gate decides afresh and an `UNQUALIFIED` decision there gives `T`; a gate decided on a candidate frame declares that frame, passes Admission step 6 there, and is satisfied after integration, in the new revision run for a D1/D2 subject; a frame gate decision of an abandoned candidate never becomes eligible in the admitted state, even when identical bytes arrive by absorption; an admitted-frame gate decision recorded before integration on changed content is refused; a second holder who sees a limitation records a `REJECT`, which vetoes the passing decisions and derives the owner's adjudication; an abandoned candidate's `REJECT` vetoes as §5.10 states, whatever its frame. **Enactment unit (SD-26):** (I) an `AUTHOR` item's iteration 1 integrates `r1` with acceptance and gate; a foreign change is absorbed, the obligation reopens and iteration 2 restores `r1`: the restoration starts a new run (a new task), iteration 1's acceptance, gate decision and revision-assessment record are in no run, `ACCEPT`, `GATE` and `REVIEW(s, r1)` are derived, and the predecessor shown is the absorbed revision; a second integration request of iteration 1's own transformation is refused (`OBLIGATION_REENACTED`); (J) an admitted `ACCEPTANCE FAIL` vetoing a peer's `PASS`, reassessed by its author in a rejected iteration's frame on evidence that iteration added: after a later iteration without that evidence integrates, the veto and the owner's adjudication obligation remain; the gate variant keeps an admitted `QUALIFIED` term exactly `P`; the failing-assessment variant keeps `undisputed = P`; (K) two partition parts each change one `NATIVE` D1/D2 composite: each part's integration starts its own run and claims only its share; part B's frame records do not act after part A integrates; (L) a cutover is carried by its transformation's integration: its `REVIEW(s, r)`, acceptance and gate are derived in that frame from the ledger alone (two derivation hosts with different Dispatcher journals agree), and a re-cutover after rollback under the same `MIGRATE` item is a new task with a new run, the first native tenure's gate decision and record not in it; (N) gate veto across runs: iteration 1 of an `AUTHOR` item is gate-`REJECT`ed by `H`; a re-dispatched iteration 2 with identical D2 content gets `H2`'s `ACCEPT`: `h2` is vetoed, `GATE(g)` is `REFUSED`, `ADJUDICATE_DISAGREEMENT` is derived and nothing integrates; the same through another item or an absorbed revert reaching the same revision; contrast: an iteration yielding a different revision is not vetoed; (O) a fenced admission re-applied after the human decision is a new task: its `NATIVE` D1/D2 subjects get a new run and need fresh acceptance and gate; with the fence kept, those subjects are back at their earlier revisions in a new run and need them too; (P) relief follows the veto's key: `H`'s gate `REJECT` in iteration 1's run; iteration 2 adds the missing evidence with `s` unchanged; `H`'s `ACCEPT` in iteration 2's frame naming the `REJECT` in `supersedes` is admitted, ends the veto in that frame (`gterm = T`, no adjudication obligation there), leaves it standing in the admitted state while iteration 2 is pending, and ends it there after integration; a reassessment recorded in iteration 1's frame never acts in iteration 2's; the same for the owner's adjudication, for a revert or another item reaching the same revision, and, for reviews: `H`'s `NO_PASS` on `X1` at item revision `i1`; after an amendment to `i2`, the owner's `PASS` on `X2` (identical content) discharges `REVIEW(X2)` without superseding anything and relieves an agent's `PASS` on `X2`; after a revert to `i1`, an agent's `PASS` on `X1` is still vetoed and `X1` does not integrate without the author's or owner's pass of `X1`; the same through a clean rebase and a reverted governing-closure unit; a `REVIEW` naming another transformation's `NO_PASS` in `supersedes` is rejected; independence of relief: an independent peer's `PASS` on `X1` vetoed by `H`'s `NO_PASS`, then an owner's or author's `PASS` on `X1` admitted as non-independent (`UNKNOWN` lineage on a manual route, or lineage overlapping the author's): the veto stays, `REVIEW(X1)` is not discharged and `X1` does not integrate; an independently attested owner pass of `X1` then relieves it; challenge route: an ordinary challenge against `H`'s `NO_PASS` upheld by an adjudicator with `UNKNOWN` or overlapping lineage leaves the veto, `ADJUDICATE_DISAGREEMENT` stays derived and nothing integrates, while an `ATTESTED_FRESH` disjoint adjudicator's upholding ends it; the same for `CONFORMANCE`, `ACCEPTANCE`, `PLAN_ACCEPTANCE` (where it is the only relief after amendment), `EQUIVALENCE` and `COMPLETENESS`; a human author upholding a challenge to a `FAIL` on their own revision counts only under the owner exception, with the common-mode dependency shown; an R2 adjudication of a challenge against a human gate or product-scope `REJECT` is refused; a non-independent `DISMISSED` of a blocking challenge against a passing judgment leaves it blocked; a non-independent `REVIEW PASS` does not answer `REVIEW(X)`, which stays dispatchable; chain cases: an independent revocation of an `ACCEPTANCE`, `REVIEW`, `CONFORMANCE`, `PLAN_ACCEPTANCE`, `GATE_DECISION ACCEPT` or subject triple, then a counter-challenge upheld by the revision's author or an `UNKNOWN`-lineage agent: that adjudication is refused and the revocation stands, while an `ATTESTED_FRESH` disjoint counter-adjudicator's upholding lifts it; a non-independent dismissal of a blocking challenge against an observation, a subject triple, or an independent upholding is refused, so the observation does not stand, the triple stays blocked and the resolution stays contested; an R2 counter-upholding against an R3 human upholding is refused; a refused adjudication leaves `ADJUDICATE(c)` dispatchable; a human author's direct `ACCEPTANCE PASS` on their own revision leaves `valid(s) ≠ T` and `ACCEPT(s)` derived, except under the owner exception with the common-mode dependency shown; a human acceptance of a revision with absorbed bytes counts with a `NON_AUTHORSHIP_ATTESTATION`; one definition: a machinery analyzer `COMPLETENESS(X, EXEC)`, with or without a content change to `X`, bounds the closure and the §31.3 red-then-green case completes; an agent's `LEGACY_ACCEPTANCE` of a Case B subject supports; an author's self-declared `EQUIVALENCE` about the author's own change covers nothing; the author's counter-upholding of an independent revocation is refused by an Admission generated from §3.4 and from step 3 alike; a claim author's dismissal of a blocking challenge against an `IMMATERIALITY` on her own claim is refused, and an independent adjudicator's restores the disposition; a revision author's dismissal of a blocking challenge against the revising reviewer's record is refused; a refused adjudication leaves its `TASK_RESULT` admitted and `ADJUDICATE(c)` dispatchable; the same for `CONFORMANCE` and for a failing assessment's non-independent disposition; a `PLAN_ACCEPTANCE` rejection under objective `o1` superseded under `o2` is not lifted for `o1`; (R) supersession targets: an assessor's own `PASS` reassessment of the same realization, obligation and reading supersedes its `FAIL` and disposes of it where it acts, as does the owner's adjudicating assessment; a `PASS` for another obligation or reading naming it is rejected (`AUTH_SUPERSEDES`); an owner's `PLAN_ACCEPTANCE ACCEPTED {A1}` naming a `REJECTED {A1, B1}` is rejected; an `EQUIVALENT` of another class naming a `NOT_EQUIVALENT` is rejected; a human author's direct reassessing `ACCEPTANCE PASS` on an obligation its `FAIL` answered is admitted; a re-partition derives part obligations distinct from the earlier partition's, partitions only undischarged obligations, and keeps a discharged part discharged; `H`'s `COMPLETE` at members' revision `v2` naming its `INCOMPLETE` at `v1` is rejected, a `COMPLETE` at `v1` naming it is admitted, and after a revert to `v1` an agent's `COMPLETE` at `v1` stays vetoed and a failure it would bound stays counting; a `PLAN_ACCEPTANCE` rejection whose rejected set was amended is lifted only by an upheld challenge; (S) cutover timing: a carrier that integrates before any cutover record exists leaves `s`'s mode unchanged, and a later `MODE_TRANSITION` declaring its frame is refused; a cutover record in the frame of a pending transformation of another item kind is refused, as is a second record in one enactment; a carrying integration then fenced leaves `s` `NATIVE` and invalid with the stated options; a cutover record declaring the admitted frame is refused; of two pending carriers of one subject, the second has no frame once the first has cut it over; (Q) cutover end to end: a `LEGACY(p)` D2 subject cut over by an `AUTHOR` item's transformation and a D4 subject by a `MIGRATE` item's, each with a human `MODE_TRANSITION` in the carrying frame; the frame derives `REVIEW(s, r)`, acceptance and gate from the ledger alone; the integration is refused until conditions 1-6 and §7.6 hold; an agent-submitted `MODE_TRANSITION` is refused; a cutover record for a D2 subject in a `MIGRATE` transformation's frame is refused; a D4 cutover with no content change completes under its item; (M) a ruleset adoption that re-identifies a D2 revision starts a run identified by its entry, and its reversal revives nothing. **Run identity (SD-25; B1-D):** (G) an `AUTHOR` candidate changing a `NATIVE` D2 subject: its frame `REVIEW(s, r)`, `ACCEPT(s)` and `GATE(g)` obligations have the same identities, and its frame records name the same run, whether it integrates next or after an unrelated records-only admission, and that admission starts no run; a concurrent absorption that changes the subject makes the frame records stale and derives their revalidation; a different enactment that reaches the same bytes first starts its own run, and the candidate's frame decisions are not in it; (H) a candidate whose item requires a gate on an unchanged `NATIVE` D2 subject, in a run another enactment started: its frame decision is in the admitted run in the frame and after integration, and the gate term is the same in both. **Composition (SD-28, SD-29; R14):** (T) with genuine revisions `r0`, `r1`, `r2` of a unit and independently bound judgments, a standing `NOT_EQUIVALENT(r0, r2, k)` and passing `r0 -> r1`, `r1 -> r2` of class `k`: a record with `content(u, r0, k)` does not close unqualified in either admission order, `ADJUDICATE_DISAGREEMENT` is derived, and the owner's `EQUIVALENT(r0, r2, k)` naming the objection in `supersedes` restores the reuse; the same for a longer path, an objection on an interior segment, a vetoed direct pass beside a parallel path, chains converging on `cur(u)` (`r0 -> r1 -> r3` with `r2 -> r3`), an objection recorded with reversed endpoints, two hops each under a blocking challenge with an in-force risk override (`PROVISIONAL`), frame enactment and continuity after a loss boundary; contrasts: a chain through a hop whose class does not cover the objection's, a path that does not join the objection's revisions, and another unit stay usable. (U) completeness: subject `s` with units `u1`, `u2`, `u1` having an undeclared `DEF` prerequisite `p` outside `s`; independent `COMPLETE` on `{u1}` and `{u2}`, then an independent `INCOMPLETE` on `units(s)`: the acceptance closure of `s` is not bounded by the singletons (it widens and includes `p`), `ADJUDICATE_DISAGREEMENT` is derived, and the owner's adjudication restores the bound; the same against an analyzer declaration on `units(s)`; contrasts: an `INCOMPLETE` on `{u1}` beside a `COMPLETE` on `units(s)` reaches nothing, and a judgment of another class stays usable. (V) plan coverage (SD-30): an acceptance of item revision `i1`, a tightening amendment to `i2`, then an independent `REJECTED` of `i2`: the item is not issuable and `ADJUDICATE_DISAGREEMENT` is derived; a peer's fresh acceptance of `i2` is vetoed too; the rejecter's or the owner's acceptance of `i2` relieves that target and restores issuance, as does the owner's adjudication naming the rejection while its basis holds; after the principal reverts to `i1`, or loosens one field back within `i1`'s bounds, the acceptance of `i1` stays vetoed (it shares a tightening with `i2`), no `PLAN_ACCEPT` is derived, `ADJUDICATE_DISAGREEMENT` stays derived, and the rejecter's or the owner's acceptance of `i1` relieves it, its brief stating that the relief also clears coverage of `i2` (SD-31, SD-32); after a further tightening to `i3` instead, the acceptance of `i1` stays vetoed, a peer's fresh `ACCEPTED(i3)` is vetoed, the rejection stays in the gate, coordination and plan-acceptance briefs, and the rejecter's or the owner's acceptance of `i3`, or an upheld challenge, restores issuance; a rejection of `a1` on its first revision, a one-unit budget tightening to `a2` and a peer's fresh `ACCEPTED(a2)`: not issuable, `ADJUDICATE_DISAGREEMENT` derived, the rejection in the new acceptor's brief; a rejection of `a0`, an R2 amendment to `aQ` incomparable with `a0` accepted independently, then any later revision: the acceptance of `aQ` is vetoed from the rejection's admission (`aQ` and `a0` have the same prose and fixed fields), and stays vetoed through an R1 tightening to `a3 ⊒ a0` and a loosening or revert below it, with `ADJUDICATE_DISAGREEMENT` derived throughout, until the rejecter's or the owner's acceptance of `aQ` relieves it; the 4c52205 trajectory (accepted budget 10, scope `{a,b}`; rejected budget 5, scope `{a,b,c}`; tightening to budget 5, scope `{a,b}`; loosening to budget 6) stays not issuable at every step; contrast: an acceptance of a revision whose prose differs from `a0`'s is not reached, and the rejection is carried into its acceptor's brief; the rejecter's own `ACCEPTED` of `a0` naming the rejection in `supersedes` is admitted after a further tightening, while `a0 ⊑ cur`; a rejection of `{A1, B1}` vetoes an acceptance naming `{A1}` alone, and one recorded under objective revision `o1` vetoes an acceptance under `o2` naming the same item revision; after an R2 prose edit, a new target, the next acceptor's brief shows the standing rejection labeled as another reviewer's; likewise after an amendment of the objective alone (item revision unchanged), after one with another item also amended, and for a rejection naming several items when only one is asked about, while a peer's pass on the new target stays vetoed and the rejecter's or owner's exact-target pass relieves it; a brief selector restricted to rejections of an earlier item revision fails this case. (X) identity (SD-33): a `REJECTED` of item `A` at `a1`; a human removes part `P.A` and declares `P.A2` with byte-identical prose and contract, or copies `A` into another plan; a fresh peer's acceptance of `A2` is vetoed, `ADJUDICATE_DISAGREEMENT` is derived, the whole-plan brief carries the rejection, and the rejecter's or the owner's acceptance of `A2` relieves it; a transformation `NO_PASS` on `X1` under `A`, then `A` re-identified as `A2` (byte-identical, or with a heading one byte different, or with an amended contract) and a re-dispatched `X2` with the same changed-unit content: the peer's `PASS` on `X2` is vetoed, its review brief carries the `NO_PASS`, and `X2` does not integrate without the author's or the owner's pass (SD-34); the plan-acceptance and re-review briefs of the plan subject carry the rejection and the findings of removed items; an amendment of `A`'s contract with the same changed-unit content stays vetoed as before; after a `NO_PASS` of `X1` on unit `u` of an integrated item, a re-dispatched enactment that changes only `v` (or nothing) has a review over `out(o) = {u, v}` with `u` at `X1`'s content: a peer's `PASS` of it is vetoed and the owner's adjudication obligation is derived, while one that re-does `u` is not reached; a `NO_PASS` of an empty re-dispatch whose review judged retained `u1` reaches a later review keeping `u1` but neither a review of unrelated `w9` nor a repair to `u2`; a reviewer who authored retained `u1` is not independent for a re-dispatched review over it (SD-42); a peer's `NO_PASS` of a candidate admitted after another candidate of the same obligation integrated still reaches that candidate's own earlier `PASS`; after a `NO_PASS` on retained `u1`, an R2 amendment of the item's budget, a re-identification or a copy into another plan keeps `u1` in the next transformation's `J`, and an item with different prose does not; the human who authored a change is not independent for its joint-invariant review (SD-44); a second candidate issued while a first of the same obligation was pending is refused at integration (`STALE_RETAINED`) once the first integrated, and its re-issued task retains the first's outputs; a part's implementer is not independent for the item-level review (SD-45); contrast: a transformation with different changed-unit content is not reached, and a `PASS` of the same content under an unrelated item is vetoed until its author's or the owner's pass (disclosed cost). A reach or carry keyed on the item's identity or on its prose fails these cases. (Y) gate basis (SD-35): a gate's rendered evidence core showing (i) an open non-blocking challenge, (ii) a permitted risk-overridden challenge, (iii) a stale non-required realization and a finding whose provenance moved, (iv) a standing gate rejection from another enactment, and (v) the holder's own rejection, superseded by the holder's `ACCEPT`: Admission and Derivation call `current` on no challenge-tier record and read no report's provenance; the core retains every item; the decision supports at `T`, or `P` when qualified, exactly as its required evidence and, for D1/D2, revision assessment allow; an unresolved objection still vetoes it; a change or loss of required evidence still prevents unqualified closure; direct and frame cases, both admission orders; negative control: turning a required premise's `record` entry into `identity` must fail; the same for a review shown an earlier stale run of the candidate's checks beside the current one: only the current run is a premise. (Z) no stranded obligation (item 31): `NATIVE` D1 `a` and `NATIVE` D2 `b` governed by it, `b`'s `AUTHOR` result reading `a`; integrate, accept and gate `b`; then accept a real change of `a`: an in-run re-acceptance and gate of unchanged `b` are admitted with the old revision-assessment record, and `b` is valid again; the same after an amendment of the `AUTHOR` item after integration and after a change of a unit the reviser merely read; negative controls: revocation, block and loss withholding of the record still make the acceptance non-current, and a risk override makes it `P`; a gate decision relying on an assessment that is re-realized and re-assessed derives `REVALIDATE`, which a superseding decision by its author or the owner on the new core answers; an acceptance that declares an additional `record` entry on a stale revision-assessment record is refused at step 6; the same for an acceptance whose completeness judgment is superseded or revoked, and for a review whose check execution goes stale; across every obligation of §10.2, none is dispatched whose every answer Admission must refuse, and no non-current judgment a current obligation depends on is left without a ready or a waiting route (an earlier enactment's review after a re-dispatch, a joint-invariant review after a change outside its scope). Identity: a `FAIL` on `s` at `r`, then `s` re-identified as `s2` with byte-identical content and a declared `renamed_from`: a peer's `PASS` on `s2` is not vetoed (S10), and its acceptance brief carries the `FAIL` as history; without a declared lineage the brief does not, as §32.2 discloses; the same for a `NOT_EQUIVALENT` or `INCOMPLETE` whose units are re-identified. (W) independence of equivalence and completeness: a human author who changed `u` in one request records `EQUIVALENT(u, r0, r1, EDITORIAL)` in a later records-only request: it is admitted as non-independent, covers nothing and restores no old evidence or acceptance; the same for an `UNKNOWN`-lineage reviewer task and for a completeness judgment; an `ATTESTED_FRESH` reviewer's equivalence in a separate request covers; the author's `EQUIVALENT(u, r1, r0, EDITORIAL)` with reversed endpoints is non-independent too and, its hop running `r1 -> r0`, never serves a path from `r0`; a reverter's equivalence about their own revert is non-independent; a cutover `MIGRATION` equivalence over legacy content of unknown authorship is admitted as independent only for a human with a `NON_AUTHORSHIP_ATTESTATION` or under the owner exception, and §31.9 counts exactly those. Discriminator: an implementation that shows the caveat but closes unqualified, lets an equivalence path or a union of completeness judgments bypass a standing objection to what it composes, or lets tightening coverage carry an acceptance past a standing rejection whose controls the current revision keeps, keys the equivalence or completeness requirement on the request or on one side of the change, reads a `sat` hop against its recorded direction, falls back to an earlier decision, carries a cap across runs, reads supersession or veto relief from every admitted record whatever its frame, or keys a run by ledger position or by obligation, keys the gate veto or its supersession authority on the run-parameterized obligation, lets a review's supersession or relief cross item revisions or bases, or lets an earlier iteration's or partition sibling's frame records act after another enactment of the obligation integrates, must fail.

#### 31.7 Frames, migration, intake and external units

Candidate frames through the production path (implementer's genuine `read` then edit; before-image, output and context roles; prospective structure; bootstrap from a part with no prospective acceptance; transformation identity with two adoption sets; rebase variants; merge determinism under the pinned implementation and conflicts producing no frame); intake through the one route (manual edit, untracked generated file, opaque binary quarantined and never executed, external branch, authority-like document, agent overstep, foreign manifest edit, neutral auto-adoption only when enabled); migration (single opaque subject; byte-preserving refinement; the holistic Gaussian-units counterexample; legacy section import refused; carve-out with `LEGACY_RELEASE`; cutover quiescence record; version rollback needs a fresh import; no dual-current mode); cross-repository (pins never stale by external movement; consultation supersession; unreachable ledgers supersede nothing; producer-then-consumer sequence).

#### 31.8 Security, Core independence and fitness

No secrets or private telemetry in the ledger or repository; adversarial records inject no actions; instruction-like evidence stays inert; human decisions need the declared mechanism; inspection views give safe aggregates; §26.2 fitness checks; Core's own test suite and frozen-profile tests pass without SSDS installed (PC-001); SSDS installed does not change any Core prompt for version-bound work.

#### 31.9 Usability and doctrine realization (G3, measured, never claimed)

Live trajectories on real tasks in shadow mode, paired against the document-controlled 7.2.1 baseline on the same executors and fixtures, with gates calibrated from simulated operating characteristics before any spend, evaluator and oracle instruments validated first, and rules, custody and blinding frozen before runs (7.x lessons). Measures: agents complete bounded work without reading machine records and with less context; unauthorized mutation, claim integrity, owed-duty presence, narration where none was owed, and survival of material delegated findings to the human, on the 7.x panel rerun with SSDS briefs, contracts, conformance and escalation. Detection is reported separately, because enforcement is not expected to improve it. Claims stay bounded to the duties, harnesses and models exercised (SD-6). Costs are measured, not asserted: false staleness under widening, promotion frequency, reading and reproduction burden, retention cost, human-attention volume, fence frequency (R4), and the rate of transformation reviews that only a human or the owner exception can pass because their judged scope retains content of unknown or broad authorship (SD-42), the re-dispatches and `STALE_RETAINED` refusals that same-key coupling causes, and the size of retained-unit sets (SD-44, SD-45). Also measured: the rate of blocking challenges that only a rerun or the owner exception could dismiss because the eligible adjudicator set was empty (§5.10 (a) `authors`); the share of equivalence and completeness judgments, cutover `MIGRATION` equivalences included, that needed a human non-authorship attestation or the owner exception because their content's authorship was unknown (SD-29); and how often a standing objection's reach widened closures or stopped reuse that no consumer contested (R14).

#### 31.10 G1 document checks (executable now)

- the Manual and closure map exist at their routes; the closure map maps every §21 item and every §16.2 row to a Manual section;
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` passes (routing and lifecycle frontmatter only);
- `python3 -I qualification/ssds80/judgment_disagreement_model_check.py --mutations` exits 0: on the cases it models (§31.3) the §5.10 rules hold every §5.10 (g) invariant against its oracle, and every re-introduced earlier defect is caught. A design diagnostic of the written rules (DS-001): it cannot establish adequacy, cases it does not model are unchecked, and a green run is not production-owner evidence;
- `git diff --check` is clean;
- PEM schema validation passes for the bound basis;
- the frozen Architecture 1.6.0 file is byte-unchanged;
- no protocol `source/`, `dist/`, profile or snapshot file changed.

These establish structural facts only. Whether the Manual is adequate is for independent Review.

### 32. Limits, residual risks and reopen triggers

#### 32.1 Where machinery stops

Machinery prepares but never decides: whether two scientific or numerical formulations mean the same; whether a change is editorial beyond byte and normalization identity; whether an acceptance supports a newly scoped subject; whether a foreign structural declaration expresses intended governance; whether a set of objects is genuinely simultaneously defined; whether a discrepancy is a D4 defect or exposes inadequate D3, D2 or D1; whether evidence supports a claim and whether gate evidence is adequate; whether a relation is real or a scope complete; how a legacy region decomposes; whether an architectural change preserves its parent; whether a Serious Challenge is warranted and how it is adjudicated; whether a risk override is acceptable; whether a marked product surface is accepted; whether a confidentiality incident needs destructive remediation. For each, machinery produces a **focused question**: exact subject, scope and revisions; the distinctions already resolved; the evidence and its status; what the answer changes; the allowed outcomes. The answer is a recorded judgment that then propagates mechanically.

#### 32.2 Residual risks

- Semantic dependencies an agent uses without machinery observing them (§9.4).
- Circular reasoning stated only in prose (§2.5).
- Lost admitted history whose every copy, checkpoint and high-water mark is gone, with a stale product (§23.8); attestations that are wrong.
- Machinery cannot make an agent notice what it did not notice, or make a judgment good (§29.6); a formally consistent but lenient reader.
- A failure becomes stale mechanically only through runs that read the failing realization's pins and record its value for every recorded execution attribute, and never when it read an unpinnable input (§6.5-§6.6). Variation in an execution attribute no runner class records (a run-time CPU-kernel selection, or a host-mounted driver under a class that records only its image) is invisible to both predicates, so a failure caused by it can be made stale by a run that differs only there (§17.5); the same holds for randomness the runner does not supply and for scheduling nondeterminism, until a differing run on the same content is observed (§6.10). Runner classes that do not observe every read outside the tree support no mechanical stop at all; their failures, red-then-green iterations included, go to the owner (§17.5, SD-18).
- Bounded clone-tracking for moved-and-rewritten claims (§6.4); a move plus substantial rewrite escaping rename detection (§1.11); content moved out of the paths a `QUARANTINE` names (§18.4).
- Under §1.5, an LFS-tracked input is pointer text in the execution's tree; evidence that needs LFS data fetches the object as an observed, pinned external read, and a class that cannot observe such reads makes it unpinnable. Submodule commits are not kept reachable by this ledger (§21.4 covers this repository's commits), so a reproduction on `tree(a⁻)` can become impossible if the submodule's host drops the commit.
- A passing realization that read an unpinnable input, or ran under a class that does not observe reads outside the tree, stays current while its tree-resident entries hold (workplan §6.6); only its permissive uses for stopping a failure are excluded.
- A declared term that later comes to resolve to `ABSENT` changes identity but raises no specific finding unless it is a malformed anchor (§1.3, §1.9).
- Exact identity narrows adverse matching as well as permissive: a differing run on a tree that differs from `tree(a⁻)` only in line endings a text-mode reader translates, or in the mode of a file the execution never executes, is no longer `on⁻` `tree(a⁻)` and leaves (2), and a yielding run on such a variant of `G` leaves (4). This follows from one identity for both polarities and is bounded to representation-only differences for bounded bases (§1.5, §6.5). An unbounded basis's own `on⁻` matches only an identical tree, though `link⁻` still links it through narrower records; such bases serve no stop (§6.6).
- The write-set region test aligns bytes by the pinned line-wise diff (§7.2), so a D4 edit on a line shared with a D1-D3 symbol span (one-line C or C++ definitions, minified files) counts against the D1-D3 unit; this fails closed (§1.2).
- `link⁻` is fail-closed: a recorded basis that omitted content the execution actually read (a defective tracer, a wrong completeness judgment) links runs that differ there, so a genuinely fixed failure can keep counting until the owner disposes of it (§6.6).
- Under SD-23, incidental reads outside the tree (user caches, host configuration files, `/proc`) that differ between runs make them unmatched for (1) and (3), so such failures go to the owner; runner classes bound this by declaring host files as environment components and running with hermetic home and cache directories (§17.5).
- Late publication after a foreign return of the ref to exactly `B_n` (§22.3).
- Forgery by a holder of an Admission key or issue key; more than `f` faulty witnesses with control of the replica (§23).
- VM-level snapshot and resume of a running Admission process mid-publication-window (R4's incarnation model treats it as the same incarnation): outside the declared crash model.
- Joint validity of independently valid changes where no relation, invariant or evidence covers the interaction (§9.1).
- Independence is fixed at admission: an upheld challenge against a co-submitted attestation does not change a record's classification, so the correction is a challenge against the credited record itself. Broad `authors` sets fail closed: an observation of an unbounded realization has every author of the tree, a triple with absorbed bytes admits only a human with `NON_AUTHORSHIP_ATTESTATION` or the owner exception, and so does a transformation review whose judged scope retains content of unknown authorship (a drift re-dispatch after an absorbed change), while every retained unit adds its producers to the set its reviewers must be independent of, and because retained units are keyed on prose and fixed fields in any item or plan (SD-44) they include every same-key enactment's outputs, grow without bound and never drop a unit later enactments stopped touching, so some blocking challenges can be dismissed only by rerunning evidence or by the owner (measured in §31.9).
- A superseding judgment judges its exact target under its own basis context: if that context later reverts (a governing unit returns to the revision the superseded judgment was made under), a peer's earlier passing judgment on the same target can be current and unvetoed although no one re-judged it in that context; this agrees with targets being triples and with early cutoff (§5.5), and only a latch on vetoed judgments would close it.
- A cutover whose carrying integration is fenced or `OVERTAKEN` leaves the subject `NATIVE` on legacy bytes, invalid until the carrier is re-applied as a new enactment or a rollback `MODE_TRANSITION` is recorded (§19.5); a carrier that integrates before its cutover record needs another iteration for the cutover.
- One standing objection vetoes every judgment a contradicting composition needs, including compositions no consumer uses and judgments whose own basis is stale (R14): equivalence reuse on a unit can stop, and an `INCOMPLETE` on a scope widens every closure inside it, up to the whole tree, until its author, the owner or an upheld challenge ends it.
- A standing adverse judgment on a subject triple does not freeze re-scoping or promotion as an unresolved blocking challenge does (§8.3 step 4, §19.4): parts can be acceptable while the whole fails, so new subjects' acceptances are new targets it does not reach; their briefs show it only through the inspector's history.
- A transformation review's reach compares judged scopes (`J` of one containing the other's, SD-42), and the parts of one item share its prose and fixed fields, so a later part's `J` retains the earlier parts' integrated outputs and a partition whose parts integrate in sequence to exactly a rejected iteration's content is reached by its `NO_PASS` at the part that completes it, though not at the earlier parts; a part issued before an earlier part integrated is refused at integration as stale and re-issued (SD-44, SD-45); the item-level review of the integrated result (§13.7) and the unresolved findings carried into re-review briefs (§16.5) are the safeguards.
- `sat` hops keep their recorded direction (§4.4), so an independent equivalence recorded the other way, or judged before a revert for consumers on the other side, serves no path in that direction; a second judgment is needed.
- An acceptance or gate objection, and an objection to a relation among named units (`EQUIVALENCE`, `COMPLETENESS`, `INTAKE_DISPOSITION`, `PRODUCT_SCOPE_ACCEPTANCE`), does not reach a re-identification of its subject or units (S10: acceptance never transfers by content); it is carried as history into the next judge's brief only where a declared lineage links the identities, so a remove-and-redeclare without lineage leaves it to the inspector's history (§5.10 (a), §16.5).
- Two distinct plan items with byte-identical prose and fixed fields share one rejection's reach (SD-33), and a transformation review's veto reaches every review whose judged scope contains its own under any item (SD-34, SD-42), so a judgment about one vetoes the other until its author or the owner relieves it. A copy of an item into another plan together with an amendment of its prose or fixed fields is neither reached by a plan rejection nor carried into that plan's briefs.
- An amendment of a plan item's prose or fixed fields is a new target a standing rejection does not reach; the rejection is carried into the next acceptor's brief (§16.5), not enforced as a veto there. A control-only branch incomparable with a rejected revision is reached from the rejection's admission, even if the branches are never joined, until the rejecter or the owner relieves it (SD-32); and relieving an acceptance of `r` clears its coverage of every tightening of `r`, those it shares with the rejected revision included. Relief is admitted only while the relieved acceptance's basis holds; a vetoed acceptance that no longer covers the current revision blocks no work, but the adjudication it derives ends only by supersession of the rejection while its basis holds, or by an upheld challenge, which is then the only lift.
- A `NOT_EQUIVALENT` on a composite reaches no equivalence on its parts, and one on a part none on the composite: part and composite equivalences do not entail each other, so a record relying on every part of a composite can stay current around a standing objection to the composite's change.
- Every non-machinery `EQUIVALENCE` and `COMPLETENESS` needs an independent qualifier measured against the authors of the change or members it judges (SD-29), on both sides of an equivalence's change and including whoever re-produced the content by a revert or restore, so the author of the older content cannot qualify either, and one over content of unknown authorship (absorbed pushes, legacy imports, restores) needs a human with a `NON_AUTHORSHIP_ATTESTATION` or the owner exception; this includes a cutover's `MIGRATION` equivalence over legacy content (§19.5 condition 2) and completeness judgments on legacy scopes, and costs migration throughput (measured in §31.9).
- The 2026-10-12 governing-version adoption instruction remains paraphrase-only; only stakeholder restatement or recovered authentic evidence closes it.

#### 32.3 Reopen triggers

Reopen this architecture at its earliest affected owner if, on real repositories or live trajectories:

- conservative widening, part-to-subject routing or whole-tree execution-basis fallback make too much work non-current or too many promotions necessary to be useful;
- read recording proves infeasible across target harnesses, so bases are systematically too weak;
- whole-tree fallbacks (now the only alternative to a `COMPLETENESS(EXEC)` judgment) make passing evidence non-current too often, or too many failures are unbounded and so go to the owner (and, for D1/D2 claims, to the floor) because no analyzer or reviewer completeness judgment bounds their closure, or submodule hosts routinely drop commits that reproductions need; line-ending or mode churn on D1/D2 subjects routinely starts new revision runs needing revising reviews and human gates, or incidental external reads routinely prevent mechanical stops (§1.5, §6.5); most realizations run on classes that do not observe reads outside the tree, so most failures go to the owner; or failures caused by execution attributes no runner class records are made stale and later found live, or reproductions with the failing realization's recorded attributes are routinely unobtainable on the designated runners (§6.9, §17.5);
- keeping every system version and analyzer set that recorded execution bases name, so that recorded terms can be re-resolved (§5.9, §6.3), proves burdensome;
- adverse judgments routinely block work pending the owner's adjudication, or vetoes are used to stall work; a candidate-frame `REJECT` on a subject the candidate leaves unchanged vetoes in the admitted state while the candidate is pending and keeps vetoing after it is abandoned, until its author reassesses or the owner adjudicates (§5.10);
- gate terms accumulate members: every eligible passing decision stays in the minimum with its own evidence core, and only its author or the owner can supersede it, so items that repeatedly require an unchanged gate add decisions whose staleness lowers the term even while a fresh decision by another holder passes (§5.5); measure at G3 the number of eligible members per gate and the `REVALIDATE` work they generate;
- the acting rule (SD-25, SD-26) means a record in one pending candidate's frame supports nothing in another candidate's frame until that candidate integrates, and nothing from a rejected iteration's frame carries to the next iteration, so parallel candidates and replacement iterations realize, review, accept and gate again (§7.3, §7.6; the gate core shows identical-content decisions, §16.6); measure at G3 the human acceptance and gate work per integrated item;
- publisher crashes inside the publication window are frequent enough that fence-induced D1/D2 re-gating (R4) becomes a material share of human gate work;
- implementer obligations are not latched (SD-36, SD-40): an absorbed foreign change, or a later admitted item's change, to an integrated item's outputs, to what its implementer or reviewer read, or to its governing units, and an R1 tightening, make its obligation `OPEN`, and it is re-dispatched (§10.4, §8.6 drift); each re-dispatch is a new task, enactment and run, spending the item's iteration budget (after which it goes to `COORDINATE(plan)`), and may undo a later accepted item's change, bounded only by budgets; a pending candidate keeps its own routes; an earlier change's joint-invariant or specification review ends when a later one in the same scope is derived; every R1 tightening of an integrated item re-dispatches it, even one its content already meets, and an open peer veto of an integrated review re-dispatches the item beside its adjudication, spending budget even if the owner dismisses the veto; measure re-dispatch churn, read-only changes in particular; review independence is measured over the judged scope `J`, so a drift re-dispatch after an absorbed change, and a long-lived item's re-dispatches, may need a human reviewer (SD-42, §31.9); keyed on prose and fixed fields, retained units couple items: when another same-key item's or partition part's outputs move, every item retaining them is re-dispatched, two same-key items in different plans can drive each other's re-dispatches until their budgets are spent, a standing objection to an earlier part's content vetoes every later part's review until relieved, and an integration issued before a same-key sibling integrated is refused as stale (SD-44, SD-45);
- the obligation-routing residual accepted by a bounded stop (SD-41), each a named G2 reopen trigger for real-owner qualification (§31.5): (a) an item obligation's identity under an R2 amendment that leaves its prose and fixed fields unchanged (one reading keeps the obligation and its budget count, the other derives a new one with an empty `out(o)` and `subject(o)`); (b) a `COORDINATE(plan)` decision for a spent budget or an out-of-scope finding answered by an amendment that keeps the obligation's identity, after which the condition still holds and no route is derived; (c) an item-level review of a partitioned item whose findings name no part, which no obligation carries; (d) a pending candidate whose earlier iteration was rejected or ended `INCOMPLETE` or `PARTIAL`, which the list's route 3 does not end; (e) an out-of-scope NO-PASS on an integrated enactment other than the latest, which route 4 does not read, or of the latest one while a pending candidate's route 3 masks it, so no `COORDINATE(plan)` is derived for it (SD-43); reopen §10.4 at the first real-owner case that reaches one of them;
- unit declaration cost, the TOML manifest, the closed scope-term grammar or partition-by-construction rules outweigh their locality benefit, or prove unable to express real document and code structure;
- Git-hosted ledgers cannot meet single-ref compare-and-swap, durability, privacy, scale or hosting constraints;
- no practical independent witness set satisfying `q_a + r > N + f` exists for the target deployment class, or witness latency on the Admission path proves unacceptable;
- structural quarantine produces so much invalidity that intake cost outweighs its protection;
- simultaneous-definition groups prove so frequent or large that subjects become too coarse, or owners need a sound recursive-warrant exception the closed vocabulary cannot express;
- the confidentiality protocol proves operationally unrealizable;
- requalification after a loss boundary proves too costly, or continuity attestations become routine shortcuts;
- integration-head reconciliation proves unworkable on a target host, or fences (including those R4 causes after crashes) become frequent enough that fencing decisions burden the human routinely;
- the fixed predicate templates cannot express a required project policy without breaking stratification;
- a later accepted protocol version requires the ledger to be a canonical home for findings or tensions, or changes doctrine this Manual binds, until its inheritance reconciliation is done;
- agents still do bookkeeping; contract authoring and lint cost more than the verification they buy; write scopes are so narrow that amendment requests dominate coordination;
- `HARD` templates block legitimate work often enough to be amended away, or agents learn to satisfy checks while defeating their purpose;
- coordination becomes a bottleneck, or principal decisions are routinely overturned;
- human-attention volume exceeds what the inspector can sustain, or downgrades hide material findings;
- constructed independence proves illusory (common-mode failures dominate review misses);
- owner dispositions, human-routed adjudications, discriminating-reading obligations (one per genuinely new outcome per counted assessor-read failure) or reproductions become a material share of evidence work; discriminating observations prove routinely unobtainable (no declared outcomes, non-reproducing outcomes, low-bit variation under free attributes, unpinnable inputs, external runners without enumeration); retained trees and reproductions cost more than the dispositions they make cheap;
- failures of admitted obligations found in one lineage routinely delay other lineages, or scheduled executions routinely end `INCOMPLETE`;
- accepted relaxations of mechanical specifications routinely make failures stale unexamined; discriminating readings become a route for retiring concerns under edited readings; lenient readers pass outcomes that show the defect;
- residual owner dispositions (lineages dropping their own failing test-first checks, failures latched by transient foreign pushes) become frequent, or disagreement becomes routine;
- any inherited guarantee proves unpreservable.

#### 32.4 Open uncertainties

**Empirical** (§31.9 measures them; none is claimed): rate of false staleness; promotion frequency in Case B; analyzer completeness for real Python and C++ scientific code; read-recording feasibility per harness; practical granularity; derivation cost and checkpoint sizing; ledger growth over years; witness availability and latency; quarantine and SDG frequency; agent context and success against the baseline; contract authoring cost; template detection and false-positive rates; amendment, escalation and downgrade rates; human-attention load; fence frequency; whether doctrine realization on the 7.x panel improves over 7.2.1 on the behaviors that did not respond to text.

**Decision provenance**: the paraphrase-only 2026-10-12 adoption instruction (§32.2).

### 33. Non-goals

SSDS 8.0 does not: convert scientific reasoning or evidence into machine records or encode scientific truth in rules; provide a general rule or theorem language; require a graph database, network database, hosted service or distributed consensus; infer independence outside judged-complete scope; transfer acceptance by byte identity, scope arithmetic or widening; let agents write canonical state, let derived relations override source, or let D4 behavior create accepted D1-D3 authority; treat Git branches, commits or pull requests as workflow semantics; depend on server-negotiated multi-ref atomicity; assert currentness for state a witness quorum does not hold, claim rollback detection beyond the declared witness model, or claim that lineage migration erases leaked data; let repository presence, a foreign push, a restore or a merge change effective structure, ruleset or acceptance; reconstruct or guess lost admitted history, or let retained authority cross a known loss without requalification or accountable attestation; license a relation cycle by common subject identity, or let a definition or condensation warrant a claim; require every write to pass through an interface; expose machine records as routine agent UX; use search as an authority resolver; execute unknown artifacts to classify them; force all-at-once migration or stop valid production for incomplete migration; allow two current authorities over one subject; use migration as a hidden redesign channel; keep document-controlled workflow as a dual-current fallback for native scopes; add webhooks, brokers or hosted services before polling and local operation prove insufficient; add registries, wrappers or fields solely to mirror inherited doctrine (the realization map of §29 is a design artifact); treat a clean conformance view, a passing check or an agent's own claim as discharge of what a judgment must discharge; let a heuristic or prose-reading check block or pass work; let a contract carry executable check code, or an agent role edit templates, roles, routing or floors; let any agent role choose a decision's class, lower a report below a floor or discharge human attention; make a principal a long-lived process whose memory is workflow state; use a model judgment as a mechanical check; provide atomic admission across repositories; or provide a universal scientific observation database.

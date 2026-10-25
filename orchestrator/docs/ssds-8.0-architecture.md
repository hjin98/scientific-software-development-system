---
kind: architecture-manual
architecture_id: SSDS-ARCHITECTURE-MANUAL
manual_version: 1.0.0
status: accepted-current
protocol_version: 7.2.1
target_system_version: 8.0.0
governing_workplan: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
governing_workplan_design_revision: 24
phase_b_semantic_candidate: e23f14208be869e6a78cfd7b312e447254ee1851
phase_b_workplan_blob: 610f373b97fb8152d2a5742e17fa172e12204756
phase_b_review: qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md
phase_c_handoff: qualification/ssds80/PHASE-C-HANDOFF-SSDS-8.0.md
closure_map: qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md
mechanism_catalogue: orchestrator/docs/ssds-8.0-mechanism-catalogue.md
level: architecture (SD-47, stakeholder decision record item 43)
supersedes_on_acceptance: SDP-ORCHESTRATOR architecture 1.6.0, for SSDS-governed scopes only (§26.4)
gate: G1-accepted; G2-authorized (shadow only, SD-55)
amendment_a1: accepted (SD-51, SD-53; stakeholder decision record items 47, 49), §5.10 (f), (h)(4), §10.2, §10.3
amendment_a2: accepted (SD-52, SD-53; stakeholder decision record items 48, 49), §4.1, §10.4
amendment_a3: accepted (SD-53, stakeholder decision record item 49); restores §32.2 and §32.3 disclosures lost in the SD-47 condensation; no decision changes
amendments_a4_a6: accepted (SD-55, stakeholder decision record item 51) with the post-review corrections; A4 the §5.10 (e) cross-item owner (finding 913db8f N6); A5 and A6 the 2a17a83 Review's N1 and N2 (§32.2, §17.5, §32.3); no decision changes
accepted_at_g1: SD-50 (stakeholder decision record item 46), semantic candidate dddfedf72ed9711b8fcd46865b5c99eb50771ac5, blob b4077eb5879570b0aee56b068be8588beeaa5e9e
amendments_accepted: SD-53 (stakeholder decision record item 49), semantic candidate 2a17a8305db5ed312dc453f9d86ccf5faee8ab74, blob e90c1a4db68e9410e81eefafdcfcff92b888c57b; SD-55 (item 51), A4-A6 reviewed at afd3be2640b6a6e33a3d744efd76d324c6e5931a and accepted with corrections at cb468ecad19ba41715527b4de42d90262e02cf87, blob 0e304061b965eea8b124c9942f5c9aff4fa9a2d6; SD-60 (item 56), A7 and A8 confirmed by the Phase D Reviews 517af45 to 39fe39b and accepted, blob 6226f323365966bbcf653545f3a35b1fd7d6e060; SD-62 (item 58), A9 passed by the Phase E Review of 09f3505 and accepted, blob 25122b5e2bf0f5c7755afe0cc32161aa5a6215c4 (this header then updated to record it); SD-66 (item 62), A10 revision 2 passed by the different-family re-Review of 3a7a43d and accepted on proposal blob 3de6a9a219f5265a168223295acf95b301b17bbc against Manual blob fe43f04f5a698688727f7473a7c2e4d5345ae911, applied verbatim with these lifecycle lines
amendment_a7: accepted (SD-56, SD-57, SD-60; stakeholder decision record items 52-53, 56); the program is `ssds` and operator data lives in an SSDS home outside every repository (§0.5, §16.10, §21.5, §26.2-§26.4)
amendment_a8: accepted (SD-58, SD-60; stakeholder decision record items 54, 56); a bounding completeness judgment is checked on the content the run it bounds ran on (§6.5); resolves SERIOUS CHALLENGE SC-1 of the Phase D Review 0e49deb
amendment_a9: accepted (SD-61, SD-62; stakeholder decision record items 57, 58) after the different-family Phase E Review of 09f3505 passed it; `ssds.unclassified` mandatory at genesis and never removed, so every governed byte has an owner (§1.8, §1.9); resolves SERIOUS CHALLENGE SC-E1 of the Phase E step 4 review
amendment_a10: accepted (SD-63, SD-64, SD-65, SD-66; stakeholder decision record items 59-62) after the different-family re-Review of 3a7a43d passed it; project-memory occasions, derived memory facts and closeout learning (new §16.11 and its pointer edits)
d4: shadow-only (G2, SD-55); no SSDS authority over any subject before G4
active_serious_challenge: none
---

# SSDS 8 Architecture Manual

```text
STATUS: ACCEPTED-CURRENT at gate G1 (SD-50, 2026-10-18). Gate G2 authorized SSDS 8 D4 for shadow
        implementation only (SD-55, 2026-10-19): no SSDS authority over any subject before G4.
AMENDMENTS A1 (SD-51), A2 (SD-52) and A3: ACCEPTED (SD-53, 2026-10-18) on semantic candidate
          2a17a8305db5ed312dc453f9d86ccf5faee8ab74 after the independent D3 Review
          qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-2A17A83-A1A2A3-DIFFERENT-FAMILY-PASS.md: A1,
          eligibility per route and per state (§5.10 (f), (h)(4), §10.2, §10.3); A2, the identity key
          governing a loosening amendment (§4.1, §10.4); A3, residual-risk and reopen-trigger disclosures
          restored from the catalogue (§32.2, §32.3).
AMENDMENTS A4-A6: ACCEPTED (SD-55, 2026-10-19) after the independent D3 Review
          qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-AFD3BE2-DIFFERENT-FAMILY-PASS.md, with its
          non-blocking corrections at cb468ec: A4, the owner where a reach crosses items or plans
          (§5.10 (e)); A5, waiting with qualified independent people present (§32.2); A6, runner-attribute
          costs and two reopen triggers (§17.5, §32.3). No decision changes.
AMENDMENTS A7 and A8: ACCEPTED (SD-60, 2026-10-21) after the independent Phase D Reviews, which confirmed
          them from 517af45 to qualification/ssds80/PHASE-D-IMPLEMENTATION-REVIEW-SSDS-8.0-39FE39B-DIFFERENT-FAMILY-PASS.md.
          A7 (SD-56, SD-57): one program named `ssds` (distribution, import package and command; the `sdp`
          names retired, Level 0 Core as `ssds.core` with its behaviour unchanged) and one SSDS home for
          operator data outside every repository (§0.5, §16.10, §21.5, §26.2-§26.4); two §26.4 rows were
          corrected to it after the Phase D Review 0e49deb (finding B-B1). A8 (SD-58): a completeness
          judgment that bounds a run's basis is checked on the content that run ran on, not on the state
          of evaluation (§6.5), resolving SERIOUS CHALLENGE SC-1 of the Phase D Review 0e49deb.
AMENDMENT A9: ACCEPTED (SD-62, 2026-10-22) after the different-family Phase E Review
          qualification/ssds80/PHASE-E-IMPLEMENTATION-REVIEW-SSDS-8.0-09F3505-DIFFERENT-FAMILY-NO-PASS.md
          passed it (A9 PASS; the Phase E implementation was NO-PASS there): genesis declares
          `ssds.unclassified`, and no structure change removes it, so every governed byte has an owner and
          every change is in the effect-keyed write set (§1.8, §1.9), resolving SERIOUS CHALLENGE SC-E1 of
          the Phase E step 4 review (SD-61).
AMENDMENT A10: ACCEPTED (SD-66, 2026-10-25), revision 2, after the different-family re-Review
          qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-3A7A43D-A10-DIFFERENT-FAMILY-PASS.md passed it:
          Project Engineering Memory occasions, derived memory facts and closeout learning (new §16.11
          and its pointer and consequence edits), the re-derivation of SSDP 8.0 Amendment 1 items A, B, D
          and E (SD-63, SD-64, SD-65).
GOVERNING PROTOCOL: SSDP 7.2.1 (release identities owned by PROTOCOL-RELEASE-STATE.yaml)
TARGET: SSDS 8.0.0
BOUND TO: SSDS 8.0 workplan design revision 24 (revision 23's Phase B semantic candidate
          e23f14208be869e6a78cfd7b312e447254ee1851, workplan blob 610f373b97fb8152d2a5742e17fa172e12204756,
          independent Phase B D3 Review PASS, qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md;
          revision 24 is the stakeholder-directed level split, SD-47, judged a sound level assignment
          by the f044820 and 8c1f2f2 Reviews and accepted at G1, SD-50)
LEVEL: architecture. Mechanism is in orchestrator/docs/ssds-8.0-mechanism-catalogue.md, non-authoritative,
       carried to G2 (§0.1).
SERIOUS CHALLENGE: none
ACCEPTANCE: G1 accepted by the stakeholder (stakeholder decision record item 46, SD-50) on semantic
            candidate dddfedf72ed9711b8fcd46865b5c99eb50771ac5 after the independent D3 Review
            qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-DDDFEDF-DIFFERENT-FAMILY-PASS.md, with the §0.6
            defaults as proposed. Later commits change lifecycle lines only unless an accepted change says
            otherwise. No product-scope item is marked (§0.5); the mechanism catalogue is not accepted.
```

This Manual is the single owner of SSDS 8 durable architecture: the components and what each owns, the authority boundaries between them, the invariants every realization must keep, and the decision taken on each question the workplan's §21 leaves to it. When accepted it owns that architecture; until then it is a proposal and binds no implementation. The exact mechanism that realizes these decisions (syntax, schemas, field lists, algorithms, validation orders, route tables) is not here: it is in the mechanism catalogue, as proposed material that G2 accepts, replaces or drops against executable models (§0.1). The SSDS 8.0 workplan remains the cycle contract that produced this Manual; its rationale and review records are history, never proof of adequacy.

## Part 0. Orientation

### 0.1 Authority, binding and level

| Question | Answer |
|---|---|
| What does this Manual own once accepted? | Every material current architecture claim about SSDS 8 for SSDS-governed scopes: components and their ownership, authority boundaries, the invariants of §0.4 as realized here, and each §21 decision at the architecture level (workplan revision 24). Each such claim has exactly one statement here. |
| What does it not own? | Scientific meaning (D1), numerical-method meaning (D2), D4 specification and code, SSDP doctrine, project policy values, release identities (`PROTOCOL-RELEASE-STATE.yaml`), and the behavior of the frozen Level 0 Core for version-bound work (§26.4). Nor the exact mechanism: that is the catalogue's, as proposal. |
| What is the mechanism catalogue? | `orchestrator/docs/ssds-8.0-mechanism-catalogue.md`: the Manual candidate 61 text verbatim, which held the mechanism, under a front part with the **residual register** of open mechanism questions. It is non-authoritative and binds nothing. Catalogue §n realizes Manual §n. Where a catalogue clause disagrees with this Manual, this Manual governs and the disagreement is a register entry; the catalogue never supplies a second current meaning. G2's shadow workplan accepts, replaces or drops each catalogue mechanism against executable models and closes every register entry (workplan §25 criterion 13). It is not a D4 specification. |
| What does acceptance require? | G1: workplan §25 criteria 1-8, 11 and 12. Criterion 2 is this Manual resolving every §21 item at the architecture level; `qualification/ssds80/MANUAL-CLOSURE-MAP-SSDS-8.0.md` maps each item to its section. The map is not a second owner. |
| What is a G1 blocker? | A defect of the architecture (workplan §25 criterion 11): a contradiction among this Manual's components, ownership, authority boundaries or invariants; an invariant, inherited guarantee or §21 decision shown unrealizable or omitted; or a decision here that a conforming realization can satisfy while violating material upstream meaning. A counterexample to a catalogue mechanism that leaves these intact is a register entry, closed at G2 at the same no-blocker bar. Review count and recurrence never move a finding between the two (SD-47). |
| What does acceptance not do? | It authorizes no D4. Shadow implementation needs G2 (a reviewed shadow D3->D4 workplan derived from this Manual that settles the catalogue, and explicit stakeholder authorization). Runtime acceptance is G3; native authority over a subject is G4 for that subject. |

**Normative language.** "Must", "never" and "only" state architecture. A section marked **[D3 decision]** fixes a choice the workplan left to the Manual. A clause marked **[delegated]** names a choice left to D4 within the stated contract. Formulas in this Manual are definitions where they appear; their exact computation is the catalogue's. Examples are not normative.

**Decision status.** Every [D3 decision] is a proposal until G1. A **[proposed default]** is a parameter value the stakeholder may change at G1 or later through its owning lifecycle record without reopening the architecture; §0.6 lists them.

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

The Phase B Review passed workplan revision 23. The following decisions go beyond filling a delegated detail: each narrows or makes explicit a reviewed contract. Each is listed so that Review can check it rather than find it. The full statement, rationale and costs of each are in catalogue §0.3; the decision stands here.

| # | Reviewed contract (workplan) | Architecture decision |
|---|---|---|
| R1 | §6.6 `on` and the currency of a passing realization | A realization's execution basis is recorded once, at realization, with the context needed to re-resolve it, and every consumer reads that one record. Of the two matching predicates, the adverse one reads only tree-resident recorded content under the record's own context; every other dimension (external inputs, execution attributes the specification leaves free, the bounding of the basis) enters only the permissive one, so the permissive predicate implies the adverse one by construction and losing completeness or changing structure can only narrow permissive matches (SD-11 to SD-18, SD-23; §6.3, §6.5). |
| R2 | §6.6 support-graph cycle clause | Every non-trivial strongly connected component of the instantiated support graph is forced to `F` before any value is presented (§5.6). |
| R3 | §6.6 derivation over every authenticated prefix | An authenticated entry that violates the closed schema or the entry shape halts current assertion from that position until a human-gated recovery (`INTEGRITY_HALT`, §5.7). |
| R4 | §15.3 durable publication-attempt log | The publisher of an entry is the Admission process incarnation that appended it; only it may perform the publication, at most once; any restart, other process or host fences. No attempt log exists (§22.3). |
| R5 | §6.1 coverage partition checked at admission | Leaves partition governed content by construction for every tree; nothing is ever owned twice (§1.4). |
| R6 | §6.1 `scope_id` independent of bytes | Scope identity is the hash of the scope declared on the subject itself, so byte-preserving refinement keeps scope identity, revision and tenure (§1.5). |
| R7 | §6.2 `CHALLENGES` only as a record-level relation | An authored `CHALLENGES` relation lets an in-repository tension home bind its implicated authorities with inquiry status; it is evidential only and never a validity or warrant prerequisite (§2.2). |
| R8 | §6.8 step 3 supersession authority | Supersession authority follows the kind of the superseded record; no peer supersedes another actor's judgment; a transformation review's or plan acceptance's veto across targets is lifted per target by its author's or the owner's passing judgment of that target (§5.10, §8.3). |
| R9 | §7.4 discharge; the workflow owner's "no erasure by vote" | Every task ends in exactly one `TASK_RESULT`. A judgment obligation is answered by its first acting judgment and never dispatched again. A standing adverse judgment vetoes every passing judgment of its kind in its reach, whatever their order, until an independent route ends it; an answered obligation under such an objection is `REFUSED` (§5.10, §10.3-§10.4). |
| R10 | §2 S11, acceptance never revives | Across tenures no acceptance revives; within one tenure a subject that is not a `NATIVE` D1 or D2 subject reuses its acceptance by content identity, and a `NATIVE` D1/D2 subject's acceptance and gate decision are current only within the revision run in which they were made (SD-21, SD-22; §10.2). |
| R11 | §7.4 human gates | A gate `ACCEPT` requires adequacy; the gate term is the minimum over every eligible unsuperseded passing decision, a `QUALIFIED` one capped at provisional (SD-24; §5.5). |
| R12 | §6.9 frame records across iterations and rebases | The unit of enactment is one producing task's transformation with its clean rebases. A record acts only in its own enactment's frames and in admitted states after that enactment integrates; an enactment integrates at most once; re-application is a new enactment (SD-25, SD-26; §5.2, §7.6). |
| R13 | §5.3/§6.1 challenge tier; independence of dispositions | Every record that can end an objection or support a judgment carries the independence floor: a non-independent adjudication is refused; a non-independent judgment supports nothing. Independence is measured against the authors of what the record judged, by one rule (§5.10). The owner exception covers only an authenticated owner's disposition of a failing assessment, as the workplan states; elsewhere an author is never independent, and an obligation with no eligible judge waits on human attention (SD-48). |
| R14 | §6.6 `sat` path composition; closure by completeness | One reach rule: an adverse judgment vetoes every passing judgment of its kind that, alone or composed with others, claims what it denies; what is compared is what each judged, never the name under which it was judged (SD-28 to SD-34, SD-42; §5.10). |
| R15 | §6.8 step 8 collateral regression | Admission refuses only a request that makes another obligation's passing required evidence fail; discharge is current state, never latched; an obligation reopened by a later change takes the one route its state gives it (SD-36 to SD-41; §8.3, §10.4). |

Every other clause restates the reviewed contract or decides a §21 item inside it. The order in which refinements were made and which Review motivated each are in closure map §7; they are provenance. The stakeholder decisions SD-11 to SD-52 are cited where they apply; SD-47 (record item 43) made this Manual architecture-level and moved the mechanism to the catalogue.

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
  - *Within the requested deliverable (this architecture):* `ask`/`read` answers naming their qualified head (§16.2); task briefs with incompleteness notices (§16.3); gate briefs led by a separable non-narrative core (§16.6); the conformance view of each result (§14.6); the inspector view and digest (§16.8); historical views at any ledger position (§5.8); `ssds export`, a snapshot of the ledger and derived views at a named qualified head in canonical JSON (§26.3); the canonical-JSON ledger itself, readable with Git and a JSON reader without SSDS code or an AI (§21.2), which is the tool-independent route.
  - *Beyond the requested deliverable:* **None.** Projection of a project's own scientific records, exploration interfaces and discovery stores stay with project products. SSDS references their homes and adds no universal observation database.
- **Realized-record architecture.** Canonical source: the ledger plus the content it names. Derived projections: every view, regenerated, never edited (§5.8). Drill-down identity: record identity, unit identity plus revision, scope identity, ledger position and qualified head. Streaming and interim exposure: a long execution's progress is operator state; its realized outcome enters only as an admitted observation, and the inspector shows pending executions as pending. Restart continuity: the ledger and Git content; derived state rebuilds. Privacy and security: §24-§25; inspection and export views are trust boundaries that give the strongest safe aggregate and state the limitation.

### 0.6 Proposed defaults

| Parameter | Proposed default | Owner of a change | Section |
|---|---|---|---|
| derivation checkpoint interval | at least every 1,000 entries and at every lifecycle entry | ruleset adoption | §5.9 |
| Dispatcher-run execution time cap | 168 hours | system version | §6.9 |
| iteration budget per item | 3, system cap 10 | plan contract within the cap | §13.7 |
| mutation-testing threshold | 0.70 | contract parameter | §14.5 |
| `HARD` template qualification | detection Wilson 95% lower bound ≥ 0.95 over ≥ 200 seeded violations in ≥ 20 trajectories; false-positive upper bound ≤ 0.01 over ≥ 300 clean trajectories | ruleset adoption | §14.7 |
| cutover reconstruction minimum | `RECONSTRUCTED` for D1-D3, `PARTIAL` for D4 | policy | §19.5 |
| publisher takeover wait | 300 seconds | policy | §22.3 |
| high-entropy secret detection | ≥ 4.5 bits per character over tokens of ≥ 20 characters | policy, never lower than the system list | §24.1 |
| PEM match-path candidates per task | 10 | policy | §16.11 (d) *[Amendment A10, SD-63.]* |

## Part I. Primitives

### 1. Units, scopes, subjects and the manifest

#### 1.1 Unit

A **unit** `u` has a stable, opaque logical identity; a **kind**, which fixes its owning **domain** and the acceptance contract that applies; a **scope** (the repository regions it covers); a declaration source; and a **role**, leaf or composite. Every unit is either a **subject** (default) or a declared **part** of its enclosing composite. Identities are opaque, so no meaning is inferred from their text; the prefix `ssds.` is reserved for system units (§1.8) and a residual part (§1.4) has a derived identity no declaration may use.

**Kinds [D3 decision].**

| Kind | Domain | Meaning |
|---|---|---|
| `D1` | D1 | scientific/mathematical formulation |
| `D2` | D2 | algorithm and numerical method |
| `D3` | D3 | software architecture |
| `D4` | D4 | specification and implementation, including tests that are not evidence specifications |
| `EVIDENCE_SPEC` | the domain of the claims it `EVIDENCES` (§2.2) | an evidence specification |
| `EVIDENCE_RECORD` | none (non-authority) | an in-repository finding, tension or evidence home; never authority text (S13) |
| `PLAN` | plan | a change-plan unit (§11) |
| `GENERATED` | the domain of its generator | content reproduced by regeneration (§9.3) |
| `EXTERNAL` | external | an immutable external pin (§20) |
| `POLICY` | governance | the project policy unit; protected (§25.3) |
| `MANIFEST` | governance | the unit manifest; content edits are ordinary, effect only by admission |
| `UNCLASSIFIED` | none | content whose kind is not yet judged |

A subject's kind and domain are declared on the subject and its parts inherit them; a region that needs another domain is its own nested subject.

#### 1.2 The unit manifest

**[D3 decision]** Structural declarations live only in one repository-owned **unit manifest**, parsed by a data-only parser that never instantiates objects or executes content (T2). A manifest that does not parse is, for every declaration key, a quarantined delta against admitted structure (§1.6). Semantic declarations of a unit (its relations, defined objects, simultaneous-definition groups and joint invariants, §1.7) are part of that unit's revision; every other declaration is structural.

**Write set [D3 decision; SD-14].** A request's write set is keyed on **effect**, not on changed bytes or keys: it contains every effective unit, in either structure, whose owned content, declarations, resolved regions, membership or governance signature differs between the current observed tree and the request's merged tree, computed at the head where each check runs, so changes admitted concurrently never enter it and an effect that arises only when a change meets them does. Every write-scope check, the domain rule (§13.2) and every trigger keyed on a changed unit's kind or domain read this one set.

**Inline anchors.** An anchor only delimits a leaf span inside a file a manifest scope term names. It never declares role, membership, kind, domain or scope. Immutable or version-pinned artifacts are never rewritten to acquire anchors.

#### 1.3 Scope terms and resolution

**[D3 decision]** A unit's scope is an ordered list of terms from a closed grammar: a whole file, a path prefix, a Markdown heading span, a language symbol's source span, an anchor span, and a whole file inside a composite. Every term resolves as a pure function of file bytes under a pinned resolver, never reading host inputs. A term that does not resolve, or resolves ambiguously, yields `ABSENT`: a value, not an error, so a unit whose region vanishes changes revision and every reliance on it becomes non-current. The governed content of a tree is every tracked path not excluded by the effective `ignore` patterns.

#### 1.4 Partition by construction

**[D3 decision; refinement R5]** Leaves partition the governed content of every tree by construction, so no observed bytes can produce an overlap: siblings are statically disjoint by declaration; members lie inside their composite; each byte belongs to the innermost unit whose resolved region contains it; regions of units not nested by membership that coincide or partially overlap resolve to `ABSENT` with an integrity finding, in one pass that does not cascade; bytes of a composite no other unit owns belong to its implicit **residual part**; bytes no unit owns belong to the reserved **uncovered region**, `UNCLASSIFIED` (§18). Composites form a laminar family, because membership is a forest.

#### 1.5 Revision, content identity and scope identity

**Content identity [D3 decision].** Content identity is exact. Its one representation, for identity and for every comparison of owned content (write set, diff mapping, currency, matching), is the Git tree entry: type, mode and blob bytes, a gitlink's commit identity included. Every designated runner materializes exactly that representation, with no line-ending, filter or sparse-checkout transformation; content outside the tree (an LFS object, a file absent from the tree) is an external read. Exactly one normalization exists: an anchor line is removed where the system version's fixed comment classifier classifies it as a comment. Nothing else is normalized. A unit's revision hashes its content and its semantic declarations; `cur(u)` is its revision in the observed tree. A future normalization is a system-version change (§27).

**Scope identity [D3 decision; refinement R6].** `scope_id(s)` is the hash of the scope terms declared on the subject itself, independent of bytes and of how parts partition them; parts must partition exactly those terms. Byte-preserving refinement therefore keeps scope identity, revision and tenure; a change to the subject's own terms is a scope change and ends its tenure (§1.6).

Revisions are computed from Git content on demand and memoized by key; no separate hash graph is stored.

#### 1.6 Effective structure, quarantine and tenure

**Effective structure** `Σ_n` is the structure in force at ledger position `n`: genesis admits it; an ordinary or intake admission changes it exactly by the structural changes it authored or explicitly adopted; an absorption never changes it. It is a fold over admitted entries, never a second stored copy. Units, leaves, composites, residual parts, `scope_id`, `subj` (the nearest enclosing subject), kind, domain, governed boundary and tenure derive from it, resolved against the observed bytes.

- **Quarantine** `Q_n` is the set of declaration keys whose observed value differs from `Σ_n`.
- **Governance-affecting classification [D3 decision].** A quarantined delta is governance-affecting iff applying it alone would change some unit's identity, kind, domain, role or enclosing composite, some subject's scope identity or covered regions, or the governed boundary; otherwise it is governance-neutral (a re-partition inside one subject's unchanged regions). The classification is fixed by the system version, never by policy. `aff(Q_n)` is every subject the quarantined deltas together would affect.
- **Tenure.** A subject's governance signature is its role, scope identity, kind/domain and governance mode. Its tenure is the current uninterrupted run with an unchanged signature; demotion, a scope change, a kind or domain change or a mode change ends it, and a restoration starts a new one. Acceptance belongs to a tenure; challenges, revocations and supersessions target exact triples and records and survive tenure changes.

**Content proposes; admitted records enact.** Acceptance, governance mode, reconstruction status, lifecycle and effective structure are derived from records, never from fields in unit content.

#### 1.7 Semantic declarations

Semantic declarations are authored relations (§2), defined-object declarations, simultaneous-definition group declarations (§2.4) and joint-invariant declarations (§9.2), written in the manifest's table for the unit or inline in its regions. Inline markers are content and change the unit's revision. **Single definer:** two current units defining the same object name are both ill-formed until the owner removes one declaration.

#### 1.8 System units and genesis structure

Genesis declares the reserved leaves `ssds.manifest`, `ssds.policy` (protected, §25.3) and `ssds.unclassified`, the outermost owner of every governed byte no other top-level unit contains, so that the uncovered region is empty: every change then lies in some effective unit, so the effect-keyed write set (§1.2), the write-scope boundary (§14.3), Admission's proof (§8.3) and derived impact (§5.8) see it. A genesis whose structure does not declare `ssds.unclassified` with the empty prefix is refused. *[Amendment A9, SD-61.]* An item that may write content no other unit owns names that content in its write scope (§13.1).

#### 1.9 Static structural checks

Every admission checks the merged tree's structure (§8.3 step 4), and the checks define part of `well_formed` (§2.5): identity grammar and uniqueness; kind present on subjects and absent on parts; membership a forest; sibling disjointness and containment; scope conservation for a refinement; every term well formed and resolved by a pure resolver; every newly declared or changed file or span term resolving at its admission; no `renamed_from` cycle; residual identities never declared; the reserved leaves of §1.8 declared, `ssds.unclassified` with the empty prefix (*Amendment A9, SD-61*).

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

The 7.2.1 tension search keys (owner/path plus heading, anchor or object ID; exact revision; claim locator; earlier revisions; former names or paths; recorded predecessors) resolve onto unit identity, revision history, `renamed_from` lineage as a fold over admitted structure (a removed declaration never removes admitted lineage), Git rename history and `SUPERSEDES`/`REPLACES` relations, through `ask(locate)` (§16.2). A tension home binds every implicated authority by unit identity. A move plus substantial rewriting that neither lineage nor rename detection reveals is a stated limitation.

### 2. Relations

#### 2.1 Relation and provenance class

A **relation** is `(subject, type, object, class, provenance)`, stored in the direction subject -> prerequisite; reverse traversal is impact analysis, never a second relation. **Authored** relations are semantic declarations inside the subject's scope, part of every enclosing subject's revision, changed only by changing content. **Derived** relations are computed by a pinned analyzer and cached, never edited, never canonical. **Proposed** relations are records that take effect only through an admitted content change. **Record-level** relations (challenge targets, adjudication, supersession) are fields of records, never edits to their targets.

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

A ruleset adoption (§27.1) is rejected unless every type has every attribute, `SIMULTANEOUS` appears only on `DEFINITIONAL` types and `NEUTRAL` only on derived `STRUCTURAL` types, no rule names a `NEUTRAL` type, `CHALLENGES` or `EVIDENCES` as a validity or warrant prerequisite, and every layer constraint has a closed form. Removing, renaming or reclassifying a type declares how existing uses are read, migrated or rejected, and the adoption gate is shown the subjects that would become ill-formed. A type absent from the ruleset has unknown required semantics and fails closed.

#### 2.4 Simultaneous-definition groups and cycle legality

A **simultaneous-definition group** (SDG) names units whose meanings are defined together; it is part of its subject's revision, its members share one subject, and SDGs are laminar. **Cycle legality:** every cycle among authored relations other than `CHALLENGES`, and derived relations that are not `NEUTRAL`, must lie inside one SDG and use only `SIMULTANEOUS` edges. Contracting each SDG yields the acyclic order used for layers, ordering and impact; the contraction is a representation, never a warrant. Code recursion is derived, `NEUTRAL`, legal and never warrant.

#### 2.5 Well-formedness

`well_formed(s)` (S0) is false when a unit of `s` fails a static structural check, lies on an illegal cycle, carries an authored relation of an unknown type or one violating its layer or subject-kind constraint, belongs to a malformed SDG, or conflicts under the single-definer rule. Admission rejects a request that would make an affected subject ill-formed; a violation that reaches the tree otherwise makes the subject invalid in S2. Machinery checks declared relations only; circular reasoning stated only in prose is for review and Challenge.

#### 2.6 Completeness

`COMPLETENESS(X, R)` asserts that every `R`-prerequisite of a unit in scope `X` lying outside `X` is declared (boundary completeness). It relies on the content of `X`'s members and on `X`'s membership, so adding, removing or editing a member makes it non-current, and it never transfers through refinement or scope change. **Analyzer completeness declarations [D3 decision].** An analyzer version declares, per language and configuration, the constructs for which its derived relations are complete and the incompleteness markers it detects; it supplies boundary completeness only for a scope in which it found no marker, as an ordinary machinery `COMPLETENESS` record that is current only while its content holds and its analyzer is pinned, and challengeable like any judgment. A marker never overrides a qualified actor's judgment, and observed reads never bound a closure.

### 3. Records and the ledger schema

#### 3.1 The ledger

The **ledger** is the single canonical store of everything not derivable from content: append-only, totally ordered, authenticated (§23.2), in one closed versioned schema, written only by Admission. An entry is provisional when appended and admitted when a witness quorum holds its head (§22); whether a record is current is derived (§5.5). Rejections and refusals are recorded. Purely operational facts (task issue, leases, launches, retries) live in the Dispatcher's private operator journal under intent -> effect -> observed outcome (C4) and never enter derived workflow state.

#### 3.2 Common record envelope [D3 decision]

Every record is a canonical JSON object with no free-text fields (C7): identifiers in declared grammars, enumerations, digests, integers, booleans, informational timestamps, validated paths and content references. Every record carries its identity (a digest of its content), kind, schema version, the ruleset in force when submitted, actor and actor class, the frame it is evaluated in (§7), its target, basis (§4), outcome, enumerated reasons, explicit supersessions, its task binding (§12.2), the governing version it declares (§16.9), execution provenance, and content references to narrative homes, evaluated outcomes and artifacts. Derivation reads only ledger-stored objects; every other reference is for drill-down and binding health.

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

The closed kinds are, by tier: **support** — `ACCEPTANCE`, `REVIEW`, `CONFORMANCE`, `EQUIVALENCE`, `COMPLETENESS`, `EVIDENCE_ASSESSMENT`, `IMMATERIALITY`, `PLAN_ACCEPTANCE`, `INTAKE_CLASSIFICATION`, `INTAKE_DISPOSITION`, `LEGACY_ACCEPTANCE`, `EXTERNAL_ACCEPTANCE`, `RECONSTRUCTION_PROPOSAL`, `TASK_RESULT`, the reports `FINDING`, `AMENDMENT_REQUEST`, `BLOCKER`, `HUMAN_QUESTION`, and `COORDINATION_DECISION`, `MATERIALITY_RECLASSIFICATION`, `HUMAN_DECISION`, `GATE_DECISION`, `PRODUCT_SCOPE_ACCEPTANCE`, `LINEAGE_ATTESTATION`, `NON_AUTHORSHIP_ATTESTATION`; **challenge** — `CHALLENGE`, `ADJUDICATION`, `WITHDRAWAL`, `RISK_OVERRIDE`, `CONTINUITY_ATTESTATION`; **observation** — `REALIZATION`, `CHECK_EXECUTION`, `EXTERNAL_CONSULTATION`, `ANALYZER_OUTPUT`, `AVAILABILITY`, `CUSTODY_ENUMERATION`; **admission** — `ADMISSION`, `ABSORPTION`; **lifecycle** — `GENESIS`, `RULESET_ADOPTION`, `SCHEMA_MIGRATION`, `MODE_TRANSITION`, `LEGACY_RELEASE`, `KEY_LIFECYCLE`, `TRUST_MECHANISM_CHANGE`, `PROJECT_FORK`, `REPLICA_REDESIGNATION`, `WITNESS_SET_REDESIGNATION`, `LEDGER_LOSS`, `FORK_RESOLUTION`, `LINEAGE_MIGRATION`, `LINEAGE_RETIREMENT`, `REDACTION_NOTICE`. Each kind fixes its target type, outcome vocabulary, producer class and treatment after a loss boundary.

A support-tier record's **target** is the exact thing it judges, so supersession on the same target never reaches content the superseder did not judge; a `GATE_DECISION` is superseded on its gate and subject triple in any run. The frame a record declares is where it resolves, not part of its target. An adverse outcome keeps its veto across a loss boundary, because adversity follows existence (§5.10).

**Review targets [D3 decision; SD-47, closing the 9431629 N2 target route].** A `REVIEW` targets exactly one of three things, each its own target type with its own identity:

1. a **transformation** `id(X)` (§7.1): the review of one candidate change, answering `REVIEW(X)`; a `CONFORMANCE` judgment targets the same transformation together with the contract item revision;
2. a **subject triple** `(s, scope_id, rev)`: a review of a subject revision, among them the revising review of a `NATIVE` D1/D2 revision (§10.2);
3. an **integrated result**: of a partitioned item revision (the item-level review, §13.7), of a joint invariant's scope after the change that derived it (§9.2), or of a marked high-consequence surface after the change that derived it. Its identity names its kind, the item revision, invariant or surface, and the admitted state it judges, so it never coincides with a transformation's own review of the same change.

Each obligation that a review answers names its target type (§10.2), and the reach of a review's objection, its relief and its independence are stated per target type in §5.10.

#### 3.5 Actor qualifications

Project policy (§25.3) maps each judgment kind, target domain and outcome to a required actor class and qualification, above system floors it may raise and never lower. An authenticated human is required for D1 and D2 `ACCEPTANCE`, every `GATE_DECISION`, `RISK_OVERRIDE`, Serious Challenge adjudication, an adjudication in a chain containing an R3 human record, `CONTINUITY_ATTESTATION`, `PRODUCT_SCOPE_ACCEPTANCE`, `HUMAN_DECISION`, the two attestation kinds and every lifecycle record. A marked product surface is accepted only by the stakeholder or task authority policy designates (or a D1/D2 gate holder whose core showed it, as their own co-submitted record); technical D3 review never accepts it (S12). No actor reviews, accepts, conforms or plan-accepts its own work (A5; §5.10).

#### 3.6 Compatibility contract [D3 decision]

The schema is closed: Admission rejects an unknown kind or field, a missing required field or a value outside its grammar (C5). A system version declares the ledger schema versions it reads; an entry of an unreadable version ends current assertion at that position without being an integrity defect. Any change to a kind, field or enumeration is a new schema version adopted by `SCHEMA_MIGRATION` (§27.2), and no record is re-adjudicated under a newer schema or ruleset (P2).

### 4. Basis

#### 4.1 Basis entries and modes

A **basis entry** is `(mode, target, consumption class, role)`, its mode fixed at admission by the rule for the record's kind and never inferred at evaluation. The modes are: `content` (the exact revision, or one reached by an equivalence path for the entry's consumption class, or by the control-tightening order for plan control); `validity` (the content condition and the validity of the prerequisite's subject, for direct governing or warrant prerequisites in another subject only); `execution` (a realization's recorded execution basis, §6.3); `record` (the named record is current); `standing` (the named record stands, whatever its own basis); and `identity` (always satisfied; for targets of challenge-tier records, supersessions, dispositions and records shown but not relied on).

**A dependence states what it relies on [D3 decision; stakeholder record item 31].** A `record` entry imports the named record's currency, a `standing` entry only that it stands, an `identity` entry only that it exists; each entry takes the mode its depender's conclusion needs. Every `record` entry has a route when it fails (a wider closure, a rerun or reading, a revalidation of a pending candidate's result, a new obligation after an amendment of the prose or fixed fields, a new plan acceptance after one that only loosens a tightenable field), and no obligation is ready whose answer's mechanical minimum cannot hold without one of these routes being derived (§10.3).

**Subject boundary.** A prerequisite in another subject gets a `validity` entry where validity is required; one in the record's own subject gets a `content` entry. A record never holds a `validity` entry on its own subject, so no acceptance supports itself and warrant stays acyclic.

#### 4.2 Composition

A record's basis is the union of the mechanical minimum for its kind (§4.3), every recorded read during its task (§16.4), and declared reliance the actor adds. An actor can add to the mechanical minimum, never remove from it. An unpinnable read is recorded as such and keeps the record out of every permissive comparison of executed content (§6.5).

#### 4.3 Mechanical minimum per kind [D3 decision]

Every kind has a fixed mechanical minimum. Its principles: the target is read exactly; governing and warrant prerequisites are read across subjects by validity and the governing closure as context; a judgment about work carries a `content` entry on every unit of its judged content (§5.10); a judgment relies, in `record` mode, only on the premises its conclusion needs to hold now, and records it was shown but does not rely on (earlier runs, history, adverse records, challenges) in `identity` mode, since being shown is not being relied on (stakeholder record item 31); an acceptance or gate decision on a `NATIVE` D1/D2 revision carries a `standing` entry on the revision-assessment record it relies on (§10.2); reports and challenges carry provenance only, never consumed. The per-kind table is catalogue §4.3.

#### 4.4 Consumption classes and equivalence paths [D3 decision]

Consumption classes are `EXACT` (no equivalence coverage), `EDITORIAL`, `REPRESENTATION`, `MIGRATION`, `CONSUMER:<kind>` and `PLAN_CONTROL` (the control-tightening order, §13.4, which is an order, never a sameness claim). An `EQUIVALENCE` covers an entry of its own class, and editorial and representation equivalences cover every consumer class. A `content` entry is satisfied through a path of current, unvetoed equivalence judgments of covering classes from the recorded revision to the current one, each hop in its recorded direction; a hop under a standing objection is not current, so no path counts through it (§5.10). The author of a change can never be the sole qualifier of an equivalence or completeness judgment about it.

#### 4.5 Conservative widening

Widening addresses dependency uncertainty only and never establishes equivalence, completeness or acceptance. A unit's enclosing-scope chain, built from admitted structure only, runs from the unit through each enclosing composite and each ancestor directory to the whole governed tree plus the uncovered region.

#### 4.6 Closure

`closure(S, R)` is the least fixed point of following declared and derived `R`-prerequisites and, for each reached unit, adding the smallest scope of its chain that a current `COMPLETE` judgment bounds for every class in `R`, or the whole governed tree, marked `UNBOUNDED`, where none does. Exact closure needs a current singleton completeness judgment on every reached unit. Missing dependency knowledge never proves independence (S5).

## Part II. Derivation

### 5. The derivation and its strata

#### 5.1 Function

```text
derive(L_n, content of the trees L_n names) -> exactly one derived state D_n
```

`L_n` is the authenticated ledger prefix through position `n`; the ruleset and effective structure are read from it, and nothing is supplied from outside. Derivation is a pure function. Which prefix may be presented as current is decided outside it, by currentness qualification (§23), so witness reads, live refs, wall clock, operator state and search indexes never enter `D_n`. A transformation frame `D_n[X]` is the same function over a hypothetical tree and structure fixed by `id(X)` (§7). Four strata, each reading only lower strata, recursion only inside S1 and S2 in forms proved unique (§5.3, §5.6).

**Fixed predicate templates.** The SSDS system version fixes every derivation predicate. Project policy only parameterizes them (judgment kinds and passing outcomes, qualifications above the floors, additions to mechanical minima, required judgments, gates and evidence per domain, triggers, the project-memory root (§16.11), routing and raised floors, role narrowing, enabled templates, budgets and time bounds). *[Amendment A10, SD-63.]* There is no rule language and no executable policy. **[D3 decision]** A ruleset adoption is rejected if any parameter would make a stratum read a stratum at or above it, or polarity depend on anything but kind, outcome and target; every template declares its stratum, and the check compares declared strata, never policy text.

#### 5.2 S0 — observed content, effective structure and ledger syntax

S0 is the ruleset in force; the expected integration head and the observed tree; the publication classification (§22.2); loss boundaries; effective structure, quarantine, revisions, relations and well-formedness (§1-§2); record syntax, target conditions and supersession; and the adverse-scope facts of failing assessments (§6.4). S0 never reads a derived acceptance or validity; the policy unit and structural declarations take effect only through admitted records.

**Acting records [D3 decision; SD-25, SD-26; refinement R12].** Every S0, S2 and S3 rule is evaluated in one **state**: the admitted state or a frame `D_n[X]` (§7). The **enactment** of a transformation is that transformation with its clean machinery rebases: the transformations of one producing task. A later iteration, a partition part and a re-dispatch are new tasks and so new enactments. An admitted record **acts** in a state iff it declares the admitted frame, or a frame of an enactment that has integrated, or the frame of the state's own enactment. This is the one rule for which records a state reads permissively: support, withdrawal, relief of a veto, disposition, gate eligibility, answering and run membership read only acting records. Adverse records are outside it: an adverse judgment vetoes in every state (§5.10), and a failing assessment counts wherever §6.4 puts it. Acting is monotone along admitted history, and a record of an enactment that never integrates never acts in an admitted state.

#### 5.3 S1 — challenge tier

Challenge-tier polarity is syntactic, by kind, outcome and target: an upheld adjudication of an ordinary challenge is restrictive (a revocation); a challenge of a restrictive adjudication is a counter-challenge; withdrawals, risk overrides, continuity attestations, dismissals and upholdings of counter-challenges are relaxers. Every target is strictly earlier, so polarity, force and continuity are a recursion on strictly increasing positions with exactly one value, although negation appears. A subject triple's S1 status is `REVOKED`, `BLOCKED`, `PROVISIONAL` (blocked but risk-overridden) or `CLEAR`. Effects are conservative in both directions: an open blocking challenge suspends any relaxer it targets, an upheld one removes its force permanently, and repair of a revoked triple needs a new revision or a successful challenge of the upholding. **Loss boundary.** A record before an admitted `LEDGER_LOSS` has no permissive effect after it unless an in-force continuity attestation holds it (`cont`); restrictive records, supersessions and S0 facts are not gated (§23.6). Challenge-tier targets carry no tenure, so a challenge on a triple binds every tenure in which the triple recurs.

#### 5.4 Record polarity summary (every kind)

Support-tier judgments support through currency and are withheld after a loss boundary until requalified or held; reports and coordination records create S3 obligations keyed on existence; failing assessments and adverse judgments object by existence and survive a loss boundary; dispositions (a supersession, an upheld adjudication, an `IMMATERIALITY`) are permissive and withheld as dispositions after a boundary while their other effects survive; challenge-tier records act through S1 polarity; observations are premises and staleness evidence, their permissive use withheld after a boundary; admission entries, structure and trees are S0 constants; lifecycle records are S0 constants as a `LEDGER_LOSS` re-establishes them. Catalogue §5.4 tabulates every kind.

#### 5.5 S2 — support tier

Values lie in the lattice `F < P < T` (non-current/invalid < provisional < current/valid). A record's **base** is `F` unless it acts, is not superseded, is neither revoked nor blocked, holds across loss boundaries, meets its target condition, is not vetoed and is not non-independent (§5.10); it is `P` if provisional. A record is **current** when its base and every basis entry are satisfied in the state. A subject is **valid** when its triple stands, it is well formed and unquarantined, and some acceptance on its exact current triple in its tenure is current together with every required judgment kind, every required human gate's term and every required evidence obligation; a counting, undisposed failing assessment about it caps its validity at `P` (§6), whether or not that obligation is still required.

**Gate term [D3 decision; SD-24, SD-25; refinement R11].** A required gate's term is the minimum over every eligible, unsuperseded passing `GATE_DECISION` acting in the state, each capped at `P` when `QUALIFIED`, and `F` when none is eligible. No order of admission or integration decides between holders or frames, and a qualification lifts only when its own decision is superseded by its author or the owner. A holder who accepts with a stated limitation lets work continue only visibly provisionally, and only where policy permits provisional continuation.

**Evidence.** An evidence obligation holds when a current passing admissible assessment exists and every counting failing assessment is disposed of, a live disagreement capping it at `P` (§6).
**Supersession and risk override.** A record superseded in a state never becomes current again there. A risk override never resolves a challenge: it turns `BLOCKED` into `PROVISIONAL`, and `P` propagates by minimum (§10.5). **Early cutoff.** When an upstream subject changes and a re-review of a dependent passes without changing it, every record that named the dependent's unchanged revision and did not itself see the upstream text is current again with no further work. Machinery decides only byte identity and the one normalization; every other sameness is an `EQUIVALENCE` judgment.

#### 5.6 Uniqueness and support cycles [refinement R2]

S2 is monotone on a finite lattice: S0 and S1 facts, base and vetoes are constants, disposition currency enters only positively, and staleness reads bounding completeness only positively (its standing, and the currency of the records it cites, A8). It therefore has exactly one least fixed point. Before evaluation, every non-trivial strongly connected component of the instantiated static support graph is forced to `F`, with one finding per component (an integrity obligation unless the cycle arose through absorbed content), so no acceptance can support itself and a cycle is never presented at `P` or `T`. Admission keeps the support graph acyclic (§8.3 step 5).

#### 5.7 Corrupt prefixes [refinement R3]

The Ledger Store rejects an unauthenticated chain before derivation runs (§23.2). An authenticated entry that violates the closed schema, the entry-shape rule or a kind's syntactic constraints puts every position at or after it into **`INTEGRITY_HALT`**: earlier positions stay available as historical views, no current assertion is made, Admission appends only a human-gated recovery record abandoning the chain from that entry, and a `CRITICAL` integrity obligation is raised. An unreadable schema version is not corruption (§3.6).

#### 5.8 S3 — consequence tier and views

S3 holds the non-monotone functions nothing below reads: obligations (including intake of each quarantined delta, re-application of overtaken admissions and requalification after a loss boundary), discharge, readiness, blockers, drift, impact sets, context answers, briefs, conformance, routing, escalation, coordination and decision classes, views and integrity findings. S3 explains and schedules quarantine and ill-formedness; S2 already enforced them. **Historical views** derive at any earlier position with the ruleset in force there and claim no currentness.

#### 5.9 Determinism, analyzers, caching and checkpoints

For every authenticated input, S0 is a function, S1 a well-founded recursion, S2 the unique least fixed point with the clamp, and S3 a function, in the admitted state and every frame (C2, C3, C8). **Analyzer pinning [D3 decision].** Derivation at a position runs exactly the analyzer set its ruleset pins, never what a host has installed; a host that lacks a required analyzer or system version makes no current assertion. Nondeterministic, expensive or host-dependent analyzer output is recorded as an observation and replayed. Changing the analyzer set is a human-gated ruleset adoption shown its re-acceptance burden. **Caching** is keyed by inputs, and incremental derivation must equal from-scratch derivation. **Checkpoints [D3 decision].** A derivation checkpoint caches derived state under a key recomputed from the ledger before use, carries no currentness, and bounds restart replay (§0.6).

#### 5.10 Judgment disagreement [D3 decision; owner; refinements R8, R9, R12, R13, R14; SD-24 to SD-35, SD-41 to SD-49, SD-51]

This section is the **one owner** of judgment disagreement: which outcomes object, what each judgment judged, how far an objection reaches, what ends it and who may end it, how independence is measured, and what follows in S3. Every other section that touches these rules points here; where one restates a consequence, this section governs. Failing evidence assessments keep §6 for start, adverse scope, matching and staleness; their dispositions and the independence of those dispositions are governed here.

**(a) Adverse outcomes.** `ACCEPTANCE` `FAIL`, `REVIEW` `NO_PASS`, `CONFORMANCE` `NONCONFORMANT`, `PLAN_ACCEPTANCE` `REJECTED`, `EQUIVALENCE` `NOT_EQUIVALENT`, `COMPLETENESS` `INCOMPLETE`, `GATE_DECISION` `REJECT`, `PRODUCT_SCOPE_ACCEPTANCE` `REJECTED`, and every `INTAKE_DISPOSITION` other than `ABSORB`; a failing `EVIDENCE_ASSESSMENT` is adverse under §6.

**(b) Judged content: one provenance rule [D3 decision; SD-47 (A)].** Every judgment judges a definite body of content, its **judged content** `W(j)`, and every rule here that asks what a judgment judged reads that one set: how far an objection reaches, which target a relief exempts, and whom a judge must be independent of. No kind has a second definition.

- A judgment about **work** — a transformation's `REVIEW` or `CONFORMANCE`, an item-level review, a joint-invariant or high-consequence review (§3.4 target types 1 and 3) — judges the content, in the state its target fixes, of every unit inside its target's scope that the work has changed. The **work** of a transformation, or of an item revision, is every integrated enactment for an item revision with the same prose and fixed fields (§13.4), in any part, plan or partition, together with the transformation's own change; the work of a joint-invariant or high-consequence review is the change that derived it. The **state** is the candidate's merged tree for a transformation, the item revision's integrated result for an item-level review, and the integrated result after the deriving change for a joint-invariant or high-consequence review. The **scope** is the task's write scope, the item revision's write scope, or the invariant's declared units or the marked surface.
- A judgment about a **subject or named units** judges what it names: an acceptance, a subject-triple review or a gate decision, the subject revision's content (by S10 these stay on their subject triple and never transfer by content); an `EQUIVALENCE`, the content that differs between its two endpoints, on either side; a `COMPLETENESS`, its members' content at their revisions; an assessment, its claim content; a disposition, the claim content of the assessments it covers; a plan acceptance, the prose and fixed fields of the item revisions it names; a revision assessment, the assessed revision; an intake disposition or product-scope acceptance, the delta or surface it names.
- The **authors** of `W(j)` are the actors whose admitted records produced each piece of it at its revision (a revert, restore or re-application that re-produced it included), and are unknown where any piece has no admitted producing record (absorbed pushes, legacy imports, restores, manual merges). Authorship is a ledger fact, read the same way by every rule.

So an output kept by an empty or partial re-dispatch, by a part a re-partition replaced, or by an item copied under the same prose and fixed fields stays judged with its producer; content the work changed and someone later replaced is judged at its current content, with its current producer; content in the scope that the work never changed (another item's output, legacy content) is not judged as this work and does not widen its authors. A change of the item's prose or fixed fields starts new work, whose judged content holds only what that work changes (§32.2).

`W(j)` is fixed by `j`'s target: for a transformation it is a fact of `id(X)`, which names the base and the candidate, so every judgment of one transformation judges the same content whenever it is admitted. A judgment supports an integration only for the content it judged: where the content the integrated state gives the same work in the same scope differs from `W` of the judged target, the judgment does not support that integration, and the item takes a new iteration (realized by the catalogue's rebase staleness and `STALE_RETAINED` refusal, register RR-2).

**(c) Reach** (one rule; R14, SD-29). An adverse judgment `j⁻` objects, in a state, to every passing judgment `z` of its kind for which some set of judgments of that kind asserting in that state, together with `z`, claims what `j⁻` denies, while that set alone does not. What passing judgments claim:

| Kind | What passing judgments claim, alone or composed | Per-target relief | Passing aggregation |
|---|---|---|---|
| judgments about work (`REVIEW` of a transformation or an integrated result, `CONFORMANCE`) | each judges its `W`: `z` is reached when `W(z)` contains `W(j⁻)` at the same content, under any item, revision or plan, and `W(j⁻)` is nonempty; an empty `W(j⁻)` reaches only its own target. A re-dispatch keeping rejected content is reached; one that changes it, or a review of unrelated content, is not | the adverse judgment's author's or the owner's independent passing judgment on that exact target | ∃ (§10.4) |
| `ACCEPTANCE`, `REVIEW` of a subject triple | the same triple, in any frame or tenure | — | ∃ over the subject's acceptances (§5.5) |
| `PLAN_ACCEPTANCE` | a rejection of item revision `r*` denies `r*` and every tighter revision; an acceptance of `r` claims `r` and every tighter revision; they contradict exactly when `r` and `r*` have the same prose and fixed fields, in any item or plan; the current revision is not read; acceptances do not compose. This is a conservative resolution policy, not a claim about the rejection's ground | the rejecter's or the owner's independent passing acceptance on that exact target (SD-30); relieving an acceptance clears its coverage of every tightening of its revision | ∃ over coverage (§11.2) |
| `EQUIVALENCE` | judgments on one unit of covering classes, each read in either direction, claim equivalent every two revisions they connect: `z` is reached when it lies on a chain joining `j⁻`'s two revisions | — | ∃ path through unvetoed hops (§4.4) |
| `COMPLETENESS` | judgments of one class on sub-scopes at the same member revisions claim complete every scope their union covers: `z` is reached when it is needed in such a union covering `j⁻`'s scope; machinery and judgments alike | — | per closure (§4.6) |
| `GATE_DECISION` | the same gate and subject triple, in any frame, tenure or run | — | minimum (§5.5) |
| `PRODUCT_SCOPE_ACCEPTANCE`, `INTAKE_DISPOSITION` | the same named surface or delta | — | ∃ |
| failing `EVIDENCE_ASSESSMENT` | its adverse scope (§6.4) | — | §6 |

A passing judgment **asserts** when it would stand above `F` but for vetoes; a provisional one asserts. The reach reads only S0 and S1 facts. A re-identification of a subject or unit is a new target for the subject- and name-keyed kinds; where a declared lineage links it to the old identity, the standing objection is carried into the next judge's brief (§16.5).

**(d) Objection.** An adverse judgment counts by existence: it is never-lost (§8.3 step 6), its own currency is irrelevant, a loss boundary does not withhold it, and it needs no independence (independence is required to support, never to object). It objects in every state, whatever its frame, to every passing judgment in its reach, admitted before or after it.

**(e) What ends an objection, and who.** Exactly four routes, each counting only from a record that is independent by (f), and only in the states where that record acts (§5.2):

1. **reassessment** by the adverse judgment's own author (a human; an agent's task has ended), superseding it on its supersession target;
2. **adjudication by the owner**, superseding it on its supersession target;
3. **per-target relief** (judgments about work and plan acceptances only): the author's or the owner's passing judgment on a reached target, which exempts that target only;
4. an **upheld challenge** against the adverse judgment.

No qualified peer supersedes another actor's judgment; a contrary peer judgment is a disagreement. The **owner** of a target is the actor policy names to adjudicate disagreements in its domain (for an agent, the execution bound to that disagreement's adjudication obligation, never a peer with the same qualification). *[Amendment A4, SD-55.]* Where a reach crosses items or plans (c), the owner is the owner of the adverse judgment's target, and the reached judgment's own owner is shown on the obligation.

**(f) Independence.** These records carry an independence requirement: every review, conformance, acceptance and plan-acceptance judgment; every `EQUIVALENCE` and `COMPLETENESS` that is not a machinery record, whatever request carries it (SD-29); every disposition of a failing assessment; every reviewer's `INTAKE_DISPOSITION`; every `ADJUDICATION`. Machinery records and imports carry none; gate decisions and product-scope acceptances are R3 decisions by holders policy fixes. A record with a requirement is **independent** of its target only when its judge is not among the authors of the judged content (b): an agent's lineage must be positively attested fresh (§12.2) and disjoint from them, and unknown authorship is never disjoint from an agent's lineage; an authenticated human must not be one of them or must present a `NON_AUTHORSHIP_ATTESTATION`. **Owner disposition of a failing assessment [SD-48].** The one exception is the reviewed workplan's (workplan §6.6, §6.8 step 3): where policy names no qualified human outside a claim's authors (or the claim's authorship is unknown), the authenticated human policy names as the claim's owner may record a disposition of a failing assessment about that claim (§6.7: an `IMMATERIALITY`, a superseding reassessment or adjudication, or an adjudication upholding a challenge against it), admitted as independent with the common-mode dependency recorded and shown in the inspector view. It applies to no other record: for a review, conformance, acceptance, plan acceptance, equivalence, completeness, intake disposition or any other adjudication, an author of the judged content is never independent, and a recorded common-mode dependency does not make it so. **Eligible judge, per route and per state [SD-51].** A judge is **eligible** for a record in a state only when it is independent of that record's own judged content (the objection's for a reassessment, supersession or adjudication; the relieved target's for a relief; the answered target's for an answer), the record would act in that state (§5.2; a judgment about a transformation declares that transformation's frame, §7.5), and the record's basis is admissible there. **No eligible judge.** Where no actor policy qualifies is eligible for the answer an obligation needs, or for any of the four routes of a standing objection, in the state at hand, the obligation or objection waits: no admissible independent record exists there, and S3 derives human attention naming it and the missing judge (§10.3). This covers an actor who is qualified and independent but whose record could not act where it is needed, for example a supersession of a judgment about an abandoned transformation. Policy may then name an eligible judge (a ruleset adoption), or the work may be changed or withdrawn; independent closure is never manufactured. The classification is fixed at admission. Independence is enforced at two points only: Admission refuses an `ADJUDICATION` that is not independent of the authors of its challenge chain's root or whose class is below the chain's (§12.4); and derivation gives every non-independent record (`nonind`) base `F`, so it supports, supersedes, relieves and disposes of nothing and is kept as data. The Dispatcher selects reviewers outside the authors so that the check is not spent on predictable refusals (§16.5).

**(g) Consequences in S3.** A standing adverse judgment that vetoes an acting passing judgment derives the owner's `ADJUDICATE_DISAGREEMENT` (§10.2), and the vetoed judgment derives no revalidation; a vetoed non-independent judgment derives it too, so its contrary claim is shown. An answered judgment obligation whose target carries a standing, unrelieved adverse judgment in its reach is `REFUSED` (§10.4), whichever answered first. A non-independent passing judgment does not answer an obligation whose discharge requires independence. Every gate brief lists every standing adverse judgment whose reach includes the decision asked (§16.6).

**(h) Invariants.** The rules above are written to satisfy, for every realization:

1. **No unresolved support.** A passing judgment in the reach of a standing, unrelieved objection supports nothing, alone or through any composition.
2. **Every route is independent.** No non-independent or refused record ends an objection, supports, supersedes, relieves or disposes.
3. **Relief stays inside what was judged.** A superseder ends an objection only by judging its own supersession target; a reliever only for its own exact target.
4. **Liftable or waiting [SD-49].** For every state in which a standing objection vetoes, either some admissible independent record of routes 1-4 would end it there, or no eligible judge for any of those routes exists there (eligibility per route and per state, (f)): the objection is then shown waiting on that named missing judge, human attention is derived, and the vetoed judgment supports nothing meanwhile. Only a change of state that makes an eligible judge available (for example, policy naming one) makes a route admissible; waiting, human attention and a risk override never end the objection.
5. **State locality.** A permissive record of a pending, abandoned or replaced enactment changes no admitted value; an adverse judgment objects in every state.
6. **Order independence.** For one admitted set of records, every derived value is the same whatever their admission order.
7. **Class.** No adjudication below its chain's class is admitted.
8. **Routed.** Wherever a standing objection vetoes an acting passing judgment, the owner's adjudication is derived.
9. **One judged content.** Reach, relief and independence read the same `W` (b) for each judgment, and no actor among the authors of `W(j)` is admitted as an independent judge of `j` (A5, A9), the owner disposition of a failing assessment ((f), SD-48) being the one exception; where no eligible independent judge exists, independent closure is unavailable and human attention is derived.

`qualification/ssds80/judgment_disagreement_model_check.py` and `qualification/ssds80/item_review_history_probe.py` are diagnostics of the catalogue's realization of these rules on the cases they model, never adequacy evidence (§31.3; register RR-1, RR-2, RR-10).

### 6. Assessment disagreement

#### 6.1 Owner requirements realized here

The 7.2.1 evidence owner requires that a valid failing observation is evidence, that a stale failing observation is not admissible against current authority and a stale passing one is not admissible confirmation, that an unresolved material disagreement keeps dependent guidance and closure visibly qualified, that resolved reassessment stay distinguishable from live disagreement, and that nothing is resolved by vote, count, latest editor or record order or by suppressing contradictory observations. This section is the D3 concretization.

**No mechanical lapse.** A failing assessment, once it counts, counts against its claim until a disposition stands or discriminating observations show it stale in the frame. No content change, structural change, specification change, frame outcome, challenge or ledger order ends it by itself. Staleness is not refutation: a failing assessment never makes validity `F`; it caps it at `P`, and reassessment decides.

**The family rule.** Every input to the disagreement predicates obeys three clauses: **start** — machinery makes a failing assessment start counting only on an admitted fact or in its own lineage, and once started in the admitted state it never stops there by machinery; **stop** — only a judgment that addresses it, or evidence that discriminates in the observations, stops it; **standing** — a stop earned by supersession stands on immutable facts and its own record's standing, in the states where that record acts, while a stop by discriminating observations holds in each frame exactly while that frame's observations show it.

#### 6.2 Applicability dimensions

The protocol obligation is the evidence obligation (assessments for different obligations never conflict, and an obligation that stops being required keeps its disagreement); the specification's fixed regime and attributes decide **admissibility**; stochastic replicate identity and every attribute the specification leaves free are **execution variation**, so admissible assessments differing only there conflict; everything the execution read, with the reading applied, is the **assessed content**, which decides reruns and staleness and never whether a failure starts counting; the candidate is the **frame**; everything else is provenance, which can end currency, never adversity.

#### 6.3 Assessed content

A failing assessment's assessed content is recorded once, at admission, as content identities: the **executed content** (the specification, its execution closure widened by §4.6, every read the runner observed, external reads by pin or as unpinnable, and every execution attribute the runner class records) and the **reading** (the specification revision applied and the claim content read). **Recorded execution basis [D3 decision; refinement R1].** It is recorded once, in the `REALIZATION`, at the granularity the closure and runner reached, with its own resolution context (system version, `ignore` patterns, analyzer set), and every consumer reads that one record. **Guard:** the adverse matching predicate is a function of the record and the compared bytes alone; nothing adopted later changes what a recorded term denotes.

#### 6.4 Start: anchors, home, about, starts

Admission records each failing assessment's anchors (the subjects whose scope held the evaluated target, in the admitted state at its base and in its frame) and its lineage (the obligation its transformation was produced for). Its **home** is those anchors and every subject that later received their regions by admitted structural change; nothing removes a subject from home, so no change outside a disposition sheds a dispute from the subjects that held the claim. A failure is **about** its home, the subjects with a required obligation in its obligation's lineage, and, while no home subject still contains it, whatever subject now holds the evaluated content. It counts in every frame of its own lineage from admission, and in the admitted state and other lineages' frames from the first position at which its obligation is required there; from then on it counts at every later position whatever happens to the content. Moved-and-rewritten claims are followed only as far as stated (§32.2).

#### 6.5 Matching: configuration, outcome and the two matching predicates [refinement R1]

A realization's **configuration** is its specification, regime, parameter instance and every attribute the specification fixes; its observed values of free attributes are recorded execution attributes, never configuration. Its **evaluated outcome** is the part of the observation the oracle reads, in canonical form; an output's identity is `(specification unit, output name)` across revisions, with declared renames. **Two matching predicates, one construction rule.** The adverse predicate compares only tree-resident recorded terms, re-resolved under the record's own context. The permissive predicate is the adverse one conjoined with identity of the whole class of everything that can distinguish two executions of one configuration without being tree-resident recorded content (the complete set of external locators and pins, no unpinnable read, every recorded execution attribute) and with a basis bounded by completeness judgments that stand and hold on the content the run ran on: their membership and content entries are that content's, and each other premise holds in the state of evaluation **[A8, SD-58]**. A bounding judgment certifies the basis of one run on one tree, so a later change elsewhere does not unbound it, and a genuine fix can make a failure stale. So `on⁺ ⇒ on⁻` by construction for every structure, boundary, analyzer set, external input and attribute; losing completeness or changing structure only narrows permissive matches. Every use names its predicate: permissive uses (making a failure stale, lowering a decision class) use `on⁺`; adverse uses (keeping a failure counting) use `on⁻` or the existential linking predicate that contains it. **Verdicts.** A declarative mechanical oracle's verdict is recomputed under any reading; an embedded oracle's verdict is known only under the reading it ran; a needed verdict that is not computable is treated as a failure (fail closed).

#### 6.6 Stop: staleness by discriminating observations

A failing assessment is **stale** in a frame only when four conditions hold: (1) **reproduced** — a standing, permissively matching second execution on the failing run's content gave the same failing outputs; (2) **never differed** — no admitted execution linked adversely to that content, whatever its standing, gave other outputs there, otherwise the configuration is nondeterministic in fact and goes to the owner; (3) **observed here** — a standing, permissively matching execution of the configuration exists on the frame's content; (4) **not yielded here** — no admitted execution linked adversely to the frame's content yields the failure under the frame's reading. Every stop rests on a narrow record of the failing run's content. For an assessor-read oracle, condition (4) needs one **discriminating reading**: an independent assessment that reads `PASS` for the frame's outcome and `FAIL` for the reproduced failing outcome in one record; one outcome cannot be read both ways under one reading. A discriminating reading covers every observation with the outcome it read `PASS`, under the same reading. Removing a check makes nothing stale when the check was in force at the failure's base; an accepted change of a declarative reading that the admitted outcome passes does, and its review brief lists what it would make stale (§16.5).

#### 6.7 Stop: effective disposition

A failing assessment is **disposed of** by an independent supersession by its own assessor or the owner's adjudication, by an upheld challenge against it or its realization, or by a current `IMMATERIALITY` judgment covering it. A supersession stands on immutable facts; an `IMMATERIALITY` at its own currency; an upholding while in force, held and uncontested. Nothing else ends a disagreement: not an open challenge, a loss boundary, a positive-only requalification, any content or structural change, another configuration's passing assessment, a passing rerun that yields the failure, the candidate's rejection or integration, an obligation's retirement, split or retargeting, an unauthorized later assessment, or ledger order. Re-disposal after a disposition stops standing uses existing records.

#### 6.8 Decision class, independence and floor events

Staleness is not a decision: it is derived from designated-runner observations and, for an assessor-read oracle, a recorded discriminating reading. Every disposition, the failing assessor's own reassessment included, carries the independence requirement against the authors of the claim content, with the one owner-disposition exception (§5.10 (f), SD-48). **Class.** Dispositions of another actor's failure are R2, R3 where any subject the failure is about is or has been D1 or D2 authority; a discriminating reading is R2, R3 in the same case unless the failure is shown to be the candidate's own. **Floor event (D1/D2).** A counting, undisposed, non-stale failure about D1/D2 authority on a claim that has an admitted pass becomes a floor item once it is shown to concern admitted content, or reproduction has failed, or no reading can be admitted: human attention keyed on its existence, closed only by an authenticated human judgment.

#### 6.9 Scheduling

While a failure counts undisposed and not stale, S3 derives a **rerun obligation** for what conditions (1) or (3) lack (each run with the failing realization's pins and recorded attributes), and, for an assessor-read oracle whose current outcome no standing reading covers, one **reading obligation** for an independent reviewer at the class above; a reader who disagrees over one outcome under one reading cannot record either, and the obligation closes into the owner's adjudication. Where (2) has failed or no run could serve (1) or (3), nothing is scheduled and the failure is the owner's. The Dispatcher keeps at most one outstanding execution per configuration, attributes and frame; every designated-runner execution it starts ends in an admitted, never-lost observation, complete or `INCOMPLETE`. **[D3 decision; proposed default]** The specification declares the time bound; the system caps Dispatcher-run executions (§0.6); longer realizations run under external custody, whose observations make nothing stale unless its enumeration lists every run of the configuration it performed.

#### 6.10 Effects and uniqueness

A live disagreement makes the evidence term `P`, so validity and discharge are visibly provisional and briefs label the evidence `disputed`; S3 derives the owner's adjudication obligation, and the inspector shows which observations make each failure stale. The disagreement predicates preserve §5.6's monotonicity. **Stochastic specifications.** The assessed unit is the declared granularity: an ensemble's realization is the whole ensemble and its outcome the declared statistic; replicate variation inside one realization is not disagreement; a free seed is a recorded attribute, so runs under another seed enter conditions (2) and (4), and a seed-dependent failure goes to the owner. Acceptance never depends on the latest single replicate: a later passing ensemble neither supersedes nor disposes of a counted failing one, so edit-and-rerun is not a route to a pass.

### 7. Transformation frames

#### 7.1 Transformation identity

A **transformation** is `X = (B, C, A)`: `B` the recorded base (an admitted integration commit), `C` an immutable candidate commit on an isolated ref, and `A` the exact set of quarantined structural deltas its request adopts (§18); `id(X)` hashes the three. It is fixed by the task result that first submits the candidate. `Δ(X)` is the set of effective units whose revision differs between `B` and `C`; `Δ_Σ(X)` the structural changes `C` authors, with `A`.

#### 7.2 Frame state and the fixed merge

At admitted head `n`, the frame `D_n[X]` is derivation over the same ledger with the observed tree replaced by the merge `M_n(X)` of `C` onto the current tree from base `B`, and structure replaced by `Σ_n ⊕ Δ_Σ(X)`. **[D3 decision]** The merge is a pinned, deterministic three-way merge belonging to the system version: no rename detection, repository merge drivers or rerere; a both-sides change that does not merge line-wise without overlap, or a declaration key changed differently on both sides, is a conflict. In the frame the proposal's declarations are not quarantined; every other quarantined delta stays quarantined.

#### 7.3 Basis-entry roles

Every `content` entry of a frame record has one role, computed from `B`, `C` and the entry: a **before-image** (a changed unit at its base revision; satisfied while the live head still has it, and a fixed fact after integration), an **output** (a changed unit at its candidate revision; satisfied at its merged revision), or **context** (an unchanged unit; ordinary currency). A frame record is satisfied only by records that act in the state at hand; no frame designation transfers currency.

#### 7.4 Existence: inspection, not enactment

The frame exists when the merge is clean and the proposed structure is well formed (every structural check except the enactment condition). Without that there is no frame, nothing in it can be current, and a new iteration follows: machinery never resolves a conflict (K3). A frame is never presented as current state, and nothing in the admitted state reads it.

#### 7.5 Declared frame and what frames decide

A task result, check execution, realization on the candidate, a judgment about the transformation, a gate decision answering a gate derived in the frame, a co-submitted product-scope acceptance and a cutover `MODE_TRANSITION` the transformation carries declare frame `id(X)`; every other record declares the admitted frame. Obligations in the frame are those the integration would produce. What a frame record supports, supersedes or relieves has effect only where it acts (§5.2). An acceptance in the frame names a subject effective in the proposed structure: a **prospective acceptance**. Nothing evaluated in a frame changes the admitted state.

#### 7.6 Integration enacts; prospective acceptance binds once

The integrating admission of `X` admits exactly the merged tree and proposed structure in one entry, after full structural validation including the **enactment condition**: every promotion, restoration or cutover carries a prospective acceptance that counts for the tenure it starts, and a cutover meets its conditions (§19.5). A prospective acceptance counts for a tenure only if the integration is of its own enactment, with the same structure, its basis holding at integration, and it has not counted for an earlier tenure; so it counts for at most one tenure. **Rebase.** A clean rebase is the same task and enactment; a frame record counts for the rebased transformation only if every entry holds in its role there, and a structural record also needs unchanged proposed structure. Records never move between frames by assertion.

## Part III. Admission and concurrency

### 8. Admission

#### 8.1 Admission requests

An **admission request** is the typed result of `submit` (§16.1), built by machinery: its identity, its task binding (§12.2), the obligations whose discharge it claims, its base, its candidate commits or none, the quarantined deltas it adopts and the records it submits. The admission record that accepts or rejects it is the complete identity and audit trail of a change; no other change primitive exists. **[D3 decision]** A request's identity is the hash of its content, so a repeated identical request returns the recorded decision and appends nothing. Admission is the **sole ledger writer**; other movement of the integration ref has no admitted status and is absorbed before the next append (§8.6).

#### 8.2 Queue order

**[D3 decision]** Admission processes requests one at a time against the admitted head it holds, in arrival order, except that a request carrying only never-lost records is never delayed behind one that may need revalidation. Any order is correct, because each request is validated against the head it is appended on (§9.1).

#### 8.3 Validation order

Admission validates, in this order, against the admitted head it holds, and either appends or rejects with recorded reasons. The exact checks are catalogue §8.3; what each step decides is architecture:

1. **schema** — every record well formed under the closed schema; bounded secret checks (§24.1); unknown required semantics fail closed.
2. **reference** — every identity, revision, task, obligation, target and named run exists and matches; a rebase's claimed transformation is the pinned merge of the transformation it rebases.
3. **authorization** — actor class qualified for each kind (§3.5); acceptance only on effective, unrevoked, well-formed subjects in their current or prospective tenure, never on parts; the task binding verified against an issue key in force (or, for never-lost records, a retired uncompromised key whose retirement lists the envelope); the envelope names an existing obligation of the role it was issued for; the declared governing version equals the envelope's; **independence and adjudication eligibility** exactly as §5.10 (f) defines; **supersession authority** by the kind of the superseded record (refinements R8, R9; §5.10 (e)); a discriminating reading admitted only at its class; the bound role permits each record kind and outcome, the effect-keyed write set lies within the contract's write scope, and protected surfaces are untouched without their own authority.
4. **structure** — on the merged tree: the effective-structure delta is exactly what the request authors, realigns, carries or adopts, validated together by the well-formedness checks (§1.9, §2.5), with no mode mixing without its transition, SDG members kept together, and a change of a unit's kind or domain released by its current domain's owner; the challenge freeze (no change of signature, scope, regions or membership of a subject whose revision is under an unresolved blocking challenge or revoked); and, for an integration, the enactment condition (§7.6). Admission never creates quarantine.
5. **dependency well-formedness** — challenge targets strictly earlier and of permitted kinds; no `validity` entry on a record's own subject; the static support graph gains no new or larger non-trivial component.
6. **currency** — every basis entry of every submitted support-tier record other than a report is satisfied in its role in its frame at the current head; otherwise the record is stale and routed to revalidation. **Never-lost records are exempt**: reports, challenges, failing assessments, adverse judgments and designated-runner observations are admitted whatever the request's fate, provided they pass their own checks, and a never-lost record failing its own checks is recorded as refused.
7. **legality** — the bound obligation exists. **[D3 decision; refinement R9]** Every task ends in exactly one `TASK_RESULT`, and the result-only `HARD` templates run at admission: a non-clean result refuses every passing judgment and principal decision in the request while its never-lost records and the result are admitted; so does a result that states a memory uncertainty no standing human decision accepts for its obligation (§16.11 (g)). *[Amendment A10, SD-63.]* **One enactment, one integration [SD-26]**: a second integration of one enactment is refused. An answered judgment obligation refuses a later passing judgment bound to it, except an authorized supersession and a further gate decision. **Revision assessments first [SD-16, SD-19, SD-22]**: a passing acceptance or gate `ACCEPT` on a `NATIVE` D1/D2 revision is refused unless a revision-assessment record for exactly that revision counts (§10.2). A human decision on a fenced admission is admissible only once that admission is settled (§22.3). A claimed discharge must be undischarged at the head and hold after the request's own records, with affected evidence rerun on the merged tree, with clean conformance for a contracted task obligation (§14.6); clean conformance includes the freshness of a HAS the result carries, re-evaluated whenever the request is revalidated (§16.11 (f)). *[Amendment A10, SD-63.]* An integration whose judged content no longer matches what its judgments judged is refused as a new iteration (§5.10 (b)).
8. **no collateral regression [refinement R15]** — for every other obligation whose required evidence the merged tree affects, no evidence term that passes at the current head may fall (a fall from `T` to `P` counts as failing); a request that makes one fail is refused. The only legal way to make another closure's evidence fail is an accepted change to a prerequisite authority, whose request carries a current prospective acceptance and gate decisions of that authority, exempt only for the obligations that depend on it. A judgment the request makes non-current is not a regression: the obligation it supported reopens in current state and takes the route §10.4 gives it.
9. **commit and admit** — Admission reads the live integration head; the request is appended only if that head is the expected head or an equivalent publication of it (§22.2), otherwise an absorption is appended first and the request revalidated. One entry is appended by single-ref compare-and-swap, provisional until a witness quorum holds it; only then is the request reported admitted, the integration ref published, work dispatched from the new state and the next entry appended (§22.4).

#### 8.4 Reason codes [D3 decision]

Every rejection and refusal carries enumerated reason codes, one per failed check, grouped by step and closed per schema version (catalogue §8.4).

#### 8.5 Dependency rules restated for authors

A challenge-tier record targets only strictly earlier records, and a challenge targets a challenge only as a counter-challenge of a restrictive adjudication. A judgment about a part never holds `validity` on its own subject. An equivalence relates two revisions of one unit and never relies on a consumer of that unit.

#### 8.6 Absorption

Absorption of a foreign change already on the integration ref records what happened, so it cannot be stale or illegal: it skips steps 1-8 and is a pure integration observation carrying no submitted records. It sets the observed tree and changes nothing else; its consequences arise only through lower strata (foreign declarations become quarantine, foreign content changes revisions, foreign relation violations make subjects ill-formed), and the S3 obligations that follow only schedule and explain (§18).

#### 8.7 Self-reference and agent PASS

Records reference the candidate commit and are never stored inside it; envelopes on run branches are transport, ingested into the ledger, never merged (G2, G3). An admitted `PASS` is a recorded fact about what an actor concluded; closure is a derived discharge (§10.4).

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

- **Serialization surfaces.** Policy may declare units as serialization surfaces; the Dispatcher then issues at most one mutating task whose write scope intersects such a unit at a time, and at most one coordination task per plan. Serialization is scheduling, never correctness.
- **Joint invariants.** A joint-invariant declaration names an invariant and the units whose joint behavior it constrains. Every admitted change touching that scope derives a review of the integrated result against the invariant (target type 3, §3.4) by an R2 reviewer, plus the evidence that `EVIDENCES` the invariant's unit. Each change derives its own; an earlier change's obligation ends when a later change in the same scope derives one, unless it is `REFUSED`. Policy may mark further surfaces high-consequence, which derives the same integrated-result review for every change to them.

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

An obligation's identity is deterministic from the rule, target and parameters that derive it. The system kinds and their holders are: `IMPLEMENT`, `REPAIR`, `MIGRATE`, `AUTHOR` (authoring or materially revising D1-D3 authority) and `DOCUMENT` for accepted, issuable items with contracts (implementer); `INVESTIGATE` (investigator); `CONTRACT` and `COORDINATE(plan)`, the decision owed on a plan (principal); `PLAN_ACCEPT`, `REVIEW(X)` while `X` is unintegrated, `REVIEW(s, r)` (the revising review of a `NATIVE` D1/D2 revision), the integrated-result reviews (item-level, `JOINT_INVARIANT(i, k)`, high-consequence), `ACCEPT(s)`, `ASSESS`, `READING`, `SPEC_REVIEW`, `ADJUDICATE` and `ADJUDICATE_DISAGREEMENT` (reviewer or the owner, or a human by class); `REVALIDATE(x)` for an acting judgment no longer current that a current obligation depends on, never for a judgment that a standing objection vetoes, and for an item obligation's review or task result only as §10.4 routes it (the role of `x`'s kind); `REALIZE`, `RERUN`, `REISSUE` and `RECONSULT` (Dispatcher); `GATE`, `HUMAN_ATTENTION` (for a routed report, a floor event, a judgment obligation or standing objection with no eligible judge, §5.10 (f), §10.3, or a memory uncertainty no independent review judges, §16.11 (g)) and `INTEGRITY` (human); `INTAKE` (investigator, then a disposition reviewer); `REQUALIFY` (the role of the withheld record's kind). *[Amendment A10, SD-63.]* The triggers are catalogue §10.2. Obligations belonging to no plan go to the role their kind names, and a decision owed on them to the standing plan's principal or, with none, the human (§12.5).

**Revision assessments and the revision run [D3 decision; SD-16, SD-19, SD-22, SD-25].** For every `NATIVE` subject of kind D1 or D2: a **revision-assessment record** for `(s, r)` is an admitted `TASK_RESULT` whose complete `revision_assessments` slot names exactly `s` at `r`, from an `AUTHOR` task whose candidate yields `r` or a task answering `REVIEW(s, r)`, however `r` was produced. The **revision run** of `s` is identified by the event at which its current revision took its value (an integration's enactment, an absorption or adoption, a tenure start), known before the event and equal in the frame and after it; any later change of the revision, a return to earlier bytes included, is a new run. A passing acceptance or gate `ACCEPT` names its run and is current only in it; it is admissible only while a revision-assessment record for that revision counts (in the run and standing), on which it carries a `standing` entry. Machinery computes the revision's **predecessor** for display in the brief, slot and gate core; it is never an equality condition. `ACCEPT`, `GATE` and `REVIEW(s, r)` carry the run among their parameters, so a new run derives new obligations.

**Evidence obligations under change [D3 decision].** An evidence obligation is identified by its claim and specification lineages, which follow retargets, splits and renames. Retirement, split or retargeting never disposes of a failing assessment; the owner disposes explicitly.

#### 10.3 Readiness

**No stranded obligation [D3 decision; stakeholder record item 31].** In every state a judgment obligation is dispatched only while an answer of its kind with its mechanical minimum can hold at Admission; otherwise it is shown waiting on the failing entry, and the route that restores that entry is derived instead. A judgment obligation with an independence requirement is dispatched only to a judge eligible for its answer in the state (§5.10 (f): independent of the answered target's judged content, its record acting there, its basis admissible); where none exists, it is shown waiting on one and human attention is derived (SD-48, SD-51); an obligation whose last result stated an unaccepted memory uncertainty waits likewise on that human or a readable reader (§16.11 (g)), never dispatched to a judge whose answer would be non-independent or could not act. *[Amendment A10, SD-63.]* The same holds for ending a standing objection: §5.10 (h)(4) is the one statement of when an objection is liftable and when it waits on a missing judge, and the owner's adjudication obligation it derives is dispatched only in the first case (SD-49). A ready obligation whose every answer Admission must refuse is a defect, and so is a non-current judgment a current obligation depends on with no ready or waiting route. One class waits by design: an adjudication of a disagreement for which neither the owner's supersession nor relief is admissible, because the bases they need no longer hold, waits on an upheld challenge or on the owner's never-lost adverse record, and the vetoed record then blocks no work.

An obligation is **ready** when every prerequisite it names is valid (or provisional where an override or policy permits) and its plan item, if any, is covered by a current plan acceptance. Readiness is derived from the ledger and content alone; whether a ready obligation is dispatched now is the Dispatcher's operational decision and never feeds back into derived state.

**Iterations and attempts [D3 decision].** An **iteration** of an obligation counts its admitted `TASK_RESULT` records; a NO-PASS leaves an implementer obligation undischarged, and its next task is the next iteration on a new candidate. A **task** has a random identity the Dispatcher issues; an **attempt** is one execution of it, recorded only in the operator journal, and a failed attempt spends no iteration.

**Answered judgment obligations [D3 decision; refinement R9].** A judgment obligation is answered in a state by the first judgment acting there of its kind on its exact target that is bound to it or recorded on its target by an authenticated human; a non-independent passing judgment does not answer an obligation that requires independence. An answered obligation is never dispatched again: a passing answer discharges it (§10.4); an adverse answer closes it undischarged, and the next step is a new target, the adverse judgment's author's reassessment or the owner's adjudication. It stays unanswered, and may be dispatched again within budget, only when its task ended with no admitted judgment.

#### 10.4 Discharge

Discharge is an S3 classification with four values: `DISCHARGED`, `DISCHARGED_PROVISIONAL`, `OPEN`, and `REFUSED` for an answered judgment obligation whose target carries a standing, unrelieved adverse judgment in its reach (§5.10 (g)). An obligation is discharged when some current judgment of its kind on its subject, by a qualified and, where required, independent actor, has a passing outcome; its subject's revision is neither blocked nor revoked; every evidence obligation of it holds and its subject's evidence is undisputed, a live disagreement making the value provisional (§5.5, §6.10); and every human gate's term holds. The value is provisional when any input is `P`, permitted only inside an override's scope or where policy permits provisional continuation for its kind, and otherwise `OPEN`. A vetoed passing judgment is not current, so a standing objection is never discharged around, in either order of admission.

**Discharge is not latched [SD-36].** An obligation discharged at one head is `OPEN` at a later head whose state no longer satisfies it; Admission step 8 refuses only collateral evidence regression (refinement R15). For an item obligation, its subject is the union of the subjects every integrated enactment of it changed, so a re-dispatch never narrows what its terms read (SD-37).

**Routes of an item obligation [D3 decision; SD-37 to SD-41, SD-52].** An item obligation's identity is its item and the prose and fixed fields of its accepted revision (§13.4), and that key governs [SD-52]: an R1 tightening and an amendment that only loosens a tightenable field keep the obligation (its `out(o)`, its subjects and its iteration count), the loosened item waiting for a new plan acceptance before it is issuable (§11.2, §11.4); only an amendment of the prose or fixed fields derives a new obligation. Its outputs `out(o)` are the units its integrated enactments changed, with their revisions after its latest integration, and they have **moved** while some current revision differs. In each state an item obligation has exactly one route, stated once in catalogue §10.4: before integration, and for a pending candidate after it, the ordinary iteration routes (a conflicting rebase or a refused integration is a new iteration; an in-scope NO-PASS or incomplete result is the next iteration within budget; out-of-scope findings and discrepancies go to the principal); after integration, in order, a fence awaiting or kept by the human goes to that decision, a holding predicate is discharge, a pending candidate keeps its own routes, a standing adverse review outside the item's scope or an item-level review naming no part goes to `COORDINATE(plan)`, a spent budget goes to `COORDINATE(plan)`, and otherwise the obligation is re-dispatched as a new task and enactment (drift when its outputs moved). No revalidation is derived for an integrated enactment's review or task result (SD-40). An adverse item-level review is a standing adverse review of each part whose outputs its findings name. A drift task's brief names the change that moved its outputs and states that later accepted changes are preserved; a drift candidate that changes nothing is reviewed and integrated as an empty transformation. A judgment obligation keyed on a past event is derived only while what it judged can still be current, and one answered `REFUSED` stays derived until a coordination decision answers it, so a finding is never retired by a later obligation whose judge did not see it. **Bounded stop [SD-41].** Five residual cases of this routing were accepted as named G2 reopen triggers (register RR-4 to RR-8; §32.3); the identity question behind RR-4 is decided above (SD-52), and the mechanism of all five is settled at G2.

Impact on other subjects is not a discharge condition: those are separate obligations. A missing required check is an undischarged obligation; no rule turns it into a pass.

#### 10.5 Provisional propagation and risk-override scope [D3 decision]

A `RISK_OVERRIDE` declares its continuation scope as a closed set: the subjects and items covered (identities), the obligation kinds allowed to discharge provisionally, and whether descendants created after the override inherit it (default no). It never covers `GATE`, `HUMAN_ATTENTION`, `ADJUDICATE` or `INTEGRITY` obligations. Inside the scope, `P` inputs discharge as `DISCHARGED_PROVISIONAL`; outside it they stay `OPEN`. Every view, brief and gate core labels provisional values with the override and the challenge it overrides; descendants whose support passes through a `P` value are `P` (min-propagation) and can never emit unqualified closure.

### 11. Change plans, plan acceptance and integration flow

#### 11.1 Plan structure [D3 decision]

A change plan is a `PLAN` subject: a Markdown document whose manifest declaration sections it into an **Objective** part and **item** parts, each item holding one typed item declaration (its id, kind, objective reference, governing units at revisions, acceptance criteria with their evidence, affected units, required gates, acyclic layer-respecting dependencies, and its work contract, §13). The item kinds are `IMPLEMENT`, `REPAIR`, `MIGRATE`, `INVESTIGATE`, `AUTHOR` (with its one authority domain) and `DOCUMENT`. Lifecycle fields in prose and directory placement are non-authoritative or generated (§19.8).

#### 11.2 Plan acceptance

A `PLAN_ACCEPTANCE` judgment (R2, by an execution other than the contract's author) names the objective section and the item revisions it accepts, the items with consumption class `PLAN_CONTROL`. An item is **issuable** only while a current plan acceptance covers its current revision. Item-level revisions give locality: an amendment is an ordinary change to the plan unit; tasks whose basis names a changed item become non-current; tasks on unchanged items continue. Running tasks remain bound to their basis; no revision pretends an old task saw new requirements.

#### 11.3 Plan invariants

Rechecked mechanically on every plan-unit change, as part of contract lint (§13.2): referenced units exist in `Σ`; item dependencies are acyclic and respect layer order; gates policy requires for the item kinds and domains are present; acceptance criteria name resolvable evidence specifications or `REVIEW`; every changed contract passes lint. A plan that fails is admitted as content (the principal's change is recorded) but its changed items are not issuable.

#### 11.4 Amendment policy [D3 decision]

An amendment's class is computed by lint from the diff between the accepted item revision and the current one (§13.4): control tightening keeps the existing plan acceptance current (R1); every other amendment needs independent plan acceptance (R2). The plan's policy section declares, per plan, whether an R2 amendment may be accepted by **scoped review** of the changed items plus their derived impact set, or needs whole-plan review. Changes to the plan objective, acceptance criteria, item topology (`depends_on`, added or removed items) or gates always need whole-plan review. A scoped reviewer always receives the whole-plan objective and may escalate to whole-plan review. There is no global planning or working phase and no global stop: an unaccepted amendment only makes its own items non-issuable.

#### 11.5 Results, review and integration

Implementation work enters canonical state through two ordinary admissions and an integration. **Result:** a records-only request bound to its task, claiming no discharge, carrying its `TASK_RESULT`, which fixes `X`; machinery attaches the factual part (diff mapped to units, touched relations, reads), and the Dispatcher runs the contract's required executions on the exact candidate through a designated runner; conformance is derived. **Review:** once conformance is `CLEAN`, `REVIEW(X)` is ready; result, executions, review and conformance declare frame `id(X)`; a reviewer task submits its judgments with its own `TASK_RESULT`; a candidate that promotes, restores or adopts a subject also gets a prospective acceptance in the frame. **Integration:** once the claimed obligation's discharge would hold on the candidate, the Dispatcher submits an integration request carrying no new judgment; a rebase that does not apply cleanly is a new iteration (K3), and a clean one re-derives conformance, review being re-requested only by the routes §10.4 gives a pending candidate. Records-only work has no integration step; a rejected candidate stays recorded with its conformance view and reports.

### 12. Workflow roles and decision classes

#### 12.1 Role and domain

A **workflow role** is an authority envelope: what an execution may write, which record kinds and outcomes it may submit, which decisions it may make. It is distinct from SSDP's D1-D4 domain roles, which are content: the epistemic procedure a brief carries for its subject's domain (§16.3). A brief composes the two. No agent role is a principal in the authentication sense of §25.1: its records are proposals attributed to an execution identity.

#### 12.2 Authenticated task binding and lineage

**[D3 decision]** The Dispatcher issues every task as an **envelope** signed with a registered issue key: task identity, bound obligation, role, contract revision, governing version (§16.9), route, lineage class, input sessions and issue position, and, for revision-assessing tasks, the predecessors to display. Admission verifies the signature and checks role, write scope and record kinds against it; admitted records carry the binding, so derivation and replay read it from the ledger alone. Binding and discharge are separate. **Lineage classes and context-lineage provenance [D3 decision].** On a harness route the Dispatcher starts a fresh session for the task, gives it alone a per-task submission credential and signs a launch attestation naming the session and the sessions of the task's inputs: lineage `ATTESTED_FRESH`. On manual and Git-envelope routes the session cannot be observed: a judgment is `UNKNOWN` unless an authenticated human attests that it ran in a fresh context without the author's conclusions (`HUMAN_ATTESTED_FRESH`). Independence is credited only to positively attested lineage; two lineages are disjoint iff no session of one's attestation closure appears in the other's.

#### 12.3 System role templates [D3 decision]

| Role | Holds | May write and submit | May not |
|---|---|---|---|
| **Principal** | `COORDINATE`, `CONTRACT` | its plan's units; its `TASK_RESULT`, coordination decisions, materiality reclassifications, reports, challenges | write product, authority or evidence units; submit review, conformance, acceptance, plan-acceptance or human judgments; keep its own amendment covered; change verification rules |
| **Implementer** | the implementer item kinds; `REVALIDATE` of its own result | its contract's write scope and named evidence specifications; its `TASK_RESULT` (`COMPLETE`, `PARTIAL`, `BLOCKED`, `INFEASIBLE`), reports, challenges | edit plans, contracts, other evidence specifications, verification rules or protected surfaces; judge its own work |
| **Reviewer** | review, acceptance (R2), plan acceptance, assessment, reading, adjudication (R2), specification and integrated-result reviews, intake dispositions, revalidation of those | records only: the support- and challenge-tier judgments of those kinds, its `TASK_RESULT`, reports, challenges | write content; judge work or a contract its own execution or lineage authored; receive the author's narrative or conclusions |
| **Investigator** | `INVESTIGATE`, intake classification | scratch workspaces and named finding homes; findings, classifications, reconstruction proposals, proposed relations | write product or authority units; submit acceptance |
| **Human** | `GATE`, `HUMAN_ATTENTION`, every R3 decision | every R3 kind; any content as ordinary change that enacts nothing until admitted | — |

Every role may submit reports and challenges, which are never-lost; every launched execution runs in a fresh context for one task. **Separation constraints.** No execution holds principal and reviewer roles; no reviewer judges what its own lineage authored; a plan acceptance is never by the contract's author lineage; the obligation kind determines the role (A4). **Policy extension limits.** Policy may add roles only by narrowing a template; it may not widen one, combine principal and reviewer, give an agent role an R3 decision, or let any role edit roles, templates, routing, floors or decision classes.

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

A **work contract** is part of its item, authored by the plan's principal, revisioned with the item, accepted by its plan acceptance and bound into every task's basis through the item revision; obligations outside any item get the system contract of their kind (§13.6), so every task has exactly one contract. A contract declares: the `scientific` flag (the 7.2.1 scientific-checks predicate); an iteration budget; **boundaries** (write scope, frozen public interface, permitted dependency additions, the evidence specifications the item may change, finding homes for an investigator); **obligations**, each with a statement in the item's prose and exactly one primary verifier (a `HARD` check template, an evidence specification with its runner class, or `REVIEW`) and optional secondary `HARD` checks; **expectations** (artifacts, evidence, required result slots); and **escalation triggers**; optionally **memory** (`memory.bind`, entries or the project memory bound as relevant to the item, and `memory.terms`, applicability terms for candidate matching) and a **change intent** (`change_intent`, a set from `rework`, `replacement`, `consolidation`, `optimization`, `scaling`, `migration`, `revert`, `restoration`), declared by the principal and judged in plan acceptance like every other field (§16.11). *[Amendment A10, SD-63.]* The schema is closed (C5).

#### 13.2 Lint

Lint is mechanical, runs on every plan-unit change with the plan invariants, and establishes form only: fields typed and resolvable; **ref locality [D3 decision]** (every prose reference resolves only inside the item's own part and the plan's Objective, so all prose an item relies on is in its revision or its plan acceptance); the write scope within the item's affected units and free of protected surfaces, plan units and unnamed evidence specifications; **domain rule [D3 decision]** (an `IMPLEMENT`, `REPAIR`, `MIGRATE` or `DOCUMENT` item's write scope and effect-keyed write set contain no D1-D3 unit, so an agent changes what a D1-D3 unit owns only through an `AUTHOR` item of that one declared domain; a structural change across domains has no agent item route and is a human change or an R2 intake adoption); one primary verifier per obligation, each a `HARD` template or a named specification and runner class; the triggered slots required; minimum coverage held; a budget within the cap. Whether the contract captures the item is judged in plan acceptance by an execution other than its author: a strong verifier over a weak contract proves only what the contract asked.

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

An amendment is **control tightening** (R1) iff the item's prose is byte-identical and every field of the item and its contract is unchanged or moved only in its tightening direction (a narrower write scope, allowance or homes; a wider frozen interface; added secondary `HARD` checks; more required slots and triggers (entries added to `memory.bind`, intents added to `change_intent`); a smaller budget; `scientific` turned on); every other change, any prose change included, is R2, and a field outside the whitelist is R2. A change to `memory.terms` is R2: under the candidate cap a new term can displace a candidate the accepted revision required (§16.11 (d)). *[Amendment A10, SD-63.]* Prose carries meaning a reviewer judges, so machinery never classifies a prose change as tightening. The order `r ⊑ r'` it defines is checked against the **accepted** revision, is the only rule-defined coverage order (`PLAN_CONTROL`, §4.4), and claims only that an acceptance's conclusion about what is asked still applies under tighter controls. The fields it keeps unchanged, with the prose, are the item's **fixed fields**; the prose and fixed fields together are the key of an item's work (§5.10 (b), §10.4).

#### 13.5 Result slots [D3 decision; §19.2 delegation schema]

The delegation request is the work contract and the return is the `TASK_RESULT` with typed slots, each a typed value, `NONE` with an enumerated reason, or a content reference to a narrative home; an empty required slot without a typed reason is `INCOMPLETE`. The slot vocabulary is `deviations`, `unverified_assumptions`, `claims` (each factual claim with the records establishing it), `findings` (with the `OPEN`/`RESOLVED` status of earlier findings in a re-review), `null_envelope`, `variant_search`, `tension_search`, `choices`, `retention`, `delegate_returns`, `bidirectional`, `o1_content`, `revision_assessments`, `audit_conclusion`, `pem_activation`, `historical_applicability` and `closeout_learning`, each triggered by the task kind, subject domain and `scientific` flag as catalogue §13.5 lists; the three memory slots are triggered as §16.11 (c) and (h) state. *[Amendment A10, SD-63.]*

#### 13.6 System contracts

Judgment obligations get an empty write scope, the `claims`, `findings` and (for scientific subjects) `bidirectional` slots, `revision_assessments` for a revising review, and the default budget spent only while unanswered; intake investigations an empty write scope with policy homes; coordination the plan's units; revalidation and requalification the original task's contract.

#### 13.7 Task partition and budgets

A `PARTITION` coordination decision splits the **execution** of one item revision into tasks, never the item: the parts' obligation sets partition the item's (for a re-partition, its undischarged ones), their write scopes are disjoint subsets of the item's, and their order is acyclic; lint checks all three. Each part's task is bound to its own part obligation and is its own enactment; the item, its plan acceptance and its scope are unchanged. A later partition supersedes an earlier one only for undischarged obligations; discharged part obligations stay required. The item is discharged when every required part is and an **item-level review** of the integrated result has passed, because separately reviewed parts can violate a joint property. The item-level review's target is the item revision's integrated result (target type 3, §3.4), its judged content is the item's work in the item's write scope at that result, over whose authors its independence is measured and its reviewer selected (§5.10 (b), (f)); it is derived anew when a part integrates again and waits while a part's outputs have moved; an adverse one is a standing adverse review of each part whose outputs its findings name. Policy may waive it only for named item kinds. **Budgets [D3 decision; proposed default].** Within budget, an incomplete result or an in-scope NO-PASS starts the next iteration mechanically, its brief carrying the conformance view and findings as data, never the previous narrative; budget exhaustion, out-of-scope findings and discrepancies go to the principal. An operational failure is a Dispatcher retry and spends no iteration.

### 14. Conformance verification and the check library

#### 14.1 Conformance

**Conformance** of a task result is an S3 classification evaluated in the candidate's frame: a pure function of the contract at the task's basis, the base and candidate trees, the result record and the observations recorded for that exact candidate, and, for the memory templates, the PEM facts of the state it is evaluated in (§16.11 (f), (g)). *[Amendment A10, SD-63.]* It is never stored. For a result without a candidate (reviewer, principal and records-only investigator results), conformance is the same function over the result record and its contract, and, for the memory templates, the PEM facts of the admitted head at its admission, and its result-only templates are also enforced at admission (§8.3 step 7). *[Amendment A10, SD-63.]* Expensive or nondeterministic checks (test execution, mutation testing, static analyzers) run on the exact candidate by a designated runner and are recorded as `CHECK_EXECUTION` observations; deterministic checks are memoized like analyzers. No component is added: Derivation evaluates, the Dispatcher executes, Admission enforces (§8.3 steps 3 and 7).

#### 14.2 Templates and force

Check templates are fixed, versioned functions of `ρ_n`. A contract only parameterizes them and never carries executable check code. A project-specific template enters only by human-gated ruleset adoption after qualification (§14.7). Each template declares one **force**: `HARD` templates may yield `VIOLATION`, `INCOMPLETE` or `DISCREPANCY`; `HEURISTIC` templates yield `SIGNAL` only. Every template that reads prose is `HEURISTIC` by system rule, so no control decision parses prose (A7). A model's verdict is never a template: it is an R2 judgment.

#### 14.3 The library [D3 decision]

The system library has six families, each template with exactly one force: **`BOUNDARY`** (`HARD`: effect-keyed write set within scope with the domain rule, protected surfaces, frozen interface, dependency allowance, generated units untouched, credential values); **`TEST_INTEGRITY`** (`HARD`: no deleted, skipped or expected-to-fail tests, evidence specifications untouched; `HEURISTIC`: fewer assertions, widened tolerance); **`OBLIGATION`** (`HARD`: required artifact linked by a derived `TESTS` relation, required evidence realized by the designated runner on the exact candidate, evidence basis fields, slots filled, memory occasions answered, HAS coverage and basis identity, HAS freshness, memory-unavailable reasons matching the reader state, a review's disposition of a memory uncertainty (§16.11), no new stubs, mutation strength); **`FAITHFULNESS`** (`HARD`: outcome consistent with obligations, deviations declared, citations support their slots, governing units at basis revisions; `HEURISTIC`: prose numbers, certainty vocabulary); **`DOMAIN`** (`HARD`: dimensional consistency of annotated quantities, tolerances declared, layer direction; `HEURISTIC`: unit inference); **`ORACLE`** (`HARD` declarative oracles: exact, absolute, relative and ULP tolerance, range, set equality, monotonicity). *[Amendment A10, SD-63.]* Removing every `HEURISTIC` template must leave every admission decision and every discharge unchanged (§31).

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

For Python and C++, a pinned analyzer version provides diff-to-unit mapping (one input to the effect-keyed write set), public interface extraction (host-dependent C++ preprocessing recorded as an observation), `symbol` span resolution as a pure function of file bytes, derived `IMPORTS`, `CALLS`, `BUILD_DEPENDS` and `TESTS` relations, and completeness declarations with incompleteness markers (§2.6); the parser libraries are part of the analyzer identity the ruleset pins. **Mutation testing** seeds the system operator set over the candidate's changed lines only, run by the designated runner with recorded tool and seed; a score below the contract's threshold is `INCOMPLETE` (§0.6). **Unit annotations** use one Python annotation form and one comment form with UCUM expressions; unannotated quantities are inferred only heuristically.

#### 14.6 The conformance view

The conformance view of a result lists, per obligation: verifier, template results with classes and findings, the observations used (by record id, with their runner and custody), and the set-valued class. It is rendered deterministically from derived state and shown to the reviewer and the principal; it is never a judgment.

#### 14.7 Qualifying a template as `HARD` [D3 decision; proposed defaults]

A template is adopted as `HARD` only after qualification on real trajectories, with thresholds and samples frozen before the runs, against detection on seeded violations and false positives on clean trajectories (§0.6); one that misses either stays `HEURISTIC`. A defective template is corrected only by ruleset adoption; admissions are never re-adjudicated and current conformance is re-derived (§27.1).

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

A coordination task decides each routed report with a `COORDINATION_DECISION` whose allowed outcomes are a function of the report's kind, reason and target domain: `RESOLVE_LOCAL` (inside the item's delegated space; never for an authority- or contract-defect request), `AMEND` (a plan-unit change follows in the same request), `CHALLENGE` (against the earliest affected owner; required for an authority defect targeting D3 or D4), `ESCALATE` (human attention), `DECLINE` (with a reason, non-floor reports only) and `PARTITION` (§13.7). A decision owed with no report behind it (an item-obligation route of §10.4, detected recurrence, a `REFUSED` integrated-result or specification review, a stale memory binding or a proposed memory update, §16.11 (e), (h)) allows the outcomes catalogue §15.5 lists for it, and is answered by the first admitted decision naming it; `ESCALATE` does not answer an item route. *[Amendment A10, SD-63.]* An `AMEND` decision's plan change is linted and integrated, enacting nothing by itself; each changed item's issuability follows from its plan acceptance and amendment class (§13.4).

#### 15.6 Annotate, merge, upgrade, downgrade

The principal may annotate any human-attention obligation; its framing is Channel A interpretation, rendered apart from the evidence core. It may merge duplicates (the merged entry lists every member, and one human judgment may answer it as a whole), upgrade materiality, and reclassify a non-floor `MATERIAL` report to `ROUTINE` by a `MATERIALITY_RECLASSIFICATION`, which counts only while in force, moves the item to the digest, is challengeable (an upheld challenge or a later loss boundary returns it), and is never a discharge. Floor items cannot be reclassified. Human attention is discharged only by an authenticated human judgment (A8).

#### 15.7 Recurrence

Recurrence is detected mechanically: the same `HARD` template failing on the same obligation across iterations; the same finding family (template, target unit or relation family) across items; repeated discrepancies by one route; a candidate that reverts integrated work (§16.11 (b)). *[Amendment A10, SD-63.]* Detection creates a `COORDINATE` decision whose brief carries the convergence duty: consider the shared owner and simplification before another local repair, and route a challenge where the contract or its governing authority may be at fault. Detection is mechanical; the response is judgment. Detection never creates a memory entry; a recurrence is also a memory occasion (§16.11 (b)). *[Amendment A10, SD-63.]*

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
| `history(x)` | ledger history of `x`; offered only when a memory occasion fires (§16.11) or on explicit request (`HISTORICAL`) *[Amendment A10, SD-63.]* |
| `memory(x)` | PEM facts bearing on `x`: owner-bound entries with binding states, tag and typed matches for given terms, the reader state and the accepted and overlay identities; `HISTORICAL`, offered on request or when a memory occasion fires (§16.11) *[Amendment A10, SD-63.]* |
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
| `HISTORICAL` | PEM entries and Git history; offered only when a memory occasion fires or on explicit request (§16.11) *[Amendment A10, SD-63.]* |
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
| a memory occasion (§16.11 (b)) | PEM owner, plus the candidates and `HISTORICAL` items and the memory slots of §16.11 (c) *[Amendment A10, SD-63.]* |
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

A review brief **contains**: the governing content inline; the contract; the candidate diff and machine-produced facts; the conformance view with every `SIGNAL` as a labeled pointer; the evidence with status, including, for a candidate changing a specification, the counted failures the change would make stale or whose discriminating readings it would stop covering, as a required review item; the result's disclosure slots, labeled as the author's claims to test; the memory bindings the candidate would make stale and any memory-unavailable reason, the latter as a required review item whose acceptance the passing judgment records (§16.11 (e), (g)); for a scientific subject, the 7.2.1 bidirectional Review question as the required `bidirectional` slot; for a substantial authority review, the out-of-matrix abstraction-adequacy duty. *[Amendment A10, SD-63.]* It **excludes** the author's outcome classification, rationale and narrative, commit messages and transcripts, the principal's annotations and expectations, and any earlier conclusion by the author. The brief's evidence section marks the current executions and realizations of the exact candidate, which the review relies on; earlier, superseded or stale runs are history.

**Carried objections [D3 decision; SD-30 to SD-34].** Every standing adverse judgment whose reach includes the target asked (§5.10 (c)) is supplied by default, labeled as another judge's. As history, every standing objection on a subject or unit that a declared lineage links to the one asked is supplied too. A re-review brief carries the earlier review findings on the same plan subject that no later independent, acting, unvetoed review records `RESOLVED`, and a plan-acceptance brief the standing rejections naming any item of the plan subject, at any revision, or an item revision elsewhere with the same prose and fixed fields, whole; policy may withhold a carry only where the re-review's independence requires it, and the brief then says so.

**Constructed independence.** The Dispatcher launches every review in a fresh context distinct from the authoring task's and the contract author's, selects a judge outside the authors of the judged content (§5.10 (b), (f)), and records lineage class, model family, route and toolchain. Independence fails closed (§12.2). Where a claim relies on independence, the review records material common-mode dependencies (model family, source corpus, toolchain, oracle); policy may require a different model family or a distinct evidence route for high-consequence surfaces. *Residual:* the artifact under review can carry its author's framing in comments and docstrings; that is content to review.

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

Three transports expose the same operations: an MCP server; the CLI (`ssds <operation>`, §26.3); and a **Git-envelope** transport for zero-context web agents: an immutable signed task envelope `task.json` plus the rendered brief on an isolated run ref `refs/heads/ssds/run/<task-id>`, a result envelope `result.json` plus candidate commits written back to that ref, and polling-first fetch of that specific ref. Run refs are transport: never merged, retired by policy, regenerable from the ledger and obligations. Harness adapters only map operations and launch, observe and cancel executions (admit, start, events, control response, cancel, terminal result, §26.4). The bootstrap is `Execute SSDS task <task-id>` plus the minimum locator the environment does not already bind (repository, run ref, envelope path, protocol source). It fails truthfully when protocol material cannot be resolved. Transport and process success never imply evidence admissibility or task success. Local and Git-envelope transports give identical admissions for identical submissions.

#### 16.11 Project Engineering Memory [D3 decision; amendment A10]

This section is the one owner of how SSDS realizes the governing PEM contract: which of its occasions machinery detects, what a task owes when one fires, what machinery derives from memory, who accepts what machinery cannot decide, and what follows. PEM meaning (the activation predicate and its qualifiers, retrieval, the HAS shape, binding meanings, admission, maturity and claim strength) stays with the PEM owners at the governing source (S8). Nothing here adds a PEM field, a memory store or a judgment, and every other section that touches memory points here. This section fixes capabilities, holders, force and acceptance boundaries; the reader's exact facts and failure causes, the revert predicate, route resolution before genesis, term normalization and ranking, slot schemas, decision keys and outcome lists are catalogue §16.11 mechanism. *[Amendment A10, SD-63.]*

**(a) Memory is content; its acceptance is recorded; its facts are derived.** Policy names the PEM subject, the root unit and its partition units (`pem_root`, §5.1), by default the unit that owns the project's discovery root. With none named, no PEM fact is derived and every PEM duty stays at the level the injected PEM owner text gives it (E3). The **accepted PEM publication** is the revision of that subject named by its latest standing acceptance in its current tenure: an `ACCEPTANCE` of a `NATIVE` subject, or, for a `LEGACY(p)` or `UNGOVERNED` subject, a `LEGACY_ACCEPTANCE` citing the project's own PEM acceptance evidence (§19.2), each by the actor policy designates under PEM governance (§3.5). It is never inferred from the observed tree, a path or a parse: an absorbed foreign change (§8.6) or a candidate changes no accepted publication, and the two coincide only where the project's acceptance process makes them coincide. With no such acceptance there is no accepted publication. PEM content that differs from the accepted publication, whether observed in the admitted state or a candidate's in a frame `D_n[X]` (§7), is a **candidate overlay**: composed against the publication only when it validates, visibly candidate, unable to erase an entry by omission, and seen only where it is observed. A pinned, data-only **PEM reader**, an analyzer in the sense of §5.9 that never executes content or instantiates objects from it (T2), reads the accepted publication's content, which the ledger keeps reachable (§21.4), and any overlay. It derives the facts the decisions below need: for every family and notice its identity, kind, state, authority binding, owner routes, normative status, applicability (tags, and typed bindings where the schema defines them) and lineage; its **record identity**, a digest of its complete canonical record; and the **reader state**, `READABLE`, or `UNREADABLE` with a cause (no accepted publication, absent, unparseable, unsupported schema, partial or conflicting composition). These **PEM facts** are S3: cached only in the derived index, rebuilt like derived relations, never stored in a record (P3). No copy of memory exists, so none can disagree with it. The reader is not schema authority: what it cannot read with certainty makes it `UNREADABLE`, never a guess. When the publication's root names another project than the one genesis records (§19.9), every entry is **foreign**: shown as external or historical evidence, never an owner-bound or typed candidate, its owner routes external, until project governance reconciles lineage and an accepted publication records it.

**(b) Occasions.** Machinery detects these occasions of the PEM activation predicate, each in its own clause's words:

| Occasion | Detected from | Effect |
|---|---|---|
| a plan item explicitly binds relevant memory | the item contract's `memory.bind` (§13.1), whose relevance plan acceptance judged | memory **activated** |
| migration | item kind `MIGRATE`, or `change_intent` contains `migration` | **assessment** |
| rework of mature semantics or concretization; replacement or consolidation of mature machinery; optimization or scaling | `change_intent` contains `rework`, `replacement`, `consolidation`, `optimization` or `scaling`; or the write scope intersects units policy tags `mature` | **assessment** |
| revert or restoration | `change_intent` contains `revert` or `restoration`; or, on the candidate, a unit of its effect-keyed write set returns to a revision it held at an earlier admitted position other than its current one, or the candidate restores a subject (§19.4) | **assessment** |
| recurrence | recurrence detection (§15.7), on the `COORDINATE` decision it creates | **assessment** |
| any further occasion policy adds as a trigger (§5.1), for example a non-empty tag match | policy | **assessment** |

An assessment occasion never activates memory by itself; it requires the task to judge the clause's qualifier ("substantial", "mature", "where prior choices matter"). Occasions machinery cannot detect stay agent judgment under the injected owner text (E3): suspected recurrence that detection has not found; history that can materially change a decision; a revert, restoration or recovery neither declared nor byte-identical. An agent may activate memory on any task where the predicate's own conditions hold, and returns a HAS when it does.

**(c) What a task owes.** When any occasion fires, the brief carries the PEM owner text (§16.3), the reader state, and the candidates of (d) as `HISTORICAL` items with their match path and binding state, and the result owes two slots (§13.5). `pem_activation` holds one answer per fired assessment occasion: activates or not, with a content reference to the reason. `historical_applicability` is owed when the binding occasion fires or any answer activates: a content reference to the HAS in its canonical shape (in the durable home the governing work names, otherwise the result envelope), whose typed part is the three `pem_basis` identities and each dispositioned entry's identity and disposition; reasons stay in the home (§16.4). `HARD` `OBLIGATION` templates check that every fired occasion has an answer, that the HAS dispositions every candidate the recorded brief listed (§16.4), that its basis identities are the accepted publication and overlay of the state it was made in, and its freshness (f). They establish presence, coverage, identity and freshness only; whether a judgment, a disposition or the search behind it is adequate is review's (E3). Candidates are a floor: the bounded canonical-metadata search the PEM owner requires is still owed whenever memory is activated. An occasion detected only on the candidate (a revert, a restoration) triggers the slots at conformance, and a result without them is `INCOMPLETE` (§14.4).

**(d) Candidates.** In a state, a task's candidates are: (1) the entries its contract binds; (2) **owner-bound** entries: `AUTHORITY_BOUND` families, owner-recorded `PROPOSED_FOR_PROMOTION` families and normative notices whose owner route resolves (e) to a unit the brief carries as `GOVERNING` (§16.2), whatever their binding state; (3) **typed matches**, where the schema defines owner or surface bindings: those resolving to a unit of the task's subjects or write scope (mechanism and regime bindings are shown, never matched, because SSDS holds no mechanism or regime facts); (4) **tag matches**: exact equality, after the catalogue's normalization, between the contract's `memory.terms` and an entry's applicability tags. Match-path candidates (3, 4) are capped (§0.6), selected by a deterministic function of the terms and the PEM facts; a truncation is shown with the omitted count, and the result says whether the agent widened its search. Bound and owner-bound candidates are never truncated and never count against the cap. In a frame, the candidates are the union of those derived from the accepted publication and from the overlay, each entry the overlay changes or retires marked so. Foreign entries are never owner-bound or typed candidates. Completeness is declared only for owner-bound candidates and only over resolved routes; an empty candidate set is rendered "no candidate", never "no applicable memory" (S5).

**(e) Owner bindings and reverse impact.** An owner route **resolves** when it names this project and its path and section locate a governed unit (§1.11); the entry is then bound to that unit at the content the route's revision gives it. A route that names this project and locates no unit is **unresolved**; one naming another project is **external**. A binding's **reference position** is where the publication that first carried the entry's current record identity took effect in project history, not where SSDS learned of it: for a native `ACCEPTANCE`, that acceptance's position; for a `LEGACY_ACCEPTANCE`, which imports an earlier acceptance fact (§19.2), the earliest admitted position whose observed integration head contains the accepted revision, or genesis when the revision predates it. Importing, re-importing or requalifying an unchanged publication, or a new tenure of the PEM subject over it, therefore never moves the reference position; only an accepted publication that changes the entry's record does. In the admitted state a resolved binding is:

- **stale** iff, at its reference position or some later admitted position, the owner unit's subject was valid (§5.5) at content that is neither the bound content nor reached from it by a path of current `EDITORIAL` or `REPRESENTATION` equivalence judgments (§4.4): an accepted owner change happened, whatever the owner's content is now, so a change later restored still counts;
- **current** iff it is not stale and the owner's subject is valid now at the bound content or content so reached;
- **review required** otherwise: the owner subject is not valid now, or only provisionally; or the interval from the reference position crosses a recorded loss boundary (§23.6), whose abandoned positions history does not hold, until an accepted publication after the boundary changes the entry's record.

The test reads admitted history through historical views (§5.8), a bounded derived query over the ledger, so it does not depend on the reader having been readable in between. Machinery decides only byte identity, so every owner change without such an equivalence counts (failing closed). In a frame, a binding to content the candidate changes, or to an owner valid there only by a prospective acceptance, is review required: candidate content never makes an authority binding current. Only a current binding is shown as healthy; every other state is shown wherever the entry appears (candidates, `HISTORICAL` items, `memory(x)`), and the PEM owner's rule that an unhealthy binding carries no retained force applies. Reverse impact covers every `AUTHORITY_BOUND` family, owner-recorded `PROPOSED_FOR_PROMOTION` family and normative notice of the accepted publication whose route resolves, whether or not any task is open: each stale binding derives a `COORDINATE` decision for the standing plan's principal (§12.5; the human where there is none), one for each accepted owner change after the reference position, keyed on the entry, the owner unit and the admitted position of that change, whose brief carries the PEM owner and its schema-governance owner, with outcomes `AMEND` (whose plan change follows in the same request, §15.5: an item that reconciles the entry through PEM governance by confirming, remapping, downgrading or retiring it), `CHALLENGE` (against the owner change) or `ESCALATE`. Answering the decision does not make the binding current: only a later accepted publication that changes the entry's record moves its reference position, and each further owner change derives its own decision, also while the binding is already stale. Reverse reconciliation for owner-recorded `PROPOSED_FOR_PROMOTION` families is stronger than the inherited duty, which names `AUTHORITY_BOUND` entries and normative notices; it gives a proposal no force. A candidate that would make a binding stale lists it in its review brief (§16.5) and in `impact(diff)`. External and unresolved bindings, and the part of an interval before genesis, stay under the inherited reverse-reconciliation duty (E3); an interval across a loss boundary is review required, as above.

**(f) Freshness.** An entry's **dependency identity** is a digest of its record identity, the root fields that qualify every entry (schema, coverage, accepted base and overlay identity), and the states the reader derives for its routes (binding states under (e); evidence-route availability where retained content lets it decide). A HAS is **fresh** in a state iff every entry it dispositions and every entry that would now be a candidate of the task has there the dependency identity it had at the HAS's basis; an entry new since then is not. A material change to an entry (its claim, evidence rows or assessments, coverage, maturity, guidance or binding health) therefore stales exactly the HASes that depend on it, and a change to an unrelated entry stales none. Dependencies the reader cannot establish mechanically (an external evidence artifact, a material change outside memory) stay with the PEM owner's refresh duty (E3). A `HARD` `OBLIGATION` template checks freshness in the state the result is evaluated in (§14.1): the candidate's frame, re-derived after every clean rebase and at every revalidation of an integration request, including the one after an absorption (§11.5, §8.3 step 9); for a result without a candidate, the admitted head at its admission. A stale HAS makes the result `INCOMPLETE` and takes that class's route (§14.4); the next iteration's brief names the entries that changed. Because integration requires clean conformance on the rebased candidate (§8.3 step 7), a memory or bound-owner advance before integration cannot close work on an obsolete HAS. After integration the freshness verdict of the integrated enactment stands as decided: later memory reopens no closed work, while the obligation's ordinary terms still follow §10.4.

**(g) Memory unavailable.** The reader state that counts is the one in the state the result is evaluated in; the brief states the state at issue, and if memory recovers or breaks during a task, that evaluation decides. While it is `UNREADABLE`, no candidate is derived, and a slot owed under (c) or (h) may be `NONE` with the typed reason `PEM_UNAVAILABLE`, and only then: the template compares the reason with the derived reader state, so the claim is corroborated by derivation, never by assertion. Such an answer states an uncertainty that only an independent judgment or a human accepts:

1. **Work under review.** Where an independent review judges the result's work (a transformation, item-level or integrated-result review), the result itself carries no passing judgment or decision. The review's brief carries the uncertainty as a required review item (§16.5), and Admission admits a passing judgment of that review only with its typed acceptance of the uncertainty (a result-only `HARD` template, §8.3 step 7); a review that rejects it does not pass. The work's permissive effects all pass through that judgment.
2. **Every other result** (records-only work, a coordination decision, a judgment, including a reviewer's own result that states the uncertainty). Admission refuses every passing judgment and principal decision in the request, as for a non-clean result (§8.3 step 7), while the result and its never-lost records are admitted, unless the result cites a standing `HUMAN_DECISION` that accepts the same uncertainty, the same reader-state cause, for the same obligation. In that case the citing record carries a `standing` basis entry on that decision (§4.1). `HUMAN_ATTENTION` is derived, keyed on the obligation and the cause (§10.2). The obligation is shown waiting on it and is not dispatched again until the human decides or the reader is `READABLE` (§10.3). After an acceptance, the next task's result cites it, and its passing judgments and decisions are then admissible. After a rejection, the obligation waits for a readable reader.

No permissive effect of a result that states an uncertainty therefore exists before the uncertainty is accepted. A refused judgment supports nothing at S2, plan coverage (§11.2) and subject validity (§5.5) included, and a refused decision answers nothing. The stratum order is unchanged: Admission refuses, and S2 reads only the admitted human decision, positively, through a basis entry. Never-lost records (adverse judgments, reports, challenges) are admitted whatever the uncertainty. Work that does not depend on the obligation proceeds, so memory is never a single point of failure. An acceptance binds one uncertainty for one obligation: the accepting review's or human's own record owes no further acceptance of it. While the reader is `READABLE`, the PEM owner's other fallbacks remain the agent's: dispositions may be `REVIEW_REQUIRED`, and partial coverage is handled by bounded intake or stated uncertainty (E3).

**(h) Closeout learning.** The results of an item whose kind is `REPAIR`, whose `change_intent` contains `rework`, `replacement`, `consolidation`, `optimization`, `scaling`, `revert` or `restoration`, or whose candidate carries a detected revert or restoration owe the slot `closeout_learning`: `NOT_MATERIAL` (a first clean local defect with no recurrence or generalization signal, or no material change), `NO_UPDATE`, `UPDATE_PROPOSED` (a content reference to the proposed memory change) or, under (g) and with (g)'s acceptance, `NONE` with `PEM_UNAVAILABLE`; each but the last with a content reference to its reasoning. `migration` alone does not owe it, because the PEM owner's closeout clause does not name it. An `UPDATE_PROPOSED` answer derives a `COORDINATE` decision for the plan's principal with outcomes `AMEND` (a plan item that changes memory under PEM governance) or `DECLINE` with a reason. No answer writes, admits or promotes memory. An under-classified change (a material repair answered `NOT_MATERIAL`, a rework planned without an intent) is for review and for later recurrence detection; the risk is accepted (§32.2).

**(i) Limits.** Machinery never judges applicability, a qualifier, recurrence, materiality, adequacy or admission; never writes, admits or promotes memory; never treats observed or candidate content as accepted memory or an accepted owner; never copies lesson text into a record or brief beyond entry identities, digests, enumerations and content references; and never derives from a PEM entry an obligation that blocks or closes a D1-D4 subject. Only (e), (g) and (h) derive decisions or human attention, and each goes to a principal or a human.

## Part VI. Evidence and intake

### 17. Evidence

| SSDP evidence concept | SSDS 8 representation |
|---|---|
| specification | an `EVIDENCE_SPEC` unit with `EVIDENCES` -> the unit holding the claim, declared or derived `EXECUTION_DEPENDS_ON`, and its specification declaration (§17.1) |
| realization | a `REALIZATION` observation whose basis has a **target** part (the claim's content) and an **execution** part (executed content, §6.3) plus the configuration fields (§17.2) |
| observation | the realization's evaluated outcome, by content identity, plus references to native artifacts (logs, data) |
| assessment | an `EVIDENCE_ASSESSMENT` judgment; a reassessment replaces an earlier one only by authorized supersession (§8.3); a counting failing assessment and a passing assessment for one obligation are a disagreement (§6) |

#### 17.1 Specification declaration [D3 decision]

Every `EVIDENCE_SPEC` unit carries exactly one specification declaration, part of its revision and of every reading: its oracle kind (declarative, embedded or assessor-read, §6.5), designated runner class, time bound, declared outputs with canonical forms, verdict templates over them, the **fixed** attributes (regime, parameter instance, and any backend, precision, environment identity or seed policy it declares), its assessment granularity (single or ensemble, with replicate count, statistic and seed policy), and output renames. Fixed attributes are **claim-defining**: a realization differing in one is inadmissible. Every attribute not fixed is **free** (execution variation); the D2 owner of the claim decides which are claim-defining, and free is the conservative default for disagreement. A fixed environment names a content-addressed environment identity; a recorded attribute it does not determine stays free. A change to a specification raises `SPEC_REVIEW` for its owner, whose brief lists the counted failures it would make stale and the readings it would stop covering.

#### 17.2 Realization basis fields

A `REALIZATION` records its specification and claim revisions, its recorded execution basis (§6.3) read once by every consumer, any unpinnable reads, its configuration, its recorded execution attributes (the basis's attribute entries, never a second field), its runner, its tree, its positions, and either its evaluated outcome in the ledger store or `INCOMPLETE` with an enumerated reason. Logs and data stay in native artifacts by reference. An incomplete realization enters no `PASS`/`FAIL` assessment; process exit or harness success is never admissibility.

#### 17.3 Evaluated outcomes [D3 decision]

The evaluated outcome is a canonical JSON object `{output name: value}` over the declared outputs, stored as a `LEDGER`-store object (§21.4). Canonical forms: `binary64-hex` (IEEE-754 bit pattern, exact), `decimal-shortest` (round-trip shortest decimal), `rounded:<n>` (declared rounding to `n` significant digits, a D2 decision of the specification's owner), integers, booleans, enumerations, and `digest` (a content identity of a large output artifact). An `ENSEMBLE` outcome is the declared statistic over the replicates plus the replicate count; replicate-level outputs are native artifacts. Identity of outcomes on failing outputs (§6.6) is byte equality of canonical values.

#### 17.4 Admissibility and currency

An assessment is **admissible** for obligation `e` iff its realization instantiated the specification revision `e` names (or a revision in its lineage under the reading rules of §6.6), every fixed attribute matches that revision's declaration, and the realization is complete. A realization supports a claim at revision `c` only while its recorded execution basis is satisfied (`execution` mode, §4.1: the recorded regions unchanged, or an equivalence judgment of class `CONSUMER:REALIZATION` covering each changed unit) together with its bounding completeness judgments, and its target is `c`. An execution-dependency change triggers a rerun obligation, including the configuration of every failing assessment counted against the claim (§6.9); a target change triggers an assessment-review obligation. Stale passing evidence never discharges. Failing evidence is never dropped by a change (§6).

**Binding health.** `AVAILABILITY` observations record when a referenced artifact becomes unavailable: the historical record survives, and present use becomes `UNAVAILABLE` (an evidence term that needs it is not `T`). Raw data stays in native stores; the ledger stores identities and bounded classifications.

**Realized-record/observation boundary.** A realized-record item is an observation only when an evidence realization produced it; retaining it neither assesses nor re-identifies it. A `CHALLENGE` carries the finding's inquiry status (`EXPLORATORY` or `CONFIRMATORY`) as its own attribute, separate from evidence strength, applicability and disposition. Findings and tensions keep their one canonical home in project evidence records or native issues; the ledger references that home by identity and never becomes it (S13).

#### 17.5 Who may realize evidence: runners and custody [D3 decision]

A realization discharges an evidence obligation only when a **designated runner** of the specification's runner class executed or reproduced it: **Dispatcher-controlled** (an isolated workspace the Dispatcher owns, the exact tree in the §1.5 representation, a registered runner key) or **external custody** (an HPC scheduler, CI service or laboratory system designated by policy, whose records cite custody evidence and whose observations make a failure stale only after its custody enumeration lists every run of the configuration). **Recorded execution attributes and read observation [SD-17, SD-18].** Each runner class declares the execution attributes it records (environment components at a stated granularity; backend, precision, device and host attributes; every seed it supplies) and whether it observes every read outside the tree; an execution of a class that does not, or that misses a declared attribute, counts as having an unpinnable read, so its failures support no mechanical stop and go to the owner. Variation in an attribute no class records is invisible to matching, a disclosed residual (§32.2). *[Amendment A6, SD-55.]* A declared attribute the Dispatcher cannot request (a node identity) can leave matching reproductions and observations unavailable or hard to obtain for a failure of its class, since only executions that happen to record the same value can serve; observations that do match still serve. A change of a class's declared set, by contrast, makes every failure recorded under the other set unmatchable for the stop conditions; the policy change that makes it shows those failures. Declared attributes should be requestable where the runner allows. Results an agent reports from its own workspace are findings, never admissible for discharge; a `CHECK_EXECUTION` is evidence for a scientific claim only where an evidence specification names it.

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

A quarantined delta becomes effective in exactly one way: an admission request carries an `ABSORB` disposition adopting it, which makes it part of its transformation's identity, and Admission validates it exactly as if the requester authored it now (challenge freezes, enactment condition, mode consistency, SDG integrity). Adoption is re-authoring under current rules, never ratification of presence. **Realignment** is an ordinary change that makes the declaration equal admitted structure. **Contrary dispositions.** A later standing adverse disposition of an enacted `ABSORB` vetoes its support but does not undo the enactment: it derives the owner's adjudication and, where upheld, a realignment obligation; an `ABSORB` of a delta under a standing adverse disposition is refused, so neither order lets enactment outrun a standing objection. A `QUARANTINE` disposition names observed paths of its intake object; a subject owning any byte of those paths is treated as `UNCLASSIFIED` for governing use while the disposition stands, and content moved out of the paths leaves it (§32.2). **[D3 decision]** Where policy enables it, the Dispatcher may adopt a governance-neutral delta as a recorded, challengeable machinery disposition; a governance-affecting delta always needs an R2 disposition.

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

Agents may propose candidate D1-D3 units reconstructed from D4 behavior, papers, comments, tests and history; a proposed upstream unit is accepted only through its owner's acceptance, descendants relying on it stay provisional meanwhile, and no D4 behavior creates accepted authority. Reconstruction that cannot recover intent records `PROVISIONAL` or `UNKNOWN` (M5).

A **cutover** of a subject from `LEGACY(p)` or `UNGOVERNED` to `NATIVE` requires: (1) reconstruction status at the policy minimum (§0.6); (2) a current `MIGRATION`-class equivalence stating that only representation changed, or a separately governed change; (3) the owner's prospective acceptance of the native revision in the carrying frame; (4) for a carve-out, promotion first and the legacy process owner's release (§19.6); (5) a quiescence record listing every known in-flight legacy run on the subject as drained, pinned or migrated, attested complete by the human gate (M6); (6) the human-gated cutover decision. **A cutover is carried by an integration [D3 decision].** The carrier is a transformation of an accepted item naming the subject (an `AUTHOR` item for D1-D3, a `MIGRATE` item otherwise, possibly with an unchanged tree); the cutover `MODE_TRANSITION` is a human record in the carrier's frame, admitted only while that enactment has not integrated and only once per enactment; conditions 1-6 are enactment conditions checked at the carrier's integration, which enacts the transition. After cutover only Admission governs the subject; legacy-side edits are foreign changes (§18). A cutover whose carrier is then fenced or overtaken leaves the subject `NATIVE` on legacy bytes and invalid until re-applied as a new enactment or rolled back (§32.2).

#### 19.6 Carve-out release

A `LEGACY_RELEASE` is a human-gated lifecycle record by the actor policy designates as the legacy process owner for `p`, naming the exact scope released from the legacy process. It is required before a carve-out cutover and enacts nothing else.

#### 19.7 Version rollback

Rollback is version rollback to the immutable pre-cutover baseline (B2): stop Admission for the affected scope, resume the pinned baseline process there (resolved from `PROTOCOL-RELEASE-STATE.yaml`, never guessed), repair SSDS separately. The `MODE_TRANSITION` back to `LEGACY(p)` ends each affected subject's tenure, so pre-cutover legacy imports never revive; a fresh `LEGACY_ACCEPTANCE` is needed. Ledger rollback (§23) is an integrity incident, not a version rollback; an unrecoverable admitted loss adds a boundary, which composes with a later version rollback because the mode change ends tenure and the boundary withholds every pre-loss import independently. A cutover lost inside an abandoned interval leaves the retained mode in force, with every retained import withheld until requalified.

#### 19.8 Documents, workplans and skills after cutover

Change plans and authority documents remain semantic artifacts. In natively governed documents, lifecycle fields (`status:`) and directory placement (`active/`, `archive/`) are removed or generated from derived state and marked non-authoritative; a manual edit to them enacts nothing. Skills remain epistemic procedures and stop owning workflow transitions represented by rules. The PEM owner text is injected whole (§16.3); no memory duty is removed from it because §16.11 realizes part of it mechanically, and §29.6 lists the parts that stay judgment. *[Amendment A10, SD-63.]* Historical pre-cutover workplans and records stay immutable under their original semantics.

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

SSDS governs one ledger per project and provides no atomic admission across repositories; cross-repository projects couple through immutable pins. An `EXTERNAL` unit's scope is one pin: a Git repository identity, full commit and region; a package ecosystem, name, exact version and digest; a dataset digest and locator; or a DOI with variant and locator. Its content never changes, so reliance on it never goes stale; a change of pin is an ordinary local change. A read outside the realization's tree, other than an environment component the runner class records, is an external read, pinned by the same grammar where possible.

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

Each ledger entry is one Git commit on the authoritative ledger ref whose tree holds the entry as canonical JSON, an Ed25519 signature by the appending Admission host key, and the ledger-store objects the entry introduces (evaluated outcomes, refused record bytes). The entry carries the ledger identity, its position, schema, the digest of the previous entry, its kind (admission, absorption or lifecycle), the appending host key and process incarnation (§22.3), the observed integration head `obs` (§22.1), and its admission, absorption or lifecycle content and records. The authenticated chain is the digest chain plus signatures; Git's commit chain is transport and must agree with it (a mismatch is corruption, §5.7); commit metadata is fixed and never read. **Reachability.** An entry commit's further parents are every commit it newly references (base, admitted, observed and candidate commits, fence commits, the trees realizations ran on), so the ledger keeps every content commit it references reachable and product-ref force-pushes or deletions cannot make history underivable.

#### 21.3 Append and durability [D3 decision]

The append is a compare-and-swap of the single ledger ref from the expected previous entry: a durable local reference transaction for a local authoritative repository, or a push with an explicit expected old value to a remote authoritative replica. No multi-ref capability is needed. The declared crash model is process crash and operating-system crash or power loss of the authoritative host; loss of a remote server is covered by the witness quorum (§23). A losing writer revalidates against the new head (§9.1).

#### 21.4 Retention of referenced objects and evaluated content

The ledger retains every entry, every `LEDGER`-store object, and reachability of every referenced commit for its lifetime. Evaluated outcomes and the trees on which failing and reproducing executions ran are therefore always available to derivation (§6). Native artifacts referenced by `REPO`, `HOME` or `RUNNER` references are not retained by the ledger; their unavailability is a binding-health event (§17.4). Nothing referenced is purged except under the confidentiality protocol (§24.2), which weighs later scientific judgment before any irreversible purge.

#### 21.5 Location options [D3 decision]

Genesis chooses one: (i) the reserved ref `refs/ssds/ledger/<ledger_id>` in the project repository; or (ii) a dedicated ledger repository (for example private, when governance records must be more private than the product), on the ref `refs/ssds/ledger/<ledger_id>`. Semantics are identical. **[A7, SD-56]** The default is (ii), with the ledger repository in the operator's SSDS home (§26.3), so governance records never mix into a product or program repository; (i) applies only when a genesis declares it. Genesis names the **authoritative replica** (repository URL and ref); a change is a human-gated `REPLICA_REDESIGNATION`.

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

**Publisher.** Each Admission process takes a random incarnation identity when it starts and records it, with its host key, in every entry it appends. The publisher of admission `n` is the incarnation named in entry `n`; only it, during its lifetime, performs the effect `B_n -> C_n`, at most once, tracked in its own memory. No durable attempt log exists, so copied, restored, shared or inherited operator state cannot authorize a publication.

**Fencing.** Any other incarnation that finds the integration ref still at `B_n` with the publication pending appends, after the takeover wait (§0.6), a **fencing absorption**: an absorption of `B_n` classifying `n` as overtaken and carrying the effect `B_n -> F` to a fence commit with `B_n`'s tree, performed by its own publisher. Exactly one compare-and-swap from `B_n` can succeed. A fence restores `tree(B_n)`, so every `NATIVE` D1/D2 subject `n` changed is back at its earlier revision in a new run, and re-applying `n` is a new task and enactment (R12).

**Settlement.** An admission is **settled** once some later admitted entry observed the ref away from its base. Human attention for an ambiguous admission is raised when its first fence is admitted, and the human decision on it is admissible only once it is settled: re-apply or keep the fence, or, if the publication landed late, accept it or revert by an ordinary admission. **ABA policy.** A foreign reset of the ref to exactly `B_n` is indistinguishable from a publication not yet applied, so every such state outside the publisher's first attempt is fenced; a foreign return to `B_n` while a stale publisher resumes after a fence is detected as `LATE_PUBLICATION`, never prevented — a disclosed residual. **Idempotency and replay.** The effect identity is fixed by entry `n`; a compare-and-swap from the exact predecessor never overwrites foreign work; classification reads only commits the ledger keeps reachable, so replay explains every publication from the ledger alone. The procedure and every failure point are catalogue §22.3.

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

A faulty witness may be lost, rolled back or adversarial; genesis and every redesignation reject parameters violating the inequality. The deployment classes are `LOCAL_TRUST` `(1, 1, 1, 0)` (one witness on another medium, not rolled back with the replica), `TEAM` `(3, 2, 2, 0)` (three administrative controls) and `HARDENED` `(4, 3, 3, 1)` (one faulty witness tolerated), each premise stated in status views. Witnesses are append-only Git refs on separately administered hosts, append-only directories on another medium (local trust only) or transparency logs; acknowledgment means durable retention. They hold Admission-signed checkpoints of entry digests and human-gated retirement statements, append-only per ledger; any participant may relay an authenticated checkpoint (read repair), which can complete a quorum but cannot forge one.

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

The only narrowing of a loss boundary is accountable. A `CONTINUITY_ATTESTATION` is a human-gated challenge-tier judgment by an actor policy designates, naming a `LEDGER_LOSS`, a scope either **complement** (everything except the listed possibly affected subjects and records) or **explicit** (only the listed ones), and evidence references (hosting audit logs, notifications, CI artifacts, operator journals, a surfaced abandoned chain). While in force it holds what it covers, and dependents follow through S2. Any qualified actor may challenge it; an upheld challenge withdraws it permanently; a later boundary withholds it like any relaxer. It is the only way a pre-boundary record becomes current again without a fresh record, and never an inference from agreement between product and ledger.

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
ssds.core (Level 0 Core)        imports nothing from the SSDS components or the root module
```

Also enforced: no derivation module reads the clock, the network, environment variables or the live integration ref (an import allowlist); every SSDS file lives under `orchestrator/`; one composition root, the root module (§26.3); no private cross-module imports. Fitness checks are sensors of the dependency rule, not architecture truth.

#### 26.3 Deployment and composition [D3 decision]

- **One program, one composition root [A7, SD-56].** SSDS is one program named `ssds`: one distribution, one import package and one command. The root module (`ssds.cli`, outside `ssds.core`) is the only composition root per installation. It composes the Level 0 Core (`ssds.core`) and the SSDS components and mounts one flat command set:
  - Core's version-bound commands, with their accepted behaviour: prompt rendering, the profile stage commands, `projects`, `capabilities`, `doctor`;
  - the SSDS operations: `open`, `ask`, `read`, `report`, `submit`, `decide`, `status`, `inspect`, `admission serve`, `dispatcher serve`, `mcp serve`, `genesis`, `qualify`, `export`.

  A name claimed by both is a defect caught in acceptance. Core never imports the SSDS components or the root module, and Core's own acceptance runs without them (1.6.0 invariant 12, PC-001). Other extensions register through the versioned entry-point group `ssds.extensions.v1`. The former program names (`sdp`, `sdp_orchestrator`, `sdp-orchestrator-core`, `sdp-orchestrator-ssds`, the group `sdp_orchestrator.extensions.v1`) are retired without alias. Identifiers inside frozen profiles and persisted records (for example `sdp.content.v1`) are data, not program names, and do not change.
- **Packaging [A7].** Distribution `ssds`, built from `orchestrator/` (containment root unchanged), as a regular package `ssds`: one distribution needs no namespace package. It contains `ssds.core` and one subpackage per component. Public surfaces are `ssds.api.v1` (logical operations and records) and `ssds.spi.v1` (harness adapter, runner, witness and analyzer provider contracts); Core's are `ssds.core.api.v1` and `ssds.core.spi.v1`.
- **Processes.** Admission and the Dispatcher run as long-lived local processes started through `ssds … serve`; Interface hosts (CLI, MCP) are short-lived or long-lived; Derivation is a library. Multiple Admission hosts may exist; correctness comes from the ledger compare-and-swap and witness quorum, not from leader election.
- **Program and operator data [A7, SD-56].** Program code and protocol references are immutable package content. Everything SSDS writes for an operator lives in one **SSDS home** outside every repository: `$SSDS_HOME`, by default `$HOME/.ssds`. It holds:
  - configuration (`config.toml`);
  - ledger repositories, by default one per project (§21.5 (ii));
  - witness stores for `LOCAL_TRUST`;
  - the derived index and caches (§21.6);
  - Dispatcher workspaces, and operator state and journals.

  SSDS keeps none of these inside a product or program repository. Core's configuration owner (defaults -> config/profile -> environment allowlist -> explicit CLI/API) holds operator-local SSDS settings in a namespaced `[ssds]` section: repository and ledger locations, key references, harness routes, runner endpoints, witness endpoints. Secrets are references, never values. There is no earlier installation to detect or migrate (SD-57). Project policy is not configuration: it is governed content adopted by the ledger (§25.3).

#### 26.4 Executed supersession of Architecture 1.6.0 for SSDS-governed scopes [D3 decision]

On acceptance of this Manual, `orchestrator/docs/architecture.md` (Architecture 1.6.0, frozen) is superseded **for SSDS-governed scopes only**. For version-bound older work, the implemented Level 0 Core keeps its accepted behavior unchanged (its program names and configuration location change by A7, its behavior does not): one composition root, version/profile-separated source resolution, frozen historical profiles, versioned JSON records, no cross-version substitution (PC-001). The frozen document is not edited. The Tracker, Adapter and Scheduler levels were never implemented, so no Level 1-3 data migrates; their functions are preserved below.

| # | 1.6.0 product invariant | Final disposition for SSDS scopes |
|---|---|---|
| 1 | progressive usefulness; Core alone complete | **Replaced**: staged usefulness (read-only derivation and interface useful without Admission); document-only operation is not complete for native scopes (§19). **Preserved** for version-bound work through Core prompt mode |
| 2 | `core <- tracker <- adapters <- scheduler` | **Retired** with the ladder; **replaced** by §26.1-§26.2 dependency direction |
| 3 | graceful degradation without silent policy bypass | **Replaced**: degradation is truthful non-closure plus read-only derivation, labeled `UNQUALIFIED` or historical; no-silent-bypass **preserved** |
| 4 | one CLI and one composition root; extensions via versioned SPIs | **Preserved and closed**: one `ssds` command and one composition root, the root module (§26.3, A7); no second root |
| 5 | versioned public boundaries | **Preserved**: `ssds.api.v1`, `ssds.spi.v1`, `ssds.core.api.v1`, `ssds.core.spi.v1` (A7) |
| 6 | no duplicated workflow authority | **Replaced**: ledger plus Admission is the single workflow authority for native scopes; workplans and profiles keep transitions only for `LEGACY(p)` |
| 7 | manual operation is first-class | **Replaced in part**: manual invocation and the Git-envelope route stay first-class; manual results enter by admission; manual document control is not complete for native scopes |
| 8 | capability recommendation precedes resource scheduling | **Retired** as a module boundary (both in the Dispatcher); substance **preserved**: recommendation evidence never acts as quota or resource authority |
| 9 | benchmark observations preserve context | **Preserved and closed**: the Dispatcher's route-recommendation evidence keeps source, benchmark and version, model identity, effort, harness and configuration, value with uncertainty, generated and fetched time, freshness and identity-match quality (`EXACT_CONFIG_MATCH`, `MODEL_EFFORT_PROXY`, `MODEL_ONLY_PROXY`, `UNRESOLVED`), in operator state; never derived workflow state; incompatible metrics are never combined into one scalar |
| 10 | scheduler subordinate to workflow intent | **Preserved and strengthened**: the Dispatcher acts only on derived-ready obligations and cannot affect derived state |
| 11 | private state outside project repositories | **Replaced in part**: operator state private, in the SSDS home outside every repository (§26.3, A7); the closed-schema ledger in a Git repository designated at genesis, by default a dedicated ledger repository in that home (§21.5, A7), which may be private |
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
| §3 capability ladder and distributions | **Retired**; Level 0 Core **preserved** for version-bound work as `ssds.core`, inside the one distribution `ssds` (§26.3, A7) |
| §4 repository layout, Python packaging and namespace | **Replaced in part (A7)**: one distribution `ssds` under `orchestrator/`, a regular package with `ssds.core` and `api.v1`/`spi.v1` (§26.3), so the PEP 420 namespace is retired; cross-module imports only through public API/SPI |
| §5.1 API versus SPI | **Adopted** |
| §5.2 compatibility | **Adopted**: a public major is a semantic contract; persisted schema, ledger schema, ruleset, interface and profile versions are independent dimensions (§28) |
| §5.3 public records | **Adopted** with SSDS canonical JSON (RFC 8785) for records; timestamps UTC; IDs opaque; digests carry algorithm, scheme and value; unsupported required semantics fail; records never hold live objects |
| §5.4 pagination | **Adopted** for `ask` results, history and inspector listings |
| §5.5 problems/errors | **Adopted**: `Problem{code, message, retryable, details}`, codes namespaced `ssds.*`, Admission reason codes carried in `details`; callers never parse messages; redaction per owning boundary |
| §5.6 idempotency/mutation | **Adopted**: `ask`/`read`/render are read-only; `submit` idempotent by request identity; `decide` idempotent by the decision record's identity; Dispatcher start idempotent per attempt |
| §5.7 sync/async boundary | **Adopted**: `ask`, `read`, `report` and `decide` synchronous; `submit` returns `PROVISIONAL` and the outcome is observed by request identity; harness execution through handles |
| §5.8 two-stage API freeze | **Superseded**: the SSDS API v1 is frozen once, at the G3 implementation review, for the whole system |
| §6 Core composition SPI | **Preserved** for other programs' extensions (`ssds.extensions.v1`); the SSDS components are not extensions: the root module `ssds.cli` composes them with Core (§26.3, A7) |
| §7 Core shared records | **Mapped**: `ProjectKey` -> genesis project identity; `WorktreeKey` reused for K2 leases; `RunId` retained for Core prompt mode only (SSDS uses task and attempt identity); `DigestRef` reused; `ProtocolProfileRef` reused for `LEGACY(p)` rendering; `WorkplanRef` not reused (plans are units); `CandidateRef` **declined** (transformation identity `(B, C, A)` replaces it, §7.1); `StageResultEnvelope` **declined** (the typed `TASK_RESULT` and admission request replace it); `EventEnvelope` remains Core's non-durable event; SSDS never derives state from events |
| §8 Core/Prompt module | **Preserved** for version-bound work |
| §9 Tracker | **Retired** as a module; functions **replaced**: history and projection by Ledger and Derivation (historical views, §5.8); status and next action by obligations and readiness; manual result ingestion by the Git-envelope result and `submit`; retention and export by the ledger and `ssds export`; the storage/lease SPI by the Dispatcher's operator journal and worktree leases |
| §10 Adapters | **Retired** as a module; functions **replaced** by the Dispatcher: routes and identities, manual and direct delivery, pre-render route admission, worktree lease, execution lifecycle (invariant 15), benchmark sources, cache and identity resolver, static recommendation |
| §11 Scheduler | **Retired** as a module; functions **replaced** by the Dispatcher: account and resource ledgers and meters (operator state, never workflow), reservations, prediction, AUTO route selection, future-stage reserves, failover; a configured-required resource policy that is unavailable fails closed |
| §12 configuration ownership; secrets as references | **Preserved and closed** (§26.3) |
| §13 persistence/event ownership | **Replaced** by §21 stores; "persisted state is not repository authority" **retired** for native scopes, where the ledger is authority |
| §14 CLI capability behavior | **Preserved** in behaviour for Core commands under the `ssds` command (A7); SSDS operations join the same command set (§26.3); Tracker/Adapter/Scheduler command sets retired with their modules |
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
| all roles | load memory on the activation predicate's occasions; judge the qualifiers | E0 + E2 + E3 | detected occasions inject the owner and require `pem_activation` (§16.11 (b), (c)); undetectable occasions stay E3 (§29.6) *[Amendment A10, SD-63.]* |
| all roles | retrieve memory and record a canonical HAS covering what is materially relevant | E0 + E2 + E3 | candidates as a floor; `historical_applicability` coverage and basis checked; the search beyond candidates and every disposition judged (§16.11 (c), (d)) *[Amendment A10, SD-63.]* |
| all roles | refresh a HAS when the memory basis, overlay or a governing owner advances before closure | **E0** | freshness template, re-derived on every rebase; integration needs it (§16.11 (f), §8.3 step 7) *[Amendment A10, SD-63.]* |
| all roles | reconcile owner-bound learning when its owner changes | E1 + E3 | bindings current only against an accepted, valid owner; every accepted owner change in admitted history makes them stale and routes them to the principal (§16.11 (e)); external, unresolved and pre-genesis intervals stay E3 *[Amendment A10, SD-63.]* |
| all roles | missing memory is not absence; memory is no single point of failure | **E0** + E3 | empty candidates never rendered as absence; `PEM_UNAVAILABLE` only against the derived reader state, and its uncertainty accepted only by the work's independent review or a human before the result counts (§16.11 (d), (g)) *[Amendment A10, SD-63.]* |
| all roles | closeout learning assessment before closure of a material repair, rework, optimization, revert or restoration | E2 + E1 + E3 | `closeout_learning` slot; `UPDATE_PROPOSED` routed to the principal (§16.11 (h)) *[Amendment A10, SD-63.]* |
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

These stay judgment only, and SSDS claims nothing more for them than that the review step runs and its record survives: **detection** (noticing anomalies, tensions, upstream defects; the 7.x study found detection did not respond to protocol text in any arm, and enforcement is not expected to change it); adequacy of authority, contracts, evidence and gate evidence; semantic equivalence and completeness; scientific and numerical interpretation; materiality; whether a Serious Challenge is warranted; the quality of discriminating readings (a lenient but formally consistent reader); the adequacy of a tension search; whether memory activates on a detected occasion, and noticing an occasion machinery cannot detect (suspected recurrence, history that can change a decision, an undeclared partial revert or recovery); the adequacy of a HAS and of the search beyond its candidates, including partial-coverage intake; the capability-transfer map; reverse reconciliation for external or unresolved owners; whether a change was material for closeout learning; real-owner versus proxy judgments; whether a change belongs upstream; reliance on reads machinery cannot observe; behavior inside an agent's own workspace; hygiene operations on Git refs. *[Amendment A10, SD-63.]*

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
| PEM reader and derived PEM facts (§16.11) | candidate floor, binding staleness and HAS freshness without a copy of memory | prose duties only (the 7.x load rate); a persistent projection (a mirror that can disagree); an on-demand query recorded as an observation (records a pure function of content) | keep; an analyzer, no store *[Amendment A10, SD-63.]* |
| operator state | private keys, leases, transcripts, high-water marks | in-repository state (violates G4) | keep |
| transport run refs | zero-context web agents | — | keep; regenerable |
| publication-attempt log | (formerly: evidence of "no attempt" across restarts) | **in-memory per incarnation (R4)** | **removed** in this Manual |
| partition validity check over observed bytes | (formerly: detection of overlapping leaves) | **partition by construction (R5)** | **removed** as a dynamic check; static checks remain |
| frames, transformation identity | pre-integration review with defined currency | reviewing only after merge (loses K1 for review) | keep |
| roles, envelopes, contracts, conformance, reports, inspector | stakeholder-directed enforcement layer (SD-1-SD-6) | instruction text (the 7.x evidence: compliance with text is probabilistic) | keep |
| fences | revocation of a stale publisher's effect authority | ledger checks before CAS (a paused publisher outlives them) | keep |

**What the refinements changed.** No new primitive, component, persistent surface or record tier is added by this Manual, and two mechanisms are removed (R4, R5). The assessment-disagreement family keeps its record kinds and components; R1 fixes how the reviewed execution basis is recorded and which of two predicates each use reads, and R2 makes a fail-closed promise explicit. The revision-assessment condition (SD-16 to SD-22) adds one admissibility condition and one obligation trigger, using the existing `TASK_RESULT` and its slot; the qualified-gate cap reuses `P`; the acting rule (SD-25, SD-26) replaces per-consumer frame exceptions by one S0 rule and withdraws the capabilities listed as R12; R9 extends the reviewed assessment rule to every judgment kind instead of adding a mechanism per kind. **SD-47.** After 61 Review rounds each closed a blocker and found its neighbour, the stakeholder chose consolidation over further additive repair (the convergence owner's rule): one judged-content rule replaces the separate definitions of what each review kind judged (§5.10 (b)), the review targets are three typed kinds (§3.4), and the exact mechanism moved to the non-authoritative catalogue for G2, so this Manual decides architecture and adds no mechanism. Practical costs remain reopen triggers (§32.3), not grounds to claim burden reduction. Amendment A10 adds an analyzer, two contract fields, three slots and two `COORDINATE` triggers; no primitive, component, store, record kind or tier. *[Amendment A10, SD-63.]*

**Stabilization question.** Would this architecture still be deliberately chosen today for the same governing contract? Within the evidence available at Phase C, yes: each element carries a capability an invariant requires. The answer is design rationale, not evidence of adequacy; independent Review and the G3 measurements decide.

### 31. Qualification design

#### 31.1 Principles

Subsections 31.4 to 31.8 are not used here: their test groups are carried to G2 (§31.2).

Qualification binds every claim to the property its method can discriminate (DS-001). Synthetic fixtures and model cases establish mechanical properties only; semantic adequacy (promotion, equivalence, completeness, gate adequacy, reading quality) needs real-owner cases and independent Review. Persistence and recovery claims use deterministic failpoints with the production owner executing. **No executable SSDS evidence exists at G1.** Every runtime group is **UNEXECUTED**; G1 needs only the document checks of §31.10. A missing required check is never a pass.

| Gate | Evidence it needs |
|---|---|
| G1 | §31.10 document checks; independent D3 Review of this Manual at the architecture level (§0.1); stakeholder acceptance |
| G2 | a shadow D3->D4 workplan that settles every catalogue mechanism against executable models, closes every register entry (catalogue C.2) and carries the acceptance program below, independently reviewed |
| G3 | the program below executed against production owners, with independent implementation Review |
| G4 | per subject: §19.5 cutover conditions, demonstrated rollback (§19.7), human and project approval |

#### 31.2 The acceptance program carried to G2

The program's groups are those of catalogue §31.2-§31.9, each with its negative discriminators (cases a shallow or proxy implementation passes and a correct one fails): derivation, structure and relations; assessment disagreement; judgment disagreement (with the history-derived item-level and transformation cases of register RR-1 and RR-2); admission, publication, currentness and loss; workflow, contracts, conformance and routing (with the five routing residuals RR-4 to RR-8); escalation and the inspector, including the no-stranded-obligation test (§10.3); frames, migration, intake and external units; security, Core independence and fitness. The G2 workplan may re-derive any of them; it may not drop a discriminator without recording why it is unnecessary. Amendment A10 adds the memory group of §7 of its proposal (occasions, coverage, freshness, staleness, unavailability, closeout, foreign lineage, and the absence of any memory write). *[Amendment A10, SD-63.]*

#### 31.3 Diagnostics of the catalogue

`qualification/ssds80/judgment_disagreement_model_check.py` checks the catalogue's judgment-disagreement rules on the cases it models (core, equivalence chains, completeness covers, plan coverage, gate basis, obligation routing, review scope), with mutations re-introducing earlier defects; its oracle shares helpers and claims with the rules and several of its tables are hand-chosen, so a green run establishes that encoded checks fire, never that a rule is adequate (register RR-10). `qualification/ssds80/item_review_history_probe.py` derives item-level judged content from explicit integration histories and shows that the catalogue's item-level entries, and the first wording of SD-46, miss producers that the Manual's rule (§5.10 (b)) excludes; its expectations are written per history, but it models only the item-level review. Both are diagnostics (DS-001), not qualification.

#### 31.9 Usability and doctrine realization (G3, measured, never claimed)

Live trajectories on real tasks in shadow mode, paired against the document-controlled 7.2.1 baseline on the same executors and fixtures, with gates calibrated before any spend, instruments validated first, and rules, custody and blinding frozen before runs (7.x lessons). Measures: agents complete bounded work without reading machine records and with less context; unauthorized mutation, claim integrity, owed-duty presence, narration where none was owed, and survival of material delegated findings to the human, on the 7.x panel. Detection is reported separately, because enforcement is not expected to improve it. Claims stay bounded to the duties, harnesses and models exercised (SD-6). Costs are measured, not asserted: false staleness under widening, promotion frequency, reading and reproduction burden, retention cost, human-attention volume, fence frequency (R4); judgment obligations that wait for an eligible independent judge because their judged content has unknown or broad authorship, and failing-assessment dispositions made under the owner exception (SD-48); re-dispatches, integration refusals and serialization that work-keyed judged content causes, and the size of judged-content sets; challenges no eligible adjudicator could take; equivalence and completeness judgments needing a human attestation or the owner exception; and how often a standing objection's reach widened closures or stopped reuse that no consumer contested (R14); memory occasions answered `activates: false` and candidates dispositioned `NOT_APPLICABLE`, per occasion and match path (precision), and accepted recurrences whose earlier task had no candidate for the recurring family (recall, read from canonical PEM at later revisions outside derivation); integrations refused for a stale HAS; stale-binding decisions per owner change (§16.11). These are retrieval-mechanism evaluation data, never PEM evidence, application episodes or input to temperature or maturity. *[Amendment A10, SD-63.]*

#### 31.10 G1 document checks (executable now)

- the Manual, the mechanism catalogue and the closure map exist at their routes; the closure map maps every §21 item and every §16.2 row to a Manual section;
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` passes (routing and lifecycle frontmatter only);
- `python3 -I qualification/ssds80/judgment_disagreement_model_check.py --mutations` and `python3 -I qualification/ssds80/item_review_history_probe.py` exit 0 (diagnostics of the catalogue, §31.3);
- `git diff --check` is clean;
- PEM schema validation passes for the bound basis;
- the frozen Architecture 1.6.0 file is byte-unchanged;
- no protocol `source/`, `dist/`, profile or snapshot file changed.

These establish structural facts only. Whether the Manual is adequate is for independent Review.

### 32. Limits, residual risks and reopen triggers

#### 32.1 Where machinery stops

Machinery prepares but never decides: whether two scientific or numerical formulations mean the same; whether a change is editorial beyond byte and normalization identity; whether an acceptance supports a newly scoped subject; whether a foreign structural declaration expresses intended governance; whether a set of objects is genuinely simultaneously defined; whether a discrepancy is a D4 defect or exposes inadequate D3, D2 or D1; whether evidence supports a claim and whether gate evidence is adequate; whether a relation is real or a scope complete; how a legacy region decomposes; whether an architectural change preserves its parent; whether a Serious Challenge is warranted and how it is adjudicated; whether a risk override is acceptable; whether a marked product surface is accepted; whether a confidentiality incident needs destructive remediation. For each, machinery produces a **focused question**: exact subject, scope and revisions; the distinctions already resolved; the evidence and its status; what the answer changes; the allowed outcomes. The answer is a recorded judgment that then propagates mechanically.

#### 32.2 Residual risks

- Semantic dependencies an agent uses without machinery observing them (§9.4); circular reasoning stated only in prose (§2.5).
- Lost admitted history whose every copy, checkpoint and high-water mark is gone, with a stale product (§23.8); attestations that are wrong.
- Machinery cannot make an agent notice what it did not notice, or make a judgment good (§29.6); a formally consistent but lenient reader.
- A failure becomes stale mechanically only through runs that match the failing realization's complete external-input record and recorded attributes, never one that read an unpinnable input; variation in an attribute no runner class records, randomness the runner does not supply and scheduling nondeterminism are invisible until a differing run on the same content is observed (§6.5, §6.10, §17.5); classes that do not observe reads outside the tree send their failures to the owner.
- Bounded clone-tracking for moved-and-rewritten claims (§6.4); a move plus substantial rewrite escaping rename detection (§1.11); content moved out of the paths a `QUARANTINE` names (§18.4); LFS inputs are external reads, and submodule commits are not kept reachable by this ledger.
- Exact content identity narrows adverse as well as permissive matching for representation-only differences, and the effect-keyed write set aligns bytes line-wise, so a D4 edit on a line shared with a D1-D3 span counts against the D1-D3 unit (fail closed, §1.2, §1.5).
- Late publication after a foreign return of the ref to exactly `B_n` (§22.3); forgery by a holder of an Admission or issue key; more than `f` faulty witnesses with control of the replica (§23); a VM-level snapshot of a running Admission process mid-publication, outside the crash model.
- Joint validity of independently valid changes where no relation, invariant or evidence covers the interaction (§9.1).
- Independence is fixed at admission, and broad authorship fails closed: judged content of unknown authorship admits only a human with a non-authorship attestation, and every producer of judged content is excluded from judging it (§5.10 (f)). Only an owner's disposition of a failing assessment may use the owner exception (SD-48); any other judgment with no eligible independent judge waits on human attention, which can stall work in a project with few qualified humans until policy names a judge. *[Amendment A5, SD-55.]* It can wait even where qualified independent people exist, when none of their records could act, or have an admissible basis, in the state that needs it (§5.10 (f)): another qualified human is not always enough.
- A change of an item's prose or fixed fields starts new work whose judged content holds only what that work changes; content the earlier work produced and the new work keeps unchanged is then not judged as the new work's, and its earlier findings reach the new work only through the re-review carry (§5.10 (b), §16.5).
- A superseding judgment judges its exact target under its own basis context; if that context later reverts, an earlier peer judgment on the same target can be current again without re-judgment (early cutoff, §5.5).
- A cutover whose carrying integration is fenced or overtaken leaves the subject `NATIVE` on legacy bytes, invalid until re-applied or rolled back (§19.5).
- One standing objection vetoes every judgment a contradicting composition needs, including compositions no consumer uses (R14); a standing adverse judgment on a subject triple does not freeze re-scoping as a blocking challenge does; an objection to a subject or named units does not reach a re-identification except through the lineage carry (§5.10 (c)); part and composite equivalences do not entail each other.
- Two item revisions with the same prose and fixed fields share one rejection's reach and their reviews' reaches, so a judgment about one vetoes the other until its author or the owner relieves it (§5.10 (c)).
- Every non-machinery equivalence and completeness judgment needs an independent qualifier, which costs migration throughput where legacy authorship is unknown (§5.10 (f), §19.5).
- Memory occasions are detected only from declared intent, policy tags, byte-identical reverts, restorations and recurrence detection: an undeclared rework or a partial revert raises no occasion, and a material repair answered `NOT_MATERIAL` owes no further closeout; review and later recurrence detection are the mitigation (§16.11 (b), (h)). Tag matching finds only exact declared terms, and every owner change without an editorial or representation equivalence makes its bindings stale (§16.11 (d), (e)). A binding to a `LEGACY(p)` owner with no imported acceptance stays review required, and an owner-change interval before genesis is not in admitted history; both stay with the inherited duty. A memory uncertainty on a result no independent review judges waits on a human, and the judgment or decision refused meanwhile is redone by a new task after the human accepts (§16.11 (g)). A binding whose interval crosses a loss boundary stays review required until its entry is reconciled (§16.11 (e)). *[Amendment A10, SD-63.]*
- *Restored by amendment A3 (SD-53), lost in the SD-47 condensation:*
  - A passing realization that read an unpinnable input, or ran under a class that does not observe reads outside the tree, stays current while its tree-resident entries hold; only its permissive uses for stopping a failure are excluded (§6.5).
  - A declared term that later resolves to `ABSENT` changes identity but raises no specific finding unless it is a malformed anchor (§1.3, §1.9).
  - The adverse linking predicate fails closed: a recorded basis that omitted content the execution read (a defective tracer, a wrong completeness judgment) links runs that differ there, so a genuinely fixed failure can keep counting until the owner disposes of it (§6.6).
  - Incidental reads outside the tree (user caches, host configuration) that differ between runs leave them unmatched for a mechanical stop (SD-23), so such failures go to the owner unless runner classes declare host files as environment components and run with hermetic home and cache directories (§17.5).
  - An upheld challenge against a co-submitted attestation does not change a record's independence classification; the correction is a challenge against the credited record itself (§5.10 (f)).
  - A re-partition can split rejected content across parts whose write scopes each hold only some of it, so no part's review is reached by the earlier `NO_PASS`; the item-level review, whose judged content holds the whole item's work, is reached, and unresolved findings are carried into re-review briefs (§5.10 (b), §13.7, §16.5).
  - Equivalence hops keep their recorded direction (§4.4): an independent equivalence recorded the other way, or judged before a revert for consumers on the other side, serves no path in that direction, and a second judgment is needed.
  - A plan rejection reaches an acceptance on a control-only branch incomparable with the rejected revision from the rejection's admission, even if the branches never join, until the rejecter or the owner relieves it; relieving an acceptance clears its coverage of every tightening of its revision, those it shares with the rejected revision included; relief is admitted only while the relieved acceptance's basis holds (§5.10 (c)).
  - A candidate-frame gate `REJECT` on a subject the candidate leaves unchanged vetoes in the admitted state while the candidate is pending and after it is abandoned, until its author reassesses or the owner adjudicates (§5.10 (d)).
- The 2026-10-12 governing-version adoption instruction remains paraphrase-only; only stakeholder restatement or recovered authentic evidence closes it.

#### 32.3 Reopen triggers

Reopen this architecture at its earliest affected owner if, on real repositories or live trajectories:

- conservative widening, part-to-subject routing or whole-tree execution-basis fallback make too much work non-current or too many promotions necessary to be useful; read recording proves infeasible across target harnesses; unit declaration cost, the manifest or the partition rules outweigh their locality benefit or cannot express real structure;
- keeping every system version and analyzer set that recorded execution bases name proves burdensome; or too many failures go to the owner because no run can serve a mechanical stop;
- adverse judgments routinely block work pending the owner's adjudication, or vetoes are used to stall work; gate terms accumulate stale members; the acting rule makes parallel candidates and replacement iterations repeat realization, review, acceptance and gating at a material cost (§5.2, §7.6);
- publisher crashes inside the publication window make fence-induced D1/D2 re-gating a material share of human gate work;
- current-state discharge (SD-36 to SD-40) makes drift re-dispatch, budget spending or undoing of later accepted changes a material cost;
- a register entry (catalogue C.2) cannot be closed at G2 without changing a decision here: in particular any of the five routing residuals accepted by SD-41's bounded stop (RR-4 to RR-8), or the judged-content rule of §5.10 (b) proving unrealizable on recorded histories (RR-1, RR-2);
- Git-hosted ledgers cannot meet single-ref compare-and-swap, durability, privacy, scale or hosting constraints; no practical witness set satisfying `q_a + r > N + f` exists for the deployment class, or witness latency on the Admission path proves unacceptable;
- structural quarantine, simultaneous-definition groups, the confidentiality protocol, requalification after loss, continuity attestations or integration-head reconciliation prove unworkable or become routine shortcuts;
- the fixed predicate templates cannot express a required project policy without breaking stratification; a later accepted protocol version changes doctrine this Manual binds;
- agents still do bookkeeping; contracts, lint or `HARD` templates cost more than they buy or are gamed; coordination becomes a bottleneck; human-attention volume exceeds what the inspector can sustain; constructed independence proves illusory;
- owner dispositions, discriminating readings or reproductions become a material share of evidence work, or discriminating observations prove routinely unobtainable, or readings become a route for retiring concerns;
- *amendment A6 (SD-55):* failures caused by execution attributes no runner class records are made stale and later found live, or reproductions with the failing realization's recorded attributes are routinely unobtainable on the designated runners (§6.5, §17.5); retained trees and reproductions cost more than the dispositions they make cheap (§21.4);
- *amendment A10:* memory answers or dispositions become rote, or stale-binding decisions or HAS-freshness iterations become a material cost; the §31.9 measures show a recall gap that owner, typed and tag matching cannot close (then consider a similarity recall net producing `CANDIDATE` observations under an explicit trust decision for memory text); or the PEM schema owner rejects typed applicability bindings and tag matching proves too weak to keep (§16.11). *[Amendment A10, SD-63.]*
- *restored by amendment A3 (SD-53), lost in the SD-47 condensation:* whole-tree execution-basis fallbacks make passing evidence non-current too often or send most failures to the owner (and D1/D2 failures to the floor); submodule hosts routinely drop commits that reproductions need; line-ending or mode churn on D1/D2 subjects routinely starts new revision runs; incidental external reads routinely prevent mechanical stops; failures of admitted obligations found in one lineage routinely delay other lineages, or scheduled executions routinely end `INCOMPLETE`; residual owner dispositions (lineages dropping their own failing test-first checks, failures latched by transient foreign pushes) become frequent, or disagreement becomes routine; accepted relaxations of mechanical specifications routinely make failures stale unexamined, or lenient readers pass outcomes that show the defect;
- any inherited guarantee proves unpreservable.

#### 32.4 Residual register

The mechanism questions this Manual leaves to G2 are listed once, in catalogue C.2: RR-1 item-level review judged content; RR-2 transformation judged scope and the retained-unit machinery; RR-3 review target typing in the catalogue tables; RR-4 to RR-8 the five routing residuals; RR-9 replay of the historical mechanism findings; RR-10 diagnostic construction; RR-11 the catalogue's general owner exception, narrowed here by SD-48. Each is closed only against an executable model at G2, at the same no-blocker bar; one that turns out to bear on a decision here reopens G1.

#### 32.5 Open uncertainties

**Empirical** (§31.9 measures them; none is claimed): rate of false staleness; promotion frequency in Case B; analyzer completeness for real Python and C++ scientific code; read-recording feasibility per harness; practical granularity; derivation cost and checkpoint sizing; ledger growth over years; witness availability and latency; quarantine and SDG frequency; agent context and success against the baseline; contract authoring cost; template detection and false-positive rates; amendment, escalation and downgrade rates; human-attention load; fence frequency; whether doctrine realization on the 7.x panel improves over 7.2.1 on the behaviors that did not respond to text.

**Decision provenance**: the paraphrase-only 2026-10-12 adoption instruction (§32.2).

### 33. Non-goals

SSDS 8.0 does not: convert scientific reasoning or evidence into machine records or encode scientific truth in rules; provide a general rule or theorem language; require a graph database, network database, hosted service or distributed consensus; infer independence outside judged-complete scope; transfer acceptance by byte identity, scope arithmetic or widening; let agents write canonical state, let derived relations override source, or let D4 behavior create accepted D1-D3 authority; treat Git branches, commits or pull requests as workflow semantics; depend on server-negotiated multi-ref atomicity; assert currentness for state a witness quorum does not hold, claim rollback detection beyond the declared witness model, or claim that lineage migration erases leaked data; let repository presence, a foreign push, a restore or a merge change effective structure, ruleset or acceptance; reconstruct or guess lost admitted history, or let retained authority cross a known loss without requalification or accountable attestation; license a relation cycle by common subject identity, or let a definition or condensation warrant a claim; require every write to pass through an interface; expose machine records as routine agent UX; use search as an authority resolver; execute unknown artifacts to classify them; force all-at-once migration or stop valid production for incomplete migration; allow two current authorities over one subject; use migration as a hidden redesign channel; keep document-controlled workflow as a dual-current fallback for native scopes; add webhooks, brokers or hosted services before polling and local operation prove insufficient; add registries, wrappers or fields solely to mirror inherited doctrine (the realization map of §29 is a design artifact); keep a copy, registry or database of project memory, copy lesson text into records, judge memory applicability or admission, or write memory (§16.11); treat a clean conformance view, a passing check or an agent's own claim as discharge of what a judgment must discharge; let a heuristic or prose-reading check block or pass work; let a contract carry executable check code, or an agent role edit templates, roles, routing or floors; let any agent role choose a decision's class, lower a report below a floor or discharge human attention; make a principal a long-lived process whose memory is workflow state; use a model judgment as a mechanical check; provide atomic admission across repositories; or provide a universal scientific observation database. *[Amendment A10, SD-63.]*

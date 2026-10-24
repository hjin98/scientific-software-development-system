# Independent D3 Review — SSDS 8 Manual amendment A10

```text
GOVERNING SSDP: 7.2.1; public source aaeaf8b6b2121b9fb8aba31917c8265649c43954;
               recovery efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REPOSITORY:    hjin98/scientific-software-development-system
BRANCH:        ssds-8.0-graph-native-architecture
ENVELOPE:      4e62eb9bc0ec8fad87e387b45be58cc9a19be969
HANDOFF:       qualification/ssds80/MANUAL-AMENDMENT-REVIEW-HANDOFF-SSDS-8.0-A10-0368198.md
HANDOFF BLOB:  152432d2ce78f2cc544ecdb1b863f6060d53f2b9
CANDIDATE:     0368198210706151c69a4119f6288ce8baa8d884
BASELINE:      4f055e5c708bcca24bf4b403a7f6c3a3a542e0c2
SCOPE:         proposed §16.11 and all §4.2 consequence edits, judged as applied to the
               accepted A1–A9 Manual; companion item C judged for consistency only
MANUAL:        orchestrator/docs/ssds-8.0-architecture.md
MANUAL BLOB:   fe43f04f5a698688727f7473a7c2e4d5345ae911
PROPOSAL:      qualification/ssds80/MANUAL-AMENDMENT-A10-PROPOSAL-SSDS-8.0-PROJECT-ENGINEERING-MEMORY.md
PROPOSAL BLOB: 871ecb574b7d15e6e860ff171bfb70d75d1394e7
ITEM-C BLOB:   34594fefd81337ead9473683d40755a60e108696
REVIEW METHOD: independent owner reconstruction, static counterexample trajectories,
               bounded Challenge Pass and out-of-matrix adequacy pass; candidate-only
               structural checks; no A10 executable model or live qualification
REVIEWER:      GPT model family, engaged through Codex CLI in the stakeholder's own
               terminal at the stakeholder's request. The author's session typed only
               the handoff pointer. Engagement provenance is supplied by the user;
               this record does not claim a production SSDS lineage attestation.
AUTHOR FAMILY: Claude, identified by the candidate's co-author attribution.
DATE:          2026-10-24
SCRATCH:       /tmp/ssds80-manual-review-a10-0368198
```

## SERIOUS CHALLENGE

None against the accepted Manual or SSDP PEM owners. Their distinction between observed content, accepted authority, candidate support and current applicability is coherent for this scope. The blockers below concern the proposed concretization and its coverage claims; they do not reopen unchanged A1–A9 or amend SSDP 7.2.1.

## Verdict

**NO-PASS for A10 as a D3 change, under criterion 11.** Five G1 blockers remain: the accepted-publication and binding shortcuts; an insufficiently specified freshness dependency; uncertainty accepted without a guaranteed independent judgment; non-monotone candidate selection classified as control tightening; and loss of owner-change reconciliation across an unreadable interval.

The pinned reader, reuse of existing result slots and separation from item C are viable directions. Passing structural checks do not cure these semantic defects. A10 remains proposed; this Review accepts nothing and authorizes no D4.

## G1 blockers

### B1 — Observed PEM content and matching owner bytes can stand in for acceptance

**Owner text.** Proposed §16.11(a), proposal line 114, calls the PEM units' admitted content the “accepted PEM publication” and says policy declares the publication line by naming `pem_root`. Section (e), line 133, makes a resolved binding current iff current bytes equal the routed bytes or an eligible equivalence path connects them. Neither condition independently establishes the required accepted project state or accepted owner. The public-source PEM owner, “Retrieval and HAS” step 1, selects the base by project Git acceptance policy; the schema owner, “Authority binding representation,” requires immutable owner provenance in the project-governed accepted state and expressly excludes candidate-only authority. Manual S3, §8.6, §19.2, §19.9 and §20.2 preserve the observation/acceptance distinction.

**Trajectory.** Project policy selects integrated state P and PEM publication M0, with a candidate overlay on a development branch. A shadow or mixed-mode ledger observes that branch. A foreign push changes the existing PEM unit to M1; Admission absorbs it under §8.6, without steps 1–8 or any PEM acceptance event. Its schema and root identity still parse. A10(a) now calls M1 accepted merely because those are the admitted unit bytes. Naming the discovery-root unit has not established that the project publication event occurred. A task can consequently receive the wrong `accepted_pem` basis while following A10's new rule.

There is a second discriminator within the same acceptance boundary. An overlay records an `AUTHORITY_BOUND` route to a locally governed owner's proposed revision U1. The frame contains U1, so the route locates a unit and its bytes match. The proposed iff classifies the binding current even before any prospective acceptance counts. The fact that SSDS knows the candidate bytes does not establish that U1 is the accepted owner. Keeping the overlay visibly candidate is necessary but insufficient: its individual authority claims cannot self-ratify either.

**Consequence.** This is an architecture-level acceptance shortcut, not a parser choice. An accepted owner or publication cannot be recovered from the path parameter and equality test alone. The same problem exists when content is `LEGACY`, `UNGOVERNED`, absorbed, or still prospective.

**Minimum repair.** Preserve independently selected exact accepted project/PEM identities as inputs witnessed by the project's real acceptance process; distinguish them from the ledger's observed tree. Permit coincidence only where that process actually makes the events coincide. Compose a validated overlay against that base. Define binding currentness to require accepted-owner provenance and applicable owner validity in addition to resolution and equivalence; otherwise show `REVIEW_REQUIRED`. Reuse existing imports, judgments and records where sufficient; no parallel acceptance registry is requested.

**Discriminator.** Hold the ledger tree constant while varying independently witnessed accepted publication/owner state. Absorption alone and candidate-only matching bytes must not change an accepted basis or produce a healthy authority binding. A later real acceptance event must permit the corresponding transition without rewriting history.

### B2 — The freshness predicate does not bind all material changes it claims to cover

**Owner text.** Proposed §16.11(a) lists derived family/notice fields; (f), line 135, compares those “PEM facts” for dispositioned and currently candidate entries. The list names identity, kind, state, authority binding, owner route, normative status, applicability tags/bindings and lineage. It does not define identity as a digest of the complete entry and its material dependencies. The PEM owner's “Retrieval and HAS” step 5 and the evidence owner's “Change impact and closure” require refresh for material changes including claim, evidence admissibility/binding health, coverage, maturity and guidance. Those are not all represented by the listed facts. Section (c)'s basis-identity check establishes the state in which the HAS was made; it does not require that old state to remain the current basis, which is what (f) is supposed to decide selectively.

**Trajectory.** At N0 an item binds PC-X. The agent searches canonical memory and produces a correct HAS against M0. Its candidate result is admitted. Before integration another accepted PEM update M1 invalidates the evidence on which that disposition relied, or changes the entry's coverage/binding health to expose a material uncertainty. The family ID, kind, `CURRENT` state, authority route, tags, typed bindings and lineage all remain unchanged. An ID-based reader satisfies (a)'s field list, and (f)'s equality then reports fresh at the clean rebase. The old disposition has not been refreshed against the changed warrant.

If “identity” was intended to mean a complete entry-content digest rather than its schema ID, that materially necessary meaning is missing. Such an implementation could avoid this trajectory, but an equally conforming ID interpretation cannot; the architecture must exclude the latter. Historical and evidential inputs can also be shown by identity rather than added to a support record's content basis (§4.3). Ordinary read recording is therefore not a replacement for the asserted freshness guarantee. Always placing the whole PEM root in every content basis would instead invalidate unrelated changes and abandon the proposal's selective guarantee.

There is also an unreconciled sibling signature: §14.1 says conformance for a result without a candidate is a function of its result record and contract alone. A10(f) requires the current admitted head at that result's admission. That additional state dependence must be made explicit at the conformance owner, rather than relying on the catalogue to choose between incompatible input descriptions.

**Minimum repair.** Bind freshness to complete material entry/publication dependencies, by content identities or another explicitly sufficient projection, without copying lesson prose into records. Preserve bounded selectivity and explicit uncertainty for dependencies that cannot be established mechanically. Reconcile §14.1 with the new state-dependent result-only checks. Retain checks at result admission and every integration revalidation, including §8.3 step 9's absorption/retry path.

**Discriminator.** Change only evidence assessment, binding health, coverage or claim-relevant guidance after result admission; leave the current listed matching fields unchanged. A materially affected HAS must become incomplete or require an explicit refresh. An unrelated entry change must not do so. Exercise both candidate and records-only result admission. These are proposed qualification cases, not executed A10 tests.

### B3 — A required review-brief item does not ensure independent acceptance of unavailability

**Owner text.** Proposed §16.11(g), line 137, permits owed slots to be `NONE/PEM_UNAVAILABLE` when corroborated by the reader, then infers that uncertainty is accepted only by an independent reviewer or human because “the review brief of that work” carries a required item. Manual §11.5 gives records-only work no integration step; §13.6 gives coordination a system contract, not a mandatory review of its result; §15.5 permits its decision to be answered by the first admitted coordination decision. A7 and §14.4 distinguish conformance from judgment.

**Trajectory.** Repeated routine failures on D4 work derive a non-floor recurrence coordination decision. That is a memory assessment occasion under A10(b). The reader is unreadable when the principal task is issued and remains unreadable at admission. The principal returns the owed slots with the corroborated unavailable reason and chooses `DECLINE` with a reason, which the existing recurrence route allows. Its result-only checks are clean, and the records-only request answers the coordination decision. No `REVIEW(X)` exists and no floor or escalation requires a human judgment. There is no later review brief to receive the required item. Machinery has allowed final resolution on uncertainty without the promised independent acceptance.

**Minimum repair.** State which existing independent judgment or human decision must count before each affected result/decision can close, including records-only and principal work. Derive that review/attention route when it otherwise does not exist. Do not require an endless review of reviewer results: bind the acceptance to the particular underlying uncertainty and decision. Keep unrelated work usable.

**Discriminator.** Run the non-floor, records-only recurrence trajectory with an unreadable PEM. A syntactically valid unavailable reason must be corroborated but must not, by itself, authorize the final permissive decision. Show a ready independent route or a visible human wait; then show an admissible acceptance or rejection of that uncertainty.

### B4 — Adding matching terms is not necessarily control tightening under the candidate cap

**Owner text.** Proposal §4.2 edit 5, line 155, adds entries in `memory.terms` to §13.4's tightening direction. Proposed §16.11(d), line 131, caps match-path candidates; (c) makes the recorded candidates the mechanically required HAS floor. Accepted §13.4 permits R1 reuse of plan acceptance only under its control-tightening order. The cap's selection is delegated and has no non-eviction invariant.

**Trajectory.** An accepted item has term `z`; ten matching entries Z01–Z10 form its required floor under cap 10. The principal adds term `a`, changing no prose or other field. Ten additional entries A01–A10 match it. A deterministic lexical selection of the first ten candidates is permitted by the current proposal and replaces all Z entries with A entries. A new task must disposition the A entries but no longer mechanically owes any Z disposition. The amendment is classified R1 even though one set of required controls was exchanged for another rather than strengthened. Showing an omitted count and retaining a general E3 search duty do not preserve the previous hard floor.

**Minimum repair.** Keep `memory.terms` outside the tightening whitelist unless the selection/coverage semantics ensure that adding terms cannot remove a previously required control. Alternatively require R2 for that change. Bound `memory.bind` additions must remain non-truncatable as already stated. Do not solve this by asserting that more search terms are intrinsically tighter.

**Discriminator.** Compare required coverage before and after a term addition at and above the cap, with new matches sorting/ranking ahead of old matches. A purported R1 change must preserve every old mandatory disposition or be classified R2. This property belongs to the accepted control order, even though the exact ranking algorithm belongs at G2.

### B5 — Current-state staleness can lose an owner-change interval while the reader is unreadable

**Owner text.** Proposed §16.11(e), line 133, claims that an owner change during an unreadable interval “is not lost” because staleness is a state predicate. Its currentness test expressly accepts equality to the bound content. The upstream workflow and evidence owners require reverse reconciliation on a change of an owner cited by an authority-bound capability or normative notice; the evidence owner also requires affected applicability/binding reconciliation on revert/restoration. The proposal limits its explicit residual E3 reverse-reconciliation duty to external or unresolved routes.

**Trajectory.** At N0 a readable accepted memory binds PC-X to local accepted owner U at bytes A. Memory becomes unreadable. While unreadable, U changes by an accepted semantic change to B, then returns by an accepted restoration to A, without editorial/representation equivalences and without reconciling PC-X. The root becomes readable again with its old binding. The live-state test now sees A equal A: the binding is current, no stale-binding coordination decision is derived, and there was no readable intermediate state in which to derive one. The changed interval and its reconciliation duty have vanished from the proposed mechanism, although the canonical ledger still records them. The same trajectory can affect a normative notice.

The simpler control trajectory A→B while unreadable, followed by a readable root with the unchanged route, does produce a stale binding. That positive case supports net-change detection only. This finding does not assert that final A necessarily has obsolete normative force; it establishes that equality of endpoints does not discharge the intervening mandatory reconciliation or substantiate the unconditional “not lost” claim.

**Minimum repair.** On recovery of readability, preserve the duty to inspect the material owner-change interval from canonical history, or retain an explicit E3 reconciliation/uncertainty route for intervals the live predicate cannot cover. Narrow the mechanical coverage claim accordingly. A derived bounded history query may suffice; a new persistent memory projection is not required.

**Discriminator.** Compare A→B and A→B→A during unreadability, without any reconciliation or equivalence judgment, then restore readability. Both must expose the unresolved interval duty; an explicit admissible reconciliation can resolve it. Endpoint byte equality alone must not count as that reconciliation.

## G2 register entries

**A10-R1 — Freshness lifetime and unavailability timing.** Make the pre-integration guard's lifetime exact. At each result admission and integration attempt, including retry after absorption, compare the proper state; after integration preserve the historical freshness decision without making it a permanent content dependency that reruns every old HAS. This can coexist with SD-36: new material output/evidence changes still reopen the ordinary obligation terms. Specify separately whether an unavailable reason requires unreadability at issue, at evaluation, or both; (g) currently mentions both contexts. The interface must explain the relevant transition and usable route if memory recovers or breaks mid-task. This is delegated routing detail once B2 and B3's guarantees are fixed.

**A10-R2 — Reverse-impact scope and follow-through.** Define the global scan over local bindings independently of a particular task's `GOVERNING` brief. The reference in (e) to “those of (d)(2)” must retain the entry classes without accidentally restricting global reverse impact to owners in an extant task's brief. Exercise no standing plan, a principal decision while the binding remains stale, a rejected challenge, delayed reconciliation, and another owner change. `AMEND` must actually carry its plan change; `CHALLENGE` and `ESCALATE` need their existing downstream holders. An answered decision is not evidence that the binding became healthy. Continued visible `REVIEW_REQUIRED` may be appropriate; no permission to retain obsolete force follows from answering the decision. No separate no-stranded contradiction is established here beyond B3 and B5.

**A10-R3 — Separate architectural guarantees from catalogue mechanism.** Section 4.3 explicitly delegates the reader field list, failure causes, exact revert predicate, historical route resolver, normalization, slot schemas, templates, decision keys and outcomes. Section 4.1 presently supplies several of those exact choices as text to apply verbatim. Keep one architectural statement of required capabilities, force, holders and acceptance boundaries; put exact schemas, keys and algorithms in proposed catalogue material. The architecture must retain the acceptance, coverage and liveness guarantees identified above; those cannot be delegated away as field-list details. This is a level/ownership cleanup, not grounds to add another component.

**A10-R4 — Candidate and reader qualification at real owners.** Qualify safe data-only parsing, coherent root/partition publication, complete-schema handling, pre-genesis route resolution, base/overlay union, explicit retirement, deterministic normalization/capping and rebuild parity at the real reader/derivation/conformance/Admission/interface boundaries. Distinguish unsupported schema from ordinary partial historical coverage. Remove cached derived facts and show identical replay; no helper-only fixture may qualify the assembled path. These checks are future G2/D4 obligations, not missing executions of an existing A10 implementation.

## Non-blocking findings

- Item C is an optional future schema proposal. Under schema 1, typed candidates can be empty while explicit bindings, owner-bound candidates, tags and canonical agent search remain available. A10 does not require an invented typed-binding field or adoption of a new schema. Item C's own adoption and compatibility decisions remain with the protocol repository.
- The accepted/overlay candidate union preserves entries whose matching tags are narrowed or whose state is retired by an overlay. That is a useful floor, provided the accepted base itself is independently resolved and composition validated as required by B1.
- Qualifiers remain judgment: detecting migration, declared optimization or a trivial revert can require an activation answer without asserting that substantiality, maturity or historical materiality is true. An extra policy occasion likewise need only trigger assessment. “An agent may activate memory on any task” must be read subject to the retained upstream predicate, not as permission to load unrelated memory.
- Closeout includes the inherited material repair/rework/optimization/revert/restoration classes and correctly excludes migration alone. The result may propose an update but cannot admit or promote memory. Under-classification and inadequate reasons remain semantic review risks, expressly disclosed.

## Eight judgments required by the handoff

1. **Fidelity to PEM owners — NO-PASS.** The activation qualifiers, canonical three-key HAS basis, candidate visibility, missing-memory fallback, capability-transfer duty and closeout migration exclusion survive in the intended design. Recovery and suspected recurrence remain E3 rather than silently removed; §29.6 lists them. Base/acceptance resolution fails B1; material refresh fails B2; independent uncertainty acceptance fails B3; unreadable-interval reverse reconciliation fails B5. Schema validity is not lineage or acceptance evidence.

2. **Manual invariants — NO-PASS.** A ruleset-pinned, pure, data-only reader over retained content is a legitimate §5.9 analyzer. Its facts can be S3 and rebuildable without fact records, using the existing ledger/tree and ruleset inputs. That does not make its input accepted or its semantic projection sufficient. B1 violates the acceptance boundary; B2 leaves a decision-sensitive dependency and a conformance-input conflict. S5, S8, S9, A6, C3, C7, P3, T2 and T3 otherwise remain viable constraints: empty candidates prove no absence; PEM prose stays data; no model decides applicability; no external live ref may enter pure derivation. A4 needs the actual uncertainty route in B3. A7 is preserved only if typed controls carry the material dependencies rather than parsing reasons. The fields have operational purposes, so their existence alone does not violate §33.

3. **Reverse impact — NO-PASS.** Directed current, unvetoed editorial/representation paths are an appropriate conservative currency test once accepted-owner provenance is established. Semantic change without such a path must fail closed. Normative notices and authority-bound entries are named; owner-recorded promotion proposals are an expressly stronger reconciliation trigger, not promoted authority. The unconditional unreadable-interval claim fails B5. A10-R2 records the task/global scope and first-answer follow-through questions. A stale binding remains unusable for retained force even after its coordination decision is answered.

4. **Freshness and unavailability — NO-PASS.** Re-derivation on every clean rebase can reach the two candidate admission/integration boundaries; Admission step 9's absorption/revalidation closes the head-race window when those checks are actually state-dependent and repeated. B2 prevents the present projection from proving the advertised full material coverage. B3 disproves independent acceptance for all unavailable results. Corroborating unreadability itself is a sound pure derivation claim and does not require a new observation record. A10-R1 distinguishes a historical pre-integration guard from latched discharge: later memory alone need not rerun closed work, while current output/evidence terms still obey §10.4.

5. **Siblings and single ownership — NO-PASS.** Inspected §1.11, §4.4, §5.1, §5.9, frames, §10.2–§10.4, §11.5, §12.5, §13.1–§13.6, §14.1–§14.4, §15.5/§15.7, §16.2–§16.5/§16.9, §19.8–§19.9, §20, §29 and §30 with the proposed edits. The material conflicts are B1 at acceptance/import/absorption, B2 at the freshness/conformance inputs, B3 at records-only coordination and B4 at tightening. A10-R2/R3 cover the remaining ownership details. Phase E currently injects PEM for `MIGRATE` and recurrence in `interface/render.py:243–244`. A10 retains those injection occasions but adds assessment slots, candidate/freshness behavior and a newly detected-revert recurrence signal; it is more than a slot-only change. These extensions are stated in the proposal and are future work, not accepted changes to Phase E's realized behavior.

6. **Level — viable with A10-R3.** Reader ownership, no mirror, pure derivation, minimum coverage, independent uncertainty acceptance and impact/freshness boundaries are D3 decisions. The detailed field list, keys, normalization and exact predicates should have the catalogue's status §4.3 assigns them. Conversely, acceptance provenance, monotone control coverage and a real holder for required judgments cannot be left to catalogue discretion. No new component, primitive, store or obligation kind is necessary to repair the blockers.

7. **Cost and disclosure — bounded, not demonstrated.** Sections 31.9, 32.2 and 32.3 disclose false activation, missed detection, tag limits, conservative staleness, rote answers and iteration/decision burden. The recall measure is a bounded later measurement, not exhaustive recall or a maturity input. The reader plausibly avoids the synchronization cost of a persistent projection. Section 30's “keep” is an architectural recommendation conditional on corrected semantics; it does not demonstrate cheaper operation than prose or recorded queries. No runtime or outcome improvement was measured. Recovery-interval work and independent review of records-only uncertainty must also be costed after repair.

8. **Prerequisite and item-C boundary — prerequisite justified; item C not required.** The PEM blob is `1561797125622f355f84eb27319f87e8fa4227d9` both at candidate and independently resolved `main@af0455753e20ee54a969c844872e29e270007211`. It names the protocol project/repository, protocol 6.5.0 and accepted base `23e46543…`; PC-001's route names the protocol repository. Its five families are foreign under proposed (a), and its sole authority-owner route is external under (e); there are zero notices. Thus it supplies no local owner-bound candidate or stale local binding under that proposal. This is not absence of relevant evidence. The lineage prerequisite covers the derived facts/candidate/reverse-impact work, matching SD-63 item B; it neither blocks this review nor authorizes a lineage edit. Project governance must reconcile lineage before that D4 work. Item C adds optional selection affordances and is not a hidden prerequisite for the schema-1 path.

## Bounded Challenge Pass and evaluated variants

The criterion for each static variant was whether a locally conforming A10 realization could violate a material upstream duty, or whether existing authority already excluded the attempted violation. These are **16 reasoning trajectories**, not executed implementation tests or a numerical search.

| # | Trajectory | Result |
|---|---|---|
| C01 | Accepted item binds memory; all assessment answers say false | Binding still requires HAS; attempted bypass excluded by (c). |
| C02 | Trivial migration/optimization/revert occasion; sound false qualifier answer | Assessment need not activate memory; qualifier preserved. |
| C03 | No detected occasion; agent discovers suspected recurrence or material prior choices | Upstream predicate and disclosed E3 duty remain; no proof of automatic detection claimed. |
| C04 | Branch/foreign PEM update absorbed without project publication acceptance | B1 survives. |
| C05 | Overlay owner route matches candidate-only authority bytes before acceptance | B1 survives. |
| C06 | Add matching terms when new matches displace old matches at cap 10 | B4 survives. |
| C07 | Schema 1 memory with no typed applicability fields | Still usable through other paths; item C is optional. |
| C08 | Overlay retires or narrows a base entry | Union retains the base candidate floor; valid composition still required. |
| C09 | Unreadable memory; owner A→B; restore readability | Net stale state is recoverable; positive control for B5. |
| C10 | Unreadable memory; owner A→B→A; restore readability without reconciliation | B5 survives. |
| C11 | Non-floor recurrence coordination, unavailable slots, records-only `DECLINE` | B3 survives. |
| C12 | Change material entry evidence/coverage while retaining the enumerated matching facts | B2 survives under the admitted ID-based reader interpretation. |
| C13 | Bound owner or candidate-relevant entry advances between result admission and clean rebase/integration | Intended guard can catch changed facts; full claim remains conditional on B1/B2 and step-9 revalidation. |
| C14 | Memory changes only after integration | Historical guard need not reopen old work; current discharge still applies to ordinary terms; A10-R1. |
| C15 | `REPAIR` answered `NOT_MATERIAL`; migration alone; material revert answered `UPDATE_PROPOSED` | Review judges materiality; migration exclusion holds; proposed update only derives a principal decision. |
| C16 | Unavailable implementer result with a real independent `REVIEW(X)` | Required review item is useful on this path; it cannot establish universal coverage of C11. |

The out-of-matrix pass reconstructed acceptance provenance, temporal coverage, judgment holders and monotonicity before applying the author's §7 list. It found C04/C05, C06, C10–C12. The proposal's discriminators were reviewed as proposed future cases; none was represented as run. No accepted D1/D2 claim was needed for these judgments, and no upstream scientific/numerical challenge was found.

## Advice on proposal §9 open decisions 1–6

1. **Advice — reader realization:** prefer the pinned pure reader after B1/B2/B5 are fixed. Preserve accepted provenance and complete material dependencies; “no mirror” alone is insufficient.
2. **Advice — candidate match occasion:** keep off by default. An optional assessment trigger is compatible with the unchanged activation qualifiers; a hit must not itself assert applicability.
3. **Advice — contract fields:** both intent and explicit memory binding/terms have useful roles. Accept their semantics before schemas; repair the `memory.terms` tightening classification under B4. Keep under-declared intent as an explicit review limitation.
4. **Advice — promotion reverse impact:** keep the stronger rule for owner-recorded proposals if measured burden is acceptable. Show proposed status and do not infer normative force or invent a missing owner route.
5. **Advice — stale-HAS route:** reuse `INCOMPLETE` initially after repairing dependency coverage and records-only handling. A lighter refresh route would require its own architecture decision; do not add it preemptively. Measure actual budget consumption.
6. **Advice — cap 10:** acceptable as a proposed match-path default, not as established adequacy. Retain uncapped explicit/owner-bound candidates, omission disclosure and canonical search; require the monotonicity discriminator before any R1 treatment of term additions.

## Verification, limits and gaps

The candidate was extracted with `git archive` under the named scratch directory. All judgments and checks above use that snapshot or explicit immutable Git objects, not current working files. The full candidate/baseline diff contains exactly two added files, 271 and 80 lines, 351 insertions total.

| Required check | Observed result | Limit |
|---|---|---|
| `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` at candidate | PASS, 5 tests | Routing/lifecycle structure only; log `consolidation.log` in scratch. |
| `git diff --check 4f055e5c… 0368198…` | PASS, no whitespace errors | No prose-semantic adequacy inference. |
| `git diff --stat 4f055e5c… 0368198…` | Two proposal files, 351 insertions | No implementation in delta. |
| `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md` at candidate | PASS with original Git database supplied: schema 1, 5 families, 0 notices | The first archive-only invocation failed because route realization lacked a local Git repository; retained in `pem-validation.log`. Successful rerun used `GIT_DIR=<original repo>/.git`, `GIT_WORK_TREE=<candidate archive>` and candidate source; log `pem-validation-with-git.log`. Schema validity does not reconcile SSDS lineage. |
| Frozen paths compared baseline→candidate | PASS: no byte changes in either architecture document, root PEM, `source/`, `dist/`, or `orchestrator/src/` | Exact Git-object comparison, independent of current worktree edits. |

Resolved the public-source software-design entrypoint and its applicable kernel, architecture, workflow, PEM/schema, semantic-definition, evidence, testing and Git owners. Read stakeholder decision items 57–59/SD-61–SD-63, Phase E E13 and §7, actual injection events, canonical PEM metadata and relevant validator provenance checks. Catalogue material was context for existing routes, never authority over the Manual.

**Task-local HAS.** Project policy independently designates `main` as the integrated PEM line; the bound G2 workplan §1 identifies its exact state below. Candidate PEM bytes are identical, so there is no task overlay. Foreign lineage is retained explicitly rather than repaired or treated as absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: "hjin98/scientific-software-development-system@af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md (blob 1561797125622f355f84eb27319f87e8fa4227d9; inherited protocol-project lineage)"
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: "External/historical hypothesis about proxy qualification; independently reconstructed prose semantics; structural passes do not qualify A10 adequacy."
  - id: PC-001
    disposition: NOT_APPLICABLE
    reason: "Foreign capability binding; no successor profile implementation or mutation here. Frozen-path duty comes directly from this handoff and was checked."
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: "No canonical router repair or generated-package change is being performed."
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: "No immutable source fallback publication or release lifecycle mutation."
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: "No bootstrap publication; exact candidate and governing source were supplied and independently resolved."
```

Searched canonical metadata of all five families irrespective of summary or temperature; no notices exist in this publication. No family was granted local incidence or normative force. Partial historical coverage remains a limitation; no broader absence claim is made.

**Gaps.** No A10 implementation or executable model exists at the candidate, so reader safety, runtime determinism, replay, counterexample tests at real owners, false-positive rates, recall, cost and live independence enforcement are unqualified. No external source handoff or author's earlier review rounds were supplied or relied on. Final behavior of every future ranking, route resolver or template is not established. These are explicit future qualification needs, not executed §7 discriminators. The blockers are established at the proposed decision level without substituting an invented model for a real owner.

At entry the live worktree was clean at `22804035f28069606f1e5c955a5df57aa725a7bc`. During review unrelated fitness-test and Admission source/test edits, plus shell/editor/agent configuration paths, appeared concurrently. They were not used, edited, staged or reverted. The only repository file written by this reviewer is this record; scratch remains under the named `/tmp` directory. No commit, push, branch switch, acceptance, PEM edit or implementation action was performed.

## Scientific checks and common-mode limits

Material findings are B1–B5, with A10-R1–R4 as the bounded mechanism/qualification register. **No realized scientific results were produced, run or reviewed.** The executed tests and validator provide software structural evidence only; scientific null envelope: zero scientific datasets, simulations, estimators or empirical outcome claims.

Variant disclosure: 16 static semantic trajectories, C01–C16, selected for acceptance provenance, trigger fidelity, monotonicity, temporal freshness, unavailable-result judgment, overlay preservation and item-C independence. There was no fitted threshold, numerical optimization or selection among scientific results. No consequential reliance on accepted D1/D2 authority occurred, so no D1/D2 tension search is claimed. Unanswered implementation and empirical parts are the gaps above.

The reviewer is of a different model family from the amendment author and did not author the candidate. Shared dependencies remain: the same canonical Manual/PEM corpus, proposal framing, Git object database, Python toolchain and repository structural oracles. Different family and a separate reviewing context do not establish epistemic independence from those sources. Owner reconstruction and explicit counterexamples provide a distinct reasoning route; the five green structural tests remain narrow evidence. The author's earlier same-family rounds were not a premise. No subagents were used.

## D4 boundary

**D4 stays not authorized for A10.** Repair and independently re-review the proposal; stakeholder acceptance remains separate. Any eventual implementation needs the reviewed G2 placement/workplan change and the scoped PEM-lineage prerequisite. This record changes no accepted Manual text, protocol doctrine, Phase E acceptance, runtime qualification or native cutover authority.

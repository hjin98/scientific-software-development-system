Governing SSDP version: 7.2.1.

# SSDS 8 gate G1 — decision brief for candidate dddfedf

This brief presents gate G1 for the stakeholder's explicit decision (Phase C handoff §8 step 6; workplan §25). It is coordination evidence, not authority: it accepts nothing, and the stakeholder's decision, recorded verbatim in the stakeholder decision record, is the only acceptance. **D4 stays NOT AUTHORIZED** whatever is decided here; shadow implementation needs G2.

## 1. What is being decided

| Item | Identity | Status |
|---|---|---|
| SSDS 8 Architecture Manual | `orchestrator/docs/ssds-8.0-architecture.md` at `dddfedf72ed9711b8fcd46865b5c99eb50771ac5`, blob `b4077eb5879570b0aee56b068be8588beeaa5e9e`, `manual_version: 1.0.0` | proposed; asked for acceptance |
| Workplan design revision 24 | blob `11b1462b20dac578af5e3e14f9df616a1da424d0` (§21 preamble; §25 criteria 2, 4, 11, 13) | proposed; asked for acceptance |
| Mechanism catalogue | `orchestrator/docs/ssds-8.0-mechanism-catalogue.md`, blob `31d7a8a3477a9a0c127786f75b698959bc313cd4` | **not** asked for acceptance: non-authoritative G2 input with residual register RR-1 to RR-11 |
| Proposed defaults | Manual §0.6 | asked for acceptance or change |

The independent technical evidence is `qualification/ssds80/MANUAL-REVIEW-SSDS-8.0-DDDFEDF-DIFFERENT-FAMILY-PASS.md`: a GPT-family G1 Review, engaged by the stakeholder, **PASS, no G1 blocker**, under the revision-24 bar.

## 2. G1 criteria (workplan §25: criteria 1-8, 11, 12)

| # | Criterion | State and basis |
|---|---|---|
| 1 | Protocol 7 inheritance reconciliation passed independent Review | met: Phase B PASS covers Phase A (`WORKPLAN-REVIEW-SSDS-8.0-E23F142-PASS.md`) |
| 2 | one accepted Manual resolves every §21 obligation at the architecture level | technically met: the dddfedf Review's closure audit found no §21 item or §16.2 row undecided; acceptance is criterion 12 |
| 3 | one canonical writer per ledger; no document, profile, view or scheduler enacts a transition | technically met (Manual §3.1, §8.1, §26.1) |
| 4 | primitives and derived semantics specified at the level of their semantics, the §6.6 uniqueness argument checked | technically met (§1-§7; §5.6); exact algorithms are catalogue material for G2 |
| 5 | every §16.2 and §18 inherited guarantee carried, replaced, retired with reason or closed | technically met (§26.4; the Review found no undecided row) |
| 6 | concurrency correctness rests on admission-time validation, residual risk stated | technically met (§9, §8.3) |
| 7 | intake is the single route; migration is coverage refinement plus qualified promotion with per-subject cutover | technically met (§18, §19) |
| 8 | persistence, quorum admission, currentness, publication, known-loss recovery, confidentiality and evolution specified | technically met (§21-§25, §27) |
| 11 | independent D3 Review finds no G1 blocker or active Serious Challenge | met: dddfedf PASS |
| 12 | explicit stakeholder acceptance of this major architectural change | **open: the stakeholder's decision** |

"Technically met" means one independent Review found no defect at the architecture level. It is not executed evidence.

## 3. What acceptance commits to, and its known costs

Accepting the Manual accepts these decisions with their disclosed costs (Manual §0.3, §32.2-§32.3; closure map §5):

- **Level split (SD-47, revision 24).** G1 judges architecture; every catalogue mechanism, including the realizations of SD-36 to SD-46 and the author's earlier choices under record item 19, stays proposal material that G2 accepts, replaces or drops against executable models, at the same no-blocker bar.
- **Independence (SD-47 A, SD-48, SD-49).** One judged-content rule for every review kind; no author of the judged content is an independent judge, except an owner's disposition of a failing assessment; where no eligible independent judge exists, the obligation waits on human attention. Cost: in a project with few qualified humans, work stalls until policy names a judge.
- **Disagreement (R9, R14).** A standing adverse judgment blocks the contrary passing judgment, including compositions no consumer uses, until its author, the owner or an upheld challenge ends it; one reviewer's NO-PASS can hold work.
- **Publication (R4).** A crash inside the publication window costs a human decision, and for D1/D2 subjects a fresh revising review, acceptance and gate.
- **Current-state discharge (SD-36 to SD-41).** A later change to an integrated item's outputs reopens and re-dispatches it, spending its budget; five routing cases are named G2 reopen triggers (RR-4 to RR-8).
- **Exact content identity.** A line-ending or mode change is a revision change needing re-acceptance (and, for D1/D2, a revising review and gate); runners must materialize Git bytes exactly.
- **Evidence matching (SD-17, SD-18, SD-23).** A failure becomes stale mechanically only through runs matching its pins and recorded attributes; classes that do not observe external reads send failures to the owner.
- **D1/D2 revisions (SD-16, SD-19, SD-22).** No `NATIVE` D1/D2 revision, however produced, is accepted or gated without a revision-assessment record for exactly that revision, current only within its revision run; no override exists.
- **Work-key reset (dddfedf N2).** Changing an item's prose or fixed fields starts new work; earlier output it keeps is outside the new work's judged content, carried only through re-review findings.

**Proposed defaults (§0.6):** checkpoint interval 1,000 entries; 168-hour execution cap; budget 3 (cap 10); mutation threshold 0.70; `HARD` qualification bounds (≥ 0.95 detection, ≤ 0.01 false positives, frozen samples); cutover reconstruction minimum; 300-second takeover wait; entropy threshold 4.5 bits per character. Each may be accepted or changed now or later through its lifecycle record.

**Product scope:** the Manual marks no inspectability surface beyond the requested deliverable (§0.5); nothing needs product-scope acceptance.

## 4. What stays open after acceptance

- **Evidence.** Every runtime check of Manual §31 is UNEXECUTED; no SSDS implementation exists. The diagnostics are design checks of the catalogue only. The full `--mutations` run was green at candidate 63's tree (the model is byte-unchanged since); the dddfedf reviewer reran the core and review-scope families, not the whole sweep.
- **Mechanism.** Register RR-1 to RR-11 (catalogue C.2), including the replay of earlier mechanism findings (RR-9) and the diagnostic's limits (RR-10); the dddfedf Review added a per-state route-eligibility discriminator to RR-11 (its N4). A G2 finding that a Manual decision is unrealizable reopens G1.
- **Aids.** The closure map still describes candidate-61 mechanism in some rows (dddfedf N3); it is a subordinate aid.
- **Provenance.** Phase B N1: the 2026-10-12 governing-version adoption instruction exists only as the workplan's paraphrase; only the stakeholder's restatement or recovered evidence closes it.

## 5. Common-mode and confidence

The Manual's author is of the Claude family; the PASS is one GPT-family Review, engaged by the stakeholder. Several earlier reviewers, including Phase B's and the last four, were GPT-family; most others Claude-family. They share the repository, source corpus, workplan framing, toolchain and diagnostics. An earlier PASS (candidate 38) was later countered by a same-family Review. A corroborating Review is not required by criterion 11 and is the stakeholder's choice.

## 6. Decisions the stakeholder may take

1. **Accept G1**: the Manual at `dddfedf` and workplan revision 24, with the defaults as proposed or as changed. Then the author records the decision verbatim, marks the Manual and revision accepted with their bounded impact, and the next work is the G2 shadow D3->D4 workplan (criteria 13-14).
2. **Ask for a corroborating Review first** (another family or engagement), then decide.
3. **Accept with changes**, naming them; a change to a Manual decision needs a new candidate and its Review.
4. **Decline or defer**, with the reason recorded.

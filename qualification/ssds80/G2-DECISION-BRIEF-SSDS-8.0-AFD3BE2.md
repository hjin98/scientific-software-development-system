Governing SSDP version: 7.2.1.

# SSDS 8 gate G2 — decision brief for candidate afd3be2

This brief presents gate G2 for the stakeholder's explicit decision (architecture workplan §25 criteria 13-14; G2 workplan §6). It is coordination evidence, not authority. It accepts nothing: the stakeholder's decision, recorded verbatim in the stakeholder decision record, is the only acceptance or authorization. Until that decision, **SSDS 8 D4 stays NOT AUTHORIZED**.

## 1. What is being decided

| Item | Identity | Status |
|---|---|---|
| G2 shadow D3->D4 workplan, revision 3 | `workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md` at `afd3be2640b6a6e33a3d744efd76d324c6e5931a`, blob `f7ba1940a72bbb3724b95295568b40c0757f27cb` | independent Review PASS (criterion 13); asked for authorization (criterion 14) |
| Post-review corrections | commit `cb468ecad19ba41715527b4de42d90262e02cf87` (G2 workplan §4.14): the Review's three non-blocking findings | made after the Review, not reviewed; to accept or set aside |
| Manual amendments A4-A6 | `orchestrator/docs/ssds-8.0-architecture.md` at `afd3be2` (blob `314fa5e6a065868b0bf6176418705894f86c831d`), proposed by the author under SD-53 | independent Review PASS (part 2); asked for acceptance |
| The recurrence policy | the G2 workplan's §10.2/§15.5 register row | the author's proposal (see §3) |

The Review record is `qualification/ssds80/G2-WORKPLAN-REVIEW-SSDS-8.0-AFD3BE2-DIFFERENT-FAMILY-PASS.md`. The two earlier rounds were NO-PASS: `...-13D67BE-DIFFERENT-FAMILY-NO-PASS.md` and `...-D8AB75C-DIFFERENT-FAMILY-NO-PASS.md`. Their four blockers are repaired and re-reviewed (G2 workplan §4.12-§4.14).

**What the amendments say.** A4-A6 change no decision; each clarifies or discloses.

- **A4:** where a reach crosses items or plans, the owner is the owner of the adverse judgment's target, and the reached judgment's own owner is shown on the obligation (§5.10 (e)).
- **A5:** an obligation can wait even when qualified independent people exist, if none of their records could act or have an admissible basis where needed (§32.2).
- **A6:** the costs of unrequestable runner attributes and of a change of a class's declared attributes (§17.5), and two reopen triggers (§32.3).

## 2. The G2 criteria

| Criterion | Evidence | State |
|---|---|---|
| 13: a shadow D3->D4 workplan derived from the accepted Manual | each register row names the Manual decision it realizes (G2 workplan §4.2) | met; Review judgment 1 |
| 13: each catalogue mechanism accepted, replaced or dropped against executable models | §4.2, from Stage S steps S1-S5 (`qualification/ssds80/models/`, `run_models.py --seeds`) | met; Review judgment 2 |
| 13: every residual-register entry closed | §4.11 (RR-1 to RR-11) | met for G2. Production-owner checks are carried to Stage D, never claimed. |
| 13: bounded to shadow operation | §2 item 1, §5.1 item 2, §5.2 | met |
| 13: independently reviewed | the afd3be2 PASS | met |
| 14: the stakeholder explicitly authorizes the shadow implementation | this decision | open |

## 3. What authorization commits to, and its known costs

Authorization opens **Stage D**: Phases D-H of the architecture workplan (§23), as G2 workplan §5 makes them concrete.

- **Phases.** D builds a read-only kernel with a human-gated shadow genesis. E adds a read-only interface and workflow layer. F runs Admission and the Dispatcher in shadow. G pilots intake and migration. H covers adversarial and fault qualification.
- **Shadow only.** SSDS never holds authority over any subject. Every subject is `LEGACY(p)` or `UNGOVERNED`, and the document-controlled 7.2.1 baseline keeps governing. The shadow ledger sits outside anything document control reads, and no SSDS process holds a credential that can move a governed ref or file. No cutover happens.
- **Delivery.** SSDS ships as a Core extension (`sdp-orchestrator-ssds`, namespace `sdp_orchestrator.ssds`) through Core's existing entry-point group, so no Core change is needed. The architecture fitness checks come first. Protocol `source/`, `dist/`, profiles and the frozen Architecture 1.6.0 stay untouched.
- **Evidence rule.** Expected values come from the settled register, never from the catalogue's §31 tables. The 27 Review-named discriminators join their acceptance groups.
- **Review cadence.** Each phase ends with an independent implementation Review and accepts nothing; acceptance is G3.

**Decisions this authorization would leave to you later.**

- **The shadow genesis human gate (Phase D):** yours.
- **Every live agent trajectory or measurement spend (Phase E, Phase F):** a campaign needing its own frozen plan, its own Review and your separate authorization. G3 cannot be met without that live evidence (criteria 9-10).
- **The external scientific repository pilot (Phase G):** needs that repository owner's permission and a read-only clone.

**The recurrence policy.** It sits inside SD-54's chain rule, but SD-54's received message ended mid-word, so this part is the author's proposal (d8ab75c N1):

- once a coordination condition has persisted through **3** answers that left the item unchanged (a proposed default), the chain's next decisions are held for human attention, with the convergence duty in the brief;
- only an authenticated human's answer counts on a held decision, and it continues the chain as any answer does.

**Costs.**

- **Implementation effort:** the shadow system is a substantial build.
- **Review effort:** each phase's implementation Review. GPT-family Reviews through the stakeholder's Codex account are budget-limited.
- **Measurement:** campaign costs, decided separately.
- **Disclosed costs:** the Manual's §32 costs (owner work, human attention, re-dispatch churn, fail-closed waiting) are measured at G3, not claimed away.

## 4. What stays open after authorization

- **G3** (criteria 9, 10, 15): every acceptance group executed at its production owner, the live measurements, and independent implementation Review. Nothing at G2 qualifies production behaviour (DS-001).
- **G4:** native cutover, per subject.
- **A4-A6**, if not accepted now: the `2a17a83` text keeps governing.
- **Authority-index residue:** its front matter still reads `protocol_version: 6.6.0` (finding FFBAD17 N7). It is outside this cycle and can go to a repository-hygiene task.
- **Empirical uncertainties:** Manual §32.5.

## 5. Common mode and confidence

- **One reviewer family.** All independent Reviews of the G1 Manual, of A1-A6 and of the G2 workplan were GPT-family. The last three ran through the same Codex channel the stakeholder supplies. A single family improves process diversity over self-review but is not epistemic independence.
- **Author-written models.** The author wrote the design models and their stated expectations. The Reviews reconstructed them independently and found the defects the author missed: B1 in two successive rounds, and B2 twice.
- **Convergence path.**
  - The routing family took three rounds and was settled by consolidation: one answer-qualified chain, and an exhaustive property check over 14,508 answer chains.
  - The finding index took three rounds; it is now 712 findings with per-finding witnesses and a self-tested inventory check.
- **What remains uncertain:** whether the settled mechanism is adequate at real owners. That is what Stage D and G3 test.

## 6. Decisions the stakeholder may take

1. **G2: authorize** the shadow implementation (Stage D, Phases D-H, shadow only) under G2 workplan revision 3. Choose whether that is with or without the post-review corrections at `cb468ec`; the author recommends with them. Optionally also accept the recurrence policy as proposed, or change its count or human hold.
2. **A4-A6:** accept them. Choose whether as reviewed at `afd3be2`, or with the N1 (A6 wording) and N3 (A4 locator) corrections at `cb468ec`; the author recommends the latter, which narrows A6's claim as the Review recommended.
3. **Defer or redirect:** for example, ask for another Review of the post-review corrections first, or narrow Stage D to Phases D-E before Admission is built.
4. **Separately:** whether to open a repository-hygiene task for the authority-index residue.

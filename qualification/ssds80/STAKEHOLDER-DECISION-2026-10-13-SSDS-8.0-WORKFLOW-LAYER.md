---
kind: stakeholder-decision-record
governing_protocol_version: 7.2.1
target_system_version: 8.0.0
decision_date_utc: 2026-10-13
status: stakeholder-adopted
decides: SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE design revisions 5-6 (workflow execution and verification layer; doctrine-realization objective)
answers: qualification/ssds80/WORKPLAN-REVIEW-SSDS-8.0-FFBAD17-NO-PASS.md N1 and N3
---

Governing SSDP version: 7.2.1.

# Stakeholder decision: SSDS 8.0 workflow execution and verification layer

This record preserves the stakeholder's instructions of 2026-10-13 verbatim, as the independent Review of `ffbad17` (finding N3) required. The workplan's §0.1 cites it. The stakeholder owns the SSDS 8 line and its objectives. This record accepts design principles and objectives. It does not accept the D3 architecture: that still needs an independent D3 PASS and explicit stakeholder acceptance of the major change (workplan §25 items 11-12). It authorizes no D4.

## Verbatim instructions

**1. Direction (2026-10-13, first message of the session).**

> "Now let's discuss how the workflow system of the orchestractor would work. In reality, one rarely executes according to the initial plan. The workplan have to be constantly amended, revised, and reshaped as new gaps and problems are discovered during implementation and execution. What does the current workflow handling look like? I am assuming that the orchestrator would automatically handle relaying of work from one role to another, context management, and request to change of the workflow by an agent. I suggest role-based workflow execution, where there should be a principle executor who have the authority to handle the workflow and offload work to other roles. The implementer, for example, should not have the authority to modify or redefine the workplan, and the reviewer should be handed a clean context to judge the work being done. Those information will be handed back to the principle agent, then make decisions based on information provided by the other agents. According to the 7.x epistemic discovery requirement, there should also be a deterministic flow of important discoveries and decisions deemed important enough to be reported back to the human inspector. That should be handled and relayed automatically and be reported by the principle agent, where questions will be raised and presented through the orchestrator program. The human investigator then can interface cleanly and handle the important questions while letting the agents as well as the deterministic framework handle the rest automatically and seamelessly. Take a look at the current SSDS 8.0 workplan and see whether the proposed architecture supports it. More importantly, the deterministic machinery should be the backbone for all the doctrine and functionality claimed by SSDP, and provide the deterministic machinery to reliably achieve them, as the latest qualification evidence already suggests that pure-language driven SSDP cannot reliably achieve all the functionality and improvements it claims. Think carefully about how we should achieve this, and how the deterministic machinery would integrate with the SSDP doctrine and functionality to create a robust scientific software development and reporting system, with a deterministic data-flow framework with AI agents comfortably sitting on top and enhanced by it. Offload as much work as possible to deterministic machinery and let agent only handle things only it can handle, like semantic analysis, concept handling, and routine decision-making."

**2. Decision classes and verification (2026-10-13).**

> "I particularly agree with your permission classification system. As we've seen from the SSDP qualification lesson, non-conformance to language directives are expected. There should thus be deterministic verification machinery: Work obligations, boundaries, and expectations be written by agents into machine-readable form. Then the implementer would implement, but the deterministic verification machine would verify whether all job obligations are complete and any over-stepping of boundaries. The machine should basically add an additional layer of check to make sure that each agents are within it's authorized boundaries, executed obligations, and reported as faithful. Complex semantic and logic are the job of the reviewer, but basic domain and keyword checks, and basic logic and mechanical verification should be achievable by the machines."

The "permission classification system" is the decision-class classification R0 (machinery), R1 (principal), R2 (independent review) and R3 (human) proposed in the session and realized in workplan §7.5.

**3. Drafting instruction (2026-10-13).** "Yes, proceed and draft it." (Design revision 5, `ffbad17`.)

**4. Review route (2026-10-13).** Asked how the independent D3 Review of revision 5 should run, the stakeholder chose "Fresh subagent here (Recommended)": a fresh-context agent launched with a neutral handoff, with the shared model family recorded as a common-mode dependency. That Review is `WORKPLAN-REVIEW-SSDS-8.0-FFBAD17-NO-PASS.md`.

**5. Answers to N3 and N1, and repair instruction (2026-10-13).**

> "N3: I've accepted your design principles so record it. N1: Yes my proposed "reliably achieve all doctrine" is a hope and realistically the limit to what a machine can do must be tested. I do not expect perfection any time soon, but working toward it as we discover challenges and I'm hopeful we will approach the goal with some success. Now proceed to fix the findings. Write a reviewer prompt in the end and I will let ChatGPT handle it."

## Decisions adopted

| # | Decision | Realized in (workplan) |
|---|---|---|
| SD-1 | Role-based workflow execution. A principal executor coordinates and delegates; implementers have no authority over the workplan; reviewers receive a clean context; results return to the principal for decision | §7.5, §7.8, §9.6, §9.7 |
| SD-2 | A deterministic flow carries important discoveries and decisions to the human inspector through the orchestrator, while agents and the deterministic framework handle the rest | §7.9, §9.8 |
| SD-3 | Decision classes R0-R3 are the design direction | §7.5 |
| SD-4 | Obligations, boundaries and expectations are machine-readable. Deterministic verification checks obligation completion, boundary overstep and faithful reporting. Complex semantics stay with reviewers; basic domain, keyword, logic and mechanical checks are done by machine | §7.6, §7.7 |
| SD-5 | **The design principles of revision 5 are accepted (N3).** This includes the interpretations the Review named as needing stakeholder acceptance: keyword and prose checks are non-blocking `HEURISTIC` signals; the objective is read as bounded by what machinery can enforce, with agents doing semantic analysis, concept handling and routine decisions | §0, §1.1-§1.3, §2.5 (A5-A9), §7.7 |
| SD-6 | **The doctrine-realization objective is an aspiration whose machine limits must be tested (N1).** Perfection is not expected soon. The target is progress as challenges are discovered, measured rather than claimed. Every realization claim stays bounded to its mechanism and its evidence | §1.1, §7.7 (realization levels), §22 (doctrine-realization measurement), §26 |
| SD-7 | Repair the `ffbad17` Review's findings (design revision 6). The next independent D3 Review is by ChatGPT, a different model family, from a handoff prompt written at the end of the revision | workplan revision 6; `REVIEW-HANDOFF-SSDS-8.0-REVISION-6.md` |

## Not covered

- The 2026-10-12 instruction that adopted 7.2.1 as the governing version and directed the rebase (workplan §0.4) was given in an earlier session and is not reproduced here. It remains recorded only as the workplan's paraphrase until the stakeholder restates it.
- Acceptance of the SSDS 8 architecture, of the Architecture Manual, or of any marked product inspectability surface: these are later decisions.

# Independent D3 Review — SSDS 8 Architecture Manual amendments A1–A3, candidate 2a17a83 — PASS

```text
GOVERNING SSDP: 7.2.1
REPOSITORY:    hjin98/scientific-software-development-system
BRANCH:        ssds-8.0-graph-native-architecture
CANDIDATE:     2a17a8305db5ed312dc453f9d86ccf5faee8ab74
SCOPE:         Accepted-Manual amendment delta A1, A2 and A3, its affected siblings,
               and workplan §25 criterion 11; not a new whole-Manual/G2 review
MANUAL:        orchestrator/docs/ssds-8.0-architecture.md
MANUAL BLOB:   e90c1a4db68e9410e81eefafdcfcff92b888c57b
BASELINE:      dddfedf72ed9711b8fcd46865b5c99eb50771ac5
BASELINE BLOB: b4077eb5879570b0aee56b068be8588beeaa5e9e
PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
RECOVERY:      efdd1b59a7592b1cecef0a0013c35b54a7a6315d
REVIEW METHOD: Independent pinned-object reconstruction; bounded Challenge and
               out-of-matrix passes; route/state and identity trajectories;
               catalogue-disclosure comparison; candidate-archive diagnostics
REVIEWER:      GPT family; directly engaged by the stakeholder through the named
               handoff; this reviewing context did not author the candidate
```

The task handoff is `qualification/ssds80/MANUAL-AMENDMENT-REVIEW-HANDOFF-SSDS-8.0-A1A2A3-2A17A83.md`, blob `f78957c02df63660369da353f1c45ac152199509` at inspected checkout `ab5546f19c7d2712b4f5bcff4ff5701f2f0f6e7a`. Its optional A3-only command compares the candidate with itself and is empty. No earlier A1/A2 delta Review was reused; this Review used the main scope's complete `dddfedf..2a17a83` Manual diff. All candidate document/model execution used an archive of the full candidate SHA, not checkout HEAD.

Other candidate bindings:

| Artifact | Candidate blob / role |
|---|---|
| `workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md` | `7e608ec8833e4805e2d2a1cdc5049b4c0fb3370c` at this candidate; accepted design revision 24 was blob `11b1462b20dac578af5e3e14f9df616a1da424d0` at G1, with subsequent lifecycle annotations; §25 criterion 11 supplies the architecture-level bar |
| `workplans/active/SSDS-8.0-G2-SHADOW-D4-WORKPLAN.md` | `c3c0d8dd29dbcd5c5a6dd3795c88eefe4ca1633d`; proposed, unauthorized; §4.2, §4.5–§4.8 are hypotheses and design evidence |
| `orchestrator/docs/ssds-8.0-mechanism-catalogue.md` | `31d7a8a3477a9a0c127786f75b698959bc313cd4`; non-authoritative proposed mechanism and disclosure comparison source |
| `qualification/ssds80/STAKEHOLDER-DECISION-2026-10-13-SSDS-8.0-WORKFLOW-LAYER.md` | `9344ee5268a5a4228a1181d82836cfde79c2d52b`; items 44–48 and SD-48–SD-52 inspected |

Release identities were resolved from `PROTOCOL-RELEASE-STATE.yaml`. Entered the D3 role at the immutable public source and loaded the kernel, architecture, workflow/lifecycle, semantic-definition, evidence, testing, convergence and PEM owners there. PEM schema/publication and the versioning owner's frozen-profile rule were loaded for their specific questions. Relevant requirements are independent falsification before durable acceptance, exact definitions before substantive inference, no closure from synthetic proxies, bounded impact on affected descendants, and no weakening of independence to cure waiting. No new D1/D2 formulation or numerical-method authority was needed.

## SERIOUS CHALLENGE

**Two bounded defects of the accepted baseline are re-derived below: the per-state waiting contradiction at §5.10(f)/(h)(4), and conflicting obligation-identity clauses at §10.4.** SD-51 and SD-52 select their proposed resolutions. A1 and A2 reconcile these defects in the reviewed candidate; no surviving Serious Challenge against the amended architecture or governing SSDP 7.2.1 was established in this bounded Review.

This distinction matters: a technical PASS of proposed repairs does not retroactively make the accepted baseline consistent, accept the amendments, or permit dependent implementation to assume they already govern. Until stakeholder acceptance, the candidate's explicit `dddfedf` fallback remains the lifecycle boundary. A3 remains proposed too.

## Verdict

**PASS — technical D3 amendment Review evidence, with no surviving G1 blocker.**

A1 makes eligibility a property of an actual route record in the state needing it, preserving each route's own judged content and all existing independence floors. A2 lets the stated identity key govern without erasing outputs, subjects or spent iterations when only controls change. A3's nine restored risk disclosures and restored trigger group are consequences of the existing decisions, rather than additional closure permissions. Non-blocking disclosure omissions and G2 evidence limits are recorded below.

This verdict accepts none of A1–A3. Their stakeholder acceptance, G2 mechanism/workplan closure and any implementation authorization remain separate.

## G1 blockers

None found in the proposed delta and inspected affected siblings. There is therefore no surviving blocker trajectory, minimum repair or blocker discriminator to assert. The two baseline trajectories below explain what the proposals repair, not additional blockers against those repairs.

## Seven requested judgments

### 1. A1 gap: lawful baseline state and attempted alternative routes

**The stated gap exists under the literal baseline (f); (h)(4)'s per-state reading repairs its meaning, but the baseline's explicit reference to (f) leaves the meanings inconsistent.** This is not inferred from a green or red model result.

Construct already-integrated same-key work whose retained content has producers `A` and `H`. A fresh agent `N` reviews a transformation `X` retaining that nonempty content, records `NO_PASS`, and ends its task; `X` is abandoned. A distinct re-dispatch `Z` retains it and adds content produced by human `O`. Thus `W(X)` is nonempty and contained, at identical content, in `W(Z)`. A fresh independent peer's passing review of `Z`, bound to its own obligation, asserts in `D_n[Z]` but is vetoed by the standing objection (§5.10(b)–(d)). This does not redispatch the already-answered review obligation of `X`.

Policy qualifies `O` as the domain owner and `H` as the challenge adjudicator, with no other resolver. These are permitted policy restrictions; ordinary peers cannot supersede the objection or grant relief. Resolve all four routes:

| Route | Why unavailable in `D_n[Z]` |
|---|---|
| 1: author's reassessment | `N` is an ended agent execution; a fresh execution is not its author. |
| 2: owner's supersession | `O` is independent of `W(X)`, but a superseding judgment of `X` must declare `X`'s frame (§7.5). `X` never integrated, so it does not act in `Z` (§5.2). |
| 3: exact-target relief | `O` authored part of `W(Z)` and is not independent for relief of that target. `N` cannot resume as the ended actor. |
| 4: upheld challenge | `H` authored the objection's judged content; its adjudication is non-independent and refused. An open challenge is not a disposition. |

The baseline “Where every actor qualified … is among the authors” test does not describe this state: `O` is a qualified independent non-author of the objection's content. Yet no admissible independent ending record acts there. The literal baseline waiting arm fails while the liftable arm is false. A future policy adoption or integration changes the state; neither witnesses a route in the original state. There is no applicable general author-owner exception: SD-48 is limited to failing-assessment dispositions.

The owner's route-2 adjudication is a judgment on the supersession target, not a way to relabel that transformation judgment as an admitted-frame challenge adjudication. Route 4 separately requires the appropriately qualified independent adjudicator of a challenge. I found no missed admissible route in this constructed policy/state.

### 2. A1 amendment: route, target, frame and admissibility

**Closes the gap within SD-51's bounds.** Candidate §5.10(f) requires independence of the record's own judged content, acting in the state, and a basis admissible there. This imports existing definitions, rather than replacing them:

| Record | Judged content for independence | State/effect condition |
|---|---|---|
| Reassessment / superseding owner judgment | The objection's exact supersession target | Its required frame must act; its own required basis must be admissible. |
| Challenge adjudication | The objection's content at the challenge-chain root | The adjudication's declared frame and chain class apply; author exclusion is not waived. |
| Relief | The exact reached target being relieved | Its own frame must act and its own basis must be admissible; relief does not erase the objection globally. |
| Ordinary answer | The target that answer judges | It must answer that obligation's target, act there and satisfy its mechanical minimum. |

In the gap state the objection now waits with human attention, while the peer pass continues to support nothing. Making `O` independent of the larger `W(Z)` permits exact-target relief; allowing an independent adjudicator permits route 4; evaluating in `X`'s own extant frame permits acting supersession; an already-integrated enactment's records act under §5.2. These are different controls, not substitutes for one another. A subject-triple judgment is not forced into its origin candidate's transformation frame, so the abandoned-transformation restriction does not spread to unrelated targets.

“Only when” is a necessary eligibility floor, not an automatic declaration that every independent actor can issue every record. Policy qualification, correct role/target, class, Admission checks, and the four authorized routes remain necessary. Conversely, a route with an unavailable basis is not made available by merely counting a qualified non-author. No new actor class, record kind, persistence surface or fifth route was introduced.

### 3. A1 siblings: state quantifiers and routing

**No surviving contradiction found on the named affected surface.**

| Owner / sibling | Reconstruction |
|---|---|
| §5.10(e) | Still exactly four independent, acting ending routes. The new definition tests those routes, not peer votes. |
| (h)(1), (2), (3) | Veto still removes support; non-independent/refused records end nothing; supersession and relief keep distinct exact targets. |
| (h)(4) | Waiting now uses the same per-route/state eligibility as (f). No promise that a qualified person alone can end every veto. |
| (h)(5), (6) | No new permissive cross-frame effect or admission-order tie-breaker. Eligibility reads the actual state rather than publication timing. |
| (h)(7), (8), (9) | Required class and one `W` remain; derivation of the owner's adjudication is distinct from dispatchability of an admissible answer. An ineligible owner can have a derived obligation that waits. |
| §10.2 | `HUMAN_ATTENTION` now explicitly includes an objection with no eligible route, as well as a judgment obligation with no eligible answer. |
| §10.3 | Dispatch requires an eligible answer, independently of readiness and of another route's availability. An available challenge route does not authorize dispatching an ineligible owner supersession. |
| §10.3 “One class waits by design” | Its stale-basis, non-blocking-work case remains a particular waiting case. It does not say it is the only possible waiting case; the preceding text explicitly handles missing-judge waiting with a biting veto. |
| §0.3 R9 and R13 | First acting answers, `REFUSED`, independence and missing-judge attention survive. The one failing-assessment exception stays narrow. |
| §32.2 | “Eligible” resolves through the new owner, so waiting costs include route/state ineligibility. Its illustration about few humans is narrower than the whole cost; N1 recommends making the added example explicit. |

### 4. A1: no non-independent or administrative closure

**No new closure route found.** The amendment changes availability classification, not the support floor. Section 5.5 still gives a non-independent or vetoed pass base `F`; §5.10(g), §10.3 and §10.4 prevent it from answering/discharging around the objection. Human attention names a decision need; it is not relief. Section 10.5's override propagates `P` within its scope and does not cover adjudication or human-attention obligations; (h)(4) explicitly says an override never ends the objection. A different independent peer's pass remains vetoed. False attestations are a disclosed trust failure, not an authorized cure for known authorship.

### 5. A1 waiting cost

**Disclosed in substance, with a non-blocking clarity improvement (N1).** Section 32.2 says a judgment with no eligible independent judge waits on human attention and can stall work; “eligible” now includes the acting/basis conditions. Section 32.3 already reopens for routinely blocking objections, acting-rule costs and excessive human attention. The new cost is waiting even with qualified independent people available, because none can supply an effective record in the needed state. The Manual's explicit abandoned-transformation example in (f) makes it recoverable. It would help a gate reader to repeat that local example in the risk paragraph; no independent-closure guarantee was silently weakened.

### 6. A2: identity, plan acceptance, work key and budgets

**The baseline contradiction exists and the candidate resolves it according to SD-52.** At `dddfedf`, §10.4 keys the obligation on item, prose and fixed fields, then says every R2 amendment derives a new one. Increasing a budget or widening a write scope relative to the accepted revision is R2 under §13.4 but leaves that key unchanged. One clause preserves `out(o)`, subjects and count; the other resets them. No executable realization satisfies both meanings.

The candidate makes the key govern and says only prose/fixed-field changes derive a new obligation. Consider an integrated item with `out(o) = {u}`, a nonempty subject set and three admitted result iterations. A control-only loosening keeps all three, even if its larger budget allows further iterations. It cannot clear the three spent iterations or turn retained `u` into previously unjudged work. The R2 revision waits for independent plan acceptance (§11.2, §11.4); a new accepted budget changes the ceiling, not the count. Exhaustion still routes to the principal under §10.4/§13.7.

Cheap sibling controls were also checked against the owners: an R1 tightening preserves identity and its existing acceptance coverage; a prose change starts new work and a new obligation; a fixed-field change does likewise; a mixed tightening/loosening with unchanged prose/fixed fields still keeps the key but needs R2 acceptance when it is not tightening relative to the accepted revision. Classification is against that accepted revision, not merely the immediately preceding delta: loosening a previously tightened control while remaining inside existing accepted coverage is not automatically a new R2. The amendment's references to §13.4 and §11.4 preserve this distinction.

The §5.10(b) work key intentionally differs from obligation identity: work provenance spans same-prose/fixed-field items and plans, whereas an obligation also names its item. A2 changes neither relation. Section 4.1 now distinguishes the failed-entry route requiring new work from the one needing new plan acceptance. Section 32.2's disclosed new-work boundary for prose/fixed-field changes remains accurate; control loosening does not acquire that reset. Detailed routing and plan-acceptance realization remain G2 work, not established by the four direct identity cases.

### 7. A3: restored disclosures and remaining gaps

**Each added risk is a consequence of the accepted decisions. None grants new acceptance, relief or staleness authority.** The risk summary has a different reader function from the detailed owner; a risk's being derivable in the body does not make its summary disclosure gratuitous. The nine risk additions were compared individually:

| A3 risk | Governing consequence / overlap assessment |
|---|---|
| Passing realization with unpinnable/unobserved external reads | §§6.3–§6.5, §17.4–§17.5 distinguish ordinary passing currency from permissive failure-stopping uses. Existing risk text covered the failure side, not this explicit passing-side limit. All other currentness conditions still apply. |
| Declared term later resolving to `ABSENT` | §1.3/§1.9 identity and malformed-anchor treatment; no new detector or specific finding is promised. |
| Omitted executed content in a recorded basis | §6.5–§6.6 adverse linking can retain a genuinely fixed failure; this is a fail-closed cost, not evidence of actual tracing completeness. |
| Incidental external reads | Complete external-input matching under §6.5 and runner boundaries under §17.5; hermetic execution is a mitigation, not a bypass. |
| Challenged co-submitted attestation | §5.10(f)'s fixed classification and challenge against the credited record; extends the existing fixed-at-admission disclosure with its concrete consequence. |
| Re-partition splits the rejected content | §5.10(b)–(c), §13.7 and §16.5: disjoint part scopes can each hold only a proper subset, so no individual part review contains all rejected `W`; the item-level review of the unchanged rejected result does, and carries its producers/findings. A changed result is evaluated at its actual content. |
| Directional equivalence hop | §4.4's directed reuse paths are distinct from the orientation-free comparison used for disagreement reach. Reversing a record does not supply a missing reuse direction. |
| Incomparable control-only branch and relief coverage | §5.10(c)'s same-prose/fixed-field rejection reach, §11.2/§13.4 coverage and §8.3 basis check. Relief remains exact-target even though that acceptance covers its tightenings. |
| Pending/abandoned candidate gate rejection | §5.10(d)'s cross-state adverse existence, distinct from permissive acting. Naming ordinary resolution routes here does not remove the upheld-challenge route in (e). |

The added §32.3 group restores explicit triggers concerning submodule availability, representation churn and revision runs, external reads, cross-lineage delays/`INCOMPLETE`, residual owner dispositions, relaxed readings and lenient readers. Whole-tree fallback and failures going to the owner already overlap earlier trigger bullets; that is harmless repetition, not another decision. N2 records remaining disclosure details; A3 should not be described as literal exhaustive restoration.

The comparison covered catalogue §32.2–§32.3 and body/refinement passages identifying costs and residuals, especially §§6.5–§6.6, §9.4, §10.4, §13.7, §16.5, §17.5 and §30. Catalogue claims about globally accumulated retained units, broad owner exceptions, or earlier routing interpretations cannot simply be restored: they are proposed mechanisms superseded or bounded by the current scoped `W`, SD-48, SD-51/52 and the register. In particular A3 correctly replaces the old re-partition account with the current part-scope/item-level distinction. No additional omitted architectural invariant or decision was established by this bounded disclosure comparison.

## G2 register entries and evidence obligations

These are existing register consequences, not new G1 blockers or a Review of the settled-mechanism register as a whole.

| Entry | Required downstream discrimination |
|---|---|
| RR-11 / RR-10 | Carry per-record judged content, correct declared frame/acting state, policy qualification/class and actual basis admissibility through the executable resolver and Dispatcher. Test the Q1 state, later independent relief, non-author owner controls, human-author reassessment, unknown lineage and the narrow failing-assessment exception. |
| RR-4 / RR-5 | Carry real `out(o)`, subject union and admitted iteration count through control-only amendments, acceptance waiting, budget changes and a coordination response leaving the condition true. The four identity cases directly encode a Boolean decision; they do not implement this assembled transition. |
| RR-1 / RR-2 / RR-3 / RR-9 | Re-partition's safeguard must use history-derived scoped `W` and a disjoint integrated-result target, with retained producers and findings in actual briefs. Replaying catalogue-era expected results must not restore obsolete global retained-scope or broad-exception semantics. |

The route model is bounded design evidence. `routes_per_state` uses supplied authorship, acting flags and policy choices, with a dedicated relief-basis Boolean; it does not execute production Admission, general basis currency, challenge chains, qualification/class enforcement or dispatch. Its waiting helper is the negation of its route enumeration, so agreement between them is not an independent proof that no admissible route was omitted. The Manual reconstruction above, rather than that identity, supplies the semantic judgment. These limits leave real G2/G3 checks open.

## Non-blocking findings

**N1 — Make A1's additional waiting cost explicit in §32.2.** Eligibility's canonical definition makes the current paragraph apply, and (f) supplies the concrete example. Still, a reader of the cost paragraph alone may infer that obtaining another qualified independent human always suffices. Add the local consequence that qualified independent actors may all lack a record that can act or an admissible basis in the needed state. This changes no rule and is not a G1 blocker.

**N2 — A3 leaves some specific catalogue disclosures compressed or absent.** Catalogue §32.3 explicitly reopens when failures caused by execution attributes no runner class records are made stale and later found live. Candidate §§17.5/32.2 disclose invisibility, and §32.5 names false staleness as an empirical uncertainty, but the specific reopen condition is not restored in §32.3. Catalogue §17.5 also explains the operational costs of unrequestable recorded attributes and changes to a runner's declared attribute set; §32.3 explicitly compares retained-tree/reproduction cost with disposition cost. The Manual retains broad unavailability/resource/owner-work triggers, but not these specific consequences. Preserve them as focused disclosure/runner-design considerations at G2, or add concise accurate summaries; do not claim every catalogue disclosure has been restored verbatim. They do not establish an omitted required invariant, an impossible decision, a new permissive route or a violation by an otherwise conforming realization, so they are non-blocking under criterion 11.

**N3 — Correct the optional A3-only handoff locator.** It names `2a17a83..2a17a83`, an empty diff. The main scope unambiguously names the correct baseline and full candidate; this Review executed that scope, so this clerical error creates no coverage gap here.

## Bounded Challenge / out-of-matrix result

Temporarily ignoring the supplied model decomposition, I tried to obtain permissive closure from (i) an independent but inactive superseder, (ii) an owner independent of the smaller objection but not the larger relieved target, (iii) a non-independent challenge adjudicator, (iv) a contrary peer pass, (v) waiting/attention/override, and (vi) a control-only budget reset. None survives the amended owner rules. The first five retain the objection unless an authorized independent acting route exists; the last preserves the count and acceptance gate.

I also checked the asymmetric controls: relief can become possible without supersession becoming possible; a subject-triple supersession is not a transformation supersession; plan-control classification uses the accepted revision; and a re-partition's part reviews can pass without settling an objection that still reaches the item-level result. No further locally compliant trajectory violating the protected upstream meaning was established. This is bounded falsification, not a proof of all states or policies.

## PEM applicability and historical limits

PEM activated because the named G2 workplan binds it and this amendment addresses a recurring judgment/identity family. Project policy designates `main` as the integrated publication line. Inspected local `main` is exactly the workplan-bound `af0455753e20ee54a969c844872e29e270007211`; its PEM blob and the candidate's are both `1561797125622f355f84eb27319f87e8fa4227d9`. No overlay is composed. The file's older candidate-overlay description is historical integrated content, not a new branch's self-ratification. Schema validation succeeded. No fetch or memory update was performed.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: "af0455753e20ee54a969c844872e29e270007211:PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9"
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: Synthetic route and identity greens cannot establish prose adequacy or production behavior.
  - id: PC-001
    disposition: APPLICABLE
    reason: The requested preservation check protects frozen source and profile resources; current versioning authority independently supplies the requirement.
  - id: SP-001
    disposition: NOT_APPLICABLE
    reason: No source-router repair or generated-package change is proposed by this delta.
  - id: SP-002
    disposition: NOT_APPLICABLE
    reason: This review does not construct or publish a protocol public-source fallback.
  - id: FF-001
    disposition: NOT_APPLICABLE
    reason: No immutable bootstrap publication or replacement fallback is in scope.
```

All five canonical family metadata records and current notices were searched, including entries absent from the hottest summary. DS-001 is evidence-only. PC-001's historical binding is not used as current authority: the public-source versioning owner's “Orchestration profiles” independently requires older profiles to remain frozen and independently testable. The other three lessons were not promoted by analogy. PEM coverage remains partial through `23e46543c174a8451bbadc402df63538105eab10`; its metadata cannot prove absence of later lessons. Bounded later historical intake used the two named G1 Reviews, stakeholder items 44–48, the relevant register and current Manual/G2 passages. Previous PASS conclusions were tested as hypotheses, not inherited. This is not a replay of every historical Review or every G2 mechanism finding.

## Verification and limits

Scratch and candidate archive were confined to `/tmp/ssds80-manual-review-2a17a83`, under the environment's temporary root. Candidate execution was isolated from checkout changes. Required checks all completed:

| Check | Observed result / claim limit |
|---|---|
| `python3 -B -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the candidate archive | **5/5 passed**, exit 0. Routing/lifecycle structure only. `-B` only suppresses bytecode writes. |
| `git diff --check dddfedf72ed9711b8fcd46865b5c99eb50771ac5 2a17a8305db5ed312dc453f9d86ccf5faee8ab74` | **Exit 0**, no whitespace errors. |
| `python3 -I qualification/ssds80/models/run_models.py --seeds` in the archive | **Exit 0**, self-tests and seeds OK; current/settled cases have zero misses; required historical counterexamples reproduced. Detailed accounting below. |
| `git diff --exit-code fad3ee410ab9df0d94740cebb6969e161911b126 2a17a8305db5ed312dc453f9d86ccf5faee8ab74 -- orchestrator/docs/architecture.md source/ dist/` | **Exit 0**, no changes in these complete path scopes, including tree-entry identities. Supplementary profile/snapshot path comparison also returned no changed paths. |
| Candidate `python3 source/project_engineering_memory.py PROJECT-ENGINEERING-MEMORY.md`, paired with original `GIT_DIR` and archive `GIT_WORK_TREE` | **Exit 0**, schema 1 valid, 5 families, 0 notices. Structural validity is not historical completeness or semantic authority. |

Primary model accounting, excluding seed diagnostics:

| Case group | Current/settled result | Historical comparison |
|---|---|---|
| 11 item + 12 objection cases | Manual: 0 misses | candidate61: 16; sd46_first: 11; candidate62: 9; candidate63: 8 misses; these are expected refutations, not failed current-family checks |
| S2: 7 transformation + 3 binding + 5 target + 7 route cases | Manual: 0 misses | Catalogue: 11 expected misses |
| Q1: 1 per-state question | A1 liftable-or-waiting holds with no available route | Literal baseline (f) makes (h)(4) false in that state |
| S3: 13 routing cases | Settled: 0 misses | Catalogue: 9 expected misses |
| S3: 4 identity cases | Settled: 0 misses | Catalogue: 1 expected miss, loosening keeps-and-waits |
| S5: 10 structure + 11 relation cases | Settled: 0 misses | 0 required refuted readings unreproduced |

There are **84 named primary cases/questions** in those groups. The seed stage additionally executes the history probe and the unmutated review-scope and obligation-routing families; it reported `seeds: OK`. This invocation is not the old full `--mutations` campaign, and no such campaign or full seven-family run is claimed here. The handoff requires the Stage S `--seeds` invocation for this delta. Earlier full-campaign assertions remain historical evidence, not new executions by this reviewer.

Unverified: production SSDS Admission/Derivation/Dispatcher and rendered waiting explanations; complete policy/class/lineage and basis-transition matrices; actual partition/re-dispatch integration and budget persistence; scientific evidence staleness on real runners; deployment, witness, publication, recovery, migration/cutover and operational benefit. These are not passes. This Review did not re-review unchanged Manual decisions, close the whole G2 register, rerun the whole repository acceptance workflow, build packages or authorize live shadow operation. The requested frozen paths are unchanged and the repository mutation is this review record only; those broader implementation checks are not newly required for a record-only delta review.

## Scientific-checks answers

- **Material findings:** the two baseline contradictions and their proposed reconciliation are material to admissible review/evidence governance. There is no surviving G1 blocker against the amendments. G2 evidence obligations and non-blocking disclosures are above. Asserter: the directly engaged AI reviewer, GPT family.
- **Realized scientific results / null envelope:** produced, ran and reviewed no realized scientific results. Ran deterministic governance diagnostics and structural checks only. No scientific data, simulation, numerical experiment, training/evaluation campaign or scientific-result interpretation was examined; no empirical safety, correctness rate or burden reduction is asserted.
- **Variants:** one pinned amendment candidate and one accepted Manual baseline, with no repair/selection of another candidate. The model run compares the five S1 readings, two S2 readings, two S3 routing readings, two identity readings and the two S5 case modules with their named refuted alternatives, over the 84 primary cases above; seeds are additional regression diagnostics. Semantic controls and nine A3 risk items are enumerated above. Selection followed the handoff, the affected owner relations and cheap counterexamples, not favorable outcomes. No held-out scientific data were reused, and earlier author/reviewer searches are not bounded by these local counts.
- **D1/D2 tensions:** no consequential judgment depended on a particular accepted scientific formulation or numerical method. The D1/D2 tension-search trigger did not fire; no native scientific tension-home search is claimed.
- **Unanswered parts:** no requested amendment judgment or required delta check remains unanswered. Production realization, historical completeness and the stated G2/G3 evidence limits remain open at their own gates. No delegate was used and no delegate result is pending. The requested record is the one durable home for this Review; no scientific retention/projection was changed.

## Common-mode note

The reviewer is of the GPT family, different from the Manual author's Claude family, and was engaged directly by the stakeholder. Earlier G1 reviewers were also GPT-family reviewers; this is not a new model-family corroboration of their conclusions. The handoff, source corpus, repository history, Python environment and author-supplied models/expectations are shared dependencies. Independent reconstruction of Manual route/frame/identity consequences reduces reliance on those expectations, but neither fresh context nor a different family removes common-mode risk. The design models are not production consumers or independent scientific oracles.

## D4 statement

**SSDS 8 D4 remains NOT AUTHORIZED.** This PASS supplies technical amendment-review evidence only. Stakeholder acceptance is still needed for A1, A2 and A3. G2 still requires its own mechanism/register closure, independently reviewed shadow workplan and explicit authorization; G3/G4 retain their runtime and subject-specific gates. No implementation change, commit, push or external publication was performed.

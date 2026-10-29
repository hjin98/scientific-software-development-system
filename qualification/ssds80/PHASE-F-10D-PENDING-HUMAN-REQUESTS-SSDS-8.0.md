# Phase F 10d — two prepared human requests (unsigned)

Governing SSDP: 7.2.1; Phase F revision 57, F121–F122; SD-55, SD-69, SD-82 and stakeholder item 72.
Asserter: AI implementing agent, Codex family, 2026-10-29. Infrastructure evidence only.

**Neither request is signed or admitted.** The user authorized preparation of the proposed pair in this chat's
continuation. These permanent records need the human's review and SSH signatures. No private human key was
accessed. Preparing them did not append a ledger entry or adopt a delta. Both were prepared at position 3,
head `6d43121b440743a3b6e9f78b7600a40e4fc5ba7a`, on `ssdp-shadow-2`.

The canonical original-append finding remains
`PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md` at that commit, SHA-256
`8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5`.
The original actual-append comparison remains **FAILED/contaminated**, not retroactively qualified.
No unqualified 10d, Phase F or exit PASS follows from either signature.

## FINDING: preserve the repair and qualification gap

Request: `sha256:75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a`.
Record: `sha256:6b2dbc477713971c7011ce485b93317d2183dce8e6f4b3c39e9e26e5e61ef014`.

Review [request.json](/home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a/request.json)
and [summary.txt](/home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a/summary.txt).
Sign [request-message.txt](/home/samjin/.ssds/state/ssdp-shadow-2/requests/75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a/request-message.txt)
with your own key, namespace `ssds`.

Meaning: the eight-key repair was ACCEPTED at position 2; the three reserved leaves are effective, quarantine
is empty and policy is unchanged. Its original actual-append boundary window failed during concurrent restricted
tool mount setup. No SSDS-caused writer was established; subsequent replay and passes do not qualify that append.
This is a MATERIAL, non-blocking `INSPECTABILITY_GAP` report targeting `orchestrator.program`, `ssds.manifest`
and `ssds.policy`. A FINDING cannot itself suspend work (§15.1). Its non-blocking flag does not waive the
workplan's qualification requirement. Its narrative routes to the immutable evidence home above.

## AVAILABILITY: verified retained policy bytes

Request: `sha256:bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34`.
Record: `sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6`.

Review [request.json](/home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34/request.json)
and [summary.txt](/home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34/summary.txt).
Sign [request-message.txt](/home/samjin/.ssds/state/ssdp-shadow-2/requests/bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34/request-message.txt)
with your own key, namespace `ssds`.

Meaning: the verified SSDS chain reader at position 3 returned the 11-byte LEDGER object
`sha256:da93db77ebb07776dbd095f79fe28cbf4d42340c27bc33547ed7eeb2d3c93ea1`.
SHA-256 matched; the bytes were `schema = 1` followed by a newline, and the committed policy matched.
`Policy.parse` returned no explicit domain, workflow or runner settings; system defaults apply. The observation
is `AVAILABLE` on that content digest. It is neither policy adoption nor approval of defaults, a future
availability guarantee, nor qualification of the original append. Human availability observations are SD-82's
accepted producer under catalogue §17.4; retained LEDGER objects are governed by §21.4.

## Remaining human responsibilities and execution

1. Review and sign the two messages above. Each request has one record and no adoption deltas. The signing
   command is `ssh-keygen -Y sign -f <your-key> -n ssds <absolute-request-message.txt>`; substitute only your own
   key and the selected link's absolute path. Never send the private key to an agent.
2. After signatures exist, the agent can admit each through `ssds report` or `ssds submit`, preserving separate
   command and endpoint-comparison results in one isolated host context. Unsigned requests must not be submitted.
3. Disposition the original append's specific qualification gap. A later clean append can support only its own
   bounded claim. Any changed closure criterion requires explicit governing approval; the original failure stays.
4. Choose a genuine direction for the signed `decide` refusal after the FINDING has an admitted obligation identity.
   Proposed intent for endorsement: keep the original gap open, defer its resolution, continue independent shadow
   qualification. Resolve the actual `HUMAN_DECISION` grammar and derived obligation before preparation. A refused
   request admits no decision and resolves no report; retain human direction separately in the stakeholder home.
5. Frozen-candidate 11b, complete difference classification, independent other-family review, step 12 and stakeholder
   acceptance remain separate unfinished duties. Pushing still needs the prescribed user-terminal route, unavailable
   to this continuation; no alternate credential route is authorized.

An earlier unsigned workspace `324bd39ebcf696b22fa1991ec870f8d7a0d046ef243c05d309be0cd74709d8c6` was superseded
before presenting signing links, to improve provenance wording. Do not sign or submit it. It appended nothing.

## Preparation review and limits

Fresh Codex review: PASS after correcting the proposed FINDING from custom reasons and `blocking:true` to
`INSPECTABILITY_GAP`, `blocking:false`. Minor notes were applied: provenance says `prepared-for-human-review`,
and the builder asserts its observation position is 3. Schema validation passes for the final inputs. Preparation
does not execute Admission; final signed requests still need actual authentication and effect checks.

The same review exposed a real schema defect: forbidden report reasons and a blocking FINDING could pass
Admission. Its independent repair/qualification belongs to the continuation checkpoint; it does not change these
already conforming records or the original append's status.

No realized scientific results, scientific gate evidence, pipeline selection or product inspectability surfaces
are asserted. Request-content revisions are infrastructure preparation variants, retained in the execution history.

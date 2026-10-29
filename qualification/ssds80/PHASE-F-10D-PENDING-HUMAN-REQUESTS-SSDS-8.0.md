# Phase F 10d — corrected FINDING needs one new signature

Governing SSDP 7.2.1; Phase F F121–F122; stakeholder item 73. Asserter: AI implementing agent, Codex family.

**AVAILABILITY was program-ACCEPTED at position 6; do not sign it again. Original FINDING was refused at
position 5. The corrected FINDING below is unsigned and unsubmitted.** A new signature is required because
the message changes. The original append's FAILED/contaminated qualification gap remains open. Review also
found a D4 provenance-conformance gap in the accepted AVAILABILITY; see the canonical 10d evidence. Program
ACCEPT/QUALIFIED is not full Manual conformance or 10d/exit acceptance.

## Current signing request

Request: `sha256:785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd`.
Record: `sha256:6cb7310af48103616eed3c65c4047b7353374f4b754cc2d23e991d6de32fd307`.
Base: position 6, observed product `425c92581c0431efd0d4084a9e13bdde93175506`. One record, no candidates or
adoption deltas. Human signer is the registered stakeholder key; no private key was accessed by an agent.

Review [request.json](/home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd/request.json)
and [summary.txt](/home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd/summary.txt).
Sign [request-message.txt](/home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd/request-message.txt):

```bash
ssh-keygen -Y sign -f /home/samjin/.ssh/ssds-genesis -n ssds \
  /home/samjin/.ssds/state/ssdp-shadow-2/requests/785d8fa6c50221a3b2d6a0b6ec4cb25b6cfa5f68d6154e0878f5da4e2c2192dd/request-message.txt
```

The key path comes from the recorded genesis signing setup; the command runs only in the human's terminal.
Reply "Signed" after it creates request-message.txt.sig. The agent then verifies the signature over this exact request and submits it through isolated SSDS checks. Unsigned requests must not be submitted.

## Meaning and exact changes

The report remains a MATERIAL, non-blocking INSPECTABILITY_GAP on orchestrator.program, ssds.manifest and
ssds.policy. The eight-key repair was ACCEPTED at position 2, reserved leaves effective, quarantine empty and
policy unchanged. Its original actual-append boundary window FAILED/was contaminated during concurrent restricted
tool setup; no SSDS-caused writer was established. Later passes do not retroactively qualify it. The stakeholder
must disposition that specific qualification gap before an unqualified closure claim. A FINDING cannot itself
suspend work (§15.1); non-blocking does not waive the workplan requirement.

Complete narrative stays in the same immutable evidence artifact from commit
`6d43121b440743a3b6e9f78b7600a40e4fc5ba7a`, original path
`qualification/ssds80/PHASE-F-10D-SHADOW-LEDGER-EVIDENCE-SSDS-8.0.md`, content SHA-256
`8d29d152af813ad6942dd272c7b8bfb52da332f91af2b605d0efa50ad7ef98a5`. The native Git blob locator is
`9f6d5616f995b04d62c2a87e777005df903347ef`; `git show` of that id reads the exact frozen narrative.

Three fields changed from the refused proposal: locator is that same artifact's blob id, provenance is null,
and informational timestamp is refreshed. Target, reason, materiality, non-blocking flag, content digest and
supersedes:[] are unchanged. The old locator tripped the unchanged entropy policy; the blob identity passes
its declared identity grammar. Narrative provenance was outside Manual §3.2/C7, so the narrative is now only
in its canonical home. No secret detector, source code, policy or architecture was weakened.

Final schema/secret validation, exact message verification and fresh Codex review passed. One scratch real-
Admission rehearsal (throwaway key, fixture guide target) rejected the old locator and accepted this corrected
content; this is bounded rehearsal, not actual signed admission. Full native results and limits are in the
canonical 10d evidence.

## Preserved prior results and remaining duties

Original FINDING request `75ced219d746c4f3a6894f25782d2074b42bc44280075c7de9785192fa64034a` is signed
but REJECTED/SECRET_DETECTED at position 5; do not sign/re-submit it. Earlier unsigned prototype `324bd39e…`
is also superseded as a preparation. Neither finding record was admitted.

AVAILABILITY request `bb381a05ef168abe7ad80ad1c175faa00fb4bb0ae0e78ac86fc00284a7cd5f34`, record
`sha256:2716f8c4df47515c93b6304a2e1bf96b03c13955102aa4820f4d9925a1ebf9e6`, was ACCEPTED at 6. The
policy object's exact 11-byte content and AVAILABLE observation are verified. Its narrative provenance is a
separate D4 conformance gap; immutable data remains unchanged and no acceptance waiver is inferred. The canonical
evidence routes that gap to envelope enforcement and safe historical-data handling before deploying a fix.

After this FINDING is admitted, choose a genuine direction and use the actual derived obligation for the signed
decide-refusal exercise. It cannot itself resolve a report because Phase F refuses human decisions at entry.
Original-gap disposition, C7 enforcement/data handling, historical study, frozen-candidate classification and
other-family review, step 12 and acceptance remain open. Push still requires the prescribed user-terminal route.
No scientific results, scientific gate evidence or scientific variant selection are asserted.

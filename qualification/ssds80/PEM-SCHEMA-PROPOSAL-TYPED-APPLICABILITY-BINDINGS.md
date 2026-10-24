---
kind: pem-schema-change-proposal
target_repository: hjin98/scientific-software-development-protocol
target_owner: source/shared/references/project-engineering-memory-schema.md
target_owner_baseline: hjin98/scientific-software-development-protocol@aaeaf8b6b2121b9fb8aba31917c8265649c43954:source/shared/references/project-engineering-memory-schema.md (SSDP 7.2.1 public source; byte-identical to the 6.6.0 public source 22f4bdba53795da3a6f13f162529f3a843fc37ae)
target_protocol_version: a future protocol version the protocol repository chooses; not 7.2.1, whose owners are frozen
status: proposed; prepared in hjin98/scientific-software-development-system, not submitted
submission: only on the stakeholder's say-so; nothing has been opened in the protocol repository
origin: item C of SSDP 8.0 Amendment 1 revision 4 (sha256 bcf611b6c310deaca9463df5745823aca263c035606e3ebda16ecccff62d3048), routed to the PEM schema owner by SD-63 (stakeholder decision record item 59)
consumer: SSDS 8 Manual amendment A10 (proposed), §16.11 (d)(3); A10 works without this proposal
pem_doctrine_mutation: proposed here, decided only by the schema owner's own review and ratification
active_serious_challenge: none
---

# Proposal to the PEM schema owner: typed applicability bindings

## 1. Problem

Schema 1 represents applicability as free text. Each family's `applicability` is a list of cue phrases (this repository's PEM uses, for example, `frozen profile`, `protocol recovery`, `successor profile generation`), and `semantic_identity.applicability_dimensions` is prose. The project validator's only selection support, `select_applicable` in `source/project_engineering_memory.py`, matches query terms case-insensitively as substrings over each non-retired family's ID, summary, aggregation scope, applicability tags and `semantic_identity` values, and over each non-retired notice's ID, summary and applicability.

Free text serves a reading agent well and a machine poorly:

- **No machine-matchable binding to what a lesson is about.** A consumer that knows a task's owners and surfaces (an orchestrator, a review tool) cannot decide mechanically which entries concern them; it can only match strings.
- **Substring matching is noisy.** A short term matches unrelated prose; a precise term misses an entry tagged with a synonym. Neither result is evidence about applicability, and the agent-facing contract already says that index or tag output cannot prove absence.
- **Applicability meaning can drift silently.** The identity-envelope rule ("same accepted family IDs cannot silently change kind, semantic identity envelope, or applicability meaning") is enforceable for typed fields; for free tags it is a judgment the validator cannot check.

Owner routes already have a typed, immutable form in schema 1 (`authority_owner`, notice `owner`, `pem-repair-acceptance.owner`: `owner/project@<immutable-revision>:path#stable-section`). This proposal extends the same discipline, optionally, to applicability.

## 2. Proposed shape (additive and optional)

```yaml
applicability: [<existing free-text cues>]          # unchanged and still required
applicability_bindings:                              # optional
  owners:     [<owner/project>@<immutable-revision>:<path>#<stable-section>]
  surfaces:   [{path: <repository-relative path>, symbol: <optional symbol>, resolver: path | symbol}]
  mechanisms: [<term from the root's declared mechanism vocabulary>]
  regimes:    [{variable: <declared regime variable>, op: in | eq | ge | le, value: <value>}]
  coverage_note: <what the bindings deliberately do not cover>
```

- `owners` uses the existing schema-1 immutable owner-route form, so a binding names the owner a lesson concerns in the same protocol-generic way an authority binding does, never a consumer's internal identifiers. A consumer maps routes to its own identities when it reads them.
- `surfaces` names repository content a lesson concerns, by path and optionally by symbol.
- `mechanisms` and `regimes` name the mechanism family and regime predicates in a declared vocabulary, so they can be compared rather than read.
- `coverage_note` keeps the binding honest about what it does not express; free-text `applicability` remains the complete statement of meaning.

The same optional block applies to notices (`NT-###`).

## 3. Proposed rules

1. **Representation, not meaning.** Bindings that only make an entry's existing applicability meaning explicit are a within-envelope reconciliation, recorded explicitly with its evidence as the schema owner already requires for within-envelope changes. Bindings that narrow or widen meaning are a semantic change and need lineage (`SUPERSEDES`, `SPLIT_FROM` and the rest), exactly as for any change outside the identity envelope.
2. **Declared vocabularies.** The root front matter declares the `mechanisms` vocabulary and the regime `variable` names (with their value domains). A term outside the declared vocabulary is a validation error, never a guessed match.
3. **Resolution and binding health.** An owner route resolves as schema-1 owner routes do. A path surface resolves when the path exists at the accepted project state. A symbol surface may use a replaceable semantic-code resolver; the resolver is tooling, never schema authority. A binding that does not resolve makes that binding `REVIEW_REQUIRED` in `binding_health`, and current use of the entry degrades as for any unhealthy binding; it never silently narrows applicability.
4. **No absence claims.** Bindings never establish that an entry does not apply. An entry without bindings, or whose bindings do not intersect a task, may still be decisive; the agent-facing contract's search over canonical metadata, regardless of temperature or summary, is unchanged.
5. **Identity envelope.** The validator's identity-envelope check compares `applicability_bindings` as well as kind and semantic identity, so bindings cannot change under an unchanged ID without an explicit within-envelope reconciliation or lineage.
6. **Owner field for proposals.** The schema owner is asked to consider requiring a recorded owner route for `PROPOSED_FOR_PROMOTION` capabilities. Schema 1 requires `authority_owner` only for `AUTHORITY_BOUND`; a proposal for promotion without a named owner cannot be reconciled when that owner changes.
7. **Compatibility.** The owner decides between schema 1 additive-optional fields and a schema 2. In either case, records without bindings stay valid and are read through their free-text cues; no consumer may require bindings for a record to count as current memory.

## 4. Effects on other owners

- **Agent-facing contract** (`project-engineering-memory.md`): no change is needed. "Retrieval and HAS" step 2 already matches "bounded current metadata over owner, surface, mechanism/capability, regime, project scope and task"; bindings are such metadata. The HAS shape is unchanged.
- **Template** (`source/shared/templates/project_engineering_memory_template.md`): an optional commented example block, and the root vocabulary declarations.
- **Validator** (`source/project_engineering_memory.py`, implementation only): parse and validate the block and the vocabularies; extend the identity-envelope comparison; optionally a typed selection alongside `select_applicable`, whose output stays a derived, non-authoritative candidate list.
- **Evidence and versioning owners:** binding health follows the evidence owner's rules; a schema 2 would follow the versioning owner's compatibility rules.

## 5. Qualification cases (for the owner's own acceptance workflow)

1. A record with bindings and a record without bindings both validate; the latter is read through its cues.
2. A `mechanisms` term outside the declared vocabulary is rejected.
3. Changing `applicability_bindings` under an unchanged ID without a within-envelope reconciliation or lineage is rejected.
4. An unresolvable surface makes that binding `REVIEW_REQUIRED`, and current positive use of the entry degrades accordingly.
5. An empty typed selection is never reported as "no applicable memory".
6. If rule 6 is adopted, a `PROPOSED_FOR_PROMOTION` capability without an owner route is rejected.

## 6. Out of scope

Regime predicates are what a future physical-simulation sandbox would need for regime-bounded lessons; that use, cross-project memory and a user-level memory tier are outside this proposal. Similarity or embedding retrieval over PEM text is not proposed. Nothing here changes the activation predicate, retrieval, admission thresholds, maturity rules, claim strengths, the HAS shape or accepted-base selection.

## 7. Provenance

Item C of the handoff's amendment, revision 4, which passed an independent review round of the author's own model family (process independence only; static evidence; the validator was not run). The text above is re-stated against the 7.2.1 owner, which is byte-identical to the 6.6 owner the amendment cited (public sources 22f4bdba and aaeaf8b6), and it adds rule 4, the notice scope and the qualification cases. Its consumer in SSDS is amendment A10 §16.11 (d)(3), which matches only `owners` and `surfaces` and shows `mechanisms` and `regimes` without matching them.

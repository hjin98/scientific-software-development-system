# SSDS 8 Architecture Manual — Independent D3 Review, candidate e2154ac

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: e2154ac12827be11a324fe6b10b2a13dcb3753ba
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R10, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: ce44958201fc9cc0cb515b9ce700a76522f457b9
    CLOSURE MAP BLOB: 325049008a1c29f8451b946e0eb68bc9397b2dfb (review aid only)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (differs only by Review/lifecycle coordination text; checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98
    REVIEW METHOD: D3 role entered at the governing public source; immutable-owner reconstruction;
           whole-Manual read at the exact candidate; deductive counterexamples in both polarities;
           family-level search after recurrence (convergence owner); prior-finding regression;
           required structural checks; one byte-level Git toolchain diagnostic; no implementation
           or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

All Manual section and line references are to the exact candidate, read from a `git archive` snapshot. The checkout HEAD was the later handoff commit `28769ae4`, clean, on the requested branch. `PROTOCOL-RELEASE-STATE.yaml` independently gave accepted-current 7.2.1 with the public-source and recovery identities above. Governing owners were read with `git show aaeaf8b…:<path>`: `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract, scientific checks), then `architecture-and-design.md`, `abstraction-and-concretization.md`, `convergence-and-cycle-economy.md`, and the cited parts of `evidence-evolution-and-dependencies.md` and `workflow-and-workplans.md`. Governing SSDP version for this task: 7.2.1.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** The blocker below is a defect of the proposed D3 concretization. The Phase B workplan is still proposed architecture, so a gap between it and the Manual is not a challenge to accepted authority.

The baseline owner text this Review applies, unchanged: the D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed … reliability … constraint"; the kernel, "Verification and Challenge": a child can "perfectly satisfy a too-weak abstraction and still be wrong"; the evidence owner, "Applicability, immutable observation, and superseding assessment": "A stale passing observation is not admissible confirmation" and "PASS/accepted/closed cannot depend on stale, rejected, unavailable-required or otherwise inadmissible evidence."

## Verdict

**NO-PASS.** One D3 blocker survives, stated at family level as the method requires:

- **B1 (content-identity family, second round).** The repaired content identity is exact over Git blob bytes plus entry type and mode, but the Manual never fixes that this is the representation its consumers use or compare. A designated runner may execute on a checkout whose bytes differ from the blobs (Git attributes), so a tree-resident change can alter what the execution read while the recorded basis still matches. Sibling defects: anchor-looking data lines are still normalized away, and the effect-keyed write set compares bytes only, so it misses a mode or type change that now changes a D1-D3 revision.

The SD-23 (`ext` over the complete external-input record) and SD-24 (`QUALIFIED` gate capped at `P`, `INADEQUATE` refused) repairs close the 3540d98 B2 and B3 trajectories. The equal-region repair closes the 3540d98 B4 trajectory. The binary-byte, regular-to-link and executable-bit cases of 3540d98 B1 are closed. The D1-D3 change rule has no new finding of its own; B1's third sibling touches its write-set input. This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Content identity is not bound to the representation its consumers read and compare

**Earliest owner.** Manual §1.5, the single content-identity owner, together with three consumers that do not use the representation §1.5 hashes:
- the execution-recording and runner contract (§6.3 read and unit entries, §17.5 runner classes);
- the effect-keyed write set and the diff-to-unit mapping (§1.2, §14.5);
- the anchor-normalization domain (§1.2, §1.5).

Workplan §21 items 1 ("content normalization and boundary-marker rules"), 4 ("the mechanical computation of each realization's executed content … observed runner reads"), 11 ("trusted-runner designation and custody") and 23 (the effect write set; SD-14). This is a D3 representation defect; it asks no new D1/D2 rule.

**Owner and contract text.**
- Evidence owner (quoted above): a stale passing observation is not admissible confirmation, and closure cannot depend on stale evidence.
- Workplan §6.6, the reviewed contract: executed content is "everything the realization's execution read, recorded at realization by content identity", and "missing dependency knowledge never proves that two executions read the same content". Workplan §6.1 restricts content identity to "rule-defined **conservative** normalizations; pure structural boundary markers … are normalized out".
- SD-14 (verbatim record): "every unit whose **owned content**, declarations, regions, membership or signature … differs".
- The Manual's own claims: §1.5, "Content identity is exact"; §17.4, "Stale passing evidence never discharges"; §13.2, "no change to a D1-D3 unit's owned content … by whatever route … can happen except through an `AUTHOR` item"; and the E0 claims of §29.4/§29.5 resting on that rule.

**Trajectory A — a checkout transform hides an input change. Primary; blocker-grade on its own.**

1. The tracked file `data/table.csv` (`a,b\n1,2\n`) is read by the solver of specification `S`. `S` declares `EXECUTION_DEPENDS_ON` its solver unit, a current `COMPLETENESS(EXEC)` bounds the closure, and the runner class observes reads completely. A Dispatcher-controlled designated runner materializes the commit with standard Git checkout. It reads `data/table.csv`, and the read entry records `({path = "data/table.csv"}, cid)` over the **blob** (§6.3, line 846). Realization `q` passes and is assessed. `valid(s) = T`.
2. An admitted change adds `.gitattributes` with `*.csv text eol=crlf`. It changes no byte of `data/table.csv`'s blob. `.gitattributes` is governed content of some other unit, outside `q`'s recorded basis: no read entry names it, since the execution never reads it, and the bounded closure records no widened entry covering it.
3. A checkout of the new tree now presents `a,b\r\n1,2\r\n` to the solver. A parser that keeps `\r` in the last field reads different values. This review's scratch diagnostic confirmed the toolchain fact: the blob id was unchanged across the two commits (`cfa20f81…`), and the cloned working file contained `\r\n`. That shows Git checkout behavior, not SSDS behavior.
4. In `q`'s record, every unit, read and widened entry re-resolves to its recorded identity, so `sat(execution) = T` (§4.1), `q` stays current, and no `REALIZE` is derived (§10.2: only "without a current admissible realization"). `valid(s)` stays `T` on evidence the execution would no longer reproduce. The same path is open through `working-tree-encoding`, clean/smudge `filter` attributes, and an external-custody CI runner whose checkout honors attributes or `core.autocrlf`. Note that realization currency never reads attribute entries.

Nothing in the Manual forbids the runner from honoring attributes. §17.5 says only "on the exact candidate or merged tree", which fixes the commit, not the materialization. By contrast, §7.2 states "Repository attributes, custom merge drivers and rerere never apply" for the frame merge. The author excluded attributes there but not at execution.

**Trajectory B — an anchor-looking data line is normalized away. Sibling, disclosed but not decided.** A Python test oracle holds the string `EXPECTED = """\n# ssds:begin alpha\nx = 1\n# ssds:end alpha\n"""`, the expected output of a code generator. That is realistic for any tool emitting SSDS anchors, including SSDS's own repository. Changing the line to `# ssds:begin beta` changes the test's behavior. §1.5 removes both lines from identity ("treated as an anchor line wherever it stands, including inside a string literal or a shell heredoc"), so `cid`, `content` and `rev` are unchanged and the old passing realization stays current. The same holds for an anchor example inside a fenced code block of a D1-D3 Markdown document: edits there leave `rev` and acceptance current. This is not a "pure structural boundary marker" and not a conservative normalization in the workplan's sense. §32.2 discloses it as a residual, but it is neither listed as a refinement in §0.3 nor stakeholder-decided. The 3540d98 Review named it a sibling needing a "semantic-domain boundary".

**Trajectory C — the write set no longer covers what content identity covers. Sibling, entered through the B1 repair.**

1. An `IMPLEMENT` item with write scope `src/` produces a candidate that also sets mode `100755` on `docs/method.md`, which holds a `NATIVE` D2 subject declared by `heading` terms.
2. In the §1.2 write set, owned bytes, declaration keys, resolved regions, membership and signature are all unchanged, so the D2 subject is not in it. The diff-to-unit mapping maps "changed byte ranges" only (§14.5). `BOUNDARY.write_scope` and the §13.2 domain rule pass.
3. After integration, every `cid` of that file changes, because §1.5 hashes "entry type and mode of the file". So `rev` of the D2 subject changes, a new revision run starts, its acceptance and gate stop being current, and every descendant loses validity.

The target-keyed revising duty still applies, so no acceptance escapes assessment. What fails is the §13.2 guarantee and the E0 claims of §29.4/§29.5 that a non-`AUTHOR` agent item cannot change what a D1-D3 unit owns. A regular file replaced by a link with byte-identical content under a `path` term is the same case. A conforming implementation following §1.2 literally admits it.

**Precision siblings, found in the same search.**
- (iv) Removing the CRLF normalization leaves undefined whether a line ending `\r\n` is recognized as an anchor (`ssds:begin name\r`) or as a heading. The answer decides both resolution and which bytes §1.5 removes, so it bears on whether adding anchors to a CRLF file is the byte-preserving refinement §19.3 relies on.
- (v) The "bytes" of a gitlink entry, which §1.5 lists as an entry type, are undefined.

**Family assessment (convergence owner, "Review strategy after recurrence").** This is the content-identity family's second round, after 3540d98 B1. The shared cause: §1.5 defines one encoding, but the Manual nowhere states that this encoding *is* the representation each consumer is about, namely
- what an execution read (A);
- what an authority means (B);
- what an agent changed (C).

So each consumer silently uses a different representation. It is not the §6 matching clause, which reads the recorded identities faithfully. Sibling C entered through the previous repair, as the handoff warned. Further sibling search, such as enumerating every Git attribute or filesystem layer, would become implementation-like. The siblings above characterize the cause.

**Minimum repair direction (subtractive or narrowing; no new primitive, record kind or registry).**
1. State once, at §1.5, that the identity's representation is the Git tree entry (type, mode, blob bytes). Require every designated runner, Dispatcher-controlled or external custody, to present exactly that representation to the execution: no eol or encoding conversion, no clean/smudge or `ident` filter, no sparse or skip-worktree divergence. This mirrors §7.2. A runner class that cannot guarantee it is treated like a class that cannot observe its reads, failing closed.
2. Make every consumer that compares "owned content" compare the same representation. The write set and the diff-to-unit mapping must include a type or mode change. Equivalently, define the owned content of §1.2 as §1.5's.
3. Admit anchor-line removal only where the pinned pure resolver classifies the line as a comment and not as data (Python tokens, Markdown outside fenced code). Remove file types where that cannot be decided from the table. Define CRLF recognition, and define gitlink identity.

Alternatives the stakeholder may prefer:
- Record attribute files and checkout configuration as read entries (adds recorded state).
- Drop anchor normalization and cover anchor-only refinements by an `EDITORIAL` `EQUIVALENCE` judgment (each such refinement then costs a judgment).

**Required discriminator.** At the real Content Model → Dispatcher/runner → realization currency → discharge owners:
- (A) Absorb a `.gitattributes` `eol`/`working-tree-encoding` change with the read blob unchanged. The passing realization must stop being current, or the runner must provably have read blob bytes. A runner honoring attributes must fail the case.
- (B) An anchor-syntax line inside a Python string and inside a Markdown fenced block changes `cid`, while a genuine comment anchor still leaves `rev` unchanged.
- (C) An `IMPLEMENT` item changing only the mode of a D2 file is a `VIOLATION`.
- (iv) CRLF and LF files give the same refinement result.

The existing §31.2 "Exact identity" cases do not discriminate any of these.

## 2. Non-blocking findings

- **N1 — Partition rule 3 needs an evaluation order (partition family, precision).** §1.4 rule 3 makes regions "resolve to `ABSENT`" by comparing them with other units' regions, and also when "a member region … falls outside its composite's resolved region". It does not say whether the pairwise partial-overlap and equality tests read the §1.3 term resolutions in one pass, or regions already set to `ABSENT`, or whether a member under an `ABSENT` composite cascades.
  - Under a cascade-first reading: composite `A` (`symbol mod.K`) partially overlaps sibling anchor `b`, so `A` is `ABSENT`, then its member `m` (`symbol mod.K.f`) is `ABSENT`. A top-level anchor `c` whose region equals `m`'s raw region keeps its bytes.
  - Under the single-pass reading: `m` and `c` are equal, so both are `ABSENT`.
  - A purely post-state reading has no fixed point for two equal regions.

  The single-pass reading is the most literal and coherent, so this is not a blocker. Still, `cid(c)` and byte ownership differ by reading. State "single pass over §1.3 resolutions; no cascade" (or the cascade rule), and add the case to §31.2. The same mixed semantics existed for partial overlap before this candidate.
- **N2 — SD-24 ordering and liveness.**
  - (a) `valid` takes the maximum over current gate `ACCEPT`s, so an earlier current `UNQUALIFIED ACCEPT` dominates a later `QUALIFIED` one. §5.5's prose "the cap lifts only through a later `UNQUALIFIED` `ACCEPT`" suggests a latest-wins reading. State that a holder who comes to qualify supersedes their own earlier acceptance (R8 own-author reassessment), or define the order.
  - (b) Once a `QUALIFIED ACCEPT` is current, the `GATE(g)` trigger ("without a current `ACCEPT`") is false. No gate obligation or inspector entry then prompts the lifting decision. Where policy does not permit provisional continuation, the item obligations stay `OPEN` with no derived action. The lift itself is realizable: `decide` records directly, so §8.3 step 7's `OBLIGATION_ANSWERED` (which refuses judgments "bound to" the obligation) does not refuse it.
  - (c) "lets work continue" holds only where policy permits provisional continuation (§10.3, §10.4); say so.
- **N3 — Surfacing and accounting of this round's changes.**
  - SD-24 narrows the reviewed discharge clause (workplan §7.4: "every human gate of o is discharged by a current authenticated human judgment"). It is stakeholder-directed and stated in §0.3's history paragraph, §5.5 and §10.4, but it is not a refinement row. Add R11 with the property it preserves.
  - The R5 row omits the equal-region case.
  - §30's account omits the added entry type and mode and the equal-region rule.
  - Closure-map item 7 still says "three-valued discharge" and omits `unq`.

  The aid confers no authority.
- **N4 — SD-23's restrictive cost and a precision edge.** Requiring the same complete external-input set under a class that observes every read outside the tree means incidental reads break (1) and (3):
  - user caches (font and JIT caches) present in one run and not another;
  - host configuration files;
  - `/proc` files.

  A legitimate fix that changes which external file is read also never stops mechanically. That is the stakeholder's chosen fail-closed direction (SD-23 text), but §17.5 and §32.3 should name it as a cost and reopen trigger. Runner-class guidance (classify host files as environment components; hermetic home directories) would bound it. Precision: "the same set of external locators, each with the same pin" is ambiguous when one execution reads one locator under two pins. Compare the multiset of `(locator, pin)` pairs.
- **N5 — Exactness has a permissive side and a cost, both undisclosed (both-direction attack).**
  - On the permissive side, a differing run on a tree that differs from `tree(a⁻)` only by line endings that a text-mode reader translates, or by the mode of a non-executed data file, is no longer `on⁻` `tree(a⁻)`. It leaves (2), and a yielding run on such a variant of `G` leaves (4). This follows from the reviewed single identity for both polarities and is bounded, so it is not a blocker. §6.6 or §32.2 should state it next to the "outside the recorded regions" statement.
  - On the cost side, a line-ending or mode churn on a D1/D2 subject now starts a new revision run needing a revising review and a human gate. Only the closure map says this; §32.3 should.

## 3. Closure audit

I located each workplan §21 item and clause in the Manual directly and used the closure map only as an index. "Answered" means a substantive D3 answer exists; it is not runtime qualification or stakeholder acceptance.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11: manifest and anchor syntax, normalization, scope identity, partition, single definer, fold, keys, `ABSENT`/uncovered, classification, `aff`, signature and tenure | **Not substantively closed (B1 B, iv, v)**; N1 precision |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 6.8, 17.1; gate `adequacy`/`qualification` semantics now in §3.4/§5.5 | Answered (3540d98 B3 closed); N2 |
| 4 | §§4.1-4.6, 6.3 | **Not substantively closed (B1 A)**: the recorded read identity is not the read content under attribute-honoring materialization |
| 5 | §§5-7, 17, 22.3 | Answered; inputs carry B1; N1, N5 |
| 6 | §§8, 21-23 | Answered |
| 7 | §10 (four-valued discharge surfaced in R9; `unq`) | Answered; N2 |
| 8 | §11, §13.2 ref locality, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered; N2(b) |
| 11 | §§17, 6.10 | **Not substantively closed (B1 A)**: runner designation lacks a materialization contract |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered (3540d98 N1 prospective run now defined in §10.2) |
| 14 | §§21-25 | Answered; runtime unexecuted |
| 15, 16 | §25.1-§25.3 | Answered |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered |
| 20 | §20 | Answered |
| 21 | §29.7 | Answered |
| 22 | §30 | Present; N3 accounting; B1 qualifies its adequacy conclusion |
| 23 | §12, §1.2/§13.2 write set | **Partly open (B1 C)**: the write set no longer covers what content identity covers |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; the §29.4/§29.5 E0 claims for the domain rule need B1 C |

**Workplan §16.2, both tables.** All 26 product-invariant rows and every frozen-surface row (§3-§22, including §4 layout/namespace and §14 CLI) have final dispositions in Manual §26.4. I read them against the rows. No row is merely routed, and nothing changed in §26 since 3540d98.

**Material decisions versus delegated D4.** The Manual marks file-type-table extension, diff implementation, checkpoint encoding, parsers and limit values as `[delegated]`. Checkout materialization is not delegated anywhere; it is simply unstated. That is the architectural gap of B1 A, since it decides what the recorded identity means.

## 4. Refinements R1-R10

| # | Assessment |
|---|---|
| R1 | **Sound as a matching construction**: the SD-23 formula now agrees with the class rule (same complete locator set and pins; no unpinnable read; every recorded attribute); `on⁺ ⇒ on⁻` holds by construction; one record serves currency, matching, floor and class. **Its input identity has B1** (the record does not denote what the execution read under attribute-honoring materialization), and N4/N5 should be disclosed. |
| R2 | Sound: SCC clamp to `F` before presentation; unchanged. |
| R3 | Sound: authenticated syntactic corruption halts current assertions; unchanged. |
| R4 | Sound within its declared crash model; VM snapshot/ABA residuals disclosed; unchanged. |
| R5 | **Sound for the equal-region trajectory** (both `ABSENT`, integrity finding, member-equals-composite stays the member's). N1 precision on evaluation order; row text should mention equality (N3). |
| R6 | Sound as scope identity; byte-preserving refinement keeps `scope_id`/`rev`, subject to B1 (iv) for CRLF files. |
| R7 | Sound: authored `CHALLENGES` excluded from warrant, validity and cycle legality. |
| R8 | Sound; it also supplies the supersession route N2(a) needs. |
| R9 | Sound; the answered-obligation rule does not block the SD-24 lift because `decide` is a direct human record; liveness gap in N2(b). |
| R10 | Sound for the named run/tenure cases; 3540d98 N1's prospective-run precision is now supplied in §10.2. B1 C can start runs from a mode change by a non-`AUTHOR` item. |
| SD-24 (unlisted) | A sound narrowing toward the workflow owner's Channel C rule ("The gate does not close unqualified when missing realized records could plausibly change its judgment") and S2; needs an R-row (N3). |

## 5. Previous findings and Phase B closures

"Closed" means the named trajectory is excluded by the present text, independently re-derived; it is not runtime evidence. Prior records were read as hypotheses only.

### 3540D98 (different family)

| ID | Disposition and basis |
|---|---|
| B1 | **Partly closed.** Binary `0d`→`0a`, executable bit and regular→link with the same bytes now change `cid` (§1.5: exact bytes plus entry type and mode). The family is open as B1 here (materialization, data anchors, write set). |
| B2 | Closed: `ext` requires the same complete locator set with the same pins (§6.5 line 900; construction rule); disjoint, subset, superset and alias variants fail `ext`; (2)/(4) still use `on⁻` without pins (§6.6). |
| B3 | Closed: `ACCEPT` requires `ADEQUATE` (§3.4, §16.6); `unq(h) = P` for `QUALIFIED` enters `valid` and discharge (§5.5 line 732, §10.4 line 1216); `P` propagates by min. Residue N2. |
| B4 | Closed: equal regions of units not related by membership both resolve to `ABSENT` with an integrity finding (§1.4 rule 3). Residue N1. |
| N1 | Closed: §10.2 defines the frame's prospective run (unchanged `cur`, integration-started run, rebases and iterations, requested cutover). |
| N2 | Closed as disclosure (§32.2: later `ABSENT` raises no specific finding). |
| N3 | Closed for items 4 and 10 (recompiled); new aid residue in item 7 (N3 here). |
| N4 | Held: adoption-transcript gap, unrecorded variation, rewrite/quarantine limits, VM/ABA, costs and witness availability stay disclosed (§32.2-§32.4). |

### 798B2B4

| ID | Disposition and basis |
|---|---|
| B1 | Closed: never-integrated frame acceptances are in no admitted run; predecessor is a display computed from admitted-state acceptances before the run (§10.2). |
| B2 | Closed: run membership is a target condition (`tgt`, §5.2) read by `base`, `valid`, `ACC`, the `ACCEPT`/`GATE` triggers and discharge (§10.2 "Currency"). |
| B3 | Closed: predecessor display includes declared lineage and prior byte owners and the reviser may extend it; no equality conditions counting (§10.2). |
| B4 | Closed for link retargeting (§6.3 records every traversed link and the target). Regular→link with the same bytes is now closed by §1.5. The family residue is B1 here. |
| N1 | Closed: R10/S11 and §10.2 say "`NATIVE` subject of kind D1 or D2", excluding `EVIDENCE_SPEC`/`GENERATED`. |
| N2 | Closed: the acceptance carries a `record` entry on the revision-assessment record, so an override's `P` propagates (§10.2, §4.3). |
| N3 | Closed: per-subject predecessor map in the envelope, display only (§12.2). |
| N4 | Closed: `REVIEW(s, r)` derived for a requested cutover by a `MIGRATE` item or the cutover gate's derivation (§10.2, §19.5). |
| N5 | Closed as disclosure: misspelled prefixes (§1.9) and later `ABSENT` (§32.2). |
| N6 | Closed: the revision-condition `holds` is gone; only §23.7 `holds` remains. |
| N7 | Closed as document coverage: §31.5 frames/reverts/tenure starts; §31.3 links. |
| N8 | Partly closed: aid recompiled; residue in N3 here. |

### 71CF9B3

| ID | Disposition and basis |
|---|---|
| B1 | Closed: the run starts at any position where `cur(s)` took its value, tenure starts included (scope, kind, replacement, re-cutover); no route list (§10.2). |
| B2 | Closed: an old in-tenure D1/D2 acceptance fails `tgt` after a revision change; S11/R10 restored (§0.3, §0.4). |
| N1 | Closed: predecessor is display; the run key, not a recurring value, controls currency. |
| N2 | Closed: only a counting record answers `REVIEW(s, r)`; obligations carry `run(s)`. |
| N3 | Closed: §12.2 map, §13.5 slot, §16.6 section 3, §30 account. |
| N4 | Closed: §19.5 condition 3 binds the cutover acceptance; §10.2 gives its prospective run. |
| N5 | Closed: §6.10, §17.5 and §31.3 agree on supplied versus runner-external randomness. |
| N6 | Closed: link recording (§6.3); identity of the recorded entries is B1 here. |
| N7 | Closed as disclosure: empty file, prefix exemption, realignment, `ABSENT` analyzer bar (§1.9, §2.6); later absence disclosed (§32.2). |
| N8 | Partly closed: aid residue N3 here. |

### 86AB683

| ID | Disposition and basis |
|---|---|
| B1 | Closed: a record counts only in the run, with `status1 ∉ {REVOKED, BLOCKED}` and `cont`; the acceptance's `record` premise carries later revocation/withholding (§10.2). |
| N1 | Closed: cutover binding and prospective run (§19.5, §10.2). |
| N2 | Closed: supplied versus unsupplied randomness disclosed consistently (§6.10, §31.3). |
| N3 | Closed: unpinnability, attribute set and observation flag recorded by value at realization (§6.3). |
| N4 | Closed as disclosure (§1.9, §2.6, §32.2). |
| N5 | Closed: `ignore`-key quarantine paths defined by changed governed status (§18.4). |
| N6 | Closed: one slot entry per revised subject; §16.6 renders every counting record. |
| N7 | Partly closed: aid residue N3 here. |

### 1FFBBF0

| ID | Disposition and basis |
|---|---|
| B1 | Closed: free seed is a recorded attribute compared by `ext`; a non-observing class records an unpinnable read (§6.3, §6.5, §17.5). |
| B2 | Closed: Admission refuses a passing D1/D2 acceptance or gate `ACCEPT` without a counting record for exactly `(s, r)`, in every frame, human submissions included (§8.3 step 7). |
| N1 | Closed: newly declared file/span terms must resolve at admission; pure resolver; `ABSENT` bars analyzer completeness (§1.9, §2.6). |
| N2 | Closed: write set by owned bytes and declarations; nested-only revision stated (§1.2, §16.6). B1 C is a new, different gap (mode/type). |
| N3 | Closed: predecessor display for `AUTHOR` and revising review alike (§10.2, §13.5). |
| N4 | Closed: structural-delta `QUARANTINE` paths defined (§18.4). |
| N5 | Closed as disclosure (§17.5 declared-set changes). |
| N6 | Closed: environment-component files excluded from external reads (§20.1). |
| N7 | Partly closed: aid residue N3 here. |

### 53669A5

| ID | Disposition and basis |
|---|---|
| B1 | Closed: the class rule compares every recorded attribute (§6.5). |
| B2 | Closed: direct human acceptance/gate before a counting record is refused at Admission (§8.3 step 7). |
| B3 | Closed: the intake target rule concerns targets, not timing; contrary dispositions after adoption admissible; `ABSORB` refused against a standing adverse disposition (§18.4). |
| N1 | Closed by SD-17's withdrawal; red-then-green stops through matching attributes (§31.3). |
| N2 | Closed: scope "`NATIVE` kind D1/D2", nested-only gate statement (§10.2, §16.6). |
| N3 | Closed: §31.5 puts `ssds.manifest` in the `AUTHOR` scope. |
| N4 | Closed: cross-domain structural route is human or adoption (§13.2). |
| N5 | Closed: resolver purity versus later `ABSENT` (§1.9). |
| N6 | Closed within path scope; moved-out content disclosed (§18.4, §32.2). |
| N7 | Closed: declaration-key conflicts (§7.2). |
| N8 | Closed for the named statements; new §30 omissions are N3 here. |
| N9 | Partly closed: aid residue N3 here. |

### D837363

| ID | Disposition and basis |
|---|---|
| B1 | Closed: free environment values are attributes, compared only permissively (§6.5, §17.1). |
| B2 | Closed: pure byte resolvers; resolution context recorded by value at execution start, never from the envelope (§1.3, §6.3). |
| B3 | Closed: target-keyed revising record before any passing D1/D2 acceptance (§8.3 step 7, §10.2). |
| B4 | Closed: write set compares `T_n` under `Σ_n` with `M_n(X)` under `Σ_n ⊕ Δ_Σ(X)` over every declaration key (§1.2). Its bytes-only content criterion is B1 C here. |
| N1 | Closed: nested different-kind revision does not put the parent in the write set; gate core says so. |
| N2 | Closed: cross-kind route (§13.2). |
| N3 | Closed: `QUARANTINE` effect via `ok` and intake constraints (§18.4, §5.5). |
| N4 | Closed as disclosure: re-identification ends reading coverage; adoption gate shown (§27.3). |
| N5 | Closed: `ssds.manifest` always in the write set when its bytes change. |
| N6 | Closed. |
| N7 | Closed: `OPEN`/`RESOLVED` in `findings`; predecessor in `revision_assessments` (§13.5). |
| N8 | Partly closed: aid residue N3 here. |

### CC005DB

| ID | Disposition and basis |
|---|---|
| B1 | Closed for governed-boundary and new-part routes (effect write set, §1.2). The mode/type route is new, B1 C. |
| B2 | Closed: system version in the recorded resolution context (§6.3). |
| B3 | Closed: product-scope acceptance is its own record kind; surface veto does not touch the gate's decision (§3.5, §5.5). |
| N1 | Closed: tracked ignored files are read entries; absent-from-tree files external (§4.2, §6.3, §20.1). |
| N2 | **Partly closed.** The environment/external/output boundary is stated (§6.3, §20.1). SD-23's complete-set equality raises the incidental-read cost it named (N4 here). |
| N3 | Closed: pure resolvers, no permissive frozen-analyzer fallback; host lacking a set asserts nothing (§5.9, §6.3). |
| N4 | Closed for recorded terms (term-level, §6.3); unit-level evaluation order is N1 here. |
| N5 | Closed: contrary-order mechanics (§18.4). |
| N6 | Closed as explicit re-review policy (§16.5). |
| N7 | Closed as disclosure (§27.3). |
| N8 | Partly closed: aid residue N3 here. |

### C6DA678

| ID | Disposition and basis |
|---|---|
| B1 | Closed: pins and unpinnable reads never narrow `on⁻`, (2), (4) or `adm` (§6.5, §6.8). |
| B2 | Closed: `same` for reviews spans item revisions at identical changed content (§5.5). |
| B3 | Closed: effect write set attributes manifest effects to the affected units (§1.2, §13.2). |
| N1 | Closed: `stands⁻` requires the chain's last record to stand (§5.5). |
| N2 | Closed: intake dispositions have adverse outcomes; intake answered (§5.5, §10.3). |
| N3 | Closed as disclosure: agent own-author reassessment unavailable (§5.5, §8.3). |
| N4 | Closed: `COMPLETENESS` sameness includes member revisions (§5.5). |
| N5 | Closed: `REFUSED` surfaced in R9 (§10.4). |
| N6 | Closed: pure resolvers (§1.3, §14.5). |
| N7 | Closed for classification (§6.3, §20.1); the identity of the entries is B1 here. |
| N8 | Closed: residual-part identity defined (§6.3). |
| N9 | Closed: empty prefix uses distinguished (§1.3, §1.8). |
| N10 | Closed as bounded re-review policy (§16.5). |
| N11 | Closed: `ref` resolution confined to the item part and `Objective` (§13.2). |
| N12 | Partly closed: §30 residue N3 here. |

### B595F2C

| ID | Disposition and basis |
|---|---|
| B1 | Closed: unit/term granularity; changes outside recorded regions leave both predicates (§6.3, §6.6). |
| B2 | Closed: ref locality plus byte-identical prose for tightening (§13.2, §13.4). |
| B3 | Closed for `DOCUMENT` (§13.2); B1 C is a different, mode-based route. |
| B4 | Closed: answered once, never re-dispatched; symmetric veto; every task ends in one `TASK_RESULT` (§8.3 step 7, §10.3, §5.5). |
| N1 | Closed: machinery R0 `COMPLETENESS` producer (§2.6, §3.4). |
| N2 | Closed: host-dependent output recorded as `ANALYZER_OUTPUT`; scope resolvers pure (§5.9, §14.5). |
| N3 | Closed: analyzer set in `RULESET_ADOPTION` and §27.1. |
| N4 | Closed: complete external pin record compared permissively (SD-23, §6.5). |
| N5 | Closed: single-provisional check in qualification (§5.7, §23.4). |
| N6 | Closed: `TEST_INTEGRITY`/`BOUNDARY` on any item touching `D4`/`EVIDENCE_SPEC` (§13.3). |
| N7 | Closed for the named statements (§30); residue N3 here. |
| N8 | Closed: `AUTHOR` scope defined (§13.2). |

### 6FF4ED1

| ID | Disposition and basis |
|---|---|
| B1 | Closed: `on⁺ ⇒ on⁻` by construction; frozen resolution context (§6.3, §6.5). |
| B2 | Closed: any prose change is R2 (§13.4). |
| B3 | Closed: analyzer set pinned by `ρ_n`; missing set asserts nothing (§5.9). |
| B4 | Closed: `AUTHOR`/`DOCUMENT` obligations, holder, contracts and slots (§10.2, §12.3, §13). |
| N1 | Closed: not-computable yields only on evaluated outputs; "either" clause separate (§6.5, §6.6). |
| N2 | Closed: supersession authority by kind (§8.3 step 3, R8). |
| N3 | Closed: schema field present and, now, propagated (SD-24). |
| N4 | Closed: no new or grown SCC; absorbed cycles reported (§8.3 step 5). |
| N5 | Closed: analyzer completeness only as challengeable `COMPLETENESS` (§2.6). |
| N6 | Closed: `CHALLENGES` excluded (§2.3-§2.5). |
| N7 | Closed: static checks plus dynamic `ABSENT` for crossing and equal regions (§1.4); N1 precision. |
| N8 | Closed: single-provisional in qualification. |
| N9 | Closed: map rows present (§29.3). |
| N10 | Closed: §26.4 dispositions for 1.6.0 §4 and §14. |
| N11 | Closed: export within deliverable (§0.5). |
| N12 | Closed for the named annotations. |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| Y1 identical-outcome coverage | Held (§6.5 coverage; §6.6 "Standing per frame"). |
| Y2 candidate-own not re-escalated | Held (§6.8 class). |
| EF8445A/552AC01 N2 strata, completeness polarity, class basis | **Re-tested** with an alternate tree differing only outside a recorded narrow basis: a differing old-content run stays in (2) and a yielding present-content run stays in (4) under completeness `P`, blocked, revoked or loss-withheld, because both use `on⁻`, which reads no completeness and no pins (§6.5-§6.6); losing completeness only narrows (1)/(3). Held. B1 A limits what the recorded identity denotes, not this polarity. |
| Absorbed assessor-read relaxation | Held (§6.5 coverage; §6.6 mechanical "yields"). |
| Identical-outcome floor / reader disagreement | Held (§6.5 refusal; §6.8 floor). |
| Material difference, X1-X3, later PASS | Held (§6.5 discriminating reading; §6.7). |
| Promotion/refinement/enactment | Held (§7.6, §19.4). B1 (iv) affects refinement in CRLF files. |
| Adversity vs currency/challenge/loss | Held (§5.4, §6.7). |
| Salvage, retirement, unauthorized supersession | Held (§8.3 steps 3 and 6, §10.2). |
| Scope anchors, home, independence | Held (§6.4, §6.8). |
| Start latch | Held (§6.4). |
| U1/U2/W1/W2 executed content and reading | Held for recorded reads; B1 A shows the recorded read identity may not be the read content. |
| Contrary-run retention, nondeterminism | Held (§6.6 (2)/(4)); N5 notes the exactness narrowing. |
| Warrant/S1/S2 cycles, fail-closed support cycles | Held: §5.6 clamps every non-trivial SCC to `F` before presentation. |
| Corrupt prefixes | Held: §5.7 `INTEGRITY_HALT`. |
| Effective structure, quarantine, tenure | Held (§1.6, §8.3 step 4, §19.4). |
| Phase B N1 adoption provenance | Disclosed (§32.2, §32.4). |
| Phase B N2 positive-only completeness | Held, as re-tested above; §31.3 carries the real-owner cases. |
| Phase B N3 diagnostic bounds | Held (§31.3 "Diagnostic model"). |
| Phase B N4 cost and applicability | Held as reopen triggers (§32.3); N4/N5 add two costs to disclose. |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | `.gitattributes` `eol`/encoding change with read blob unchanged; standard or CI checkout | **Violation (B1 A)** |
| 2 | Anchor-syntax line inside a Python string or Markdown fenced block edited | **Violation (B1 B)**, disclosed but undecided |
| 3 | `IMPLEMENT` item changes only a D2 file's mode (or regular→same-byte link under a `path` term) | **Violation of §13.2/E0 claim (B1 C)**; revising duty still applies |
| 4 | Anchor or heading recognition in CRLF files; gitlink identity | Underspecified (B1 iv, v) |
| 5 | 3540d98 B1 cases: `0d`→`0a`, executable bit, regular→link same bytes | Held: identity changes |
| 6 | 3540d98 B2: disjoint, subset, superset, alias, missing external locators | Held: `ext` false; (2)/(4) unaffected |
| 7 | SD-23 restrictive: fix changing the external read set; incidental host/cache reads | Fails closed; cost undisclosed (N4) |
| 8 | 3540d98 B3: material missing record outside required evidence, `QUALIFIED ACCEPT` | Held: `valid = P`, descendants `P`, discharge provisional or `OPEN`; `INADEQUATE ACCEPT` refused |
| 9 | Earlier `UNQUALIFIED`, later `QUALIFIED` gate acceptance | Formula keeps `T` unless superseded (N2a) |
| 10 | Lifting the cap after `GATE(g)` was answered | Admissible through direct `decide`; no derived prompt (N2b) |
| 11 | Lifecycle human gates (cutover, `RULESET_ADOPTION`, `LEDGER_LOSS`) and `QUALIFIED` | Held: they are lifecycle enactments, not `GATE_DECISION`s; native D1/D2 validity still passes through `GATE_DECISION` and `unq` |
| 12 | `unq` under loss boundary, veto, risk override | Held: `base` dominates; `unq` is an S0 constant, stratification unchanged |
| 13 | 3540d98 B4: sibling `symbol`/`anchor` regions made equal by an absorbed edit | Held: both `ABSENT`, finding, order-independent |
| 14 | Equal regions combined with a partially overlapping composite | Reading-dependent result (N1) |
| 15 | A new declaration whose region equals an existing unit's | Held: §1.9 resolution check refuses it |
| 16 | D1/D2 revert, rule-3 `ABSENT` flip and back, CRLF round trip | Held: each value change starts a new run; nothing revives |
| 17 | Frame whose change to `s` equals a concurrent integration's | Held, conservatively: frame records predate the new run and do not count |
| 18 | Consumer-equivalent byte variant differing run in (2)/(4) | Permissive narrowing, bounded (N5) |
| 19 | Phase B N2 completeness polarity with `P`/blocked/revoked/loss-withheld judgment | Held (§5 table) |
| 20 | Support cycle through absorbed `about` or completeness edge; corrupt authenticated prefix | Held (§5.6, §5.7) |

## 7. Minimum architecture and capability transfer

No primitive, component, persistent surface or record tier is added. SD-24 reuses `P` and the existing provisional-continuation rules. SD-23 changes one conjunct. The equal-region rule reuses `ABSENT` and the integrity finding. The line-ending normalization is removed, which is a subtraction. B1's minimum repair adds contract statements, not mechanism. The §30 table remains the minimum justified set within this review's evidence, subject to B1 and N3.

Capability transfer: the §26.4 tables are unchanged since 3540d98 and were re-read against workplan §16.2 and §18. Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS (§26.2-§26.3).

PEM was activated because this is mature-machinery replacement. Accepted/base memory `PROJECT-ENGINEERING-MEMORY.md` is byte-identical between `main` and the candidate, and its repository tests pass. The HAS dispositions in workplan §0.3 are realized:
- PC-001: §26.3/§26.4/§28/§31.8;
- SP-002: G3 and §21.2;
- FF-001: §19.9 genesis procedure, §24.2;
- DS-001: §31.1;
- SP-001: §5.8 regenerated views.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`; nothing is claimed as executed. The new cases are useful and name negative discriminators: §31.2 equal regions and exact identity, §31.3 complete external-input record, §31.6 qualified gates.

Green fixtures could coexist with the following defects:
- B1 A: no case varies materialization, and the "Exact identity" case changes only blobs, so an attribute-honoring runner passes every listed case.
- B1 B: no data-line anchor case.
- B1 C: no mode-only write-set case.
- N1: no case combines equality with a partially overlapping composite.
- N2: no earlier-unqualified or lift-liveness case.

The diagnostic model (default mode, green) does not model these clauses, as §31.3 states (DS-001).

## 9. Doctrine-realization map and O1

The §29 map is unchanged. I re-checked §29.4 row by row against the expanded 7.2.1 scientific checks: delegate questions, gaps, findings, realized results, variants, tensions, choices, retention, claims, before loss, resources, persistence, persisting tensions, inaccessible homes, product changes, authority content and the revising-duty row. §29.2-§29.3 cover the entry contract and role contracts, and §29.6 lists the disclosed E3 duties.

One correction is owed: the E0 claims that an agent "can change what a D1-D3 unit itself owns only through an `AUTHOR` item" (§29.4; §29.5 documentation row) are false for mode/type changes until B1 C is repaired.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture, and visibly marks within-deliverable surfaces, including `sdp ssds export` and the tool-independent canonical-JSON ledger, with "Beyond the requested deliverable: **None**". No inspectability-driven product requirement was found unmarked. Technical Review accepts no marked item.

## 10. What I verified and how; what I could not verify

**Verified, at the exact candidate:**
- I read the whole Manual. I read the diff from `3540d98`, the closure map and its diff, workplan §6.1/§6.6/§7.4/§21 excerpts and §0.3 HAS, the stakeholder record (SD-11 to SD-24 and entry 18 verbatim), the 3540d98 record in full, and the finding headings of every earlier record.
- `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- `git diff --check 3540d98… e2154ac…`: clean.
- `git diff --stat fad3ee4… e2154ac…`: 29 files, all under `qualification/ssds80/` plus the Manual and one index line in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`.
- `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4`.
- The workplan blob at the candidate differs from the Phase B blob only in Review/lifecycle coordination text.
- Optional extras: `python3 -m unittest tests.test_protocol_63_engineering_memory` (28 OK) and `qualification/ssds80/s1_disagreement_model_check.py` (default mode `REV23`, 0 failures over 1,574,464 transitions).
- One scratch Git diagnostic showed blob-identical, checkout-different bytes under an `eol=crlf` attribute.

Scratch files are under `/tmp/claude-1000/ssds80-manual-review-e2154ac/`; the sandbox refused `/tmp/ssds80-manual-review-e2154ac/`.

**Not verified:**
- Any SSDS implementation or runtime behavior (none exists).
- G3 costs.
- External or native issue homes.
- The full text of earlier Review records beyond their findings sections, which were used only as hypotheses.
- Whether every Git attribute and filesystem layer is covered; the search stopped at the family characterization.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence. It produced, ran or reviewed no realized scientific results.

1. **Material findings.** B1 (blocker) and N1-N5 (non-blocking) above. All are D3 architecture findings. There are no D1/D2 scientific or numerical findings and no out-of-scope scientific findings. I launched no tools or agents beyond the commands listed in section 10.
2. **Realized results.** None produced, run or reviewed, and no gate evidence prepared, so no null envelope is owed. The commands in section 10 are software and toolchain checks on documents and Git, not realized scientific results.
3. **Variants.** Yes, as design and interpretation variants, not result selection:
   - B1 repair directions: four considered (byte-exact materialization; recording attribute files and checkout configuration; analyzer-classified anchor recognition; dropping anchor normalization with `EDITORIAL` equivalence). Selection criterion: preserve the owner-required property with the least added mechanism (convergence owner, "Active simplification trigger").
   - Two readings of §1.4 rule 3 (single pass versus cascade), plus a third post-state reading rejected for having no fixed point. Criterion: literal text and single-valuedness.
   - Two readings of SD-24 ordering (maximum versus latest).
   - The diagnostic model was run in its default mode only.

   No data, held-out set or delegated search was involved. The recommendation is non-binding; the stakeholder chooses.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority: the judgment rests on accepted SSDP 7.2.1 protocol owners (D3, kernel, convergence, evidence, workflow), the proposed workplan and the stakeholder record. No scientific or numerical formulation is accepted for the SSDS product.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The corpus, the inherited workplan framing, the prior Review records (ten of them same-family), the diagnostic model and the toolchain are shared dependencies. The 3540d98 and Phase B reviewers were of another family (GPT). Fresh context does not establish epistemic independence. In particular, this Review's main finding extends the 3540d98 Review's B1 family, which a different-family reviewer opened. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.

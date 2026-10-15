# SSDS 8 Architecture Manual — Independent D3 Review, candidate e9e6e9f

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system (local checkout)
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: e9e6e9f47fef3706cea98b8226d92a61a0df22cb
    SCOPE: whole proposed Manual as the durable D3 owner: (a) §21/§16.2 closure, (b) fidelity and
           refinements R1-R11, (c) out-of-matrix adequacy, (d) inheritance and capability transfer,
           (e) qualification design, (f) doctrine-realization map, (g) O1 content and product-scope marks
    MANUAL: orchestrator/docs/ssds-8.0-architecture.md
    MANUAL BLOB: 058c1b5cc5f5d7f8d5c1159aa0838f4b00a37405 (checked)
    CLOSURE MAP BLOB: c7eb695860d529397da9d70ed90f41f6e85d129c (review aid only; checked)
    PARENT WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md,
           design revision 23; Phase B candidate e23f14208be869e6a78cfd7b312e447254ee1851
           (blob 610f373b97fb8152d2a5742e17fa172e12204756); blob at this candidate
           91bde236465178f20c7348280e036d2884dfc216 (differs only by Review/lifecycle coordination text; checked)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    PRIOR REVIEWS, HYPOTHESIS ONLY: E23F142 Phase B PASS; Manual NO-PASS records 6FF4ED1, B595F2C,
           C6DA678, CC005DB, D837363, 53669A5, 1FFBBF0, 86AB683, 71CF9B3, 798B2B4, 3540D98, E2154AC
    REVIEW METHOD: D3 role entered at the governing public source; immutable-owner reconstruction;
           whole-Manual read at the exact candidate; deductive counterexamples in both polarities;
           family-level search after recurrence (convergence owner, method step 6a), with particular
           attention to the repairs of the previous round's non-blocking findings; prior-finding
           regression; required structural checks; one scratch Git toolchain diagnostic; the optional
           diagnostic model; no implementation or runtime qualification
    REVIEWER: Claude model family (the same family as the Manual's author); a fresh-context
           sub-agent launched by the authoring session from the named handoff; no authoring
           conversation received
    MUTATION BOUNDARY: this record only; no commit or push

Governing SSDP version for this task: 7.2.1.

All Manual section and line references are to the exact candidate, read from a `git archive` snapshot. The checkout HEAD was the later handoff commit `5e0d47b5` on the requested branch. `PROTOCOL-RELEASE-STATE.yaml` identities are the ones the handoff names; governing owners were read with the public-source tree at `aaeaf8b…`: `source/roles/software-design/SKILL.md` and its expanded `dist/skills/software-design/SKILL.md` (entry contract, routing, scientific checks), then `architecture-and-design.md`, `abstraction-and-concretization.md`, `convergence-and-cycle-economy.md`, and the cited passages of `evidence-evolution-and-dependencies.md` and `workflow-and-workplans.md`. Further owners named by the handoff were not loaded because no decision in this Review turned on them.

## SERIOUS CHALLENGE

**None against accepted SSDP 7.2.1 or the frozen Architecture 1.6.0 / Level 0 Core.** Both blockers below are defects of the proposed D3 concretization. The Phase B workplan and the Manual are proposed architecture, so a gap between them is not a challenge to accepted authority.

The baseline owner text this Review applies, unchanged:
- D3 owner, "D3 boundary and feasibility": "A D3 candidate is admissible only when it satisfies every applicable D1/D2 invariant and directly governed security, reliability, compatibility, resource, performance/scaling, deployment and external-interface constraint."
- Kernel, "Verification and Challenge": "A child can perfectly satisfy a too-weak abstraction and still be wrong".
- Evidence owner, "Applicability, immutable observation, and superseding assessment": "A stale passing observation is not admissible confirmation." and "PASS/accepted/closed cannot depend on stale, rejected, unavailable-required or otherwise inadmissible evidence."
- Workflow owner, "Human gates and closeout learning": "Orchestration may represent pending/accepted/rejected state but cannot self-approve it." and, under Channel C, "The gate does not close unqualified when missing realized records could plausibly change its judgment."

## Verdict

**NO-PASS.** Two D3 blockers survive, each stated at family level as method step 6a requires:

- **B1 (content-identity family, third round).** The e2154ac repair fixed one representation and required every runner to materialize it. But realization currency, the consumer the e2154ac trajectory concerned, still reads only recorded tree-resident entries. Two new carve-outs let what the execution read change while every such entry stays the same:
  - the fallback for a runner class that cannot guarantee the representation ("treated as one that does not observe its reads") fails closed only for failure matching, never for passing evidence;
  - a read into a submodule is an external pin that currency never compares with the gitlink entry that selects it.

  Siblings: the attribute-driven Git LFS exception, the owner of the anchor comment classifier, and write-set entries that own no bytes.
- **B2 (gate-qualification family, second round).** The repair of e2154ac N2(a) keys the `QUALIFIED` cap on the qualified acceptance's *currency*. So an agent's blocking challenge, an upheld challenge, staleness of the qualified acceptance's evidence core, or a loss boundary lifts the cap whenever an earlier unqualified `ACCEPT` for the same gate and revision is current. The subject then becomes unqualified-valid without any unqualified gate decision after the limitation, which is not what SD-24 directs. Siblings: §10.4 still states the pre-repair existential, contradicting §5.5; and §5.6's monotonicity argument is now false as written.

The SD-23 multiset, the equal-region single-pass rule, the CRLF recognition rule, the type-and-mode write set (for files with bytes), the classified anchor removal (for Python strings and Markdown fenced blocks) and the disclosures added in §32.2-§32.3 each close the trajectory they target. The D1-D3 change rule and the §6 matching clause have no new finding of their own. This verdict is technical evidence for G1 only. It accepts no architecture, default or product scope, and it authorizes no D4.

## 1. Blockers by earliest owner

### B1 — Realization currency does not read what selected the execution's input

**Earliest owner.** Manual §1.5 "The representation", which is the single content-identity owner, together with the consumers it names:
- realization currency (§4.1 `execution` mode, §17.4);
- the recorded execution basis (§6.3 read and pin entries);
- the runner contract (§17.5);
- the write set (§1.2).

Workplan §21 items 1 ("content normalization and boundary-marker rules"), 4 ("the mechanical computation of each realization's executed content (execution basis, observed runner reads, whole-tree fallback)") and 11 ("trusted-runner designation and custody"). This is a D3 representation defect; it asks no new D1/D2 rule.

**Owner and contract text.**
- Evidence owner (quoted above): a stale passing observation is not admissible confirmation.
- Workplan §6.6, the reviewed contract: executed content is "everything the realization's execution read, recorded at realization by content identity", and "missing dependency knowledge never proves that two executions read the same content".
- The Manual's own claims:
  - §1.5: the representation is "for identity and for every comparison of owned content (the write set and the diff-to-unit mapping, §1.2, §14.5; currency; matching)";
  - R1: "one representation serves every consumer";
  - §17.4: "Stale passing evidence never discharges";
  - §31.2 (A): "a runner honoring the attributes fails qualification".

**Trajectory A — the fallback class reopens the e2154ac trajectory verbatim. Primary; blocker-grade on its own.**

1. Policy designates an external-custody runner class `ci-windows`. Git for Windows defaults to `core.autocrlf=true`, so the class cannot guarantee byte-exact materialization. Following §1.5 ("A runner class that cannot guarantee this is treated as one that does not observe its reads (§17.5)") and §17.5, policy designates it as such, and every execution of the class is recorded as having an unpinnable read.
2. Specification `S` (runner `ci-windows`) reads tracked `data/table.csv`. Its read entry records the **blob** identity (§6.3). Realization `q` passes, is assessed, and discharges `S`'s evidence obligation. §17.4 lets any designated runner discharge, and nothing restricts passing evidence from a non-observing class.
3. An admitted change adds `.gitattributes` with `*.csv text eol=crlf` (or `working-tree-encoding`). No recorded entry names `.gitattributes`. The blob of `data/table.csv` is unchanged, yet the runner's checkout now presents different bytes.
4. `q`'s unit, read and widened entries all re-resolve to their recorded identities, so `sat(execution) = T` (§4.1) and `q` stays current. No `REALIZE` is derived (§10.2: only "without a current admissible realization"), and `valid` keeps resting on a passing observation the execution would not reproduce.

The fallback's only effect is the unpinnable-read flag. That flag acts on permissive uses of failures only: §6.3, "an unpinnable read keeps the observation out of every permissive use (§6.5), so it supports no mechanical stop, while its adverse uses are unchanged"; §6.5, "Permissive uses — those that can make a failure stale or lower a decision class". Passing-evidence currency is neither. So the "fail-closed" treatment the repair (and the e2154ac record's own repair suggestion) relies on does not reach the consumer the e2154ac trajectory broke. The §31.2 (A) case tests only a runner that claims byte-exactness, so it cannot see this.

**Trajectory B — a submodule bump. Primary; blocker-grade on its own; entered through the repair of e2154ac B1 (v).**

1. `src/solver.py` (unit `kern`, D4) imports code from a submodule at `vendor/lib` (gitlink, mode `160000`, commit `C1`). `S` declares `EXECUTION_DEPENDS_ON kern`.
2. A qualified actor records a current `COMPLETENESS(EXEC)` on `{S, kern}`. That is a reasonable judgment, because the Manual itself classes submodule content as outside the tree: §1.5, "the submodule's own content is not part of the tree, and a read into it is an external read pinned by that commit". The runner class observes every read outside the tree.
3. `q` passes. The submodule files it read are recorded only as pin entries `({git = …, commit = C1, path = …})` (§6.3 "a read of a file absent from the tree is an external read (pin entries)"; §20.1 pin grammar). No unit, read or widened entry covers the gitlink path.
4. An admitted change bumps the gitlink to `C2`, changing the submodule code the solver executes. Currency compares only unit, read and widened entries (§4.1, §17.4), never pins (§20.1: "Its content never changes, so `content` entries on it never go stale"). So `q` stays current and discharges.

The scratch diagnostic confirmed the toolchain fact: across the bump, `src/solver.py` keeps blob `822bf7c0…`, only the `160000` entry changes (`37752b4c…` to `4cf60752…`), and no submodule file appears in the superproject tree.

The matching consumers are not affected: `ext` compares the pin, so (1)/(3) fail closed. Currency, however, ignores it. That contradicts R1's "one representation serves every consumer" and §1.5's list, which includes currency. The gitlink is a tree-resident selector of what the execution read, exactly like the symbolic link that 798b2b4 B4 required to be recorded, but nothing records it as traversed.

**Sibling C — the permitted Git LFS transform is attribute-driven.** §1.5 forbids transforms "whatever `.gitattributes` or Git configuration say", then permits "a content-addressed one whose output the blob bytes alone determine and verify (a Git LFS smudge checked against the pointer's object identity)". Standard Git LFS applies the smudge only where `.gitattributes` names `filter=lfs`. So whether the execution reads the pointer text or the object is decided by an unrecorded attribute file. Removing the `filter=lfs` line, with the pointer blob unchanged, flips what `S` reads while the read entry is unchanged: Trajectory A again, through the one permitted exception.

An implementer must choose between two readings, and the Manual does not decide. On one, "output the blob bytes alone determine" forbids attribute-driven application. On the other, the named example (Git LFS) invites it.

**Sibling D — which owner fixes the anchor classifier.**
- §1.5 says normalization is "fixed by the system version and never by policy", yet removes anchor lines only where "the pinned pure resolver of the file's type classifies that line as a comment".
- For Python and C++ that resolver is the language analyzer (§14.5).
- §27.3 says "normalizations (§1.5) … belong to the SSDS system version; the analyzer set belongs to the ruleset".

If the classifier is the analyzer, an analyzer-set `RULESET_ADOPTION` can re-identify revisions: for example, Python 3.12 tokenizes comments inside multi-line f-string replacement fields differently from 3.11. That contradicts §5.9 ("judgments whose basis named analyzer output become non-current only if the output changed") and skips the §27.3 re-acceptance display. The guard of §6.3 survives, because the resolution context records the analyzer set. Not blocking alone.

**Sibling E — write-set entries that own no bytes.** §1.2 now includes "the entry type and mode of every file it owns bytes of". A unit owns no bytes of an empty file, or of a gitlink. Yet `cid` hashes the entry type and mode of "every file a term resolves into", and the commit a gitlink records.

So an `IMPLEMENT` item that sets the executable bit on an empty file under a D2 `prefix`, or bumps a gitlink under a D2 or D3 `prefix`, changes that subject's revision without putting it in the write set. The §13.2 domain rule and the §29.4/§29.5 E0 claims fail for these entries; this is the e2154ac B1 C residue. Not blocking alone; the fix is to say "every file its terms resolve into".

**Family assessment (convergence owner, "Review strategy after recurrence"; "Active simplification trigger").** This is the third successive round in the family: 3540d98 B1, then e2154ac B1, now this one. It is a **non-local recurrence**, not a clean local defect.

The shared cause is the same each round. What an execution read is determined by:
- the recorded tree-resident entries; and
- **selectors** the runner applies: checkout transforms, attribute-driven filters, gitlink commits, and before 798b2b4 symbolic links.

Currency compares only the first set. Each repair has added a statement about runner behavior plus an exception (a fallback class, a permitted transform, a gitlink rule), and each exception reopened the class. This matches the owner's trigger ("special cases accumulating around one owner"). Further sibling search (every filesystem layer, case-insensitive checkouts, `git archive` `export-subst`) would become implementation-like. §1.5's class rule ("presents exactly this representation") already makes those D4 obligations, except where the Manual itself carves an exception.

**Minimum repair direction (subtractive; no new primitive, record kind or registry).**
1. Remove the fallback for passing evidence. A runner class that cannot guarantee the §1.5 representation is not a designated runner for discharge. Alternatively, its passing realizations are never current after any change to the tree outside the recorded entries; that is, a whole-tree basis.
2. Record every tree-resident selector a read traverses, by the existing rule for symbolic links: a read into a submodule records the gitlink entry as a read entry, so a bump changes currency.
3. Either drop the LFS exception (present pointer bytes; the object becomes an external read pinned by its object identity, with the pointer recorded as above), or require that whether to smudge is a function of the blob bytes alone.
4. Name the system version as the owner of the comment classifier.
5. Say "every file its terms resolve into" in §1.2.

Options for the stakeholder (Phase C handoff §5), since this is a non-local recurrence:
- **(a)** the subtractive repair above;
- **(b)** record materialization inputs (`.gitattributes` files, checkout configuration, gitlinks) as read entries of every realization, which adds recorded state;
- **(c)** restrict governed evidence to Dispatcher-controlled byte-exact runners, which narrows product scope;
- **(d)** a different-family Review before repair.

**Required discriminators.** At the real Content Model → Dispatcher/runner → realization currency → discharge owners:
- **(A)** Under a class declared unable to guarantee the representation, absorb a `.gitattributes` `eol` change with the read blob unchanged. The passing realization must not stay current, or must never have discharged.
- **(B)** A submodule bump with every other byte unchanged makes the passing realization non-current and derives `REALIZE`.
- **(C)** Removing `filter=lfs` with the pointer blob unchanged either makes the realization non-current or leaves what the runner presents unchanged.
- **(D)** An analyzer-set adoption that changes Python tokenization leaves every `cur` unchanged, or is shown as a re-identification at its gate.
- **(E)** An `IMPLEMENT` item that only changes the mode of an empty D2 file, or a gitlink under a D2 `prefix`, is a `VIOLATION`.

The present §31.2 "Representation" cases discriminate none of A-E.

### B2 — The qualified-gate cap follows the qualified acceptance's currency

**Earliest owner.** Manual §5.5 (the `valid` gate term and the cap paragraph), together with:
- §10.4 discharge;
- §16.8 "Qualified gates";
- §0.3 R11.

Workplan §21 item 7 ("three-valued discharge, provisional propagation") and item 3 (gate outcome vocabulary). The repair of e2154ac N2(a) entered here.

**Owner and contract text.**
- SD-24, verbatim: a `QUALIFIED` `GATE_DECISION ACCEPT` "supports validity and discharge only as `P` (bounded continuation, visibly qualified, propagating by `min`) until an unqualified gate decision on the same revision". Entry 18 of the same record says "until a later unqualified gate decision".
- Workflow owner, quoted above: orchestration "cannot self-approve", and the gate "does not close unqualified when missing realized records could plausibly change its judgment".
- Manual §0.4 **A8**: "a material finding survives to its owner; escalation is keyed on existence, never currency; only an authenticated human judgment discharges human attention"; and §15.6: "Human attention is discharged only by an authenticated human judgment (A8)."
- Manual §5.3: "Effects are conservative in both directions"; a challenge or loss boundary "can only restore a block or a revocation, never lift one".
- R11 itself: the cap holds "until its author supersedes it unqualified".
- §5.5 instead: "The cap lifts when no current `QUALIFIED` `ACCEPT` remains: its own author supersedes it … or it stops being current."

**Trajectory (the case §5.5's own "whatever their order" sentence addresses).**

1. D2 subject `s` at revision `r` in its run, with a counting revision-assessment record and a required gate `g`.
2. Holder `H1` records `GATE_DECISION ACCEPT`, `ADEQUATE`, `UNQUALIFIED` (`h_u`) on the evidence core rendered then. `valid(s) = T`.
3. A later realization or finding shows a material limitation (for example, convergence shown only for a narrow regime). Holder `H2`, or `H1` without naming `h_u` in `supersedes`, records `ACCEPT`, `ADEQUATE`, `QUALIFIED` (`h_q`) on a core that includes that record. Per §5.5, `valid(s) = P`, descendants are `P`, and the inspector keeps an entry open.
4. Any of the following makes `current(h_q) = F` while `h_u` stays current:
   - **(a)** any qualified actor, including an agent, raises a blocking `CHALLENGE` against `h_q` (a support-tier record; §3.4 permits it), so `status1(h_q) = BLOCKED`;
   - **(b)** that challenge is upheld. This is the case where the adjudicator agrees the limitation is *worse* than `h_q` stated;
   - **(c)** a record in `h_q`'s evidence core goes stale (`GATE_DECISION` holds `record` entries on "every record of the evidence core shown", §4.3), for example because the limiting realization's read data file changed; `h_u`'s older core did not contain that record;
   - **(d)** a `LEDGER_LOSS` lies between them, so `h_q` is withheld and `h_u` is not.
5. The conjunct `⋀_{current … h} unq(h)` drops `h_q`. Since `current(h_u) = T`, the gate term and `valid(s)` return to `T`, the descendants become unqualified, and the inspector entry closes ("until no current `QUALIFIED` `ACCEPT` remains"). No unqualified gate decision was made after the limitation was stated.

Effects:
- In (a), an agent's restrictive instrument closes a human-stated limitation and lifts a human-attention entry without a human judgment, contrary to A8 and §15.6.
- In (b), the strongest restrictive outcome makes the subject *more* valid, an inversion of §5.3.
- In (c), ordinary content drift erases the limitation silently: no obligation is derived, because `GATE(g)` sees a current `ACCEPT`.
- All four exceed SD-24, which lifts the cap only by an unqualified gate decision. The R11 row and §5.5 now disagree on the lifting rule.

**Sibling (b) — discharge still states the old existential.** §10.4 says "every human gate of o has a current authenticated ACCEPT, valued P if it is QUALIFIED (§5.5 unq)". With `h_u` and `h_q` both current, the natural reading (an existential with a per-witness value, as in the formula's first line) gives `T`; §5.5's conservative rule gives `P`. So in the exact case the N2(a) repair targeted, `GATE(g)` and dependent obligations can discharge `DISCHARGED` while `valid(s) = P`. Two statements of one closure condition disagree, and an implementer must choose.

**Sibling (c) — stratification statement now false as written.** The new conjunct ranges over `{h : current(h)}`, so `valid(s)` is anti-monotone in `current(h_q)`. §5.6 still says "S2's right-hand sides are built from `min` and `max` over S2 variables and constants … The system is therefore monotone", and the R2 rationale says "Forcing only lowers values". Clamping a `QUALIFIED` `h` that lies on a forced cycle to `F` *raises* `valid(s)` when an unqualified `ACCEPT` is current.

Single-valuedness (C8) still holds, but only because the clamp leaves an acyclic graph that is evaluated once in topological order, and the static graph already has an edge from each subject to every gate judgment naming it (§5.6 item 2). The Manual does not give that argument, and its stated one is false.

**Family assessment.** This is the gate-qualification family's second round (3540d98 B3, closed by SD-24; then the e2154ac N2 residue). It entered through the repair of a non-blocking finding, as the handoff warned. The cause is local and single: the cap is keyed on *currency* where the Manual's own adversity rule keys restriction on *existence and standing* (§5.5 "An adverse judgment counts by existence"; §5.4 "adversity follows existence"). It is a clean local defect with three manifestations, not a non-local recurrence, so a local repair suffices.

**Minimum repair direction (subtractive; restores monotonicity).** Read the cap from S0/S1 facts, as the veto already is:
- a `QUALIFIED` `ACCEPT` for `(g, r)` caps the gate term at `P` while it **stands**: not superseded by its own author's later `UNQUALIFIED` `ACCEPT` (the R11 rule), or disposed of by the owner's adjudication;
- a challenge, staleness or loss boundary never lifts it;
- the gate term becomes `(⋁ current(h)) ∧ capq(g, r)`, with `capq` an S0/S1 constant, so §5.6's argument holds verbatim;
- §10.4 references this one term instead of restating it;
- the §16.8 entry closes only on an authenticated human judgment.

A second option the stakeholder may prefer: Admission admits a `GATE_DECISION ACCEPT` on an answered `(g, r)` only as its author's superseding reassessment, so at most one gate decision stands per gate and revision.

**Required discriminators.** Each with `h_u` then `h_q` on one gate and revision:
- a blocking challenge against `h_q`, an upheld one, staleness of a record only `h_q`'s core holds, and a boundary between them each leave `valid(s) ≤ P` and the inspector entry open;
- `GATE(g)` discharge agrees with `valid`'s gate term in every case;
- only `h_q`'s author's `UNQUALIFIED` `ACCEPT` (or the owner's adjudication) lifts the cap.

The present §31.6 case ("a later `UNQUALIFIED` `ACCEPT` … lifts the cap") discriminates none of these.

## 2. Non-blocking findings

- **N1 — An `ABSENT` composite's revision is blind to its surviving members (partition family; entered through the e2154ac N1 repair).** Under the single-pass, no-cascade rule, a composite subject `A` set to `ABSENT` by partial overlap keeps its member `m` with `m`'s bytes, but `content(A)` hashes only `A`'s own terms, now `ABSENT`. If `A` is then accepted at that revision, edits to `m` change neither `cur(A)` nor the run. A D2 method section can then change under an unchanged acceptance and gate without a revising review.

  Nothing in Admission, the gate or §16.6 refuses this. Still, the trajectory needs a reviewer and a gate holder to accept a subject whose content is `ABSENT` with an integrity finding open, so it is a judgment failure the machinery merely permits: not blocking. Cheapest repair: refuse acceptance (`AUTH_ILL_FORMED`) of a triple any of whose subject's declared terms resolves to `ABSENT`.
- **N2 — Classifier precision (content-identity family).**
  - (i) Under CommonMark a line beginning `<!--` *is* an HTML block (type 2), so "a Markdown HTML-comment line outside fenced code and HTML blocks" literally excludes every comment anchor. Say "outside fenced code, indented code and other HTML blocks".
  - (ii) Indented code blocks are not named, though the class rule ("classifies that line as a comment, not as data") covers them.
  - (iii) The Manual does not say whether `anchor`-term *resolution* also uses the classifier. If it matches by syntax, a data line that looks like an anchor (the e2154ac Trajectory B oracle string) duplicates the real anchor and makes the term `ABSENT`. That is restrictive, but it contradicts the "data, not anchor" intent.
- **N3 — The SD-23 multiset makes `ext` sensitive to read counts.** "The same multiset of (external locator, pin) pairs" separates two runs that read one pinned file once and twice (library caching, retries). Comparing the *set* of pairs closes the e2154ac N4 ambiguity (one locator under two pins gives two pairs) equally well, without that fail-closed noise. Restrictive only.
- **N4 — Closure-widening wording under complete observed reads (pre-existing; bears on B1 B).** §6.3 says the widening "reaches the whole tree" only where no completeness judgment bounds the closure *and* observed reads are incomplete; §4.6's algorithm widens on the judgment alone; §2.6 says markers never override "complete observed reads". State once whether complete observed reads bound the closure. B1 B holds under either reading, because its premise includes a current `COMPLETENESS(EXEC)`.
- **N5 — Accounting.** §30, R1's rationale and the closure map (item 1 and the stakeholder-attention list: "materialized byte-exact by every runner") omit the non-guaranteeing fallback and the gitlink and LFS carve-outs. They therefore state a stronger property than §1.5 and §17.5 deliver (see B1). The aid confers no authority.

## 3. Closure audit

I located each workplan §21 item and clause in the Manual directly, and used the closure map only as an index. "Answered" means a substantive D3 answer exists; it is not runtime qualification or stakeholder acceptance.

| §21 | Independently located answer | Result |
|---|---|---|
| 1 | §§1.1-1.11 | **Not substantively closed (B1 C-E)**: representation exceptions, classifier owner, write-set entries without bytes; N1, N2 |
| 2 | §§1.7, 2.1-2.6 | Answered |
| 3 | §§3.1-3.6, 6.8, 17.1; gate `adequacy`/`qualification` (§3.4, §5.5) | Answered as vocabulary; the qualification semantics carries B2 |
| 4 | §§4.1-4.6, 6.3 | **Not substantively closed (B1 A, B)**: currency of passing realizations does not compare runner selectors (fallback class, gitlink); N4 |
| 5 | §§5-7, 17, 22.3 | Answered for §6 and strata; §5.6's monotonicity statement is false as written (B2 c) |
| 6 | §§8, 21-23 | Answered |
| 7 | §10 | **Not substantively closed (B2)**: two statements of the gate term in discharge versus validity; cap lifted by currency |
| 8 | §11, §13.2, §13.4 | Answered |
| 9 | §9 | Answered |
| 10 | §16 | Answered; the §16.8 qualified-gate entry carries B2 |
| 11 | §§17, 6.10 | **Not substantively closed (B1 A, C)**: runner designation admits a non-guaranteeing class whose passing evidence discharges; LFS exception undefined |
| 12 | §18 | Answered |
| 13 | §§19-20 | Answered |
| 14 | §§21-25 | Answered; runtime unexecuted |
| 15, 16 | §25.1-§25.3 | Answered |
| 17 | §26 (both transfer tables) | Answered |
| 18, 19 | §§27, 28 | Answered; §27.3 versus §1.5 classifier owner is B1 D |
| 20 | §20 | Answered; submodules as "supported class" (§20.4) carry B1 B |
| 21 | §29.7 | Answered |
| 22 | §30 | Present; its "runners must materialize exactly that representation" overstates (N5) |
| 23 | §12, §1.2/§13.2 | Answered except the residue of B1 E |
| 24 | §13 | Answered |
| 25 | §14 | Answered as design; no threshold accepted |
| 26 | §§15-16 | Answered |
| 27 | §29 | Present; the §29.4/§29.5 E0 claims "only through an `AUTHOR` item" need B1 E |

**Workplan §16.2, both tables.** All 26 product-invariant rows and every frozen-surface row (§3-§22, including §4 layout and namespace and §14 CLI) have final dispositions in Manual §26.4. I read them against the rows. No row is merely routed, and §26 is unchanged since e2154ac (diff).

**Material decisions versus delegated D4.** File-type-table extension, diff implementation, checkpoint encoding, parsers and limit values are marked `[delegated]`, correctly. Two architectural decisions are left implicit, which is part of B1:
- whether a non-guaranteeing runner class may discharge;
- whether gitlink traversal is a recorded read.

## 4. Refinements R1-R11

| # | Assessment |
|---|---|
| R1 | **Sound as a matching construction**: `on⁺ ⇒ on⁻` by construction; the guard holds, because the resolution context records the analyzer set that now also classifies anchors; the multiset `ext` is restrictive only (N3). **Its "one representation serves every consumer" claim fails for currency (B1 A, B).** |
| R2 | Sound for cycle nodes (presented `F`). The rationale "forcing only lowers values" is false once B2's conjunct exists (B2 c). |
| R3 | Sound; unchanged. |
| R4 | Sound within its crash model; residuals disclosed; unchanged. |
| R5 | Sound for equal and partially overlapping regions in one pass (e2154ac N1 closed); N1 here is a new consequence of no-cascade. |
| R6 | Sound; CRLF recognition (iv) now defined, so byte-preserving refinement holds in CRLF files of classified types; in unclassified types an anchor refinement changes `rev`, as §1.5 states. |
| R7 | Sound; unchanged. |
| R8 | Sound; it supplies the own-author route B2's repair needs. |
| R9 | Sound; unchanged. |
| R10 | Sound for its cases; mode and type churn starts runs (disclosed, §32.3). |
| R11 | **The row is a sound narrowing toward SD-24 and the Channel C rule, but §5.5 does not realize it**: §5.5 adds "or it stops being current", and §10.4 restates the pre-repair existential (B2). |

## 5. Previous findings and Phase B closures

"Closed" means the named trajectory is excluded by the present text, which I re-derived independently; it is not runtime evidence. Prior records were read as hypotheses only.

For findings whose cited text lies outside the sections this round changed (the diff from e2154ac touches only §0.3, §1.2, §1.4, §1.5, §5.5, §6.5, §14.5, §16.8, §17.5, §30, §31.2 and §32.2-§32.3), I re-read the cited present text and give the basis. Where my disposition differs from the e2154ac record's, I say so.

### E2154AC (same family)

| ID | Disposition and basis |
|---|---|
| B1 | **Partly closed.** (A) closed for runners that guarantee the representation, but reopened by the fallback class, the gitlink rule and the LFS exception (B1 A-C here). (B) closed for Python strings and Markdown fenced blocks; precision residue N2. (C) closed for files with bytes; residue B1 E. (iv) closed (LF line end, one CR ignored). (v) defined, and the definition creates B1 B. |
| N1 | Closed: single pass over §1.3 resolutions, no cascade (§1.4 rule 3; §31.2 (E)). New consequence N1 here. |
| N2 | (a) **Partly closed**: conservative over current acceptances, but the cap now lifts by non-currency, and §10.4 keeps the existential (B2). (b) Closed as display (§16.8 entry), but the entry closes on non-currency (B2). (c) Closed ("only where policy permits provisional continuation", §5.5). |
| N3 | Closed: R11 row, R5 row mentions equality, §30 account, map item 7 recompiled. |
| N4 | Closed: costs and guidance disclosed (§17.5, §32.2, §32.3); multiset precision (N3 here). |
| N5 | Closed as disclosure (§32.2 representation narrowing; §32.3 churn trigger). |

### 3540D98 (different family)

| ID | Disposition and basis |
|---|---|
| B1 | **Partly closed**: binary, executable-bit and link cases change `cid` (§1.5). The family is open as B1 here. |
| B2 | Closed: `ext` compares the complete multiset of `(locator, pin)` pairs (§6.5); disjoint, subset, superset and alias variants fail `ext`; (2)/(4) use `on⁻` without pins. |
| B3 | Closed for its single-acceptance trajectory (`ADEQUATE` required; `unq = P` enters `valid` and discharge). The family reopens with two acceptances (B2 here). |
| B4 | Closed: equal regions of units not related by membership resolve to `ABSENT`, in one pass (§1.4). |
| N1 | Closed: prospective run defined (§10.2). |
| N2 | Closed as disclosure (§32.2, later `ABSENT`). |
| N3 | Closed (aid recompiled). |
| N4 | Held: residuals and costs disclosed (§32.2-§32.4). |

### 798B2B4

| ID | Disposition and basis |
|---|---|
| B1 | Closed: never-integrated frame acceptances are in no admitted run (§10.2). |
| B2 | Closed: run membership is `tgt`, read by `base`, `valid`, `ACC`, triggers and discharge (§5.2, §10.2 "Currency"). |
| B3 | Closed: predecessor is a display only (§10.2). |
| B4 | Closed for links (§6.3 records traversed links); the analogous gitlink traversal is B1 B here. |
| N1-N3 | Closed: R10 scope "`NATIVE` subject of kind D1 or D2"; acceptance carries `record` on the assessment record (§4.3); envelope predecessor map (§12.2). |
| N4 | Closed: `REVIEW(s, r)` derived for a requested cutover (§10.2, §19.5). |
| N5 | Closed as disclosure (§1.9, §32.2). |
| N6 | Closed: no revision-condition `holds` remains. |
| N7 | Closed as document coverage (§31.5, §31.3). |
| N8 | Closed (aid). |

### 71CF9B3

| ID | Disposition and basis |
|---|---|
| B1 | Closed: the run starts at any position where `cur(s)` took its value (class rule, §10.2). |
| B2 | Closed: old in-tenure D1/D2 acceptances fail `tgt` after a revision change; S11/R10 present (§0.3, §0.4). |
| N1-N4 | Closed: predecessor is display; only a counting record answers `REVIEW(s, r)`; §12.2/§13.5/§16.6/§30 present; cutover binding (§19.5). |
| N5 | Closed: supplied versus runner-external randomness (§6.10, §17.5, §31.3). |
| N6 | Closed for links (§6.3). |
| N7 | Closed as disclosure (§1.9, §2.6, §32.2). |
| N8 | Closed (aid). |

### 86AB683

| ID | Disposition and basis |
|---|---|
| B1 | Closed: a record counts only in the run, with `status1 ∉ {REVOKED, BLOCKED}` and `cont`, carried through the acceptance's `record` entry (§10.2). |
| N1-N6 | Closed: cutover binding (§19.5); randomness disclosure (§6.10); unpinnable flag, attribute set and observation flag recorded by value (§6.3); disclosures (§1.9, §2.6, §32.2); quarantine paths (§18.4); one slot entry per subject (§13.5, §16.6). |
| N7 | Closed (aid). |

### 1FFBBF0

| ID | Disposition and basis |
|---|---|
| B1 | Closed: free seed is a recorded attribute; a non-observing class records an unpinnable read (§6.3, §6.5, §17.5). |
| B2 | Closed: §8.3 step 7 refuses a passing D1/D2 acceptance or gate `ACCEPT` without a counting record, in every frame, for humans too. |
| N1 | Closed: newly declared file and span terms must resolve (§1.9). |
| N2 | Closed for content, keys, regions, membership and signature; type and mode now included. Residue for entries without bytes is B1 E. |
| N3-N6 | Closed: predecessor display (§10.2, §13.5); structural-delta quarantine paths (§18.4); declared-set change disclosure (§17.5); environment-component files excluded from external reads (§20.1). |
| N7 | Closed (aid). |

### 53669A5

| ID | Disposition and basis |
|---|---|
| B1 | Closed: `ext` compares every recorded attribute (§6.5). |
| B2 | Closed: direct human acceptance or gate before a counting record refused (§8.3 step 7). |
| B3 | Closed: the intake target rule concerns targets, not timing (§18.4). |
| N1-N8 | Closed: SD-17 withdrawal (red-then-green, §31.3); "`NATIVE` kind D1/D2" scope (§10.2); `ssds.manifest` in `AUTHOR` scope (§13.2, §31.5); cross-domain structural route human or adoption (§13.2); resolver purity (§1.9); moved-out content disclosed (§18.4, §32.2); declaration-key conflicts (§7.2); named statements present. |
| N9 | Closed (aid). |

### D837363

| ID | Disposition and basis |
|---|---|
| B1 | Closed: free environment attributes are compared only permissively (§6.5, §17.1). |
| B2 | Closed: pure byte resolvers; resolution context recorded by value at execution start (§1.3, §6.3). |
| B3 | Closed: target-keyed revising record (§8.3 step 7, §10.2). |
| B4 | Closed: write set compares `T_n` under `Σ_n` with `M_n(X)` under `Σ_n ⊕ Δ_Σ(X)` (§1.2). Residue B1 E. |
| N1-N7 | Closed: nested different-kind revision (§1.2, §16.6); cross-kind route (§13.2); `QUARANTINE` effect (§18.4, §5.5); re-identification disclosure (§27.3); manifest always in the write set; `OPEN`/`RESOLVED` findings and predecessor slot (§13.5). |
| N8 | Closed (aid). |

### CC005DB

| ID | Disposition and basis |
|---|---|
| B1 | Closed for boundary and new-part routes (effect write set, §1.2). Residue B1 E. |
| B2 | Closed: system version in the recorded resolution context (§6.3). |
| B3 | Closed: product-scope acceptance is its own record kind (§3.5, §5.5). |
| N1 | Closed: tracked ignored files are read entries (§6.3, §20.1). |
| N2 | **Closed as disclosure** (the e2154ac record had it partly closed): incidental-read cost and hermetic guidance stated (§17.5, §32.2). |
| N3-N7 | Closed: no permissive frozen-analyzer fallback (§5.9, §6.3); term-level resolution and single-pass rule 3 (§6.3, §1.4); contrary-order mechanics (§18.4); re-review policy (§16.5); re-identification disclosure (§27.3). |
| N8 | Closed (aid). |

### C6DA678

| ID | Disposition and basis |
|---|---|
| B1 | Closed: pins and unpinnable reads never narrow `on⁻`, (2), (4) or `adm` (§6.5, §6.8). |
| B2 | Closed: `same` spans item revisions at identical changed content (§5.5). |
| B3 | Closed: effect write set (§1.2, §13.2). |
| N1-N6 | Closed: `stands⁻` requires the chain's last record to stand (§5.5); intake adverse outcomes (§5.5, §10.3); own-author reassessment disclosure (§5.5, §8.3); `COMPLETENESS` sameness with member revisions (§5.5); `REFUSED` (§10.4); pure resolvers (§1.3, §14.5). |
| N7 | Closed for classification (§6.3, §20.1); the identity of gitlink-selected reads is B1 B here. |
| N8-N11 | Closed: residual-part identity (§6.3); empty prefix (§1.3, §1.8); re-review policy (§16.5); `ref` locality (§13.2). |
| N12 | Closed (§30 recompiled); N5 here is a new omission. |

### B595F2C

| ID | Disposition and basis |
|---|---|
| B1 | Closed: unit and term granularity (§6.3, §6.6). |
| B2 | Closed: `ref` locality and byte-identical prose for tightening (§13.2, §13.4). |
| B3 | Closed for `DOCUMENT` (§13.2); B1 E is a different route. |
| B4 | Closed: answered once; symmetric veto; one `TASK_RESULT` per task (§8.3 step 7, §10.3, §5.5). |
| N1-N8 | Closed: machinery `COMPLETENESS` producer (§2.6); `ANALYZER_OUTPUT` (§5.9, §14.5); analyzer set in `RULESET_ADOPTION` (§27.1); complete external record (§6.5); single-provisional check (§5.7, §23.4); `TEST_INTEGRITY`/`BOUNDARY` (§13.3); named statements (§30); `AUTHOR` scope (§13.2). |

### 6FF4ED1

| ID | Disposition and basis |
|---|---|
| B1 | Closed: `on⁺ ⇒ on⁻`; frozen resolution context (§6.3, §6.5). |
| B2 | Closed: any prose change is R2 (§13.4). |
| B3 | Closed: analyzer set pinned by `ρ_n` (§5.9). The classifier owner is B1 D. |
| B4 | Closed: `AUTHOR`/`DOCUMENT` obligations, holders, contracts and slots (§10.2, §12.3, §13). |
| N1, N2 | Closed: computability yields on evaluated outputs (§6.5, §6.6); supersession by kind (§8.3 step 3). |
| N3 | **Partly closed**: the `qualification` field is present and propagates, but by currency (B2). |
| N4-N12 | Closed: no new or grown SCC (§8.3 step 5); analyzer completeness only as challengeable `COMPLETENESS` (§2.6); `CHALLENGES` excluded (§2.3-§2.5); static checks plus dynamic `ABSENT` (§1.4); single-provisional in qualification; map rows (§29.3); §26.4 dispositions; export within the deliverable (§0.5); annotations present. |

### Phase B §3 closures and N1-N4

| Closure or limit | Present reconstruction |
|---|---|
| Y1 identical-outcome coverage; Y2 candidate-own not re-escalated | Held (§6.5 coverage; §6.8 class). |
| EF8445A/552AC01 N2 strata, completeness polarity, class basis | **Re-tested.** I used an alternate tree differing from `tree(a⁻)` only outside a recorded narrow basis, including a tree differing only in `.gitattributes` or a gitlink outside the recorded entries. A differing old-content run stays in (2), and a yielding present-content run stays in (4), under completeness `P`, blocked, revoked or loss-withheld: both use `on⁻`, which reads no completeness, no pins and no S2 value (§6.5-§6.6). Losing completeness only narrows (1)/(3). Held. |
| Absorbed assessor-read relaxation; identical-outcome floor; material difference X1-X3 | Held (§6.5-§6.8). |
| Promotion, refinement, enactment | Held (§7.6, §19.3-§19.4); refinement in unclassified file types now changes `rev`, as stated. |
| Adversity versus currency, challenge, loss | Held for assessments and adverse judgments (§5.4, §6.7). **B2 shows the one place where qualification follows currency instead.** |
| Salvage, retirement, unauthorized supersession; scope anchors, home, independence; start latch | Held (§8.3 steps 3 and 6, §10.2, §6.4, §6.8). |
| U1/U2/W1/W2 executed content and reading | Held for recorded reads; B1 A-B show recorded identities that do not denote what was read. |
| Contrary-run retention, nondeterminism | Held (§6.6 (2)/(4); §6.10). |
| Warrant/S1/S2 cycles, fail-closed support cycles | Held for cycle nodes (§5.6 clamp before presentation); the downstream monotonicity statement is B2 (c). |
| Corrupt prefixes | Held (§5.7 `INTEGRITY_HALT`). |
| Effective structure, quarantine, tenure | Held (§1.6, §8.3 step 4, §19.4). |
| Phase B N1 adoption provenance | Disclosed (§32.2, §32.4). |
| Phase B N2 positive-only completeness | Held, as re-tested above; §31.3 carries real-owner cases. |
| Phase B N3 diagnostic bounds | Held (§31.3 "Diagnostic model"). |
| Phase B N4 cost and applicability | Held as reopen triggers (§32.3), now including churn and incidental-read triggers. |

## 6. Out-of-matrix trajectories attempted

| # | Trajectory | Result |
|---|---|---|
| 1 | `.gitattributes` `eol`/encoding change, read blob unchanged, byte-exact Dispatcher runner | Held: runner presents blob bytes (§1.5, §17.5) |
| 2 | The same under a runner class declared unable to guarantee the representation | **Violation (B1 A)**: passing evidence stays current |
| 3 | Submodule bump with every recorded tree-resident entry unchanged | **Violation (B1 B)**: currency ignores pins; matching fails closed |
| 4 | `filter=lfs` removed, pointer blob unchanged | **Ambiguous (B1 C)** |
| 5 | Analyzer-set adoption changing Python comment tokenization | **Contradiction (B1 D)**: may re-identify revisions |
| 6 | `IMPLEMENT` item: mode of a D2 file with bytes; of an empty D2 file; gitlink under a D2 prefix | Held; **escapes (B1 E)**; **escapes (B1 E)** |
| 7 | Anchor-syntax line in a Python string or Markdown fenced block | Held: data, kept in `cid` |
| 8 | Comment anchor in an HTML-block-adjacent or indented Markdown line | Wording-dependent (N2) |
| 9 | CRLF and LF files with the same anchors and headings | Held: same recognition |
| 10 | Composite partially overlapping a sibling, its member equal to a top-level anchor | Held: one pass, both `ABSENT` |
| 11 | Accepting an `ABSENT` composite, then editing its surviving member | Permitted; revision blind (N1) |
| 12 | `h_u` then `h_q` on one gate: blocking or upheld challenge on `h_q`; `h_q` basis stale; loss between | **Violation (B2)**: cap lifts, `valid = T` |
| 13 | The same pair: discharge versus validity | **Contradiction (B2 b)** |
| 14 | `QUALIFIED` gate decision on a forced cycle | `valid(s)` rises when the clamp applies (B2 c); C8 still holds |
| 15 | Single `QUALIFIED` `ACCEPT`, author supersedes unqualified | Held: lifts as SD-24 directs |
| 16 | `INADEQUATE` `ACCEPT` | Held: refused |
| 17 | Repeated reads of one pinned file across runs | Restrictive only (N3) |
| 18 | 3540d98 B2 variants (disjoint, subset, superset, alias locators) | Held |
| 19 | D1/D2 revert, mode churn, rule-3 flip and back, frame records of a non-integrated lineage | Held: each value change starts a new run; nothing revives |
| 20 | Gitlink bump on a D1/D2 subject's `prefix` | Held for `rev` (new run); write set misses it (B1 E) |
| 21 | Phase B N2 completeness polarity with `P`/blocked/revoked/loss-withheld judgment | Held (§5 table) |
| 22 | Support cycle through absorbed `about` or completeness edge; corrupt authenticated prefix | Held (§5.6, §5.7) |

## 7. Minimum architecture and capability transfer

No primitive, component, persistent surface or record tier is added this round. The added statements are contract statements, plus two exceptions (the non-guaranteeing fallback and the LFS transform) and a gitlink rule. Those exceptions are exactly where B1 enters. Both minimum repairs remove mechanism or keep it constant:
- B1: one fallback and one exception removed; the existing link-recording rule extended to gitlinks;
- B2: a currency-indexed conjunct replaced by an S0/S1 standing constant, which restores the monotonicity argument.

The §30 table remains the minimum justified set within this Review's evidence, subject to N5.

Capability transfer: the §26.4 tables are unchanged since e2154ac and were re-read against workplan §16.2 and §18. Core prompt mode, frozen profiles and the containment root are preserved, and Core never imports SSDS (§26.2-§26.3).

PEM was activated, because this is mature-machinery replacement. Accepted/base memory `PROJECT-ENGINEERING-MEMORY.md` is byte-identical between `main` and the candidate, and `tests.test_protocol_63_engineering_memory` passes (28 tests). The workplan §0.3 HAS dispositions are realized:
- PC-001: §26.3/§26.4/§28/§31.8;
- SP-002: G3 and §21.2;
- FF-001: §19.9;
- DS-001: §31.1, and see §8 below;
- SP-001: §5.8.

`orchestrator/docs/architecture.md` (blob `39e6de72…`) and everything under `source/` and `dist/` are byte-unchanged from `fad3ee4`.

## 8. Qualification-design adequacy

§31.1 states that no executable SSDS evidence exists at G1 and that every runtime group is `UNEXECUTED`. Nothing is claimed as executed. The new §31.2 "Representation" cases (A)-(E) name negative discriminators.

Green fixtures could coexist with the defects (DS-001):
- B1 A: case (A) exercises only a runner claiming byte-exactness; no case designates a non-guaranteeing class and checks its passing evidence.
- B1 B-C: no submodule or LFS case.
- B1 D: the §31.2 analyzer-pinning case checks historical views, not `cur` across an analyzer adoption.
- B1 E: case (C) uses a file with bytes.
- B2: §31.6 has a single acceptance and a later unqualified one, with no coexisting acceptances, challenge, staleness or boundary.
- N1: no acceptance of an `ABSENT` composite.

The diagnostic model was run in its default mode: `REV23`, 0 failures over 1,574,464 transitions, model file unchanged since e2154ac. It does not model these clauses, as §31.3 states.

## 9. Doctrine-realization map and O1

The §29 map is unchanged. I re-checked §29.4 row by row against the expanded 7.2.1 scientific checks:
- delegate questions, gaps, findings, realized results, variants, tensions;
- choices, retention, claims, before loss, resources, persistence, persisting tensions;
- inaccessible homes, product changes, authority content and the revising-duty row.

§29.2-§29.3 cover the entry contract and role contracts; §29.6 lists the disclosed E3 duties. Two corrections are owed:
- The E0 claims that an agent "can change what a D1-D3 unit itself owns only through an `AUTHOR` item" (§29.4; §29.5 documentation row) are false for entries without bytes until B1 E is repaired.
- The Channel C realization (§29.7 first row; §16.6) relies on B2's cap. Until B2 is repaired, "the gate does not close unqualified" is not realized at E0 when two acceptances coexist.

O1 (§0.5) states the realized record, readers, routine questions and realized-record architecture. It visibly marks the within-deliverable surfaces, including `sdp ssds export` and the tool-independent canonical-JSON ledger, with "Beyond the requested deliverable: **None**". I found no inspectability-driven product requirement left unmarked. Technical Review accepts no marked item.

## 10. What I verified and how; what I could not verify

**Verified, at the exact candidate:**
- **Reading.** I read the whole Manual. I read the diff from e2154ac (Manual and closure map); workplan §0.3, §7.4 and §21 at the candidate; and the stakeholder record in full (SD-1 to SD-24 and entries 1-18). I read the e2154ac record in full and the finding tables of the earlier records it summarizes, as hypotheses. I read the Phase C handoff §5 and the governing owners named above at `aaeaf8b…`.
- **Blobs and workplan.** Manual, closure-map and workplan blobs match the handoff. The workplan differs from the Phase B blob only in coordination text (word diff inspected).
- **Tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v`: 4 tests, OK.
- **Whitespace.** `git diff --check e2154ac… e9e6e9f…`: clean.
- **Additions.** `git diff --stat fad3ee4… e9e6e9f…`: 31 files, all under `qualification/ssds80/`, plus the Manual and one index line in `workplans/active/SSDP-6.1-7.0-WORKPLAN-AUTHORITY-INDEX.md`.
- **Frozen surfaces.** `orchestrator/docs/architecture.md`, `source/` and `dist/` are byte-unchanged from `fad3ee4`.
- **Optional extras:**
  - `tests.test_protocol_63_engineering_memory`: 28 tests, OK;
  - `PROJECT-ENGINEERING-MEMORY.md` identical to `main`;
  - the diagnostic model (above).
- **Scratch diagnostic.** One Git diagnostic showed that a gitlink bump changes only the `160000` entry while files read inside the submodule are absent from the superproject tree. That is a toolchain fact, not SSDS behavior.

Scratch files are under `$TMPDIR/ssds80-manual-review-e9e6e9f/` (`/tmp/claude-1000/…`).

**Not verified:**
- any SSDS implementation or runtime behavior (none exists);
- Git LFS behavior (not installed; B1 C rests on its documented attribute-driven filter);
- G3 costs;
- external or native issue homes;
- the full text of earlier Review records beyond their findings tables;
- whether every filesystem or checkout layer is covered; the family search stopped at characterization, as method step 6a allows.

## 11. Scientific-checks answers

This task reviews D3 authority for software that mediates scientific evidence. It produced, ran or reviewed no realized scientific results.

1. **Material findings.** My material findings are B1 and B2 (blockers) and N1-N5 (non-blocking) above. All are D3 architecture findings. I have no D1/D2 scientific or numerical findings and no out-of-scope scientific findings. I launched no agents. The tools I ran are listed in section 10, and none produced a finding beyond those stated.
2. **Realized results.** None produced, run or reviewed, and no gate evidence prepared, so no null envelope is owed. The unit tests, the diagnostic model and the scratch Git diagnostic are software and toolchain checks on documents and Git, not realized scientific results.
3. **Variants.** Yes, design and interpretation variants only; this was not result selection over data:
   - B1 repair directions: four options named, (a)-(d). Selection criterion for the recommendation: preserve the owner-required property with the least added mechanism (convergence owner, "Active simplification trigger").
   - B2 repair directions: two options (standing-keyed cap; one gate decision per gate and revision). Same criterion.
   - Two readings each of three clauses, kept as findings rather than resolved:
     - the LFS exception (attribute-driven or blob-determined);
     - the classifier owner (system version or analyzer);
     - §10.4's gate term (existential or conservative).
   - The diagnostic model was run in its default mode only.

   No data, held-out set or delegated search was involved. The recommendations are non-binding; the stakeholder chooses.
4. **Tension search.** Not triggered. I relied on no accepted D1/D2 authority for a consequential judgment. The judgments rest on:
   - accepted SSDP 7.2.1 protocol owners (D3, kernel, convergence, evidence, workflow);
   - the proposed workplan;
   - the stakeholder record.

   No scientific or numerical formulation is accepted for the SSDS product.

Gaps: none in these answers.

## 12. Common-mode note

I share the Manual author's model family (Claude). The authoring session launched me from a handoff it wrote. The corpus, the inherited workplan framing, the prior Review records (eleven of the twelve Manual Reviews same-family), the diagnostic model and the toolchain are shared dependencies. The 3540d98 and Phase B reviewers were of another family (GPT). Fresh context does not establish epistemic independence.

In particular, B1 A shows that the e2154ac record's own repair suggestion (treat a non-guaranteeing class "like a class that cannot observe its reads, failing closed") did not fail closed for passing evidence. The repair adopted it, and same-family review carried the error forward for one round. B2 likewise entered through the repair of a same-family non-blocking suggestion. The stakeholder reserves the choice of a final different-family confirmation.

## 13. D4 statement

SSDS 8 D4 is **not authorized**. This NO-PASS accepts no architecture, no proposed default and no product scope. G1 also requires a later independent PASS on a repaired candidate and explicit stakeholder acceptance. G2 requires a reviewed shadow D3->D4 workplan and explicit stakeholder authorization.

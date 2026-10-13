# SSDS 8.0 prospective architecture workplan — Independent D3 Review, Revision 21

    GOVERNING SSDP: 7.2.1
    REPOSITORY: hjin98/scientific-software-development-system
    BRANCH: ssds-8.0-graph-native-architecture
    CANDIDATE: ef8445a3bafb86086546ceff3eaa8b0171dbdb25
    SCOPE: whole proposed architecture; (a) the revision-21 simplification pass under the convergence owner:
           removal of the pair as a supersession record (Admission authorization, withdrawal latch, `here`,
           reading pair, Dispatcher run enumeration, decision-class pair exceptions, floor deferral); the
           derived test `stale_G` and its polarity rule; "in force at the base"; the reading ground of
           `IMMATERIALITY` (R2); the floor as an event on ledger facts; the deliberate staleness of mechanical
           failures after accepted relaxations; the execution-basis, external-read and attribution changes;
           the bounded model check with mechanical and assessor-read failures, a restorable tightened
           reading, four outcomes, owner-stated P13/Q/Q2, `--jobs` and `REV20`; (b) workflow execution and
           verification layer and the doctrine-realization objective; (c) persistence, derivation,
           concurrency and migration; (d) Protocol 7.2.1 inheritance reconciliation; plus the family-level
           convergence assessment the handoff requires (method step 5)
    PRIMARY WORKPLAN: workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
    PRIMARY WORKPLAN BLOB: 9db8178b5894b4518517aaf69819f3e556711916 (verified)
    GOVERNING PUBLIC SOURCE: aaeaf8b6b2121b9fb8aba31917c8265649c43954
    GOVERNING RECOVERY: efdd1b59a7592b1cecef0a0013c35b54a7a6315d
    HISTORICAL REPAIR SOURCE: SSDP 6.6, 22f4bdba53795da3a6f13f162529f3a843fc37ae
    PRIOR REVIEWS, HYPOTHESIS ONLY: F9D9DE8, 441CF5C, 8A75346, FFBAD17, F3608F5,
           AC71FA9, 730490D, FB3E542, 124B0B7, 97E753F, 4C35D92, 644EB72, 62C0B24,
           203A42B, A414588, 6FE1000, 4EC0024, BA7F738, 947370D; all NO-PASS
    REVIEW METHOD: immutable-owner reconstruction in the D3 role; the simplification attacked as a whole,
           with emphasis on what each removed mechanism had carried; prior-finding re-derivation;
           family-level convergence assessment; exact-candidate structural tests, whitespace check, the
           bounded model check in every requested mode, and a bounded probe of the model on the
           trajectories found here
    REVIEWER: Claude model family; a fresh-context sub-agent launched by the authoring session from
           REVIEW-HANDOFF-SSDS-8.0-REVISION-21.md (stakeholder SD-8); same model family as the author
    RECORD FILE: WORKPLAN-REVIEW-SSDS-8.0-EF8445A-NO-PASS.md

Candidate section references below mean the [primary workplan at the candidate][wp]. Governing-owner links pin the public source above. This context authored neither the candidate nor any prior Review, received none of the authoring conversation, and treated the handoff's scope description, the workplan's self-assessments (§0.1, §27.36-§27.37), the model check's green result and every prior verdict as hypotheses.

The blocker below is a deduction from the proposed contracts, not an observed SSDS runtime failure. Its trajectories are reproduced in the candidate's own bounded model, which returns the permissive value on them and whose owner-stated properties agree with that value (§1, §7). Its asserter is the reviewer named above; its disposition is **OPEN** against the exact candidate. This record is its canonical home. Revisit after the D3 owner has repaired the assessor-read branch of `stale_G` at §6.6, regenerated §0.1, §22, §26, §27 and the model check from the result, and frozen a replacement candidate. No accepted project scientific D1/D2 claim is challenged.

## SERIOUS CHALLENGE

**None against accepted governing authority.** The [kernel][kernel] says: “A coherent parent with a wrong child is an ordinary blocker.” The governing [evidence owner][evidence] is coherent and realizable for this concern:

- “A valid failing observation is evidence. A stale failing observation is not admissible evidence against current authority. A stale passing observation is not admissible confirmation.”
- “Use `review-required` when applicability is uncertain.”
- “Evidence only establishes claims its oracle and exercised semantic owner can discriminate.”
- “When competent evidence assessments materially conflict, preserve the disagreement and route adjudication to the governing claim/owner or obtain discriminating evidence. Do not resolve material assessment disagreement by majority vote, latest-editor order, reviewer seniority, count, temperature, or serialized record position. … An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.”

The [convergence owner][convergence] is coherent too. Its active-simplification rule says: “Add machinery only when a required capability genuinely remains absent or one canonical mechanism replaces broader existing complexity”. Its review strategy says: “A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign.” The blocker lies in the D3 candidate, which is proposed and not accepted. It is therefore an ordinary blocker.

The stakeholder record (blob `edbf40da…`, unchanged) supports what the workplan attributes to it under SD-1 to SD-8. One attribution in §0.1 and §27.36 is not in that record: that the stakeholder “further directed that revisions and Reviews be done in the D3 role under the 7.2.1 owners”. That instruction appears only as a paraphrase in the coordination file `SESSION-CONTINUATION-HANDOFF-SSDS-8.0.md` (N1 below). It changes no design decision. Nothing in the candidate claims that a sub-agent PASS accepts the architecture (§25).

## Verdict

**NO-PASS.** One blocker remains, **X**: for an **assessor-read** oracle, `stale_G` takes “a different evaluated outcome” as discriminating evidence that the frame's content does not yield the failure. It has three concrete members. Each is locally compliant, and each makes a stated guarantee of the candidate false.

- **X1 — a candidate failure that the admitted code also has disappears from the admitted state, with no judgment and no human item.** A reviewer fails a candidate on a defect that the admitted output shows too. The candidate's own change (a vectorization, a reordered reduction, anything on the numerical path) has shifted the low bits of the evaluated outcome. Once the reproduction is admitted, the admitted state's existing evidence run is “another outcome”, so the failure is stale there at once. The admitted claim stays `T` on its old passing assessment, and no floor event fires. That contradicts §6.6's “machinery never decides that a frame failure does not concern admitted content” and reopens `6fe1000` A2 for assessor-read oracles.
- **X2 — the later assessor wins after a perturbation.** This is `4ec0024` B′1 with low-bit drift instead of byte identity. An iteration, or an integrated refactor, perturbs the outcome without touching the defect. The earlier FAIL is stale on the bit difference, and any independent assessor's ordinary PASS of the new realization then closes the claim. No record ever reads the two outcomes under one reading. That is resolution by “latest-editor order”, and it falsifies §27.36's attack row “Make a real failure stale by a cosmetic change | (4) reads the outcome: an identical outcome yields it”.
- **X3 — the D1/D2 decision class and the system's own equivalence judgment are bypassed.** Take a D1/D2 failure of admitted content, followed by a change that alters the outcome. Its stop is now R0 plus an R2 PASS. Revision 20 had kept it R3 (`ba7f738` N3), so that closure is reopened. Where the change carries an admitted `EQUIVALENCE` judgment (“does not affect this consumer”), the old passing assessment stays current through it. The failure then becomes stale with **no new assessment at all**, on an outcome difference that the system's own judgment has declared immaterial. The floor item still latches for a failure of admitted content. But validity and discharge are `T` while it is open, which the evidence owner forbids (“An unresolved material disagreement keeps dependent present guidance/closure visibly qualified”).

The cause is single, so this is one blocker. A verdict function can say whether a new outcome yields a failure. Identity of an assessor-read outcome cannot, because only a reading can. Revision 20 carried that reading in condition 3, “one qualified assessor, independent of the claim's authors, records both readings in one assessment”, and kept the D1/D2 class R3 where a fix could be the admitted code's. Revision 21 removed both with the pair. §26 lists “lenient assessments of outcomes that differ from a failing one only cosmetically” as a residual. X1 and X3 need no lenient assessor, though, and X2 needs only a competent one who reads differently. That is the disagreement the owner requires to be preserved.

Revision 21 otherwise holds. W1 and W2 are closed on their trajectories, and so are 947370d N2, N3, N4 and N6. N5 is closed in part. The mechanical branch of `stale_G` survived every trajectory attempted here (§4). It is a genuine simplification: it removes a record special case, an Admission check, a latch, a custody enumeration, two class exceptions and a deferral, and it adds one derived test.

This is the twelfth consecutive NO-PASS on the §6.6 disagreement family. This time the defect does not sit where two repairs meet. It sits where the simplification removed a capability that the owner requires and that the removed machinery carried. The repair is subtractive (§1, §5). This Review does not hold that the family needs another redesign (§9).

Requested checks:

- The four routing tests pass, and `git diff --check` is clean.
- The model check is green at depth 4 (1,378,642 transitions, 68/68 discriminators) and at depth 5 (81,511,449 transitions, 0 failures, 68/68 discriminators).
- Every sensitivity mode is red on properties other than the oracle. `REV20=1` is red only on P10 and P13, both restated in revision 21 (§6).
- A bounded probe shows that the model returns `T` on X1, X2 and X3, and that its “owner-stated” `owner_stale` agrees, because it compares assessor-read outcomes by identity just as the candidate does.

None of these checks establishes semantic adequacy.

## 1. Blockers by earliest owner

### X — assessor-read staleness by outcome identity (members X1, X2, X3)

**Owner text at the candidate.**

- §6.6 `stale_G`: “(4) not yielded here: no admitted observation o with on(o, G), standing or not, yields a-'s failure on any failing output under G's reading”, where “yields a-'s failure on output x under G's reading: mechanical oracle — G's reading's verdict on x is FAIL; assessor-read oracle — o's evaluated outcome on x is a-'s”.
- §6.6, Where counting starts: “including a candidate's failure of an admitted test: machinery never decides that a frame failure does not concern admitted content.”
- §6.6, “Discrimination, not repetition”: “(4) reads the outcome itself: a rerun that yields the outcome `a-` failed, under `a-`'s reading, can never make it stale, even after a cosmetic change (`6fe1000` B1; `4ec0024` B′1). Interpretive disagreement over one outcome therefore goes to `a-`'s own assessor, the owner's adjudication or `IMMATERIALITY`.”
- §6.6, Decision class: “Staleness is not a decision: it is derived from designated-runner observations (R0).” §7.5 R3: “dispositions of a disagreement on a D1/D2 claim”.
- §6.6 floor: created only for “a failure of admitted content”, “one that an admitted observation of admitted content yields under the admitted reading”, nondeterminism in fact, or an `INCOMPLETE` scheduled execution, each “while it is not stale there”.
- §1.2: “mechanically decidable only conservatively -> deterministic machinery, answered by sound over-approximation (never under-approximation)”. §2 S4: a failing assessment keeps the claim qualified “until a judgment addressing it, or discriminating evidence, disposes of it”.
- §22: “These must remove the qualification: discriminating observations … with no record and no decision: for a genuine fix whose outcome flips, with a mechanical oracle and with an assessor-read one”.
- §27.36: “Make a real failure stale by a cosmetic change | (4) reads the outcome: an identical outcome yields it”.

**X1 trajectory (every step locally compliant).** D2 subject `s` with claim `c`: “the integrator conserves energy over 10^6 steps”. Specification `σ EVIDENCES c`, with an **assessor-read** oracle on the declared evaluated outcome, the energy series. No canonical form is declared; Manual item 5 makes one optional. The admitted code at `B` already shows a slow secular drift. An earlier assessor read it PASS (`a+`, current).

1. An implementer's candidate `X` vectorizes the force loop. The reduction order changes, so the energy series differs from `B`'s in the low bits, and the drift is unchanged.
2. The designated runner executes `σ` on `X`. An independent reviewer `Y` reads the drift and assesses FAIL (`a-`), naming the energy output.
3. `a-`'s obligation is admitted, so `a-` counts in the admitted state at once (`starts`). S3 schedules a reproduction on `X`'s retained tree. It is identical, so conditions (1) and (2) hold.
4. The admitted state's evidence run on `B`, which already supports `a+`, is a standing observation on admitted content, so (3) holds. Its series differs from `a-`'s in the low bits. Under the assessor-read clause it does not yield `a-`'s failure, so (4) holds. `stale_D(a-)` is true.
5. `adverse` is empty, `undisputed(s, e) = T`, and `current(a+) = T`, so `ev(s, e) = T` and `s` is valid. No floor event fires: `a-` is not a failure of admitted content, the admitted observation is not identical, nothing is nondeterministic and nothing ended `INCOMPLETE`. No adjudication obligation exists in the admitted state.

`Y`'s finding about behaviour of the admitted D2 code never reaches the owner or the human. It blocks `X`'s own lineage only while that lineage's frames reproduce it (X2).

**X2 trajectory.** Continue X1, or start from an admitted failure:

- *Within the lineage.* The implementer's iteration 2 (`X'`) makes another output-perturbing edit, such as a reassociated sum or an added diagnostic that changes the floating-point order, and leaves the drift. `a-` is stale in `X'`'s frame by the same four conditions. A fresh reviewer `Z` assesses `X'` PASS. The review brief carries `a-` only as stale evidence, and previous findings only “where policy may supply” them (§9.6). `X'` integrates unqualified.
- *Admitted.* For an admitted failure, an integrated refactor plays the same role. Any qualified, independent assessor's PASS of the new realization supplies `ev`.

No record reads `a-`'s reproduced series and the new series under one reading. `Y` and `Z` disagree materially about one behaviour. The later one wins because the bits differ. That is `4ec0024` B′1 (“The opposing side won by being later after a cosmetic edit”), with low-bit drift instead of byte identity. For assessor-read numerical outputs, low-bit drift is the normal effect of any change on the numerical path. So “(4) reads the outcome itself” protects only the byte-identical case.

**X3 trajectory.** D1 or D2 subject; failure `a-` of admitted content by an independent assessor or a human. The floor item is created at once and latches.

1. A refactor `r` arrives with an `EQUIVALENCE` judgment by a qualified, independent actor, of consumption class “does not affect this consumer”. It integrates, and its rerun shifts the low bits.
2. `a+` stays current through the equivalence path (§6.4, §6.7). The reproduction and the rerun make `a-` stale. `ev(s, e) = T`, with **no new assessment and no judgment about `a-`**.
3. Without the equivalence judgment the trajectory is the same, except that an R2 PASS of the new realization is needed (X2).

Either way:

- The D1/D2 disagreement is settled at R0 or R2. Revision 20 required R3 here: “A trial on later admitted content may carry a fix of a failure that the base already had, so such a pair stays R3 (`ba7f738` N3).”
- `valid(s)` and §7.4 discharge are `T` while the floor item is open. The design says that human unavailability leaves dependent work not ready (§9.8), but nothing here waits on the item.
- The equivalence judgment asserts that the change is immaterial to this consumer. Staleness treats the change as discriminating. Two of the candidate's own records contradict each other, and machinery chooses the permissive one.

**Bounded probe** (the candidate's model, unmodified, `REV21`). Each line gives `V`, `stale`, the model's own `owner_stale` and its oracle:

- `(PASS, FAIL(cand), EXEC(old, 1), EXEC(2))` (X1): `T / True / True / unqualified`;
- `(PASS, FAIL, MOVE, EXEC(old, 1), EXEC(3), PASS)` (X2): `T / True / True / unqualified`;
- `(PASS, FAIL, MOVE(equiv), EXEC(old, 1), EXEC(3))` (X3, no new assessment): `T / True / True / unqualified`;
- contrast, identical value: `P / False / False / qualified`.

The model has no notion of an outcome that differs in value but not in what the assessor's reading finds. Its “owner-stated” `shows` uses identity for assessor-read failures, exactly as the candidate does. P13, Q and Q2 therefore cannot flag X.

**What it violates.**

- The [evidence owner][evidence]: “Evidence only establishes claims its oracle and exercised semantic owner can discriminate”. For an assessor-read oracle, a bit difference discriminates nothing the oracle evaluates. Further:
  - “Use `review-required` when applicability is uncertain”: whether `a-`'s concern applies to a bit-different outcome is exactly what is uncertain;
  - “preserve the disagreement and route adjudication … Do not resolve material assessment disagreement by … latest-editor order”;
  - “An unresolved material disagreement keeps dependent present guidance/closure visibly qualified.”
- The candidate's own guarantees: §1.2 (an under-approximation of “yields” answered permissively); S4; the §6.6 sentences quoted above; and the §7.5 R3 row in substance (X3).
- The stakeholder's SD-2: a material D1/D2 discovery reported by a reviewer (X1) is decided by machinery instead of reaching the human.
- Earlier closures that §0.1 says were “held fixed”: `6fe1000` A2 (X1), `4ec0024` B′1 (X2) and `ba7f738` N3 (X3).

An implementer cannot satisfy the `stale_G` text and these guarantees together on these trajectories without choosing between them.

**Earliest owner.** D3 §6.6, the assessor-read clause of “yields” in `stale_G` and the decision class of what replaces it, with the §7.9 floor, §22, §26 and §27.36. Not Manual: §6.6 fixes the identity test explicitly, and §22 fixes the intended outcome (“with an assessor-read one … with no record and no decision”). Manual item 5's optional canonical form narrows X but does not remove it. Rounding only moves the boundary, and a different value that shows the same defect still differs.

**Minimum repair direction.** Subtractive, inside the revision-21 abstraction:

- **Restrict mechanical staleness to oracles with a verdict function.** For an assessor-read failure, “not yielded” is a reading, not an observation. Drop the identity clause. Let (4) hold for an assessor-read failure only where one qualified assessor, independent of the claim's authors, reads `a-`'s reproduced outcome FAIL and `G`'s observed outcome PASS under `G`'s reading **in one record**. That is revision 20's condition-3 form. Carried by the ordinary passing assessment of `G`'s realization, it needs no new record kind, no Admission pair check and normally no extra task.
- **Restore the class distinction that the removed exceptions carried.** That reading is R2. It is R3 where any subject is or has been D1/D2 and `a-`'s content was the admitted content at its base, or `G`'s content is later admitted content that may carry a fix of a failure the base already had (`ba7f738` N3). The reading-ground `IMMATERIALITY` keeps its R2 case.
- **Alternatively, remove assessor-read staleness altogether** and route those failures to `a-`'s assessor, the owner or `IMMATERIALITY`. §26 then carries the cost.

Either form removes mechanism. Neither restores the pair, the latch, `here` or the enumeration.

**Required discriminators**, through real Admission, Derivation, discharge and inspection consumers:

- **X1.** A candidate refactor that perturbs an assessor-read output's low bits; a reviewer FAIL on a defect the admitted output also shows; the item abandoned. The admitted claim stays qualified, with an adjudication obligation, and for D1/D2 a floor item, until a reading. Contrast: a genuine candidate-only failure (the admitted outcome reads PASS in the same record) becomes stale at R2, with no human item.
- **X2.** An iteration perturbs bits and leaves the defect; a fresh reviewer PASSes. The lineage stays qualified until one record reads both outcomes. Contrast: the same with a mechanical oracle becomes stale with no record.
- **X3.** A D1/D2 failure of admitted content, then an equivalence-covered, output-perturbing refactor. The claim stays qualified until an R3 reading. Contrast: a mechanical D1/D2 failure fixed by an outcome that the admitted reading passes becomes stale at R0.
- **In the model.** Give assessor-read outcomes a materiality partition that only a recorded reading reveals, for example values 1 and 3 materially equal. Restate `owner_stale` for assessor-read failures as “a recorded single reading discriminates”. That way P13, Q and Q2 stop encoding the identity choice under test.

## 2. Non-blocking findings

### N1 — stakeholder-instruction provenance remains partly evidenced

- `f3608f5` N1 is unchanged: the 2026-10-12 adoption instruction is paraphrase-only (§0.4; stakeholder record, “Not covered”).
- New: §0.1 and §27.36 attribute to the stakeholder an instruction that “revisions and Reviews be done in the D3 role under the 7.2.1 owners”. It is recorded only as a paraphrase in the coordination file `SESSION-CONTINUATION-HANDOFF-SSDS-8.0.md`, not in the stakeholder decision record. It changes no design decision.

Earliest owner: §0.1, §0.4, pending stakeholder restatement.

### N2 — the polarity rule omits the judgments that bound an observation's execution basis

`stale_G`'s permissive inputs must “stand”, but standing means only `cont` and no blocking challenge on the observation's realization. Whether an observation is `on` a frame is decided by the content identities its basis recorded. Where a `COMPLETENESS` judgment narrowed that basis (§6.5; it is a `record` entry of the realization, §6.4), a later upheld challenge against the judgment leaves the observation “on” every frame that matches its narrow basis. That includes a frame that differs in a file the execution actually read. Passing currency fails closed on that revocation. Staleness does not, so the candidate's own rule (“everything that can make a failure stale must stand”) is not met.

The trajectory is narrow. It needs a wrong completeness judgment, its revocation, and no later run of the failing configuration on the frame. It is restrictive in the other direction, because a yielding run on the frame keeps the failure counting. Hence non-blocking.

Repair: a permissive use of an observation also requires every judgment that bounded its recorded basis to stand; otherwise read the basis as the whole tree. Earliest owner: §6.6 standing; model P6, which checks only “never raises”.

### N3 — the deliberate relaxation change rests on an unguaranteed premise

§0.1 and §6.6 justify mechanical staleness after an accepted relaxation by “the accepted revision's own review saw the failure labelled `disputed`”. In the relaxing candidate's frame, `G`'s reading is the relaxed one, so the failure is already stale there once the frame's run exists. After an absorbed foreign relaxation it is stale in the admitted state before any acceptance, because `G`'s reading is the observed specification. Neither review is shown the failure as `disputed`, and §7.7 treats widened tolerances as `HEURISTIC` only. This is owner-conformant in outcome, because the failure applied a revision no longer in force once the relaxation is accepted, and no permissive validity effect precedes acceptance.

Repair: make the counted mechanical failures that a specification change would make stale a required item of that change's review brief (E2), or define “`G`'s reading” for staleness as the accepted specification revision. Earliest owner: §6.6, §9.6; §26 already carries the rate.

### N4 — reading-ground `IMMATERIALITY` for D1/D2 is R2, with no human item (947370d N5, partly closed)

Admission's precondition, “`a-`'s reading was not in force at its base”, is met by any byte change to the claim unit in the frame, including an editorial one. The floor's second event excludes this case. A D1/D2 concern about admitted behaviour, voiced in a frame that touched the claim text, is therefore retired at R2 with no floor item. The “names the material difference” requirement is a judged slot (E3), not a mechanical check. The disclosure in §26 is adequate for a non-blocking residual. Consider keeping the floor event for D1/D2 where the admitted observation is identical. Earliest owner: §6.6 decision class, §7.9.

### N5 — residual prose that does not mention staleness (editorial)

The §10 table's assessment row and §7.4's discharge comments still say that a counted failure and a passing assessment “are a disagreement, which counts until a standing disposition”. They do not mention that `stale_G` also ends counting. §6.6 governs. Regenerate those lines from it.

## 3. Re-verification of previous Reviews' findings

“Closed” means the named deductive trajectory is excluded by the candidate's contract, not executed qualification or acceptance.

### 947370D

| Finding | Disposition | Basis |
|---|---|---|
| W1 once-admitted, relaxed reading restored by a candidate | **Closed** | Mechanical: the verdict under `G`'s reading passes the admitted outcome, so the failure is stale once reproduced. Assessor-read: reading-ground `IMMATERIALITY`, whose precondition is “not in force at the base”. Model discriminators |
| W2 mechanical reading pair judged under the failure's reading | **Closed** | The verdict is always read under the frame's reading. An output shift within the admitted tolerance keeps the failure stale. Model discriminator and contrasts |
| N1 adoption provenance | **Partly closed** | Unchanged; widened by the new attribution (N1 above) |
| N2 floor event or state; never created without a pair | **Closed** | An event on four ledger facts; nondeterminism in fact creates it |
| N3 whole-tree basis forced by any marker; unpinned external reads | **Closed** | A marker blocks only analyzer completeness; an unpinnable read fails closed. Related new gap: N2 |
| N4 an earlier disposed failure forbade reading pairs | **Closed** | Removed with condition 5 |
| N5 reading pair retired a concern voiced under an editorial variant | **Partly closed** | The judgment must name the material difference; no floor item (N4 above) |
| N6 attribution of resubmitted never-lost bytes | **Closed** | §6.8 step 3: the envelope is transport, and the original actor and lineage class are kept |

### Earlier Reviews

The `947370d..ef8445a` diff touches:

- the workplan: §0, §0.1, §6.6, §6.8 step 3, the §7.5 R3 row, the §7.9 floor, §10, a §21 item, §22, §26, §27.36-§27.37 and §28;
- three lines of the authority index;
- the model check, the continuation handoff, and two added qualification records (the revision-20 handoff and the `947370d` Review).

No earlier Review record, `source/`, `dist/`, `orchestrator/`, test, release-state, PEM, stakeholder-record or archived-predecessor path changed. This was verified by `git diff --name-status`, hunk positions and blob identities.

- **4EC0024.**
  - B′1: **closed** for byte-identical outcomes; **reopened** for assessor-read outcomes perturbed by the change (X2).
  - B′2: **closed**, because conditions (2) and (4) read every admitted observation, whatever its standing.
  - C1: **closed**, because standing is per frame and a revert yields.
  - C2a-C2c: **closed**, because the start latch is kept.
  - N1-N8: as recorded at `947370d`.
- **6FE1000.**
  - A1 and A3: **closed**.
  - A2: **closed** for editorial reading changes and for mechanical oracles; **reopened** for assessor-read failures whose candidate change perturbs the evaluated outcome (X1).
  - B1 and B2: **closed**; a superseder that is neither own nor owner is refused at step 3.
- **BA7F738.**
  - U1a, U1b, U1c, U2a and U2b: **closed** on their trajectories.
  - N2: its accepted residual (assessor-read identity) is now the cause of X.
  - N3: **reopened** (X3).
  - N4-N7: **closed** or superseded by removal.
- **A414588 A1-A3 and B, 203A42B A and B, 62C0B24 A, 644EB72 A and B, 4C35D92 A, 97E753F A, B1 and B2, 124B0B7 A, FFBAD17 A, FB3E542 A: closed.**
  - `home`, the anchor sets, authorship fail-closed, `qual` over retired obligations, `IMMATERIALITY` currency and `bind(j)` are unchanged.
  - The `644eb72` B case (removing a check in force at the base) is preserved by the “either” clause of “yields”.
  - `4c35d92`'s assessor-read reading change still raises reassessment when the outcome is identical. Mechanical relaxations are the declared deliberate change (N3).
  - FB3E542 B: **partly closed**, through X.
- **Strata.**
  - `stale` reads S0 observations and S1 standing (`cont`, the challenge status of realizations), so it is a constant in S2.
  - `undisputed` stays monotone, and S2 keeps its unique least fixed point.
  - S0 and S1 are unchanged. The floor event is S3 and does not affect the single value of `D_n`.
  - The strata stay well-founded and single-valued.
- **“Impossible” claims.**
  - “a rerun that yields the outcome `a-` failed … can never make it stale, even after a cosmetic change” is true only for byte-identical outcomes and is false in substance for assessor-read numerical outputs (X2).
  - “machinery never decides that a frame failure does not concern admitted content” is false for assessor-read oracles (X1).
  - “no run can be hidden from (2) or (4)” holds.
  - “runs on other content never delay anything” holds.

The remaining 730490D, AC71FA9, F3608F5, 8A75346, 441CF5C and F9D9DE8 closures do not depend on the changed text and remain **closed**. FFBAD17 N7 (inherited index and whitespace residue) remains outside this scope.

## 4. Out-of-matrix trajectories attempted

| Attempt | Result |
|---|---|
| Candidate refactor perturbs an assessor-read output; reviewer fails a defect that the admitted output also shows | **Fails** (X1); reproduced in the model |
| Iteration perturbs bits; fresh reviewer passes | **Fails** (X2) |
| D1/D2 failure of admitted content; equivalence-covered, output-perturbing refactor | **Fails** (X3); `T` with no new assessment, in the model |
| Same three trajectories with a mechanical oracle | Hold: the verdict function decides, and a perturbation that the reading still fails yields |
| Byte-identical rerun after a comment-only change (`4ec0024` B′1 as written) | Holds |
| Mechanical test-first tightened tolerance, abandoned; later output shift within the admitted tolerance (W2) | Holds: stays stale; contrasts count |
| Once-admitted, relaxed reading restored and failed (W1), mechanical and assessor-read | Holds: stale; R2 reading-ground judgment |
| Tightened reading later integrated after a stale mechanical failure | Holds: yields again |
| Revert of a fix outside the named content | Holds: yields again |
| Unrelated candidate run on other content (U1b) | Holds: not `on` the frame |
| Nondeterminism on the failure's own content, before or after staleness | Holds: (2) fails; floor event for D1/D2 |
| Pre-loss reproduction or observation; observation under an overridden blocking challenge | Holds: not standing, so nothing is made stale |
| Yielding observation that is challenged or from before a loss boundary | Holds: read whatever its standing (restrictive; a later-discredited one keeps counting, which §26 discloses) |
| Revoked completeness judgment behind an observation's narrow basis | Partly holds (N2) |
| Accepted relaxation of a mechanical specification; absorbed foreign relaxation | Owner-conformant once accepted; the review premise is unguaranteed (N3) |
| Editorial claim edit in a frame, D1/D2 failure of admitted behaviour, assessor-read | Never stale (identity); R2 reading-ground judgment with no floor item (N4) |
| Specification with no declared evaluated outcome; unpinnable external read | Holds: fails closed to the owner |
| External custody runner without run enumeration | Holds: makes nothing stale |
| Resubmitted refused never-lost bytes | Holds: original actor and lineage class kept |
| Non-independent or unauthorized `supersedes` | Holds: refused at step 3 |
| Workflow layer, publication, frame enactment, intake, migration and recovery trajectories of earlier records | Hold as recorded; that text is untouched by revision 21 |

## 5. Minimum-architecture and capability-transfer assessment

**Minimality.** Revision 21 adds no primitive, record kind, store or component (§27.37). In the §6.6 family it is a genuine net simplification, and for mechanical oracles it reaches what this Review judges to be the minimum justified concretization of the evidence owner: one derived per-frame test over admitted observations, with the polarity stated once. It went one step further than the owner allows. It removed a **required capability**, the discriminating reading for oracles without a verdict function, together with the compensating machinery. The convergence owner keeps machinery that supplies a capability that “genuinely remains absent” otherwise. The repair in §1 restores that capability as a property of an existing record (the passing assessment) and adds no machinery.

**Capability transfer** (§18, PEM). The removed pair carried four capabilities:

| Capability | Where revision 21 carries it |
|---|---|
| Identical outcomes never discriminate | Condition (4) |
| Nondeterminism goes to the owner | Condition (2) |
| A revert re-counts | Per-frame (3) and (4) |
| An assessor-read stop needs one independent reading of both outcomes, at R3 for D1/D2 admitted-content fixes | **Nowhere** (X) |

The §27.36 table lists the first three and omits the fourth. That is the capability-transfer gap the architecture owner warns about: “do not drop an authority-bound capability merely because the old mechanism is ugly or because a new implementation appears simpler”. The capability is bound by the evidence owner's discrimination and disagreement rules. It is not an `EVIDENCE_ONLY` lesson.

**Predecessor comparison.** Revision 21 did not touch §16.2 or §18. Blobs verified at the candidate, equal at `947370d`:

| Predecessor | Blob |
|---|---|
| befe678 hypothesis archive | `af9c005b15c4d0cfc56b0efb4dfe6b032fa4d958` |
| Consolidated Protocol 8 plan archive | `cc795f4058f99041c751c97ce46e7bcf5483ec9e` |
| Orchestrator Architecture 1.6.0 (equal at public source and candidate) | `39e6de727f6c35402962509d30d947962992eaad` |

The bounded semantic comparison of §16.2 and §18 recorded by earlier Reviews still holds by identity.

**PEM basis and HAS.** Project instructions designate `main` as the integrated publication line. `git ls-remote origin refs/heads/main` gives `af0455753e20ee54a969c844872e29e270007211`, which equals the workplan's basis. Its `PROJECT-ENGINEERING-MEMORY.md` blob equals the candidate's, `1561797125622f355f84eb27319f87e8fa4227d9`. There is no branch overlay. Missing coverage proves no absence.

```yaml
pem_basis:
  accepted_project_state: af0455753e20ee54a969c844872e29e270007211
  accepted_pem: PROJECT-ENGINEERING-MEMORY.md@1561797125622f355f84eb27319f87e8fa4227d9
  candidate_overlay_semantic_candidate: NONE
has:
  - id: DS-001
    disposition: APPLICABLE
    reason: The model is green at depth 4 and 5 with 68/68 discriminators while X holds. Its owner-stated owner_stale and shows compare assessor-read outcomes by identity, as the candidate does, so P13, Q and Q2 cannot see X (probe, section 1). Section 22 expects an assessor-read outcome flip to remove the qualification with no record, and has no case of a perturbed but materially equal outcome.
  - id: PC-001
    disposition: APPLICABLE
    reason: Frozen profiles required through the versioning owner; preserved by section 24; untouched by revision 21.
  - id: SP-001
    disposition: APPLICABLE
    reason: Evidence-only analogy. Repair at the owning D3 rule (section 6.6) and regenerate sections 0.1, 22, 26, 27 and the model from it.
  - id: SP-002
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: Self-reference-safe identity unchanged by revision 21.
  - id: FF-001
    disposition: NOT_MATERIAL_TO_FINDINGS
    reason: No immutable publication in scope; it remains applicable to later genesis and release.
```

**7.2.1 reconciliation (scope d).** The release state at the candidate names 7.2.1 accepted-current, with public source `aaeaf8b6…` and recovery `efdd1b59…`, matching the handoff. `source/PROTOCOL_VERSION` is 7.2.1 at the public source. The diff changes no §0.4, §19 or §24 text, and no `source/`, `dist/`, `orchestrator/`, release-state or PEM path. The §0.4 obligation table and the §19 landing points therefore stand. The inherited evidence doctrine is not yet realized at X.

**Workflow layer and doctrine realization (scope b).** §7.5 changed only in its R3 row and §7.9 only in its disagreement floor. The rest of §7.5-§7.10 and §9.6-§9.8 is unchanged, and earlier closures there stand. The floor-as-event rule is sound as an event (947370d N2 closed). X shows one place where SD-2's “deterministic flow of important discoveries … to the human inspector” is not realized: a D1/D2 reviewer's discovery about admitted behaviour, made in a candidate frame (X1). §1.1 claims only what mechanism and evidence establish, consistent with SD-6.

**Persistence, derivation, concurrency, migration (scope c).** Untouched apart from §6.6 and §10. The strata assessment is in §3.

## 6. Qualification-program adequacy

§22's disagreement group carries W1, W2, U1, U2 and the B′1 contrasts. It cannot discriminate X. Its only B′1 case uses “a rerun whose evaluated outcome equals the failing one”. It requires that “a genuine fix whose outcome flips … with an assessor-read one” remove the qualification “with no record and no decision”, and it has no case in which the outcome flips while the assessor-read defect remains. A fixture suite built from §22 would be green with X present.

The [testing owner][testing] asks: “What is the smallest plausible semantically wrong concretization that could still pass this evidence?” Revision 21 as written is one for X.

The model check's sensitivity is real but partly self-referential again:

- `REV20=1` fails only P10 and P13. P10's `discriminates` and P13's `owner_stale` were restated for revision 21 and encode its choices: the reading in force when admitted, and identity for assessor-read outcomes. They detect W1 and W2, which were genuine, and therefore measure the old rule's distance from the new rule as well as from the owner.
- The earlier modes fail long-standing properties (P7, P9, P11, P12, Q, Q2), so their sensitivity stands.
- `owner_stale` is written without calling the candidate's predicates, but it makes the same semantic choice at the one point where X lives. Independence of code is not independence of semantics (DS-001).

Add the discriminators named in §1, and the materiality partition for assessor-read outcomes in the model.

The four consolidation tests establish frontmatter and routing only. HARD-template thresholds, mutation strength, evaluator calibration, custody, blinding, paired baselines and doctrine-realization measurement remain later-gate obligations (§22-§25). No campaign was run and no improvement estimate is asserted.

## 7. What was verified and how

- **Candidate identity.** Resolved the candidate SHA and the workplan blob `9db8178b…`, matching the handoff. Extracted a `git archive` of the exact candidate into a scratch subdirectory. Later commits, including the handoff commit `19654e8`, were excluded.
- **Governing source.** `aaeaf8b6…`, `efdd1b59…` and `af045575…` were present. `22f4bdba…` was fetched by SHA (`git fetch --depth=1`) into the object store only; no ref or working file changed.
- **Owners read** at `aaeaf8b6` with `git show`:
  - the D3 role entrypoint (`software-design/SKILL.md`: routing, D3 design contract, Independent Review and Challenge, Completion);
  - architecture, read first in full (learned-capability binding, mechanism-to-capability transfer, simplicity and recurrence, Review);
  - evidence, in full;
  - convergence: core progression, active simplification trigger, review readiness, review strategy after recurrence;
  - workflow: Review and optional independent cognitive trajectories;
  - testing: the smallest plausible wrong concretization;
  - the kernel's Challenge text;
  - PEM entries by identifier.

  Release identities were resolved from `PROTOCOL-RELEASE-STATE.yaml` at the candidate.
- **Candidate read.**
  - In full: §0-§0.1 (revision 21 record), §1-§2, §6.4-§6.6, §6.8, §7.4-§7.10, §9.3-§9.8, §10, §22's disagreement and model-check items, §26, §27.36-§27.37 and §28.
  - The `947370d..ef8445a` diff hunk list; the revision-20 pair text at `947370d` for comparison (conditions 1-5 and the decision class); the authority-index diff; the stakeholder record; the model-check source in full.
- **Unit tests.** `python3 -m unittest tests.test_protocol_80_orchestrator_consolidation -v` in the archive: **4 passed, 0 failures**, Python **3.13.16**.
- **Whitespace.** `git diff --check 947370d3… ef8445a3…`: **exit 0**, no diagnostics.
- **Model check**, depth 4, `--jobs 4`, 1,378,642 transitions in every mode:

  | Mode | Failures | By property | Discriminators differing | Exit |
  |---|---|---|---|---|
  | default `REV21` | 0 | — | 0 (68/68 as expected) | 0 |
  | `REV20=1` | 5,357 | P10 1,467, P13 3,890, O 0 | 9 | 1 |
  | `REV19=1` | 11,001 | P10 130, P13 10,831, P14 40, O 0 | 15 | 1 |
  | `REV18=1` | 13,181 | P10 1,058, P11 24, P12 2,120, P13 9,979, O 0 | 17 | 1 |
  | `REV17=1` | 106,061 | P9 25,777, P10 71,066, P11 192, P12 6,072, P13 2,954, O 0 | 20 | 1 |
  | `REV16=1` | 116,171 | P7 504, P9 25,721, P10 68,884, P12 6,120, P13 2,858, Q 5,056, Q2 300, O 6,728 | 23 | 1 |
  | `REV14=1` | 126,747 | P7 988, P8 1,072, P9 25,665, P10 66,016, P12 6,168, P13 2,632, Q 9,988, Q2 874, O 13,344 | 24 | 1 |
  | `REV13=1` | 294,863 | P7 14,724, P9 23,817, P10 64,004, P12 5,903, P13 2,632, Q 64,726, Q2 12,241, O 106,816 | 26 | 1 |
  | `REV12=1` | 300,356 | P5 329, P7 14,724, P9 23,797, P10 61,099, P12 5,923, P13 2,586, Q 68,455, Q2 12,577, O 110,866 | 29 | 1 |
  | `REV11=1` | 311,152 | P7 14,724, P9 24,049, P10 68,977, P11 216, P12 5,557, P13 2,954, Q 66,294, Q2 12,197, O 116,184 | 33 | 1 |
  | `REV10=1` | 312,058 | P1 3,352, P7 14,724, P9 23,833, P10 68,977, P11 216, P12 5,887, P13 2,954, Q 61,618, Q2 12,121, O 118,376 | 31 | 1 |

  Every mode fails properties other than the oracle, and the totals match §27.36.
- **Model check**, depth 5, default mode, `--jobs 4`: **81,511,449 transitions, 0 failures, 68/68 discriminators, exit 0** (74 min 4 s on a shared host), matching §0.1 and §27.36.
- **Probe.** The candidate's own `Ledger`, `owner_stale`, `reproduced_now` and `oracle_unqualified`, loaded unmodified from the archive (§1). The probe script lives in a scratch subdirectory and is not part of the record.
- **Identities.** Verified the predecessor blobs, the release-state identities, the PEM blob at the candidate and at `af04557`, the stakeholder-record blob `edbf40da…`, the test blob, and the changed-path list, at both `947370d` and the candidate.
- **Repository untouched.** No candidate, source, distribution, index, release state, PEM or frozen resource was changed. The only repository output is this record. Nothing was committed or pushed.

**Scientific inquiry envelope.** Examined architecture-mediated evidence applicability, oracle kinds, staleness, readings, decision classes and escalation. Materiality here is the ability to change support, closure, human routing or the next authorized action. No physical or numerical result is asserted; the energy-drift example is illustrative. One pinned candidate was reviewed through multiple deductive trajectories and one model probe. No variant search over scientific analyses was performed, and no delegates were launched. The judgment relies on accepted engineering, evidence, workflow and convergence doctrine, not on project D1/D2 authority, so the tension-search duty was not triggered.

## 8. What could not be verified

- **PEM schema validation** was not rerun. The PEM blob is unchanged since earlier Reviews. This is not a pass.
- **Remote state** was read once by `git ls-remote`. No further remote-state claim is made.
- **Readings and Manual compositions.**
  - X assumes that an assessor-read specification declares an evaluated outcome without a canonical form, or with one that a perturbation can cross. Manual item 5 makes the form optional. A canonical form that erased every perturbation would also erase genuine fixes, so it cannot be the repair.
  - X1 assumes that the admitted state's existing evidence run is an observation `on` admitted content. §6.6's “normally no new trial” says it is.
  - X2's lineage variant assumes that policy does not supply the previous review's findings (§9.6 “may”). Supplying them informs the new reviewer but does not make the stop a reading.
- **The §1 repair** is a direction, not a verified design. Its equivalence on the trajectories that defeated revisions 10-20 is the owner's to establish.
- **Runtime evidence.** No SSDS production owner, witness deployment, harness adapter or Architecture Manual exists. Runtime fidelity, read recording per harness, failure injection, lineage attestation, privacy enforcement, scaling and burden reduction remain unexecuted (§21-§26), and none is counted as a pass.
- **Repository acceptance.** The full repository regression, package build and validation, distribution parity, frozen-resource census and Core snapshot tests were not rerun. This Review changes no protocol source or descendants.

## 9. Family-level convergence assessment (method step 5)

**(1) Did the simplification reduce the failure surface or move it?** For mechanical oracles it reduced it. W1 and W2 dissolve rather than being patched. Every predicate that two earlier repairs had to agree on (pair formation, `here`, the reading pair, the withdrawal latch, “ever admitted”) is gone. No mechanical-oracle trajectory survived here (§4). For assessor-read oracles it moved the surface. The pair's condition 3 was the one element that supplied discrimination where no verdict function exists. Revision 21 replaced it with outcome identity, which is a proxy. Revisions 10-16 each fell to a proxy for “failing evidence that may still apply” that was permissive somewhere; identity is permissive wherever an outcome changes without its defect changing.

**(2) Is it the minimum justified concretization?** Nearly. The minimum is revision 21 with the assessor-read branch of “yields” replaced by a recorded single reading, or removed (§1). That removes text, adds no record kind, and keeps every simplification revision 21 made.

**(3) Is the family still recurring?** Yes, for the twelfth consecutive cycle. The pattern has changed, though. Since revision 18 each defect sat where two repairs met; X sits where a removal dropped a capability. The convergence owner's caveat now applies: “A clean local repair that genuinely closes the cause remains sufficient; recurrence does not automatically force redesign.” This Review routes X at family level, as the oracle-kind question across every stop of the family (stale, the floor events, the decision class), and does not call for another redesign of the disposition abstraction.

**(4) Common-mode causes still present.**

1. **A same-family Review's proposal adopted with its blind spot.** The `947370d` Review's §5 outline proposed staleness where an observation “differs from `a-`'s outcome on the failing outputs”. It asserted that “the lenient-assessor residual is the same as the candidate's assessor-read `here` today”. That was not so: revision 20's `here` judged standing only after a one-record dual reading had formed the pair. Revision 21 adopted the identity test. This is cause 1 of that Review's list, recurring.
2. **The qualification instrument shares the rule's semantic choice.** `owner_stale` and `shows` compare assessor-read outcomes by identity, so the green result and the “owner-stated” P13, Q and Q2 coexist with X (DS-001).
3. **Framing.** This Review's handoff lists “(mechanical verdict or assessor-read identity)” among the items to re-verify, which presents identity as given. §27.36's attack table asks “cosmetic change” only in its byte-identical form.
4. **Verification on motivating trajectories.** §22 adds the `947370d` trajectories and their contrasts. The assessor-read branch was tested only on genuine fixes.
5. **Shared model family, corpus and toolchain** between the author and every Review since revision 11 (SD-8), and a scratchpad shared with the authoring session (§10).

## 10. Common-mode dependency

This reviewer is a fresh-context sub-agent **of the same model family as the author** (Claude), launched by the authoring session from a handoff the author wrote, under stakeholder SD-8. That is a material common-mode dependency. Shared blind spots, framing inherited from the handoff's scope list, and the same corpus and toolchain are all plausible. The [workflow owner][workflow] says: “Separate context improves process independence but not epistemic independence when agents share model, source corpus, toolchain or oracle”. §9 item 1 shows the dependency concretely: the blocker sits in wording that the previous same-family Review proposed. The repair direction in this record carries the same risk.

The scratchpad directory provided to this sub-agent is shared with the authoring session, and it already held the author's files. This reviewer read none of them. It wrote its own outputs in its own subdirectories, and two files at the scratchpad root (`wp.diff`, `wp20.md`, a diff and a `git show` of the revision-20 workplan). If files of those names existed before, they were overwritten; no other file there was read or changed.

The handoff gave no author conclusions. This record supplies **no different-family corroboration**. The design's own §9.6 lets policy require it for high-consequence surfaces, and the stakeholder has waived it for this cycle. A PASS from this cycle would still need owner adjudication and the production evidence of later gates ([workflow, Optional independent cognitive trajectories][workflow]).

## 11. D4 statement

**D4 remains NOT AUTHORIZED.** Phase B Review is NO-PASS. The next step is the owning D3 repair:

- repair the assessor-read branch of `stale_G` and the decision class of what replaces it at §6.6 (§1), keeping the revision-21 simplification;
- regenerate §0.1, §22, §26, §27 and the model check from the result, with a materiality partition for assessor-read outcomes;
- freeze a replacement immutable candidate.

Even a later Phase B PASS authorizes nothing by itself:

- G1 needs the accepted Manual and explicit stakeholder acceptance of the major change.
- G2 needs a separately reviewed shadow workplan and stakeholder authorization.
- G3 needs real-owner implementation evidence.
- G4 adds per-subject cutover, quiescence and rollback (§23-§25).

This Review grants no Manual acceptance, implementation permission, spend release, cutover, ratification or promotion.

[wp]: https://github.com/hjin98/scientific-software-development-system/blob/ef8445a3bafb86086546ceff3eaa8b0171dbdb25/workplans/active/SSDS-8.0-GRAPH-NATIVE-DETERMINISTIC-ORCHESTRATION-ARCHITECTURE.md
[kernel]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/abstraction-and-concretization.md
[evidence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/evidence-evolution-and-dependencies.md
[workflow]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/workflow-and-workplans.md
[testing]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/testing-and-validation.md
[convergence]: https://github.com/hjin98/scientific-software-development-system/blob/aaeaf8b6b2121b9fb8aba31917c8265649c43954/source/shared/references/convergence-and-cycle-economy.md

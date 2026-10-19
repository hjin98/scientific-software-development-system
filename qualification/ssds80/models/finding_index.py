"""Build the G2 Stage S step S4 finding index from the SSDS 8 Review records.

Governing SSDP version: 7.2.1. Coordination evidence: an index, never a disposition by itself.

For every Manual and workplan Review record under qualification/ssds80/, extract each heading-level
finding (B<n>, N<n>, SC-<n>, Blocker <X>, ...), its title line and the section references its text
cites, and route it to the catalogue section that owns it (its first cited §n, else the record's
most-cited section). Findings already reproduced by the S1-S3 design models are marked with the model
case that reproduces them (MODELLED below, stated by hand from the records). Everything else is
OPEN with its owning section, to be judged when S5 settles that section.

Run: python3 -I qualification/ssds80/models/finding_index.py > qualification/ssds80/G2-S4-FINDING-INDEX.md
"""

from __future__ import annotations

import collections
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (record short id, finding id) -> the S1-S3 model cases that reproduce it, stated by hand
MODELLED = {
    ("9431629", "B1"): "S1 item cases empty_redispatch, partial_redispatch, all_empty, kept_part_repartition",
    ("F044820", "B1"): "S1 author_owner_* (seven target kinds), human_adverse_author; S2 author_owner_waits",
    ("8C1F2F2", "B1"): "S1 author_owner_* invariant check; unknown_lineage_owner_agent",
    ("E810508", "B1"): "S2 same_key_in_scope_after_issue, same_key_other_scope_after_issue",
    ("E810508", "B2"): "S1 item cases (an item-level target and entries)",
    ("47B9F77", "B2"): "S1 objection cases (independence of integrated-result reviews)",
    ("B365947", "B1"): "S3 routing cases (RR-4 to RR-8, SD-41 residual)",
    ("085C979", "B1"): "S2 transformation cases (one judged content at roles, reach and denial)",
}

# (record, finding) -> (disposition, note), written by hand during S5 after reading the finding against
# the catalogue section and the accepted Manual. Dispositions:
#   CLOSED-BY-SEED     the settled mechanism closes it; the named mutation of the earlier diagnostic
#                      re-introduces the defect and is caught (RR-10 limits that evidence)
#   CLOSED-ARCH        closed at the architecture level by the accepted Manual's text
#   CLOSED-S2-S3       closed by a Stage S register row (the row names the evidence)
#   COST               a disclosed cost or stakeholder trade-off, accepted at G1 (SD-50), not a defect
#   NA-SD47            wording, citation or residue in a superseded candidate's text, rewritten at SD-47
#   NA-RR10            the earlier diagnostic's construction, now register entry RR-10
#   NA-LATCH           a mechanism withdrawn (R15's latch, SD-36)
#   A3 / A4            restored to the Manual by amendment A3 (proposed) / to restore in a later A4
#   STAGE-D            closed at the architecture level, carried as a Stage D real-owner discriminator
#   CLOSED-S5          closed by a Stage S step S5 model case (named)
#   CLOSED-PHASE-B     a workplan finding closed in the workplan before its Phase B PASS (e23f142),
#                      whose re-verification covers it; the catalogue realizes the reviewed contract
DISPOSED: dict[tuple[str, str], tuple[str, str]] = {}


def _d(rec, ids, disp, note):
    for i in ids.split():
        DISPOSED[(rec, i)] = (disp, note)


# §1
_d("3540D98", "B4", "CLOSED-S2-S3", "§1.4 row; S5 §1 equal_sibling_regions")
_d("B46C250", "N6", "CLOSED-S2-S3", "§1.4 row; S5 §1 nested_non_member")
_d("5C55D4B", "B2", "CLOSED-S2-S3", "§1.2 write-set row; S5 §1 span_shift_not_a_change")
_d("CC005DB", "B1", "CLOSED-S2-S3", "§1.2 write-set row; S5 §1 governed_boundary, new_part_over_existing_bytes")
_d("D837363", "B4", "CLOSED-S2-S3", "§1.2 write-set row; S5 §1 concurrent_admission_not_counted, combination_effect")
_d("3540D98", "B1", "STAGE-D", "Manual §1.5 one representation; runner materialization test")
_d("E2154AC", "B1", "STAGE-D", "Manual §1.5 one representation; runner materialization test")
_d("E9E6E9F", "B1", "STAGE-D", "Manual §1.5, §17.5; realization currency reads the recorded representation")
_d("6FF4ED1", "B3", "CLOSED-ARCH", "Manual §5.9 analyzer set pinned by the ruleset")
_d("6FE1000", "N5", "COST", "Manual §32.2 broad authorship fails closed")
# §2-§4
_d("34803DF", "N3", "CLOSED-ARCH", "Manual §2.6 analyzer identity a currency condition")
_d("29DA56E", "N3", "CLOSED-ARCH", "Manual §3.5 floors include the R3 chain adjudication")
_d("6B986DE", "N4", "CLOSED-ARCH", "Manual §5.10 (f) class of a chain")
_d("63DDF91", "B1", "CLOSED-ARCH", "Manual §3.4 completeness target with member revisions; completeness-cover seed")
_d("653E88C", "B1", "CLOSED-BY-SEED", "revision_assessment_record_mode (standing mode)")
_d("EDABD81", "N1", "CLOSED-ARCH", "Manual §4.1 standing reads what counts reads")
_d("82D618C", "N2 N5", "NA-SD47", "post-integration REVALIDATE withdrawn (SD-40); wording rewritten")
_d("B46C250", "N1", "CLOSED-ARCH", "Manual §5.5 evaluation in the state at hand")
_d("D94A293", "B1", "CLOSED-BY-SEED", "gate_basis_record_all")
_d("653E88C", "N1", "CLOSED-ARCH", "Manual §4.3 required premises are the required-evidence section's")
_d("83A82DF", "N2", "NA-SD47", "supersession cell wording rewritten")
_d("A6ED164", "B1", "CLOSED-BY-SEED", "endpoint_only_equivalence_reach, directed_chain_only")
_d("0D2B35E", "N2", "A3", "hop-direction cost restored to Manual §32.2")
_d("3540D98", "B3", "CLOSED-ARCH", "Manual §5.5 gate term caps a QUALIFIED decision at P (R11)")
_d("653E88C", "N3", "NA-RR10", "")
_d("AD7ECE7", "N1", "NA-RR10", "")
_d("EDABD81", "N6", "NA-RR10", "")
_d("6B986DE", "N8", "COST", "Manual §32.2")
_d("63DDF91", "N1", "COST", "Manual §32.2 relief admitted only while the basis holds (A3)")
_d("6FE1000", "N8", "NA-SD47", "workplan cycle-record residue")
_d("F185036", "N1", "COST", "Manual §32.3 drift re-dispatch cost")
_d("051CCE3", "N1", "CLOSED-S2-S3", "§3.4 typed targets row")
_d("9431629", "N2", "CLOSED-S2-S3", "§3.4 typed targets row")
_d("AD7ECE7", "N4", "CLOSED-S2-S3", "§3.4 typed targets row")
_d("E810508", "N4", "CLOSED-S2-S3", "§3.4 typed targets row")
_d("AD7ECE7", "B1", "CLOSED-S2-S3", "§5.10 (a) W row")
_d("6B986DE", "B1", "CLOSED-BY-SEED", "challenged_record_authors")
_d("093164F", "B1", "CLOSED-S2-S3", "§10.4 routing rows (S3)")
_d("8F4E75D", "B1", "CLOSED-S2-S3", "§10.4 routing rows (S3)")
# §5
_d("051CCE3", "N6 N7", "COST", "Manual §32.2 context-relative supersession; trade-offs")
_d("085C979", "SC-1", "CLOSED-BY-SEED", "adverse_changed_units; Manual §5.10 (c) empty W reaches only its target")
_d("085C979", "B1", "CLOSED-BY-SEED", "judged_output_role_only, independence_on_delta; S2 W row")
_d("085C979", "N3", "NA-SD47", "")
_d("095CE55", "N2", "CLOSED-ARCH", "Manual §5.10 (h)8 routed")
_d("0B6C4FA", "B2", "CLOSED-ARCH", "gate tenure filter withdrawn; Manual §5.5, §19.4")
_d("0D2B35E", "N3 N4", "NA-RR10", "")
_d("29DA56E", "N6", "COST", "party exclusion left to policy (closure map §5), accepted at G1")
_d("29DA56E", "N7", "COST", "Manual §32.2")
_d("34803DF", "N1", "NA-RR10", "")
_d("34803DF", "N2", "NA-SD47", "attribution wording")
_d("362AF9F", "N4", "CLOSED-ARCH", "Manual §8.3 step 2 a rebase records the transformation it rebases")
_d("362AF9F", "N7", "COST", "Manual §32.3")
_d("3940DBC", "N4", "NA-RR10", "")
_d("47B9F77", "N5", "CLOSED-S2-S3", "§10.4 out-of-scope findings row (S3 oos_latest_masked_by_pending)")
_d("494C810", "N2", "NA-LATCH", "")
_d("4C52205", "N5", "NA-RR10", "")
_d("4C52205", "N6", "NA-SD47", "")
_d("5895687", "N1", "CLOSED-ARCH", "Manual §13.4 fixed fields: every field the tightening order holds fixed")
_d("5895687", "N3", "CLOSED-ARCH", "Manual §5.10 (c) plan row; restated in §32.2 by A3")
_d("5895687", "N4", "NA-RR10", "")
_d("5895687", "N6", "NA-SD47", "")
_d("61CD09B", "B1", "CLOSED-ARCH", "Manual §5.10 (e) route 3 exact-target relief (R8)")
_d("61CD09B", "N7", "COST", "Manual §32.2-§32.3")
_d("63DDF91", "N6", "COST", "Manual §32.2-§32.3")
_d("6B986DE", "N2", "A3", "attestation-challenge disclosure restored to Manual §32.2")
_d("6B986DE", "N5", "NA-SD47", "")
_d("6B986DE", "N7", "COST", "party exclusion left to policy, accepted at G1")
_d("71CF9B3", "B2", "CLOSED-ARCH", "Manual §10.2 revision run (SD-22)")
_d("82D618C", "N7", "NA-RR10", "")
_d("83A82DF", "N1", "CLOSED-ARCH", "Manual §5.10 (c) plan row states the claim per acceptance")
_d("83A82DF", "N4", "NA-RR10", "")
_d("8C1F2F2", "N1", "CLOSED-ARCH", "status wording fixed at dddfedf (SD-49)")
_d("8C1F2F2", "N2", "COST", "Manual §32.2 work-key reset")
_d("913DB8F", "N1", "CLOSED-ARCH", "Manual §10.3 waits by design; §5.10 (h)4 as amended by A1")
_d("913DB8F", "N2 N5", "NA-SD47", "")
_d("913DB8F", "N3", "CLOSED-ARCH", "one key, prose and fixed fields, for plan and work (Manual §13.4, §5.10 (b))")
_d("913DB8F", "N4", "NA-RR10", "")
_d("913DB8F", "N6", "A4", "cross-item or cross-plan owner rule dropped from Manual §5.10 (e) by the SD-47 condensation; the catalogue keeps it")
_d("913DB8F", "N7", "COST", "Manual §5.10 (c) plan row is a conservative resolution policy")
_d("9E5A763", "N2", "NA-SD47", "")
_d("A6ED164", "N1", "NA-RR10", "")
_d("A6ED164", "N2", "NA-SD47", "")
_d("A6ED164", "N3", "COST", "Manual §32.2-§32.3")
_d("AD7ECE7", "N2", "NA-SD47", "")
_d("B365947", "B2", "CLOSED-BY-SEED", "review_reach_changed_only; S2 W row")
_d("B365947", "N2", "COST", "Manual §32.3 drift re-dispatch")
_d("B46C250", "B1", "CLOSED-BY-SEED", "frame_acts_everywhere")
_d("BF23372", "N4", "NA-RR10", "")
_d("C4E8DE7", "N2", "NA-LATCH", "")
_d("C6DA678", "B2", "CLOSED-ARCH", "Manual §5.10 (c) reach by judged content, not item revision")
_d("CC005DB", "B3", "CLOSED-ARCH", "Manual §5.10 (c) product-scope row")
_d("D6734C4", "N1", "CLOSED-ARCH", "Manual §5.10 (h)5 states the adverse exception")
_d("D6734C4", "N2", "COST", "")
_d("D94A293", "N1", "CLOSED-ARCH", "Manual §5.10 (c) plan row: a conservative resolution policy")
_d("DDDFEDF", "N2", "COST", "Manual §32.2 work-key reset")
_d("E548472", "N2", "CLOSED-ARCH", "Manual §5.10 (h)6 over the admitted set")
_d("E548472", "N4", "NA-RR10", "")
_d("E810508", "N2", "CLOSED-ARCH", "Manual §5.10 (b) a prose or fixed-field change starts new work")
_d("E810508", "N5", "CLOSED-S2-S3", "§8.3 step 2 DROP row (no retained field)")
_d("E810508", "N6", "NA-SD47", "")
_d("E9E6E9F", "B2", "CLOSED-ARCH", "Manual §5.5 gterm caps on the qualified decision's own currency (R11)")
_d("EDABD81", "B2", "CLOSED-ARCH", "root-only revalidation removed; Manual §4.1 routes")
_d("EDABD81", "N2", "CLOSED-ARCH", "Manual §5.10 (b) subject kinds stay on their triple (S10)")
_d("EDABD81", "N3", "CLOSED-ARCH", "Manual §16.5 lineage carry")
_d("F044820", "N1", "COST", "Manual §32.2 work-key reset")
_d("F044820", "N2", "NA-SD47", "closure-map aid")
_d("F22B4DC", "B1", "CLOSED-ARCH", "Manual §5.2 enactment is one task with its rebases (SD-26)")
_d("F22B4DC", "N3", "NA-SD47", "")
_d("F22B4DC", "N6", "COST", "Manual §32.3")
_d("F7419D5", "B1", "CLOSED-ARCH", "Manual §5.2 acting rule, §5.5 gate term in one state")
_d("A18B544", "B2", "CLOSED-ARCH", "Manual §5.5 gterm per eligible decision (SD-24)")
_d("0B6C4FA", "B2", "CLOSED-ARCH", "gate tenure filter withdrawn")
_d("47B9F77", "B1", "CLOSED-S2-S3", "§5.10 (a) W row: a fact of id(X), work-keyed")
_d("8C1F2F2", "B1", "CLOSED-S2-S3", "S1 objection cases; A1 (pending)")
_d("F044820", "B1", "CLOSED-S2-S3", "§5.10 (a) owner-exception row (SD-48)")


# §6
_d("0B6C4FA", "B1", "CLOSED-S5", "S5 §6 unbounded_run_still_linked")
_d("5C55D4B", "B1", "CLOSED-S5", "S5 §6 unbounded_run_still_linked")
_d("1FFBBF0", "B1", "CLOSED-S5", "S5 §6 unpinnable_supports_no_stop")
_d("3540D98", "B2", "CLOSED-S5", "S5 §6 differing_pin_goes_to_owner (complete pin set)")
_d("C6DA678", "B1", "CLOSED-S5", "S5 §6 differing_pin_goes_to_owner")
_d("53669A5", "B1", "CLOSED-S5", "S5 §6 differing_free_attribute_goes_to_owner")
_d("D837363", "B1", "CLOSED-S5", "S5 §6 differing_free_attribute_goes_to_owner (environment)")
_d("6FF4ED1", "B1", "CLOSED-S5", "S5 §6 context_change_keeps_implication")
_d("CC005DB", "B2", "CLOSED-S5", "S5 §6 context_change_keeps_implication")
_d("D837363", "B2", "CLOSED-S5", "S5 §6 context_change_keeps_implication; Manual §6.3 guard")
_d("29DA56E", "N2", "CLOSED-ARCH", "Manual §5.10 (f) a human's non-authorship attestation for every kind")
_d("494C810", "N3", "NA-LATCH", "")
_d("798B2B4", "B4", "STAGE-D", "catalogue §6.3 records each link traversed; a runner read-tracing test")
_d("A18B544", "B1", "CLOSED-ARCH", "Manual §17.5 a class that does not observe outside reads makes every execution unpinnable")
_d("B595F2C", "B1", "CLOSED-ARCH", "Manual §6.3 basis recorded at the granularity the closure reached")
_d("F22B4DC", "N1", "CLOSED-ARCH", "Manual §5.2 observations and readings outside the acting rule")
_d("E23F142", "N1", "COST", "paraphrase-only 2026-10-12 instruction, Manual §32.2")
_d("E23F142", "N2", "CLOSED-ARCH", "Manual §6.5 completeness read positively only")
_d("E23F142", "N3", "NA-RR10", "")
_d("E23F142", "N4", "COST", "empirical costs measured at G3 (Manual §31.9)")


# §7
_d("051CCE3", "N3", "CLOSED-ARCH", "Manual §19.5 cutover carried by an integration; §32.2")
_d("27EF339", "B3", "CLOSED-ARCH", "Manual §7.5 a gate decision on a gate derived in the frame declares the frame")
_d("362AF9F", "N3", "CLOSED-S2-S3", "§7.1 one producing context row (S2 binding cases)")
_d("61CD09B", "N5", "CLOSED-S2-S3", "§7.1 one producing context row (S2 binding cases)")
_d("47B9F77", "N1", "NA-RR10", "")
_d("E810508", "N1", "NA-RR10", "")
_d("4C52205", "SC-1", "CLOSED-ARCH", "resolved by the stakeholder (SD-32); Manual §5.10 (c) plan row")
_d("E548472", "SC-1", "CLOSED-ARCH", "resolved by the stakeholder (SD-31); revert exemption dropped")
_d("4C52205", "N4", "A3", "relief clears coverage of shared tightenings, restored to Manual §32.2")
_d("575DC78", "B1", "CLOSED-ARCH", "Manual §5.5 gate term is the minimum over eligible decisions (R11)")
_d("5895687", "N5", "COST", "plan row is a conservative resolution policy")
_d("B365947", "N3", "NA-SD47", "closure-map residue")
_d("C77447B", "N2", "NA-LATCH", "")


# §8-§13
LATCH = "R15's latch, withdrawn by SD-36"
for rec, ids in (("095CE55", "B1 N3"), ("3876473", "B1 N1 N2 N3 N4"), ("3940DBC", "B1 N1 N2 N3 N5"),
                 ("494C810", "B1"), ("C4E8DE7", "B1 N6"), ("C77447B", "B1 N1 N6")):
    _d(rec, ids, "NA-LATCH", LATCH)
_d("095CE55", "N1", "CLOSED-ARCH", "Manual §10.2 SPEC_REVIEW(spec, r): each change its own obligation")
_d("095CE55", "N5", "NA-SD47", "stale-result route rewritten (SD-40)")
_d("C77447B", "N3", "CLOSED-ARCH", "Manual §5.10 (b) a joint-invariant review judges the change inside the invariant's scope")
_d("C77447B", "N4", "CLOSED-S2-S3", "§10.4 routing rows (S3 fence routes)")
_d("494C810", "N6", "CLOSED-ARCH", "Manual §22.2 a records-only request has no effect to publish")
_d("093164F", "N3", "NA-RR10", "")
_d("093164F", "N4", "CLOSED-ARCH", "Manual §10.3 a disagreement's adjudication waits by design; §5.10 (h)4 (A1)")
_d("EB86A71", "N1", "CLOSED-S2-S3", "§10.2 COORDINATE keying row (S3): each condition one decision")
_d("EB86A71", "N3", "NA-RR10", "")
_d("EB86A71", "N4", "CLOSED-ARCH", "Manual §10.4 a disagreement's obligations are not item routes")
_d("EB86A71", "N5", "COST", "joint-invariant review per change in scope (Manual §9.2, §32.3)")
_d("8F4E75D", "N1 N2", "CLOSED-ARCH", "Manual §8.3 step 8 exemption for a request carrying a current prospective acceptance of the prerequisite authority")
_d("8F4E75D", "N3", "CLOSED-ARCH", "Manual §10.4 a REFUSED event-keyed obligation derives a decision until answered")
_d("AD7ECE7", "B2", "CLOSED-S2-S3", "§10.4 out-of-scope findings row (S3)")
_d("47B9F77", "N2", "CLOSED-S2-S3", "§3.4 typed targets row (S2)")
_d("47B9F77", "N4", "CLOSED-S2-S3", "§13.7 item-level target row (S2)")
_d("47B9F77", "N6", "NA-SD47", "")
_d("F22B4DC", "N4", "CLOSED-ARCH", "Manual §10.4 discharge is not latched (SD-36)")
_d("82D618C", "B1", "CLOSED-ARCH", "Manual §8.3 step 8 refuses only evidence regression (R15)")
_d("82D618C", "N1", "CLOSED-ARCH", "Manual §10.2 REVALIDATE: depends on means no other judgment satisfies the term")
_d("82D618C", "N3", "CLOSED-ARCH", "Manual §10.3 the waiting class stated as a class")
_d("82D618C", "N6", "NA-SD47", "")
_d("EDABD81", "B1", "CLOSED-BY-SEED", "revision_assessment_record_mode (a standing entry)")
_d("EDABD81", "N4", "NA-SD47", "stale-review statements rewritten (SD-40)")
_d("EDABD81", "N5", "CLOSED-ARCH", "Manual §10.3 no stranded obligation covers readiness and waiting routes")
_d("EDABD81", "N7", "CLOSED-ARCH", "Manual §8.3 step 8 judgment staleness is not regression")
_d("F185036", "B1", "CLOSED-S2-S3", "§10.4 routing rows (S3); current-state ends (SD-37)")
_d("F185036", "N2", "COST", "joint-invariant re-review per change (Manual §9.2)")
_d("F185036", "N4", "CLOSED-ARCH", "Manual §8.3 step 8 names the prerequisite-authority exemption")
_d("F185036", "N5", "NA-RR10", "")
_d("F185036", "N6", "NA-SD47", "")
_d("29DA56E", "N1", "CLOSED-ARCH", "Manual §10.3 a non-independent judgment answers no obligation requiring independence")
_d("51070E5", "N2", "CLOSED-ARCH", "Manual §10.3 a non-independent judgment answers no obligation requiring independence")
_d("6B986DE", "N1", "CLOSED-ARCH", "Manual §10.3 an obligation whose judgments were all refused stays dispatchable")
_d("29DA56E", "N4", "NA-SD47", "")
_d("51070E5", "N4 N5", "NA-SD47", "")
_d("51070E5", "N1", "CLOSED-ARCH", "Manual §5.10 (f) the classification is fixed at admission from the binding")
_d("1FFBBF0", "B2", "CLOSED-S5", "S5 §10 revert_starts_a_new_run; Manual §10.2 run known before the event (SD-25)")
_d("53669A5", "B2", "CLOSED-ARCH", "Manual §8.3 step 7 revision assessments first, for gates and human acceptances too")
_d("798B2B4", "B1 B2", "CLOSED-S5", "S5 §10 revert_starts_a_new_run; Manual §10.2 revision run (SD-22)")
_d("798B2B4", "B3", "CLOSED-ARCH", "Manual §10.2 the predecessor is a display, never an equality condition (SD-22)")
_d("86AB683", "B1", "CLOSED-ARCH", "Manual §10.2 a record counts only in its run")
_d("D837363", "B3", "CLOSED-ARCH", "Manual §10.2 REVIEW(s, r) derived wherever a record is missing, however the revision was produced")
_d("6FF4ED1", "B2", "CLOSED-S5", "S5 §13 prose_change_is_not_tightening")
_d("6FF4ED1", "B4", "CLOSED-ARCH", "Manual §10.2 AUTHOR and DOCUMENT obligation kinds and holders")
_d("B595F2C", "B2", "CLOSED-S5", "S5 §13 ref_outside_item_part_rejected")
_d("B595F2C", "B3", "CLOSED-S5", "S5 §13 document_item_cannot_touch_authority")
_d("C6DA678", "B3", "CLOSED-S5", "S5 §13 document_item_cannot_touch_authority; S5 §1 write-set cases")
_d("B595F2C", "B4", "CLOSED-ARCH", "Manual §10.3 answered judgment obligations; §8.3 step 7 one TASK_RESULT per task (R9)")
_d("051CCE3", "N2", "CLOSED-S5", "S5 §13 repartition_keeps_discharged_parts")
_d("63DDF91", "N2", "CLOSED-S5", "S5 §13 repartition_keeps_discharged_parts")
_d("9E5A763", "N3", "CLOSED-S5", "S5 §13 repartition_keeps_discharged_parts, repartition_lint_over_undischarged")
_d("362AF9F", "N2", "CLOSED-ARCH", "Manual §13.7 each part bound to its own part obligation and its own enactment")
_d("61CD09B", "N4", "CLOSED-ARCH", "Manual §13.7 each part bound to its own part obligation")
_d("F03B15E", "N2", "CLOSED-ARCH", "catalogue §13.7 part obligation identified by item revision, PARTITION record and part index")
_d("4C52205", "N2", "NA-SD47", "")
_d("E548472", "N3", "CLOSED-ARCH", "Manual §13.4 the order claims only that the acceptance still applies under tighter controls")
_d("653E88C", "N4", "COST", "plan row is a conservative resolution policy, accepted at G1")
_d("BF23372", "N2", "COST", "Manual §32.2 a standing adverse judgment on a triple does not freeze re-scoping")
_d("BF23372", "N3", "A3", "re-partition consequence restored to Manual §32.2")
_d("B365947", "N5", "NA-SD47", "")
_d("F03B15E", "B1", "CLOSED-ARCH", "Manual §3.4 a support record's target is the exact thing it judges")
_d("F03B15E", "N1", "CLOSED-ARCH", "Manual §10.3 answered by a judgment bound to it or recorded on its target by a human")
_d("9431629", "N3", "CLOSED-S2-S3", "§8.3 step 7 STALE_RETAINED replaced by the judged-content support check (S2)")


# §14-§25
LIMITS = "historical, provenance and empirical limits carried (Manual §32.2, §32.5, §31.9; register RR-9)"
for rec, ids in (("085C979", "N4"), ("29DA56E", "N8"), ("51070E5", "N7"), ("6B986DE", "N9"), ("9E5A763", "N5"),
                 ("A6ED164", "N4"), ("D6734C4", "N3")):
    _d(rec, ids, "COST", LIMITS)
TRADE = "retained trade-offs, accepted at G1 (Manual §32.2-§32.3)"
for rec, ids in (("0D2B35E", "N5"), ("34803DF", "N5"), ("83A82DF", "N5"), ("913DB8F", "N8"), ("BF23372", "N6")):
    _d(rec, ids, "COST", TRADE)
_d("9431629", "N4", "CLOSED-S5", "this index and the S5 per-section dispositions (RR-9)")
_d("8C1F2F2", "N3", "NA-SD47", "closure-map aid")
_d("DDDFEDF", "N3", "NA-SD47", "closure-map aid")
_d("DDDFEDF", "N1", "CLOSED-ARCH", "status wording repaired at dddfedf")
_d("DDDFEDF", "N4", "CLOSED-S2-S3", "§5.10 (d)/(h)(4) per-state row (S2 route cases; A1)")
_d("27EF339", "B1", "CLOSED-S5", "S5 §6 unbounded_run_still_linked")
_d("27EF339", "B2", "CLOSED-S5", "S5 §1 span_shift_not_a_change, innermost ownership")
_d("3876473", "N5", "NA-SD47", "")
_d("494C810", "N5", "NA-SD47", "")
_d("8F4E75D", "N6", "NA-SD47", "")
_d("F03B15E", "N4", "NA-SD47", "")
_d("AD7ECE7", "N5", "NA-SD47", "dispositions of earlier findings, superseded by this index")
_d("093164F", "N1", "CLOSED-ARCH", "Manual §15.5 decisions with no report allow the outcomes catalogue §15.5 lists")
_d("093164F", "N2", "NA-SD47", "re-attestation of integrated results withdrawn (SD-40)")
_d("362AF9F", "N1", "CLOSED-ARCH", "Manual §5.2, §22.2-§22.3 re-application is a new task and enactment (R12)")
_d("C4E8DE7", "N4 N5", "NA-LATCH", "")
_d("4C52205", "N3", "CLOSED-ARCH", "Manual §16.5 carried objections: a standing rejection is carried while it stands")
_d("E548472", "N1", "CLOSED-ARCH", "Manual §16.5 a finding ends only by an independent, acting, unvetoed RESOLVED")
_d("D6734C4", "B1", "CLOSED-ARCH", "Manual §16.5 carries every standing rejection naming an asked item at any revision")
_d("61CD09B", "N1", "CLOSED-ARCH", "Manual §16.6 the core lists every standing adverse judgment in reach")
_d("D94A293", "N2", "COST", "cross-plan continuity bounded (Manual §32.2)")
_d("F185036", "N3", "CLOSED-ARCH", "Manual §10.4 drift brief and empty transformation")
_d("53669A5", "B3", "CLOSED-ARCH", "Manual §18.4 contrary dispositions after ABSORB derive adjudication and realignment")
_d("61CD09B", "B2", "CLOSED-S5", "S5 §19 cutover_record_after_carrier_integrated_refused")
_d("F03B15E", "B2", "CLOSED-S5", "S5 §19 cutover_record_after_carrier_integrated_refused")
_d("F03B15E", "N3", "COST", "fenced cutover half state disclosed (Manual §19.5, §32.2)")
_d("63DDF91", "N3", "CLOSED-ARCH", "Manual §19.5 cutover carried by an integration; fails closed")
_d("61CD09B", "N2", "CLOSED-ARCH", "Manual §22.3 fence re-gating stated; §32.3 trigger")


def s1_evidence():
    """(record, finding) -> the s1 diagnostic's named discriminators that reproduce it."""
    import subprocess
    import sys
    path = os.path.join(ROOT, "s1_disagreement_model_check.py")
    out = subprocess.run([sys.executable, "-I", path, "--depth", "1"], capture_output=True, text=True).stdout
    ev: dict = {}
    for rid, fid in re.findall(r"\[ok\] ([0-9a-f]{7}) ([A-Z][A-Za-z0-9′]*)", out):
        base = re.match(r"[A-Z]\d?", fid).group(0) if fid[0] != "o" else fid
        ev.setdefault((rid.upper(), fid), True)
        ev.setdefault((rid.upper(), base), True)
    return ev


def mutation_evidence():
    """(record, finding) -> mutation names whose description cites that finding."""
    import importlib.util
    import sys
    path = os.path.join(ROOT, "judgment_disagreement_model_check.py")
    spec = importlib.util.spec_from_file_location("jdmc_index", path)
    m = importlib.util.module_from_spec(spec)
    sys.modules["jdmc_index"] = m
    spec.loader.exec_module(m)
    out: dict = {}
    for name, (_fams, desc) in m.MUTATIONS.items():
        for rid, fid in re.findall(r"\b([0-9a-f]{7})\s+((?:B|N|SC-)\d+)", desc):
            out.setdefault((rid.upper(), fid), []).append(name)
    return out


HEAD = re.compile(r"^(?:#{2,4}\s+|\*\*)((?:B|N|SC-?)\d+(?:\([a-z]\))?|Blocker [A-Z][\'′1-9]?)\b[^\n]*", re.M)
SECREF = re.compile(r"§(\d+)(?:\.(\d+))?")


def records():
    pats = ["MANUAL-REVIEW-SSDS-8.0-*.md", "WORKPLAN-REVIEW-SSDS-8.0-*.md"]
    for pat in pats:
        for f in sorted(glob.glob(os.path.join(ROOT, pat))):
            yield f


def short_id(name: str) -> str:
    m = re.match(r"(?:MANUAL|WORKPLAN)-REVIEW-SSDS-8\.0-([0-9A-F]{7})", name)
    return m.group(1) if m else name


def findings(path: str):
    text = open(path, encoding="utf-8").read()
    heads = list(HEAD.finditer(text))
    seen = set()
    all_refs = collections.Counter(m.group(1) for m in SECREF.finditer(text))
    default = all_refs.most_common(1)[0][0] if all_refs else "?"
    for i, m in enumerate(heads):
        fid = m.group(1)
        if fid in seen:
            continue
        seen.add(fid)
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[m.start():end]
        refs = [r.group(0) for r in SECREF.finditer(body)]
        owner = SECREF.search(body)
        owner = owner.group(1) if owner else default
        title = re.sub(r"^[#*\s]+", "", m.group(0)).strip().rstrip("*")
        yield fid, title[:140], owner, refs[:6]


MUTS: dict = {}
S1EV: dict = {}


def main():
    global MUTS, S1EV
    MUTS = mutation_evidence()
    S1EV = s1_evidence()
    rows = []
    for f in records():
        name = os.path.basename(f)
        kind = "workplan" if name.startswith("WORKPLAN") else "manual"
        rid = short_id(name)
        for fid, title, owner, refs in findings(f):
            base = re.sub(r"\([a-z]\)$", "", fid)
            model = MODELLED.get((rid, base))
            hand = DISPOSED.get((rid, base))
            muts = MUTS.get((rid, base))
            if model:
                disp = f"CLOSED-BY-MODEL: {model}"
            elif hand:
                disp = f"{hand[0]}: {hand[1]}" if hand[1] else hand[0]
            elif muts:
                disp = "CLOSED-BY-SEED: " + ", ".join(muts)
            elif (rid, base) in S1EV or (rid, base.replace("Blocker ", "")) in S1EV:
                disp = "CLOSED-BY-SEED: s1_disagreement_model_check.py discriminator"
            elif kind == "workplan" and rid != "E23F142":
                disp = "CLOSED-PHASE-B"
            else:
                disp = f"OPEN: S5 §{owner}"
            rows.append((kind, rid, name, fid, title, owner, " ".join(refs), disp))
    by_owner = collections.Counter(r[5] for r in rows if r[7].startswith("OPEN"))
    print("Governing SSDP version: 7.2.1.\n")
    print("# G2 Stage S step S4 — finding index (generated)\n")
    print("Generated by `qualification/ssds80/models/finding_index.py`; do not edit by hand. Coordination "
          "evidence for the G2 shadow workplan §4.1 S4: each heading-level finding of the SSDS 8 Review "
          "records, routed to the catalogue section that owns it. `CLOSED-BY-MODEL` names the S1-S3 model "
          "cases that reproduce the finding; `OPEN` findings are judged when S5 settles their section. "
          "Extraction is mechanical: a finding stated only in running prose, or routed by a misleading "
          "first reference, may be missing or misrouted, so S5 reads each record it owns in full. Section "
          "references in workplan Review records name workplan sections (for example workplan §6.6, "
          "derivation), which S5 maps to the catalogue section that realizes them.\n")
    tally = collections.Counter(r[7].split(":")[0] for r in rows)
    print(f"Records: {len({r[2] for r in rows})}; findings: {len(rows)}; by disposition: "
          + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())) + ".\n")
    print("Open findings per owning section: " + ", ".join(
        f"§{k} {v}" for k, v in sorted(by_owner.items(), key=lambda kv: (len(kv[0]), kv[0]))) + ".\n")
    print("| Record | Finding | Title | Owner | Sections cited | Disposition |")
    print("|---|---|---|---|---|---|")
    for kind, rid, name, fid, title, owner, refs, disp in rows:
        t = title.replace("|", "\\|")
        print(f"| {kind} {rid} | {fid} | {t} | §{owner} | {refs} | {disp} |")


if __name__ == "__main__":
    main()

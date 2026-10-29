"""Manual/catalogue §15.1 vocabulary and non-blocking FINDING, through schema and Admission."""
import unittest

from ssds.admission.request import request_message
from ssds.ledger.read import read_chain, with_id
from ssds.ledger.schema import record_violations

from ._fixtures import record, sshsig
from .test_admission_requests import RequestFixture


# Transcribed from the accepted §15.1 table, independent of the validator's map.
VOCABULARY = {
    'CHALLENGE': ['AUTHORITY_DEFECT', 'EVIDENCE_DEFECT', 'CONFORMANCE_DEFECT', 'STRUCTURE_DEFECT'],
    'FINDING': ['TENSION', 'ANOMALY', 'OPPORTUNITY', 'DEFECT', 'INSPECTABILITY_GAP'],
    'AMENDMENT_REQUEST': ['SCOPE_DEVIATION', 'MISSING_PREREQUISITE', 'INFEASIBLE_CRITERION',
                          'CONTRACT_DEFECT', 'AUTHORITY_DEFECT'],
    'BLOCKER': ['PREREQUISITE_UNAVAILABLE', 'ENVIRONMENT', 'AMBIGUITY'],
    'HUMAN_QUESTION': ['DECISION_NEEDED', 'CLARIFICATION'],
}


def report(kind, reasons=(), **fields):
    target = {'record': 'sha256:' + '1' * 64} if kind == 'CHALLENGE' else {'units': ['guide']}
    values = {'blocking': False, 'serious': False, 'inquiry': 'EXPLORATORY'} if kind == 'CHALLENGE' else {
        'materiality': 'ROUTINE'}
    return record(kind, target=target, reason=list(reasons), fields={**values, **fields})


class Vocabulary(unittest.TestCase):
    def test_each_prescribed_reason_and_empty_reasons_remain_representable(self):
        for kind, reasons in VOCABULARY.items():
            for chosen in [[], *[[reason] for reason in reasons], reasons]:
                with self.subTest(kind=kind, reasons=chosen):
                    self.assertEqual(record_violations(report(kind, chosen)), [])

    def test_unknown_and_other_kinds_reasons_are_refused_even_beside_valid_ones(self):
        for kind, reasons in VOCABULARY.items():
            foreign = 'ANOMALY' if kind != 'FINDING' else 'ENVIRONMENT'
            for invalid in ['NOT_A_REPORT_REASON', foreign]:
                with self.subTest(kind=kind, reason=invalid):
                    self.assertTrue(record_violations(report(kind, [*reasons, invalid])))

    def test_finding_never_blocks_but_optional_false_stays_valid(self):
        self.assertEqual(record_violations(report('FINDING', ['DEFECT'])), [])
        self.assertEqual(record_violations(report('FINDING', ['DEFECT'], blocking=False)), [])
        self.assertIn('FINDING cannot block', record_violations(report('FINDING', ['DEFECT'], blocking=True)))
        for kind in ['AMENDMENT_REQUEST', 'BLOCKER', 'HUMAN_QUESTION']:
            self.assertEqual(record_violations(report(kind, blocking=True)), [])


class AdmissionGrammar(RequestFixture):
    def submit_human(self, rec):
        rec = with_id({**rec, 'actor': self.human()})
        request = self.request([rec], base_position=len(self.entries()) - 1)
        request['binding'] = {'human': {'actor': self.human(),
                                       'signature': sshsig(self.private, request_message(request))}}
        return rec, self.admit(request)

    def test_a_true_nonblocking_finding_is_admitted_and_retained(self):
        rec, decision = self.submit_human(report('FINDING', ['INSPECTABILITY_GAP'], blocking=False))
        self.assertEqual(decision.admitted, (rec['id'],))
        chain = read_chain(self.home.ledger_repository('demo'), 'demo')
        self.assertIsNone(chain.halt)
        self.assertIn(rec, chain.entries[-1].records)

    def test_forbidden_finding_variants_fail_real_admission(self):
        for reasons, fields in [(['INSPECTABILITY_GAP'], {'blocking': True}),
                                (['NOT_A_REPORT_REASON'], {}), (['ENVIRONMENT'], {})]:
            with self.subTest(reasons=reasons, fields=fields):
                rec, decision = self.submit_human(report('FINDING', reasons, **fields))
                self.assertNotIn(rec['id'], decision.admitted)
                self.assertIn('SCHEMA_RECORD', dict(decision.refused).get(rec['id'], ()) + decision.reasons)
                self.assertFalse(any(rec['id'] == r['id'] for e in self.entries() for r in e.records))

"""Qualification harness fixtures: expectations from F123 and Manual §1.8, §8.3, §24.1, §25.3."""
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from tests.ssds.test_admission_genesis import GenesisFixture, MANIFEST
from tests.ssds._fixtures import commit, git

spec = importlib.util.spec_from_file_location('difference_study', SCRIPTS / 'difference_study.py')
study = importlib.util.module_from_spec(spec)
spec.loader.exec_module(study)


class Study(GenesisFixture):
    def run_study(self, candidate, **kwargs):
        return study.study(self.product, candidate, self.root / 'study-home',
                           modes={'*': {'mode': 'UNGOVERNED'}}, real_baseline=self.baseline, **kwargs)

    def test_real_owners_and_both_directions_of_consequences(self):
        (self.product / 'guide.md').write_text('# Guide\n\n## Introduction\n\nChanged.\n\n## Usage\n\nRun it.\n')
        clean = commit(self.product, 'clean content delta')
        manifest = self.product / '.ssds/manifest.toml'
        manifest.write_text(MANIFEST.replace('kind = "D4"', 'kind = "D3"'))
        changed_kind = commit(self.product, 'change kind')
        manifest.write_text(MANIFEST)
        restored = commit(self.product, 'restore declaration bytes')
        manifest.write_text(MANIFEST.replace('path = "guide.md"', 'file = "missing.md"'))
        missing = commit(self.product, 'unresolved changed term')
        manifest.write_text(MANIFEST)
        commit(self.product, 'restore valid terms')
        (self.product / '.ssds/policy.toml').write_text('schema = 1\n# a human policy edit\n')
        protected = commit(self.product, 'protected touch')
        fake = 'ghp_' + 'A' * 36
        (self.product / 'src/tool.py').write_text("token = '" + fake + "'\n")
        credential = commit(self.product, 'synthetic credential-shaped fixture')
        result = self.run_study(credential)
        rows = {r['commit']: r for r in result['commits']}
        self.assertEqual(rows[clean]['checks']['2'], [])
        self.assertEqual(rows[clean]['checks']['1']['credential_template'], [])
        self.assertEqual(rows[clean]['checks']['3'], [])
        self.assertIn('SCHEMA_UNSUPPORTED', {f['code'] for f in rows[changed_kind]['checks']['2']})
        self.assertTrue(rows[changed_kind]['consequence_changes']['quarantine']['added'])
        self.assertTrue(rows[restored]['consequence_changes']['quarantine']['removed'])
        self.assertIn('STRUCT_TERM_UNRESOLVED', {f['code'] for f in rows[missing]['checks']['2']})
        self.assertTrue(rows[protected]['checks']['3'])
        self.assertTrue(all('if agent-made' in f['applicability'] for f in rows[protected]['checks']['3']))
        self.assertTrue(rows[credential]['checks']['1']['credential_template'])
        self.assertNotIn(fake, json.dumps(result), 'the report never contains matched credential bytes')
        self.assertTrue(all(r['checks']['4']['status'] == 'vacuous' for r in result['commits']))
        self.assertTrue(result['boundary']['unchanged'])
        self.assertEqual(result['summary']['evaluated'], 7)
        self.assertEqual(result['initialization']['commit'], self.baseline)
        self.assertEqual([r['parent'] for r in result['commits']],
                         [self.baseline, *[r['commit'] for r in result['commits'][:-1]]])
        stored = json.loads((self.root / 'study-home/difference-study.json').read_text())
        self.assertEqual(stored['candidate'], credential)
        self.assertEqual(stored['initialization']['modes'], {'*': {'mode': 'UNGOVERNED'}})

    def test_historical_initialization_retains_unclassified_requirement(self):
        from ssds.content import read_tree
        from tests.ssds._fixtures import init_repo
        other = init_repo(self.root / 'old-product')
        (other / 'a').write_text('a\n')
        absent = commit(other, 'no manifest')
        (other / '.ssds').mkdir()
        (other / '.ssds/manifest.toml').write_text('schema = 1\n')
        missing = commit(other, 'manifest without unclassified')
        (other / '.ssds/manifest.toml').write_text('schema = 1\n[[unit]]\nid = "ssds.unclassified"\n'
                                                 'kind = "UNCLASSIFIED"\nscope = [{prefix = ""}]\n')
        first = commit(other, 'earliest admissible historical genesis')
        (other / 'a').write_text('b\n')
        candidate = commit(other, 'first evaluated delta')
        result = study.study(other, candidate, self.root / 'old-study-home',
                             modes={'*': {'mode': 'UNGOVERNED'}}, real_baseline=first)
        self.assertEqual(result['initialization']['commit'], first)
        self.assertEqual([r['commit'] for r in result['excluded']], [absent, missing])
        self.assertIn('ssds.unclassified', ' '.join(result['excluded'][1]['initialization_problems']))
        self.assertEqual([r['commit'] for r in result['commits']], [candidate])
        self.assertEqual({f['unit'] for f in result['commits'][0]['checks']['2']
                          if f['code'] == 'STRUCT_RESERVED_LEAF'}, {'ssds.manifest', 'ssds.policy'})
        # The historical exception must not leak into production owners after initialization.
        self.assertTrue(study.baseline.baseline_structure(read_tree(other, first), '.ssds/manifest.toml').problems)

    def test_subject_and_part_identities_survive_consequence_projection(self):
        guide = self.product / 'guide.md'
        guide.write_text(guide.read_text().replace('Hello.', 'Hello.\n<!-- ssds:rel DEPENDS_ON missing -->'))
        candidate = commit(self.product, 'a relation defect in a part')
        result = self.run_study(candidate)
        rows = result['commits'][0]['consequence_changes']['ill_formed']['added']
        self.assertTrue(any(row['key'] == 'guide' and any(d['unit'] == 'guide.intro' for d in row['value'])
                            for row in rows), rows)
        projected = study.changes({'drift': {}}, {'drift': {'guide': True}})
        self.assertEqual(projected['drift']['added'], [{'key': 'guide', 'value': True}])

    def test_unsafe_or_existing_home_is_refused_before_ledger_access(self):
        forbidden = (Path.home() / '.ssds', Path.home() / '.ssh', self.product / 'bad-home', self.root)
        for home in forbidden:
            with self.subTest(home=home), patch.object(study, 'initialize') as initialize:
                with self.assertRaises((ValueError, SystemExit)):
                    study.study(self.product, self.baseline, home)
                initialize.assert_not_called()
        self.assertFalse((self.product / 'bad-home').exists())

    def test_cli_requires_explicit_scratch_home_and_full_candidate(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(SystemExit):
            study.main(['--repository', str(self.product), '--candidate', self.baseline])
        with self.assertRaises(ValueError):
            study.population(self.product, 'HEAD', lambda _: self.fail('must reject before tree read'))


if __name__ == '__main__':
    unittest.main()

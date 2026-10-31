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
        self.assertEqual(stored, json.loads(json.dumps(result)))
        self.assertEqual(stored['execution'], {'status': 'COMPLETE', 'phase': 'FINISHED',
                                              'expected_deltas': 7, 'pending': None})
        self.assertEqual(stored['boundary']['status'], 'PASSED')

    def test_interrupted_checks_retain_only_completed_commit_rows(self):
        guide = self.product / 'guide.md'
        guide.write_text(guide.read_text() + '\nFirst change.\n')
        first = commit(self.product, 'first evaluated delta')
        guide.write_text(guide.read_text() + '\nSecond change.\n')
        second = commit(self.product, 'interrupted evaluated delta')
        owner = study.checks

        def interrupt(support, parent, candidate):
            if candidate == second:
                raise RuntimeError('fixture interruption before checks')
            return owner(support, parent, candidate)

        with patch.object(study, 'checks', side_effect=interrupt), self.assertRaises(RuntimeError):
            self.run_study(second)
        stored = json.loads((self.root / 'study-home/difference-study.json').read_text())
        self.assertEqual(stored['execution'], {'status': 'INCOMPLETE', 'phase': 'CHECKS',
                                              'expected_deltas': 2,
                                              'pending': {'parent': first, 'commit': second}})
        self.assertEqual([r['commit'] for r in stored['commits']], [first])
        self.assertEqual(stored['summary']['evaluated'], 1)
        self.assertEqual(stored['summary']['before_or_at_real_baseline'], 0)
        self.assertEqual(stored['summary']['after_real_baseline'], 1)
        self.assertEqual(stored['summary']['findings_by_code'], {})
        self.assertEqual(stored['boundary']['status'], 'UNEXECUTED')
        self.assertIsNone(stored['boundary']['unchanged'])

    def test_absorbed_commit_is_not_reported_complete_before_projection(self):
        guide = self.product / 'guide.md'
        guide.write_text(guide.read_text() + '\nChanged.\n')
        candidate = commit(self.product, 'absorbed but unprojected delta')
        owner = study.consequence_state
        calls = 0

        def interrupt(support):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise RuntimeError('fixture interruption after absorption')
            return owner(support)

        with patch.object(study, 'consequence_state', side_effect=interrupt), self.assertRaises(RuntimeError):
            self.run_study(candidate)
        stored = json.loads((self.root / 'study-home/difference-study.json').read_text())
        self.assertEqual(stored['execution'], {'status': 'INCOMPLETE', 'phase': 'CONSEQUENCES',
                                              'expected_deltas': 1,
                                              'pending': {'parent': self.baseline, 'commit': candidate}})
        self.assertEqual(stored['commits'], [])
        self.assertEqual(stored['summary']['evaluated'], 0)
        self.assertIsNone(stored['boundary']['unchanged'])
        self.assertEqual(stored['boundary']['status'], 'UNEXECUTED')
        from ssds.ledger.read import read_chain
        chain = read_chain(self.root / 'study-home/ledgers/difference-study.git', 'difference-study')
        self.assertIsNone(chain.halt)
        self.assertEqual(study.expected_head(chain.entries), candidate)

    def test_completed_projection_with_changed_product_is_not_complete(self):
        guide = self.product / 'guide.md'
        guide.write_text(guide.read_text() + '\nCommitted change.\n')
        candidate = commit(self.product, 'evaluated delta')
        owner = study.consequence_state
        calls = 0

        def change_product(support):
            nonlocal calls
            calls += 1
            result = owner(support)
            if calls == 2:
                guide.write_text(guide.read_text() + '\nUnexpected product write.\n')
            return result

        with patch.object(study, 'consequence_state', side_effect=change_product), self.assertRaises(ValueError):
            self.run_study(candidate)
        stored = json.loads((self.root / 'study-home/difference-study.json').read_text())
        self.assertEqual(stored['summary']['evaluated'], 1)
        self.assertEqual(stored['execution']['status'], 'FAILED_BOUNDARY')
        self.assertEqual(stored['boundary']['status'], 'FAILED')
        self.assertFalse(stored['boundary']['unchanged'])
        self.assertTrue(stored['boundary']['differences'])

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



class StudyRefusals(unittest.TestCase):
    def test_a_content_read_error_is_a_refusal_not_a_traceback(self):
        """A missing commit or blob raises ``GitReadError``; the study reports it as refused (review of e4a2590d)."""
        import contextlib
        import io

        from ssds.content import GitReadError

        err = io.StringIO()
        with patch.dict(os.environ, {'SSDS_HOME': '/nonexistent/scratch'}), \
                patch.object(study, 'study', side_effect=GitReadError('object x is missing')), \
                contextlib.redirect_stderr(err), self.assertRaises(SystemExit) as stop:
            study.main(['--repository', '.', '--candidate', 'a' * 40])
        self.assertEqual(stop.exception.code, 1)
        self.assertIn('difference study refused: object x is missing', err.getvalue())


def per_object_read_raw(repo, head):
    """The reader before the cost repair, a process per object: the oracle the batched reader must equal."""
    from ssds.ledger.read import ChainRejected, RawEntry

    from ssds.ledger.read import _environment

    def run(*args):
        result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, check=False, env=_environment())
        if result.returncode:
            raise ChainRejected(result.stderr.decode('utf-8', 'replace').strip())
        return result.stdout

    raws, commit = [], head
    while commit is not None:
        header = run('cat-file', 'commit', commit).decode('utf-8', 'replace')
        parents = tuple(line.split()[1] for line in header.split('\n\n', 1)[0].splitlines() if line.startswith('parent '))
        files = {}
        for item in run('ls-tree', '-r', '-z', commit).split(b'\0'):
            if item:
                meta, _, path = item.partition(b'\t')
                files[path.decode('utf-8')] = run('cat-file', 'blob', meta.split(b' ')[2].decode('ascii'))
        raws.append(RawEntry(commit, parents, files))
        try:
            position = json.loads(files.get('entry.json', b'{}')).get('position')
        except ValueError:
            position = None
        if position == 0 or not parents:
            break
        commit = parents[0]
    raws.reverse()
    return raws


class BatchedChainRead(unittest.TestCase):
    """Phase F cost inquiry: ``read_raw`` reads every object through one ``cat-file --batch`` process, with the
    bytes, order and rejections of the per-object reads it replaces."""

    def setUp(self):
        import tempfile
        from ssds.ledger.append import append_entry, create_ledger_repository, import_commits
        from ssds.ledger.signatures import HostKey
        from tests.ssds._fixtures import approve, entry, genesis_record, human_key, init_repo
        from ssds.ledger.qualification import FileWitness

        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        product = init_repo(root / 'product')
        (product / 'README.md').write_text('# Demo\n')
        baseline = commit(product, 'baseline')
        self.ledger = create_ledger_repository(root / 'home' / 'ledgers' / 'demo.git')
        key = HostKey.generate()
        human_private, human_line = human_key(root)
        import_commits(self.ledger, product, [baseline])
        genesis = approve(genesis_record(key, human_line, FileWitness(root / 'w').root, baseline), human_private)
        head = append_entry(self.ledger, entry('demo', 0, None, key, lifecycle=genesis), key, None,
                            referenced=[baseline])
        for position in (1, 2, 3):
            data = json.dumps({'n': position}).encode()
            objects = {'sha256:' + __import__('hashlib').sha256(data).hexdigest(): data, 'sha256:' + 'a' * 64: b'x'}
            head = append_entry(self.ledger, entry('demo', position, head.digest, key, kind='ABSORPTION', obs=baseline,
                                                   absorption={'fence': None}), key, head.commit, objects=objects)
        self.head = head.commit

    def git(self, *args, data=None):
        return subprocess.run(['git', '-C', str(self.ledger), *args], input=data, capture_output=True,
                              check=True).stdout.decode('ascii').strip()

    def commit_with(self, listing):
        tree = self.git('mktree', '--missing', data=listing.encode())
        return self.git('commit-tree', tree, '-p', self.head, '-m', 'x')

    def test_the_bytes_order_and_parents_equal_the_per_object_reads(self):
        from ssds.ledger.read import read_chain, read_raw

        batched, oracle = read_raw(self.ledger, self.head), per_object_read_raw(self.ledger, self.head)
        self.assertEqual(batched, oracle)
        self.assertEqual([list(r.files) for r in batched], [list(r.files) for r in oracle], 'ls-tree order')
        self.assertTrue(any(p.startswith('objects/') for r in batched for p in r.files), 'a subtree is read')
        self.assertEqual(len(read_chain(self.ledger, 'demo').entries), 4)

    def test_one_process_reads_the_whole_chain(self):
        from ssds.ledger import read

        with patch.object(read.subprocess, 'run', side_effect=AssertionError('a process per object')):
            with patch.object(read.subprocess, 'Popen', wraps=read.subprocess.Popen) as popen:
                read.read_raw(self.ledger, self.head)
        self.assertEqual(popen.call_count, 1)

    def test_what_the_per_object_reads_rejected_is_rejected(self):
        from ssds.ledger.read import ChainRejected, read_raw

        blob = self.git('hash-object', '-w', '--stdin', data=b'kept')
        cases = {
            'a missing file': self.commit_with('100644 blob ' + 'b' * 40 + '\tentry.json\n'),
            'a submodule commit': self.commit_with(f'160000 commit {self.head}\tsub\n'),
            'a missing subtree': self.commit_with('040000 tree ' + 'c' * 40 + '\tobjects\n'),
            'a head that is a blob': blob,
            'an unknown head': 'd' * 40,
            'a head naming two objects': f'{self.head}\n{self.head}',
        }
        for name, head in cases.items():
            with self.subTest(name):
                with self.assertRaises(ChainRejected):
                    per_object_read_raw(self.ledger, head)
                with self.assertRaises(ChainRejected):
                    read_raw(self.ledger, head)

    def test_a_missing_parent_and_a_missing_repository_are_rejected(self):
        from ssds.ledger.read import ChainRejected, read_raw

        tree = self.git('rev-parse', self.head + '^{tree}')
        body = f'tree {tree}\nparent {"e" * 40}\nauthor a <a> 0 +0000\ncommitter a <a> 0 +0000\n\nx\n'
        orphan = self.git('hash-object', '-t', 'commit', '-w', '--literally', '--stdin', data=body.encode())
        for repo, head in ((self.ledger, orphan), (self.ledger.parent / 'absent.git', self.head)):
            with self.subTest(str(repo), head=head):
                with self.assertRaises(ChainRejected):
                    per_object_read_raw(repo, head)
                with self.assertRaises(ChainRejected):
                    read_raw(repo, head)


class StoredObjectEdges(unittest.TestCase):
    """The batched reader against the per-object oracle over literally written objects, in both object formats:
    tag peeling, ``ls-tree -r`` interleaving, entry types, malformed trees and nesting deeper than recursion."""

    def outcome(self, reader, repo, head):
        from ssds.ledger.read import ChainRejected
        try:
            return [(r.commit, r.parents, list(r.files.items())) for r in reader(repo, head)]
        except ChainRejected:
            return 'rejected'

    def build(self, fmt):
        import hashlib
        import tempfile
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        repo = Path(tmp.name) / 'r.git'
        subprocess.run(['git', 'init', '-q', '--bare', f'--object-format={fmt}', str(repo)], check=True)

        def git(*args, data=None):
            return subprocess.run(['git', '-C', str(repo), *args], input=data, capture_output=True,
                                  check=True).stdout.decode().strip()

        def obj(kind, body):
            return git('hash-object', '-t', kind, '--literally', '-w', '--stdin', data=body)

        def tree(*entries):
            return obj('tree', b''.join(m + b' ' + n + b'\0' + bytes.fromhex(o) for m, n, o in entries))

        def commit(tree_line, parents=()):
            body = tree_line + ''.join(f'parent {p}\n' for p in parents) + 'author a <a> 0 +0000\ncommitter a <a> 0 +0000\n\nm\n'
            return obj('commit', body.encode())

        entry = obj('blob', b'{"position": 0}')
        other = obj('blob', b'x')
        tag = obj('tag', f'object {other}\ntype blob\ntag t\ntagger a <a> 0 +0000\n\nt\n'.encode())
        sub = tree((b'100644', b'x', other))
        nested = tree((b'100644', b'a.txt', other), (b'40000', b'b', sub), (b'100644', b'c.txt', other),
                      (b'100644', b'entry.json', entry), (b'120000', b'link', other), (b'40755', b'odd', sub))
        valid = commit(f'tree {nested}\n')
        heads = {
            'interleaved subtrees, a symlink and an odd directory mode': valid,
            'a second entry on top': commit(f'tree {tree((b"100644", b"entry.json", other))}\n', [valid]),
            'an annotated tag of the head': obj('tag', f'object {valid}\ntype commit\ntag h\ntagger a <a> 0 +0000\n\nh\n'.encode()),
            'a file entry naming a tag of a blob': commit(f'tree {tree((b"100644", b"entry.json", entry), (b"100644", b"t", tag))}\n'),
            'two tree lines': commit(f'tree {nested}\ntree {sub}\n'),
            'a tree line after a parent line': commit(f'parent {valid}\ntree {nested}\n'),
            'a directory entry naming a blob holding tree bytes': commit(
                f'tree {tree((b"40000", b"d", obj("blob", b"100644 x" + bytes(1) + bytes.fromhex(other))))}\n'),
            'an empty name': commit(f'tree {tree((b"100644", b"", other))}\n'),
            'a mode digit 8': commit(f'tree {tree((b"100648", b"f", other))}\n'),
            'an abbreviated tree': commit(f'tree {nested[:12]}\n'),
            'an uppercase tree line': commit(f'tree {nested.upper()}\n'),
            'an empty mode': commit(f'tree {obj("tree", b" f" + bytes(1) + bytes.fromhex(other))}\n'),
            'a truncated entry': commit(f'tree {obj("tree", b"100644 f" + bytes(1) + bytes.fromhex(other)[:-1])}\n'),
        }
        width = 40 if fmt == 'sha1' else 64
        node = tree((b'100644', b'leaf', other))
        bodies = []
        for _ in range(1100):  # deeper than the recursion limit; one hash-object call writes them all
            body = b'40000 d\0' + bytes.fromhex(node)
            node = hashlib.new(fmt, b'tree %d\0' % len(body) + body).hexdigest()
            bodies.append(body)
        folder = Path(tempfile.mkdtemp(dir=Path(repo).parent))
        names = []
        for n, body in enumerate(bodies):
            (folder / str(n)).write_bytes(body)
            names.append(str(folder / str(n)))
        written = git('hash-object', '-t', 'tree', '--literally', '-w', '--stdin-paths', data='\n'.join(names).encode())
        self.assertEqual(written.split()[-1], node)
        self.assertEqual(len(node), width)
        heads['a 1,101-level nesting'] = commit(f'tree {tree((b"100644", b"entry.json", entry), (b"40000", b"deep", node))}\n')
        return repo, heads

    def test_the_batched_reader_equals_the_per_object_reads(self):
        from ssds.ledger.read import read_raw
        expected = {'interleaved subtrees, a symlink and an odd directory mode': 'read',
                    'a second entry on top': 'read', 'an annotated tag of the head': 'read',
                    'a file entry naming a tag of a blob': 'read', 'two tree lines': 'read',
                    'a 1,101-level nesting': 'read', 'an uppercase tree line': 'read'}
        for fmt in ('sha1', 'sha256'):
            repo, heads = self.build(fmt)
            for name, head in heads.items():
                with self.subTest(fmt=fmt, case=name):
                    oracle = self.outcome(per_object_read_raw, repo, head)
                    self.assertEqual(self.outcome(read_raw, repo, head), oracle)
                    self.assertEqual('read' if oracle != 'rejected' else 'rejected', expected.get(name, 'rejected'))
            order = [p for _, _, files in self.outcome(read_raw, repo, heads['interleaved subtrees, a symlink and an odd directory mode']) for p, _ in files]
            self.assertEqual(order, ['a.txt', 'b/x', 'c.txt', 'entry.json', 'link', 'odd/x'])

    def test_a_name_with_a_nul_is_rejected(self):
        from ssds.ledger.read import ChainRejected, read_raw
        repo, heads = self.build('sha1')
        with self.assertRaises(ChainRejected):
            read_raw(repo, heads['two tree lines'] + '\0junk')


class ImportFactReuse(unittest.TestCase):
    """Phase F cost inquiry: ``imports`` reuses facts only for the same path and exact bytes, within a bound on
    the retained objects' sizes."""

    def setUp(self):
        from collections import OrderedDict
        from ssds.analyzers import python

        self.python = python
        for name, value in (('_imports_retained', OrderedDict()), ('_imports_size', 0)):
            patcher = patch.object(python, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    SOURCES = {
        'pkg/sub/a.py': b'from . import b\nfrom ..c import d\nimport os\n',
        'other/a.py': b'from . import b\nfrom ..c import d\nimport os\n',
        'top.py': b'from ... import x\n',
        'dyn.py': b'import importlib\nimportlib.import_module("m")\n__import__("n")\neval("1")\n',
        'broken.py': b'def (:\n',
        'pkg/__init__.py': b'from .core import run\n',
    }

    def test_reused_facts_equal_fresh_analysis_and_depend_on_the_path(self):
        python = self.python
        first = {path: python.imports(path, data) for path, data in self.SOURCES.items()}
        with patch.object(python, '_imports', side_effect=AssertionError('reanalyzed')):
            again = {path: python.imports(path, data) for path, data in self.SOURCES.items()}
        self.assertEqual(again, first)
        self.assertEqual(first, {path: python._imports(path, data) for path, data in self.SOURCES.items()})
        self.assertNotEqual(first['pkg/sub/a.py'].modules, first['other/a.py'].modules, 'same bytes, other path')
        self.assertEqual(first['top.py'].markers, ('relative-import-above-package',))
        self.assertEqual(first['broken.py'], python.ImportFacts((), ('dynamic-code',)))
        self.assertEqual(first['dyn.py'].markers, ('dynamic-code', 'dynamic-import'))

    def test_changed_bytes_at_a_path_are_analyzed_afresh(self):
        python = self.python
        self.assertEqual(python.imports('m.py', b'import a\n').modules, ('a',))
        self.assertEqual(python.imports('m.py', b'import b\n').modules, ('b',))
        self.assertEqual(python.imports('m.py', b'import a\n').modules, ('a',))

    def test_the_retained_size_stays_within_the_budget_least_recent_first_out(self):
        python = self.python
        sizes = {}
        for n in range(4):
            data = f'import m{n}\n'.encode()
            python.imports(f'f{n}.py', data)
            sizes[n] = python._retained_size((f'f{n}.py', __import__('hashlib').sha256(data).digest()),
                                             python._imports(f'f{n}.py', data))
        budget = sizes[1] + sizes[2] + sizes[3]
        python._imports_retained.clear()
        python._imports_size = 0
        with patch.object(python, '_IMPORTS_BUDGET', budget):
            for n in range(4):
                python.imports(f'f{n}.py', f'import m{n}\n'.encode())
                self.assertLessEqual(python._imports_size, budget)
                self.assertEqual(python._imports_size, sum(size for _, size in python._imports_retained.values()))
            self.assertEqual([k[0] for k in python._imports_retained], ['f1.py', 'f2.py', 'f3.py'])
            python.imports('f1.py', b'import m1\n')  # a reuse makes it the most recent
            python.imports('f0.py', b'import m0\n')
            self.assertEqual([k[0] for k in python._imports_retained], ['f3.py', 'f1.py', 'f0.py'])
            big = b'\n'.join(f'import module_{n}'.encode() for n in range(2000))
            self.assertEqual(len(python.imports('big.py', big).modules), 2000, 'an oversized result is still exact')
            self.assertNotIn('big.py', [k[0] for k in python._imports_retained], 'and is not retained')


if __name__ == '__main__':
    unittest.main()

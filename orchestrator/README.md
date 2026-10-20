# ssds

One program, `ssds`: one distribution, one import package and one command
(SSDS 8 Architecture Manual §26.3).

- **Level 0 Core** (`ssds.core`) renders one complete, copy/paste-ready,
  profile-correct Scientific Software Development Protocol prompt for a configured
  target repository. Core alone is a finished operating mode: it needs no database,
  agent process, model catalog, quota meter, or scheduler. Frozen profiles stay
  packaged, and workplan version binding prevents silent reinterpretation across
  versions.
- **SSDS 8 components** (`ssds.content`, `ssds.analyzers`, `ssds.ledger`,
  `ssds.derivation`, `ssds.admission`, `ssds.dispatcher`, `ssds.interface`), one
  per component of [the Architecture Manual](docs/ssds-8.0-architecture.md) §26.1.
  **Shadow implementation only**: they hold no authority over any subject and
  never gate document control.

See [the Core user guide](docs/core-user-guide.md) for installation,
configuration, stages and the full command reference.

```bash
pip install ./orchestrator            # from a checkout of this repository
ssds doctor
ssds software-implementation --workplan workplans/active/MY-WORKPLAN.md

# checkout development, without installing
python3 orchestrator/bin/ssds --help
```

Both forms run the one composition root, `ssds.cli:main`, which mounts Core's
commands and, as they are built, the SSDS operations in one flat command set.
Operator configuration and data live in the SSDS home (`$SSDS_HOME`, by default
`~/.ssds`), outside every repository.

Public contracts are `ssds.core.api.v1` and `ssds.core.spi.v1` for Core, and
`ssds.api.v1` and `ssds.spi.v1` for SSDS; other modules are implementation
detail. Other extensions register through the entry-point group
`ssds.extensions.v1`.

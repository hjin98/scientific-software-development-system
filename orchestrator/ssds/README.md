# sdp-orchestrator-ssds

SSDS 8, the graph-native deterministic orchestration system, as an extension of
the SDP Orchestrator Core (`sdp-orchestrator-core`). Its architecture is
[the SSDS 8 Architecture Manual](../docs/ssds-8.0-architecture.md).

**Shadow implementation only.** This distribution holds no authority over any
subject: it derives, renders and records beside document control and never gates
it. The document-controlled protocol baseline keeps governing.

The distribution registers one Core extension, `sdp.ssds`, through Core's
entry-point group `sdp_orchestrator.extensions.v1`. Core never imports it.

| Package | Component (Manual §26.1) |
|---|---|
| `sdp_orchestrator.ssds.content` | Content Model |
| `sdp_orchestrator.ssds.analyzers` | Analyzers |
| `sdp_orchestrator.ssds.ledger` | Ledger Store |
| `sdp_orchestrator.ssds.derivation` | Derivation Engine |
| `sdp_orchestrator.ssds.admission` | Admission |
| `sdp_orchestrator.ssds.dispatcher` | Dispatcher |
| `sdp_orchestrator.ssds.interface` | Interface |

Public surfaces are `sdp_orchestrator.ssds.api.v1` and `sdp_orchestrator.ssds.spi.v1`.

Acceptance, from the repository root (Manual §26.2 fitness checks and the
installed registration):

```bash
python -m pip install ./orchestrator ./orchestrator/ssds -r orchestrator/requirements-dev.txt
python -m unittest discover -s orchestrator/ssds/tests -t orchestrator/ssds -v
```

"""Derivation Engine (Manual §26.1): the four strata S0-S3 and every query over
them. A pure function of the ledger prefix and the content it names (§5.1):
never writes canonical state, chooses the current prefix or reads the live
integration ref, the clock, the network or the environment (§26.2).

``derive(chain, trees)`` is the entry point: ``trees`` maps a commit identity to
its content tree, so derivation itself reads no Git. ``consequences`` adds the
S3 kernel. A derivation checkpoint (``History.checkpoint``) resumes the S0 fold
and equals derivation from scratch; storing it is its caller's.
"""

from . import queries
from .baseline import BaselineStructure, baseline_structure
from .history import DERIVATION_VERSION, CheckpointInvalid, History, TreeSource
from .reports import allowed_outcomes
from .s3 import Consequences, Finding, Obligation
from .state import F, P, Policy, T, State
from .support import Support
from .workflow import Workflow


def derive(chain, trees: TreeSource, position: int | None = None, checkpoint: bytes | None = None) -> Support:
    """The derived state ``D_n`` of a verified chain at ``position`` (default: the last readable position)."""

    return Support(State(History(chain, trees, checkpoint), position))


def consequences(chain, trees: TreeSource, position: int | None = None, checkpoint: bytes | None = None) -> Consequences:
    """``D_n`` with its S3 kernel: findings, obligations and whether the view may assert currentness."""

    return Consequences(derive(chain, trees, position, checkpoint))


__all__ = [
    "BaselineStructure", "CheckpointInvalid", "Consequences", "DERIVATION_VERSION", "F", "Finding", "History",
    "Obligation", "P", "Policy", "State", "Support", "T", "TreeSource", "Workflow", "allowed_outcomes", "queries", "baseline_structure", "consequences",
    "derive",
]

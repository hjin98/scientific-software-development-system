"""Derivation Engine (Manual §26.1): the four strata S0-S3 and every query over
them. A pure function of the ledger prefix and the content it names (§5.1):
never writes canonical state, chooses the current prefix or reads the live
integration ref, the clock, the network or the environment (§26.2).
"""

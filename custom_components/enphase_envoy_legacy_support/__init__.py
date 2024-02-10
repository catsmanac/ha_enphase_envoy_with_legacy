"""Initializaion Stub for Enphase Envoy integration with support for legacy.

This custom integration uses the Enphase Envoy core integration and registers
an additional updater that reads production data from legacy envoy html pages.
Code here are stubs required to use the core integration that don't change core
and a modified async_setup_entry that has added the registeration off the
legacy_updater with the Envoy after it's initiated.
"""
from __future__ import annotations

from pyenphase import Envoy, register_updater

from .legacy_updater import LegacyProductionScraper

### start of addition to original core enphase_envo.__init__ ###
# register the updater to get production data from envoy legacy html pages.
register_updater(LegacyProductionScraper)
### end of addition to original core enphase_envo.__init__ ###

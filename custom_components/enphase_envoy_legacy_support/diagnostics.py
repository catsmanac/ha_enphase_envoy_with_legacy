"""Diagnostics support for Enphase Envoy.

This custom integration registers an HTML updater with Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
can collect data from legacy Envoy devices with firmware < 3.9 as well.
"""
from __future__ import annotations

from typing import Any

from attr import asdict

from homeassistant.config_entries import ConfigEntry

from pyenphase.envoy import get_updaters
from pyenphase.updaters.base import EnvoyUpdater

from .legacy_updater import LegacyProductionScraper

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""

    updaters: list[type[EnvoyUpdater]] = get_updaters()
    legacy_registered = (LegacyProductionScraper in updaters)


    diagnostic_data: dict[str, Any] = {
        "config_entry": entry.as_dict(),
        "LegacyProductionScraper_registered": legacy_registered,
    }

    return diagnostic_data

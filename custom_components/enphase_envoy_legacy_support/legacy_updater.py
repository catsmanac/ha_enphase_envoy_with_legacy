"""HTML Scraper Updater for Pyenphase / Enphase Envoy solar energy monitor.

This custom integration registers an HTML updater with Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
can collect data from legacy Envoy devices with firmware < 3.9 as well.
"""
from __future__ import annotations

import re

from pyenphase import EnvoyData, EnvoySystemProduction
from pyenphase.const import URL_PRODUCTION, SupportedFeatures
from pyenphase.exceptions import ENDPOINT_PROBE_EXCEPTIONS
from pyenphase.updaters.base import EnvoyUpdater

# rgerex keys to read production data from legace (fw <= 3.7) html pages
_KEY_TO_REGEX = {
    "watts_now": r"<td>Current.*</td>\s*<td>\s*(\d+|\d+\.\d+)\s*(W|kW|MW)</td>",
    "watt_hours_last_7_days": r"<td>Past Week</td>\s*<td>\s*(\d+|\d+\.\d+)\s*(Wh|kWh|MWh)</td>",
    "watt_hours_today": r"<td>Today</td>\s*<td>\s*(\d+|\d+\.\d+)\s*(Wh|kWh|MWh)</td>",
    "watt_hours_lifetime": r"<td>Since Installation</td>\s*<td>\s*(\d+|\d+\.\d+)\s*(Wh|kWh|MWh)</td>",
}

_PAGE_TEXT_KEY = "Since Installation"


class LegacyEnvoySystemProduction(EnvoySystemProduction):
    """Get production data from envoy legacy html."""

    @classmethod
    def from_production_legacy(cls, text: str) -> EnvoySystemProduction:
        """Parse Legacy envoy html into EnvoySystemProduction dataclass."""
        data: dict[str, int] = {
            "watts_now": 0,
            "watt_hours_today": 0,
            "watt_hours_last_7_days": 0,
            "watt_hours_lifetime": 0,
        }
        for key, regex in _KEY_TO_REGEX.items():
            if match := re.search(regex, text, re.MULTILINE):
                unit = match.group(2).lower()
                value = float(match.group(1))
                # scale to w or wh
                if unit.startswith("k"):
                    value *= 1000
                elif unit.startswith("m"):
                    value *= 1000000
                data[key] = int(value)
        return cls(**data)


class LegacyProductionScraper(EnvoyUpdater):
    """Updater for Envoy legacy html."""

    async def probe(
        self, discovered_features: SupportedFeatures
    ) -> SupportedFeatures | None:
        """Probe the Envoy for legacy html and return PRODUCTION SupportedFeatures."""
        if SupportedFeatures.PRODUCTION in discovered_features:
            # Already discovered from another updater, leave alone
            return None
        try:
            response = await self._probe_request(URL_PRODUCTION)
            data = await response.text()
        except ENDPOINT_PROBE_EXCEPTIONS:
            return None
        # text should contain some key words to validate
        if _PAGE_TEXT_KEY not in data:
            return None
        # Signal back we can provide production data
        self._supported_features |= SupportedFeatures.PRODUCTION
        return self._supported_features

    async def update(self, envoy_data: EnvoyData) -> None:
        """Provide the Envoy Production data from the legacy HTML Page."""
        response = await self._request(URL_PRODUCTION)
        production_data = await response.text()
        envoy_data.raw[URL_PRODUCTION] = production_data
        envoy_data.system_production = (
            LegacyEnvoySystemProduction.from_production_legacy(production_data)
        )

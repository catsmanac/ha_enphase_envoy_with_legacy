"""Configuration for Enphase Envoy Legacy Support.

This custom integration registers an HTML updater with the Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
can collect data from legacy Envoy devices with firmware < 3.9 as well.
"""
import logging
from typing import Any

from homeassistant import config_entries

from .const import CONF_UPDATER, DOMAIN, NAME, UNIQUE_ID
from .legacy_updater import LegacyProductionScraper

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Enphase Envoy legacy support config flow."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        if not self.unique_id:
            await self.async_set_unique_id(UNIQUE_ID)
        if self.unique_id:
            self._abort_if_unique_id_configured(error="single_instance_allowed")
        return self.async_create_entry(
            title=NAME,
            data={CONF_UPDATER: LegacyProductionScraper.__name__}
        )

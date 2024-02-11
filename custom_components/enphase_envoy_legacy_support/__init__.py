"""Initialization for Enphase Envoy Legacy Support.

This custom integration registers an HTML updater with the Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
can collect data from legacy Envoy devices with firmware < 3.9 as well.
"""
from __future__ import annotations

import logging

from pyenphase import register_updater
from pyenphase.envoy import get_updaters
from pyenphase.updaters.base import EnvoyUpdater

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN
from .legacy_updater import LegacyProductionScraper

# Use empty_config_schema because the component does not have any config options
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigEntry):
    """Register the LegacyProductionScraper with Pyenphase module."""
    updaters: list[type[EnvoyUpdater]] = get_updaters()
    if LegacyProductionScraper not in updaters:
        if _LOGGER.level == logging.DEBUG:
            _LOGGER.debug("Registering LegacyProductionScraper in Pyenphase")
        register_updater(LegacyProductionScraper)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Enphase Envoy legacy support from a config entry."""
    return True

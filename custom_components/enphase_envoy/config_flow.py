"""Config flow Stub for Enphase Envoy integration with support for legacy.

This custom integration uses the Enphase Envoy core integration and registers
an additional updater that reads production data from legacy envoy html pages.
Code here are stubs required to use the core integration and do not change core.
"""
from __future__ import annotations

import logging

from pyenphase import Envoy

import homeassistant.components.enphase_envoy.config_flow as cf
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


async def validate_input(
    hass: HomeAssistant, host: str, username: str, password: str
) -> Envoy:
    """Validate the user input using core Enphase Envoy integration."""
    return await cf.validate_input(hass, host, username, password)


class ConfigFlow(cf.ConfigFlow):
    """Stub to Handle a config flow using core Enphase Envoy integration."""

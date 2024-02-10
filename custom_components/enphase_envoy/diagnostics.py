"""Diagnostics Stub for Enphase Envoy solar energy monitor with support for legacy.

This custom integration uses the Enphase Envoy core integration and registers
an additional updater that reads production data from legacy envoy html pages.
Code here are stubs required to use the core integration and do not change core.
"""
from typing import Any

import homeassistant.components.enphase_envoy.diagnostics as ee_diagnostics
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

# this is a stub and just uses the Enphase_Envoy Core component
async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Use core enphase envoy integration diagnostics."""
    return await ee_diagnostics.async_get_config_entry_diagnostics(hass, entry)

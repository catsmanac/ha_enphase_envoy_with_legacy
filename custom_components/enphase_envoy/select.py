"""Select Stub for Enphase Envoy solar energy monitor with support for legacy.

This custom integration uses the Enphase Envoy core integration and registers
an additional updater that reads production data from legacy envoy html pages.
Code here are stubs required to use the core integration and do not change core.
"""
import homeassistant.components.enphase_envoy.select as ee_select
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


# this is a stub and just uses the Enphase_Envoy Core component
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up core enphase envoy integration select platform."""
    await ee_select.async_setup_entry(hass, config_entry, async_add_entities)

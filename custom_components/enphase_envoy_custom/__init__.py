"""Initializaion Stub for Enphase Envoy integration with support for legacy.

This custom integration uses the Enphase Envoy core integration and registers
an additional updater that reads production data from legacy envoy html pages.
Code here are stubs required to use the core integration that don't change core
and a modified async_setup_entry that has added the registeration off the
legacy_updater with the Envoy after it's initiated.
"""
from __future__ import annotations

from pyenphase import Envoy, register_updater

import homeassistant.components.enphase_envoy.__init__ as ee_init
from homeassistant.components.enphase_envoy.const import DOMAIN, PLATFORMS
from homeassistant.components.enphase_envoy.coordinator import EnphaseUpdateCoordinator
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.httpx_client import get_async_client

from .legacy_updater import LegacyProductionScraper


# this is an as-is copy of the core enphase envoy with added the registration of the updater
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Enphase Envoy from a config entry."""

    host = entry.data[CONF_HOST]
    envoy = Envoy(host, get_async_client(hass, verify_ssl=False))

    ### start of addition to original core enphase_envo.__init__ ###
    # register the updater to get production data from envoy legacy html pages.
    register_updater(LegacyProductionScraper)
    ### end of addition to original core enphase_envo.__init__ ###

    coordinator = EnphaseUpdateCoordinator(hass, envoy, entry)

    await coordinator.async_config_entry_first_refresh()
    if not entry.unique_id:
        hass.config_entries.async_update_entry(entry, unique_id=envoy.serial_number)

    if entry.unique_id != envoy.serial_number:
        # If the serial number of the device does not match the unique_id
        # of the config entry, it likely means the DHCP lease has expired
        # and the device has been assigned a new IP address. We need to
        # wait for the next discovery to find the device at its new address
        # and update the config entry so we do not mix up devices.
        raise ConfigEntryNotReady(
            f"Unexpected device found at {host}; expected {entry.unique_id}, "
            f"found {envoy.serial_number}"
        )

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Stub Unload a config entry using core Enphase ENvoy integration."""
    return await ee_init.async_unload_entry(hass, entry)


async def async_remove_config_entry_device(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry
) -> bool:
    """Stub to Remove an enphase_envoy config entry from a device.

    use core Enphase Envoy integration to remove config entry.
    """
    return await ee_init.async_remove_config_entry_device(
        hass, config_entry, device_entry
    )

"""The enphase_envoy_with_legacy component.

This custom integration registers an HTML updater with Pyenphase module used
by the HA Core Enphase Envoy integration. When registered, the HA Enphase Envoy
can collect data from legacy Envoy devices with firmware < 3.9 as well.
"""
DOMAIN = "enphase_envoy_legacy_support"

CONF_UPDATER = "updater"

NAME = "Enphase Envoy Legacy HTML support"

UNIQUE_ID = f"{DOMAIN}_for_enphase_envoy"

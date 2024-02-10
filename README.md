# Enphase Envoy (+HTML Extension)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration#readme)

This is a HACS custom integration providing a Envoy Legacy HTML production data extension to the [Home Assistant Core Enphase Envoy integration](https://www.home-assistant.io/integrations/enphase_envoy) for [enphase envoys/IQ Gateways](https://enphase.com/en-us/products-and-services/envoy-and-combiner).

It is using the Enphase_Envoy integration code directly from HA Core and registers an updater to it. The updater adds support to obtain production data from Legacy Envoys running firmware's before 3.9 which only provide HTML based information. As the HA Core integration is used under the hood, all newer Envoys supported by the HA Core integration are supported as well.

You should only deploy this custom integration when running an Enphase Envoy legacy model with firmware before 3.9, either stand-alone or in a mixed environment with newer models.

Only use with Home Assistant 2023.12 or newer.

## Installation

1. Make appropriate backups of you Home Assistant installation and data.
2. Install [HACS](https://hacs.xyz/) if you haven't already
3. Add this GITHUB repository as a [custom integration repository](https://hacs.xyz/docs/faq/custom_repositories) in HACS
4. Restart home assistant
5. Go to the HACS Integrations page in HA, select the custom repository and download the `Enphase Envoy (+HTML extension)` custom integration
6. After download restart Home Assistant.
7. If you are not yet using the Enphase Envoy integration, add the integration through the home assistant configuration flow and the [Enphase Envoy integration](https://www.home-assistant.io/integrations/enphase_envoy#envoy-authentication-requirements)

If you decide to install this manually without the use of HACS, then make sure to only place the files in custom_components/enphase_envoy from this repository into the folder /config/custom_components/enphase_envoy on your Home Assistant system.

As this custom integration is using the HA core enphase envoy integration, it is compatible with that. If you used an other custom integration before, compatibility may differ and entities may restart their history from scratch again with different names, may not exist anymore and new ones may show up, or all may work just fine.

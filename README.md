[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration#readme)

This is a HACS custom integration providing a Legacy HTML production data extension to the [Home Assistant Core Enphase Envoy integration](https://www.home-assistant.io/integrations/enphase_envoy) for [enphase envoys/IQ Gateways](https://enphase.com/en-us/products-and-services/envoy-and-combiner).

It is using the actual Enphase_Envoy integration code (no copy) from HA Core and registers an updater to it which adds support to obtain production data from Legacy Envoys running firmwares before 3.9 which only provide HTML based information. As the HA Core integration is used under the hood, all newer Envoys supported by the HA Core integration are support as well.

Only use with Home Assistant 2023.12 or newer.

# Installation

1. Make appropriate backups of you Home Assistant installaion and data.
2. Install [HACS](https://hacs.xyz/) if you haven't already
3. Add this repository as a [custom integration repository](https://hacs.xyz/docs/faq/custom_repositories) in HACS
4. Restart home assistant
5. Go to the HACS Integrations page in HA, select the custom repository and download the `Enphase Envoy (with Legacy HTML extension)` custom integration
6. After download restart Home Assistant.
7. Add the integration through the home assistant configuration flow and the [Enphase Envoy integration](https://www.home-assistant.io/integrations/enphase_envoy#envoy-authentication-requirements)

If you decide to install this manually without the use of HACS, then make sure to only place the files in custom_components/enphase_envoy_custom from this repository into the folder /config/custom_components/enphase_envoy on your Home Assistant system.

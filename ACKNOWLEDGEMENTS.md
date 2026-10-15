# Acknowledgements

Apple + Google Tracking Server brings existing community projects together; it
does not claim authorship of their protocols, research, providers or tools.
Thank you to the maintainers and contributors whose work makes this possible.

## Finding-network foundations

| Project | Maintainer / team | Role in this project |
| --- | --- | --- |
| [OpenHaystack](https://github.com/seemoo-lab/openhaystack) | SEEMOO Lab and contributors | Foundational research and tooling for custom Apple Find My-compatible Bluetooth trackers |
| [macless-haystack](https://github.com/dchristl/macless-haystack) | dchristl and contributors | Apple report-retrieval provider and account flow used by the Apple integration |
| [GoogleFindMyTools](https://github.com/leonboe1/GoogleFindMyTools) | leonboe1 and contributors | Google Find Hub research, custom-tracker registration, report decryption and EID maintenance |
| [google-find-hub-sync](https://github.com/traccar/google-find-hub-sync) | Traccar and contributors | Maintained GoogleFindMyTools fork used as the Google provider base |
| [anisette-v3-server](https://github.com/Dadoum/anisette-v3-server) | Dadoum and contributors | External Apple authentication helper, pulled directly from upstream |

The optional **Traccar Server** map integration is distinct from the Google
provider fork above. A separate Traccar Server is never required to use this app.

## Maps, flashing and development tools

| Project | Role |
| --- | --- |
| [Leaflet](https://leafletjs.com/) | Interactive web map |
| [OpenStreetMap contributors](https://www.openstreetmap.org/copyright) | Map data; preserve visible map attribution |
| [DAP.js](https://github.com/ARMmbed/dapjs) | Browser CMSIS-DAP/WebUSB communication |
| [pyOCD](https://github.com/pyocd/pyOCD) | Nordic target flash-algorithm basis and portable local flashing tool |
| [esp-web-flasher](https://github.com/NabuCasa/esp-web-flasher) | Browser ESP flashing, with the Adafruit/Toit/NabuCasa lineage noted in the bundled license |
| [esptool-js](https://github.com/espressif/esptool-js) and [esptool](https://github.com/espressif/esptool) | Espressif flashing tools |
| [Zephyr](https://www.zephyrproject.org/), [Nordic Semiconductor](https://www.nordicsemi.com/) and [PlatformIO](https://platformio.org/) | Optional firmware platform and build ecosystem |
| [IceWhaleTech app-store builder](https://github.com/IceWhaleTech/build-appstore-action) | Native ZimaOS catalog generation |

The Python server also depends on Flask, Waitress, Requests, cryptography and
Eclipse Paho MQTT. Exact versions are pinned in the application's requirements;
transitive dependencies retain their own notices.

## What this repository adds

This project adds the multi-user web interface, local history, reversible unified
views, Google raw/reliable-location analysis, account isolation, provider setup
bridges, optional MQTT/Traccar integration, deployment recipes and firmware UI.
These additions do not imply endorsement by upstream authors, Apple or Google.

See [licensing and corresponding sources](docs/LICENSING.md) for provider source
archives and attribution boundaries. Vendored code retains its original notices;
credits here are not a replacement for license files shipped with that code.

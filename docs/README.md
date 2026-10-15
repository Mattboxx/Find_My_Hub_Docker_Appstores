# Documentation

[Project overview](../README.md) · [Support on Ko-fi](https://ko-fi.com/mattboxx)

Start with the user guide, then choose the reference for your task. English is
the primary documentation language. Screenshots use synthetic demonstration data.

## Using and operating the server

| Guide | Contents |
| --- | --- |
| [Illustrated user guide](USER_GUIDE.en.md) | Sign-in, map, history, devices, users and integrations |
| [Installation and operations](INSTALLATION.md) | Recommended All-in-One, legacy modular, first run, backups and migration |
| [Native stores and panels](STORES.md) | ZimaOS/CasaOS JSON source, Portainer, Umbrel and Runtipi |
| [Workflow demonstrations](WORKFLOWS.md) | Short walkthroughs with full-size screenshots |
| [Screenshot gallery](screenshots/README.md) | All 19 interface demonstrations |
| [Animated tours](demos/README.md) | Map/history, Nordic/ESP32 programming, configured libraries and still alternatives |
| [Google reliable locations](GOOGLE_RELIABLE_LOCATION.md) | Raw archive, derived analysis, classifications and parameters |
| [Interface languages](LOCALIZATION.md) | Translation scope, persistence and maintenance |
| [Licensing and source notices](LICENSING.md) | Project license, provider licenses and corresponding sources |
| [Upstream acknowledgements](../ACKNOWLEDGEMENTS.md) | Foundational projects and the role of each integration |

<details>
<summary>Italian documentation</summary>

[Guida illustrata in italiano](USER_GUIDE.it.md).

</details>

## Releases

Read the [1.1.22 release notes](RELEASE_1.1.22.md) for the current stable release.
Earlier notes remain versioned here; they describe historical changes rather
than the recommended installation procedure. For current commands use the
installation guide above.

## Catalog maintenance

See the [contribution and branch workflow](../CONTRIBUTING.md) before editing
the catalog. `main` is source; `gh-pages` is generated publication output.

| Path | Purpose |
| --- | --- |
| `compose.yaml` | Complete modular stack, not a web-only recipe |
| `all-in-one/` | Bundle recipe and operational guide |
| `Apps/FindMyHub/` | Native CasaOS/ZimaOS app and icon |
| `adapters/` | Umbrel and Runtipi manifests |
| `portainer/` | Portainer templates |
| `scripts/` | Catalog metadata/Compose verification |
| `.github/workflows/` | Catalog validation and immutable publication |

This is the public installation catalog, not a copy of the private application
source. Keep app IDs, source IDs and existing immutable version snapshots stable.
Do not add runtime data, credentials, personalized firmware or production maps.
Application source is maintained in the private
[`Apple-Google-Tracking-Server`](https://github.com/Mattboxx/Apple-Google-Tracking-Server)
repository. The original catalog URL remains unchanged for installed store sources.
- [Project names and compatibility](BRANDING.md)

# Find My Hub Docker App Stores

Catalog installation resources use immutable `catalog-X.Y.Z` snapshots to
prevent a cached Compose file from being mixed with newer app metadata. The
subscription URL remains `@gh-pages/store.json`; metadata/Compose changes
intended for installation require a new app version. CDN index propagation
can still take time, but each newly indexed release references its own files.

Multi-platform Docker app-store repository for **Find My Hub**. It contains one
portable Compose stack plus store-specific adapters; it is not tied to ZimaOS.

Find My Hub brings the Apple/Google trackers you own into one self-hosted map,
preserves local history and lets separate accounts share a server. It combines
existing finding networks; it does not replace them or guarantee real-time GPS.

![Find My Hub — synthetic demonstration data](docs/screenshots/02-map.jpg)

[English illustrated guide](docs/USER_GUIDE.en.md) ·
[Guida illustrata italiana](docs/USER_GUIDE.it.md) ·
[Complete feature gallery](docs/screenshots/README.md).

## Current release: 1.1.17

Stable Google reliable locations above immutable raw reports, with clustering,
consensus, anti-teleport candidates, confidence and STALE status. Choose Optimized,
Raw or Both; consult the complete paginated archive. Developer controls sit at
the bottom of the device panel and global parameters belong to administrator Setup.
MQTT/Traccar current states use the reliable Google anchor. Existing accounts,
volumes, keys, Apple behavior and firmware remain valid and unchanged.
Includes illustrated bilingual guides and 19 reviewed synthetic-data screenshots.
[Algorithm, defaults, API and migration guide](docs/GOOGLE_RELIABLE_LOCATION.md).

## What you can do

- Compare source-aware maps, navigate sightings, inspect timestamps/accuracy
  and open external navigation apps.
- Hide/show, color, rename and explicitly reorder devices on desktop/mobile.
- Combine two or more same-account trackers reversibly, retaining every member's
  full history and settings.
- Generate identities before choosing to add a device, rotate keys with explicit
  confirmation, and hand prefilled identities to firmware tools.
- Share isolated accounts; admins assign owners and alone manage provider
  connections, onboarding, infrastructure and user roles.
- Poll with the browser closed; optionally publish MQTT/Home Assistant discovery
  or forward entities to an existing Traccar Server.
- Export selected devices or download a full administrator web-data backup;
  preserve data on updates and migrate legacy installations.
- Configure/flash Nordic and ESP32 boards or download portable ZIPs; integrate
  the optimized configured FindMyAdv library into an existing ESP32 project.
- Use persistent English/Italian UI, mobile history controls and home-screen icons.

The web source repository stays **private**. This already-public catalog contains
metadata, guides and synthetic images, not personal runtime data. Existing public
container packages remain anonymously installable. Docker images contain app code:
repository privacy is not encryption. Never publish provider authentication volumes
or personalized firmware/backup ZIPs.

## Previous release highlights

Version **1.1.14** adds a complete administrator web-data backup with bilingual
restore instructions, fixes imported device settings, and corrects optional
Radioland accelerometer selection. It retains the Apple per-identity polling
fix. The store checks and refreshes every architecture-specific Compose file,
preventing mixed-version catalog updates. Existing volumes and keys stay valid.
Radioland button/LED pins still require testing on the affected PCB revision;
the LED hardware problem is not claimed resolved.
The matching release also supplies provider controller/patch sources and build
recipes in a separate source ZIP. The main web repository remains private.

Version **1.1.13** fixes older Apple trackers losing updates after adding another
tracker: the web requests each identity separately because Apple's multi-key
responses can contain reports for only one tracker. Failures are isolated per
device. Update the existing app, including its web image. Keep current volumes
and keys; no tracker re-registration or firmware flashing is required. This fix
also benefits installations using standard external Apple providers.

## Compatibility

| Platform | Entry point | Installation |
| --- | --- | --- |
| Docker, Docker Desktop, Dockge and Compose-compatible panels | `compose.yaml` | Import or run the Compose file |
| CasaOS / ZimaOS | `Apps/FindMyHub` | Register the published v2 `store.json` URL |
| Portainer | `portainer/templates.json` | Use the raw JSON URL as an App Templates URL |
| Umbrel Community App Store | `adapters/umbrel/` | Publish/fork this directory as an Umbrel community store |
| Runtipi | `adapters/runtipi/apps/find-my-hub/` | Publish/fork the adapter in a Runtipi app store |

Store formats are not standardized. The generic Compose file covers products
that can import Compose; native one-click stores require their own small
manifest, all kept in this repository.

## Generic Docker installation

```bash
git clone https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores.git
cd Find_My_Hub_Docker_Appstores
docker compose up -d
```

Open `http://HOST:8125`. Optional variables are `FINDMY_WEB_PORT`,
`APPLE_SETUP_TOKEN`, `GOOGLE_TOKEN`, `RETENTION_DAYS`, and `REFRESH_INTERVAL`.
Both provider tokens may remain empty on a trusted local network.

The catalog does not bundle or require Traccar. A standard existing Traccar
Server can be enabled later from the administrator **Setup → Traccar map**
card. If disabled or unreachable, Find My Hub continues to manage providers,
users, history, MQTT, unified views, and its own map independently.

## CasaOS / ZimaOS

Current ZimaOS versions use the v2 static catalog protocol. In
**App Store -> Add Source**, register the complete JSON source URL:

```text
https://cdn.jsdelivr.net/gh/Mattboxx/Find_My_Hub_Docker_Appstores@gh-pages/store.json
```

The generated `store.json`, `index.json`, application manifests, and assets
are published automatically from the `main` branch. The GitHub source archive
and the old `main.zip` address are not v2 catalog sources and must not be
registered on current ZimaOS releases.

If the old source is already saved, remove it before adding the new URL. ZimaOS
may cache external stores for several minutes; after adding the source, wait
for its refresh cycle or restart the App Store service once.

## Portainer

Set **App Templates URL** to:

```text
https://raw.githubusercontent.com/Mattboxx/Find_My_Hub_Docker_Appstores/main/portainer/templates.json
```

The template deploys the root `compose.yaml` stack.

## Umbrel and Runtipi

The Umbrel-compatible store descriptor and app are in `adapters/umbrel/`. The
Runtipi adapter is in `adapters/runtipi/apps/find-my-hub/`. These formats
are ready for testing and for submission/forking into their respective
community catalogs; approval in an official third-party catalog remains under
that catalog's maintainers.

## Container image requirement

One-click installation requires anonymous access to these multi-architecture
images:

- `ghcr.io/mattboxx/find-my-web:1.1.17`
- `ghcr.io/mattboxx/find-my-apple-provider:1.1.17`
- `ghcr.io/mattboxx/find-my-google-provider:1.1.17`

All three images are public and expose `linux/amd64` and `linux/arm64`
manifests. The CI validates every JSON and Compose manifest, builds the ZimaOS
v2 catalog, and performs an anonymous manifest request for every image. Loss
of public access is a blocking validation error because it would break
one-click installation.

The upstream Anisette dependency is pinned by multi-architecture manifest
digest in every adapter, so installing the immutable catalog version cannot
silently pull different upstream code later.

## Local validation

```bash
docker compose -f compose.yaml config --quiet
docker compose -f Apps/FindMyHub/docker-compose.yml config --quiet
APP_DATA_DIR=/tmp/find-my-hub docker compose -f adapters/umbrel/find-my-hub/docker-compose.yml config --quiet
APP_DATA_DIR=/tmp/find-my-hub docker compose -f adapters/runtipi/apps/find-my-hub/docker-compose.yml config --quiet
```

Find My Hub uses unofficial, reverse-engineered Apple and Google integrations.
It is not affiliated with Apple or Google. Use dedicated accounts and trackers
you own.

# Find My Hub

One self-hosted map for the Apple Find My and Google Find Hub trackers you own.
Keep local history, compare provider reports, manage separate user accounts and
optionally connect MQTT/Home Assistant or an existing Traccar Server.

> **Choose a deployment layout, not a different product.**
> The modular stack and All-in-One offer the same tracking interface and features.
> The default store app is the **modular stack**. It does not silently switch to All-in-One.

## Start here: which installation do you want?

| | A · Modular stack | B · All-in-One bundle |
| --- | --- | --- |
| Find My Hub containers | **3:** web, Apple provider, Google provider | **1:** web + Apple + Google together |
| Anisette for Apple | Separate upstream container | Separate upstream container |
| Total with both providers | **4 containers** | **2 containers** |
| Image names | `find-my-web`, `find-my-apple-provider`, `find-my-google-provider` | **`apple-google-tracking-server`** |
| Updates | Each service can be updated/restarted independently | The three bundled services update together |
| Best fit | Existing installations, native store installs, independent services | A new server where you prefer fewer containers |
| Installation | [Modular instructions](#option-a--modular-stack-4-containers) | [All-in-One instructions](#option-b--all-in-one-2-containers) |

**Italiano in breve:** “tre container separati” significa tre container Find My
Hub **più Anisette: quattro in totale**. All-in-One raccoglie web, Apple e Google
in un container **più Anisette: due in totale**. Le funzioni sono le stesse.
L'app dello store rimane modulare; nessuna migrazione viene fatta da sola.
[Guida completa italiana](docs/USER_GUIDE.it.md).

![Deployment comparison: modular has four containers; All-in-One has two](docs/images/deployment-options.svg)

Anisette is an Apple authentication helper, not a fourth tracking provider.
It stays in its original upstream image in **both** layouts; it is not embedded
in our bundle. Fewer containers do not automatically mean less RAM, a smaller
download, or less Apple/Google account configuration.

Already have compatible standard providers? You can run **only the web image**
and connect it to those services. See [existing-provider compatibility](#existing-standard-providers-web-only).
MQTT and Traccar are optional in every layout.

## See the application

![Find My Hub map — synthetic demonstration devices and locations](docs/screenshots/02-map.jpg)

**A map and durable history, not a live GPS guarantee.** BLE trackers advertise
near contributing phones; Apple/Google finding networks collect sightings.
Provider services fetch the reports and Find My Hub polls them into local
storage. Closing the browser does not stop server polling.

All screenshots below use synthetic demonstration accounts, identities and
locations. They show workflows, **not proof of live provider connectivity**.
Never publish your real map, identity keys, credentials or backup files.

[English illustrated guide](docs/USER_GUIDE.en.md) ·
[Guida illustrata italiana](docs/USER_GUIDE.it.md) ·
[All 19 demonstration screenshots](docs/screenshots/README.md) ·
[Google raw vs reliable data](docs/GOOGLE_RELIABLE_LOCATION.md)

## Option A — Modular stack: 4 containers

**Use this if you installed the app from ZimaOS/CasaOS, or want independently
managed web and provider containers.** The native store app and existing
store adapters use this layout: web + Apple + Google + upstream Anisette.

For a fresh server with Docker Compose, use an empty folder:

```sh
mkdir find-my-hub-modular && cd find-my-hub-modular
curl -fsSL https://raw.githubusercontent.com/Mattboxx/Find_My_Hub_Docker_Appstores/v1.1.21/compose.yaml -o compose.yaml
docker compose up -d
docker compose ps
```

Open **`http://SERVER_IP:8125`**. Create the administrator and complete **Setup**.
This recipe uses persistent named volumes. Provider ports are internal by
default; the browser talks to the web app, not directly to those containers.

**Store users:** update the existing app normally. Do not install another copy
or change its app ID just to obtain this update. The [catalog guide](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores#casaos--zimaos)
explains JSON store sources and the supported platform adapters.

## Option B — All-in-One: 2 containers

**Explicit image name: `ghcr.io/mattboxx/apple-google-tracking-server`.**
It contains web + Apple provider + Google provider, supervised as three
independent processes. The Compose recipe adds the separate upstream Anisette
container. This is **not** a one-container installation including Anisette.

For a fresh Linux server:

```sh
mkdir find-my-hub-bundle && cd find-my-hub-bundle
curl -fsSL https://raw.githubusercontent.com/Mattboxx/Find_My_Hub_Docker_Appstores/main/all-in-one/compose.yaml -o compose.yaml
mkdir -p data/anisette
sudo chown 1000:1000 data/anisette
docker compose up -d
docker compose ps
```

Open **`http://SERVER_IP:8125`** and complete the same administrator and provider
setup. On Linux, the directory preparation lets upstream Anisette write as its
unprivileged UID 1000. For a custom data path, Windows Docker Desktop, existing
data or rollback, follow the [complete bundle guide](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores/blob/main/all-in-one/README.md).

The new package name is an explicit alias of the existing stable bundle,
not a different firmware or database format. **`find-my-hub` remains a legacy
compatible image name**; existing installations are not broken or forced to move.
`find-my-web` is **web only**, never an All-in-One alias.

| Image reference | Meaning |
| --- | --- |
| `ghcr.io/mattboxx/find-my-web:1.1.21` | Web only; needs separate/existing providers |
| `ghcr.io/mattboxx/apple-google-tracking-server:1.1.21` | Web + Apple + Google bundle |
| `ghcr.io/mattboxx/apple-google-tracking-server:stable` or `:latest` | Latest stable bundle |
| `ghcr.io/mattboxx/find-my-hub:1.1.21` | Legacy name for that same bundled image |

Version tags pin a reproducible release. `latest`/`stable` follow future stable
releases; they do not update a running container by themselves. The modular
images also have their own `latest` tags. Never replace `find-my-web` with the
bundle without following the data-layout migration instructions.

## First-run checklist — both layouts

1. Open `http://SERVER_IP:8125` and create the first administrator. There is no
   anonymous map login; optional provider API tokens are separate from web login.
2. In **Setup**, configure only the providers you need. The supplied stacks
   already provide internal service addresses; `localhost` in a container is
   not your NAS or laptop.
3. Complete Apple authentication/2FA or the upstream Google login/secrets flow.
   A running container does not mean that an account is authenticated.
4. Generate/import the appropriate identities, then explicitly create a device.
   Existing devices keep their identities: an ordinary update does not require
   new keys, registration or firmware flashing.
5. Wait for an actual network sighting. Seeing a registered device or valid
   BLE advertising does not guarantee a recent location report.
6. Select a language, check the account's devices and enable integrations only
   if needed. EN, IT, ES, FR, RU and Simplified Chinese persist in that browser.

The four new locales use offline machine translations with reviewed critical
messages. Technical errors/raw JSON and generated ZIP documentation may retain
their original language. [Translation scope and maintenance](docs/LOCALIZATION.md).

## Illustrated demonstrations

### 1. Review a journey without losing older points

Select a device → **History / Storico** → choose all data, 24 hours, 7/30 days
or a custom time range → navigate with previous/next and the slider. Filtering
changes what is displayed; it does not delete stored history or change MQTT.

![History with a custom time range and point count — synthetic demo](docs/screenshots/03-history-range.jpg)

<details>
<summary>Mobile demonstration: history remains visible above the controls</summary>

![Mobile history navigation — synthetic demo](docs/screenshots/15-mobile-history.jpg)

The bottom history controls retain timestamp, source and point details. Map
padding keeps the selected point in the visible part of the map. Collapse
details if you need more room; the historical data remains accessible.

</details>

### 2. Combine several trackers into one reversible view

Open a device's settings → configure its **Unified view / Vista unificata** →
select same-account members. The logical view uses the newest applicable
provider positions, with member badges. Open any original member's settings or
show only that member's history. Unlinking does not delete keys or locations.

![Unified device view with original members — synthetic demo](docs/screenshots/04-unified-view.jpg)

<details>
<summary>See original-member settings and guarded identity changes</summary>

![Original member settings — synthetic demo](docs/screenshots/05-device-settings.jpg)

![Explicit identity rotation — synthetic demo](docs/screenshots/17-identity-rotation.jpg)

Identity rotation changes tracker keys and may require reprogramming the
physical device. It is deliberately confirmed, not part of merging, splitting
or updating a container.

</details>

### 3. Understand Google reports instead of following every newest point

Choose **Optimized**, **Raw** or **Both**. Reliable-location analysis considers
consensus, clustering and plausible movement; a lone far-away report can remain
pending rather than move the map. The raw archive stays available separately.
Open **Reports** to inspect classifications, confidence and original fields.

<details>
<summary>See Google reports and administrator reliability settings</summary>

![Original reports and derived analysis — synthetic data](docs/screenshots/18-google-reliable-reports.jpg)

![Administrator analysis settings — synthetic data](docs/screenshots/19-google-analysis-settings.jpg)

Advanced global parameters are in administrator Setup. Collapsed developer
tools stay at the bottom of the device panel. An optimized point is an estimate,
not a guarantee; consult raw reports whenever you need the original evidence.

</details>

### 4. Configure accounts, connections and optional integrations

Administrators manage users, device ownership, provider setup and infrastructure.
Ordinary users manage their own devices and identities; they cannot change
shared provider addresses or MQTT settings.

<details>
<summary>See account management, provider setup, MQTT and Traccar</summary>

![Users and roles — synthetic accounts](docs/screenshots/07-users.jpg)

![Provider setup controls — no live account credentials](docs/screenshots/08-provider-setup.jpg)

![MQTT and background polling controls — demo settings](docs/screenshots/09-mqtt.jpg)

![Optional Traccar integration — demo settings](docs/screenshots/10-traccar.jpg)

MQTT/Home Assistant and an existing Traccar Server are optional and disabled by
default. Find My Hub still owns its accounts, devices, history and map when
either integration is absent. The Google provider fork named “traccar” is not
the optional Traccar Server map integration.

</details>

### 5. Back up first; generate identities or firmware only when needed

Use administrator backup for complete web data; selective JSON export is not a
replacement for a complete backup. Apple, Google and Anisette state require their
own backups too. After generating an identity you can choose whether to create
a device, then use its firmware shortcuts with prefilled advertisement values.

<details>
<summary>See backups, identity generation and firmware tools</summary>

![Backup and export controls — synthetic data](docs/screenshots/11-backup.jpg)

![Identity generation — disposable demonstration keys](docs/screenshots/06-identities.jpg)

![ESP32 flasher — existing firmware interface](docs/screenshots/12-esp32-flasher.jpg)

![Configured ESP32 library download](docs/screenshots/13-esp32-library.jpg)

![Nordic flasher — existing firmware interface](docs/screenshots/14-nrf-flasher.jpg)

Firmware tools are optional. Screenshots describe controls, not a new hardware
compatibility test. Never publish a personalized firmware ZIP: it contains your
tracker's advertisement values. Firmware and key behavior are unchanged here.

</details>

## Updates, migration and safety

For an existing installation, take a backup, keep its current deployment layout
and update its images. In that installation's Compose folder:

```sh
docker compose pull
docker compose up -d
docker compose ps
```

A pinned image remains pinned until you explicitly change its version.
Back up databases, identities, settings and all provider state; **do not run
`docker compose down -v` and do not delete data folders**. Modular named volumes
and the bundle's `data/{web,apple,google-auth,google-keys,anisette}` bind layout
are not interchangeable without a deliberate offline migration.

To change layout: stop the old stack, back up, map/copy the verified data
directories, then start one layout and check accounts/history/provider status.
Do not run two writers against the same data or bind both installations to port
8125. If your current modular stack works, there is no need to migrate.

## Existing standard providers: web only

The convenience provider packages are optional. Existing
[macless-haystack](https://github.com/dchristl/macless-haystack) and
[traccar/google-find-hub-sync](https://github.com/traccar/google-find-hub-sync)
installations can be connected from administrator Setup. The web uses standard
Apple `POST /` and Google `GET /devices`, `GET /devices/<id>/location` contracts.
Optional onboarding/registration/EID diagnostic endpoints need a provider
version that actually implements them.

Use `ghcr.io/mattboxx/find-my-web` only when compatible providers already exist.
Configure addresses reachable from that container in administrator Setup.
The source repository's `docker-compose.yml` is web only; **this catalog's**
root `compose.yaml` is the complete modular stack. They are not interchangeable.
The components communicate over HTTP in both layouts; identities remain
separate. Bundling processes is not security isolation.

## Project boundaries and support

This is an unofficial integration, not affiliated with Apple or Google. It
does not create its own crowdsourced network or guarantee live GPS tracking.
Use only trackers/accounts you own or are authorized to manage. Keep optional
unprotected provider APIs inside a trusted LAN/VPN, and protect remote web
access with appropriate HTTPS/authentication.

The web source repository remains **private**. Public installation recipes,
provider source archives and reviewed synthetic screenshots are in the
[catalog repository](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores).
Public Docker images contain application code; repository privacy is not
encryption. Never upload authentication volumes, backups or personalized ZIPs.

If the project helps you, you can [support its development on Ko-fi](https://ko-fi.com/mattboxx).
Support is optional: no feature restrictions, reminder popups or embedded
payment/advertising widgets.

## Store adapters and previous release notes

The detailed platform instructions and earlier fixes remain below. For a fresh
installation, choose **A or B above**, rather than following both recipes.

<details>
<summary>Open native-store setup, adapter details and previous fixes</summary>


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

## Modular stack — generic Docker installation

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

The template deploys the modular root `compose.yaml`: four containers with
Anisette. For All-in-One, import `all-in-one/compose.yaml` as a separate stack
after following the Linux data-directory preparation in its guide.

## Umbrel and Runtipi

The Umbrel-compatible store descriptor and app are in `adapters/umbrel/`. The
Runtipi adapter is in `adapters/runtipi/apps/find-my-hub/`. These formats
are ready for testing and for submission/forking into their respective
community catalogs; approval in an official third-party catalog remains under
that catalog's maintainers.

## Container image requirement

One-click installation requires anonymous access to these multi-architecture
images:

- `ghcr.io/mattboxx/find-my-web:1.1.21`
- `ghcr.io/mattboxx/find-my-apple-provider:1.1.21`
- `ghcr.io/mattboxx/find-my-google-provider:1.1.21`

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

</details>

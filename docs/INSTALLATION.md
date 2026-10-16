# Installation and operations

[Project overview](../README.md) · [Native stores](STORES.md) · [User guide](USER_GUIDE.en.md)

**All-in-One (two containers) is recommended for new installations.** The
four-container modular stack is **legacy**, retained for existing deployments
and the current native-store entry. Both offer the same web features; changing
layout requires an explicit migration.

## Apple account prerequisite

Before authenticating the Apple provider, use an **Apple Account (Apple ID)
that has been registered on an Apple device at least once**, with **iCloud
activated**. The **free 5 GB iCloud plan is sufficient**; a paid storage plan
is not required. Creating a new account without initializing iCloud on a device
does not complete this prerequisite.

After that initial iCloud activation, **you can remove the Apple device from
the account**. It does not need to remain registered or connected to this server.
Keep access to the account and its two-factor authentication method for provider
sign-in. This is separate from creating the local web administrator or flashing
a tracker. It applies to both deployment layouts and standard Apple providers.

## Google account prerequisite

Use a **Google account with at least one device already registered on the
Google Find Hub network** before configuring the Google provider. A fresh
account that has not joined the finding network does not complete this setup.

For broader network coverage, open the participating Android device's offline
finding settings and choose **"With network in all areas"**, or the equivalent
maximum network participation option shown by that Android version. This is a
recommended setting, separate from the requirement to have a registered device.
Then follow the upstream Google login/secrets flow with that same account.
The local web administrator is separate from the Google account.

## Option A — All-in-One: 2 containers (recommended)

**Explicit image name: `ghcr.io/mattboxx/tagrelaylab-server`.**
It contains web + Apple provider + Google provider, supervised as three
independent processes. The Compose recipe adds the separate upstream Anisette
container. This is **not** a one-container installation including Anisette.

For a fresh Linux server:

```sh
mkdir find-my-hub-bundle && cd find-my-hub-bundle
curl -fsSL https://raw.githubusercontent.com/Mattboxx/TagRelayLab-Appstores/main/all-in-one/compose.yaml -o compose.yaml
mkdir -p data/anisette
sudo chown 1000:1000 data/anisette
docker compose up -d
docker compose ps
```

Open **`http://SERVER_IP:8125`** and complete the same administrator and provider
setup. On Linux, the directory preparation lets upstream Anisette write as its
unprivileged UID 1000. For a custom data path, Windows Docker Desktop, existing
data or rollback, follow the [complete bundle guide](https://github.com/Mattboxx/TagRelayLab-Appstores/blob/main/all-in-one/README.md).

The new package name is an explicit alias of the existing stable bundle,
not a different firmware or database format. **`find-my-hub` remains a legacy
compatible image name**; existing installations are not broken or forced to move.
`apple-google-tracking-server` also remains a compatibility alias for the bundle.
`find-my-web` is **web only**, never an All-in-One alias.

| Image reference | Meaning |
| --- | --- |
| `ghcr.io/mattboxx/find-my-web:1.1.24` | Web only; needs separate/existing providers |
| `ghcr.io/mattboxx/tagrelaylab-server:1.1.24` | Web + Apple + Google bundle |
| `ghcr.io/mattboxx/tagrelaylab-server:stable` or `:latest` | Latest stable bundle |
| `ghcr.io/mattboxx/find-my-hub:1.1.24` | Legacy name for that same bundled image |

Version tags pin a reproducible release. `latest`/`stable` follow future stable
releases; they do not update a running container by themselves. The modular
images also have their own `latest` tags. Never replace `find-my-web` with the
bundle without following the data-layout migration instructions.

## Option B — Legacy modular stack: 4 containers

**Legacy layout for existing modular installations and current native-store
entries.** It runs web + Apple + Google + upstream Anisette. For a new server,
choose the recommended All-in-One layout above. Existing installations can
keep this layout; there is no automatic migration.

If you explicitly need the legacy layout, use an empty folder:

```sh
mkdir find-my-hub-modular && cd find-my-hub-modular
curl -fsSL https://raw.githubusercontent.com/Mattboxx/TagRelayLab-Appstores/v1.1.24/compose.yaml -o compose.yaml
docker compose up -d
docker compose ps
```

Open **`http://SERVER_IP:8125`**. Create the administrator and complete **Setup**.
This recipe uses persistent named volumes. Provider ports are internal by
default; the browser talks to the web app, not directly to those containers.

**Store users:** update the existing app normally. Do not install another copy
or change its app ID just to obtain this update. The [catalog guide](STORES.md#casaos--zimaos)
explains JSON store sources and the supported platform adapters.

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

Provider addresses accept Docker hostnames, IPv4 or bracketed IPv6, for example
`http://[2001:db8::2]` with port `5500` for Google. Keep IPv6 brackets when using
a full URL. Apple setup uses port `6177`; Google setup uses `5501` by default.
These are separate from the provider query ports (`6176` / `5500`).

The four new locales use offline machine translations with reviewed critical
messages. Technical errors/raw JSON and generated ZIP documentation may retain
their original language. [Translation scope and maintenance](LOCALIZATION.md).

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
The source repository's `docker-compose.yml` is web only; the **public catalog's**
root `compose.yaml` is the complete modular stack. They are not interchangeable.
The components communicate over HTTP in both layouts; identities remain
separate. Bundling processes is not security isolation.

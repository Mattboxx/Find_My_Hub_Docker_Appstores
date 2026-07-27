# Find My Hub Docker App Stores

Multi-platform Docker app-store repository for **Find My Hub**. It contains one
portable Compose stack plus store-specific adapters; it is not tied to ZimaOS.

## Compatibility

| Platform | Entry point | Installation |
| --- | --- | --- |
| Docker, Docker Desktop, Dockge and Compose-compatible panels | `compose.yaml` | Import or run the Compose file |
| CasaOS / ZimaOS | `Apps/FindMyHub` | Register the repository ZIP as an external store |
| Portainer | `portainer/templates.json` | Use the raw JSON URL as an App Templates URL |
| Umbrel Community App Store | `adapters/umbrel/` | Publish/fork this directory as an Umbrel community store |
| Runtipi | `adapters/runtipi/apps/find-my-hub/` | Publish/fork the adapter in a Runtipi app store |

Store formats are not standardized. The generic Compose file covers products
that can import Compose; native one-click stores require their own small
manifest, all kept in this repository.

## Generic Docker installation

```bash
git clone https://github.com/mattbox03/Find_My_Hub_Docker_Appstores.git
cd Find_My_Hub_Docker_Appstores
docker compose up -d
```

Open `http://HOST:8125`. Optional variables are `FINDMY_WEB_PORT`,
`APPLE_SETUP_TOKEN`, `GOOGLE_TOKEN`, `RETENTION_DAYS`, and `REFRESH_INTERVAL`.
Both provider tokens may remain empty on a trusted local network.

## CasaOS / ZimaOS

In **App Store -> ADD**, register the source below. If an older copy was
already registered, remove it first and then add it again so the app index is
downloaded afresh:

```text
https://github.com/mattbox03/Find_My_Hub_Docker_Appstores/archive/refs/heads/main.zip
```

Older CasaOS installations can use:

```bash
casaos-cli app-management register app-store https://github.com/mattbox03/Find_My_Hub_Docker_Appstores/archive/refs/heads/main.zip
```

## Portainer

Set **App Templates URL** to:

```text
https://raw.githubusercontent.com/mattbox03/Find_My_Hub_Docker_Appstores/main/portainer/templates.json
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

- `ghcr.io/mattbox03/find-my-web:1.1.0`
- `ghcr.io/mattbox03/find-my-apple-provider:1.1.0`
- `ghcr.io/mattbox03/find-my-google-provider:1.1.0`

All three images are public and expose `linux/amd64` and `linux/arm64`
manifests. The CI validates every JSON and Compose manifest and performs an
anonymous manifest request for every image. Loss of public access is a blocking
validation error because it would break one-click installation.

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

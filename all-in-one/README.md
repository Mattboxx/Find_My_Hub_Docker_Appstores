# Apple + Google Tracking Server — All-in-One

The `apple-google-tracking-server` image runs **web, Apple provider and Google provider** as
three independently supervised processes. Anisette uses its original upstream
image in a second container. Compose starts both with one command. This is
deliberately **not a single container containing Anisette**.

**Recommended for new installations.** The four-container modular layout is legacy.

| Layout | Find My Hub containers | Anisette | Total |
| --- | --- | --- | --- |
| Modular (legacy) | Web + Apple + Google, each separate | 1 upstream container | **4** |
| All-in-One (recommended) | Web + Apple + Google inside one container | 1 upstream container | **2** |

Both layouts provide the same interface and features. The native ZimaOS/CasaOS
entry still uses the legacy modular layout for existing installations. New
installations should use All-in-One. Switching an existing deployment requires
a deliberate migration; it is not an automatic store update. `find-my-web` is web only.

The previous `ghcr.io/mattboxx/find-my-hub` name remains a compatibility alias.
Existing configurations can keep it. New installations should use the explicit
`ghcr.io/mattboxx/apple-google-tracking-server` name. No images or data are deleted.

The original separate-provider stack and standard external providers remain
supported. No installation is migrated automatically. Firmware, identities and
stored histories are not changed by choosing this deployment layout.

## Install on a server

Create an empty installation folder and download this public Compose recipe:

```sh
mkdir find-my-hub && cd find-my-hub
curl -fsSL https://raw.githubusercontent.com/Mattboxx/Find_My_Hub_Docker_Appstores/main/all-in-one/compose.yaml -o compose.yaml
mkdir -p data/anisette
sudo chown 1000:1000 data/anisette
docker compose up -d
```

Open `http://SERVER_IP:8125`, create the administrator and use **Setup**.
Apple authentication/2FA and the upstream Google login/secrets flow remain
required. Only the web port is published; Anisette and provider ports stay
internal. Initial upstream provisioning requires Internet access.

The directory preparation above is for a fresh Linux bind mount: the pinned
upstream Anisette image runs as UID 1000. It changes ownership of that directory
only, never recursively of web/provider data. If you set a custom
`APP_DATA_DIR`, prepare its `anisette` subdirectory instead. For existing data
stop the old stack and back up first; keep existing file ownership intact.
Docker Desktop on Windows uses different bind-mount permission mapping and does
not use the Linux `sudo chown` command.

By default persistent data is stored in `./data` beside your Compose file.
Optional values can be placed in an installation-local `.env`:

| Variable | Default | Purpose |
| --- | --- | --- |
| `WEB_PORT` | `8125` | Published web port |
| `APP_DATA_DIR` | `./data` | Host data root |
| `FINDMY_AIO_IMAGE` | `ghcr.io/mattboxx/apple-google-tracking-server:1.1.21` | Pinned bundle image |
| `APPLE_SETUP_TOKEN` | empty | Optional internal Apple setup token |
| `GOOGLE_TOKEN` | empty | Optional internal Google API/setup token |

Use the version tag for reproducible installations. `stable` and `latest`
track the latest stable bundle, never development builds. Provider tokens do
not replace the web account password. Keep the installation on a trusted
LAN/VPN or behind appropriately configured HTTPS access controls.

The current Compose file pins the image version even though the download link
uses `main`. Historical `v1.1.21` recipes still refer to the old image name and
remain valid. To adopt the new name in an existing bundle installation, change
only the image reference (or `FINDMY_AIO_IMAGE`), preserving every data mount,
environment value, port and Compose project name. This is not a modular-to-bundle
migration. The two names resolve to the same 1.1.21 image digest.

## Update without losing data

Back up your data first, then run these commands in the installation folder:

```sh
docker compose pull
docker compose up -d
```

A pinned version will not move to a new release until you update
`FINDMY_AIO_IMAGE` in `.env` or the Compose image tag. Do not run
`docker compose down -v` or delete the data root. To roll back, stop the new
version before restoring your offline backup and starting the previous image.

## Existing separate-stack migration

The `/data` mount contains `web`, `apple`, `google-auth` and
`google-keys`. Anisette separately mounts the host `anisette` subdirectory.
Back up **all five** directories, not just the web database.

1. Stop the old stack; never run two writers against the same data.
2. Make an offline backup of its complete data root.
3. Set `APP_DATA_DIR` to that absolute host path after verifying the five
   expected subdirectories are present. Named volumes need a separate offline
   copy; this recipe does not migrate them automatically.
4. Start the bundle and verify login, identities, histories and provider setup.
   `apple-provider` and `google-provider` aliases point into the bundle;
   `anisette` resolves to the separate upstream service.
5. Existing custom endpoint/Anisette URLs are preserved, not silently rewritten.
   If a previous experiment saved `http://127.0.0.1:6969`, update that Apple
   configuration to `http://anisette:6969` before relying on Apple requests.
6. For rollback stop both new services before restoring the backup and starting
   the original stack. Do not delete volumes or credentials.

The bootstrap only creates missing directories/configuration and refuses
unexpected data links. It never regenerates or overwrites tracker identities.

## Operations and boundaries

```sh
docker compose ps
docker compose logs --tail 100 hub
docker compose exec hub supervisorctl -c /opt/aio/supervisord.conf status
```

Supervisor restarts the three internal processes independently; Tini handles
shutdown signals and orphaned children. Separate Python environments avoid
conflicting web/Apple dependencies but are **not security isolation**.
A whole-container failure affects all three components. No Docker socket,
privileged mode or exposed process-management port is required.

The bundle health check probes web and both setup APIs, not external Apple,
Google or Anisette availability. Those may be unavailable while the web remains
usable for diagnosis. Docker does not restart a running container solely because
it is unhealthy: Supervisor handles internal process failures and Compose's
restart policy handles container exits.

Linux amd64 startup, persistence and restart are exercised locally. CI builds
amd64 and arm64 manifests; do not equate an arm64 build with a native arm64
hardware acceptance test.

## Why Anisette is separate

No explicit redistribution license was found in the reviewed
[Anisette repository](https://github.com/Dadoum/anisette-v3-server).
We therefore do **not** copy its binary or source into our image: Compose
references the pinned upstream image, downloaded directly by Docker.
Its setup instructions are also documented in the upstream README.

The bundled Apple and Google programs retain their upstream licenses and
source notices. See the provider-source archive for this release and
`/usr/share/doc/find-my-hub/CONTAINER_LICENSES.md` in the image. Each program
runs in a separate process; packaging does not relicense upstream software.
Never publish data directories, credentials or backups.

## Build locally (source repository)

From the source repository root:

```sh
docker compose -f deploy/all-in-one/compose.yaml -f deploy/all-in-one/compose.build.yaml up --build -d
```

Set `FINDMY_PROVIDER_TAG` if you need a different existing provider release;
its default is `1.1.21`. This builds the bundle locally, not Anisette.

## Italiano

La nuova immagine raccoglie web, Apple e Google. Anisette rimane nel container
originale perché non è stata trovata una licenza esplicita per ridistribuirlo.
I due container si installano insieme con il primo comando della guida; apri
poi `http://IP_SERVER:8125` e completa la configurazione dei tuoi account.

Non serve modificare un'installazione funzionante: lo stack separato resta
disponibile. Se migri, ferma prima lo stack originale, salva tutte e cinque le
cartelle dati e imposta `APP_DATA_DIR` al percorso verificato. Non avviare mai
due versioni sullo stesso archivio. Usa il tag `1.1.21` per una versione fissa,
oppure `stable`/`latest` per seguire le release stabili. Le chiavi, il firmware
e lo storico non vengono rigenerati; autenticazione Apple/Google e 2FA rimangono
necessarie.


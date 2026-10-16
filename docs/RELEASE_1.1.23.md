# Apple + Google Tracking Server 1.1.23

This maintenance release addresses four reproducible integration/lifecycle
defects found in the follow-up review:

- **MQTT/Home Assistant:** Google reliable locations with unknown accuracy no
  longer interrupt publishing, including unified views. Unknown `gps_accuracy`
  is omitted rather than falsely reported as zero; raw data is unchanged.
- **IPv6 providers:** preserve bracketed addresses when saving Apple/Google
  settings and correctly derive Google setup URLs with or without a port.
- **Last administrator:** a SQLite write transaction protects the check and
  update/delete across independent database writers, not only one Python mutex.
- **Configured ESP32 library:** drain an old scheduler task before an immediate
  `end()` / `begin()` restart or a switch to manual polling. FindMyAdv remains
  version 1.1.0 with unchanged API; the downloaded snapshot identifies its exact
  reviewed upstream commit in `UPSTREAM.json`.

Regression coverage includes isolated API/database tests, deterministic
concurrent-writer tests and the actual C++ library implementation compiled with
fake scheduler/BLE calls. Host tests do not emulate BLE RF or replace hardware
validation. PlatformIO CI checks the seven supported build configurations.

## Safe update

Keep existing data volumes, environment settings, app identity and Compose
project name. Back up first, pull images tagged `1.1.23`, and recreate the same
services. Do not reinstall the app or register trackers again.

Both the modular stack and the recommended All-in-One bundle remain available;
no automatic topology migration occurs. Anisette stays in its separate upstream
container. Standard compatible external providers remain supported.

`latest` advances to this version; the bundle's `stable` and legacy `find-my-hub`
aliases follow the same multi-architecture image. Existing immutable version
tags are not replaced. Firmware binaries, identities, location history and
raw/optimized location algorithms are not changed.

The public provider source/build-recipe asset is
`find-my-hub-provider-sources-1.1.23.zip`, with a matching SHA-256 file. It contains
no runtime credentials or private web application source. The source repository
remains private.

<details>
<summary>Italiano</summary>

Corretti quattro difetti riproducibili: pubblicazione MQTT con accuratezza Google
sconosciuta, configurazione IPv6 dei provider, concorrenza nella protezione
dell'ultimo amministratore e doppio task al riavvio immediato di FindMyAdv.
La libreria resta 1.1.0 e mantiene le API; la copia scaricata contiene la revisione
upstream esatta. Il test software del task non è una prova radio su hardware.

Per aggiornare conserva tutti i volumi dati e ricrea gli stessi servizi con le
immagini 1.1.23. Non servono nuove registrazioni, nuove chiavi o flashing.
Il bundle richiede ancora Anisette separato; lo stack modulare non viene migrato
automaticamente. I vecchi tag immutabili non vengono modificati.

</details>

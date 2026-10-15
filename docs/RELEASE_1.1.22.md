# Apple + Google Tracking Server 1.1.22

This maintenance release fixes the configured FindMyAdv library downloaded
from the ESP32 flashing page. Both bundled source copies now match the reviewed
public library snapshot, including its previously Unreleased timing fixes.

- Provider rotation respects the chosen advertising interval instead of forcing
  one-second windows. Asynchronous Bluedroid restarts cannot prematurely rotate.
- Downloaded libraries include `UPSTREAM.json` with the canonical repository,
  exact revision and normalized source hashes. FindMyAdv remains version 1.1.0;
  this snapshot does not move or replace the library's existing release tags.
- English documentation is shown first, with Italian references collapsed.
- Leaflet CSS line endings are normalized without changing styling.

No tracker keys, identities, firmware binaries, stored locations or location
analysis algorithms change. Existing standard external providers remain supported.

## Installation and update

New installations: use the [All-in-One guide](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores/blob/main/all-in-one/README.md) in the
public catalog: the bundled web/Apple/Google image plus separate upstream
Anisette (two containers). Existing modular installations retain their four
containers and stable store identity; no automatic topology migration occurs.

Use image tag `1.1.22` for reproducible deployment. `latest` follows this release;
`stable` also follows it for the bundle and its legacy `find-my-hub` alias.
Previous versioned image tags remain unchanged. Back up and retain your data
volumes when pulling and recreating containers. Do not delete account data.

Provider additions and build recipes are supplied in the matching public
`find-my-hub-provider-sources-1.1.22.zip` release asset. It contains no credentials
or private web application source. The server source repository remains private.

<details>
<summary>Italiano</summary>

Release di manutenzione: corretti i download della libreria FindMyAdv già
configurata dal sito, con rotazione dei provider proporzionata all'intervallo
advertising e fix Bluedroid già presenti nei sorgenti upstream. Il file
`UPSTREAM.json` identifica esattamente la copia distribuita; la versione tecnica
della libreria resta 1.1.0 e i suoi tag precedenti non vengono modificati.

Nessuna modifica a firmware, chiavi, identità, cronologia o algoritmo delle
posizioni. Per aggiornare conserva tutti i volumi dati e usa le immagini 1.1.22;
non è necessario ricreare i dispositivi o riflashare le schede. Il bundle
richiede ancora Anisette separato. Le installazioni modulari non vengono migrate.

</details>

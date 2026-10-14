# Find My Hub 1.1.21

## Italiano

Completa il bundle stabile introdotto nella 1.1.20: web, Apple e Google in
un'immagine, Anisette nel suo container upstream separato. I due servizi si
installano insieme con un comando Compose. Corretto il blocco all'avvio senza
volume montato dovuto a due cartelle vuote nell'immagine base Google.
La rimozione avviene solo durante la build e soltanto se le cartelle sono vuote;
il bootstrap runtime continua a rifiutare la sostituzione di dati esistenti.

Le risorse d'installazione dello store provengono da un tag GitHub immutabile
per evitare i 503 osservati sul CDN. Il link JSON dello store non cambia.

Comprende anche le sei lingue persistenti, le date localizzate e il discreto
collegamento Ko-fi. Nessuna modifica a firmware, chiavi, storico o algoritmo
delle posizioni. Lo stack separato rimane disponibile e non viene migrato
automaticamente. Conserva sempre i volumi e fai un backup prima di aggiornare.

[Installazione server del bundle](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores/blob/main/all-in-one/README.md).
Tag riproducibile: `1.1.21`. Gli alias `latest` (e `stable` per il bundle)
seguono questa release dopo il completamento della pubblicazione.

## English

Completes the stable web/Apple/Google bundle with separate upstream Anisette,
fixing clean startup without a data mount. Only empty base-image placeholders
are removed at build time; runtime data directories are never deleted or
overwritten. Existing separate-container installations are unaffected.

Immutable installation resources use the GitHub raw release tag instead of
the CDN, which returned 503 for Compose files. The store subscription URL stays
unchanged.

Includes the 1.1.20 six-language UI, localized dates and optional Ko-fi link.
No firmware, tracker identity, stored history or reliable-location algorithm
changes. Keep data volumes and take backups before updating. Public provider
source archives include the bundle recipe and supervisor/bootstrap sources,
not private web accounts, credentials or application source.

New locales are offline machine translations with reviewed critical-message
overrides, not a complete native-speaker review. Build manifests include amd64
and arm64; local startup/restart tests cover amd64, not native arm64 hardware.

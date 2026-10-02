# Find My Hub 1.1.16

## Italiano

- Le posizioni Google correnti non sono più semplicemente l'ultimo report:
  consenso, cluster, plausibilità dello spostamento e hysteresis producono una
  posizione affidabile separata, con HIGH/MEDIUM/LOW e stato STALE.
- Ogni report originale ricevuto viene conservato in un archivio immutabile,
  inclusi invalidi, duplicati e outlier. Le annotazioni sono dati derivati;
  non riscrivono gli originali. Archivio paginato e download JSON disponibili.
- Viste Ottimizzati, Raw ed Entrambi; strumenti sviluppatore in fondo al pannello,
  inizialmente chiusi. I parametri globali sono in Setup, solo per amministratori.
- Stati correnti MQTT/Home Assistant e integrazione Traccar del sito usano
  l'ancora Google affidabile. I topic eventi conservano gli avvistamenti.
- Migrazione automatica dello storico normalizzato disponibile, backup dei
  raw/analisi, guide illustrate EN/IT e 19 schermate con soli dati sintetici.

Aggiorna i tre servizi alle immagini `1.1.16` oppure `latest` e ricreali mantenendo
i volumi. Non occorre rigenerare identità o riflashare: firmware, chiavi,
registrazione, rinnovo EID e comportamento Apple non cambiano.

Limiti: la confidence è euristica, non una garanzia di correttezza. Campi o report
scartati dalle versioni precedenti non sono recuperabili. I raw crescono a ogni
polling; la soglia età contrassegna report archiviati senza cancellarli. La mappa
Raw/Entrambi disegna le pagine caricate, non tutto l'archivio. Il sorgente web
resta privato; catalogo e immagini container già pubblici restano installabili.

## English

Google current positions now use a separate reliable-location estimator rather
than blindly taking the newest report. Consensus, adaptive clusters, plausible
motion, anti-teleport candidates and hysteresis expose confidence and STALE state.
Every decoded original report is archived immutably, including invalids and
duplicates; derived annotations remain separate. Paginated raw/history/outlier
APIs, JSON download and Optimized/Raw/Both views keep originals accessible.

Developer controls are collapsed at the bottom of the device panel; global
parameters live in administrator Setup. MQTT/Home Assistant current states and
the hub's optional Traccar exporter use reliable Google anchors. Event topics
remain observations. Available normalized legacy history migrates automatically.
Backups include raw and derived tables. EN/IT documentation and 19 synthetic-data
screenshots explain the complete workflow.

Pull/recreate the three `1.1.16` (or `latest`) services while keeping volumes.
No re-registration, new keys or reflash is needed; firmware, identities, EID
renewal and Apple behavior are unchanged. Confidence is heuristic, not guaranteed
truth; lost legacy reports cannot be recovered. Monitor append-only archive
growth. Raw/Both plots loaded pages, not the whole archive. The web source stays
private while the already-public catalog and container packages remain installable.

See [algorithm, parameters, API and migration](GOOGLE_RELIABLE_LOCATION.md),
[English guide](USER_GUIDE.en.md), [guida italiana](USER_GUIDE.it.md) and
[feature gallery](screenshots/README.md).

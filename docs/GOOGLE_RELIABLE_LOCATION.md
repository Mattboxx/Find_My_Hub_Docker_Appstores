# Google raw reports and reliable location / Report originali e posizione affidabile

## Italiano

GoogleFindMyTools restituisce avvistamenti, non una garanzia della posizione
reale. Find My Hub conserva gli originali e calcola separatamente il punto
più plausibile. Firmware, identità, crittografia e rinnovo EID non cambiano.
Sono compatibili anche provider standard `google-find-hub-sync` che restituiscono
la lista originale `locations`: non servono necessariamente i nostri package.

### Consultazione

In fondo al pannello dispositivi, apri **Dati Google · strumenti sviluppatore**.
La sezione è inizialmente chiusa per lasciare spazio ai dispositivi.
**Dati Google → Ottimizzati / Raw / Entrambi** cambia la presentazione:

- Ottimizzati: usa i punti elaborati Google; Apple mantiene il comportamento
  precedente. Una posizione vecchia non viene rimpiazzata da un outlier recente.
- Raw: sulla mappa vengono disegnati
  i report geograficamente validi della pagina selezionata.
- Entrambi: sovrappone la pagina raw alla posizione/storia affidabile.

**Report** apre sempre l'archivio, anche in modalità Ottimizzati. Seleziona un
dispositivo originale, inclusi i membri di viste unificate e i dispositivi
che conservano report Google dopo la rimozione della configurazione Google.
La rimozione della configurazione non nasconde lo storico. L'archivio non
applica filtri di periodo, fonte o plausibilità della mappa. La paginazione
(200 report per pagina, Pagina successiva e download JSON) permette di
consultare tutto senza caricare anni di dati sul cellulare. Raw/Both mostrano
sulla mappa la pagina scelta, non pretendono di aver caricato l'intero archivio.
La preferenza è persistente per account. Dopo il ricaricamento, la prima pagina
dei dispositivi Google viene ripristinata automaticamente, con al massimo quattro
richieste contemporanee, senza dover aprire la finestra Report.
Report semantici, nulli, senza coordinate, con accuracy/timestamp invalidi
rimangono elencati anche se non sono disegnabili.

Espandi un report per confrontare **RAW / GoogleFindMyTools** e **DERIVED**.
Il selettore cambia solo la mappa; la finestra si apre con il pulsante **Report**.
Stati, motivazioni e campi elaborati sono tradotti nella lingua scelta.
Il JSON originale e quello tecnico dell'analisi conservano i nomi dei campi,
per non alterare i dati e permettere il confronto con le API.
Le annotazioni cambiano quando arrivano conferme; il payload originale no.
Legenda mappa: quadrato marcato = affidabile; verde = accettato; arancio =
pending; rosso = outlier/scartato; viola = duplicato; grigio = invalido.
Il JSON `payload` presenta valori non finiti come null; `raw_json` conserva
NaN/Infinity. È la serializzazione del report decodificato, non una cattura
dei byte HTTP/protobuf originali.

### Pipeline

GoogleFindMyTools → archivio raw → validazione → deduplicazione del consenso →
cluster → analisi spazio/tempo → valutazione candidati → posizione affidabile.

1. Ogni occorrenza viene archiviata prima di qualsiasi controllo, inclusi null
   e ripetizioni esatte. I raw hanno trigger SQLite contro UPDATE/DELETE.
2. La selezione richiede coordinate finite e terrestri, timestamp positivo
   e non oltre 5 minuti nel futuro, accuracy positiva e sotto il massimo.
   Accuracy assente/null resta sconosciuta e non invalida da sola il report:
   la geometria usa il raggio base, senza bonus di precisione; il campo pubblico
   accuracy resta null. Provenienze mancanti non vengono inventate.
3. Ripetizioni esatte e osservazioni entro 10 m/30 secondi non aumentano il
   supporto. Osservazioni distinte non garantiscono telefoni distinti quando
   Google non espone l'identità del contribuente.
4. Il raggio adattivo è max(base, accuracyA + accuracyB), con la somma
   limitata a tre volte il raggio base per non collegare luoghi diversi con
   accuracy eccessivamente ampie. Si applica anche la finestra temporale.
5. Il centro usa mediane lat/lon, con longitudine srotolata attraverso la linea
   del cambio data. Una accuracy dichiarata di 1 m non domina il cluster.
6. Un punto lontano singolo diventa PENDING e non sposta l'ancora. Consenso
   temporale/spaziale può confermare il trasferimento; per salti cinematicamente
   implausibili occorrono anche almeno due minuti di evidenze nel nuovo luogo.
7. La soglia cinematica si rilassa con l'età dell'ancora, evitando lock-in dopo
   ore senza dati. Sequenze plausibili e direzionalmente coerenti possono
   confermare viaggi in auto/treno anche senza un cluster fermo.
8. Il ritorno al luogo precedente marca i salti recenti non confermati OUTLIER.
   Variazioni del centro sotto 5 m non spostano il punto pubblicato; una nuova
   osservazione accettata ne aggiorna comunque il timestamp.
9. Senza nuove evidenze resta l'ultima posizione affidabile; oltre stale_timeout
   è STALE. L'età è quella dell'avvistamento, non dell'ultimo polling.

Il primo punto valido, senza un'ancora precedente, ha evidenza LOW. HIGH,
MEDIUM, LOW e score 0–100 sono euristiche, non probabilità calibrate.
isOwnReport contribuisce solo marginalmente e non conferma un salto.
Un cluster falso persistente può comunque ingannare un filtro euristico:
gli originali restano indispensabili per le verifiche importanti.

### Parametri globali dell'amministratore

**Setup → Connessioni provider → account Google → Parametri affidabilità Google**
salva impostazioni persistenti. La sezione è inizialmente chiusa ed è visibile
solo all'amministratore; gli altri utenti non possono modificarla. La finestra
Report è dedicata alla consultazione, senza impostazioni globali.

| Parametro | Default | Unità / significato |
| --- | ---: | --- |
| cluster_time_window | 900 | secondi |
| base_cluster_radius | 100 | metri |
| max_accuracy | 5000 | metri; esclusione dalla sola selezione |
| stale_timeout | 1800 | secondi dall'ultima osservazione accettata |
| candidate_confirmation_window | 900 | secondi delle evidenze di conferma |
| minimum_cluster_support | 3 | osservazioni distinte; minimo 2 |
| kinematic_speed_threshold | 100 | m/s, 360 km/h; rilassata per ancore vecchie |
| raw_history_retention | 0 | giorni; etichetta archivio, 0 = nessuna soglia |

**La retention raw non cancella nulla:** i report vecchi sono etichettati
`archived` ma restano accessibili. La retention preesistente RETENTION_DAYS
riguarda il vecchio archivio normalizzato, non quello raw. L'archivio cresce
a ogni polling, incluse ripetizioni: monitora spazio, volumi e backup.

### Migrazione, integrazioni e privacy

`events.db` contiene tabelle distinte per raw, osservazioni uniche e stato
ricalcolabile. Il lock serializza i writer. Il backup web include automaticamente
le nuove tabelle e il WAL confermato. Gli eventi Google già disponibili vengono
copiati una volta con provenienza `legacy_normalized_event`: non si possono
ricreare campi persi o report scartati dalle vecchie versioni. Nessuna identità
deve essere rigenerata e nessun tracker deve essere riflashato.

Le posizioni correnti MQTT/Home Assistant e dell'integrazione opzionale Traccar
usano l'ancora affidabile Google; nelle viste unificate si confrontano le
posizioni affidabili Google e quelle Apple dei membri. I topic `events/...`
restano osservazioni normalizzate del provider, non posizioni correnti affidabili.
Il PUSH_URL diretto di un fork esterno bypassa Find My Hub e non viene modificato:
per esportare punti affidabili usa l'integrazione Traccar del web hub.

L'eliminazione di un dispositivo non cancella i raw dal database/backup privato;
le API per dispositivo richiedono che esso esista e sia accessibile all'account.
Non pubblicare events.db, backup o esportazioni raw: contengono posizioni personali.

### API autenticata

- GET `/api/devices/{id}/locations/raw?after_id=0&limit=200`
- GET `/api/devices/{id}/locations/both?after_id=0&limit=200`
- GET `/api/devices/{id}/locations/reliable`
- GET `/api/devices/{id}/locations/history`
- GET `/api/devices/{id}/locations/outliers?after_id=0&limit=200`
- GET `/api/location-analysis/settings`
- POST `/api/location-analysis/settings` (admin, JSON e CSRF)

Raw/Both restituiscono reports, total e next_cursor; Both aggiunge reliable.
Prosegui finché next_cursor è null, anche se una pagina outliers è vuota.
Il campo analysis contiene stato, reason, distanza, delta tempo, velocità
implicita, cluster e confidence. History contiene solo punti derivati.
La vecchia API history conserva la compatibilità; il nuovo archivio raw
non viene limitato da HISTORY_CAP e rispetta l'isolamento degli account.

## English

GoogleFindMyTools returns sightings, not verified physical truth. Each original
report is archived before validation, including malformed/semantic reports,
nulls and duplicates. Derived annotations and the reliable location are stored
separately. No raw UPDATE, DELETE or automatic pruning is performed. Standard
google-find-hub-sync providers work without changing firmware, identities,
cryptography, EID renewal or their raw /location contract.

**Google data → Optimized / Raw / Both** selects the map presentation.
Open **Google data · developer tools** at the bottom of the device panel.
Changing the mode updates only the map; use **Reports** to open the archive.
Statuses, reasons and derived-field labels follow the selected language.
Original and technical-analysis JSON keep their original field names.
This section is collapsed by default. **Reports** opens the complete, unfiltered original-device archive, including
unified-view members and devices whose Google configuration was removed but
whose reports remain stored. Removing configuration does not hide the archive.
Pages contain 200 reports, with Next page and JSON download.
Raw/Both map markers show the selected archive page; unplottable reports remain
in the list. Expand any report to compare RAW and DERIVED. Bold squares represent
optimized locations; green accepted, amber pending, red outlier/rejected,
purple duplicate and grey invalid. Language and mode preferences persist per account.

Validation, evidence deduplication, adaptive clustering, robust median centers,
anchor-relative kinematics, pending relocation and hysteresis reduce isolated
teleports. Distinct observations are not necessarily distinct contributing phones.
Own-report flags or excellent claimed accuracy cannot confirm a relocation alone.
Distant singletons remain pending; confirmed clusters can relocate. Implausible
jumps also require two minutes of evidence. Kinematic limits relax as the anchor
ages, and coherent travel can confirm car/train motion without a stationary cluster.
Returning to the anchor marks unconfirmed jumps as outliers; sub-5 m refinements
retain the center. A first valid point is LOW evidence. Confidence is heuristic,
not a calibrated probability; persistent bad reports can still mislead the estimator.
STALE uses observation time, never repeated provider-fetch time.

Administrators configure the persistent global parameters in **Setup → Provider
connections → Google account → Google reliability parameters**, collapsed by
default. The Reports window contains data only, not global settings.
Distances are metres, durations seconds and speeds m/s. raw_history_retention
labels older receipts `archived`, never deletes them (0 = no age threshold).
Existing RETENTION_DAYS affects only legacy normalized events. Monitor storage:
the raw archive grows on every poll. Nonfinite values display as null in payload;
raw_json preserves literal NaN/Infinity. This is decoded report serialization,
not captured HTTP/protobuf bytes.

SQLite events.db holds immutable originals and separate rebuildable analysis.
Missing/null accuracy stays unknown, not invalid by itself: geometry uses the
base radius internally, with no precision bonus and public accuracy=null.
Raw/Both preferences survive reloads; first archive pages reload automatically
with at most four simultaneous requests. The archive remains paginated.
Backups include new tables and committed WAL contents. Available legacy events
are migrated once and clearly marked legacy_normalized_event; previously lost
metadata/discarded reports cannot be reconstructed. MQTT/Home Assistant current
states and the hub's optional Traccar integration use reliable Google anchors.
Existing events/ topics remain normalized observations, not current reliable
positions. External-fork PUSH_URL jobs bypass the hub and are not changed: use
the hub's Traccar integration for reliable exports. Deleting a device retains raw
records in private backups; device-scoped APIs require an existing accessible device.
Keep raw exports and backups private. APIs above use normal ownership/auth guards;
parameter writes require admin and CSRF. Follow next_cursor until null even when
an outliers page is empty.

Tests cover home→Morocco→home, stable home consensus, delayed Milan→Rome,
distant singleton, coherent car/train travel, long-gap recovery, accuracy=1 m
outliers, mediocre-accuracy consensus, duplicate suppression, invalid/nonfinite
reports, late-arrival replay, immutable storage, pagination, restart, account
isolation, failed polling, and reliable MQTT/Traccar current-position export.

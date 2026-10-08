# Find My Hub 1.1.19

## Italiano

- Mantiene la nuova interfaccia compatta dei Report Google, con campi leggibili,
  spiegazioni richiudibili e impostazioni sviluppatore in fondo al pannello.
- Cambiando dispositivo o pagina, rimuove subito il contenuto precedente e
  disabilita navigazione ed esportazione fino alla risposta. Una risposta
  ritardata non può sostituire il dispositivo selezionato.
- Aggiunge **Riprova** in caso di errore di caricamento e corregge il comando
  Avanti prima che la prima pagina sia disponibile.
- Sincronizza guide EN/IT, immagini della galleria, manifest e adattatori per
  ZimaOS/CasaOS, Portainer, Umbrel e Runtipi.

Aggiorna i tre container a `1.1.19` oppure `latest`, mantenendo i volumi.
Non rigenerare chiavi e non riflashare tracker. Nessuna modifica a firmware,
provider, archivio raw o algoritmo della posizione affidabile.
Le immagini supportano amd64 e arm64. La repository principale resta privata;
il catalogo e i package container già pubblici restano installabili.

Il [link JSON dello store](https://cdn.jsdelivr.net/gh/Mattboxx/Find_My_Hub_Docker_Appstores@gh-pages/store.json)
non cambia. Le risorse di installazione usano lo snapshot immutabile
`catalog-1.1.19`; il rilevamento dell'aggiornamento può richiedere un refresh
del catalogo e la propagazione della CDN.

Test: suite Python, regressioni JavaScript su caricamento, errori e risposte
concorrenti; la pubblicazione richiede inoltre i controlli Linux, sicurezza,
Compose e integrazione Docker della CI. Le immagini illustrative usano solo
dati dimostrativi; la galleria resta rappresentativa dell'interfaccia attuale.

## English

- Retains the compact Google Reports layout, readable fields, collapsed help
  and developer tools at the bottom of the device panel.
- Clears previous content when switching devices/pages and disables navigation
  and export until the response arrives. Late responses cannot replace the
  selected device's reports.
- Adds **Retry** after loading failures and fixes Next before an initial page
  is available.
- Synchronizes EN/IT guides, gallery assets, manifests and ZimaOS/CasaOS,
  Portainer, Umbrel and Runtipi adapters.

Update all three services to `1.1.19` or `latest`, preserving data volumes.
No new keys or tracker reflash are needed. Firmware, provider logic, raw data
and the reliable-location algorithm are unchanged. Images support amd64/arm64.
Main source stays private; the existing public catalog/container packages remain
installable. The public provider-source archive excludes runtime credentials.

The [JSON store subscription](https://cdn.jsdelivr.net/gh/Mattboxx/Find_My_Hub_Docker_Appstores@gh-pages/store.json)
is unchanged. Installation resources use immutable `catalog-1.1.19`; catalog
refresh/CDN propagation may delay update detection.

Validation includes Python tests and JavaScript loading/error/concurrency
regressions, plus required Linux, security, Compose and Docker integration CI.
Gallery screenshots contain only synthetic data and remain representative of
the current interface.

See the [report guide](GOOGLE_RELIABLE_LOCATION.md),
[English user guide](USER_GUIDE.en.md), [guida italiana](USER_GUIDE.it.md)
and [feature gallery](screenshots/README.md).

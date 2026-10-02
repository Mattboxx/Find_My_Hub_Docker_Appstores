# Find My Hub 1.1.18

## Italiano

- Interfaccia Report Google più leggibile: campi più grandi, valori impilati
  su mobile, selettore dispositivo con contrasto corretto e più spazio per i report.
- Spiegazioni e legenda sono raccolte in **Info e legenda**, inizialmente chiusa.
  Stati restano visibili; motivazioni, analisi e JSON originali si leggono aprendo
  il singolo report. Nessuna informazione viene rimossa o modificata.
- Prima pagina, pagina successiva e download JSON restano accessibili in fondo.
  In orizzontale la legenda non spinge i comandi fuori dalla finestra.
  Aggiunte chiusura con Escape e navigazione da tastiera con ritorno del focus.
- Guide italiano/inglese e schermata dei report aggiornate anche nel catalogo
  ZimaOS/CasaOS, con manifest e adattatori Portainer, Umbrel e Runtipi sincronizzati.

Aggiorna i tre servizi a `1.1.18` o `latest`, mantenendo i volumi esistenti.
Non rigenerare le chiavi e non riflashare i tracker. Nessuna modifica a firmware,
provider o algoritmo della posizione affidabile. I container sono distribuiti
per amd64 e arm64. La repository web rimane privata; il catalogo e i package
container già pubblici rimangono installabili senza autenticazione GHCR.

Il link di sottoscrizione dello store non cambia:
[catalogo ZimaOS/CasaOS JSON](https://cdn.jsdelivr.net/gh/Mattboxx/Find_My_Hub_Docker_Appstores@gh-pages/store.json).
Il catalogo usa lo snapshot immutabile `catalog-1.1.18`; il rilevamento
dell'aggiornamento può richiedere il refresh dello store e la propagazione CDN.

Verifiche: 177 test locali (174 riusciti, 3 test POSIX non applicabili su Windows),
controlli JavaScript e prove browser su schermi piccoli e in orizzontale.
La pubblicazione è inoltre subordinata ai test Linux, sicurezza, Compose e
integrazione Docker della CI. Il lampeggio Radioland non è dichiarato risolto:
la verifica fisica è ancora in sospeso e non riguarda questa release UI.

## English

- More readable Google Reports: larger fields, stacked mobile values,
  contrasting device-selector options and more room for the archive.
- Explanations are collapsed under **Info and legend**. Status remains visible;
  expand a report for its reason, analysis and unchanged original JSON.
  No information or original report is removed or altered.
- First, Next and JSON download remain accessible at the bottom. Landscape
  help does not push controls outside the dialog. Escape closes the dialog;
  keyboard focus stays within it and returns to the opening control on close.
- Updated EN/IT guides and report screenshot are shared with the ZimaOS/CasaOS
  catalog and synchronized Portainer, Umbrel and Runtipi installation resources.

Pull/recreate the three `1.1.18` or `latest` services, preserving data volumes.
No new keys or tracker reflash are needed. Firmware, providers and the reliable
location algorithm are unchanged. Images support amd64 and arm64. Web source
remains private; the existing public catalog and packages stay anonymously
installable. Provider controller/patch sources are supplied in the public
release's source ZIP; never upload authentication volumes or runtime backups.

The [JSON store subscription](https://cdn.jsdelivr.net/gh/Mattboxx/Find_My_Hub_Docker_Appstores@gh-pages/store.json)
is unchanged. Installation resources use immutable `catalog-1.1.18`; store
refresh/CDN propagation may delay update detection.

Validation: 177 local tests (174 passed, 3 POSIX-only Windows skips), JavaScript
checks and small-screen/landscape browser verification. Publication also requires
the Linux, security, Compose and Docker integration CI checks. Radioland physical
button/LED verification remains pending and is not claimed fixed by this UI release.

See the [report guide](GOOGLE_RELIABLE_LOCATION.md),
[English user guide](USER_GUIDE.en.md), [guida italiana](USER_GUIDE.it.md)
and [feature gallery](screenshots/README.md).

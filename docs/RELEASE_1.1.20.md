# Find My Hub 1.1.20

> Bundle note / Nota bundle: the initial bundled image failed the final clean
> startup test without a mounted data directory. Use 1.1.21 for that variant.
> The separate 1.1.20 web/Apple/Google stack passed validation and is unaffected.

## Italiano

- Interfaccia in inglese, italiano, spagnolo, francese, russo e cinese
  semplificato; scelta persistente nel browser e date localizzate. Traduzioni
  incluse nei file del sito, senza servizi esterni durante l'utilizzo.
- Piccolo collegamento facoltativo a Ko-fi in fondo al pannello e a Setup:
  donazione diretta, senza promemoria, popup o limitazioni delle funzioni.
- Nuova immagine stabile `ghcr.io/mattboxx/find-my-hub:1.1.20`, anche con alias
  `stable` e `latest`: web, Apple e Google in un container. Anisette resta nel
  suo container originale perché non è stata trovata una licenza esplicita
  di redistribuzione. I due servizi si installano insieme con Compose.
- Lo stack precedente rimane disponibile. Nessuna migrazione automatica,
  modifica firmware, rigenerazione chiavi o eliminazione dello storico.

Per aggiornare lo stack esistente usa i tag `1.1.20` dei tre container oppure
`latest`, mantenendo i volumi. Per la nuova variante consulta
[la guida di installazione](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores/blob/main/all-in-one/README.md) nel catalogo pubblico.
Non avviare le due varianti contemporaneamente sullo stesso archivio.

## English

Six persistent interface languages, locale-aware dates and bundled translation
assets; a discreet optional Ko-fi link; and a stable web/Apple/Google bundle.
Anisette stays in the original separate upstream image, not inside our image.
Compose installs both services with one command. The existing separate stack
remains supported and there is no automatic migration or firmware/key change.

New locales are machine translated offline with reviewed critical-message
overrides; native-speaker review of every string is not claimed. Written guides
and generated ZIP documentation remain EN/IT. Build manifests support amd64 and
arm64; local startup/restart tests cover amd64, not native arm64 hardware.

All raw and derived report handling is unchanged. Existing synthetic gallery
images remain representative; no real account or position data is published.

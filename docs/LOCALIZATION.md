# Interface languages and project support / Lingue e sostegno al progetto

## User-facing behavior

The map, setup, sign-in, report tools and both firmware-flashing pages offer
English, Italian, Spanish, French, Russian and **Simplified Chinese**. The chosen
language is saved in the browser's local storage and survives reloads and later
sessions on that browser. With no saved preference the browser language is used
when supported, otherwise English. Dates use the selected locale.

Translations are bundled as local JavaScript assets. The deployed application
does not call a translation service, download models or add translation-related
Python dependencies. User names, device names, keys, raw JSON field names and
original technical/provider errors are not translated. Generated firmware ZIP
instructions, library guides and the main written documentation remain EN/IT.

The four new locales were generated with offline Argos/CTranslate2 models;
selected critical messages and support controls have reviewed overrides. This
is not a claim of native-speaker review of every sentence. Native-language
corrections are welcome. Avoid changing placeholders, identifiers or technical
protocol names when correcting a translation.

## Maintainer workflow

Original EN/IT dictionaries remain in the three HTML pages. `web/i18n.js`
extends them with `web/translations/{index,flash,flash-esp32}.js`. Bundles cover
481 main-page keys, 113 Nordic keys and 109 ESP keys at the time of writing.
Template descriptors preserve function arguments without using runtime `eval`.

For a text correction edit the bundled locale and add the same correction to
`scripts/ui_translation_overrides.json`, so a later regeneration preserves it.
For full regeneration, install CTranslate2 and SentencePiece in a disposable
build environment and obtain the official English-to-es/fr/ru/zh Argos packages.
Keep models outside shipped files, for example under ignored `tmp/`.

From the repository root, in a UTF-8-capable shell:

```sh
node scripts/extract_ui_translations.mjs | python scripts/translate_ui_offline.py tmp/translation-models web/translations
node --experimental-vm-modules tests/check_inline_js.mjs
```

The extractor uses only static interface text and synthetic substitution
markers. The generator preserves URLs, code, product names and placeholders.
Tests check key coverage, supported languages, argument preservation, plural
and optional forms, local assets and residual tokenizer/substitution markers.
They do not prove translation fluency or visual fit: inspect long text on mobile
and ask native speakers to review it before claiming those properties.

## Optional Ko-fi support

A small footer at the end of the device panel and setup page invites anyone
who appreciates the project to [support it on Ko-fi](https://ko-fi.com/mattboxx).
It opens the donation page directly in a separate tab. There are no reminders,
popups, embedded widgets, advertising, payment scripts or restricted features.
The link uses `noopener`, `noreferrer` and a no-referrer policy. Ko-fi processes
the donation on its own website; the hub does not collect payment details.

## Italiano

La lingua scelta viene conservata nel browser anche tra sessioni. Sono presenti
inglese, italiano, spagnolo, francese, russo e cinese semplificato, con date
localizzate e file di traduzione inclusi nel sito: nessun servizio esterno viene
contattato per tradurre durante l'utilizzo. Le nuove traduzioni sono automatiche
offline con alcune correzioni manuali; non tutte sono state riviste da madrelingua.
Nomi, dati raw, chiavi ed errori tecnici originali non vengono alterati.
Le istruzioni negli ZIP e la documentazione estesa restano in inglese/italiano.

Il piccolo collegamento Ko-fi in fondo al pannello permette di sostenere
facoltativamente il progetto senza notifiche, pubblicità o funzioni a pagamento.

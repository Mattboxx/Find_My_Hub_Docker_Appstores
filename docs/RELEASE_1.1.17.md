# Find My Hub 1.1.17

## Italiano

- Il selettore Dati Google cambia soltanto la vista, senza aprire automaticamente
  Report. Stati, motivazioni, affidabilità e campi elaborati sono tradotti;
  il JSON originale resta invariato. La traduzione cambia anche a finestra aperta.
- Corretto l'accesso allo storico raw quando viene rimossa la configurazione
  Google da un dispositivo: i report conservati restano selezionabili, anche
  per i membri di una vista unificata, e vengono caricati nelle viste Raw/Entrambi.
- Restano gli strumenti rapidi Google in fondo al pannello, inizialmente chiusi;
  i parametri approfonditi sono nelle impostazioni del sito, solo per admin.
- Confermate le funzioni della 1.1.16: archivio immutabile, posizione affidabile,
  confidence/STALE, annotazioni, API e integrazioni MQTT/Traccar.

Aggiorna i tre servizi a `1.1.17` o `latest` mantenendo i volumi.
Non rigenerare chiavi e non riflashare i tracker. Il sorgente web resta privato;
il catalogo e i package container già pubblici rimangono installabili.

## English

- Google data mode changes only the map, without opening Reports automatically.
  Statuses, reasons, confidence and derived fields are localized, including
  switching language while the dialog is open. Original JSON remains unchanged.
- Fixed raw archive access after removing a device's Google configuration:
  stored reports remain selectable, including unified-view members, and load
  in Raw/Both map modes.
- Quick Google tools remain collapsed at the bottom of the device panel;
  detailed parameters live in the site's administrator-only settings.
- Retains 1.1.16 reliable locations, immutable archives, confidence/STALE,
  derived annotations, APIs and MQTT/Traccar integrations.

Pull/recreate the three `1.1.17` or `latest` services while preserving volumes.
No new keys or tracker reflash are needed. Web source remains private;
the existing public catalog and container packages remain installable.

See [raw and reliable location guide](GOOGLE_RELIABLE_LOCATION.md) and
[1.1.16 feature notes](RELEASE_1.1.16.md).

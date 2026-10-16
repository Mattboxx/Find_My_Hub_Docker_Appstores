# Project scope, privacy and limitations

TagRelayLab is an independent, experimental community project for self-hosted
Bluetooth tracker maps, report history and firmware integration. Compatibility
references to Apple Find My and Google Find Hub describe interoperability;
they are not the project's name or a claim of affiliation or certification.

## Your installation, your accounts

There is no project-run central tracking server. Each operator runs their own
server and providers, supplies their own credentials and stores their own data.
Several household users can share one installation with per-account ownership.
This is not a promise that all traffic stays local: the providers contact Apple
or Google, the map loads external OpenStreetMap tiles, and configured optional
integrations contact their respective servers. GitHub is used for updates and
official portable flashing-tool downloads. Ko-fi opens only if you choose it.

Protect credentials, tracker keys, personalized firmware ZIPs and backups.
Self-hosting does not remove the operator's privacy and security responsibilities.
Only track your property or people who have knowingly authorized that use.
Do not use this project for covert tracking, harassment or bypassing safeguards.

### Shared browsers

Sign out before giving another person access to a shared browser. Current web
sessions clear keys, device/report caches and map state when the account changes;
automatic key handoffs to a flasher also check the account. This cannot retract
clipboard contents or files already downloaded. Updated firmware pages clear
their key fields and prepared downloads on account changes too; writes already
started finish using a private operation snapshot, not reusable prepared state.
Close old pages and secure personalized files yourself. Another tab's logout
never interrupts a write already in progress.

## No mandatory payment or hosted service

There is no required subscription, activation payment or donation. Ko-fi support
is voluntary and does not unlock features or buy support, certification or a
warranty. The MIT license still permits commercial reuse of the project's own
code; describing a volunteer project as experimental does not add a
non-commercial restriction or override third-party licenses.

## Technical limits

- Reports depend on external finding networks, participating phones and account
  access. Coverage and delivery time are not guaranteed. This is not GPS or an
  emergency, safety-critical or anti-theft guarantee.
- The custom advertising firmware/library is not a certified commercial
  accessory and does not implement every official accessory feature or complete
  unwanted-tracking protection. Do not describe it as MFi/Fast Pair certified.
- FindMyAdv integrates into supported **ESP32 Arduino** projects with compatible
  BLE hardware and stack ownership. It does not work on every ESP chip, every
  framework or alongside every existing Bluetooth application. ESP8266 and
  ESP32-S2 have no supported BLE radio.
- Anisette remains an external upstream container. The recommended All-in-One
  installation is two containers, not one including Anisette.

## Publication is not legal clearance

The independent name and explicit notices reduce ambiguity; they do not grant
trademark rights, permission to access third-party services or legal immunity.
The name received only a preliminary web search, not a trademark-register
clearance. Provider terms, local interoperability exceptions, radio/hardware
rules and privacy law can still matter. Non-profit intent, optional donations
and self-hosting do not automatically exempt a deployment from those rules.

Read [licensing and corresponding sources](LICENSING.md). Obtain qualified
legal advice if distributing hardware or deploying outside a personal experiment.

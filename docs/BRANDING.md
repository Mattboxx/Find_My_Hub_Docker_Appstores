# Project names and compatibility

The independent public name is **TagRelayLab**, an experimental self-hosted
Bluetooth tracker server interoperating unofficially with **Apple Find My**
and **Google Find Hub**, with nRF52/nRF54L15
firmware tools and configured ESP32 library generation.

| Component | Name |
| --- | --- |
| Application and native store listing | TagRelayLab |
| Private source repository | TagRelayLab-Server |
| Public Docker catalog repository | [TagRelayLab-Appstores](https://github.com/Mattboxx/TagRelayLab-Appstores) |
| Public store title | TagRelayLab Server |
| Public ESP32 library repository | [TagRelayLab-ESP32-Library](https://github.com/Mattboxx/TagRelayLab-ESP32-Library) |
| Library API, includes and package name | FindMyAdv |

Use descriptive Apple Find My, Google Find Hub, Bluetooth tracker, ESP32,
nRF52 and nRF54L15 terms where they describe the component. Public README
headings and descriptions help people discover the public catalog and library;
the private source repository remains private and is not publicly indexed.
This unofficial project is not affiliated with Apple or Google.

Existing installation identities remain compatible: app ID
`io.github.mattbox03.findmyhub`, `store_app_id: findmyhub`, store ID
`find-my-hub-docker-catalog`, Compose project names, data paths, MQTT identities
and existing subscription URLs retain their historical names. GitHub redirects
the previous repository URLs to the new names; maintainers must not reuse those
old repository names. The catalog publisher refreshes both old and new CDN
aliases. Existing package names remain compatibility aliases, not app branding.
New All-in-One instructions use `ghcr.io/mattboxx/tagrelaylab-server`.

The three linked repositories are server, catalog and ESP32 library. The separate
nRF52 beacon research repository is not renamed or modified by this migration.
FindMyAdv remains the technical API/package name and version 1.1.0. Do not change
include paths or users' firmware APIs to follow a documentation-only rebrand.

TagRelayLab received a preliminary exact-name web search, not formal trademark
clearance. Descriptive compatibility wording is not a certification claim. See
[project scope](PROJECT_SCOPE.md); experimental intent and optional donations do
not remove license, privacy or external-service obligations.

Earlier screenshots, release notes and the archived technical reference retain
the names used when they were recorded. Stable images and immutable catalog
snapshots keep their original contents; a source branding update does not
replace an installed image or migrate an installation automatically.

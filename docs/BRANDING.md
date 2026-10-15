# Project names and compatibility

The public name is **Apple + Google Tracking**, a self-hosted **Apple Find My**
and **Google Find Hub** server for Bluetooth trackers, with nRF52/nRF54L15
firmware tools and configured ESP32 library generation.

| Component | Name |
| --- | --- |
| Application and native store listing | Apple + Google Tracking |
| Public store title | Apple + Google Tracking Server |
| Public ESP32 library repository | [Apple-Google-Tracking-Esp32-Library](https://github.com/Mattboxx/Apple-Google-Tracking-Esp32-Library) |
| Library API, includes and package name | FindMyAdv |

Use descriptive Apple Find My, Google Find Hub, Bluetooth tracker, ESP32,
nRF52 and nRF54L15 terms where they describe the component. Public README
headings and descriptions help people discover the public catalog and library;
private source repositories are not publicly indexed.
This unofficial project is not affiliated with Apple or Google.

Existing installation identities remain compatible: app ID
`io.github.mattbox03.findmyhub`, `store_app_id: findmyhub`, store ID
`find-my-hub-docker-catalog`, Compose project names, data paths, MQTT identities
and existing subscription URLs retain their historical names. The catalog
repository stays `Mattboxx/Find_My_Hub_Docker_Appstores` because installed stores
and immutable releases use its URLs. These identifiers are not visible branding.

Earlier screenshots, release notes and the archived technical reference retain
the names used when they were recorded. Stable images and immutable catalog
snapshots keep their original contents; a source branding update does not
replace an installed image or migrate an installation automatically.

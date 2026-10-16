# TagRelayLab Server 1.1.24

The project now uses the independent **TagRelayLab** name across its three
linked repositories: Server (private), Appstores and ESP32 Library. Apple Find
My and Google Find Hub are descriptive interoperability references, not a claim
of affiliation, certification or a new finding network.

## Changes

- Consistent visible name, canonical repository links and package descriptions.
  FindMyAdv remains the ESP32 API/package name, version **1.1.0**.
- Recommended bundle: `ghcr.io/mattboxx/tagrelaylab-server:1.1.24`.
  Historical bundle names remain compatible aliases. Existing immutable releases
  and tags are not replaced. The recommended layout still has **two containers**:
  bundle plus external upstream Anisette. Modular installations remain supported.
- Clear experimental scope, optional donations and no mandatory project-run
  central tracking service. External network dependencies and limitations are
  documented explicitly; self-hosting does not mean all traffic stays local.
- Public license/source page from the login and settings footer, local browser
  license texts, linked map attribution and provider source-offer endpoints.
- Matching public source archive now includes exact upstream provider sources,
  SHA-256 manifest, our patches/controllers, Docker recipes and generic firmware
  sources/build instructions. It excludes the private web backend and user data.
- Windows flashing ZIPs now download official portable esptool/pyOCD directly
  on first use, verify SHA-256 and cache the original archive for offline reuse.
  No Python installation, PATH changes or redistributed executable/DLL bundle.
  All six interface languages explain the first-run Internet requirement.
- The configured library ZIP includes the reviewed public FindMyAdv metadata
  snapshot and its exact upstream revision. No library API or firmware behavior
  changes are introduced by this release.

## Safe update

Keep your existing Compose project, app ID, settings and data volumes. Back up,
pull `1.1.24`, and recreate the same services. Do not reinstall, recreate keys or
register trackers again. Store IDs and legacy subscription links are retained;
the publisher refreshes both old and new catalog CDN aliases. Moving from the
modular stack to the bundle still requires a deliberate data migration.

Firmware `.bin`/`.hex` files are unchanged. No flashing or hardware testing is
part of this release. Downloading a new Windows ZIP changes only how the host
flashing tool is acquired; previously downloaded packages are not rewritten.

Read [licensing](LICENSING.md), [project scope](PROJECT_SCOPE.md) and
[installation](INSTALLATION.md). These technical changes are not trademark
clearance, legal advice or a promise of risk-free use of third-party services.

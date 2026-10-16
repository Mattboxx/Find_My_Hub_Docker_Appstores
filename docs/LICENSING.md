# Licensing and corresponding sources

[Project overview](../README.md) · [Documentation](README.md)

See the [upstream acknowledgements](../ACKNOWLEDGEMENTS.md) for each project's role.

The project's own code and documentation use the [MIT License](../LICENSE).
This does not replace or override the licenses of third-party programs.

| Component | Upstream | License / notice |
| --- | --- | --- |
| Apple provider | [macless-haystack](https://github.com/dchristl/macless-haystack) | AGPL-3.0-only |
| Google provider | [google-find-hub-sync](https://github.com/traccar/google-find-hub-sync), based on [GoogleFindMyTools](https://github.com/leonboe1/GoogleFindMyTools) | GPL-3.0-only |
| Anisette helper | [anisette-v3-server](https://github.com/Dadoum/anisette-v3-server) | Downloaded separately from its upstream publisher, never embedded in our bundle |
| Maps | [Leaflet](https://leafletjs.com/) and [OpenStreetMap](https://www.openstreetmap.org/copyright) | Retain their code licenses and map attribution |
| Network research | [OpenHaystack](https://github.com/seemoo-lab/openhaystack) | Retains its upstream license |
| Browser SWD tools | [DAP.js](https://github.com/ARMmbed/dapjs) | MIT |
| Browser serial tools | [esptool-js 0.6.0](https://github.com/espressif/esptool-js/tree/v0.6.0), [esp-web-flasher 5.1.4](https://github.com/NabuCasa/esp-web-flasher/tree/5.1.4) | Apache-2.0 and MIT respectively; pako retains MIT/Zlib notices |
| Target-side nRF52 flash algorithm | [pyOCD 0.44.1](https://github.com/pyocd/pyOCD/tree/v0.44.1) | Apache-2.0; provenance and full license shipped with browser assets |

## Visible notices and provider source offer

The web login and settings footer link to `/legal.html`, available without an
account. It contains full local third-party license texts and a public provider
source offer. Both provider setup APIs expose `/legal/sources` without credentials;
the Apple API also sends a source-offer `Link` header. These endpoints never
return runtime files or secrets.

The All-in-One image runs web, Apple and Google as separate supervised programs.
Bundling them does not relicense any component. Provider and bundle images carry
their source/license notices under `/usr/share/doc/`.

Matching provider additions, patch sources, entrypoints and reproducible build
recipes are available in the public [release source archives](https://github.com/Mattboxx/TagRelayLab-Appstores/releases).
Choose `find-my-hub-provider-sources-VERSION.zip` matching the image version.
From 1.1.24 the archive also includes both exact upstream source archives,
checksums, generic firmware source/build instructions and browser-license files.
Generate it with `scripts/build_compliance_sources.py --revision COMMIT --version
VERSION --output PATH.zip`; only explicitly allowlisted Git-committed sources are
exported, never a working directory or runtime volume. Publish the archive before
publishing the matching provider images. Earlier immutable releases are not
rewritten by this improvement.
The notices in that archive identify the exact upstream revisions. The OCI
`org.opencontainers.image.revision` label identifies the build's repository revision.

The main source repository is private. Public images contain application code;
repository privacy does not conceal installed code or remove source obligations.
Never include runtime credentials, tracker keys or account data in a source archive.

## Windows portable tools

New firmware ZIPs do **not** redistribute esptool/pyOCD executable or DLL bundles.
The BAT invokes our PowerShell helper, which downloads the complete unmodified
official Windows ZIP on first use and verifies a pinned SHA-256 before extraction
or execution. The verified archive is cached beside the helper; subsequent use
is offline and does not depend on Python, pip, PATH or installed tool versions.
Each run extracts afresh from the verified archive, preserving upstream licenses.
No firmware or credentials are sent by the downloader. Windows x64 and PowerShell
5.1 or later are required. Older downloaded ZIPs are not changed retroactively.

## Firmware and external dependencies

The source archive includes our generic firmware and its existing build recipes;
it does not recompile or change the shipped firmware. ESP32 Arduino framework
sources and their LGPL-2.1 license are available at
[2.0.17](https://github.com/espressif/arduino-esp32/tree/2.0.17) and
[3.3.9](https://github.com/espressif/arduino-esp32/tree/3.3.9) (C6), as selected by
the pinned PlatformIO recipes. Those sources include their own SDK/dependency
notices; retain them when rebuilding or redistributing. Zephyr/Nordic components
keep their per-file Apache/BSD/Nordic notices and are obtained through the pinned
PlatformIO/west manifests. Providing our source is not a blanket MIT relicensing
of any firmware, SDK, operating-system base image or external service.

The Anisette repository's redistribution permission is not established by this
project. It remains a separate image obtained by the operator from its upstream
publisher, not embedded in our image or source archive. Assess that upstream
component independently before republishing it.

This is a technical source/notice inventory, not a legal clearance or a promise
that external service terms permit every use. See [project scope](PROJECT_SCOPE.md).

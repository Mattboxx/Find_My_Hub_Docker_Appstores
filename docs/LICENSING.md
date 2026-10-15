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

The All-in-One image runs web, Apple and Google as separate supervised programs.
Bundling them does not relicense any component. Provider and bundle images carry
their source/license notices under `/usr/share/doc/`.

Matching provider additions, patch sources, entrypoints and reproducible build
recipes are available in the public [release source archives](https://github.com/Mattboxx/Find_My_Hub_Docker_Appstores/releases).
Choose `find-my-hub-provider-sources-VERSION.zip` matching the image version.
The notices in that archive identify the exact upstream revisions. The OCI
`org.opencontainers.image.revision` label identifies the build's repository revision.

The main source repository is private. Public images contain application code;
repository privacy does not conceal installed code or remove source obligations.
Never include runtime credentials, tracker keys or account data in a source archive.

# TagRelayLab Server 1.1.25

This maintenance release strengthens account changes in a shared browser and
aligns the configured FindMyAdv download with its reviewed public source.

## Changes

- Logout/account changes clear device-key fields, generated identities, raw
  report caches, map positions, import/export selections and administrative UI
  state. Late headers and response bodies from the old session cannot refill it.
- UI requests identify the expected account. If another tab changes the shared
  session cookie, an old form is rejected rather than submitted as the new user.
  API clients that do not use this optional binding remain compatible.
- Automatic firmware-page prefill checks its short-lived payload against the
  current account. Manual entry and offline preparation remain available; an
  account change does not interrupt an ongoing hardware operation.
- Both server library snapshots match public FindMyAdv revision
  `49207d82c191f1fc719494e67d4dfc3d137d07c6`. The Arduino dependency now has
  the same NimBLE 2.x bound as PlatformIO, and documentation distinguishes CI
  compilation from hardware validation. API, implementation and version 1.1.0
  are unchanged by this metadata update.
- Current documentation and deployment manifests use the same stable version.

## Verification and limits

Regression coverage exercises stale headers/bodies, cancellation, logout cleanup,
invalid logins, account-bound prefill and cross-tab cookie/account mismatches.
A local browser smoke test uses only disposable synthetic accounts and keys.
Existing tests also cover accounts, raw/reliable locations, unified views,
MQTT, Traccar, provider recovery, backups and deployment integrity. Linux CI
tests simulated-provider setup, persistence and restart; stable-image CI checks
clean All-in-One startup and restart. The public library's package and seven
PlatformIO configurations pass separately.

These checks are not a live Apple/Google account test, RF/hardware validation,
penetration test, trademark clearance or legal opinion. Firmware bytes, tracker
identities, stored raw/history data and existing immutable tags are unchanged.
Anisette remains external; the recommended bundle is still two containers.

## Update safely

Back up the existing data, pull `1.1.25`, and recreate the same services with the
same volumes and app IDs. Do not reinstall or regenerate tracker identities.
Reload existing browser tabs after updating. On a shared computer, also close
separate flasher pages and protect personalized downloads/clipboard contents:
logout cannot retract data already deliberately exported.

See [installation](INSTALLATION.md), [shared-browser guidance](PROJECT_SCOPE.md#shared-browsers),
[licensing/source offer](LICENSING.md) and [project scope](PROJECT_SCOPE.md).

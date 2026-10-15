# Animated interface tours

[Project overview](../../README.md) · [Workflow guide](../WORKFLOWS.md) · [Full-size screenshots](../screenshots/README.md)

These short, looping GIFs show the real interface with synthetic demonstration
data. They illustrate controls and use cases, not live Apple/Google account
connectivity, tracker coverage or a hardware flashing test.

## Map and history

[![Map overview followed by the history controls](map-history-tour.gif)](map-history-tour.gif)

An illustrated sequence of two existing interface captures: the current map,
then history with a custom date range. The positions, devices and accounts are
synthetic. This is a sequence of stills, not a recording of a live journey.
Map attribution is retained.

1. Inspect the newest reported position and its timestamp.
2. Switch to History and select the period you want to review.
3. Step through saved reports; filtering the display does not delete them.

For a motion-free version, open the [map](../screenshots/02-map.jpg) and
[history](../screenshots/03-history-range.jpg) stills or read the
[history walkthrough](../WORKFLOWS.md#1-review-a-journey-without-losing-older-points).

## Hardware programming and ESP32 library preview

[![nRF52, nRF54L15, ESP32 and the configured FindMyAdv library panel](hardware-library-tour.gif)](hardware-library-tour.gif)

Captured in Chromium in an isolated cloud environment on 2026-10-15. It shows
the current Nordic and ESP32 pages with empty identity fields: nRF52 hardware
selection, nRF54L15 ZIP/pyOCD guidance, ESP32 configuration, optional motion
settings, programming controls and the configured-library generator. No firmware
was prepared, downloaded, rebuilt or flashed, and no board was connected.

1. Select the exact nRF52, nRF54L15 or ESP32 target and board profile.
2. Review identity fields and advertising/motion options for your hardware.
3. Read the programming guidance; nRF54L15 uses a portable ZIP and pyOCD, not
   direct browser flashing.
4. For an existing BLE-capable ESP32 Arduino/PlatformIO project, use the
   configured FindMyAdv library generator instead of replacing your application.
   The generated package includes source, configured examples and an optional
   PlatformIO profile; the normal integration leaves your main loop unchanged.

For a motion-free version and the Nordic alternative, open the
[ESP32](../screenshots/12-esp32-flasher.jpg) and
[Nordic](../screenshots/14-nrf-flasher.jpg) stills. The
[illustrated guide](../USER_GUIDE.en.md) covers supported workflows and limits.

## Maintaining these assets

Keep previews short and readable at README width; link to text and full-size
stills for readers who prefer no animation. Capture only disposable accounts
and synthetic positions, or leave identity fields empty. Inspect every frame,
preserve map attribution, and mirror these files into the public catalog.
Never record production accounts, private keys, real journeys or personal ZIPs.

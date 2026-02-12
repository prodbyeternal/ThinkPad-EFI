# ThinkPad-EFI  
OpenCore EFI for Lenovo ThinkPad L15 Gen 1 (AMD)

![macOS 26 on ThinkPad L15](https://github.com/prodbyeternal/ThinkPad-EFI/blob/main/Tahoe.png?raw=true)

This repository contains an OpenCore EFI configuration mainly for running **macOS Tahoe 26** on the **Lenovo ThinkPad L15 Gen 1 (AMD)**.  
It is also compatible with **macOS Catalina -> Sequoia**.

---

## Tested Hardware

- **Model:** Lenovo ThinkPad L15 Gen 1 (AMD)
- **CPU:** AMD Ryzen 5 PRO 4650U
- **GPU:** AMD Radeon Graphics (iGPU)
- **RAM:** 16GB DDR4
- **Storage:** 2TB NVMe SSD
- **Wi-Fi:** Intel Dual Band Wireless-AC 7265

---

## Credits

This EFI is largely based on **fdvky1’s work** — huge thanks for the original foundation.

Original EFI:  
https://github.com/fdvky1/Thinkpad-L15-Hackintosh

---

## Important Notes

### Wi-Fi (itlwm setup)

You **must edit** the following file for Wi-Fi to work in macOS Recovery:

itlwm.kext/Contents/Info.plist


Scroll down and replace:
- `YOURPASSWORDHERE`
- `YOURWIFINAMEHERE`

If this step is skipped, Wi-Fi will **not work in recovery**.

You can also use the **itlwmPass.py** script inside the repo to edit the kext file for you. (Windows/Linux only)

macOS Tahoe can have graphical bugs due to NootedRed drivers being experimental. For best experience use macOS Tahoe **26.0.1**.

---

### USB Mapping

For best results, build your own **UTBMap**.

- Replace the included USB map with your own
- Open the EFI in **ProperTree**
- Run **OC Snapshot**

---

### Wi-Fi Driver Choice

- `itlwm` is used instead of `AirportItlwm`
- Chosen for better stability and compatibility across macOS versions

After installation:
- Download **HeliPort 2.0.0 beta** from GitHub
- Install it and optionally enable auto-launch at login

---

### Audio on macOS 26+

- Apple removed **AppleHDA.kext** starting with **macOS 26.0 Beta 2**
- To restore audio, use **MyKextInstaller** to reinstall AppleHDA
- **OCLP3 Beta does not work**

---

## What Works?

Everything expected from a daily-driver laptop:

- GPU acceleration (works out of the box)
- HDMI output
- Audio (after AppleHDA restoration, macOS 26 only.)
- Wi-Fi & Bluetooth
- Sleep / Wake
- Trackpad, keyboard, ports, and more

---

## macOS Installation

Create your own macOS installer using:

macrecovery.py


---

## UEFI / BIOS Settings

### Config Tab

**Display**
- Boot Display Device → ThinkPad LCD
- Shared Display Priority → HDMI
- Boot Time Extension → Disabled
- Increase the Framebuffer Size → from 512MB to 1GB at best

---

### Security Tab

- Memory Protection → Execution Prevention → On
- Secure Boot → Off

---

### Startup Tab

- UEFI/Legacy Boot → UEFI Only

---

## Disclaimer

This EFI is provided **as-is**.  
Results may vary depending on hardware revisions, BIOS versions, and macOS updates.  
Always keep backups before updating macOS or OpenCore.

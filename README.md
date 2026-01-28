ThinkPad-EFI

OpenCore EFI for Lenovo ThinkPad L15 Gen 1 (AMD)

This repository contains an OpenCore EFI configuration for running macOS Tahoe 26 on the Lenovo ThinkPad L15 Gen 1 (AMD).
It is also compatible with macOS Sequoia.

💻 Tested Hardware

Model: Lenovo ThinkPad L15 Gen 1 (AMD)

CPU: AMD Ryzen 5 PRO 4650U

GPU: AMD Radeon Graphics (iGPU)

RAM: 16GB DDR4

Storage: 2TB NVMe SSD

Wi-Fi: Intel Dual Band Wireless-AC 7265

🙏 Credits

This EFI is largely based on fdvky1’s work — massive thanks to them for the original foundation.

Original EFI:
https://github.com/fdvky1/Thinkpad-L15-Hackintosh

⚠️ Important Notes
Wi-Fi (itlwm setup)

You must edit the following file for Wi-Fi to work in macOS Recovery:

itlwm.kext → Contents → Info.plist


Scroll down and replace:

YOURPASSWORDHERE

YOURWIFINAMEHERE

If you skip this step, Wi-Fi will not work in recovery.

USB Mapping

It is strongly recommended to build your own UTBMap for best results.

Replace the included map with your own and:

Open the EFI in ProperTree

Run OC Snapshot

Wi-Fi Driver Choice

itlwm is used instead of AirportItlwm

Reason: better stability and compatibility across macOS versions

After installation:

Download HeliPort 2.0.0 beta from GitHub

Install it and optionally enable auto-launch at login

Audio on macOS 26+

Apple removed AppleHDA.kext starting with macOS 26.0 Beta 2

To restore audio:

Use MyKextInstaller to reinstall AppleHDA

❌ OCLP3 Beta does NOT work (tested extensively)

✅ What Works?

Pretty much everything you’d expect from a daily-driver laptop:

GPU acceleration (works out of the box)

HDMI output

Audio (after AppleHDA restoration)

Wi-Fi & Bluetooth

Sleep / Wake

Trackpad, keyboard, ports, etc.

In short: everything top to bottom 😄

📦 macOS Installation

Supply your own macOS installer using:

macrecovery.py

⚙️ UEFI / BIOS Settings

(Courtesy of fdvky1)

Config Tab

Display

Boot Display Device → ThinkPad LCD

Shared Display Priority → HDMI

Boot Time Extension → Disabled

Security Tab

Memory Protection → Execution Prevention → On

Secure Boot → Off

Startup Tab

UEFI/Legacy Boot → UEFI Only

❗ Disclaimer

This EFI is provided as-is.
Your mileage may vary depending on BIOS version, hardware revisions, and macOS updates.
Always keep backups before updating macOS or OpenCore.

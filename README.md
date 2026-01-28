# ThinkPad-EFI
OpenCore EFI files for Lenovo ThinkPad L15 Gen 1 (AMD)

This branch focuses on running macOS Tahoe 26 but also works for macOS Sequoia.
Tested on: Lenovo ThinkPad L15 Gen 1 (AMD), 2TB NVMe SSD, 16GB DDR4 RAM, AMD Ryzen 5 PRO 4650U with AMD Radeon Graphics, Intel Dual Band Wireless-AC 7265 Wi-Fi Card.

This EFI is largely based on top of fdvky1's EFI Files, huge thanks to them! | [Original EFI](https://github.com/fdvky1/Thinkpad-L15-Hackintosh)


Notes:
You will need to edit itlwm's files | itlwm.kext -> Contents -> Info.plist
Scroll down to where it says YOURPASSWORDHERE and YOURWIFINAMEHERE. Replace these with your info, or else you won't get Wi-Fi in the recovery.

Build your own UTBMap for better results, then replace the existing one with the one you built and use ProperTree to refresh it. (OC Snapshot)

itlwm has been chosen instead of AirportItlwm because of stability and versatility between macOS versions.
After installation, download the HeliPort 2.0.0 beta from Github and install it. Optionally make it so it opens on logon.

Apple has removed the AppleHDA kext from their os starting with 26.0 Beta 2, you will need to use MyKextInstaller to revert AppleHDA.
OCLP3 Beta doesn't work, believe me, I tried.

What works?

Basically everything top-bottom, GPU works out of the box and keeps up with everything, HDMI works too. Basically everything a laptop does :D

Supply yourself with your own macOS Install file via macrecovery.py

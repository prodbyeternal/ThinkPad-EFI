#!/usr/bin/env python3

# itlwm Wi-Fi injector by prodbyeternal, 2026.

import os
import platform
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path

#
# Wi-Fi scraping per platform
#


def get_wifi_windows():
    networks = []
    profiles = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles"], encoding="utf-8", errors="ignore"
    )

    for line in profiles.splitlines():
        if "All User Profile" in line:
            ssid = line.split(":")[1].strip()
            try:
                details = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", ssid, "key=clear"],
                    encoding="utf-8",
                    errors="ignore",
                )
                for d in details.splitlines():
                    if "Key Content" in d:
                        password = d.split(":")[1].strip()
                        networks.append((ssid, password))
                        break
            except subprocess.CalledProcessError:
                pass

    return networks

def get_wifi_linux():
    networks = []
    connections = subprocess.check_output(
        ["nmcli", "-t", "-f", "NAME,TYPE", "connection", "show"], encoding="utf-8"
    )

    for line in connections.splitlines():
        name, ctype = line.split(":")
        if ctype != "wifi":
            continue

        try:
            password = subprocess.check_output(
                [
                    "nmcli",
                    "-s",
                    "-g",
                    "802-11-wireless-security.psk",
                    "connection",
                    "show",
                    name,
                ],
                encoding="utf-8",
            ).strip()
            if password:
                networks.append((name, password))
        except subprocess.CalledProcessError:
            pass

    return networks


def get_known_wifi():
    os_name = platform.system()

    if os_name == "Windows":
        return get_wifi_windows()
    elif os_name == "Linux":
        return get_wifi_linux()
    else:
        raise RuntimeError("Unsupported OS")


#
# Recursive itlwm.kext search
#


def find_itlwm_info_plist(start_dir: Path) -> Path:
    for plist_path in start_dir.rglob("itlwm.kext/Contents/Info.plist"):
        return plist_path
    return None


#
# plist manipulation
#


def update_itlwm_plist():
    script_dir = Path(__file__).resolve().parent
    plist_path = find_itlwm_info_plist(script_dir)

    if not plist_path:
        print("❌ itlwm.kext Info.plist not found")
        sys.exit(1)

    print(f"📍 Found: {plist_path}")

    # Backup
    backup_path = plist_path.with_suffix(".plist.bak")
    shutil.copy2(plist_path, backup_path)
    print(f"💾 Backup created: {backup_path}")

    with open(plist_path, "rb") as f:
        plist = plistlib.load(f)

    wifi_entries = get_known_wifi()
    if not wifi_entries:
        print("❌ No Wi-Fi networks found")
        sys.exit(1)

    wifi_dict = {}
    for idx, (ssid, password) in enumerate(wifi_entries, start=1):
        wifi_dict[f"WiFi_{idx}"] = {"ssid": ssid, "password": password}

    plist["IOKitPersonalities"]["itlwm"]["WiFiConfig"] = wifi_dict

    with open(plist_path, "wb") as f:
        plistlib.dump(plist, f)

    print(f"✅ Injected {len(wifi_entries)} Wi-Fi networks")


#
# CLI entry
#

if __name__ == "__main__":
    if platform.system() != "Windows" and os.geteuid() != 0:
        print("⚠️  Run with sudo to read Wi-Fi passwords")
    update_itlwm_plist()

# 🧹 ADB Bloatware Flusher
<img width="480" height="270" alt="Bloatware-480x270" src="https://github.com/user-attachments/assets/8cc73b1b-894b-4a99-84a6-57bf462b0b60" />

**ADB Bloatware Flusher** is a simple but powerful Python tool that lets you safely uninstall unwanted apps (bloatware) from any Android device using ADB — all without rooting.

Remove the clutter. Reclaim your device.

Why BloatFlusher?
Because most Android devices come packed with apps you don’t need — using up space, draining battery, and cluttering your system. BloatFlusher gives you a clean, simple way to remove them safely using ADB — no root, no fuss, just control.

---

## 🚀 Features

-  Connects to your Android device via ADB
-  **Safe Mode**: Shows only removable bloatware (no critical system apps)
-  **Advanced Mode**: Lists all apps — full control, use with caution
-  Search & filter packages
-  Uninstall single or multiple apps by number or range
-  Red/Green themed CLI for clear feedback
-  Visual uninstall progress bar
-  Auto-generates uninstall logs

---

## How It Works
- Connect your Android phone via USB
- Run the tool:
```python
python adb_bloat_flusher.py
```
- Choose a mode:
  a) Safe Mode (recommended for most users)
  b) Advanced Mode (shows everything)
- View and filter installed packages
- Uninstall one or multiple apps using their list numbers
- Done! Logs are saved to adb_uninstall_log.txt

---

## Installation

## 💻 Requirements

- Python 3.x
- ADB installed and added to PATH
- USB Debugging enabled on your Android device
- Python package: `colorama`



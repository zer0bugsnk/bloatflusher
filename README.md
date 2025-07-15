# 📱 ADB Bloatware Flusher v1.0.0

**ADB Bloatware Flusher** is a simple but powerful Python tool that lets you safely uninstall unwanted apps (bloatware) from any Android device using ADB — all without rooting.

Clean. Fast. Controlled. Safe.

--- 

## Why BloatFlusher?
Because most Android devices come packed with apps you don’t need — using up space, draining battery, and cluttering your system. BloatFlusher gives you a clean, simple way to remove them safely using ADB — no root, no fuss, just control.

---

## ⚙️ Features

| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 📱 **Safe Bloatware Removal**   | Removes non-essential apps without touching core system packages.          |
| 💀 **Advanced Cleaning**        | Full package list with full control — for power users only.                |
| 🔍 **Search & Filter**          | Search apps by keyword or filter by manufacturer-specific packages.        |
| 📊 **Range-based Uninstall**    | Uninstall multiple apps with input like `1,2,5-9`.                         |
| 📁 **Log Output**               | All removed packages are logged to `adb_uninstall_log.txt`.                |
| 🎨 **Red/Green CLI UI**         | Stylish command-line interface using clear color feedback.                 |
| 🛠️ **No Root Needed**          | Uses ADB for clean and safe uninstallations without root access.           |

---

## 💻 Requirements

- Python 3.x
- ADB installed and added to PATH
- USB Debugging enabled on your Android device
- Python package: `colorama`

---

## Installation
```
git clone https://github.com/zer0bugsnk/bloatflusher.git
cd bloatflusher
pip install -r requirements.txt
python3 bloatflusher.py
```

## How to Use
- Connect your Android phone via USB
- Run the tool:
```python
python3 bloatflusher.py
```
- Choose a mode:
  a) Safe Mode (recommended for most users)
  b) Advanced Mode (shows everything)
- View and filter installed packages
- Uninstall one or multiple apps using their list numbers
- Done! Logs are saved to adb_uninstall_log.txt

---

## 🛡️ Disclaimer
⚠️ This tool is intended for educational and personal use.
⚠️ Removing core system apps (especially in Advanced Mode) can cause instability or boot issues.
⚠️ Always back up your device before using.

The developer is not responsible for any damage caused by improper use.

---

## 🙌 Contributing
Contributions are welcome!
Report bugs, suggest features, or submit pull requests via GitHub.

---

## 📄 License
This project is released under the MIT License.

---

## 💬 Final Thoughts
ADB Bloatware Flusher was created to help Android users take back control of their devices — quickly and safely.

💪 Less bloat. More performance. Full control.



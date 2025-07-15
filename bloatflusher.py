import subprocess
import time
import sys
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

LOG_FILE = "adb_uninstall_log.txt"

# Core/system packages to exclude in Safe Mode
CORE_KEYWORDS = [
    "com.android.",
    "android",
    "com.google.android.",
    "com.qualcomm.",
    "com.mediatek.",
    "com.oplus.",
    "com.coloros.",
    "system",
    "com.google.",
    "com.android.systemui"
]

def log_to_file(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def run_adb_command(cmd):
    try:
        result = subprocess.run(["adb"] + cmd.split(), capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        error = f"[!] ADB error: {e}"
        print(Fore.RED + error)
        log_to_file(error)
        return ""

def uninstall_animation(pkg):
    total_steps = 20
    print(Fore.RED + f"\nUninstalling: {pkg}")
    for i in range(total_steps + 1):
        bar = "#" * i + "-" * (total_steps - i)
        percent = int((i / total_steps) * 100)
        sys.stdout.write(Fore.GREEN + f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def is_safe_package(pkg_name):
    return not any(pkg_name.startswith(k) for k in CORE_KEYWORDS)

def list_packages(search_term="", advanced_mode=False):
    output = run_adb_command("shell pm list packages")
    packages = output.splitlines()
    packages = [pkg.replace("package:", "") for pkg in packages]
    if not advanced_mode:
        packages = [pkg for pkg in packages if is_safe_package(pkg)]
    if search_term:
        return [p for p in packages if search_term.lower() in p.lower()]
    return packages

def parse_selection(selection_str, max_index):
    indices = set()
    for part in selection_str.split(","):
        part = part.strip()
        if "-" in part:
            try:
                start, end = map(int, part.split("-"))
                indices.update(range(start, end + 1))
            except:
                continue
        else:
            try:
                indices.add(int(part))
            except:
                continue
    return sorted(i for i in indices if 1 <= i <= max_index)

def uninstall_packages(package_list):
    log_to_file("\n--- Uninstall Session @ " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ---")
    for pkg in package_list:
        uninstall_animation(pkg)
        result = run_adb_command(f"shell pm uninstall --user 0 {pkg}")
        if "Success" in result:
            msg = f"[✓] {pkg} → Success"
            print(Fore.GREEN + msg)
        else:
            msg = f"[X] {pkg} → Failed: {result}"
            print(Fore.RED + msg)
        log_to_file(msg)

def main():
    print(Fore.RED + "\n" + "=" * 65)
    print(Fore.GREEN + "     ADB Bloatware Flusher [SAFE & ADVANCED MODES]")
    print(Fore.RED + "=" * 65)

    run_adb_command("start-server")
    devices = run_adb_command("devices").splitlines()
    connected = [d for d in devices if "\tdevice" in d]

    if not connected:
        print(Fore.RED + "[!] No device found. Enable USB Debugging and reconnect.")
        return

    device_id = connected[0].split()[0]
    print(Fore.GREEN + f"[+] Connected device: {device_id}")
    log_to_file(f"[+] Connected device: {device_id}")

    advanced_mode = False

    while True:
        print(Fore.RED + "\n" + "-" * 60)
        print(Fore.RED + "OPTIONS:")
        print(Fore.GREEN + "1. List packages")
        print(Fore.GREEN + "2. Search packages")
        print(Fore.GREEN + f"3. Toggle Mode (Current: {'Advanced' if advanced_mode else 'Safe'})")
        print(Fore.GREEN + "4. Exit")

        choice = input(Fore.RED + "\nEnter choice (1-4): ").strip()
        if choice == "4":
            print(Fore.GREEN + "\nGoodbye!")
            break
        elif choice == "3":
            advanced_mode = not advanced_mode
            mode_text = "Advanced Mode" if advanced_mode else "Safe Mode"
            print(Fore.GREEN + f"[✓] Switched to {mode_text}")
            continue
        elif choice not in ["1", "2"]:
            print(Fore.RED + "[!] Invalid option.")
            continue

        search_term = ""
        if choice == "2":
            search_term = input(Fore.GREEN + "Enter search keyword: ").strip()

        packages = list_packages(search_term, advanced_mode)

        if not packages:
            print(Fore.RED + "[!] No packages found.")
            continue

        print(Fore.GREEN + f"\n[+] Found {len(packages)} package(s):\n")
        for idx, pkg in enumerate(packages, 1):
            print(Fore.GREEN + f"  {idx:>3}. {pkg}")

        selection = input(Fore.RED + "\nSelect packages to uninstall (e.g., 1-5,8): ").strip()
        if not selection:
            print(Fore.RED + "[!] No selection made.")
            continue

        try:
            selected_indices = parse_selection(selection, len(packages))
            selected_packages = [packages[i - 1] for i in selected_indices]
        except Exception as e:
            print(Fore.RED + f"[!] Error: {e}")
            continue

        if not selected_packages:
            print(Fore.RED + "[!] No valid packages selected.")
            continue

        print(Fore.RED + f"\nSelected ({len(selected_packages)}):")
        for pkg in selected_packages:
            print(Fore.GREEN + "  " + pkg)

        confirm = input(Fore.RED + "\nProceed with uninstallation? (y/n): ").strip().lower()
        if confirm != "y":
            print(Fore.RED + "Cancelled.")
            continue

        uninstall_packages(selected_packages)

if __name__ == "__main__":
    main()

# modules/log_cleaner.py

import os
import subprocess

def clear_logs():
    print("[⚠] This will clear system logs that may require root privileges.")
    confirm = input("Are you sure you want to continue? (y/n): ").lower()
    if confirm != 'y':
        print("[✋] Log cleaning aborted.")
        return

    try:
        log_paths = [
            "/var/log/auth.log",
            "/var/log/syslog",
            "/var/log/kern.log",
            "/var/log/wtmp",
            "/var/log/btmp",
            "/var/log/lastlog",
            "/var/log/messages",
        ]

        for path in log_paths:
            if os.path.exists(path):
                open(path, 'w').close()
                print(f"[🧹] Cleared: {path}")
            else:
                print(f"[ℹ] Not found (skipped): {path}")

        subprocess.run(["sudo", "journalctl", "--rotate"], check=False)
        subprocess.run(["sudo", "journalctl", "--vacuum-time=1s"], check=False)

        print("[✅] System logs cleaned successfully.")
    except Exception as e:
        print(f"[❌] Error occurred: {e}")

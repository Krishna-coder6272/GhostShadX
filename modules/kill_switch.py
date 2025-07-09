# modules/kill_switch.py

import subprocess
import time
import threading

stop_thread = False

def is_vpn_active():
    try:
        output = subprocess.check_output(["ip", "a", "show", "wg0"]).decode()
        return "inet " in output and "state UNKNOWN" not in output
    except subprocess.CalledProcessError:
        return False

def kill_internet():
    try:
        subprocess.run(["sudo", "iptables", "-I", "OUTPUT", "!", "-o", "wg0", "-j", "DROP"], check=True)
        subprocess.run(["sudo", "iptables", "-I", "INPUT", "!", "-i", "wg0", "-j", "DROP"], check=True)
        print("[🛑] Internet blocked (VPN disconnected).")
    except subprocess.CalledProcessError:
        print("[❌] Failed to apply iptables kill switch.")

def restore_internet():
    try:
        subprocess.run(["sudo", "iptables", "-D", "OUTPUT", "!", "-o", "wg0", "-j", "DROP"], check=True)
        subprocess.run(["sudo", "iptables", "-D", "INPUT", "!", "-i", "wg0", "-j", "DROP"], check=True)
        print("[✅] Internet restored (VPN active).")
    except subprocess.CalledProcessError:
        print("[❌] Failed to restore internet rules.")

def monitor_vpn(interval=5):
    global stop_thread
    last_state = None
    print("[🔄] Kill switch monitoring started...")

    while not stop_thread:
        vpn_on = is_vpn_active()
        if vpn_on and last_state != True:
            restore_internet()
            last_state = True
        elif not vpn_on and last_state != False:
            kill_internet()
            last_state = False
        time.sleep(interval)

    print("[🛑] Kill switch monitoring stopped.")

def start_monitoring():
    global stop_thread
    stop_thread = False
    t = threading.Thread(target=monitor_vpn)
    t.daemon = True
    t.start()
    return t

def stop_monitoring():
    global stop_thread
    stop_thread = True
    restore_internet()

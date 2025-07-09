# modules/vpn_control.py

import subprocess

def start_vpn():
    try:
        print("[*] Starting VPN...")
        subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)
        print("[✅] VPN started successfully.")
    except subprocess.CalledProcessError:
        print("[❌] Failed to start VPN. Please check the configuration.")

def stop_vpn():
    try:
        print("[*] Stopping VPN...")
        subprocess.run(["sudo", "wg-quick", "down", "wg0"], check=True)
        print("[✅] VPN stopped successfully.")
    except subprocess.CalledProcessError:
        print("[❌] VPN is not running or already stopped.")

def check_status():
    try:
        output = subprocess.check_output(["sudo", "wg", "show", "wg0"]).decode()
        print("[🔒] VPN Status:\n", output)
    except subprocess.CalledProcessError:
        print("[❌] VPN interface 'wg0' not active.")

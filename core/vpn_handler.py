import os
import subprocess
import time

def is_vpn_connected():
    output = subprocess.getoutput("ifconfig")
    return "tun0" in output or "ppp0" in output

def connect_vpn(config_path):
    if not os.path.exists(config_path):
        print("[!] VPN config file not found.")
        return False

    print("[*] Starting VPN...")
    command = f"sudo openvpn --config {config_path} --daemon"
    os.system(command)
    time.sleep(8)

    if is_vpn_connected():
        print("[+] VPN connected successfully.")
        return True
    else:
        print("[!] VPN connection failed.")
        return False

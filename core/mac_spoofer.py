import subprocess
import random
import re

def generate_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def get_interface():
    try:
        result = subprocess.check_output("ip link", shell=True).decode()
        interfaces = re.findall(r'^\d+: (\w+): <', result, re.MULTILINE)
        for iface in interfaces:
            if iface != 'lo':
                return iface
    except Exception as e:
        print(f"[!] Error getting interface: {e}")
        return None

def spoof_mac(interface):
    new_mac = generate_mac()
    print(f"[*] Spoofing MAC for {interface} to {new_mac}")

    subprocess.call(f"sudo ifconfig {interface} down", shell=True)
    subprocess.call(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"sudo ifconfig {interface} up", shell=True)

    print("[+] MAC address changed successfully.")
    return new_mac

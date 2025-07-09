# 👻 GhostShadX

An advanced Python-based **VPN control & privacy management tool** with support for **WireGuard**, **Kill Switch**, **Public IP tracking**, **Log cleaner**, and an optional **GUI interface** — built for cybersecurity tasks, penetration testing, and online anonymity.

---

## 🔥 Features

- ✅ Start/Stop VPN (WireGuard)
- ✅ VPN Kill Switch (Iptables based)
- ✅ Real-time Public IP Fetch
- ✅ System Log Cleaner
- ✅ GUI Interface (Tkinter)
- ✅ IPv4 leak protection
- ✅ ProtonVPN compatible
- 🛡️ Designed for Kali Linux / Debian

---

## 📸 Screenshots

> (Add your screenshots here once available)





---

## ⚙️ Installation

```bash
git clone https://github.com/Krishna-coder6272/GhostShadX.git
cd GhostShadX
pip install -r requirements.txt


---

## 🔥 VPN Setup Guide (IMPORTANT)
To use GhostShadX, you must add your own VPN configuration file (WireGuard). It will not work out of the box unless you do this setup.

---

## ✅ How to Get a Free VPN Config (via ProtonVPN)
   1-Go to: https://account.protonvpn.com/login
   2-Sign up / Login with a free account
   3-Go to Downloads → WireGuard Config Generator
   4-Select:
         -Platform: GNU/Linux
         -Server: Any free server (e.g., NL-FREE#226)
         -Device Name: GhostShadX-WG
         -Click Create and download the .conf file

---

## 📂 Where to Place the Config?
Move the downloaded file to this location:

``bash
GhostShadX/config/wg0.conf

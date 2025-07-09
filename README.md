# 👿 GhostShadX

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

## Screenshots

![GUI](https://github.com/user-attachments/assets/cafdd1a7-e46d-4887-949c-ec69e8b50b1f)





## 🔐 VPN Setup Guide (IMPORTANT)

GhostShadX requires your own VPN configuration file to work.
📥 Get Free WireGuard Config from ProtonVPN

- Go to: https://account.protonvpn.com/login
- Sign in (or sign up for a free account)
- Navigate to: Downloads → WireGuard Config Generator
- Select:
- Platform: GNU/Linux
- Server: Choose any free server (e.g., NL-FREE#226)
- Device name: GhostShadX-WG
- Click Create and download the .conf file.

---


## 📁 Add Config to the Tool

  - Move the .conf file to this location:
  - GhostShadX/config/wg0.conf
  - ✅ Rename it to {wg0.conf} (exact name required)
    
---


## 🚀 How to Run



```
git clone https://github.com/Krishna-coder6272/GhostShadX.git
cd GhostShadX
pip install -r requirements.txt
sudo apt update
sudo apt install wireguard iptables resolvconf -y
cd GhostShadX
python3 main.py
```

---

## 🖥️ GUI Mode
GhostShadX also supports a graphical interface using Tkinter.
The GUI launches from the main menu or can be called directly via:

```
sudo python3 gui_qt.py
```

---

## 📁 Folder Structure

```
GhostShadX/
├── config/
│   └── wg0.conf         ← Your VPN config
├── modules/
│   ├── vpn_control.py
│   ├── kill_switch.py
│   ├── log_cleaner.py
│   ├── public_ip.py
├── gui/
│   └── interface.py      ← Optional GUI
├── main.py
└── README.md
```


---

## 🛡️ Use Cases

- Internship/college cybersecurity projects
- Red team or penetration testing toolkit
- VPN leak test automation
- Privacy protection tools
- Network isolation with Kill Switch

---

## 🖥️ Tech Stack


- Python 3
- WireGuard
- iptables
- Tkinter (GUI)

---


## 👨‍💻 Developed By:

- Krishna Sahu
- Cybersecurity Intern | Red Teamer | Python Developer
- GitHub: Krishna-coder6272
- LinkedIn: https://www.linkedin.com/in/krishna-sahu-66a1b7275/








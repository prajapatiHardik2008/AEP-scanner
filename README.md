# 🛰️ ARP Network Scanner

A fast and simple Python-based ARP Scanner built using Scapy.
This tool scans a local network and displays active devices with their IP and MAC addresses.

---

## ⚡ Features

* 📡 Scan devices on local network (LAN)
* 🔍 Detect IP & MAC addresses
* 🚀 Fast packet-based scanning using ARP
* 🧠 Lightweight and beginner-friendly
* 💻 Works on Windows/Linux (with proper setup)

---

## 🛠️ Tech Stack

* Python 3
* Scapy

---

## 📂 Project Structure

```
ARP-scanner.py
README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/arp-scanner.git
cd arp-scanner
```

### 2. Install dependencies

```
pip install scapy
```

### 3. (Windows Only) Install Npcap

Download and install Npcap from:
https://npcap.com/

✔️ Make sure to enable **WinPcap API-compatible mode**

---

## ▶️ Usage

```
python ARP-scanner.py <IP_range>
```

### Example:

```
python ARP-scanner.py 192.168.1.1/24
```

---

## 🧠 How It Works

* Sends ARP broadcast packets across the network
* Devices respond with their MAC addresses
* Collects and displays active hosts

---

## ⚠️ Important Notes

* ⚠️ Requires **Administrator / Root privileges**
* ⚠️ Works only on **Local Area Network (LAN)**
* ❌ May NOT work on:

  * Public WiFi
  * Mobile Hotspots (due to client isolation)

---

## 🧪 Testing Tips

* Use **Home WiFi** for best results
* Or connect multiple devices to the same network
* Avoid restricted networks (college/public WiFi)

---

## 🚀 Future Improvements

* 🔄 Add Ping Sweep fallback (for restricted networks)
* 🖥️ GUI Interface (Hacker style 😎)
* 📁 Export results (CSV/JSON)
* 🌐 Hostname detection

---

## 👨‍💻 Author

Hardik Prajapati

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

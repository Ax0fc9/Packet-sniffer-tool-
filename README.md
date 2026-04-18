# Packet-sniffer-tool
# 🛡️ packet-sniffer-tool - CyberAb00d

A high-performance Python-based network packet sniffer designed for real-time traffic analysis and security auditing. This tool captures, decodes, and analyzes network packets to provide insights into data flow and potential security vulnerabilities.

---

## 🚀 Overview
As a second-year Computer Science student at the **University of Jordan**, focusing on **Cybersecurity**, I developed this project to deepen my understanding of the OSI model and TCP/IP suite. This sniffer captures raw data from the network interface and parses various protocols including Ethernet, IP, ICMP, TCP, and UDP.

## ✨ Features
- **Real-time Capture:** Captures live packets from any active network interface.
- **Protocol Decoding:** Detailed parsing of:
  - **Ethernet Frames:** MAC addresses and EtherType.
  - **IPv4 Headers:** TTL, Protocol, and Source/Destination IP.
  - **TCP/UDP Segments:** Port analysis and payload extraction.
  - **ICMP Packets:** Type and code mapping.
- **Payload Inspection:** Option to view raw data or formatted ASCII content.
- **User-Friendly Interface:** Clean console output with color-coded protocol segments.

## 🛠️ Built With
- **Language:** Python
- **Key Libraries:** `socket`, `struct`, `textwrap`
- **Environment:** Linux (Kali Linux/Ubuntu recommended for raw socket access)
1. ** Clone the repository bacsh **:
git clone https://github.com/Ax0cf9/packet-sniffer-tool.git
2. ** Navigate to the file **:
cd packet-sniffer-tool
3. ** Run the sniffer **:
sudo python3 sniffer.py

## 📦 Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/packet-sniffer-cyberai.git](https://github.com/YourUsername/packet-sniffer-cyberai.git)
   cd packet-sniffer-cyberai
Run the sniffer (Requires root privileges):

Bash
sudo python3 sniffer.py

🔐 Ethical Use Warning
This tool is developed for educational purposes and authorized security testing only. Unauthorized interception of network traffic is illegal and unethical. Use it responsibly within your own lab environment.

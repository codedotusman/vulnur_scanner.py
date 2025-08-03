# vulnur_scanner.py

# 🔍 Basic Python Port Scanner

A simple Python script that scans a list of commonly used ports on a given target IP address. Useful for beginners learning about networking, ethical hacking, and basic socket programming.

## 🚀 Features

- Scans a set of commonly used ports
- Shows which ports are open
- Uses Python's built-in `socket` library
- Lightweight and easy to understand

## 📜 How It Works

This script:
1. Prompts you to enter the target IP address
2. Iterates over a predefined list of ports
3. Attempts to connect to each port
4. Displays open ports in the console

## 🧠 Ports Scanned

The script scans these commonly used ports:

| Port | Service         |
|------|------------------|
| 21   | FTP              |
| 22   | SSH              |
| 23   | Telnet           |
| 80   | HTTP             |
| 443  | HTTPS            |
| 445  | SMB              |
| 3306 | MySQL            |
| 8080 | Alternative HTTP |
| 3389 | RDP              |

## 🧪 How to Use

1. Make sure you have Python installed (3.x)
2. Copy the script into a file called `port_scanner.py`
3. Run it in terminal:
   ```bash
   python port_scanner.py

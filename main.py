import socket

target = input("Target IP address: ")
ports = [21, 22, 23, 80, 443, 445, 3306, 8080, 3389]

print(f"\nScanning {target}...\n")

for port in ports:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} is open")
        s.close()
    except:
        pass
import sys

import socket

# Ask user for target IP or hostname
# If IP/host is given as a command-line argument, use that
if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    # Otherwise ask the user
    target = input("Enter IP address or hostname to scan (e.g. 127.0.0.1): ")


# Common ports to scan
ports = [21, 22, 23, 80, 443, 3000, 5000, 8080]

print(f"\nScanning target: {target}\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
    except Exception as e:
        print(f"[!] Error on port {port}: {e}")
    finally:
        s.close()

#!/usr/bin/env python3
"""
AETHERIUM Port Scanner - Basic TCP port scanner for security assessments.
Usage: python3 aetherium_scanner.py <target_ip>
"""

import socket
import sys
from datetime import datetime

def scan_ports(target, ports=[21, 22, 80, 443, 3306, 8080]):
    """Scan common ports on target host."""
    print(f"\n[+] AETHERIUM Security Scanner")
    print(f"[+] Target: {target}")
    print(f"[+] Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[✓] Port {port}: OPEN")
            else:
                print(f"[✗] Port {port}: CLOSED")
            sock.close()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit()
    except socket.gaierror:
        print("[!] Hostname could not be resolved")
    except socket.error:
        print("[!] Could not connect to server")
    
    print("-" * 50)
    print("[+] Scan completed")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        scan_ports(sys.argv[1])
    else:
        print("Usage: python3 aetherium_scanner.py <target_ip>")
        print("Example: python3 aetherium_scanner.py 192.168.1.1") 


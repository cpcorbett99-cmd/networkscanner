import socket
import requests
import nmap
from datetime import datetime

# Scan a range of TCP ports on the target and return any ports that respond.
def port_scan(target, start_port, end_port):
        print(f"Scanning target: {target} for open ports from {start_port} to {end_port}")
        open_ports = []

        # Check each port in the requested range.
        for port in range(start_port, end_port + 1):
                # Create a new socket for each port connection attempt.
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # connect_ex returns 0 if the port is open; otherwise it returns an error code.
                result = sock.connect_ex((target, port))

                if result == 0:  # Port is open.
                        open_ports.append(port)

                sock.close()

        return open_ports

# Connect to a specific port and read the initial banner/message sent by the service.
def banner_grab(target, port):
        print(f"Grabbing banner for {target}:{port}")
        try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
                sock.settimeout(2)

                # Receive the first chunk of data from the service.
                banner = sock.recv(1024).decode('utf-8', errors='ignore')
                sock.close()
                return banner.strip()
        except:
                # Return None if the connection fails or no banner is sent.
                return None

# Use nmap to gather service and vulnerability information for the target.
def vulnerability_scan(target):
        print(f"Scanning target: {target} for vulnerabilities...")
        nm = nmap.PortScanner()
        try:
                # -O detects OS information, -sV identifies services, and --script=vuln runs vulnerability scripts.
                nm.scan(hosts=target, arguments="-O -sV --script=vuln")
                return nm[target]
        except Exception as e:
                print(f"Error during vulnerability scan: {e}")
                return None

# Run the full scan workflow: port scan, banner grabbing, and vulnerability detection.
def network_scan(target, start_port, end_port):
        print(f'Starting network scan for target: {target}..')
        start_time = datetime.now()

        # Find all open ports in the given range.
        open_ports = port_scan(target, start_port, end_port)
        if open_ports:
                print(f'Open ports found: {open_ports}')
        else:
                print("No open ports found")

        # Try to collect a service banner for each open port.
        for port in open_ports:
                banner = banner_grab(target, port)
                if banner:
                        print(f"Banner for {target}:{port} - {banner}")
                else:
                        print(f"No banner found for {target}:{port}")

        # Run an nmap vulnerability scan and display useful findings.
        vuln_info = vulnerability_scan(target)
        if vuln_info:
                if "hostnames" in vuln_info:
                        print(f"Hostnames: {vuln_info['hostnames']}")
                if "osmatch" in vuln_info:
                        print(f"Operating System: {vuln_info['osmatch']}")
                if "vulns" in vuln_info:
                        print(f"Vulnerabilities: {vuln_info['vulns']}")
        else:
                print(f"No vulnerabilities detected or unableto detect")

        end_time = datetime.now()
        print(f"Scan completed in: {end_time - start_time}")

# Entry point for the script.
if __name__ == "__main__":
        target_ip = input("Enter the target IP or Hostname: ")
        start_port = int(input("Enter the starting port for scanning: "))
        end_port = int(input("Enter te ending port for scanning: "))

        network_scan(target_ip, start_port, end_port)
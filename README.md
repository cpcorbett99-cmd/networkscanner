# Network Scanner

A simple Python network scanning tool that checks for open ports, grabs service banners, and runs a basic vulnerability scan using `nmap`.

## Features

- Scans a chosen range of TCP ports
- Detects open ports on a target host
- Connects to open ports to read the service banner
- Uses `nmap` to collect host, OS, and vulnerability information
- Displays scan duration and results in the terminal

## Requirements

Before running the script, make sure you have:

- Python 3 installed
- Run `pip install requirements.txt` to install all requirements
- `nmap` installed on your system
- The Python packages in your environment

Install the Python dependencies:

```bash
pip install requests python-nmap
```

If you are using a virtual environment, activate it first and then run the install command above.

## Installing Nmap

On Windows, install Nmap from the official website and ensure it is available in your system PATH.

On Linux/macOS, you can usually install it using your package manager, for example:

```bash
sudo apt install nmap
```

or

```bash
brew install nmap
```

## Usage

Run the script:

```bash
python networkscanner.py
```

You will be prompted to enter:

1. The target IP address or hostname
2. The starting port number
3. The ending port number

Example:

```bash
Enter the target IP or Hostname: 192.168.1.10
Enter the starting port for scanning: 1
Enter te ending port for scanning: 100
```

The program will:

- scan the selected port range
- print any open ports
- attempt to read banners from open services
- run an `nmap` vulnerability scan for the host

## Important Note

This tool is intended for educational and authorized security testing only. Do not scan hosts or networks without permission from the owner.
This tool was created purely for educational purposes.

## Files

- `networkscanner.py` – main scanner logic
- `requirements.txt` – dependency file

## Disclaimer

Use responsibly and only on systems you are authorized to test. The author is not responsible for misuse of this program.

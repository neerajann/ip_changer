Tor IP Rotator

Automatically rotate your IP address via Tor every few seconds using Python.

This tool uses Tor's ControlPort with password authentication to request a new Tor circuit (NEWNYM) and fetch the current IP through the Tor network. Ideal for testing, privacy, and anonymity purposes.

Features

Rotate Tor exit IP every specified interval (default 10 seconds)

Uses password authentication for ControlPort (no root required)

Works with Python virtual environments (venv)

Colored terminal output

Compatible with Kali Linux and other Linux distributions

Requirements

Python 3.8+

Tor service installed and running

Python packages: stem, requests[socks]

Installation

Clone the repository:

git clone https://github.com/yourusername/tor-ip-rotator.git
cd tor-ip-rotator


Create a Python virtual environment:

python3 -m venv ~/tor_env
source ~/tor_env/bin/activate


Install required packages:

pip install requests[socks] stem


Set up Tor ControlPort:

Edit /etc/tor/torrc and add:

ControlPort 9051
HashedControlPassword <YOUR_HASHED_PASSWORD>


Generate hashed password:

tor --hash-password "mypassword"


Restart Tor:

sudo systemctl restart tor

Usage

Activate your venv:

source ~/tor_env/bin/activate


Run the IP rotator script:

python ip_changer.py


The script will rotate your IP every 10 seconds (or the interval you set in the code) and print the new IP in green.

Customization

Change interval:
Modify the INTERVAL variable in ip_changer.py:

INTERVAL = 10  # seconds


Change Tor password:
Set TOR_PASSWORD in ip_changer.py to match your torrc password:

TOR_PASSWORD = "mypassword"

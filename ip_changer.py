import time
import requests
from stem import Signal
from stem.control import Controller

TOR_PROXY = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

CONTROL_PORT = 9051
TOR_PASSWORD = "#Neerajan@9821"  # use the password you set in torrc
INTERVAL = 10  # seconds

def get_ip():
    try:
        return requests.get("https://checkip.amazonaws.com", proxies=TOR_PROXY, timeout=10).text.strip()
    except:
        return "Error fetching IP"

def rotate_ip(controller):
    controller.signal(Signal.NEWNYM)
    time.sleep(2)  # let Tor build new circuit

def main():
    with Controller.from_port(port=CONTROL_PORT) as controller:
        controller.authenticate(password=TOR_PASSWORD)
        print("=== Tor IP Rotator Started ===\n")
        while True:
            rotate_ip(controller)
            ip = get_ip()
            print(f"\033[92mNew IP: {ip}\033[0m")
            time.sleep(INTERVAL)

if __name__ == "__main__":
    main()

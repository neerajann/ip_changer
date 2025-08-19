# Tor IP Rotator

**Automatically rotate your IP address via Tor every few seconds using Python.**

This tool uses Tor's ControlPort with password authentication to request a new Tor circuit (`NEWNYM`) and fetch the current IP through the Tor network. Ideal for testing, privacy, and anonymity purposes.


## Requirements

- Python 3.8+
- Tor service installed and running
- Python packages: `stem`, `requests[socks]`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/tor-ip-rotator.git
cd tor-ip-rotator
```

### 2. Create a Python virtual environment

```bash
python3 -m venv ~/tor_env
source ~/tor_env/bin/activate
```

### 3. Install required packages

```bash
pip install requests[socks] stem
```

### 4. Set up Tor ControlPort

Edit `/etc/tor/torrc` and add:

```bash
ControlPort 9051
HashedControlPassword <YOUR_HASHED_PASSWORD>
```

Generate hashed password:

```bash
tor --hash-password "mypassword"
```

Restart Tor:

```bash
sudo systemctl restart tor
```

## Usage

### 1. Activate your virtual environment

```bash
source ~/tor_env/bin/activate
```

### 2. Run the IP rotator script

```bash
python ip_changer.py
```

The script will rotate your IP every 10 seconds (or the interval you set in the code) and print the new IP in green.

## Customization

### Change interval

Modify the `INTERVAL` variable in `ip_changer.py`:

```python
INTERVAL = 10  # seconds
```

### Change Tor password

Set `TOR_PASSWORD` in `ip_changer.py` to match your `torrc` password:

```python
TOR_PASSWORD = "mypassword"
```

## Configuration

Make sure your Tor configuration in `/etc/tor/torrc` includes:

```bash
# Enable ControlPort
ControlPort 9051

# Set your hashed password (generate with: tor --hash-password "yourpassword")
HashedControlPassword 16:E600ADC1B52C80BB6022A0E999A7734571A451EB6AE50FED489B72E3DF

# Optional: Disable DNS lookups for better privacy
ClientRejectInternalAddresses 1
```

## Troubleshooting

### Common Issues

**Tor service not running:**
```bash
sudo systemctl start tor
sudo systemctl enable tor
```

**Permission denied on ControlPort:**
- Ensure your hashed password is correctly set in `/etc/tor/torrc`
- Verify the password in your Python script matches

**Module not found errors:**
- Make sure you've activated your virtual environment
- Reinstall packages: `pip install --upgrade requests[socks] stem`

## Security Notice

⚠️ **Important:** This tool is for educational, testing, and legitimate privacy purposes only. Always comply with local laws and website terms of service. Use responsibly and ethically.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is provided for educational and research purposes only. Users are responsible for ensuring their use complies with applicable laws and regulations. The authors are not responsible for any misuse of this software.

---

**⭐ If you found this project helpful, please consider giving it a star!**

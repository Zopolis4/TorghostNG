# About NeoTorghost
NeoTorghost is a script that reroutes your computer's internet traffic through Tor.

Rewritten from [TorGhost](https://github.com/SusmithKrishnan/torghost) & [TorghostNG](https://github.com/Zopolis4/TorghostNG)

NeoTorghost was tested on:
* Arch Linux

# Before you use NeoTorghost
* BitTorrent traffic will be blocked by iptables.
* NeoTorghost will disable IPv6 to prevent IPv6 leaks.

# Installing NeoTorghost
NeoTorghost currently supports:
* GNU/Linux distros based on Arch Linux
* GNU/Linux distros based on Debian/Ubuntu

To install NeoTorghost, open your terminal and enter these commands:    
    
    git clone https://github.com/haudoudo/NeoTorghost
    cd NeoTorghost
    sudo python3 install.py
    torghostng -h
    
Alternatively, you can use it without installation by downloading `neotorghost.py`, then running it with `python3 neotorghost.py`.

# Help
    OPTIONS:
      -h,  --help     Show this help message and exit
      -s,  --start    Start connecting to Tor
      -x,  --stop     Stop connecting to Tor
      -r,  --renew    Renew the current Tor circuit
      -i,  --id       COUNTRY ID  Connect to Tor exit node of a specific country. Go to CountryCode.org to search country ID
      -m,  --mac      INTERFACE  Randomly change MAC address. Use 'ifconfig' to show interface devices
      -c,  --checkip  Check your current IPv4 address
      -d,  --dns      Use this to fix DNS when website address can't be resolved
      -p,  --privoxy  Connecting to Tor with Privoxy - Enhance your privacy
      -a,  --auto     Auto renew Tor circuit every 5 minutes
      -l,  --language Change the display language. English is the default
      -ll, --list     Show the available languages list
      -u,  --update   Check for update
      -n,  --nodelay  Disable delay time

## Added to TorghostNG
* Auto renew circuit every 5 minutes
  * Stopping NeoTorghost also disables the auto-renew
    * ```neotorghost -x ```
* Refined config
* Refined command line interaction
* Reset version
* Auto reinstalls if files are missing

You can combine multiple flags at the same time, such as:
* `neotorghost -s -m INTERFACE`: Changing MAC address before connecting
* `neotorghost -c -m INTERFACE`: Checking IP address and changing MAC address

# How to update NeoTorghost
Open Terminal and type `neotorghost -u` with sudo to update NeoTorghost, but it will download new NeoTorghost to `/root`, because you're running it as root. If you don't like that, you can type `git pull -f` and `sudo python3 install.py`.

Disable JavaScript.

# and
* **Don't spam or perform DoS attacks with Tor.**
* **Don't torrent over Tor.**
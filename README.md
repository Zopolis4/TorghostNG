# About TorghostNG
TorghostNG is a script that reroutes your computer's internet traffic through Tor. An unofficial GUI is available [here](https://github.com/AnythingSuitable/TorghostNG-GUI).

Rewritten from [TorGhost](https://github.com/SusmithKrishnan/torghost) with Python 3.

TorghostNG was tested on:
* Kali Linux
* Manjaro

# What's new in TorghostNG 2.1
* Rewrote readme
* Replaced broken links to old repo

# Before you use TorghostNG
* BitTorrent traffic will be blocked by iptables.
* TorghostNG will disable IPv6 to prevent IPv6 leaks.

# Installing TorghostNG
TorghostNG currently supports:
* GNU/Linux distros based on Arch Linux
* GNU/Linux distros based on Debian/Ubuntu

To install TorghostNG, open your terminal and enter these commands:    
    
    git clone https://github.com/Zopolis4/TorghostNG
    cd TorghostNG
    sudo python3 install.py
    torghostng -h
    
Alternatively, you can use it without installation by downloading `torghostng.py`, then running it with `python3 torghostng.py`.

# Help
    OPTIONS:
      -h, --help      Show this help message and exit
      -s, --start     Start connecting to Tor
      -x, --stop      Stop connecting to Tor
      -r, --renew     Renew the current Tor circuit
      -id COUNTRY ID  Connect to Tor exit node of a specific country. Go to CountryCode.org to search country ID
      -mac INTERFACE  Randomly change MAC address. Use 'ifconfig' to show interface devices
      -c, --checkip   Check your current IPv4 address
      --dns           Use this to fix DNS when website address can't be resolved
      -l, --language  Change the display language. English is the default
      --list          Show the available languages list
      -u, --update    Check for update
      --nodelay       Disable delay time

You can combine multiple flags at the same time, such as:
* `torghostng -s -m INTERFACE`: Changing MAC address before connecting
* `torghostng -c -m INTERFACE`: Checking IP address and changing MAC address

# How to update TorghostNG
Open Terminal and type `torghostng -u` with sudo to update TorghostNG, but it will download new TorghostNG to `/root`, because you're running it as root. If you don't like that, you can type `git pull -f` and `sudo python3 install.py`.

# Notes before you use Tor
Tor can't help you completely anonymous, just almost:
* [Tor’s Biggest Threat – Correlation Attack](https://theonionweb.com/2016/10/25/tors-biggest-threat-correlation-attack)
* [Is Tor Broken? How the NSA Is Working to De-Anonymize You When Browsing the Deep Web](https://null-byte.wonderhowto.com/how-to/is-tor-broken-nsa-is-working-de-anonymize-you-when-browsing-deep-web-0148933)
* [Use Traffic Analysis to Defeat TOR](https://null-byte.wonderhowto.com/how-to/use-traffic-analysis-defeat-tor-0149100)

It's recommended that you should use [NoScript](https://noscript.net) before before surfing the web with Tor. NoScript shall block JavaScript/Java/Flash scripts on websites to make sure they won't reveal your real identify.

# And please
* **Don't spam or perform DoS attacks with Tor.** It is ineffective, you will just waste the time, money and bandwith of Tor volunteers.
* **Don't torrent over Tor.** If you want to keep anonymous while torrenting, use a no-logs VPN.

[Bittorrent over Tor isn't a good idea](https://blog.torproject.org/bittorrent-over-tor-isnt-good-idea)

[Not anonymous: attack reveals BitTorrent users on Tor network](https://arstechnica.com/tech-policy/2011/04/not-anonymous-attack-reveals-bittorrent-users-on-tor-network)

![Don't torrent over Tor, please](https://github.com/Zopolis4/TorghostNG/raw/master/images/Don't%20torrent%20over%20Tor.png)

# Changelog
Version 2.1
* Rewrote readme
* Replaced broken links to old repo

Version 2.0
* Add a new language: German
* Change `langconf.txt` to `langconf`
* Some functions don't require ROOT to run anymore
* Fix "Check Tor connection..." loops
* Remove unneeded codes
* Fix bugs

Version 1.7
* Fix updating error
* Fix "Checking Tor connection" loop (by installing `curl`)

Version 1.6
* Fix some bugs
* Faster Installation

Version 1.5
* Fix bugs of version 1.4

Version 1.4
* Support connecting to Tor with Privoxy

You can read how to use Privoxy together with Tor at [Privoxy FAQ](https://privoxy.org/faq/misc.html#TOR)

Version 1.2
* Fix `update_commands` and others in [torghostng.py](https://github.com/gitkern3l/TorghostNG/blob/master/torghostng.py)
* Chang a few things in [`theme.py`](https://github.com/gitkern3l/TorghostNG/blob/master/torngconf/theme.py)
* Chang a few things in [`install.py`](https://github.com/gitkern3l/TorghostNG/blob/master/install.py)
* Now you can change Tor circuit with `-r`

Version 1.1
* Check your IPv6
* Change all "TOR" to "Tor"
* Block BitTorrent traffic
* Auto disable IPv6 before connecting to Tor

# Screenshots of Torghost (Version 2.0)
* TorghostNG 2.0's installation

![Installation](https://github.com/Zopolis4/TorghostNG/raw/master/images/TorghostNG%202%20Installation.png)

* TorghostNG 2.0 checking Tor status (**non-root**)

![Checking Tor status](https://github.com/Zopolis4/TorghostNG/raw/master/images/TorghostNG%202%20check%20ip%20non-root.png)

* TorghostNG 2.0 connecting to tor exit nodes in the US

![Connecting to the US](https://github.com/Zopolis4/TorghostNG/raw/master/images/TorghostNG%202%20Connect%20to%20US.png)

* TorghostNG 2.0 connecting to Tor through Privoxy

![Connecting to Tor with Privoxy](https://github.com/Zopolis4/TorghostNG/raw/master/images/TorghostNG%202%20Tor%20Privoxy.png)

* TorghostNG 2.0 in German

![German](https://github.com/Zopolis4/TorghostNG/raw/master/images/TorghostNG%202%20German.png)
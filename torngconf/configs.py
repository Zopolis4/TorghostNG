#!/usr/bin/python3

from subprocess import getoutput
from os import path

if path.isfile('/usr/bin/apt') == True:
    TOR_USER = 'debian-tor'
else:
    TOR_USER = 'tor'
    
Torrc = '/etc/tor/torngrc'
resolv = '/etc/resolv.conf'
Sysctl = '/etc/sysctl.conf'
Privoxy = '/etc/privoxy/config'

TOR_UID = getoutput('id -ur {}'.format(TOR_USER))

FIX_DNS = """nameserver 1.1.1.1
nameserver 1.0.0.1
nameserver 2606:4700:4700::1111
nameserver 2606:4700:4700::1001"""

DISABLE_IPv6 = """net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1"""

resolvConfig = 'nameserver 127.0.0.1'

privoxy_conf = """listen-address 127.0.0.1:8118
forward-socks5 / 127.0.0.1:9040 .
forward-socks4 / 127.0.0.1:9040 .
forward-socks4a / 127.0.0.1:9040 ."""

TorrcConfig = """VirtualAddrNetwork 10.0.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 5353
ControlPort 9051
RunAsDaemon 1"""

TorrcConfig_exitnode = """VirtualAddrNetwork 10.0.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 5353
ControlPort 9051
RunAsDaemon 1
ExitNodes {%s}"""

iptables_rules = """NON_TOR="192.168.1.0/24 192.168.0.0/24"
TOR_UID={}
TRANS_PORT="9040"

iptables -F
iptables -t nat -F

iptables -t nat -A OUTPUT -m owner --uid-owner $TOR_UID -j RETURN
iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 5353
for NET in $NON_TOR 127.0.0.0/9 127.128.0.0/10; do
 iptables -t nat -A OUTPUT -d $NET -j RETURN
done
iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT

iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
for NET in $NON_TOR 127.0.0.0/8; do
 iptables -A OUTPUT -d $NET -j ACCEPT
done
iptables -A OUTPUT -m owner --uid-owner $TOR_UID -j ACCEPT
iptables -A OUTPUT -j REJECT

iptables -A FORWARD -m string --string "BitTorrent" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "BitTorrent protocol" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "peer_id=" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string ".torrent" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "announce.php?passkey=" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "torrent" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "announce" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "info_hash" --algo bm --to 65535 -j DROP""".format(TOR_UID)

IpFlush = """iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X"""

set_proxy="""export https_proxy=127.0.0.1:8118
export http_proxy=127.0.0.1:8118
export socks5_proxy=127.0.0.1:9040
export socks4_proxy=127.0.0.1:9040
export socks4a_proxy=127.0.0.1:9040"""

rm_proxy="""export https_proxy=
export http_proxy=
export socks5_proxy=
export socks4_proxy=
export socks4a_proxy="""

update_commands = """cd ~ && rm -rf TorghostNG
git clone https://github.com/githacktools/TorghostNG
cd TorghostNG
sudo python3 install.py && sudo python3 install.py"""
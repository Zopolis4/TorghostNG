#!/usr/bin/python3

import argparse
from time import sleep
from json import JSONDecodeError, loads
from sys import argv, exit
from os import geteuid, system, name

try:
    from torngconf.theme import *
    from torngconf.configs import *
except ModuleNotFoundError:
    print("TorghostNG is lacking its needed files. Reinstall TorghostNG from Github pls")
    exit()

SLEEP_TIME = 1.0
VERSION = "2.0"

def the_argparse(language=English):
        parser = argparse.ArgumentParser(usage="torghostng [-h] -s|-x|-id|-r|-m|-c|-l|--list")
        parser._optionals.title = language.options
        parser.add_argument("-p","--privoxy", help=language.privoxy_help, action="store_true")
        parser.add_argument("-s","--start", help=language.start_help, action="store_true")
        parser.add_argument("-x", "--stop", help=language.stop_help, action="store_true")
        parser.add_argument("-r", "--renew", help=language.circuit_help, action="store_true")
        parser.add_argument("-id", help=language.id_help, metavar=language.country_id, type=str)
        parser.add_argument("-mac", help=language.changemac_help, metavar="INTERFACE", type=str)
        parser.add_argument("-c","--checkip", help=language.checkip_help, action="store_true")
        parser.add_argument("--dns", help=language.dns_help, action="store_true")
        parser.add_argument("-l","--language", help=language.language_help, action="store_true")
        parser.add_argument("--list", help=language.language_list_help, action="store_true")
        parser.add_argument("-u", "--update", help=language.update_help, action="store_true")
        parser.add_argument("--nodelay", help=language.no_delay_help, action="store_true")

        if len(argv) == 1:
            banner()
            parser.print_help()
            exit()

        return parser.parse_args()


if (path.isfile('/usr/bin/upgradepkg') == True) or (path.isfile('/usr/bin/torngconf/langconf') == False):
    LANGCONF = 'torngconf/langconf'
else:
    LANGCONF = '/usr/bin/torngconf/langconf'


def banner():
    print(the_banner)
    print(language.description)


def check_lang():
    try:
        if path.isfile(LANGCONF) == True:
            with open(LANGCONF) as file_lang:
                language = eval(file_lang.readline())

                file_lang.close()

                print(language.applying_language, end='', flush=True)
                print(language.done)

                return language
        else:
            language = choose_lang()
            return language
        
    except KeyboardInterrupt:
        print()
        exit()
    except (NameError, SyntaxError, AttributeError):
        language = choose_lang()
        return language
    except FileNotFoundError:
        print("TorghostNG is lacking its needed files. Reinstall TorghostNG from Github pls")
        exit()


def choose_lang(language=English):
    try:
        with open(LANGCONF, mode="w") as file_lang:            
            print(language.language_list)
            choice = int(input(language.choose_your_lang))
            
            if LANGCONF != 'torngconf/langconf':
                check_windows_check_root()
            
            if choice == 1:
                language = English
                file_lang.write("English")
            
            elif choice == 2:
                language = Vietnamese
                file_lang.write("Vietnamese")
                
            elif choice == 3:
                lannguage = German
                file_lang.write("German")
                
            else:
                print()
                print(language.invalid_choice)
                choose_lang(language)
            
            print(language.applying_language)
            file_lang.close()
            return language

    except KeyboardInterrupt:
        print()
        exit()

    except ValueError:
        choose_lang()


def check_windows_check_root(os=None):
    if os == "windows":
        if name == "nt":
            print(English.sorry_windows)
            exit()
    
    elif geteuid() != 0:
        print(English.root_please)
        exit()

        
def check_dependencies(dependence):
    if path.isfile("/usr/bin/" + dependence) == False:
            
        if dependence == "netstat":
            dependence = "net-tools"

        print(language.install_pls.format(dependence))
        exit()


def check_update():
    try:
        check_dependencies('curl')

        print(language.checking_update, end='', flush=True)
        version = getoutput('curl -s --max-time 60 https://raw.githubusercontent.com/Zopolis4/TorghostNG/master/torngconf/Version')
        sleep(SLEEP_TIME)
        print(language.done)

        if (version not in VERSION) == True:
            print(language.outofdate)
            choice = str(input(language.wanna_update))
            
            if choice[0].upper() == "Y":
                check_windows_check_root()
                print(language.updating.format(version))
                system(update_commands)
                exit()
                   
        else:
            print(language.uptodate)
    
    except KeyboardInterrupt:
        print()
        exit()


def check_tor(status):
    try:
        check_dependencies('curl')

        print(language.checking_tor, end='', flush=True)
        sleep(SLEEP_TIME)
        tor_status = loads(getoutput("curl -s --max-time 60 https://check.torproject.org/api/ip"))
        print(language.done)
        
        if tor_status['IsTor'] == False:
            if status == "failed":
                print(language.tor_failed)
                stop_connecting()
                
            elif status == "stopped":
                print(language.tor_disconnected)
            
        else:
            check_dependencies('netstat')

            if 'LISTEN' in getoutput('netstat -atnp | grep privoxy'):
                print(language.tor_success.format('Privoxy'))
                
            else:
                print(language.tor_success.format(''))

        check_ip()

    except KeyboardInterrupt:
        print()
        exit()

    except JSONDecodeError:
        print()
        sleep(1)
        check_tor(status)


def check_ip():
    try:
        check_dependencies('curl')

        print(language.checking_ip, end='', flush=True)
        sleep(SLEEP_TIME)
        ipv4_address = getoutput('curl -s --max-time 60 https://api.ipify.org')
        ipv6_address = getoutput('curl -s --max-time 60 https://api6.ipify.org')
        print(language.done)
        
        print(language.your_ip.format('IPv4') + color.BOLD + ipv4_address + color.END)
        
        if (ipv6_address != ipv4_address) and len(ipv6_address) > 0:
            print(language.your_ip.format('IPv6') + color.BOLD + ipv6_address + color.END)

    except KeyboardInterrupt:
        print()
        exit()


def start_connecting(id=None,privoxy=None):
    try:
        check_windows_check_root()

        print(icon.process + ' ' + language.start_help)
        
        # Disable IPv6
        if DISABLE_IPv6 == open(Sysctl).read():
            print(language.ipv6_already_disabled)
            
        else:
            print(language.disable_ipv6_info)

            system('sudo cp {0} {0}.backup'.format(Sysctl))
            print(language.disabling_ipv6, end='', flush=True)
            
            with open(Sysctl, mode='w') as file_sysctl:
                file_sysctl.write(DISABLE_IPv6)
                file_sysctl.close()

            sleep(SLEEP_TIME)
            print(language.done)

        getoutput('sudo sysctl -p')

        # Configure Torrc
        check_dependencies('tor')

        if id != None: # Check for exit node
            torrconfig = TorrcConfig_exitnode %(id)
            print(language.id_tip)
        else:
            torrconfig = TorrcConfig


        if (path.isfile(Torrc)) and (torrconfig == open(Torrc).read()):
            print(language.already_configured.format('TorghostNG Torrc'))
            
        else:
            print(language.configuring.format('TorghostNG Torrc'), end='', flush=True)

            with open(Torrc, mode='w') as file_torrc:
                file_torrc.write(torrconfig)
                file_torrc.close()
                
            sleep(SLEEP_TIME)
            print(language.done)

        # Configure DNS resolv.conf
        if privoxy == None:
            system('systemctl stop privoxy')
            if resolvConfig == open(resolv).read():
                print(language.already_configured.format('DNS resolv.conf'))
                
            else:
                system("cp {0} {0}.backup".format(resolv))
                
                with open(resolv, mode='w') as resolv_file:
                    print(language.configuring.format('DNS resolv.conf'), end='', flush=True)
                    resolv_file.write(resolvConfig)
                    resolv_file.close()
                    sleep(SLEEP_TIME)
                    print(language.done)

        # Stop tor service
        check_dependencies('tor')

        print(language.stopping_tor, end='', flush=True)
        system('systemctl stop tor')
        system('fuser -k 9051/tcp > /dev/null 2>&1')
        sleep(SLEEP_TIME)
        print(language.done)

        # Configure and start Privoxy
        if privoxy == True:
            check_dependencies('privoxy')

            system(set_proxy)
            
            if privoxy_conf == open(Privoxy).read():
                print(language.already_configured.format('Privoxy'))
                
            else:
                system('cp {0} {0}.backup'.format(Privoxy))
                
                with open(Privoxy, mode='w') as privoxy_file:
                    print(language.configuring.format('Privoxy'), end='', flush=True)
                    privoxy_file.write(privoxy_conf)
                    privoxy_file.close()
                    sleep(SLEEP_TIME)
                    print(language.done)
                    
            system('systemctl start privoxy')

        # Start new tor service
        check_dependencies ('tor')

        print(language.starting_tor, end='', flush=True)
        system('sudo -u {0} tor -f {1} > /dev/null'.format(TOR_USER, Torrc))
        sleep(SLEEP_TIME)
        print(language.done)

        # Show some info
        print(language.iptables_info)
        print(language.block_bittorrent)

        # Configure iptables
        print(language.setting_iptables, end='', flush=True)
        system(iptables_rules)
        sleep(SLEEP_TIME)
        print(language.done)
        
        check_tor('failed') # Check tor connection

        print(language.dns_tip) # Show some info

    except KeyboardInterrupt:
        print()
        exit()
    except FileNotFoundError:
        system('touch {}'.format(Sysctl))
        start_connecting(id,privoxy)


def stop_connecting():
    try:
        check_windows_check_root()

        print(icon.process + ' ' + language.stop_help)
        
        # Restore Privoxy configuration
        check_dependencies('netstat')

        if 'LISTEN' in getoutput('netstat -atnp | grep privoxy'):
            print(language.restoring_configuration.format('Privoxy'), end='', flush=True)
            
            if path.isfile(Privoxy + '.backup')  == True:
                system('mv {0}.backup {0}'.format(Privoxy))
            
            system('systemctl stop privoxy')
            system(rm_proxy)
            
            sleep(SLEEP_TIME)
            print(language.done)

        # Restore DNS resolv.conf configuration
        if path.isfile(resolv + '.backup') == True:
            print(language.restoring_configuration.format('DNS resolv.conf'), end='', flush=True)

            system('mv {0}.backup {0}'.format(resolv))

            sleep(SLEEP_TIME)
            print(language.done)

        # Restore IPv6 configuration
        if path.isfile(Sysctl + '.backup') == True:
            print(language.restoring_configuration.format('IPv6'), end='', flush=True)

            system('mv {0}.backup {0}'.format(Sysctl))
            system('sudo sysctl -p')

            sleep(SLEEP_TIME)
            print(language.done)

        # Reset iptables configuration
        print(language.flushing_iptables, end='', flush=True)
        system(IpFlush)
        system('fuser -k 9051/tcp > /dev/null 2>&1')
        sleep(SLEEP_TIME)
        print(language.done)

        # Restart NetworkManager
        print(language.restarting_network, end='', flush=True)
        system('systemctl restart --now NetworkManager')
        sleep(8)
        print(language.done)
        
        check_tor('stopped') # Check tor connection

        print(language.dns_tip) # Show some info

    except KeyboardInterrupt:
        print()
        exit()


def change_tor_circuit():
    try:
        check_windows_check_root()

        check_dependencies('curl')

        print(language.changing_tor_circuit, end='', flush=True)

        tor_status = loads(getoutput("curl -s --max-time 60 https://check.torproject.org/api/ip"))
        
        if tor_status['IsTor'] == True:
            system('pidof tor | xargs sudo kill -HUP')
            sleep(SLEEP_TIME)
            print(language.done)
            check_tor('stopped')
            
        else:
            print()
            start_connecting()
            
    except KeyboardInterrupt:
        print()
        exit()


def changemac(interface):
    try:
        print(language.changing_mac)
        
        i = getoutput('ifconfig {} down'.format(interface))

        if "ERROR" in i:
            print(language.interface_error.format(interface))
        else:
            system('macchanger -r {}'.format(interface))
            system('ifconfig {} up'.format(interface))
            sleep(SLEEP_TIME)
            print(language.mac_changed)
            
        print(language.ifconfig_tip)
        
    except KeyboardInterrupt:
        print()
        exit()


def fix_dns():
    try:
        check_windows_check_root()

        print(language.fixing_dns, end='', flush=True)
        
        with open(resolv, mode='w') as file:
            file.write(FIX_DNS)
            file.close()
            
        sleep(SLEEP_TIME)
        print(language.done)
        
    except KeyboardInterrupt:
        print()
        exit()


if __name__ == "__main__":
    language = check_lang()
    check_windows_check_root('windows')
    args = the_argparse(language)

    banner()
    print()
    
    if args.nodelay == True: SLEEP_TIME = 0

    if args.list == True: print(language.language_list)

    if args.language == True: language = choose_lang(language)
        
    if args.update == True: check_update()

    if args.dns == True: fix_dns()
        
    if args.checkip == True: check_tor('stopped')
        
    your_interface = args.mac
    if your_interface != None: changemac(your_interface)

    if (args.start == True) or (args.privoxy == True):
        if args.privoxy == True:
            start_connecting(None, True)
            
        else:
            start_connecting()

        exit()

    if args.stop == True:
        stop_connecting()
        exit()
        
    the_id = args.id
    if the_id:
        if args.privoxy == True:
            start_connecting(the_id, True)
        else:
            start_connecting(the_id)

        exit()
        
    if args.renew == True: change_tor_circuit()


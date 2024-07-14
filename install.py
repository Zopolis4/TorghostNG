from neotgconf.theme import *
from neotgconf.configs import *
from time import sleep
from os import geteuid, system, path, name


def banner():
    print(the_banner)
    print(language.description)


def check_windows_check_root():
    if name == "nt":
        print(English.sorry_windows)
        exit()
    
    if geteuid() != 0:
        print(language.root_please)
        exit()


def check_lang():
    try:
        if path.isfile('neotgconf/langconf') == True:
            with open('neotgconf/langconf') as file_lang:
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
        print("NeoTorghost is lacking its needed files. Reinstall NeoTorghost from Github pls")
        exit()


def choose_lang(language=English):
    try:
        with open('neotgconf/langconf', mode="w") as file_lang:            
            print(language.language_list)
            choice = int(input(language.choose_your_lang))
            
            if choice == 1:
                file_lang.write("English")
                language = English
    
            
            elif choice == 2:
                file_lang.write("Vietnamese")
                language = Vietnamese

            elif choice == 3:
                file_lang.write("German")

            else:
                print()
                print(language.invalid_choice)
                choose_lang()

            print(language.applying_language)
            file_lang.close()
            return language

    except KeyboardInterrupt:
        print()
        exit()


def uninstall():
    try:
        choice = str(input(language.wanna_uninstall))
        
        if choice[0].upper() == "Y":
            print(language.uninstalling)
            system(f'rm -rf {USRBIN}neotgconf')
            system(f'rm {USRBIN}neotorghost')
            print(language.uninstalled)
            
        else:
            print(language.neotorghost_tip.format('neotorghost') + color.END)
            
        exit()
            
    except KeyboardInterrupt:
        print()
        exit()


language = check_lang()
check_windows_check_root()
banner()


if path.isfile(USRBIN + 'neotorghost') == True:
    print(language.already_installed.format('NeoTorghost'))
    uninstall()

if path.isfile(USRBIN + 'pacman') == True:
    INSTALL_PACKAGES = "pacman -S "
        
elif path.isfile(USRBIN + 'apt') == True:
    INSTALL_PACKAGES = "apt install "
    
elif path.isfile(USRBIN + 'dnf') == True:
    INSTALL_PACKAGES = "dnf install "
        
elif path.isfile(USRBIN + 'yum') == True:
    INSTALL_PACKAGES = "yum install "
        
elif path.isfile(USRBIN + 'zypper') == True:
    INSTALL_PACKAGES = "zypper install "
        
elif path.isfile(USRBIN + 'xbps-install') == True:
    INSTALL_PACKAGES = "xbps-install -S "
        
elif path.isfile(USRBIN + 'upgradepkg') == True:
    INSTALL_PACKAGES = "upgradepkg --install-new "

else:
    print(language.sorry_some_os)
    exit()


def install_package(package):
    try:
        if path.isfile(USRBIN + ''+package) == True:
            print(language.already_installed.format(package))
            
        else:
            print(language.installing.format(package))
            
            if path.isfile(USRBIN + 'upgradepkg') == True:
                print(language.downloading.format(package))

                if package == 'tor':
                    system('wget https://slack.conraid.net/repository/slackware64-current/tor/tor-0.4.2.7-x86_64-1cf.txz')
                    system(INSTALL_PACKAGES + 'tor-0.4.2.7-x86_64-1cf.txz')
                    
                elif package == 'macchanger':
                    system('wget https://slack.conraid.net/repository/slackware64-current/macchanger/macchanger-1.7.0-x86_64-5cf.txz')
                    system(INSTALL_PACKAGES + 'macchanger-1.7.0-x86_64-5cf.txz')
                    
                elif package == 'curl':
                    system('wget http://slackware.cs.utah.edu/pub/slackware/slackware64-14.2/patches/packages/curl-7.72.0-x86_64-1_slack14.2.txz')
                    system(INSTALL_PACKAGES + '--install-new curl-7.72.0-x86_64-1_slack14.2.txz')
                    
                elif package == 'privoxy':
                    system('wget https://packages.slackonly.com/pub/packages/14.2-x86_64/network/privoxy/privoxy-3.0.28-x86_64-1_slonly.txz')
                    system(INSTALL_PACKAGES + 'privoxy-3.0.28-x86_64-1_slonly.txz')
                    
                elif package == 'netstat':
                    system('wget http://slackware.cs.utah.edu/pub/slackware/slackware64-current/slackware64/n/net-tools-20181103_0eebece-x86_64-1.txz')
                    system(INSTALL_PACKAGES + 'net-tools-20181103_0eebece-x86_64-1.txz')
                
            else:
                if package == 'netstat': package = 'net-tools'

                system(INSTALL_PACKAGES + package)

            print(icon.success + language.done)
            print(language.installed.format(package))
            
            if path.isfile(USRBIN + 'upgradepkg') == True:
                print(language.neotorghost_tip.format('python3 neotorghost.py'))
                exit()
            
    except KeyboardInterrupt:
        print()
        exit()


def install_neotorghost():
    try:
        print(language.installing.format('NeoTorghost'))
        system(f'cp -r neotorghost.py /usr/bin && cp -r neotgconf /usr/bin && cp -r neotgutil {USRBIN}')
        system(f'mv {USRBIN}neotorghost.py {USRBIN}neotorghost')
        system(f'chmod +x {USRBIN}neotorghost')
        system(f'rm -rf {USRBIN}torghostng {USRBIN}torngconf')
        
        print(icon.success + language.done)
        print(language.neotorghost_tip.format('neotorghost') + color.END)
        
    except KeyboardInterrupt:
        print()
        exit()


packages = ['tor','macchanger','privoxy','netstat','curl']
for package in packages:
    install_package(package)

install_neotorghost()
exit()
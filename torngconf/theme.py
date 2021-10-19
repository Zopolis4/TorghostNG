#!/usr/bin/python3

class color:
    BLUE = '\033[94m'
    CYAN = '\033[36m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'
    
class icon:
    success = color.GREEN+'[*]'+color.END
    process = color.CYAN+'[+]'+color.END
    info = color.YELLOW+'[i]'+color.END
    error = color.RED+'[!]'+color.END
    question = color.BLUE+'[?]'+color.END

class English:
    options = "OPTIONS"
    downloading = icon.process + "Downloading {}..."
    installing = icon.process + " Installing {}..."
    install_pls = icon.error + " Please install {} please"
    uninstalling = icon.process + " Uninstalling TorghostNG..."
    uninstalled = icon.success + " TorghostNG has been uninstalled"
    installed = icon.success + " {} has been installed"
    already_installed = icon.info + " {} is already installed"
    description = """TorghostNG 2.0 - Make all your internet traffic anonymized through Tor proxy
Rewritten from TorGhost with Python 3"""
    root_please = icon.error + " You must be root, use 'sudo TorghostNG'"
    sorry_windows = icon.error + " Sorry, TorghostNG is not designed for Windows 😛 Use Tor Browser pls"
    sorry_some_os = """I'm sorry, you have to install Tor and macchanger from source by yourself :v I'm too lazy
Tor: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Sorry BSD user, I'm still trying to find way to fully support for BSD"
    current_language = icon.info + " The current display language: "
    language_list = icon.info + """ List of languages:
    1. English
    2. Vietnamese
    3. German"""
    choose_your_lang = icon.question + " Choose your language (1-3): "
    wanna_change_lang = icon.question + " Wanna change the display language? (y/n): "
    wanna_uninstall = icon.question + " Wanna uninstall TorghostNG (y/n): "
    invalid_choice = icon.error + " Invalid choice"
    country_id = "COUNTRY ISO CODE"
    help_help = "Show this help message and exit"
    privoxy_help = "Connecting to Tor with Privoxy - Enhance your privacy"
    start_help = "Start connecting to Tor"
    stop_help = "Stop connecting to Tor"
    circuit_help = "Renew the current Tor circuit"
    id_help = "Connect to Tor exit node of a specific country. Go to CountryCode.org to search country ISO code"
    update_help = "Check for update"
    no_delay_help = "Disable delay time"
    changemac_help = "Randomly change MAC address. Use 'ifconfig' to show interface devices"
    language_help = "Change the display language. English is the default"
    language_list_help = "Show the available languages list"
    checkip_help = "Check your current IPv4 address"
    dns_help = "Use this to fix DNS when website address can't be resolved"
    done = color.GREEN+ " Done"+color.END
    disable_ipv6_info = icon.info + color.BOLD + " For security reason, TorghostNG is gonna disable IPv6 to prevent IPv6 leaks (it happened to me lmao)" + color.END
    iptables_info = icon.info + """ Non-Tor traffic will be blocked by iptables
    Some apps may not be able to connect to the Internet"""
    block_bittorrent = icon.info + """ For the goodness of Tor network, BitTorrent traffic will be blocked by iptables
    with your torrent client :'("""
    applying_language = icon.process + " Applying display language..."
    checking_update = icon.process + " Checking TorghostNG update..."
    outofdate = icon.error + " Your TorghostNG is out-of-date"
    uptodate = icon.success + " Your TorghostNG is up-to-date"
    wanna_update = icon.question + " Wanna update your TorghostNG (y/n): "
    updating = icon.process + " Updating TorghostNG to {}..."
    already_configured = icon.info + " {} file is already configured"
    configuring = icon.process + " Configuring {} file..."
    restoring_configuration = icon.process + " Restoring {} configuration..."
    ipv6_already_disabled = icon.info + " IPv6 is already disabled"
    disabling_ipv6 = icon.process + " Disabling IPv6..."
    stopping_tor = icon.process + " Stopping Tor service..."
    starting_tor = icon.process + " Starting new Tor service..."
    changing_tor_circuit = icon.process + " Changing Tor circuit..."
    setting_iptables = icon.process + " Setting up iptables rules..."
    flushing_iptables = icon.process + " Flushing iptables, resetting to default..."
    checking_ip = icon.process + " Checking your current IP..."
    fixing_dns = icon.process + " Fixing your DNS problem..."
    your_ip = icon.info + " Your current {} address: "
    checking_tor = icon.process + " Checking Tor connection..."
    tor_success = icon.success + " Congratulations! You've been connecting to Tor {}"
    tor_failed = icon.error + " The connecting process to Tor has failed"
    tor_disconnected = icon.success + " You've been disconnecting from Tor"
    try_again = icon.question + " Wanna try again (y/n): "
    restarting_network = icon.process + " Restarting NetworkManager..."
    changing_mac = icon.process + " Changing your current MAC address..."
    mac_changed = icon.success + " You MAC address has been changed"
    ifconfig_tip = icon.info + color.BOLD + " You can use 'ifconfig' to show interface devices" + color.END
    id_tip = icon.info + color.BOLD + " You can go to https://CountryCode.org to search country ISO code" + color.END
    torghostng_tip = icon.info + color.BOLD + " You can run TorghostNG with '{}'"
    dns_tip = icon.info + " If you have problem with resolving website address, use '--dns' to fix it"
    interface_error = icon.error + " There is no interface named {}. Changing failed"
    
class Vietnamese(English):
    options = "CÁC LỰA CHỌN"
    downloading = icon.process + "Đang tải {}..."
    installing = icon.process + " Đang cài đặt {}..."
    install_pls = icon.error + " Cài {} đi làm ơn đó ☹"
    uninstalling = icon.process + " Đang gỡ cài đặt TorghostNG..."
    uninstalled = icon.success + " TorghostNG đã được gỡ cài đặt"
    installed = icon.success + " {} đã được cài đặt"
    already_installed = icon.info + " {} đã được cài đặt sẵn"
    description = """TorghostNG 2.0 - Giúp bạn kết nối Internet ẩn danh qua Tor
Được gõ lại từ TorGhost bằng Python 3"""
    root_please = icon.error + " Phải chạy TorghostNG với quyền root nha, thử 'sudo torghostng' xem"
    sorry_windows = icon.error + " Xin lỗi các bạn dùng Windows nhá ☹ Các bạn dùng Tor Brower nha"
    sorry_some_os = """Với hệ điều hành này thì bạn phải cài Tor với macchanger một cách thủ công thôi :v
Tor: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Mình đang tìm các hỗ trợ BSD, xin lỗi bạn :("
    current_language = icon.info + " Ngôn ngữ hiển thị hiện tại: "
    language_list = icon.info + """ List of languages:
    1. English
    2. Vietnamese
    3. German"""
    choose_your_lang = icon.question + " Chọn ngôn ngữ của bạn (1-3): "
    wanna_change_lang = icon.question + " Muốn thay đổi ngôn ngữ hiển thị không? (y/n): "
    wanna_uninstall = icon.question + " Bạn muốn gỡ TorghostNG đi không (y/n): "
    invalid_choice = icon.error + " Lựa chọn không hợp lệ lmao :v"
    country_id = "MÃ ISO QUỐC GIA"
    help_help = "Hiển thị phần trợ giúp và thoát"
    privoxy_help = "Kết nối đến mạng Tor với Privoxy - Tăng cường ẩn danh"
    start_help = "Bắt đầu kết nối đến mạng Tor"
    stop_help = "Ngưng kết nối đến mạng Tor"
    circuit_help = "Thay đổi mạch Tor"
    id_help = "Thay đổi địa chỉ IPv4 sang một quốc gia cụ thể. Vô CountryCode.org để xem ISO code"
    update_help = "Kiểm tra cập nhật"
    no_delay_help = "Tắt hiệu ứng thời gian đi"
    changemac_help = "Thay đổi ngẫu nhiên địa chỉ MAC. Dùng lệnh 'ifconfig' để xem các interface"
    language_help = "Thay đổi ngôn ngữ hiển thị. Tiếng Anh là mặc định"
    language_list_help = "Hiển thị danh sách các ngôn ngữ hiện có"
    checkip_help = "Xem địa chỉ IP hiện tại"
    dns_help = "Dùng cái này để sửa vấn đề về DNS"
    done = color.GREEN+ " Đã xong" + color.END
    disable_ipv6_info = icon.info + color.BOLD + " Vì lý do bảo mật, TorghostNG sẽ vô hiệu hóa IPv6 để ngăn ngừa IPv6 rò rỉ (mình bị dính chưởng rồi nè lmao)" + color.END
    iptables_info = icon.info + """ iptables sẽ chặn các kết nối không đi qua Tor
    Ứng dụng nào thích chơi kết nối một mình một kiểu sẽ bị chặn"""
    block_bittorrent = icon.info + """ Vì mạng Tor, iptables sẽ chặn các kết nối BitTorrent
    Mặc dù bạn có thể "vượt rào" với phần cài đặt trong phần mềm torrent :'("""
    applying_language = icon.process + " Đang áp dụng ngôn ngữ hiển thị..."
    checking_update = icon.process + " Đang kiểm tra cập nhật..."
    outofdate = icon.error + " Torghost bạn xài đã cổ lỗ sĩ rồi :v"
    uptodate = icon.success + " TorghostNG bạn xài là bản mới nhất :D"
    wanna_update = icon.question + " Muốn cập nhật Torghost luôn không (y/n): "
    updating = icon.process + " Đang cập nhật TorghostNG lên phiên bản {}..."
    already_configured = icon.info + " Tệp cấu hình {} đã được thiết lập sẵn"
    configuring = icon.process + " Đang thiết lập cấu hình {}..."
    ipv6_already_disabled = icon.info + " IPv6 đã bị vô hiệu hóa sẵn"
    disabling_ipv6 = icon.process + " Đang vô hiệu hóa IPv6..."
    restoring_configuration = icon.process + " Đang khôi phục thiếp lập {}..."
    stopping_tor = icon.process + " Đang ngưng tiến trình của Tor..."
    starting_tor = icon.process + " Bắt đầu tiến trình Tor mới..."
    changing_tor_circuit = icon.process + " Đang thay đổi mạch Tor..."
    setting_iptables = icon.process + " Đang thiết lập quy tắc cho iptables..."
    flushing_iptables = icon.process + " Đang thiết lập lại iptables về như cũ..."
    checking_ip = icon.process + " Đang kiểm tra địa chỉ IP hiện tại..."
    fixing_dns = icon.process + " Đang sửa vấn đề DNS..."
    your_ip = icon.info + " Địa chỉ {} hiện tại: "
    checking_tor = icon.process + " Đang kiểm tra kết nối đến mạng Tor..."
    tor_success = icon.success + " Đã kết nối đến mạng Tor"
    tor_failed = icon.error + " Quá trình kết nối đến mạng Tor thất bại"
    tor_disconnected = icon.success + " Đã ngưng kết nối khỏi mạng Tor"
    try_again = icon.question + " Bạn có muốn thử lại không (y/n): "
    restarting_network = icon.process + " Đang khởi động lại NetworkManager..."
    changing_mac = icon.process + " Đang thay đổi địa chỉ MAC hiện tại..."
    mac_changed = icon.success + " Đã thay đổi địa chỉ MAC"
    ifconfig_tip = icon.info + color.BOLD + " Bạn có thể dùng lệnh 'ifconfig' để xem các interface trong máy" + color.END
    id_tip = icon.info + color.BOLD + " Bạn có thể vô https://CountryCode.org để tìm ISO code của từng quốc gia" + color.END
    torghostng_tip = icon.success + color.BOLD + " Bạn có thể chạy TorghostNG với lệnh '{}'"
    dns_tip = icon.info + " Nếu bạn gặp vấn đề với việc phân giải địa chỉ web, dùng '--dns' để sửa"
    interface_error = icon.error + " Không có interface nào tên {}. Thay đổi thất bại"
    
class German(English):
    options = "OPTIONEN"
    downloading = icon.process + "Herunterladen {}..."
    installing = icon.process + " Installieren {}..."
    uninstalling = icon.process + " TorghostNG wird deinstalliert..."
    uninstalled = icon.success + " TorghostNG wurde deinstalliert"
    installed = icon.success + " {} wurde installiert"
    already_installed = icon.info + " {} ist schon installiert"
    description = """TorghostNG 2.0 - Anonymisiere all deinen Internetverkehr druch Tor
neu programmiert ausgehend von TorGhost mit Python 3"""
    root_please = icon.error + " Du must root sein, benutze 'sudo TorghostNG'"
    sorry_windows = icon.error + " Entschuldigung, TorghostNG ist nicht kompatibel mit Windows 😛 Bitte benutze den Tor Browser"
    sorry_some_os = """Entschuldigung, aber du musst Tor und macchanger von dem Quellcode selber installieren :v Ich bin zu faul dafür
Tor: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Sorry BSD user, I'm still trying to find way that TorghostNG can fully support for BSD"
    current_language = icon.info + " The current display language: "
    language_list = icon.info + """ List of languages:
    1. English
    2. Vietnamese
    3. German"""
    choose_your_lang = icon.question + " Ändere deine Sprache (1-3): "
    wanna_change_lang = icon.question + " Willst du deine Sprache ändern? (y/n): "
    wanna_uninstall = icon.question + " Möchtest du Tor Ghost deinstallieren? (y/n): "
    invalid_choice = icon.error + " Falsche auswahl"
    country_id = "ISO Abkürzung des Landes"
    help_help = "Zeige diese hilfe Nachricht und schließen"
    privoxy_help = "Verbinen zum Tor Netzwerk mit Privoxy - Verbessere deine Privatsphäre"
    start_help = "Starte die Verbindung zu Tor"
    stop_help = "Stoppe die Verbindung zu Tor"
    circuit_help = "Erneuere die aktuelle Tor Verbindung"
    id_help = "Verbinde dich mit einem Tor-Ausgang in einem spezifischen Land. Gehe zu CountryCode.org und suche den Land ISO code."
    update_help = "Suche nach neuen Versionen"
    no_delay_help = "Schalte die Verzögerungszeit aus"
    changemac_help = "Ändere deine MAC Adresse zufällig. Benutze 'ifconfig' um Geräteinterfaces anzuzeigen"
    language_help = "Ändere die Anzeigesprache. Englisch ist der Standart"
    language_list_help = "Zeige mögliche Sprachauswahlen"
    checkip_help = "Teste deine aktuelle IPV4 Adresse"
    dns_help = "Benutze diese option um DNS zu reparieren wenn eine Website Adresse nicht aufgelöst werden kann"
    done = color.GREEN+ " Fertig"+color.END
    disable_ipv6_info = icon.info + color.BOLD + " Aus Sicherheitsgründen schaltet TorghostNG IPv6 Verkehr aus, um IPv6 Lecks zu verhindern" + color.END
    iptables_info = icon.info + """ Nicht-Tor Verkehr wird von iptables blockiert.
    Manche Anwendungen werden sich nicht mit dem Internet verbinden können"""
    block_bittorrent = icon.info + """ Um das Tor-Netzwerk nicht unnötig zu belasten, wird BitTorrent Verkehr von iptables blockiert."""
    applying_language = icon.process + " Anzeigesprache wird geändert..."
    checking_update = icon.process + " Prüfen auf neue Versionen von TorghostNG..."
    outofdate = icon.error + " Es gibt neue Versionen von TorghostNG"
    uptodate = icon.success + " Deine Verison von TorghostNG is aktuell"
    wanna_update = icon.question + " Möchtest du TorghostNG aktualisieren? (y/n): "
    updating = icon.process + " TorghostNG wird aktualisiert zur Verison {}..."
    already_configured = icon.info + " {} ist bereits konfiguriert"
    configuring = icon.process + " Konfigurieren von {} ..."
    restoring_configuration = icon.process + " Wiederherstellen der Konfiguration {}..."
    ipv6_already_disabled = icon.info + " IPv6 ist bereits ausgeschaltet"
    disabling_ipv6 = icon.process + " Ausschalten von IPv6..."
    stopping_tor = icon.process + " Tor Dienst wird gestoppt..."
    starting_tor = icon.process + " Tor Dienst wird gestartet..."
    changing_tor_circuit = icon.process + " Änderung des Tor-Pfades..."
    setting_iptables = icon.process + " Einstellen der iptables Regeln..."
    flushing_iptables = icon.process + " Aktualisieren von iptables, zurücksetzen auf Standarteinstellungen..."
    checking_ip = icon.process + " Testen deiner aktuellen IP..."
    fixing_dns = icon.process + " Reparieren deines DNS Problems..."
    your_ip = icon.info + " Deine aktuelle {} Adresse: "
    checking_tor = icon.process + " Testen deiner Tor Verbindung..."
    tor_success = icon.success + " Erfolg! Du bist nun zu Tor verbunden {}"
    tor_failed = icon.error + " Dein Verbindungsprozess zu Tor ist fehlgeschlagen"
    tor_disconnected = icon.success + " Deine Verbindung zu Tor wurde getrennt"
    try_again = icon.question + " Möchtest du es erneut probieren (y/n): "
    restarting_network = icon.process + " Neustarten des NetworkManager..."
    changing_mac = icon.process + " Änderung deiner aktuellen MAC Adresse..."
    mac_changed = icon.success + " Deine Mac Adresse wurde geändert"
    ifconfig_tip = icon.info + color.BOLD + " Du kannst 'ifconfig' benutzen um Netzwerkadapter anzuzeigen" + color.END
    id_tip = icon.info + color.BOLD + " Du kannst zu https://CountryCode.org gehen um Länder ISO codes zu finden" + color.END
    torghostng_tip = icon.info + color.BOLD + " Du kannst TorghostNG mit '{}' starten"
    dns_tip = icon.info + " Wenn du Probleme hast mit DNS, kannst du '--dns' benutzen um das Problem zu lösen"
    interface_error = icon.error + " Es existiert kein Netzwerkadapter namens {}. Änderung fehlgeschlagen"
    
the_banner = color.GREEN + """ _____               _               _   _   _  ____ 
|_   _|__  _ __ __ _| |__   ___  ___| |_| \ | |/ ___|
  | |/ _ \| '__/ _` | '_ \ / _ \/ __| __|  \| | |  _ 
  | | (_) | | | (_| | | | | (_) \__ \ |_| |\  | |_| |
  |_|\___/|_|  \__, |_| |_|\___/|___/\__|_| \_|\____|
               |___/""" + color.END

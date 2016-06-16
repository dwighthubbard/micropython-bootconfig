from network import WLAN, AP_IF, STA_IF
from time import sleep


def connect_to_wifi(wifi_networks, retries=10):
    """
    Connect to a WIFI network
    """
    print('Attempting to connect to', wifi_networks)
    wlan = WLAN(STA_IF)
    wlan.active(True)
    nets = wlan.scan()
    print('Found networks', nets)
    for net in nets:
        retry_count = 0
        for ssid, password in wifi_networks.items():
            netssid = net[0].decode()
            print(netssid, ssid)
            if netssid == ssid:
                print('Network %r found!' % ssid)
                wlan.connect(netssid, password)
                while not wlan.isconnected():
                    sleep(1)
                    retry_count += 1
                    if retry_count > retries:
                        continue
                print('WLAN connection to %r succeeded!' % ssid)
                print('Network Configuration: %s %s %s %s' % wlan.ifconfig())
                return True


def enable_ap_mode(essid=None, password=None):
    from network import AP_IF, AUTH_WPA_WPA2_PSK, WLAN
    from ubinascii import hexlify

    wifi_interface = WLAN(AP_IF)
        
    if not essid:
        essid = b"micropython-esp8266-%s" % hexlify(wifi_interface.config("mac")[-3:])
    if not password:
        password = b'MicropyBootConfig'

    print("Setting up wifi network", essid, "using password", password)
    wifi_interface.config(essid=essid, authmode=AUTH_WPA_WPA2_PSK, password=password)

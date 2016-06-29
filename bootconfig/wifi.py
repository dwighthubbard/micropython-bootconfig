from network import WLAN, AP_IF, STA_IF
from time import sleep


def connect_to_wifi(ssid, password, retries=10):
    """
    Connect to a WIFI network
    """
    wlan = WLAN(STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    retry_count = 0
    while not wlan.isconnected():
        sleep(1)
        retry_count += 1
        if retry_count > retries:
            return False
    return True


def enable_ap_mode(essid=None, password=None):
    from network import AP_IF, AUTH_WPA_WPA2_PSK, WLAN
    from ubinascii import hexlify

    wifi_interface = WLAN(AP_IF)
        
    if not essid:
        essid = b"micropython-esp8266-%s" % hexlify(wifi_interface.config("mac")[-3:])
    if not password:
        password = b'MicropyBootConfig'

    wifi_interface.config(essid=essid, authmode=AUTH_WPA_WPA2_PSK, password=password)
    del hexlify

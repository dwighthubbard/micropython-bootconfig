"""
Module to configure a micropython device
"""
import gc


def configure_device():
    from .config import get
    ssid = get('wifi_ssid')
    password = get('wifi_password')
    if not ssid:
        return

    from .wifi import connect_to_wifi
    return connect_to_wifi(ssid, password)


def header(text):
    hline = '*' * 80
    print(hline)
    print(text)
    print(hline)


def configuration():
    if not configure_device():
        header("This device is not configured, going into configuration mode")
        from .wifi import enable_ap_mode
        from .configserver import read_config_from_network
        enable_ap_mode()
        read_config_from_network()
    gc.collect()

"""
Module to configure a micropython device
"""
__version__ = '0.0.1'
__copyright__ = "Copyright 2016 Dwight Hubbard"

try:
    import ujson as json
except:
    import json


def get_value(s):
    length = s.readline().strip()
    if not length:
        return
    length = int(length)
    value = s.read(int(length))
    s.read(2)
    return value


def get_key_value(s):
    value = get_value(s).split(b'=', 1)
    return value


def read_config_from_network():
    try:
        import usocket as socket
    except:
        import socket

    print("Waiting for configuration from the network")
    config = {}
    s = socket.socket()
    address_info = socket.getaddrinfo("0.0.0.0", 8266)
    addr = address_info[0][4]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)


    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        while True:
            value = get_value(client_s)
            if not value:
                break
            value = value.split(b'=', 1)
            print(value)
            config[value[0].decode()] = value[1].decode()

        print(config)
        with open('device_config.json', 'wb') as file_handle:
            file_handle.write(json.dumps(config))
        break

        client_s.send(bytes("OK\r\n", "ascii"))
        client_s.close()

    import machine
    try:
        machine.reset()
    except:
        pass


def configure_device():
    import os
    from .wifi import connect_to_wifi

    try:
        with open('device_config.json') as f:
            config = json.loads(f.read())
            print('Configuring device with configuration', config)
            if connect_to_wifi({config['wifi_ssid']: config['wifi_password']}):
                del config
                return True
    except OSError:
        del connect_to_wifi
        return


def header(text):
    hline = '*' * 80
    print(hline)
    print(text)
    print(hline)


def configuration():
    if not configure_device():
        from .wifi import enable_ap_mode
        header("This device is not configured, going into configuration mode")
        enable_ap_mode()
        read_config_from_network()

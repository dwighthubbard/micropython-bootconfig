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
        from .config import save
        save(config)
        break

        client_s.send(bytes("OK\r\n", "ascii"))
        client_s.close()

    import machine
    try:
        machine.reset()
    except:
        pass



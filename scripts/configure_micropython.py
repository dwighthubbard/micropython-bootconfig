#!/usr/bin/env python
import argparse
import socket


def send_key_value(socket, key, value):
    key_value = key + '=' + value
    key_value = key_value.encode('ascii')
    socket.send('%d\r\n' % len(key_value))
    socket.send(key_value + '\r\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    wifi_group = parser.add_argument_group()
    wifi_group.add_argument('--ssid', help="The wifi network to connect to")
    wifi_group.add_argument('--wifi_passphrase', help='The passphrase/password for the wifi network')
    args = parser.parse_args()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.4.1', 8266))
    send_key_value(client_socket, 'wifi_ssid', args.ssid)
    send_key_value(client_socket, 'wifi_password', args.wifi_passphrase)
    client_socket.close()

import os
from machine import UART


def enable_expansion_usb_uart():
    uart = UART(0, 115200)
    os.dupterm(uart)

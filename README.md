# micropython-bootconfig

Various functionality to configure micropython boards

# Configuring start/stop on boot

## Running at start

In the repl the following commands will make bootconfig to start automatically from main.py.

    >>> from bootconfig.service import autostart
    >>> autostart()

## Disabling autostart

In the repl the following commands will prevent bootconfig from starting automatically.

    >>> from bootconfig.service import disable_autostart
    >>> disable_autostart()


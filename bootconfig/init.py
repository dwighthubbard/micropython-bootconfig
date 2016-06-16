boot_operations = {
    'webrepl': b"""import webrepl
webrepl.start()
"""
}

def create_boot_py(boot_operation=None):
    with open("/boot.py", "w") as f:
        f.write(b'# This file is executed on every boot (including wake-boot from deepsleep)\n\n')
        f.write(b'from bootconfig.device import configuration\n')
        f.write(b'configuration()\n\n')
        if boot_operation:
            f.write(boot_operations[boot_operation])

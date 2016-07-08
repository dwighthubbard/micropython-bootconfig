boot_operations = {
    'cloudclient': b"""import redis_cloudclient
redis_cloudclient.start()
""",
    'webrepl': b"""import webrepl
webrepl.start()
"""
}

def create_boot_py(boot_operations=None):
    with open("/boot.py", "w") as f:
        f.write(b'# This file is executed on every boot (including wake-boot from deepsleep)\n\n')
        f.write(b'from bootconfig.device import configuration\n')
        f.write(b'configuration()\n')
        f.write(b'del configuration\n')

        if boot_operations:
            for boot_operation in boot_operations:
                f.write(boot_operations[boot_operation])

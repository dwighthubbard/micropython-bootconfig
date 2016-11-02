import os


def autostart():
    """
    Add startup code to main.py
    """
    code = """
# Added by bootconfig
from bootconfig.device import configuration
configuration()
# End bootconfig
"""
    with open('main.py', 'a') as fh:
        fh.write(code)


def disable_autostart():
    """
    Remove the startup code from main.py
    """
    changed = False
    with open('main.py') as orig_fh:
        with open('main.py.bootconfig', 'w') as new_fh:
            in_code_section = False
            for line in orig_fh.readlines():
                if line.startswith('# Added by bootconfig'):
                    in_code_section = True
                    continue
                if in_code_section:
                    if line.startswith('# End bootconfig'):
                        in_code_section = False
                        changed = True
                        continue
                new_fh.write(line)
    if changed:
        os.remove('main.py')
        os.rename('main.py.bootconfig', 'main.py')
"""
Configuration file management functions
"""
try:
    import ujson as json
except ImportError:
    import json
try:
    import uos as os
except ImportError:
    import os


def load(config_file=None):
    """
    Get the configuration values from the config file as a Python dictionary

    Parameters
    ----------
    config_file : str, optional
        The configuration file to load, defaults to 'etc/device_config.json'

    Returns
    -------
    dict
        A dictionary of the configuration settings, the dict with be empty if there is no configuration file
    """
    if not config_file:
        config_file = 'etc/device_config.json'
    try:
        with open(config_file) as f:
            return json.loads(f.read())
    except OSError:
        pass
    return {}


def save(values, config_file=None):
    """
    Save the current configuration dictionary to the configuration file

    Parameters
    ----------
    values : dict
        The settings dictionary to save

    config_file : str, optional
        The configuration file to load, defaults to 'etc/device_config.json'
    """
    if not config_file:
        config_file = 'etc/device_config.json'

    try:
        os.mkdir('etc')
    except OSError:
        pass

    with open(config_file, 'wb') as f:
        f.write(json.dumps(values))


def get(key, config_file=None):
    """
    Get a configuration value

    Parameters
    ----------
    key : str
        The key to fetch

    config_file : str, optional
        The configuration file to get the settings from, defaults to 'etc/device_config.json'

    Returns
    -------
    bytes
        The return value as a bytestream or None if there is no such configuration setting
    """
    return load(config_file=config_file).get(key, None)


def set(key, value, config_file=None):
    """
    Get a configuration value

    Parameters
    ----------
    key : str
        The key to fetch

    value : str
        The value to store

    config_file : str, optional
        The configuration file to get the settings from, defaults to 'etc/device_config.json'

    Returns
    -------
    bytes
        The return value as a bytestream or None if there is no such configuration setting
    """
    values = load(config_file=config_file)
    values[key] = value
    save(values, config_file=config_file)


def list_settings(config_file=None):
    settings = load(config_file=config_file)
    keys = settings.keys()
    keys.sort()
    for key in keys:
        print('%s=%s' % (key, settings[key]))

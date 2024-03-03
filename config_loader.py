import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read(r"<PATH TO CONFIG.INI FILE>")  # Update the path accordingly
    return config

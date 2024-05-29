import json

CONFIG_FILE = 'db_config.json'

def carregar_configuracao():
    try:
        with open(CONFIG_FILE, 'r') as config_file:
            return json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "host": "",
            "port": "",
            "database": "",
            "user": "",
            "password": ""
        }

def salvar_configuracao(config):
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file)

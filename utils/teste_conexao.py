from peewee import MySQLDatabase, OperationalError

def testar_conexao(config):
    try:
        db = MySQLDatabase(
            config['database'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port=int(config['port'])
        )
        db.connect()
        db.close()
        return True
    except OperationalError:
        return False

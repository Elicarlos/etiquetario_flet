from peewee import *
from datetime import datetime
import json

with open('db_config.json', 'r') as config_file:
    config = json.load(config_file)

# db = SqliteDatabase('etiquetario.db')
db = MySQLDatabase(
    config['database'],
    user = config['user'],
    password = config['password'] ,
    host= config['host'],
    port = int(config['port']),
)

class Base(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = db

class Empresa(Base):
    cnpj = CharField(max_length=20, unique=True)
    razao_social = CharField(max_length=100, unique=True)
    fantasia = CharField(max_length=100, unique=True)
    numero_sif = CharField(max_length=100, unique=True)
    registro_adapi = CharField(max_length=100, unique=True)

class Tipo(Base):
    tipo = CharField(max_length=100, unique=True)

class ItemNutricional(Base):
    tipo = ForeignKeyField(Tipo, backref='tipos', on_delete='SET NULL', null=True)
    codigo = IntegerField(null=True)
    preco = CharField(max_length=100)
    corte = CharField(max_length=100, unique=True)
    codigo_barras = CharField(null=True)
    porcao_embalagem = CharField(null=True)
    porcao = CharField(null=True)
    peso = CharField(max_length=150)
    campo_adicional = CharField(null=True)
    
    valor_energetico_100g = CharField(max_length=100, null=True)
    valor_energetico_porcao = CharField(max_length=100, null=True)
    valor_energetico_vd = CharField(max_length=100, null=True)

    carboidratos_totais_100g = CharField(max_length=100, null=True)
    carboidratos_totais_porcao = CharField(max_length=100, null=True)
    carboidratos_totais_vd = CharField(max_length=100, null=True)

    acucares_totais_100g = CharField(max_length=100, null=True)
    acucares_totais_porcao = CharField(max_length=100, null=True)
    acucares_totais_vd = CharField(max_length=100, null=True)

    acucares_adicionados_100g = CharField(max_length=100, null=True)
    acucares_adicionados_porcao = CharField(max_length=100, null=True)
    acucares_adicionados_vd = CharField(max_length=100, null=True)

    proteinas_100g = CharField(max_length=100, null=True)
    proteinas_porcao = CharField(max_length=100, null=True)
    proteinas_vd = CharField(max_length=100, null=True)

    gorduras_totais_100g = CharField(max_length=100, null=True)
    gorduras_totais_porcao = CharField(max_length=100, null=True)
    gorduras_totais_vd = CharField(max_length=100, null=True)

    gorduras_saturadas_100g = CharField(max_length=100, null=True)
    gorduras_saturadas_porcao = CharField(max_length=100, null=True)
    gorduras_saturadas_vd = CharField(max_length=100, null=True)

    gorduras_trans_100g = CharField(max_length=100, null=True)
    gorduras_trans_porcao = CharField(max_length=100, null=True)
    gorduras_trans_vd = CharField(max_length=100, null=True)

    fibra_alimentar_100g = CharField(max_length=100, null=True)
    fibra_alimentar_porcao = CharField(max_length=100, null=True)
    fibra_alimentar_vd = CharField(max_length=100, null=True)

    sodio_100g = CharField(max_length=100, null=True)
    sodio_porcao = CharField(max_length=100, null=True)
    sodio_vd = CharField(max_length=100, null=True)

    informacoes_adicionais = TextField(null=True)

class Temperatura(Base):
    temperatura = CharField(max_length=250)

# Conectar e criar tabelas
db.connect()
db.create_tables([ItemNutricional, Empresa, Tipo, Temperatura])

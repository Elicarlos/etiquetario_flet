from models import Empresa, Temperatura, Tipo, ItemNutricional, db


class Controller:
    @staticmethod
    def criar_empresa(cnpj, razao_social, fantasia, numero_sif, registro_adapi):
        with db.atomic():
            Empresa.create(
                cnpj=cnpj,
                razao_social=razao_social,
                fantasia=fantasia,
                numero_sif=numero_sif,
                registro_adapi=registro_adapi
            )

    @staticmethod
    def atualizar_empresa(empresa_id, cnpj, razao_social, fantasia, numero_sif, registro_adapi):
        with db.atomic():
            empresa = Empresa.get_by_id(empresa_id)
            empresa.cnpj = cnpj
            empresa.razao_social = razao_social
            empresa.fantasia = fantasia
            empresa.numero_sif = numero_sif
            empresa.registro_adapi = registro_adapi
            empresa.save()

    @staticmethod
    def criar_tipo(tipo):
        try:
            with db.atomic():
                # Certifique-se de substituir 'Tipo' pelo nome da sua classe modelo para tipos
                Tipo.create(tipo=tipo)
            print(f'Tipo "{tipo}" criado com sucesso!')
        except Exception as e:
            print(f'Erro ao criar tipo: {str(e)}')

    @staticmethod
    def salvar_produto(dados_produto):
        # Lógica para salvar o produto, por exemplo, em um banco de dados
        # Certifique-se de implementar essa lógica adequadamente
        print("Salvando produto:", dados_produto)

        try:
            with db.atomic():
                # Criar instância do modelo ItemNutricional
                item_nutricional = ItemNutricional.create(**dados_produto)
                print(f'Produto {item_nutricional.id} salvo com sucesso!')
        except Exception as e:
            print(f'Erro ao salvar produto: {str(e)}')

    @staticmethod
    def salvar_tipo(dados_produto):
        # Lógica para salvar o produto, por exemplo, em um banco de dados
        # Certifique-se de implementar essa lógica adequadamente
        print("Salvando tipo:", dados_produto)

        try:
            with db.atomic():
                # Criar instância do modelo ItemNutricional
                tipo = Tipo.create(**dados_produto)
                print(f'Tipo {tipo.id} salvo com sucesso!')
        except Exception as e:
            print(f'Erro ao salvar tipo: {str(e)}')
            

    @staticmethod
    def obter_empresas():
        
        return Empresa.select()
    
    
    @staticmethod
    def empresas():
        empresa = Empresa.select().dicts()       
        return empresa

    @staticmethod
    def obter_tipos():
        tipos = Tipo.select().dicts()
        return [tipo['tipo'] for tipo in tipos]
    
    @staticmethod
    def obter_tipo():        
        return Tipo.select()
    
    
    @staticmethod
    def salvar_temperatura(dados_produto):
        # Lógica para salvar o produto, por exemplo, em um banco de dados
        # Certifique-se de implementar essa lógica adequadamente
        print("Salvando produto:", dados_produto)

        try:
            with db.atomic():
                # Criar instância do modelo ItemNutricional
                temperatura = Temperatura.create(**dados_produto)
                print(f'Produto {temperatura.id} salvo com sucesso!')
        except Exception as e:
            print(f'Erro ao salvar produto: {str(e)}')

    @staticmethod
    def atualizar_temperatura(item_id, valores_entradas):
        return Temperatura.update(**valores_entradas).where(Temperatura.id == item_id).execute()



    
    @staticmethod
    def obter_temperatura():
        temperatura = Temperatura.select()
        return temperatura
    
    # @staticmethod
    # def obter_temperatura():
    #     temperaturas = Temperatura.select().dicts()
    #     return [temperatura['temperatura'] for temperatura in temperaturas]
    
    
    @staticmethod
    def obter_temperatura_por_id(item_id):
        return Temperatura.get_or_none(id=item_id)
    
    @staticmethod
    def excluir_temperatura(item_id):
        return Temperatura.delete().where(Temperatura.id == item_id).execute()

    @staticmethod
    def obter_itens_nutricionais():
        itens_nutricionais = ItemNutricional.select().dicts()
        # for item in itens_nutricionais:
        #     print(item)
        return list(itens_nutricionais)
    
    @staticmethod
    def obter_item_nutricional():
        return ItemNutricional.select()
    
    @staticmethod
    def obter_tipo_all():
        tipos = Tipo.select().dicts()
        # for item in itens_nutricionais:
        #     print(item)
        return list(tipos)




    @staticmethod
    def obter_item_nutricional_por_id(item_id):
        return ItemNutricional.get_or_none(id=item_id)
    
    @staticmethod
    def obter_tipo_por_id(item_id):
        return Tipo.get_or_none(id=item_id)
    
    @staticmethod
    def atualizar_tipo(item_id, tipo):
        return Tipo.update(tipo=tipo).where(Tipo.id == item_id).execute()


    @staticmethod
    def atualizar_item_nutricional(item_id, valores_entradas):
        return ItemNutricional.update(**valores_entradas).where(ItemNutricional.id == item_id).execute()

    @staticmethod
    def excluir_item_nutricional(item_id):
        return ItemNutricional.delete().where(ItemNutricional.id == item_id).execute()

    @staticmethod
    def excluir_tipo(item_id):
        return Tipo.delete().where(Tipo.id == item_id).execute()
    

    @staticmethod
    def pesquisa(termo_pesquisa):
       
        # Realizar pesquisa no banco de dados usando o Peewee ORM
        resultados = (ItemNutricional
                      .select()
                      .where(
                          (ItemNutricional.codigo_barras == termo_pesquisa) |
                          (ItemNutricional.corte == termo_pesquisa) 
                      )
                      .dicts()).execute()

        return list(resultados)

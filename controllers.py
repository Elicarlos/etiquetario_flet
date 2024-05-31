from models import Empresa, Temperatura, Tipo, ItemNutricional, db


class Controller:
    
    @staticmethod
    def pesquisa(termo_pesquisa):
     
        # Realizar pesquisa no banco de dados usando o Peewee ORM
        resultados = (ItemNutricional
                    .select()
                    .where(
                        (ItemNutricional.codigo == termo_pesquisa) |
                        (ItemNutricional.codigo_barras.contains(termo_pesquisa)) |
                        (ItemNutricional.corte.contains(termo_pesquisa))
                    ))
        
        # Convertendo os resultados para uma lista de objetos ItemNutricional
        lista_resultados = list(resultados)  # 'resultados' já é um iterable de objetos ItemNutricional
        return lista_resultados

    
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
    def salvar_produto(produto_dados):
        try:
            # Obter ou criar o tipo
            tipo_nome = produto_dados.pop('tipo')
            tipo, created = Tipo.get_or_create(tipo=tipo_nome)
            
            # Adicionar o ID do tipo aos dados do produto
            produto_dados['tipo'] = tipo.id
            
            # Criar o item nutricional
            item_nutricional = ItemNutricional.create(**produto_dados)
            print("Produto salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar produto: {e}")
            
            
    @staticmethod
    def salvar_temperatura(dados_produto):
        # Lógica para salvar o produto, por exemplo, em um banco de dados
        # Certifique-se de implementar essa lógica adequadamente
        print("Salvando temperatura:", dados_produto)

        try:
            with db.atomic():
                # Criar instância do modelo ItemNutricional
                temperatura = Temperatura.create(**dados_produto)
                print(f'Tipo {temperatura.id} salvo com sucesso!')
        except Exception as e:
            print(f'Erro ao salvar tipo: {str(e)}')
            
            
   
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
        return list(ItemNutricional.select())
    
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
        try:
            # Verificar e processar o tipo se estiver nos valores de entrada
            if 'tipo' in valores_entradas:
                tipo_nome = valores_entradas.pop('tipo')
                tipo, created = Tipo.get_or_create(tipo=tipo_nome)
                valores_entradas['tipo'] = tipo.id

            # Atualizar o item nutricional
            rows_updated = ItemNutricional.update(**valores_entradas).where(ItemNutricional.id == item_id).execute()
            print(f"{rows_updated} registro(s) atualizado(s) com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")

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
                          (ItemNutricional.codigo == termo_pesquisa) |
                          (ItemNutricional.codigo_barras == termo_pesquisa) |
                          (ItemNutricional.corte == termo_pesquisa) 
                      )
                      .dicts()).execute()

        return list(resultados)

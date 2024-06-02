
import os
import peewee

from models import Empresa, ItemNutricional

# Obtem o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para o novo diretório 'dados_etiquetas'
dados_etiquetas_dir = os.path.join(script_dir, 'dados_etiquetas')

# def criar_etiqueta(id_produto):
def criar_etiqueta(produto_id, fabricacao, vencimento, temperatura, sexo, lote, empresa):   
    produto = ItemNutricional.get(ItemNutricional.id == produto_id)
    sif =  ''
    adapi =  ''
    for emp in empresa:
        sif = emp['numero_sif']
        adapi = emp['registro_adapi']
    

   
    tipo = produto.tipo_id    
    corte = produto.corte  
    porcao_embalagem = produto.porcao_embalagem
    porcao = produto.porcao
    alergico = produto.alergico
    valor_energetico_100g = produto.valor_energetico_100g
    valor_energetico_vd = produto.valor_energetico_vd
    carboidratos_totais_100g = produto.carboidratos_totais_100g
    carboidratos_totais_vd = produto.carboidratos_totais_vd
    acucares_totais_100g = produto.acucares_totais_100g
    acucares_totais_vd = produto.acucares_totais_vd
    acucares_adicionados_100g = produto.acucares_adicionados_100g
    acucares_adicionados_vd = produto.acucares_adicionados_vd
    proteinas_100g = produto.proteinas_100g
    proteinas_vd = produto.proteinas_vd
    gorduras_totais_100g = produto.gorduras_totais_100g
    gorduras_totais_vd = produto.gorduras_totais_vd
    gorduras_saturadas_100g = produto.gorduras_saturadas_100g
    gorduras_saturadas_vd = produto.gorduras_saturadas_vd
    gorduras_trans_100g = produto.gorduras_trans_100g
    gorduras_trans_vd = produto.gorduras_trans_vd
    fibra_alimentar_100g = produto.fibra_alimentar_100g
    fibra_alimentar_vd = produto.fibra_alimentar_vd
    sodio_100g = produto.sodio_100g
    sodio_vd = produto.sodio_vd
    peso = produto.peso
    informacoes_adicionais = produto.informacoes_adicionais

    # Obtem o diretório do script atual
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o diretório 'dados_etiquetas'
    dados_etiquetas_dir = os.path.join(script_dir, 'dados_etiquetas')
   
    # Caminho completo para o arquivo dentro de 'dados_etiquetas'
    arquivo_path = os.path.join(dados_etiquetas_dir, 'dados.prn')

    try:
        with open(arquivo_path, 'r') as arquivo:
            conteudo = arquivo.read()
            conteudo = conteudo.format(
                informacao_nutricional = 'INFORMAÇÃO NUTRICIONAL',
                valor_energetico_kcal = 'Valor energético (Kcal) ',
                carboidratos_totais_g = 'Carboidratos totais (g)',
                porcoes_por_embagalagem = "Porções por embalagens ",
                acucares_totais_g = "Açucares totais (g)",
                acucares_adicionados_g= 'Açúcares Adicionados (g)',
                proteinas_g = 'Proteínas (g)',
                gorduras_totais_g = 'Gorduras totais (g)',
                gorduras_saturadas_g = "Gorduras saturadas (g)",
                gorduras_trans_g = "Gorduras trans (g)",
                fibra_alimentar_g = 'Fibra alimentar (g)',
                sodio_mg = 'Sódio (mg)',
                percentual_diario = '*Percentual de valores diários fornecidos pela porção. ',
                alergicos = 'ALÉRGICOS: ',
                porcao = "Porção: ",
                TIPO = tipo,  
                CORTE = corte,               
                porcao_por_embalagem = porcao_embalagem,
                porcao_var = porcao,
                alergico_label = alergico,
                v_ene_100 = valor_energetico_100g,
                v_ene_vd = valor_energetico_vd,
                c_tot_100 = carboidratos_totais_100g,
                c_tot_vd = carboidratos_totais_vd,
                a_tot_100 = acucares_totais_100g,
                a_tot_vd = acucares_totais_vd,
                a_adi_100 = acucares_adicionados_100g,
                a_adi_vd = acucares_adicionados_vd,
                prot_100 = proteinas_100g,
                prot_vd = proteinas_vd,
                g_tot_100 = gorduras_totais_100g,
                g_tot_vd = gorduras_totais_vd,
                g_sat_100 = gorduras_saturadas_100g,
                g_sat_vd = gorduras_saturadas_vd,
                g_tra_100 = gorduras_trans_100g,
                g_tra_vd= gorduras_trans_vd,
                fibra_100 = fibra_alimentar_100g,
                fibra_vd = fibra_alimentar_vd,
                sodio_100 = sodio_100g,
                sodio_vd = sodio_vd,
                peso = peso,
                fabricacao = fabricacao,
                venc = vencimento,
                lote = lote,
                numero_sif = sif,
            )
            return conteudo
    except FileNotFoundError:
        print(f"O arquivo {'nome_do_arquivo'} não foi encontrado em {dados_etiquetas_dir}.")
        return None
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None

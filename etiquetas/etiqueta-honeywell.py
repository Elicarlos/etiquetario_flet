
import os

from models import Empresa, ItemNutricional

# Obtem o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para o novo diretório 'dados_etiquetas'
dados_etiquetas_dir = os.path.join(script_dir, 'dados_etiquetas')

def criar_etiqueta(id_produto):
    
    produto = ItemNutricional.get(ItemNutricional.id == id_produto)
    empresa  = Empresa.select()

    tipo = produto.tipo_id    
    corte = produto.corte  
    porcao_embalagem = produto.porcao_embalagem
    porcao = produto.porcao
    campo_adicional = produto.campo_adicional
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
    informacoes_adicionais = produto.informacoes_adicionais

    # Obtem o diretório do script atual
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o diretório 'dados_etiquetas'
    dados_etiquetas_dir = os.path.join(script_dir, 'dados_etiquetas')
   
    # Caminho completo para o arquivo dentro de 'dados_etiquetas'
    arquivo_path = os.path.join(dados_etiquetas_dir, 'dados.prn')
    
    peso = 1000
    fabricacao = "20/04/2024"
    vencimento = "21/04/2024"
    lote = 1
    sif = 10

    try:
        with open(arquivo_path, 'r') as arquivo:
            conteudo = arquivo.read()
            conteudo = conteudo.format(
                TIPO = tipo,  
                CORTE = corte,               
                porcao_por_embagalagem = porcao_embalagem,
                porcao_var = porcao,
                campo_adicional = campo_adicional,
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
                venc = '23-04-2024',
                lote = lote,
                numero_sif =sif,
            )
            return conteudo
    except FileNotFoundError:
        print(f"O arquivo {'nome_do_arquivo'} não foi encontrado em {dados_etiquetas_dir}.")
        return None
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None
import os
from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from models import Empresa, ItemNutricional


from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def criar_etiqueta(id_produto):
    produto = ItemNutricional.get(ItemNutricional.id == id_produto)
    empresa  = Empresa.select()

    tipo = produto.tipo_id    
    corte = produto.corte
    sexo = produto.sexo
    codigo_barras = produto.codigo_barras
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
    

    width, height = 800, 600  # Tamanho da etiqueta em pixels
    etiqueta = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(etiqueta)
    
    # Define as fontes
    fonte_titulo = ImageFont.truetype('../assets/arialbd.ttf', 40)
    fonte_texto = ImageFont.truetype('../assets/arialbd.ttf', 30)

    # Desenha o tipo e o corte

    width_text_tipo = draw.textlength(tipo, fonte_titulo)
    height_text_tipo = fonte_titulo.size * len(tipo.splitlines())

    x_tipo = (width - width_text_tipo) // 2
    y_tipo = (height - height_text_tipo) // 2

    width_text_corte = draw.textlength(corte, fonte_titulo)
    height_text_corte = fonte_titulo.size * len(corte.splitlines())

    x_corte = (width - width_text_corte) // 2
    y_corte = y_tipo + height_text_tipo + 20  # Ajustar espaçamento entre os textos

    # Desenhando o texto centralizado
    draw.text((x_tipo, y_tipo), tipo, fill="black", font=fonte_titulo)
    draw.text((x_corte, y_corte), corte, fill="black", font=fonte_titulo)

    # Desenha as informações nutricionais
    draw.text((10, 200), f"Porções por embalagem: {porcao_embalagem}", fill="black", font=fonte_texto)
    draw.text((10, 250), f"Porção: {porcao}", fill="black", font=fonte_texto)
    # Continuar desenhando as outras informações nutricionais...

    # Desenha as informações adicionais
    y_offset = 200
    for line in campo_adicional.split('\n'):
        draw.text((10, y_offset), line, fill="black")
        y_offset += 30  # Ajuste o espaçamento conforme necessário

    # Salva a etiqueta como PNG
    etiqueta.save("etiqueta_pillow.png")

# Exemplo de uso
criar_etiqueta(4)

import os
from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from models import Empresa, ItemNutricional


def calc_posicao_central(pdf,texto, height):  
        # Calcula a posição central do texto
        altura_texto = pdf.stringWidth(texto)
        posicao_y = (height - altura_texto) / 2
        return posicao_y

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

    buffer = BytesIO()
    
    # Registra a fonte Arial no ReportLab
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-bold', 'ARIALBD.ttf'))

    width, height = 105 * mm, 75 * mm

    pdf = canvas.Canvas("etiqyetasss.pdf", pagesize=(width, height))
    pdf.rotate(-90)
    
    posicao_y_tipo = calc_posicao_central(pdf, tipo, height)
    posicao_y_corte = calc_posicao_central(pdf, corte, height)
    
    
    
    x  ,  y = 20 * mm, 5 * mm
    
   
    
    # Desenhando o texto vertical
    pdf.setFont("Arial-bold", 4 * mm)
    pdf.drawString(posicao_y_tipo, -x, tipo)
    
    y2 = -x + 40  # Espaçamento de 200 unidades para baixo
    pdf.translate(y, y2)
    
    pdf.setFont("Arial-bold", 4 * mm)
    pdf.drawString(posicao_y_corte, -x, corte)
    
    
    
    
    pdf.save()
    
    # pdf_content = buffer.getvalue()  # Obtenha o conteúdo do PDF do buffer
    # buffer.close()  # Feche o buffer
    


    # return pdf_content
    
    
# from wand.image import Image
# from io import BytesIO

# def pdf_para_png(pdf_content):
#     with Image(blob=pdf_content, resolution=300) as img:
#         img.compression_quality = 100
#         img.format = 'png'
#         return img.make_blob('png')

# # Exemplo de uso
# pdf_content = criar_etiqueta(4)# Conteúdo do PDF em formato de bytes

# png_content = pdf_para_png(pdf_content)


    

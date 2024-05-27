import os
from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from models import Empresa, ItemNutricional

import os
from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from models import ItemNutricional

def calc_largura_texto(pdf, texto, width):
    # Calcula a posição central do texto
    largura_texto = pdf.stringWidth(texto, 'Arial', 12)
    posicao_x = (width - largura_texto) / 2
    return posicao_x

def criar_etiqueta(id_produto):
    produto = ItemNutricional.get(ItemNutricional.id == id_produto)

    tipo = produto.tipo_id  # Assume que tipo_id é um atributo textual do produto

    buffer = BytesIO()
    
    # Registra a fonte Arial no ReportLab
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    width, height = 210 * mm, 297 * mm  # Tamanho A4 para exemplo

    pdf = canvas.Canvas(buffer, pagesize=(width, height))
    pdf.setTitle("Etiqueta de Produto")

    # Definindo a fonte e tamanho
    pdf.setFont("Arial", 12)  # Define o tamanho da fonte
    pos_x = calc_largura_texto(pdf, tipo, width)
    pdf.drawString(pos_x, height - 50 * mm, tipo)  # Ajuste a posição vertical conforme necessário

    pdf.save()
    buffer.seek(0)    

    pdf_content = buffer.getvalue()  # Obtenha o conteúdo do PDF do buffer

    return pdf_content

    


#     with open(filename, 'wb') as f:
#         f.write(buffer.getvalue())
#         buffer.close()

#     return filename

# filename = "eli.pdf"   
# criar_etiqueta(4, filename)
    
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


    

import os
from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from src.models import Empresa, ItemNutricional


def calc_largura_texto(pdf,texto, width):  
        # Calcula a posição central do texto
        largura_texto = pdf.stringWidth(texto)
        posicao_x = (width - largura_texto) / 2
        return posicao_x

def criar_etiqueta(id_produto, filename):
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

    width, height = 75 * mm, 105 * mm

    pdf = canvas.Canvas(buffer, pagesize=(width, height))
    
    pdf.setTitle("Meu Pdf")
    linha_espacamento = 10 * mm   
    
    pdf.setFont("Arial-bold", 3 * mm)
    pdf.drawString(calc_largura_texto(pdf,tipo, width), 100 * mm, tipo)
    pdf.setFont("Arial-bold", 3 * mm)
    pdf.drawString(calc_largura_texto(pdf,corte, width), 95 * mm, corte)
    
   
    

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 76 * mm, width - 10 * mm, 76 * mm)

    pdf.setFont("Arial-bold", 3 * mm)
    pdf.drawCentredString(width / 2, 73.5 * mm, 'INFORMAÇÃO NUTRICIONAL')

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 73 * mm, width - 10 * mm, 73 * mm)

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 70 * mm, width - 10 * mm, 70 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 67.5 * mm, 'Porções por embalagem:')
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(38 * mm, 67.5 * mm, str(porcao_embalagem))
    
    
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 65 * mm,  'Porção:')
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(19.5 * mm, 65 * mm, str(porcao))
    
    

    pdf.setLineWidth(0.75)
    pdf.line(10 * mm, 64 * mm, width - 10 * mm, 64 * mm)

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 60 * mm, width - 10 * mm, 60 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 57.5 * mm, "Valor energético (kcal)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 57 * mm, width - 10 * mm, 57 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 54.5 * mm, "Carboidratos totais (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 54 * mm, width - 10 * mm, 54 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 51.5 * mm, "Açúcares totais (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 51 * mm, width - 10 * mm, 51 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 48.5 * mm, "Açúcares adicionados (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 48 * mm, width - 10 * mm, 48 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 45.5 * mm, "Proteínas (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 45 * mm, width - 10 * mm, 45 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 42.5 * mm, "Gorduras totais (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 42 * mm, width - 10 * mm, 42 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 39.5 * mm, "Gorduras saturadas (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 39 * mm, width - 10 * mm, 39 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 36.5 * mm, "Gorduras trans. (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 36 * mm, width - 10 * mm, 36 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 33.5 * mm, "Fibra alimentar (g)")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 33 * mm, width - 10 * mm, 33 * mm)

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 30.5 * mm, "Sódio (mg)")

    pdf.setLineWidth(0.35 * mm)
    pdf.line(10 * mm, 30 * mm, width - 10 * mm, 30 * mm)

    pdf.setFont("Arial", 2 * mm)
    pdf.drawString(10 * mm, 27.5 * mm, "*Percentual de valores diários fornecidos pela porção.")

    pdf.setLineWidth(0.1)
    pdf.line(10 * mm, 27 * mm, width - 10 * mm, 27 * mm)

    pdf.setLineWidth(0.1)
    pdf.line(40 * mm, 64 * mm, 40 * mm, 30 * mm)

    pdf.setFont("Arial-bold", 2.60 * mm)
    pdf.drawString(43 * mm, 61 * mm, "100 g")
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 57.5 * mm, str(valor_energetico_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 54.5 * mm, str(carboidratos_totais_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 51.5 * mm, str(acucares_totais_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 48.5 * mm, str(acucares_adicionados_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 45.5 * mm, str(proteinas_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 42.5 * mm, str(gorduras_totais_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 39.5 * mm, str(gorduras_saturadas_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 36.5 * mm, str(gorduras_trans_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 33.5 * mm, str(fibra_alimentar_100g))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(43 * mm, 30.5 * mm, str(sodio_100g))
    

    pdf.setLineWidth(0.1)
    pdf.line(53 * mm, 64 * mm, 53 * mm, 30 * mm)

    pdf.setFont("Arial-bold", 2.60 * mm)
    pdf.drawString(56 * mm, 61 * mm, "% VD*")
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 57.5 * mm, str(valor_energetico_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 54.5 * mm, str(carboidratos_totais_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 51.5 * mm, str(acucares_totais_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 48.5 * mm, str(acucares_adicionados_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 45.5 * mm, str(proteinas_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 42.5 * mm, str(gorduras_totais_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 39.5 * mm, str(gorduras_saturadas_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 36.5 * mm, str(gorduras_trans_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 33.5 * mm, str(fibra_alimentar_vd))
    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(56 * mm, 30.5 * mm, str(sodio_vd))
    

    pdf.setFont("Arial-bold", 2.30 * mm)
    pdf.drawString(10 * mm, 23 * mm, "ALÉRGICOS:")
    
    campo_adicional = str(campo_adicional)
    largura_maxima = 42 * mm  # Largura máxima permitida para o texto

    fonte = "Arial-bold"
    tamanho_fonte = 2.25 * mm  # Tamanho da fonte em mm

    # Calcula a largura do texto
    largura_texto = pdf.stringWidth(campo_adicional, fonte, tamanho_fonte)

    if largura_texto > largura_maxima:
        # Se o texto for maior que a largura máxima, quebra em várias linhas
        palavras = campo_adicional.split()
        linhas = []
        linha_atual = ""
        for palavra in palavras:
            if pdf.stringWidth(linha_atual + " " + palavra, fonte, tamanho_fonte) <= largura_maxima:
                linha_atual += " " + palavra
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra
        linhas.append(linha_atual.strip())

        # Desenha as linhas de texto
        y = 23 * mm
        for linha in linhas:
            pdf.setFont(fonte, tamanho_fonte)  # Define a fonte e tamanho
            pdf.drawString(25 * mm, y, linha)
            y -=  3* mm  # Espaçamento entre linhas
    else:
        # Desenha o texto em uma única linha
        pdf.setFont(fonte, tamanho_fonte)  # Define a fonte e tamanho
        pdf.drawString(25 * mm, 23 * mm, campo_adicional)

    # pdf.showPage()
    
    pdf.save()
    
    # pdf_content = buffer.getvalue()  # Obtenha o conteúdo do PDF do buffer
    # buffer.close()  # Feche o buffer
    


    with open(filename, 'wb') as f:
        f.write(buffer.getvalue())
        buffer.close()

    return filename

filename = "eli.pdf"   
criar_etiqueta(4, filename)
    
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


    

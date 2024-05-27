from io import BytesIO
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

try:
    # Conexão com o banco de dados e modelos
    from models import Empresa, ItemNutricional
except ImportError:
    print("Erro ao importar os modelos de banco de dados. Verifique se estão corretamente definidos.")

def calc_largura_texto(pdf, texto, fonte, tamanho_fonte, width):
    # Calcula a posição central do texto
    largura_texto = pdf.stringWidth(texto, fonte, tamanho_fonte)
    posicao_x = (width - largura_texto) / 2
    return posicao_x

def criar_etiqueta(id_produto):
    try:
        produto = ItemNutricional.get(ItemNutricional.id == id_produto)
    except Exception as e:
        print("Erro ao acessar o banco de dados:", e)
        return None

    buffer = BytesIO()
    
    try:
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-bold', 'ARIALBD.ttf'))
    except Exception as e:
        print("Erro ao carregar fontes:", e)
        return None

    width, height = 105 * mm, 75 * mm

    pdf = canvas.Canvas(buffer, pagesize=(width, height))
    pdf.setTitle("Etiqueta Nutricional")

    # Rotação para texto vertical
    pdf.saveState()
    pdf.translate(10 * mm, height - 10 * mm)
    pdf.rotate(90)

    # Texto vertical
    pdf.setFont("Arial-bold", 3 * mm)
    pdf.drawString(calc_largura_texto(pdf, produto.tipo_id, "Arial-bold", 3 * mm, height), 0, produto.tipo_id)

    pdf.restoreState()

    # Outras informações
    pdf.setFont("Arial-bold", 3 * mm)
    y = 60 * mm
    infos = [
        f'Porções por embalagem: {produto.porcao_embalagem}',
        f'Porção: {produto.porcao} g',
        f'Valor Energético: {produto.valor_energetico_100g} kcal',
        f'Carboidratos: {produto.carboidratos_totais_100g} g',
        f'Proteínas: {produto.proteinas_100g} g',
        f'Gorduras Totais: {produto.gorduras_totais_100g} g',
        f'Sódio: {produto.sodio_100g} mg'
    ]
    for info in infos:
        pdf.drawString(10 * mm, y, info)
        y -= 5 * mm

    pdf.showPage()
    pdf.save()

    pdf_content = buffer.getvalue()
    buffer.close()
    return pdf_content

# Exemplo de chamada da função
# pdf_content = criar_etiqueta(1)  # Substitua 1 pelo ID do produto

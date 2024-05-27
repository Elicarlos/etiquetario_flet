from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def criar_tabela(pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Configurações de fonte
    c.setFont("Helvetica", 10)

    # Dados da tabela
    dados_tabela = [     
        ["", " 100 g ", "% VD* "],      
        ["Valor energético (kcal)", "", ""],
        ["Carboidratos totais (g)", "", ""],
        ["Açúcares totais (g)", "", ""],
        ["Açúcares adicionados (g)", "", ""],
        ["Proteínas (g)", "", ""],
        ["Gorduras totais (g)", "", ""],
        ["Gorduras saturadas (g)", "", ""],
        ["Gorduras trans (g)", "", ""],
        ["Fibra alimentar (g)", "", ""],
        ["Sódio (mg)", "", ""]
    ]

    # Configurações da tabela
    largura_coluna_0 = 150  # Largura da coluna 0 ("")
    largura_coluna_1 = 60   # Largura da coluna 1 ("100 g")
    largura_coluna_2 = 60   # Largura da coluna 2 ("% VD*")
    altura_linha = 20
    altura_cabecalho = 4
    margem_esquerda = 50
    margem_inferior = 50

    # Desenhar retângulo acima da tabela
    retangulo_superior_x = margem_esquerda
    retangulo_superior_y = margem_inferior + altura_linha * len(dados_tabela) + 3
    retangulo_superior_largura = largura_coluna_0 + largura_coluna_1 + largura_coluna_2
    retangulo_superior_altura = 30
    c.rect(retangulo_superior_x, retangulo_superior_y, retangulo_superior_largura, retangulo_superior_altura)

    # Desenhar linha inferior mais grossa
    c.setLineWidth(5)
    c.line(retangulo_superior_x, retangulo_superior_y, retangulo_superior_x + retangulo_superior_largura, retangulo_superior_y)
    c.setLineWidth(1)  # Restaura a espessura da linha para o padrão



    # Desenhar segundo retângulo em cima do primeiro
    segundo_retangulo_x = margem_esquerda
    segundo_retangulo_y = margem_inferior + altura_linha * len(dados_tabela) + 33
    segundo_retangulo_largura = largura_coluna_0 + largura_coluna_1 + largura_coluna_2
    segundo_retangulo_altura = 20
    c.rect(segundo_retangulo_x, segundo_retangulo_y, segundo_retangulo_largura, segundo_retangulo_altura)

    # Desenhar retângulo no final
    retangulo_final_x = margem_esquerda
    retangulo_final_y = margem_inferior - 20
    retangulo_final_largura = largura_coluna_0 + largura_coluna_1 + largura_coluna_2
    retangulo_final_altura = 20
    c.rect(retangulo_final_x, retangulo_final_y, retangulo_final_largura, retangulo_final_altura)

    # Desenhar retângulo para informações alérgicas
    retangulo_alergicos_x = margem_esquerda
    retangulo_alergicos_y = retangulo_final_y - 30
    retangulo_alergicos_largura = largura_coluna_0 + largura_coluna_1 + largura_coluna_2
    retangulo_alergicos_altura = 30
    c.rect(retangulo_alergicos_x, retangulo_alergicos_y, retangulo_alergicos_largura, retangulo_alergicos_altura)

    # Desenhar contorno da tabela
    c.rect(margem_esquerda, margem_inferior, largura_coluna_0 + largura_coluna_1 + largura_coluna_2, altura_cabecalho + altura_linha * len(dados_tabela))

    # Desenhar linhas horizontais com numeração
    for i, linha in enumerate(dados_tabela, 0):  # Começa a partir da linha 1 para evitar a linha superior vazia
        y = margem_inferior + i * altura_linha
        c.line(margem_esquerda, y, margem_esquerda + largura_coluna_0 + largura_coluna_1 + largura_coluna_2, y)
        # c.drawString(margem_esquerda - 30, y - 10, str(i))  # Adiciona a numeração ao lado da linha

    # Desenhar linhas verticais
    c.line(margem_esquerda + largura_coluna_0, margem_inferior, margem_esquerda + largura_coluna_0, margem_inferior + altura_cabecalho + altura_linha * len(dados_tabela))
    c.line(margem_esquerda + largura_coluna_0 + largura_coluna_1, margem_inferior, margem_esquerda + largura_coluna_0 + largura_coluna_1, margem_inferior + altura_cabecalho + altura_linha * len(dados_tabela))

    # Adicionar parágrafos dentro do primeiro retângulo
    retangulo_x = margem_esquerda + 5
    retangulo_y = margem_inferior + altura_linha * len(dados_tabela) + 20  # Ajuste a posição vertical conforme necessário
    c.setFont("Helvetica", 8)
    c.drawString(retangulo_x, retangulo_y, "Porções por embalagem: cerca de 5 porções")
    c.drawString(retangulo_x, retangulo_y - 10, "Porção: 100 g (2 pedaços)")

    # Adicionar parágrafos dentro do segundo retângulo (em negrito e centralizado verticalmente)
    segundo_retangulo_x = margem_esquerda + 5
    segundo_retangulo_y = margem_inferior + altura_linha * len(dados_tabela) + 33 + (segundo_retangulo_altura / 2)  # Ajuste a posição vertical conforme necessário
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(segundo_retangulo_x + (segundo_retangulo_largura / 2), segundo_retangulo_y, "INFORMAÇÃO NUTRICIONAL")

    # Adicionar parágrafo no retângulo final
    retangulo_final_x = margem_esquerda + 5
    retangulo_final_y = retangulo_final_y + 5  # Ajuste a posição vertical conforme necessário
    c.setFont("Helvetica", 8)
    c.drawString(retangulo_final_x, retangulo_final_y, "*Percentual de valores diários fornecidos pela porção.")

    # Adicionar parágrafos no retângulo de informações alérgicas
    retangulo_alergicos_x = margem_esquerda + 5
    retangulo_alergicos_y = retangulo_alergicos_y + 5  # Ajuste a posição vertical conforme necessário

    # Calcular a altura total ocupada pelos textos no retângulo de informações alérgicas
    altura_texto_alergicos = 2 * 10  # 2 linhas de texto com tamanho de fonte 10

    # Ajustar a posição vertical do texto para que ele fique centralizado no retângulo
    y_texto_alergicos = retangulo_alergicos_y + (retangulo_alergicos_altura - altura_texto_alergicos) / 2

    # Adicionar parágrafos no retângulo de informações alérgicas (em negrito e alinhado à esquerda)
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(retangulo_alergicos_x, y_texto_alergicos + 10, "ALÉRGICOS: PODE CONTER LÁTEX NATURAL.")
    c.drawString(retangulo_alergicos_x, y_texto_alergicos, "NÃO CONTÉM GLÚTEN.")


    # Preencher os dados na tabela
    for i, linha in enumerate(dados_tabela):
        for j, dado in enumerate(linha):
            largura_coluna = [largura_coluna_0, largura_coluna_1, largura_coluna_2][j]
            x = margem_esquerda + sum((largura_coluna_0, largura_coluna_1, largura_coluna_2)[:j])
            y = margem_inferior + (len(dados_tabela) - i) * altura_linha
            c.drawString(x + 5, y - 15, dado)

    c.save()

# Exemplo de uso
pdf_path = "tabela_reportlab_modificada.pdf"
criar_tabela(pdf_path)


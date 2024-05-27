from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class TabelaPDF:
    def __init__(self, pdf_path, dados_tabela, larguras_colunas, altura_linha, altura_cabecalho, margem_esquerda, margem_inferior):
        self.pdf_path = pdf_path
        self.dados_tabela = dados_tabela
        self.larguras_colunas = larguras_colunas
        self.altura_linha = altura_linha
        self.altura_cabecalho = altura_cabecalho
        self.margem_esquerda = margem_esquerda
        self.margem_inferior = margem_inferior

    def criar_tabela(self):
        c = canvas.Canvas(self.pdf_path, pagesize=letter)

        # Configurações de fonte
        c.setFont("Helvetica", 10)

        # Desenhar contorno da tabela
        c.rect(
            self.margem_esquerda,
            self.margem_inferior,
            sum(self.larguras_colunas),
            self.altura_cabecalho + self.altura_linha * len(self.dados_tabela)
        )

        # Desenhar linhas horizontais
        for i in range(len(self.dados_tabela) + 1):
            y = self.margem_inferior + i * self.altura_linha
            c.line(self.margem_esquerda, y, self.margem_esquerda + sum(self.larguras_colunas), y)

        # Desenhar linhas verticais
        x_atual = self.margem_esquerda
        for largura_coluna in self.larguras_colunas[:-1]:
            x_atual += largura_coluna
            c.line(x_atual, self.margem_inferior, x_atual, self.margem_inferior + self.altura_cabecalho + self.altura_linha * len(self.dados_tabela))

        # Preencher os dados na tabela
        for i, linha in enumerate(self.dados_tabela):
            for j, dado in enumerate(linha):
                largura_coluna = self.larguras_colunas[j]
                x = self.margem_esquerda + sum(self.larguras_colunas[:j])
                y = self.margem_inferior + (len(self.dados_tabela) - i) * self.altura_linha
                c.drawString(x + 5, y - 15, dado)

        c.save()

# Exemplo de uso
dados_tabela_exemplo = [
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

larguras_colunas_exemplo = [150, 60, 60]
altura_linha_exemplo = 20
altura_cabecalho_exemplo = 30
margem_esquerda_exemplo = 50
margem_inferior_exemplo = 50

pdf_path_exemplo = "tabela_reportlab_modificada.pdf"

tabela_pdf = TabelaPDF(
    pdf_path_exemplo,
    dados_tabela_exemplo,
    larguras_colunas_exemplo,
    altura_linha_exemplo,
    altura_cabecalho_exemplo,
    margem_esquerda_exemplo,
    margem_inferior_exemplo
)

tabela_pdf.criar_tabela()

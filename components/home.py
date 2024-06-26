import importlib.util
import flet as ft
from controllers import Controller
import os
from pathlib import Path
import win32print
from models import Empresa

from utils.notifications import exibir_mensagem_erro, exibir_mensagem_sucesso, exibir_messagem_delete

def home(page: ft.Page):
    controller = Controller()
    
    itens_por_pagina = 5
    pagina_atual = 1
    
    


    
    
 
 
    def limpar_campos():
        codigo_field.value = ""
        corte_field.value = ""
        preco_field.value = ""
        tipo_carne_dropdown.value = None
        codigo_barras_field.value = ""
        porcao_embalagem_field.value = ""
        porcao_field.value = ""
        alergico_field.value = ""
        peso_field.value = ""
        informacao_adicional_field.value = ""
        valor_energico_field_100.value = ""
        valor_energico_field_0.value = ""
        valor_energico_field_vd.value = ""
        carboidratos_totais_field_100.value = ""
        carboidratos_totais_field_0.value = ""
        carboidratos_totais_field_vd.value = ""
        acucares_totais_field_100.value = ""
        acucares_totais_field_0.value = ""
        acucares_totais_field_vd.value = ""
        acucares_adicionados_field_100.value = ""
        acucares_adicionados_field_0.value = ""
        acucares_adicionados_field_vd.value = ""
        proteinas_field_100.value = ""
        proteinas_field_0.value = ""
        proteinas_field_vd.value = ""
        gorduras_totais_field_100.value = ""
        gorduras_totais_field_0.value = ""
        gorduras_totais_field_vd.value = ""
        gorduras_saturadas_field_100.value = ""
        gorduras_saturadas_field_0.value = ""
        gorduras_saturadas_field_vd.value = ""
        gorduras_trans_field_100.value = ""
        gorduras_trans_field_0.value = ""
        gorduras_trans_field_vd.value = ""
        fibra_field_100.value = ""
        fibra_field_0.value = ""
        fibra_field_vd.value = ""
        sodio_field_100.value = ""
        sodio_field_0.value = ""
        sodio_field_vd.value = ""
        page.update()
        
    def create_text_field(hint_text=None,label=None, width=None, expand=False, multiline=False, height=None):
        return ft.TextField(
            hint_text=None,
            label=label,
            width=width,
            expand=expand,
            multiline=multiline,
            height=height,
            border_radius=ft.border_radius.all(2),
            bgcolor=ft.colors.WHITE,
            color=ft.colors.GREY_900,
            hover_color=ft.colors.WHITE,
            border_color=ft.colors.GREY_300,
            border_width=1
        )
        
    def create_small_text_field(width=100):
        return ft.TextField(
            width=width,
            expand=True,
            border_radius=ft.border_radius.all(2),
            bgcolor=ft.colors.GREY_100,
            color=ft.colors.BLUE,
            hover_color=ft.colors.GREY_100,
            border_width=1,
            height=35,
            content_padding=ft.padding.all(10),
        )
    
    
    
    def obter_total_produtos():
        return len(controller.obter_item_nutricional())  # Supondo que temos uma função para obter o número total de produtos
    
    total_produtos = obter_total_produtos()    
    
    def carregar_etiquetas():
        p = Path(__file__).parent
        diretorio_etiquetas = p / '../etiquetas'
        etiquetas_disponiveis = []
        if diretorio_etiquetas.exists():
            etiquetas = [f for f in os.listdir(diretorio_etiquetas) if f.endswith('.py') and f != '__init__.py']
            etiquetas_disponiveis = [f[:1000] for f in etiquetas]
            
        else:
            print('Sem diretorio de etiquetas')
        
        return etiquetas_disponiveis
    
    def atualizar_dropdown_lote(selecionar_ultimo=False):
        lotes = controller.obter_lote()  
        lote_dropdown.options = [ft.dropdown.Option(lote.lote) for lote in lotes]
        if selecionar_ultimo and lotes:
            lote_dropdown.value = lotes[-1].lote 
        else:
            lote_dropdown.value = None  
        lote_dropdown.update() 
        
        
    def obter_impressoras():
            impressoras = []
            for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
                impressoras.append(printer[2])
            return impressoras
        
    def criar_etiqueta(produto_id, fabricacao, vencimento, temperatura, etiqueta_selecionada, impressora, quantidade, sexo, lote, empresa):
        path_etiqueta = Path(__file__).parent / '../etiquetas' / f'{etiqueta_selecionada}'
        
        if path_etiqueta.exists():
            print('Etiqueta Existe dentro do método')
            spec = importlib.util.spec_from_file_location(etiqueta_selecionada, path_etiqueta)
            etiqueta_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(etiqueta_module)
            return etiqueta_module.criar_etiqueta(produto_id, fabricacao, vencimento, temperatura, sexo, lote, empresa)
        
        else:
            print(f"Arquivo de etiqueta {etiqueta_selecionada}.py nao encontrada")
            
    
    # def imprimir_etiqueta(conteudo, impressora, quantidade):       
 
    #     if impressora is None:
    #         impressora = win32print.GetDefaultPrinter()
        
    #     handle_impressora = win32print.OpenPrinter(impressora)
    #     try:
    #         conteudo_bytes = conteudo.encode('utf-8')
    #         job = win32print.StartDocPrinter(handle_impressora, 1, ("Impressão de Etiqueta", None, "RAW"))
    #         for _ in range(quantidade):
    #             win32print.StartPagePrinter(handle_impressora)
    #             win32print.WritePrinter(handle_impressora, conteudo_bytes)
    #             win32print.EndPagePrinter(handle_impressora)
    #         win32print.EndDocPrinter(handle_impressora)
    #     finally:
    #         win32print.ClosePrinter(handle_impressora)
    #     print(f'Etiqueta impressa com sucesso {quantidade} vezes!')
    


    def imprimir_etiqueta(conteudo, impressora, quantidade):       
        if impressora is None:
            impressora = win32print.GetDefaultPrinter()
        
        handle_impressora = win32print.OpenPrinter(impressora)
        try:
            # Se a impressora ZPL suportar, adicione o comando ^CI28 para definir a codificação UTF-8 no início do conteúdo ZPL
            # conteudo = "^CI28\n" + conteudo
            
            # Debug: Exibir conteúdo antes da codificação
            # print("Conteúdo ZPL antes da codificação:", conteudo)
            
            conteudo_bytes = conteudo.encode('utf-8')
            
            # Debug: Exibir conteúdo após codificação
            # print("Conteúdo ZPL após codificação:", conteudo_bytes)
            
            job = win32print.StartDocPrinter(handle_impressora, 1, ("Impressão de Etiqueta", None, "RAW"))
            for _ in range(quantidade):
                win32print.StartPagePrinter(handle_impressora)
                win32print.WritePrinter(handle_impressora, conteudo_bytes)
                win32print.EndPagePrinter(handle_impressora)
            win32print.EndDocPrinter(handle_impressora)
        finally:
            win32print.ClosePrinter(handle_impressora)
        print(f'Etiqueta impressa com sucesso {quantidade} vezes!')

        
    def imprimir(e, produto_id=None):
        fabricacao = fabricacao_field.value
        vencimento = vencimento_field.value
        temperatura = dropdown_temperatura.value
        etiqueta = dropdown_etiquetas.value
        impressora = dropdown_impressoras.value
        quantidade = int(quantidade_impressao_textfield.value)
        sexo = dropdown_sexo.value
        lote = lote_dropdown.value
        
        empresa = controller.empresas()
        
        if produto_id is None:
            exibir_mensagem_erro(page, "Produto não especificado.")
            return
        
        conteudo_etiqueta = criar_etiqueta(produto_id, fabricacao, vencimento, temperatura, etiqueta, impressora, quantidade, sexo, lote, empresa)
        if conteudo_etiqueta:
            imprimir_etiqueta(conteudo_etiqueta, impressora, quantidade)
            exibir_mensagem_sucesso(page, f'Etiqueta impressa com sucesso {quantidade} vezes!')
        else:
            exibir_mensagem_erro(page, "Erro ao criar a etiqueta.")
        fechar_popup_print(e)          
            
    
    def abrir_dialog_produto(e, produto_id=None):
        if produto_id:
            editar_produto(e, produto_id)
        else:
            
            atualizar_dropdown_tipo(selecionar_ultimo=True)
            dialog_produto.open = True
            page.update()


    def fechar_dialog_produto(e):
        dialog_produto.open = False
        page.update()

    def abrir_dialog_tipo(e):
        dialog_tipo.open = True
        page.update()
        
    def abrir_dialog_print(e, produto_id):
        etiquetas_disponiveis = carregar_etiquetas()
        atualizar_dropdown_lote(selecionar_ultimo=True)

    
        if etiquetas_disponiveis:
            dropdown_etiquetas.options = [ft.dropdown.Option(etiqueta) for etiqueta in etiquetas_disponiveis]
            dropdown_etiquetas.update()  # Atualize o dropdown com as novas opções
        
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text('Nenhuma etiqueta disponível ou diretório não encontrado!'),
                bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
        dialog_print.open = True
        dialog_print.update()

        # Definir a função de clique para o botão de impressão
        dialog_print.actions[-1].on_click = lambda e: imprimir(e, produto_id)
        page.update()

    def fechar_popup_tipo(e):
        dialog_tipo.open = False
        page.update()
        abrir_dialog_produto(e)
        
    def fechar_popup_print(e):
        
        dialog_print.open = False
        page.update()
        
    def carregar_produtos(pagina_atual, itens_por_pagina):
        produtos = controller.obter_item_nutricional()
        inicio = (pagina_atual - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        return produtos[inicio:fim]
    
    tipos_cache = controller.obter_tipo()
    
    def obter_nome_tipo_por_id(tipo_id, tipos_cache):
        for tipo in tipos_cache:
            if tipo.id == tipo_id:
                return tipo.tipo
        return ""
    
    def gerar_linhas_tabela(produtos, tipos_cache):               
        rows = []
        for produto in produtos:            
            if isinstance(produto, dict):
                codigo = produto.get('codigo')
                corte = produto.get('corte')
                tipo_id = produto.get('tipo')
                tipo_nome = obter_nome_tipo_por_id(tipo_id, tipos_cache) if tipo_id else ""
                preco = produto.get('preco')
                produto_id = produto.get('id')               
                
          
            else:  # Assume que é um objeto ItemNutricional
                codigo = produto.codigo
                corte = produto.corte
                tipo_nome = produto.tipo.tipo if produto.tipo else ""
                preco = produto.preco 
                produto_id = produto.id   
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=str(codigo))),
                        ft.DataCell(ft.Text(value=str(corte))),
                        ft.DataCell(ft.Text(value=str(tipo_nome))),  # Certifique-se de que tipo_id é o atributo correto
                        ft.DataCell(ft.Text(value=str(preco))),
                        ft.DataCell(
                            ft.Row(
                                controls=[                                   
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.PRINT,
                                        width=50,                                        
                                        on_click=lambda e, produto_id=produto_id: abrir_dialog_print(e, produto_id)
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                )
            )
        return rows 
     
    
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text(value="Código")),
            ft.DataColumn(ft.Text(value="Corte")),
            ft.DataColumn(ft.Text(value="Tipo")),
            ft.DataColumn(ft.Text(value="Preço")),
            ft.DataColumn(ft.Text(value="Ações")),
        ],
        rows=gerar_linhas_tabela(carregar_produtos(pagina_atual, itens_por_pagina), tipos_cache),
        expand=True
    )
        
    def atualizar_tabela(e):
        termo_busca = search_input.value
        if termo_busca:
            produtos_pagina = controller.pesquisa(termo_busca)
        else:
            produtos_pagina = carregar_produtos(pagina_atual, itens_por_pagina)
            
        tipos_cache = controller.obter_tipo() 
        tabela.rows.clear()
        tabela.rows.extend(gerar_linhas_tabela(produtos_pagina, tipos_cache))
        paginacao_controls.controls[1].value = f"Página {pagina_atual} de {((total_produtos + itens_por_pagina - 1) // itens_por_pagina)}"
        tabela.update()
        page.update()


    search_input = create_text_field(hint_text="Busque por código, código de barras ou nome do produto...", label="Busca", width=500)
    search_input.on_change = atualizar_tabela
          
    tipo_carne_dropdown = ft.Dropdown(
        label="Tipo de Carne",
        border_radius=ft.border_radius.all(2),
        border_width=1,
        options=[]
    )
    lotes = controller.obter_lote()
    lote_dropdown = ft.Dropdown(
        label="Lote",
        border_radius=ft.border_radius.all(2),
        border_width=1,
        options=[]
    )

    novo_tipo_field = ft.TextField(label="Novo Tipo")

    dialog_tipo = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Adicionar Tipo"),
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
        content=ft.Container(
            expand=True,
            width=400,
            height=200,
            margin=ft.margin.Margin(left=0, top=15, right=0, bottom=30),
            content=ft.Column(
                controls=[novo_tipo_field]
            )
        ),
        actions=[
            ft.TextButton("Fechar", on_click=fechar_popup_tipo),
            ft.ElevatedButton(
                text="Salvar",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE
                ),
                on_click=lambda e: salvar_novo_tipo(dialog_tipo)
            )
        ]
    )
    temperaturas = controller.obter_temperatura()
    
    dropdown_temperatura = ft.Dropdown(
        label="Selecione a temperatura",
        hint_text="Selecione a temperatura",
        options=[ft.dropdown.Option(temperatura.temperatura) for temperatura in temperaturas],
        
    )

    dropdown_etiquetas = ft.Dropdown(
        label="Selecione uma etiqueta",
        hint_text="Selecione a etiqueta",                                  
        options=[]
    )
    
    impressoras_disponiveis =  obter_impressoras()
    dropdown_impressoras = ft.Dropdown(
        hint_text="Selecione a impressora",        
        options=[ft.dropdown.Option(impressora) for impressora in impressoras_disponiveis],
        width=300
    )
    quantidade_impressao_textfield = ft.TextField(label="Quantidade")
    fabricacao_field = ft.TextField(label="Fabricação")
    vencimento_field  = ft.TextField(label="Vencimento")
    dropdown_sexo = ft.Dropdown(
        hint_text="Sexo",
        options=[
            ft.dropdown.Option("F"),
            ft.dropdown.Option("M"),
        ]
                        
    )
    
    dialog_print = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Impressão"),
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
        content=ft.Container(
            expand=True,
            width=400,
            # height=350,
            margin=ft.margin.Margin(left=0, top=15, right=0, bottom=30),
            content=ft.Column(
                controls=[
                    fabricacao_field,                    
                    vencimento_field,                    
                    dropdown_temperatura,
                    dropdown_impressoras,
                    dropdown_etiquetas,
                    dropdown_sexo,
                    lote_dropdown,
                    quantidade_impressao_textfield                               

                ]
            )
        ),
        actions=[
            ft.TextButton("Fechar", on_click=fechar_popup_print),
            ft.ElevatedButton(
                text="Imprimir",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE
                ),
                on_click=lambda e: imprimir_etiqueta(dialog_tipo)
            )
        ],
    
    )
    
    codigo_field = create_text_field(label="Código", width=200)
    
    corte_field = create_text_field(label="Descrição", expand=True)
    
    preco_field = create_text_field(label="Preço", width=200)
    
    codigo_barras_field = create_text_field(label="Código de Barras", width=200)   
    
    porcao_embalagem_field = create_text_field(label="Porção por Embalagem", expand=True)
        
    porcao_field = create_text_field(label="Porção", expand=True)
    
    alergico_field = create_text_field(label="Campo Adicional", multiline=True, expand=True)
    
    peso_field = create_text_field(label="Peso", width=200)
    
    informacao_adicional_field = create_text_field(label="Informação Adicional", multiline=True, expand=True)
    
    valor_energico_field_100 = create_small_text_field()
    valor_energico_field_0 = create_small_text_field()
    valor_energico_field_vd = create_small_text_field()
    
    carboidratos_totais_field_100 = create_small_text_field()
    carboidratos_totais_field_0 = create_small_text_field()
    carboidratos_totais_field_vd = create_small_text_field()
    
    acucares_totais_field_100 = create_small_text_field()
    acucares_totais_field_0 = create_small_text_field()
    acucares_totais_field_vd = create_small_text_field()
    
    acucares_adicionados_field_100 = create_small_text_field()
    acucares_adicionados_field_0 = create_small_text_field()
    acucares_adicionados_field_vd = create_small_text_field()
    
    proteinas_field_100 = create_small_text_field()
    proteinas_field_0 = create_small_text_field()
    proteinas_field_vd = create_small_text_field()
    
    gorduras_totais_field_100 = create_small_text_field()
    gorduras_totais_field_0 = create_small_text_field()
    gorduras_totais_field_vd = create_small_text_field()
    
    gorduras_saturadas_field_100 = create_small_text_field()
    gorduras_saturadas_field_0 = create_small_text_field()
    gorduras_saturadas_field_vd = create_small_text_field()

    gorduras_trans_field_100 = create_small_text_field()
    gorduras_trans_field_0 = create_small_text_field()
    gorduras_trans_field_vd = create_small_text_field()
   
    fibra_field_100 = create_small_text_field()
    fibra_field_0 = create_small_text_field()
    fibra_field_vd = create_small_text_field()
    
    sodio_field_100 = create_small_text_field()
    sodio_field_0 = create_small_text_field()
    sodio_field_vd = create_small_text_field()
    
    
    def salvar_novo_produto(e, produto_id=None):
        
        dados_produto = {
            'codigo': codigo_field.value,
            'corte': corte_field.value,
            'tipo': tipo_carne_dropdown.value,  # Supondo que tipo_carne_dropdown contém o ID do tipo
            'preco': preco_field.value,
            'codigo_barras': codigo_barras_field.value,
            'porcao_embalagem': porcao_embalagem_field.value,
            'porcao': porcao_field.value,
            'campo_adicional': alergico_field.value,
            'peso': peso_field.value,
            'informacoes_adicionais': informacao_adicional_field.value,
            'valor_energetico_100g': valor_energico_field_100.value,
            'valor_energetico_porcao': valor_energico_field_0.value,
            'valor_energetico_vd': valor_energico_field_vd.value,
            'carboidratos_totais_100g': carboidratos_totais_field_100.value,
            'carboidratos_totais_porcao': carboidratos_totais_field_0.value,
            'carboidratos_totais_vd': carboidratos_totais_field_vd.value,
            'acucares_totais_100g': acucares_totais_field_100.value,
            'acucares_totais_porcao': acucares_totais_field_0.value,
            'acucares_totais_vd': acucares_totais_field_vd.value,
            'acucares_adicionados_100g': acucares_adicionados_field_100.value,
            'acucares_adicionados_porcao': acucares_adicionados_field_0.value,
            'acucares_adicionados_vd': acucares_adicionados_field_vd.value,
            'proteinas_100g': proteinas_field_100.value,
            'proteinas_porcao': proteinas_field_0.value,
            'proteinas_vd': proteinas_field_vd.value,
            'gorduras_totais_100g': gorduras_totais_field_100.value,
            'gorduras_totais_porcao': gorduras_totais_field_0.value,
            'gorduras_totais_vd': gorduras_totais_field_vd.value,
            'gorduras_saturadas_100g': gorduras_saturadas_field_100.value,
            'gorduras_saturadas_porcao': gorduras_saturadas_field_0.value,
            'gorduras_saturadas_vd': gorduras_saturadas_field_vd.value,
            'gorduras_trans_100g': gorduras_trans_field_100.value,
            'gorduras_trans_porcao': gorduras_trans_field_0.value,
            'gorduras_trans_vd': gorduras_trans_field_vd.value,
            'fibra_alimentar_100g': fibra_field_100.value,
            'fibra_alimentar_porcao': fibra_field_0.value,
            'fibra_alimentar_vd': fibra_field_vd.value,
            'sodio_100g': sodio_field_100.value,
            'sodio_porcao': sodio_field_0.value,
            'sodio_vd': sodio_field_vd.value
        }
        try:

            if produto_id:  # Se existe um ID, atualiza o produto
                controller.atualizar_item_nutricional(produto_id, dados_produto)
                mensagem = 'Produto atualizado com sucesso!'
            else:  # Senão, cria um novo produto
                controller.salvar_produto(dados_produto)
                mensagem = 'Produto adicionado com sucesso!'
            
            exibir_mensagem_sucesso(page, mensagem)
            limpar_campos()                       
        except Exception as erro:
            mensagem = f'Erro ao salvar o produto: {str(erro)}'
            exibir_mensagem_erro(page, mensagem)
        
        fechar_dialog_produto(e)   
        nonlocal total_produtos
        total_produtos = obter_total_produtos()
        atualizar_tabela(None)
        page.update()
   
    def editar_produto(e, produto_id):
        produto = controller.obter_item_nutricional_por_id(produto_id)
        if produto:
   
            # Configurações básicas do produto
            codigo_field.value = produto.codigo
            corte_field.value = produto.corte
            preco_field.value = str(produto.preco)
            tipo_carne_dropdown.value = produto.tipo_id  # Adicionado para definir o tipo de carne
            codigo_barras_field.value = produto.codigo_barras
            porcao_embalagem_field.value = produto.porcao_embalagem
            porcao_field.value = produto.porcao
            alergico_field.value = produto.campo_adicional
            informacao_adicional_field.value = produto.informacoes_adicionais

            # Campos nutricionais
            valor_energico_field_100.value = str(produto.valor_energetico_100g)
            valor_energico_field_0.value = str(produto.valor_energetico_porcao)
            valor_energico_field_vd.value = str(produto.valor_energetico_vd)

            carboidratos_totais_field_100.value = str(produto.carboidratos_totais_100g)
            carboidratos_totais_field_0.value = str(produto.carboidratos_totais_porcao)
            carboidratos_totais_field_vd.value = str(produto.carboidratos_totais_vd)

            acucares_totais_field_100.value = str(produto.acucares_totais_100g)
            acucares_totais_field_0.value = str(produto.acucares_totais_porcao)
            acucares_totais_field_vd.value = str(produto.acucares_totais_vd)

            acucares_adicionados_field_100.value = str(produto.acucares_adicionados_100g)
            acucares_adicionados_field_0.value = str(produto.acucares_adicionados_porcao)
            acucares_adicionados_field_vd.value = str(produto.acucares_adicionados_vd)

            proteinas_field_100.value = str(produto.proteinas_100g)
            proteinas_field_0.value = str(produto.proteinas_porcao)
            proteinas_field_vd.value = str(produto.proteinas_vd)

            gorduras_totais_field_100.value = str(produto.gorduras_totais_100g)
            gorduras_totais_field_0.value = str(produto.gorduras_totais_porcao)
            gorduras_totais_field_vd.value = str(produto.gorduras_totais_vd)

            gorduras_saturadas_field_100.value = str(produto.gorduras_saturadas_100g)
            gorduras_saturadas_field_0.value = str(produto.gorduras_saturadas_porcao)
            gorduras_saturadas_field_vd.value = str(produto.gorduras_saturadas_vd)

            gorduras_trans_field_100.value = str(produto.gorduras_trans_100g)
            gorduras_trans_field_0.value = str(produto.gorduras_trans_porcao)
            gorduras_trans_field_vd.value = str(produto.gorduras_trans_vd)

            fibra_field_100.value = str(produto.fibra_alimentar_100g)
            fibra_field_0.value = str(produto.fibra_alimentar_porcao)
            fibra_field_vd.value = str(produto.fibra_alimentar_vd)

            sodio_field_100.value = str(produto.sodio_100g)
            sodio_field_0.value = str(produto.sodio_porcao)
            sodio_field_vd.value = str(produto.sodio_vd)

            # dialog_produto.actions[-1].on_click = lambda e: salvar_novo_produto(e, produto_id)
        
            # Atualiza o dropdown de tipos antes de abrir o diálogo
            # atualizar_dropdown_tipo(selecionar_ultimo=False)
            
            atualizar_dropdown_tipo()

            # Certifique-se de que o tipo_id corresponde a uma opção no dropdown
            if produto.tipo_id in [option.key for option in tipo_carne_dropdown.options]:
                tipo_carne_dropdown.value = produto.tipo_id
                
            dialog_produto.actions[-1].on_click = lambda e: salvar_novo_produto(e, produto_id)
            dialog_produto.open = True
            page.update()

    dialog_produto = ft.AlertDialog(
            modal=True,
            title=ft.Text(value="Cadastro de Produto"),
            elevation=0,
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            content=ft.Container(
                expand=True,
                width=960,
                height=700,
                margin=ft.margin.Margin(left=0, top=15, right=0, bottom=30),
                content=ft.Column(
                    controls=[
                        ft.Tabs(
                            scrollable=True,
                            tabs=[
                                ft.Tab(
                                    text="Produto",
                                    content=ft.Container(
                                        margin=ft.margin.Margin(left=0, top=30, right=0, bottom=30),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    spacing=15,
                                                    controls=[
                                                        tipo_carne_dropdown,
                                                        ft.ElevatedButton(
                                                            text="Tipo",
                                                            icon=ft.icons.ADD,
                                                            on_click= abrir_dialog_tipo,
                                                            style=ft.ButtonStyle(
                                                                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                                                                bgcolor=ft.colors.BLUE,
                                                                color=ft.colors.WHITE
                                                            )
                                                        )
                                                    ]
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        codigo_field,
                                                        corte_field,
                                                        preco_field
                                                    ]
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        codigo_barras_field,
                                                        porcao_embalagem_field,
                                                        porcao_field,                                                        
                                                    ]
                                                ),
                                                ft.Row(
                                                    controls =[
                                                        alergico_field,
                                                        peso_field
                                                    ]
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        informacao_adicional_field
                                                    ]
                                                )
                                                                        
                                                
                                            ]
                                        )
                                    )
                                ),
                                ft.Tab(
                                    text="Nutricional",
                                    content=ft.Container(
                                        expand=True,
                                        margin=ft.margin.Margin(left=0, top=5, right=0, bottom=0),
                                        content=ft.Column(
                                            controls=[
                                                ft.DataTable(
                                                    column_spacing=100,
                                                    divider_thickness=0,
                                                    width=960,
                                                    data_row_max_height=41,
                                                    columns=[
                                                        ft.DataColumn(ft.Text(value="", expand=True)),
                                                        ft.DataColumn(ft.Text(value="100 g", width=100, text_align=ft.TextAlign.CENTER)),
                                                        ft.DataColumn(ft.Text(value="000 g", width=100, text_align=ft.TextAlign.CENTER)),
                                                        ft.DataColumn(ft.Text(value="%VD*", width=100, text_align=ft.TextAlign.CENTER)),
                                                    ],
                                                    rows=[
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Valor energético (kcal)")),
                                                                ft.DataCell(
                                                                    valor_energico_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    valor_energico_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    valor_energico_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Carboidratos totais (g)")),
                                                                ft.DataCell(
                                                                    carboidratos_totais_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    carboidratos_totais_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    carboidratos_totais_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Açúcares totais (g)")),
                                                                ft.DataCell(
                                                                    acucares_totais_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    acucares_totais_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    acucares_totais_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Açúcares adicionados (g)")),
                                                                ft.DataCell(
                                                                    acucares_adicionados_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    acucares_adicionados_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    acucares_adicionados_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Proteínas (g)")),
                                                                ft.DataCell(
                                                                    proteinas_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    proteinas_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    proteinas_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Gorduras totais (g)")),
                                                                ft.DataCell(
                                                                    gorduras_totais_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    gorduras_totais_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    gorduras_totais_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Gorduras saturadas (g)")),
                                                                ft.DataCell(
                                                                    gorduras_saturadas_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    gorduras_saturadas_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    gorduras_saturadas_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Gorduras Trans (g)")),
                                                                ft.DataCell(
                                                                    gorduras_trans_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    gorduras_trans_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    gorduras_trans_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Fibra alimentar (g)")),
                                                                ft.DataCell(
                                                                    fibra_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    fibra_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    fibra_field_vd
                                                                ),
                                                            ]
                                                        ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text(value="Sódio (mg)")),
                                                                ft.DataCell(
                                                                    sodio_field_100
                                                                ),
                                                                ft.DataCell(
                                                                    sodio_field_0
                                                                ),
                                                                ft.DataCell(
                                                                    sodio_field_vd
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    expand=1
                                                )
                                            ],
                                            expand=1
                                        )
                                    )
                                )
                            ],
                            expand=1
                        )
                    ],
                    expand=1
                )
            ),
            actions=[
                ft.TextButton("Fechar", on_click=fechar_dialog_produto),
                ft.ElevatedButton(
                    text="Salvar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE
                    ),
                    on_click=salvar_novo_produto
                ),
            ]
        )
    
    page.overlay.append(dialog_produto)
    page.overlay.append(dialog_tipo)
    page.overlay.append(dialog_print)
    
    page.update()   
    
    def salvar_novo_tipo(dialog):
        novo_tipo = novo_tipo_field.value
        if novo_tipo:  # Certifique-se de que algo foi digitado
            controller.criar_tipo(novo_tipo)
            fechar_popup_tipo(dialog)
            atualizar_dropdown_tipo(selecionar_ultimo=True)  # Atualizar dropdown e selecionar o último adicionado
            page.snack_bar = ft.SnackBar(
                content=ft.Text('Tipo adicionado com sucesso!'),
                bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open = True
            page.update()
            
    def proxima_pagina(e):
        nonlocal pagina_atual
        if pagina_atual * itens_por_pagina < total_produtos:
            pagina_atual += 1
            atualizar_tabela(e)

    def pagina_anterior(e):
        nonlocal pagina_atual
        if pagina_atual > 1:
            pagina_atual -= 1
            atualizar_tabela(e)

    def atualizar_dropdown_tipo(selecionar_ultimo=False):
        tipos = controller.obter_tipo()  # Função que obtém a lista de tipos do banco de dados
        tipo_carne_dropdown.options = [ft.dropdown.Option(tipo.tipo) for tipo in tipos]
        if selecionar_ultimo and tipos:
            tipo_carne_dropdown.value = tipos[-1].tipo  # Definir o último tipo como selecionado
        else:
            tipo_carne_dropdown.value = None  # Reset dropdown selection se não houver tipos
        tipo_carne_dropdown.update()

    

    search_row = ft.Row(
        controls=[
            search_input,
            ft.ElevatedButton(
                text="Buscar", icon=ft.icons.SEARCH,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE
                ),
                on_click=atualizar_tabela
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    
    
    paginacao_controls = ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.CHEVRON_LEFT, on_click=pagina_anterior),
            ft.Text(value=f"Página {pagina_atual} de {((total_produtos + itens_por_pagina - 1) // itens_por_pagina)}"),
            ft.IconButton(icon=ft.icons.CHEVRON_RIGHT, on_click=proxima_pagina)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )


    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        search_row,
                        ft.ElevatedButton(
                            text="Adicionar Corte",
                            on_click=abrir_dialog_produto,
                            icon=ft.icons.ADD,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                                bgcolor=ft.colors.BLUE,
                                color=ft.colors.WHITE
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                margin=ft.margin.Margin(left=20, top=10, right=30, bottom=10),
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[tabela],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        paginacao_controls
                    ],
                    expand=True
                ),
                expand=True,
                padding=ft.padding.Padding(left=30, top=1, right=30, bottom=5),
                margin=ft.margin.Margin(top=50, left=0, right=0, bottom=0)
            )
        ]
    )
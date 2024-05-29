import flet as ft
from controllers import Controller
from utils.notifications import exibir_mensagem_sucesso, exibir_mensagem_erro, exibir_messagem_delete



def tipo(page: ft.Page):
    controller = Controller()
    
    
    success_color = ft.colors.GREEN
    error_color = ft.colors.RED
    
    tipo_atual = None
    
    itens_por_pagina = 5
    pagina_atual = 1
    
    # def alert(mensagem, bgcolor_message):
    #     page.snack_bar = ft.SnackBar(
    #             content=ft.Text(mensagem),
    #             bgcolor=bgcolor_message,                
    #         )
    #     page.snack_bar.open = True
    
    def limpar_campos():
        novo_tipo_field = ""
        page.update()
        

    def obter_total_tipos():
        return len(controller.obter_tipo())  # Supondo que temos uma função para obter o número total de tipos
    
    total_tipos = obter_total_tipos()  

    def abrir_dialog_tipo(e, tipo=None):
        nonlocal tipo_atual
        tipo_atual = tipo
        if tipo:
            novo_tipo_field.value = tipo.tipo
        else:
            novo_tipo_field.value = ""
        dialog_tipo.open = True
        page.update()

    def fechar_popup_tipo(e):
        dialog_tipo.open = False
        page.update()

    search_input = ft.TextField(
        hint_text="Busque por código, código de barras ou nome do produto...",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        color=ft.colors.BLUE,
        border_width=1,
        width=500,
    )
    
    tipo_carne_dropdown = ft.Dropdown(
        label="Tipo de Carne",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.GREY_100,
        color=ft.colors.BLUE,
        border_width=0,
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
    
    page.overlay.append(dialog_tipo)
    
    page.update()
    
    def carregar_tipos(pagina_atual, itens_por_pagina):
        tipos = controller.obter_tipo()
        inicio = (pagina_atual - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        return tipos[inicio:fim]

    def gerar_linhas_tabela(tipos):
        rows = []
        for tipo in tipos:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=tipo.id)),
                        ft.DataCell(ft.Text(value=tipo.tipo)),                     
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.EDIT,
                                        width=50,
                                        on_click=lambda e, tipo=tipo: abrir_dialog_tipo(e, tipo)
                                    ),
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.DELETE,
                                        width=50,
                                        on_click=lambda e, tipo_id=tipo.id: deletar_tipo(e, tipo_id)
                    
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                )
            )
        return rows
    
    
    def deletar_tipo(e, tipo_id):
        controller.excluir_tipo(tipo_id)
        nonlocal total_tipos, pagina_atual
        total_tipos = obter_total_tipos()  # Atualiza o total de tipos
        # Verifica se a página atual deve ser reduzida após a exclusão
        if (pagina_atual - 1) * itens_por_pagina >= total_tipos and pagina_atual > 1:
            pagina_atual -= 1
        atualizar_tabela(None)  # Atualiza a tabela para refletir a exclusão
        exibir_messagem_delete(page, 'Tipo excluído com sucesso!')
        page.update()
    

    def atualizar_tabela(e):
        tipos_pagina = carregar_tipos(pagina_atual, itens_por_pagina)
        tabela.rows.clear()
        tabela.rows.extend(gerar_linhas_tabela(tipos_pagina))
        paginacao_controls.controls[1].value = f"Página {pagina_atual}"
        page.update()

    
    def salvar_novo_tipo(e):
        novo_tipo = novo_tipo_field.value
        if novo_tipo:  # Certifique-se de que algo foi digitado
            try:
                if tipo_atual:
                    controller.atualizar_tipo(tipo_atual.id, novo_tipo)  # Atualiza o tipo existente
                    mensagem = 'Tipo atualizado com sucesso!'
                    exibir_mensagem_sucesso(page, mensagem)
                 
                else:            
                    controller.criar_tipo(novo_tipo)  # Cria um novo tipo
                    mensagem = 'Tipo adicionado com sucesso!'
                    exibir_mensagem_sucesso(page, mensagem)
                    limpar_campos()
                    
                    
            except Exception as erro:
                mensagem = f'Erro ao salvar o tipo: {str(erro)}'
                exibir_mensagem_erro(page, mensagem)
     
            
            fechar_popup_tipo(e)            
            nonlocal total_tipos
            total_tipos = obter_total_tipos()
            atualizar_tabela(None)
            # page.snack_bar = ft.SnackBar(
            #     content=ft.Text(mensagem),
            #     bgcolor=ft.colors.GREEN,                
            # )
            # page.snack_bar.open = True
           
            page.update()
            
 
    def proxima_pagina(e):
        nonlocal pagina_atual
        if pagina_atual * itens_por_pagina < total_tipos:
            pagina_atual += 1
            atualizar_tabela(e)

    def pagina_anterior(e):
        nonlocal pagina_atual
        if pagina_atual > 1:
            pagina_atual -= 1
            atualizar_tabela(e)

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

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text(value="Código")),
            ft.DataColumn(ft.Text(value="Tipo")),            
            ft.DataColumn(ft.Text(value="Ações")),
        ],
        rows=gerar_linhas_tabela(carregar_tipos(pagina_atual, itens_por_pagina)),
        expand=True
    )

    paginacao_controls = ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.CHEVRON_LEFT, on_click=pagina_anterior),
            ft.Text(value=f"Página {pagina_atual}"),
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
                            text="Adicionar Tipo",
                            on_click=abrir_dialog_tipo,
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

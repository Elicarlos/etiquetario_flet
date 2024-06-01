import flet as ft
from controllers import Controller
from utils.notifications import exibir_mensagem_sucesso, exibir_mensagem_erro, exibir_messagem_delete



def lote(page: ft.Page):
    controller = Controller()
    
    
    success_color = ft.colors.GREEN
    error_color = ft.colors.RED
    
    lote_atual = None
    
    itens_por_pagina = 5
    pagina_atual = 1
    
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
    
    # def alert(mensagem, bgcolor_message):
    #     page.snack_bar = ft.SnackBar(
    #             content=ft.Text(mensagem),
    #             bgcolor=bgcolor_message,                
    #         )
    #     page.snack_bar.open = True
    
    def limpar_campos():
        novo_lote_field = ""
        page.update()
        

    def obter_total_lotes():
        return len(controller.obter_lote())  # Supondo que temos uma função para obter o número total de lotes
    
    total_lotes = obter_total_lotes()  

    def abrir_dialog_lote(e, lote=None):
        nonlocal lote_atual
        lote_atual = lote
        if lote:
            novo_lote_field.value = lote.lote
        else:
            novo_lote_field.value = ""
        dialog_lote.open = True
        page.update()

    def fechar_popup_lote(e):
        dialog_lote.open = False
        page.update()   
    
    search_input = create_text_field(hint_text="Busque por código, código de barras ou nome do produto...", label="Buscar", width=500)
    
    
    novo_lote_field = ft.TextField(label="Novo Lote")

    dialog_lote = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Adicionar Lote"),
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
        content=ft.Container(
            expand=True,
            width=400,
            height=100,
            margin=ft.margin.Margin(left=0, top=15, right=0, bottom=30),
            content=ft.Column(
                controls=[novo_lote_field]
            )
        ),
        actions=[
            ft.TextButton("Fechar", on_click=fechar_popup_lote),
            ft.ElevatedButton(
                text="Salvar",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE
                ),
                on_click=lambda e: salvar_novo_lote(dialog_lote)
            )
        ]
    )    
    
    page.overlay.append(dialog_lote)
    
    page.update()
    
    def carregar_lotes(pagina_atual, itens_por_pagina):
        lotes = controller.obter_lote()
        inicio = (pagina_atual - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        return lotes[inicio:fim]

    def gerar_linhas_tabela(lotes):
        rows = []
        for lote in lotes:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=lote.id)),
                        ft.DataCell(ft.Text(value=lote.lote)),                     
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.EDIT,
                                        width=50,
                                        on_click=lambda e, lote=lote: abrir_dialog_lote(e, lote)
                                    ),
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.DELETE,
                                        width=50,
                                        on_click=lambda e, id_lote=lote.id: deletar_lote(e, id_lote)
                    
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                )
            )
        return rows
    
    
    def deletar_lote(e, id_lote):
        controller.excluir_lote(id_lote)
        nonlocal total_lotes, pagina_atual
        total_lotes = obter_total_lotes()  # Atualiza o total de lotes
        # Verifica se a página atual deve ser reduzida após a exclusão
        if (pagina_atual - 1) * itens_por_pagina >= total_lotes and pagina_atual > 1:
            pagina_atual -= 1
        atualizar_tabela(None)  # Atualiza a tabela para refletir a exclusão
        exibir_messagem_delete(page, 'Lote excluído com sucesso!')
        page.update()
    

    def atualizar_tabela(e):
        lotes_pagina = carregar_lotes(pagina_atual, itens_por_pagina)
        tabela.rows.clear()
        tabela.rows.extend(gerar_linhas_tabela(lotes_pagina))
        paginacao_controls.controls[1].value = f"Página {pagina_atual}"
        page.update()

    
    def salvar_novo_lote(e):
        novo_lote = novo_lote_field.value
        if novo_lote:  # Certifique-se de que algo foi digitado
            try:
                if lote_atual:
                    controller.atualizar_lote(lote_atual.id, novo_lote)  # Atualiza o lote existente
                    mensagem = 'Lote atualizado com sucesso!'
                    exibir_mensagem_sucesso(page, mensagem)
                 
                else:            
                    controller.criar_lote(novo_lote)  # Cria um novo lote
                    mensagem = 'Lote adicionado com sucesso!'
                    exibir_mensagem_sucesso(page, mensagem)
                    limpar_campos()
                    
                    
            except Exception as erro:
                mensagem = f'Erro ao salvar o lote: {str(erro)}'
                exibir_mensagem_erro(page, mensagem)
     
            
            fechar_popup_lote(e)            
            nonlocal total_lotes
            total_lotes = obter_total_lotes()
            atualizar_tabela(None)
            # page.snack_bar = ft.SnackBar(
            #     content=ft.Text(mensagem),
            #     bgcolor=ft.colors.GREEN,                
            # )
            # page.snack_bar.open = True
           
            page.update()
            
 
    def proxima_pagina(e):
        nonlocal pagina_atual
        if pagina_atual * itens_por_pagina < total_lotes:
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
            ft.DataColumn(ft.Text(value="Lote")),            
            ft.DataColumn(ft.Text(value="Ações")),
        ],
        rows=gerar_linhas_tabela(carregar_lotes(pagina_atual, itens_por_pagina)),
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
                            text="Adicionar lote",
                            on_click=abrir_dialog_lote,
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

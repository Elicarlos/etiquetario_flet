import flet as ft
from controllers import Controller
from utils.notifications import exibir_mensagem_sucesso, exibir_mensagem_erro

def temperatura(page: ft.Page):
    controller = Controller()
    temperatura_atual = None
    
    itens_por_pagina = 5
    pagina_atual = 1
    
    def limpar_campos():
        nova_temperatura_field = ""
        page.update()
        

    def obter_total_temperatura():
        return len(controller.obter_temperatura())  # Supondo que temos uma função para obter o número total de temperaturas
    
    total_temperatura = obter_total_temperatura()  

    def abrir_dialog_temperatura(e, temperatura=None):
        nonlocal temperatura_atual
        temperatura_atual = temperatura
        if temperatura:
            nova_temperatura_field.value = temperatura.temperatura
        else:
            nova_temperatura_field.value = ""
        dialog_temperatura.open = True
        page.update()

    def fechar_popup_temperatura(e):
        dialog_temperatura.open = False
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
    
    nova_temperatura_field = ft.TextField(label="Nova Temperatura")

    dialog_temperatura = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Adicionar Temperatura"),
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
        content=ft.Container(
            expand=True,
            width=400,
            height=200,
            margin=ft.margin.Margin(left=0, top=15, right=0, bottom=30),
            content=ft.Column(
                controls=[nova_temperatura_field]
            )
        ),
        actions=[
            ft.TextButton("Fechar", on_click=fechar_popup_temperatura),
            ft.ElevatedButton(
                text="Salvar",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                    bgcolor=ft.colors.BLUE,
                    color=ft.colors.WHITE
                ),
                on_click=lambda e: salvar_nova_temperatura(e)
            )
        ]
    )    
    
    page.overlay.append(dialog_temperatura)
    page.update()
    
    def carregar_temperatura(pagina_atual, itens_por_pagina):
        temperaturas = controller.obter_temperatura()
        inicio = (pagina_atual - 1) * itens_por_pagina
        fim = inicio + itens_por_pagina
        return temperaturas[inicio:fim]

    def gerar_linhas_tabela(temperaturas):
        rows = []
        for temperatura in temperaturas:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=temperatura.id)),
                        ft.DataCell(ft.Text(value=temperatura.temperatura)),                     
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.EDIT,
                                        width=50,
                                        on_click=lambda e, temperatura=temperatura: abrir_dialog_temperatura(e, temperatura)
                                    ),
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.DELETE,
                                        width=50,
                                        on_click=lambda e, temperatura_id=temperatura.id: deletar_temperatura(e, temperatura_id)
                    
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                )
            )
        return rows
    
    def deletar_temperatura(e, temperatura_id):
        controller.excluir_temperatura(temperatura_id)
        nonlocal total_temperatura, pagina_atual
        total_temperatura = obter_total_temperatura()  # Atualiza o total de temperaturas
        # Verifica se a página atual deve ser reduzida após a exclusão
        if (pagina_atual - 1) * itens_por_pagina >= total_temperatura and pagina_atual > 1:
            pagina_atual -= 1
        atualizar_tabela(None)  # Atualiza a tabela para refletir a exclusão
        exibir_mensagem_sucesso(page, 'Temperatura deletada com sucesso!')

    def atualizar_tabela(e):
        temperatura_pagina = carregar_temperatura(pagina_atual, itens_por_pagina)
        tabela.rows.clear()
        tabela.rows.extend(gerar_linhas_tabela(temperatura_pagina))
        paginacao_controls.controls[1].value = f"Página {pagina_atual}"
        page.update()

    def salvar_nova_temperatura(e):
        nova_temperatura = nova_temperatura_field.value
        if nova_temperatura:  # Certifique-se de que algo foi digitado
            dados = {
                'temperatura': nova_temperatura
            }
            try:
                if temperatura_atual:
                    controller.atualizar_temperatura(temperatura_atual.id, dados)  # Atualiza a temperatura existente
                    mensagem = 'Temperatura atualizada com sucesso!'
                    exibir_mensagem_sucesso(page, mensagem)
                else:            
                    controller.salvar_temperatura(dados)  # Cria uma nova temperatura
                    mensagem = 'Temperatura adicionada com sucesso!'
                    exibir_mensagem_sucesso(page, mensagem)
                    limpar_campos()
                    
            except Exception as erro:
                mensagem = f'Erro ao salvar a temperatura: {str(erro)}'
                exibir_mensagem_erro(page, mensagem)
     
            fechar_popup_temperatura(e)            
            nonlocal total_temperatura
            total_temperatura = obter_total_temperatura()
            atualizar_tabela(None)
            page.update()
        else:
            exibir_mensagem_erro(page, "Por favor, insira uma temperatura válida.")
            
    def proxima_pagina(e):
        nonlocal pagina_atual
        if pagina_atual * itens_por_pagina < total_temperatura:
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
            ft.DataColumn(ft.Text(value="Temperatura")),            
            ft.DataColumn(ft.Text(value="Ações")),
        ],
        rows=gerar_linhas_tabela(carregar_temperatura(pagina_atual, itens_por_pagina)),
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
                            text="Adicionar Temperatura",
                            on_click=abrir_dialog_temperatura,
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

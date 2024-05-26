import flet as ft
from controllers import Controller

def produto(page: ft.Page):
    controller = Controller()

    search_input = ft.TextField(
        hint_text="Busque por código, código de barras ou nome do produto...",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        color=ft.colors.BLUE,
        border_width=1,
        width=500,
    )

    def carregar_produtos():
        produtos = controller.obter_itens_nutricionais()
        rows = []
        for produto in produtos:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=produto.codigo)),
                        ft.DataCell(ft.Text(value=produto.descricao)),
                        ft.DataCell(ft.Text(value=produto.preco)),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.EDIT,
                                        width=50
                                    ),
                                    ft.ElevatedButton(
                                        text=".",
                                        icon=ft.icons.DELETE,
                                        width=50
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                )
            )
        return rows

    def atualizar_tabela(e):
        tabela.rows.clear()
        tabela.rows.extend(carregar_produtos())
        page.update()

    def adicionar_produto(e):
        def salvar_novo_produto(e):
            codigo = codigo_field.value
            descricao = descricao_field.value
            preco = preco_field.value
            # Adicione a lógica para salvar o produto no banco de dados aqui
            controller.criar_produto(codigo, descricao, preco)
            fechar_popup(e)
            atualizar_tabela(e)
            page.snack_bar = ft.SnackBar(
                content=ft.Text('Produto adicionado com sucesso!'),
                bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open = True
            page.update()

        def fechar_popup(e):
            page.dialog.open = False
            page.update()

        codigo_field = ft.TextField(label="Código")
        descricao_field = ft.TextField(label="Descrição")
        preco_field = ft.TextField(label="Preço")

        tipo_carne_dropdown = ft.Dropdown(
            label="Tipo de Carne",
            border_radius=ft.border_radius.all(2),
            bgcolor=ft.colors.GREY_100,
            color=ft.colors.BLUE,
            border_width=0,
            options=[
                ft.dropdown.Option("Bovina")
            ]
        )

        page.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(value="Cadastro de Produto"),
            elevation=0,
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            content=ft.Container(
                expand=True,
                width=960,
                height=500,
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
                                                            on_click=adicionar_tipo,
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
                                                        ft.TextField(
                                                            label="Codigo",
                                                            width=150,
                                                            border_radius=ft.border_radius.all(2),
                                                            bgcolor=ft.colors.GREY_100,
                                                            color=ft.colors.BLUE,
                                                            hover_color=ft.colors.GREY_100,
                                                            border_width=0,
                                                        ),
                                                        ft.TextField(
                                                            label="Corte",
                                                            expand=True,
                                                            border_radius=ft.border_radius.all(2),
                                                            bgcolor=ft.colors.GREY_100,
                                                            color=ft.colors.BLUE,
                                                            hover_color=ft.colors.GREY_100,
                                                            border_width=0,
                                                        ),
                                                    ]
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        ft.TextField(
                                                            label="Codigo de Barras",
                                                            width=150,
                                                            border_radius=ft.border_radius.all(3),
                                                            bgcolor=ft.colors.GREY_100,
                                                            color=ft.colors.BLUE,
                                                            hover_color=ft.colors.GREY_100,
                                                            border_width=0,
                                                        ),
                                                        ft.TextField(
                                                            label="Porção por Embalagem",
                                                            expand=True,
                                                            border_radius=ft.border_radius.all(2),
                                                            bgcolor=ft.colors.GREY_100,
                                                            color=ft.colors.BLUE,
                                                            hover_color=ft.colors.GREY_100,
                                                            border_width=0,
                                                        ),
                                                        ft.TextField(
                                                            label="Porção",
                                                            expand=True,
                                                            border_radius=ft.border_radius.all(2),
                                                            bgcolor=ft.colors.GREY_100,
                                                            color=ft.colors.BLUE,
                                                            hover_color=ft.colors.GREY_100,
                                                            border_width=0,
                                                        ),
                                                    ]
                                                ),
                                                ft.TextField(
                                                    label="Campo Adicional",
                                                    multiline=True,
                                                    expand=True,
                                                    height=100,
                                                    border_radius=ft.border_radius.all(2),
                                                    bgcolor=ft.colors.GREY_100,
                                                    color=ft.colors.BLUE,
                                                    hover_color=ft.colors.GREY_100,
                                                    border_width=0,
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
                                                                    ft.TextField(
                                                                        width=100,
                                                                        expand=True,
                                                                        border_radius=ft.border_radius.all(2),
                                                                        bgcolor=ft.colors.GREY_100,
                                                                        color=ft.colors.BLUE,
                                                                        hover_color=ft.colors.GREY_100,
                                                                        border_width=1,
                                                                        height=35,
                                                                        content_padding=ft.padding.all(10),
                                                                    )),
                                                                ft.DataCell(
                                                                    ft.TextField(
                                                                        width=100,
                                                                        expand=True,
                                                                        border_radius=ft.border_radius.all(2),
                                                                        bgcolor=ft.colors.GREY_100,
                                                                        color=ft.colors.BLUE,
                                                                        hover_color=ft.colors.GREY_100,
                                                                        border_width=1,
                                                                        height=35,
                                                                        content_padding=ft.padding.all(10)
                                                                    )),
                                                                ft.DataCell(
                                                                    ft.TextField(
                                                                        width=100,
                                                                        expand=True,
                                                                        border_radius=ft.border_radius.all(2),
                                                                        bgcolor=ft.colors.GREY_100,
                                                                        color=ft.colors.BLUE,
                                                                        hover_color=ft.colors.GREY_100,
                                                                        border_width=1,
                                                                        height=35,
                                                                        content_padding=ft.padding.all(10)
                                                                    )),
                                                            ]
                                                        ),
                                                        # Adicione outras linhas conforme necessário
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
                ft.TextButton("Fechar", on_click=fechar_popup),
                ft.ElevatedButton(
                    text="Salvar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE
                    ), on_click=salvar_novo_produto
                ),
            ]
        )
        page.dialog.open = True
        page.update()

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
            ft.DataColumn(ft.Text(value="Descrição")),
            ft.DataColumn(ft.Text(value="Preço")),
            ft.DataColumn(ft.Text(value="Ações")),
        ],
        rows=carregar_produtos(),
        expand=True
    )

    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        search_row,
                        ft.ElevatedButton(
                            text="Adicionar Produto",
                            on_click=adicionar_produto,
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
                            controls=[
                                tabela
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    expand=True
                ),
                expand=True,
                padding=ft.padding.Padding(left=30, top=1, right=30, bottom=5),
                margin=ft.margin.Margin(top=50, left=0, right=0, bottom=0)
            )
        ]
    )

import flet as ft
import json

def banco_dados(page: ft.Page):
    def create_text_field(hint_text=None,label=None, width=None, expand=False, multiline=False, height=None, value=None):
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
        
    def carregar_configuracao():
        try:
            with open('db_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def salvar_configuracao(config):
        with open('db_config.json', 'w') as f:
            json.dump(config, f)

    config = carregar_configuracao()

    host_field = create_text_field(
        label="Localhost",
        hint_text="Localhost",
        value=config.get('localhost', ''),
        
    )

    database_field = create_text_field(
        label="Database",
        hint_text="Database",
        value=config.get('database', ''),
        
    )

    user_field = create_text_field(
        label="User",
        hint_text="User",
        value=config.get('user', ''),
        
    )

    password_field = create_text_field(
        label="Password",
        hint_text="Password",
        value=config.get('password', '')
        
        
    )
    
    port_field = create_text_field(
        label="Port",
        hint_text="Port",
        value=config.get('port', '')        
       
    )

    def salvar_dados_conexao(e):
        print("Salvando dados de conexão...")
        config = {
            'host': host_field.value,
            'database': database_field.value,
            'user': user_field.value,
            'password': password_field.value,
            'port': port_field.value
        }

        salvar_configuracao(config)
        print("Configuração salva:", config)

        # Exibir o SnackBar sem redirecionar
        page.snack_bar = ft.SnackBar(
            content=ft.Text('Banco de dados salvo com sucesso!'),
            bgcolor=ft.colors.GREEN
        )
        page.snack_bar.open = True
       
        page.update()

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(value="Configuração de Conexão com o Banco de Dados"),
                    alignment=ft.alignment.top_left
                ),
                ft.Divider(color=ft.colors.GREY),
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Row(controls=[host_field]),
                            ft.Row(controls=[database_field]),
                            ft.Row(controls=[user_field]),
                            ft.Row(controls=[password_field]),
                             ft.Row(controls=[port_field]),
                        ]
                    ),
                    margin=ft.margin.Margin(right=0, top=15, left=0, bottom=0)
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Salvar",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                            bgcolor=ft.colors.BLUE,
                            color=ft.colors.WHITE
                        ), on_click=salvar_dados_conexao),
                    alignment=ft.alignment.bottom_right,
                    expand=True
                )
            ]
        ),
        expand=True,
        padding=ft.padding.Padding(left=30, top=1, right=30, bottom=5),
        margin=ft.margin.Margin(top=15, left=0, right=0, bottom=10),
    )

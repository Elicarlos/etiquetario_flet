from components.lote import lote
from components.produto import produto
from controllers import Controller
import flet as ft
from components.home import home
from components.empresa import empresa
from components.tipo import tipo
from components.banco_dados import banco_dados
from components.tipo import tipo
from components.etiquetas import etiquetas
from components.tempertura import temperatura
from config.config import carregar_configuracao, salvar_configuracao
from utils.teste_conexao import testar_conexao

class CustomExpansionTile(ft.UserControl):
    def __init__(self, title, content, on_click=None):
        super().__init__()
        self.title = title
        self.content = content
        self.on_click = on_click
        self.expanded = False

    def build(self):
        return ft.Column(
            controls=[
                ft.ListTile(
                    title=self.title,
                    on_click=self.handle_click,
                    trailing=None,  # Remove a seta padrão
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                ),
                self.content if self.expanded else ft.Container()
            ]
        )

    def handle_click(self, e):
        if self.on_click:
            self.on_click(e)
        self.expanded = not self.expanded
        self.update()

def main(page: ft.Page):
    current_content = [None]
    
    page.window_maximized = True
    page.window_min_width = 1280 
    page.window_min_height = 720

    def exibir_mensagem_sucesso(mensagem):
        page.snack_bar = ft.SnackBar(
            ft.Text(mensagem),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()
        
    def exibir_mensagem_erro(mensagem):
        page.snack_bar = ft.SnackBar(
            ft.Text(mensagem),
            bgcolor=ft.colors.RED,
        )
        page.snack_bar.open = True
        page.update()

    def atualizar_home_container():
        nonlocal home_container
        home_container = home(page)

    def atualizar_empresa_container():
        nonlocal empresa_container
        empresa_container = empresa(page)

    def atualizar_produto_container():
        nonlocal produto_container
        produto_container = produto(page)

    def atualizar_tipo_container():
        nonlocal tipo_container
        tipo_container = tipo(page)

    def atualizar_banco_dados_container():
        nonlocal banco_dados_container
        banco_dados_container = banco_dados(page)

    def atualizar_etiquetas_container():
        nonlocal etiquetas_container
        etiquetas_container = etiquetas(page)

    def atualizar_temperatura_container():
        nonlocal temperatura_container
        temperatura_container = temperatura(page)
    
    def show_only(container):
        current_content[0] = container
        content_container.content = container
        page.update()
        
        
    # Função para salvar dados de conexão
    
        
    
        
    home_container = home(page)
    empresa_container = empresa(page)
    produto_container = produto(page)
    tipo_container = tipo(page)
    lote_container = lote(page)
    banco_dados_container = banco_dados(page)
    etiquetas_container = etiquetas(page)
    temperatura_container = temperatura(page)
        
    content_container = ft.Container(
        bgcolor=ft.colors.WHITE,
        margin=ft.margin.Margin(left=0, top=10, right=20, bottom=10),
        content=current_content[0] if current_content[0] else home_container,
        expand=True
    )    
        
    footer = ft.Container(
        bgcolor=ft.colors.WHITE,
        content=ft.Row(
            vertical_alignment=ft.VerticalAlignment.CENTER,
            controls=[
                ft.Text("© 2024 Cajuina Code"),
                ft.Text("Termos de Uso"),
                ft.Text("Política de Privacidade"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),      
        height=50,    
        margin=ft.margin.Margin(left=-10, top=1, right=-10, bottom=-10),      
    )
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        bgcolor=ft.colors.WHITE,
        color=ft.colors.GREY_900,
        title=ft.Text("W Carnes"),
    )
    
    
    sidbar = ft.Column(
        width=240,
        controls=[
            ft.ListTile(
                title=ft.Text("INÍCIO"),
                on_click=lambda e: [atualizar_home_container(), show_only(home_container)],
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            ),
            ft.ExpansionTile(
                title=ft.Text("CADASTRO"),         
                maintain_state=True,      
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                controls=[                
                    ft.ListTile(title=ft.TextButton(text="Empresa", on_click=lambda _: [atualizar_empresa_container(), show_only(empresa_container)])),
                    ft.ListTile(title=ft.TextButton(text="Corte", on_click=lambda _: [atualizar_produto_container(), show_only(produto_container)])),
                    ft.ListTile(title=ft.TextButton(text="Tipo", on_click=lambda _: [atualizar_tipo_container(), show_only(tipo_container)])),
                    ft.ListTile(title=ft.TextButton(text="Temperatura", on_click=lambda _: [atualizar_temperatura_container(), show_only(temperatura_container)])),
                    ft.ListTile(title=ft.TextButton(text="Lote", on_click=lambda _: [atualizar_temperatura_container(), show_only(lote_container)])),
                ],
            ),
            ft.ExpansionTile(
                title=ft.Text("CONFIGURAÇÃO"),         
                maintain_state=True,
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                controls=[
                    ft.ListTile(title=ft.TextButton(text="Banco de Dados", on_click=lambda _: [atualizar_banco_dados_container(), show_only(banco_dados_container)])),
                    ft.ListTile(title=ft.TextButton(text="Etiquetas", on_click=lambda _: [atualizar_etiquetas_container(), show_only(etiquetas_container)])),
                ],
            ),
        ]
    )
    
    page.add(
        ft.Row(
            controls=[
                sidbar,
                ft.Column(
                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            margin=ft.margin.Margin(left=0, top=10, right=20, bottom=10),
                            content=ft.Column(
                                controls=[
                                    content_container
                                ],
                            ),
                            expand=True
                        )
                    ],
                    expand=True
                )
            ],
            expand=True
        ),
        footer
    )

    page.bgcolor = '#EDF1F4'
    show_only(home_container)
    page.update()

ft.app(main)

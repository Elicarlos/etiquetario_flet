

from components.produto import produto
from controllers import Controller
import flet as ft
from components.home import home
from components.empresa import empresa
from components.tipo import tipo
from components.banco_dados import banco_dados
from components.tipo import tipo
from components.etiquetas import etiquetas



def main(page: ft.Page):
    current_content = [None]
        
    
           
    def exibir_mensagem_sucesso(mensagem):
        page.snack_bar = ft.SnackBar(
            ft.Text(mensagem),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()
        
    def atualizar_home_container():
        nonlocal home_container
        home_container = home(page)
        if current_content[0] == home_container:
            content_container.content = home_container
            page.update()
        
        
        
    def exibir_mensagem_erro(mensagem):
        page.snack_bar = ft.SnackBar(
            ft.Text(mensagem),
            bgcolor=ft.colors.RED,
        )
        page.snack_bar.open = True
        page.update() 

        
    
    def show_only(container):        
        current_content[0] = container
        content_container.content = container
        page.update()
        
        
    home_container = home(page)
    empresa_container = empresa(page)
    produto_container = produto(page)
    tipo_container = tipo(page)
    banco_dados_container = banco_dados(page)
    etiquetas_container = etiquetas(page)
        
    content_container = ft.Container(
        bgcolor=ft.colors.WHITE,
        margin=ft.margin.Margin(left=0, top=10, right=20, bottom=10),
        content=current_content[0] if current_content[0] else home_container,  # Inicialmente mostrando o container home
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
            ft.ExpansionTile(
                title=ft.Text("INÍCIO"),on_change=lambda _: show_only(home_container),
                maintain_state=True,
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),        
          ),
            ft.ExpansionTile(
            title=ft.Text("CADASTRO"),         
            maintain_state=True,      
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            controls=[                
                ft.ListTile(title=ft.TextButton(text="Empresa",  on_click=lambda _: show_only(empresa_container))),
                ft.ListTile(title=ft.TextButton(text="Produto", on_click=lambda _: show_only(produto_container))),
                ft.ListTile(title=ft.TextButton(text="Tipo",  on_click=lambda _: show_only(tipo_container))),

                ],
        ),
         ft.ExpansionTile(
            title=ft.Text("CONFIGURAÇÃO"),         
          
            maintain_state=True,
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            controls=[
                ft.ListTile(title=ft.TextButton(text="Banco de Dados",on_click=lambda _: show_only(banco_dados_container))),
                ft.ListTile(title=ft.TextButton(text="Etiquetas",on_click=lambda _: show_only(etiquetas_container))),
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
                        # search,
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

    page.bgcolor = ft.colors.GREY_100
    show_only(home_container)
    page.update()

ft.app(main)

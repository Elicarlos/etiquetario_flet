import flet as ft
# from components.search import search

def etiquetas(page: ft.Page):
    localhost_field = ft.TextField(
        label="Localhost",
        hint_text="Localhost",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        border_width=1,
        expand=True
    )

    database_field = ft.TextField(
        label="Database",
        hint_text="Database",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        border_width=1,
        expand=True
    )

    user_field = ft.TextField(
        label="User",
        hint_text="User",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        border_width=1,
        expand=True
    )

    password_field = ft.TextField(
        label="Password",
        hint_text="Password",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        border_width=1,
        expand=True,
        password=True  # Este campo será tratado como senha
    ) 
    
    return ft.Container(
        content=ft.Column(            
            controls=[ 
                ft.Container(
                    content=ft.Text(value="Etiquetas"),
                    alignment=ft.alignment.top_left
                ),               
                ft.Divider(color=ft.colors.GREY),
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Row(controls=[localhost_field]),
                            ft.Row(controls=[database_field]),                        
                            ft.Row(controls=[user_field]),
                            ft.Row(controls=[password_field]),
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
                                    ), on_click="salvar_produto"),
                    alignment=ft.alignment.bottom_right,
                    expand=True
                )
            ]
        ),
        expand=True,
        padding=ft.padding.Padding(left=30, top=1, right=30, bottom=5),
        margin=ft.margin.Margin(top=15, left=0, right=0, bottom=10),
        
    )

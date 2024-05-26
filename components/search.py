import flet as ft

def search(adicionar_produto):
    def realizar_busca(e):
        print(search_input.value)
    
    search_input = ft.TextField(
        hint_text="Busque por código, código de barras ou nome do produto...",
        border_radius=ft.border_radius.all(2),
        bgcolor=ft.colors.WHITE,
        hover_color=ft.colors.WHITE,
        color=ft.colors.BLUE,
        border_width=0,
        width=500,     
        # icon=ft.icons.SEARCH,
        # on_submit=realizar_busca,       
        
    )
       
    search_row = ft.Row(
        controls=[
            search_input,          
        ],
        alignment=ft.MainAxisAlignment.CENTER    
    )  
    return ft.Container(
        content=ft.Row(
            controls=[  
                ft.Row(
                    controls=[
                        search_row,
                        ft.ElevatedButton(
                            text="Buscar", icon=ft.icons.SEARCH,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                                bgcolor=ft.colors.BLUE,
                                color=ft.colors.WHITE
                            )
                        )
                    ]
                ),        
                
                ft.ElevatedButton(
                    text="Produto",
                    icon=ft.icons.ADD, 
                    on_click=adicionar_produto,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        
        ),
        margin=ft.margin.Margin(left=0, top=10, right=30, bottom=10),    
    )
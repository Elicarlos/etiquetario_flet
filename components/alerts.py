import flet as ft
def alert(page, mensagem, bgcolor_message):
    snack = page.snack_bar = ft.SnackBar(
                content=ft.Text(mensagem),
                bgcolor=bgcolor_message,                
            )
    page.snack_bar.open = True
    return snack
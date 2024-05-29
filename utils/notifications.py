import flet as ft

def exibir_mensagem_sucesso(page, mensagem):
    snack = page.snack_bar = ft.SnackBar(
                content=ft.Text(mensagem),
                bgcolor=ft.colors.GREEN,                
            )
    page.snack_bar.open = True
    return snack

def exibir_mensagem_erro(page, mensagem):
    snack = page.snack_bar = ft.SnackBar(
                content=ft.Text(mensagem),
                bgcolor=ft.colors.RED,                
            )
    page.snack_bar.open = True
    return snack


def exibir_messagem_delete(page, mensagem):
    snack = page.snack_bar = ft.SnackBar(
        content=ft.Text(mensagem),
        bgcolor=ft.colors.RED
    )
    page.snack_bar.open = True
    return snack
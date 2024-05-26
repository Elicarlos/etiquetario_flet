import flet as ft

def main(page: ft.Page):
    page.title = "AlertDialog examples"

    def abrir_outro(e):
        outro_dlg.open = True
        page.update()

    def fechar_outro(e):
        outro_dlg.open = False
        page.update()
        dlg.open = True
        page.update()

    def fechar_dlg(e):
        dlg.open = False
        page.update()

    outro_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Titulo Outro"),
        content=ft.Card(
            content=ft.Text(value="Texto Outro")
        ),
        actions=[
            ft.ElevatedButton(text="Fechar outro", on_click=fechar_outro)
        ]
    )

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Titulo Principal"),
        content=ft.Card(
            content=ft.Text(value="Texto card")
        ),
        actions=[
            ft.ElevatedButton(text="Abrir outro", on_click=abrir_outro),
            ft.ElevatedButton(text="Fechar", on_click=fechar_dlg)
        ]
    )

    def abrir_primeiro_dialogo(e):
        dlg.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Abrir Dialogo", on_click=abrir_primeiro_dialogo)
    )

    page.overlay.append(dlg)
    page.overlay.append(outro_dlg)

ft.app(target=main)

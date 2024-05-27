import flet as ft
from components.alerts import Toast


def main(page: ft.Page):
    mybutton = ft.ElevatedButton(
        text="My Toast"
    )
    
    Toast(
        page=page,
        icon=ft.icons.ABC,
        trigger = mybutton,
        bgcolor = ft.colors.GREEN,
        msg_title="Titurlo",
        msg_desc = "Mesangem desc"
        
    ).struct()
    
    

    page.add(mybutton)


if __name__ == "__main__":
    ft.app(target=main)
import flet as ft

from controllers import Controller


def empresa(page: ft.Page):
    controller = Controller()
    empresa_existente = Controller.obter_empresas().first()
    
    def create_text_field(hint_text=None,label=None, width=None, expand=False, multiline=False, height=None):
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
    
       
    cnpj_field = create_text_field(label="Cnpj", hint_text="Cnpj")
        
    razao_social_field = create_text_field(label="Razão Social",hint_text="Razão Social")
        
    fantasia_field = create_text_field(label="Fantasia", hint_text="Fantasia")
        
    numero_sif_field = create_text_field(label="Numero SIF", hint_text="Numero SIF")
        
    registro_adapi_field = create_text_field(label="Registro ADAPI", hint_text="Registro ADAPI")
    
    error_message = ft.Text(value="", color=ft.colors.RED)
    success_message = ft.Text(value="", color=ft.colors.GREEN)
    
    if empresa_existente:
            cnpj_field.value = empresa_existente.cnpj   
            razao_social_field.value = empresa_existente.razao_social
            fantasia_field.value = empresa_existente.fantasia
            numero_sif_field.value = empresa_existente.numero_sif
            registro_adapi_field.value = empresa_existente.registro_adapi
    
    
    
    def exibir_mensagem(mensagem, cor):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensagem),
            bgcolor=cor
        )
        page.snack_bar.open = True
        page.update()
        
    def salvar_empr(e):        
        cnpj = cnpj_field.value
        razao_social = razao_social_field.value
        fantasia = fantasia_field.value
        numero_sif = numero_sif_field.value
        registro_adapi = registro_adapi_field.value
     

        try:
            if empresa_existente:
                controller.atualizar_empresa(
                    empresa_existente.id,
                    cnpj_field.value,
                    razao_social_field.value,
                    fantasia_field.value,
                    numero_sif_field.value,
                    registro_adapi_field.value
                )
                exibir_mensagem("Empresa atualizada com sucesso.", ft.colors.GREEN)
            else:                
                controller.criar_empresa(
                    cnpj,
                    razao_social,
                    fantasia,
                    numero_sif,
                    registro_adapi
                )
                exibir_mensagem("Empresa criada com sucesso.", ft.colors.GREEN)

            error_message.value = ""
        except Exception as ex:
            exibir_mensagem(f"Erro ao salvar empresa: {ex}", ft.colors.RED)
            success_message.value = ""
            
        

        page.update()      
    
   
    return ft.Container(
        content=ft.Column(            
            controls=[ 
                ft.Container(
                    content=ft.Text(value="Empresa"),
                    alignment=ft.alignment.top_left
                ),               
                ft.Divider(color=ft.colors.GREY),
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Row(controls=[cnpj_field]),
                            ft.Row(controls=[razao_social_field, fantasia_field]),                        
                            ft.Row(controls=[numero_sif_field, registro_adapi_field]),
                            # error_message,  # Exibe mensagem de erro
                            # success_message
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
                                    ), on_click=salvar_empr),
                    alignment=ft.alignment.bottom_right,
                    expand=True
                )
            ]
        ),
        expand=True,
        padding=ft.padding.Padding(left=30, top=1, right=30, bottom=5),
        margin=ft.margin.Margin(top=15, left=0, right=0, bottom=10),
        
    )


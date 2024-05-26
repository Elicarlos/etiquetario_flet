

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
    
    controller = Controller()
    
    # def fechar_popup(e):
    #     page.dialog.open = False
    #     page.update()
        
    # def salvar_produto(e):
    #     # fechar_popup(e)
        
    # def editar_produto(e):
    #     # fechar_popup(e)
        
    # def deletar_produto(e):
    #     # fechar_popup(e)
        
    # def exibir_mensagem_sucesso(mensagem):
    #     success_dialog = ft.AlertDialog(
    #         modal=True,
    #         title=ft.Text(value="Sucesso"),
    #         content=ft.Text(value=mensagem),
    #         bgcolor=ft.colors.WHITE,
    #         elevation=0,
    #         shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #         actions=[
    #             ft.TextButton("Fechar", on_click=fechar_popup)
    #         ]
    #     )
    #     page.dialog = success_dialog
    #     page.dialog.open = True
    #     page.update()
    

        
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
        
        
    
        
     
    # def adicionar_empresa(e):        
    #     cnpj = cnpj_field.value
    #     razao_social = razao_social_field.value
    #     fantasia = fantasia_field.value
    #     numero_sif = numero_sif_field.value
    #     registro_adapi = registro_adapi_field.value
                
    #     if not cnpj or not razao_social or not fantasia or not numero_sif or not registro_adapi:
    #         error_message.value = "Todos os campos são obrigatórios."            
    #         page.update()
    #         return
        
    #     try:
    #         empresa_existente = controller.obter_empresas().first()         
            
    #         if empresa_existente:          
    #             controller.atualizar_empresa(empresa_existente.id,cnpj, razao_social, fantasia, numero_sif, registro_adapi)
    #             exibir_mensagem_sucesso("Empresa atualizada com sucesso")
                
              
                
    #         else:
    #             controller.criar_empresa(cnpj, razao_social, fantasia, numero_sif, registro_adapi)
    #             exibir_mensagem_sucesso("Empresa criada com sucesso")
                   
           
                
        
    #     except Exception as e:
    #         exibir_mensagem_erro(f"Erro ao criar empresa: {str(e)}")
           
            
    #     page.update() 
              
    # def salvar_empresa(e):
    #     global  cnpj_field, razao_social_field, fantasia_field, numero_sif_field, registro_adapi_field, error_message, success_message       
    #     cnpj_field = ft.TextField(
    #         label="Cnpj",
    #         hint_text="Cnpj",
    #         border_radius=ft.border_radius.all(2),
    #         bgcolor=ft.colors.WHITE,
    #         hover_color=ft.colors.WHITE,
    #         border_width=1,
    #         autofocus=True,
            
    #     )
        
    #     razao_social_field = ft.TextField(
    #         label="Razão Social",
    #         hint_text="Razão Social",
    #         border_radius=ft.border_radius.all(2),
    #         bgcolor=ft.colors.WHITE,
    #         hover_color=ft.colors.WHITE,
    #         border_width=1
    #     )
        
    #     fantasia_field = ft.TextField(
    #         label="Fantasia",
    #         hint_text="Fantasia",
    #         border_radius=ft.border_radius.all(2),
    #         bgcolor=ft.colors.WHITE,
    #         hover_color=ft.colors.WHITE,
    #         border_width=1
    #     )
        
    #     numero_sif_field = ft.TextField(
    #         label="Numero SIF",
    #         hint_text="Numero SIF",
    #         border_radius=ft.border_radius.all(2),
    #         bgcolor=ft.colors.WHITE,
    #         hover_color=ft.colors.WHITE,
    #         border_width=1,
    #     )
        
    #     registro_adapi_field = ft.TextField(
    #         label="Registro ADAPI",
    #         hint_text="Registro ADAPI",
    #         border_radius=ft.border.all(2),
    #         bgcolor=ft.colors.WHITE,
    #         hover_color=ft.colors.WHITE,
    #         border_width=1,
    #     )
        
    #     error_message = ft.Text(value="", color=ft.colors.RED)
    #     success_message = ft.Text(value="", color=ft.colors.GREEN)
        
    #     empresa = controller.obter_empresas().first()
    #     if empresa:
    #         cnpj_field.value = empresa.cnpj   
    #         razao_social_field.value = empresa.razao_social
    #         fantasia_field.value = empresa.fantasia
    #         numero_sif_field.value = empresa.numero_sif
    #         registro_adapi_field.value = empresa.registro_adapi
            
        
    #     empresa_dialog = ft.AlertDialog(
    #         modal=True,
    #         # title=ft.Text(value="Tipos"),
    #         shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #         elevation=0,
            
    #         content=ft.Container(
    #             expand=True,
    #             width=960,
    #             height=500,
    #             bgcolor=ft.colors.WHITE,
    #             content=ft.Column(
    #                 controls=[
    #                     ft.Row(                            
    #                         controls=[
    #                             ft.Text(
    #                                 value="Empresa",
    #                                 style=ft.TextStyle(
    #                                     weight=ft.FontWeight.BOLD,
    #                                     # size=25,
    #                                     # color=ft.colors.GREY
    #                                     )
    #                             ),
                         
                                
    #                         ],
    #                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    
    #                     ),
    #                       ft.Divider(
    #                                 color=ft.colors.GREY,                                
    #                       ),
    #                     ft.Row(
    #                         controls=[
    #                            cnpj_field
    #                         ]
    #                     ),
    #                     ft.Row(
    #                         controls=[
    #                             razao_social_field,
    #                             fantasia_field                            
    #                         ]
    #                     ),
    #                     ft.Row(
    #                         controls=[
    #                            numero_sif_field,
    #                            registro_adapi_field               
    #                         ]
    #                     ),
                        
    #                 ],
    #                 expand=True
    #             ),
                
    #         ),
            
    #         actions=[
    #             ft.TextButton("Fechar", on_click=fechar_popup),
    #             ft.ElevatedButton(
    #                 text="Salvar",
    #                 style=ft.ButtonStyle(
    #                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                     bgcolor=ft.colors.BLUE,
    #                     color=ft.colors.WHITE
    #             ), on_click=adicionar_empresa),
    #         ]
    #     )
    #     page.dialog = empresa_dialog
    #     page.dialog.open = True
    #     page.update()
    
    # def listar_produto(e): 
    #     page.dialog = ft.AlertDialog(
    #         modal=True,
    #         # title=ft.Text(value="Tipos"),
    #         shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #         elevation=0,
            
    #         content=ft.Container(
    #             expand=True,
    #             width=960,
    #             height=500,
    #             bgcolor=ft.colors.WHITE,
    #             content=ft.Column(
    #                 controls=[
    #                     ft.Row(                            
    #                         controls=[
    #                             ft.Text(
    #                                 value="Produtos",
    #                                 style=ft.TextStyle(
    #                                     weight=ft.FontWeight.BOLD,
    #                                     # size=25,
    #                                     # color=ft.colors.GREY
    #                                     )
    #                             ),
                              
    #                             ft.ElevatedButton(
    #                                 text="Adicionar",
    #                                 style=ft.ButtonStyle(
    #                                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                                     bgcolor=ft.colors.BLUE,
    #                                     color=ft.colors.WHITE
    #                                 ), on_click=adicionar_produto),
                                
    #                         ],
    #                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    
    #                     ),
    #                       ft.Divider(
    #                                 color=ft.colors.GREY,                                
    #                       ),
    #                     ft.Row(
    #                         controls=[
    #                             ft.Text(value="Buscar: "),
    #                             ft.TextField(
    #                                 hint_text="Tipo",
    #                                 border_radius=ft.border_radius.all(2),
    #                                 bgcolor=ft.colors.WHITE,
    #                                 hover_color=ft.colors.WHITE,
    #                                 color=ft.colors.GREY,
    #                                 border_width=1,
    #                                 width=500
    #                             ),
                                                           
    #                         ]
    #                     ),
    #                     ft.Row(
    #                         controls=[
    #                             ft.DataTable(
    #                                 width=960,
    #                                 column_spacing=100,
    #                                 data_row_max_height=41,
    #                                 columns=[
    #                                     ft.DataColumn(ft.Text(value="Código")),
    #                                     ft.DataColumn(ft.Text(value="Tipo")),
    #                                     ft.DataColumn(ft.Text(value="Ações"))
                                        
    #                                 ],
    #                                 rows=[
    #                                     ft.DataRow(
    #                                         cells=[
    #                                             ft.DataCell(
    #                                                 ft.Text(
    #                                                     value="111"
    #                                                 )
    #                                             ),
    #                                             ft.DataCell(
    #                                                 ft.Text(
    #                                                     value="Tipo"
    #                                                 )
    #                                             ),
    #                                             ft.DataCell(
    #                                                 ft.Row(
    #                                                     controls=[
    #                                                         ft.ElevatedButton(
    #                                                             text=".",
    #                                                             icon=ft.icons.EDIT,
    #                                                             width=50,
                                                    
    #                                                         ),
    #                                                         ft.ElevatedButton(
    #                                                             text=".",
    #                                                             icon=ft.icons.DELETE,
    #                                                             width=50
    #                                                         )
    #                                                     ]
    #                                                 )
                                                    
    #                                             )
    #                                         ]
    #                                     )
                                        
    #                                 ]
                                
                                    
    #                             )
    #                         ]
    #                     ),
    #                 ],
    #                 expand=True
    #             ),
                
    #         ),
    #         actions=[
    #             ft.TextButton("Fechar", on_click=fechar_popup),
    #             ft.ElevatedButton(
    #                 text="Salvar",
    #                 style=ft.ButtonStyle(
    #                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                     bgcolor=ft.colors.BLUE,
    #                     color=ft.colors.WHITE
    #             ), on_click=salvar_produto),
    #         ]
    #     )
        
    #     page.dialog.open = True
    #     page.update()
        
    # def listar_tipo(e): 
    #     page.dialog = ft.AlertDialog(
    #         modal=True,
    #         # title=ft.Text(value="Tipos"),
    #         shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #         elevation=0,
            
    #         content=ft.Container(
    #             expand=True,
    #             width=960,
    #             height=500,
    #             bgcolor=ft.colors.WHITE,
    #             content=ft.Column(
    #                 controls=[
    #                     ft.Row(                            
    #                         controls=[
    #                             ft.Text(
    #                                 value="Tipos",
    #                                 style=ft.TextStyle(
    #                                     weight=ft.FontWeight.BOLD,
    #                                     # size=25,
    #                                     # color=ft.colors.GREY
    #                                     )
    #                             ),
                              
    #                             ft.ElevatedButton(
    #                                 text="Adicionar",
    #                                 style=ft.ButtonStyle(
    #                                 shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                                 bgcolor=ft.colors.BLUE,
    #                                 color=ft.colors.WHITE
    #                                 ), on_click=adicionar_produto),
                                
    #                         ],
    #                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    
    #                     ),
    #                       ft.Divider(
    #                                 color=ft.colors.GREY,                                
    #                       ),
    #                     ft.Row(
    #                         controls=[
    #                             ft.Text(value="Buscar: "),
    #                             ft.TextField(
    #                                 hint_text="Tipo",
    #                                 border_radius=ft.border_radius.all(2),
    #                                 bgcolor=ft.colors.WHITE,
    #                                 hover_color=ft.colors.WHITE,
    #                                 color=ft.colors.GREY,
    #                                 border_width=1,
    #                                 width=500
    #                             ),
                                                           
    #                         ]
    #                     ),
    #                     ft.Row(
    #                         controls=[
    #                             ft.DataTable(
    #                                 width=960,
    #                                 column_spacing=100,
    #                                 data_row_max_height=41,
    #                                 columns=[
    #                                     ft.DataColumn(ft.Text(value="Código")),
    #                                     ft.DataColumn(ft.Text(value="Tipo")),
    #                                     ft.DataColumn(ft.Text(value="Ações"))
                                        
    #                                 ],
    #                                 rows=[
    #                                     ft.DataRow(
    #                                         cells=[
    #                                             ft.DataCell(
    #                                                 ft.Text(
    #                                                     value="111"
    #                                                 )
    #                                             ),
    #                                             ft.DataCell(
    #                                                 ft.Text(
    #                                                     value="Tipo"
    #                                                 )
    #                                             ),
    #                                             ft.DataCell(
    #                                                 ft.Row(
    #                                                     controls=[
    #                                                         ft.ElevatedButton(
    #                                                             text=".",
    #                                                             icon=ft.icons.EDIT,
    #                                                             width=50,
                                                    
    #                                                         ),
    #                                                         ft.ElevatedButton(
    #                                                             text=".",
    #                                                             icon=ft.icons.DELETE,
    #                                                             width=50
    #                                                         )
    #                                                     ]
    #                                                 )
                                                    
    #                                             )
    #                                         ]
    #                                     )
                                        
    #                                 ]
                                
                                    
    #                             )
    #                         ]
    #                     ),
    #                 ],
    #                 expand=True
    #             ),
                
    #         ),
    #         actions=[
    #             ft.TextButton("Fechar", on_click=fechar_popup),
    #             ft.ElevatedButton(
    #                 text="Salvar",
    #                 style=ft.ButtonStyle(
    #                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                     bgcolor=ft.colors.BLUE,
    #                     color=ft.colors.WHITE
    #             ), on_click=salvar_produto),
    #         ]
    #     )
        
    #     page.dialog.open = True
    #     page.update()
        
    # def adicionar_tipo(e): 
    #     page.dialog = ft.AlertDialog(
    #         modal=True,
    #         # title=ft.Text(value="Tipos"),
    #         shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #         elevation=0,
            
    #         content=ft.Container(
    #             expand=True,
    #             width=960,
    #             height=500,
    #             bgcolor=ft.colors.WHITE,
    #             content=ft.Column(
    #                 controls=[
    #                     ft.Row(
    #                         controls=[
    #                             ft.TextField(
    #                                 hint_text="Tipo",
    #                                 border_radius=ft.border_radius.all(2),
    #                                 bgcolor=ft.colors.WHITE,
    #                                 hover_color=ft.colors.WHITE,
    #                                 color=ft.colors.GREY,
    #                                 border_width=0,
    #                                 width=500
    #                             ),
    #                             ft.ElevatedButton(text="Salvar")
                                
    #                         ]
    #                     ),
    #                     ft.Row(
    #                         controls=[
    #                             ft.DataTable(
    #                                 width=960,
    #                                 column_spacing=100,
    #                                 data_row_max_height=41,
    #                                 columns=[
    #                                     ft.DataColumn(ft.Text(value="Código")),
    #                                     ft.DataColumn(ft.Text(value="Tipo")),
    #                                     ft.DataColumn(ft.Text(value="Ações"))
                                        
    #                                 ],
    #                                 rows=[
    #                                     ft.DataRow(
    #                                         cells=[
    #                                             ft.DataCell(
    #                                                 ft.Text(
    #                                                     value="111"
    #                                                 )
    #                                             ),
    #                                             ft.DataCell(
    #                                                 ft.Text(
    #                                                     value="Tipo"
    #                                                 )
    #                                             ),
    #                                             ft.DataCell(
    #                                                 ft.Row(
    #                                                     controls=[
    #                                                         ft.ElevatedButton(
    #                                                             text=".",
    #                                                             icon=ft.icons.EDIT,
    #                                                             width=50,
                                                    
    #                                                         ),
    #                                                         ft.ElevatedButton(
    #                                                             text=".",
    #                                                             icon=ft.icons.DELETE,
    #                                                             width=50
    #                                                         )
    #                                                     ]
    #                                                 )
                                                    
    #                                             )
    #                                         ]
    #                                     )
                                        
    #                                 ]
                                
                                    
    #                             )
    #                         ]
    #                     ),
    #                 ],
    #                 expand=True
    #             ),
                
    #         ),
    #         actions=[
    #             ft.TextButton("Fechar", on_click=fechar_popup),
    #             ft.ElevatedButton(
    #                 text="Salvar",
    #                 style=ft.ButtonStyle(
    #                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                     bgcolor=ft.colors.BLUE,
    #                     color=ft.colors.WHITE
    #                 ), on_click=salvar_produto),
    #         ]
    #     )
        
    #     page.dialog.open = True
    #     page.update()
               
    # def editar_tipo(e):
    #     fechar_popup(e)
        
    # def deletar_tipo(e):
    #     fechar_popup(e)
        
    # def adicionar_produto(e):
    #     global tipo_carne_dropdown
        
    #     tipo_carne_dropdown = ft.Dropdown(
    #         label="Tipo de Carne",
      
    #         border_radius=ft.border_radius.all(2),
    #         bgcolor=ft.colors.GREY_100,
    #         color=ft.colors.BLUE,                                                           
    #         border_width=0,
    #         options=[
    #             ft.dropdown.Option("Bovina")
    #         ]
    #     )
        
    #     page.dialog = ft.AlertDialog(             
    #         modal=True,
    #         # content_padding=30,
    #         title=ft.Text(value="Cadastro de Produto"),
    #         elevation=0,
    #         shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            

    #         content= ft.Container(
    #             expand=True,
    #             width=960,
    #             height=500,     
                
    #             margin=ft.margin.Margin(left=0, top=15, right=0, bottom=30),
    #             content=ft.Column(
    #                 controls = [
    #                     ft.Tabs(
    #                         scrollable=True,
    #                         tabs=[                                
    #                             ft.Tab(
    #                                 text="Produto",                                    
    #                                 content=ft.Container(
    #                                         margin=ft.margin.Margin(left=0, top=30, right=0, bottom=30),                                                                                                   
    #                                         content=ft.Column(
    #                                                 controls=[
    #                                                     ft.Row(
    #                                                         spacing=15,
    #                                                         controls=[
    #                                                             tipo_carne_dropdown, 
    #                                                             ft.ElevatedButton(
    #                                                                 text="Tipo", 
    #                                                                 icon=ft.icons.ADD, 
    #                                                                 on_click=adicionar_tipo,
    #                                                                 style=ft.ButtonStyle(
    #                                                                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                                                                     bgcolor=ft.colors.BLUE,
    #                                                                     color=ft.colors.WHITE
    #                                                                 )
    #                                                             )
    #                                                         ]
    #                                                     ),
    #                                                     ft.Row(
    #                                                         controls=[
    #                                                             ft.TextField(
    #                                                                 label="Codigo", 
                                                                    
    #                                                                 width=150,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=0,
    #                                                             ),
    #                                                             ft.TextField(
    #                                                                 label="Corte", 
                                                                    
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=0,
    #                                                             ),                                                       
    #                                                         ]                                                    
    #                                                     ),
    #                                                     ft.Row(
    #                                                         controls=[
    #                                                             ft.TextField(
    #                                                                     label="Codigo de Barras",
                                                                        
    #                                                                     width=150,
    #                                                                     border_radius=ft.border_radius.all(3),
                                                                        
    #                                                                     bgcolor=ft.colors.GREY_100,
    #                                                                     color=ft.colors.BLUE,
    #                                                                     hover_color=ft.colors.GREY_100,
    #                                                                     border_width=0,
    #                                                             ),                                                     
                                                
    #                                                             ft.TextField(
    #                                                                     label="Porção por Embalagem", 
                                                                        
    #                                                                     expand=True,
    #                                                                     border_radius=ft.border_radius.all(2),
    #                                                                     bgcolor=ft.colors.GREY_100,
    #                                                                     color=ft.colors.BLUE,
    #                                                                     hover_color=ft.colors.GREY_100,
    #                                                                     border_width=0,
    #                                                             ),
    #                                                             ft.TextField(
    #                                                                     label="Porção", 
                                                                        
    #                                                                     expand=True,
    #                                                                     border_radius=ft.border_radius.all(2),
    #                                                                     bgcolor=ft.colors.GREY_100,
    #                                                                     color=ft.colors.BLUE,
    #                                                                     hover_color=ft.colors.GREY_100,
    #                                                                     border_width=0,
    #                                                             ),
    #                                                         ]
                                                            
    #                                                     ),                                  
                                                        
                                                        
    #                                                     ft.TextField(
    #                                                         label="Campo Adicional", 
    #                                                         multiline=True, 
    #                                                         expand=True, 
    #                                                         height=100,
    #                                                         border_radius=ft.border_radius.all(2),
    #                                                         bgcolor=ft.colors.GREY_100,
    #                                                         color=ft.colors.BLUE,
    #                                                         hover_color=ft.colors.GREY_100,
    #                                                         border_width=0,
    #                                                     )
    #                                                 ]   
    #                                             )
                                                                                                                    
                                        
    #                                 )                              
    #                             ),
    #                             ft.Tab(    
                                                               
    #                                 text="Nutricional",
    #                                 content=ft.Container(
    #                                     expand=True,
    #                                     margin=ft.margin.Margin(left=0, top=5, right=0, bottom=0), 
    #                                     content = ft.Column(
    #                                         controls=[
                                            
    #                                         ft.DataTable(
    #                                             column_spacing=100,
    #                                             divider_thickness=0,
    #                                             width=960,
    #                                             data_row_max_height=41,                            
                                
                                    
    #                                             columns=[
    #                                                 ft.DataColumn(ft.Text(value="", expand=True)),
    #                                                 ft.DataColumn(ft.Text(value="100 g",width=100, text_align=ft.TextAlign.CENTER)),
    #                                                 ft.DataColumn(ft.Text(value="000 g", width=100, text_align=ft.TextAlign.CENTER)),
    #                                                 ft.DataColumn(ft.Text(value="%VD*", width=100, text_align=ft.TextAlign.CENTER)),     
                                                    
    #                                             ],
    #                                             rows=[
    #                                                 ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Valor energético (kcal)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10),
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                        
                                                            
    #                                                     ]
    #                                                 ),
    #                                                 ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Carboidratos totais (g)")),
    #                                                       ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
    #                                                     ]
    #                                                 ),
    #                                                 ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Açúcares totais (g)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ]
    #                                                 ),
    #                                                 ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Açúcares adicionados (g)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ]
    #                                                 ),
    #                                                  ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Proteínas (g)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ]
    #                                                 ),
    #                                                  ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Gorduras totais (g)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ]
    #                                                 ),
    #                                                  ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Gorduras saturadas (g)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ]
    #                                                 ),
    #                                                  ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Fibra alimentar (g)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ]
    #                                                 ),
    #                                                  ft.DataRow(
    #                                                     cells=[
    #                                                         ft.DataCell(ft.Text(value="Sódio (mg)")),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
    #                                                         ft.DataCell(
    #                                                             ft.TextField(
    #                                                                 width=100,
    #                                                                 expand=True,
    #                                                                 border_radius=ft.border_radius.all(2),
    #                                                                 bgcolor=ft.colors.GREY_100,
    #                                                                 color=ft.colors.BLUE,
    #                                                                 hover_color=ft.colors.GREY_100,
    #                                                                 border_width=1,
    #                                                                 height=35,
    #                                                                 content_padding=ft.padding.all(10)
                                                                
    #                                                             )),
                                                            
                                                            
    #                                                     ],
                                        
    #                                                 ),                                    
                                                    
                                                    
    #                                             ],
    #                                             expand=1
    #                                         )
                                            
                                                                            
                                            
    #                                         ],
    #                                         expand=1
                                       
    #                                     )
                                        
                                        
    #                                 ),
                                    
    #                             )
    #                         ],
    #                         expand=1
    #                     ),                  
    #                 ],
    #                 expand=1
                    
    #             )
    #         ),
    #         actions=[
    #             ft.TextButton("Fechar", on_click=fechar_popup),
    #             ft.ElevatedButton(
    #                 text="Salvar",
    #                 style=ft.ButtonStyle(
    #                     shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
    #                     bgcolor=ft.colors.BLUE,
    #                     color=ft.colors.WHITE
    #                     ), on_click=salvar_produto),
    #         ]
    #     )
    #     page.dialog.open = True
    #     page.update()
        
    
    def show_only(container):
        print(f"Show only: {container.__class__.__name__}, id: {id(container)}")
        current_content[0] = container
        content_container.content = container
        page.update()
        
        
    home_container = home(page)
    empresa_container = empresa(page)
    produto_container = produto(page)
    tipo_container = tipo(page)
    banco_dados_container = banco_dados(page)
    etiquetas_container = etiquetas(page)
   

    # def show_only(container):
    #     home_container.visible = False
    #     empresa_container.visible = False
    #     produto_container.visible = False
    #     tipo_container.visible = False
    #     container.visible = True
    #     page.update()
    
    
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
        # actions=[                       
        #     ft.CircleAvatar(ft.icons.PERFI),
            
        # ]        
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
            # collapsed_text_color=ft.colors.RED,
            # text_color=ft.colors.RED,
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
            # collapsed_text_color=ft.colors.RED,
            # text_color=ft.colors.RED,
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(3)),
            controls=[
                ft.ListTile(title=ft.TextButton(text="Banco de Dados",on_click=lambda _: show_only(banco_dados_container))),
                ft.ListTile(title=ft.TextButton(text="Etiquetas",on_click=lambda _: show_only(etiquetas_container))),
                # ft.ListTile(title=ft.TextButton(text="Produto")),
                # ft.ListTile(title=ft.TextButton(text="Produto")),
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
                                    # empresa_container,
                                    # produto_container,
                                    # tipo_container,
                                    # banco_dados_container
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

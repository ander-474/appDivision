import flet as ft
from fractions import Fraction
from dataclasses import field

class AppDivision():
    def __init__(self, page: ft.Page):
        self.page= page
        self.page.title = "Division app"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.bgcolor = ft.Colors.BLUE_GREY_800
        self.page.window.width = 650


        self.numerador = ft.TextField(label="Introduce el numerador", )
        self.denominador = ft.TextField(label="Introduce el denominador")
        self.result = ft.Container(
            alignment = ft.Alignment.CENTER,
            width=80,
            height=150,
            bgcolor=ft.Colors.PINK_400,
            padding=10,
            border_radius=10,
        )
        self.decimal_entrada = ft.Text(value="", style= ft.TextStyle(color=ft.Colors.WHITE, size=20))
        self.decimal_salida = ft.Text(value="", style= ft.TextStyle(color=ft.Colors.WHITE, size=20))
        self.limitador = ft.TextField(value="10", width=50)

        contenedor_principal = ft.Row(
            controls=[
                ft.Container(
                    alignment = ft.Alignment.CENTER,
                    width=300,
                    height=250,
                    bgcolor=ft.Colors.PINK_400,
                    padding=10,
                    border_radius=10,
                    content=ft.Column(
                        controls=[
                            self.numerador,
                            ft.Divider(),
                            self.denominador,
                            ft.Text(value="Limitador:"),
                            self.limitador
                        ]
                    )
                ),
                ft.Button(
                    "Calcular", 
                    on_click=self.calcular_division, 
                    bgcolor= ft.Colors.PURPLE_500
                ),
                self.result
            ]
        )
        self.log = ft.Text(value="")
        decimales = ft.Container(
            width=600,
            height=150,
            padding=ft.Padding.all(10),
            bgcolor=ft.Colors.PINK_400,
            border_radius=10,
            content=
            ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value="Expresiones en decimales",
                                style= ft.TextStyle(color=ft.Colors.WHITE, size=20)
                            ),
                            ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PRIMARY, size=40),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.decimal_entrada,
                            self.decimal_salida
                        ]
                    )
                ]
            )
        )
    
    
        self.page.add(contenedor_principal, self.log, decimales)

    def calcular_division(self, e):
        if self.denominador.value == "0":
            self.log.value = "Error: No se puede dividir entre cero"
            self.log.style = ft.TextStyle(color=ft.Colors.RED_500, size=20)

        result = int(self.numerador.value) / int(self.denominador.value)
        fraccion = Fraction(result).limit_denominator(int(self.limitador.value))
        
        self.result.content = ft.Column(
            alignment= ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value=fraccion.numerator, 
                            style= ft.TextStyle(color=ft.Colors.WHITE, size=20)
                        ),
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value=fraccion.denominator,
                            style= ft.TextStyle(color=ft.Colors.WHITE, size=20)
                        ),
                    ]
                )
                
            ]
        )
        self.decimal_entrada.value = f"{result:.3f}"
        self.decimal_salida.value = f"{(int(fraccion.numerator) / int(fraccion.denominator)):.3f}"
        self.page.update()



ft.run(AppDivision)
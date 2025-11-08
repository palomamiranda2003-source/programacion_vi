import flet as ft
import webbrowser

def mapa_view(page: ft.Page):

    def back_to_menu(e):
        page.go("/dashboard")

    def open_external_maps(e):
        url = "https://www.google.com/maps/dir/?api=1&destination=Paraguay&waypoints=Asuncion|Ciudad+del+Este"
        webbrowser.open(url)

    COLOR_FONDO = "#FFFFFF"
    COLOR_PRIMARIO = "#32BD18"
    COLOR_LIMA_SUAVE = "#F0FFF0"
    COLOR_AMARILLO = "#FFC700"
    COLOR_TEXTO = "#000000"
    COLOR_TEXTO_SEC = ft.Colors.BLACK54
    COLOR_TARJETA = "#F7F7F7"

    # Cabecera
    header = ft.Container(
        width=page.width,
        padding=ft.padding.symmetric(horizontal=20, vertical=20),
        bgcolor=COLOR_PRIMARIO,
        border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
        content=ft.Row(
            [
                ft.IconButton(ft.Icons.ARROW_BACK, icon_size=28, icon_color=ft.Colors.WHITE, on_click=back_to_menu),
                ft.Text("Mapa de Estaciones", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    # Tarjeta de mapa
    mapa_tarjeta = ft.Container(
        width=350,
        height=300,
        border_radius=15,
        bgcolor=COLOR_TARJETA,
        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(0, 3)),
        padding=ft.padding.all(15),
        content=ft.Column(
            [
                ft.Text("Mapa interactivo", size=18, weight=ft.FontWeight.BOLD, color=COLOR_TEXTO),
                ft.Icon(ft.Icons.MAP, size=80, color=COLOR_PRIMARIO),
                ft.ElevatedButton(
                    "Abrir en Google Maps",
                    on_click=open_external_maps,
                    bgcolor=COLOR_PRIMARIO,
                    color="white"
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

    # Lista de estaciones
    estaciones_tarjeta = ft.Container(
        width=350,
        border_radius=15,
        bgcolor=COLOR_TARJETA,
        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(0, 3)),
        padding=ft.padding.all(15),
        content=ft.Column(
            [
                ft.Text("Estaciones cercanas:", size=18, weight=ft.FontWeight.BOLD, color=COLOR_TEXTO),
                ft.ListView(
                    expand=False,
                    controls=[
                        ft.Text("🔋 Estación 1 - Asunción", color=COLOR_PRIMARIO),
                        ft.Text("🔋 Estación 2 - Ciudad del Este", color=COLOR_PRIMARIO),
                    ],
                    spacing=5
                ),
            ],
            spacing=10
        )
    )

    # Contenido scrollable
    contenido = ft.ListView(
        padding=ft.padding.symmetric(vertical=20),
        spacing=20,
        controls=[
            header,
            ft.Row([mapa_tarjeta], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([estaciones_tarjeta], alignment=ft.MainAxisAlignment.CENTER),
        ]
    )

    return ft.View(
        "/mapa",
        [
            ft.Container(
                expand=True,
                bgcolor=COLOR_FONDO,
                content=contenido
            )
        ],
    )

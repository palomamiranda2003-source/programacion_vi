import flet as ft
import webbrowser

def mapa_view(page: ft.Page):

    def back_to_menu(e):
        page.go("/dashboard")

    def open_external_maps(e):
        url = "https://www.google.com/maps/dir/?api=1&destination=Paraguay&waypoints=Asuncion|Ciudad+del+Este"
        webbrowser.open(url)

    # Contenido de la vista con scroll
    contenido = ft.ListView(
        padding=ft.padding.all(15),
        spacing=20,
        controls=[
            # Cabecera
            ft.Row(
                [
                    ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        icon_size=30,
                        icon_color="white",
                        on_click=back_to_menu
                    ),
                    ft.Text(
                        "Mapa de Estaciones",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color="#22FF00"
                    ),
                ],
                alignment=ft.MainAxisAlignment.START
            ),

            # “Mapa” o placeholder
            ft.Container(
                width=350,
                height=300,
                border_radius=15,
                bgcolor="#1c1c1e",
                padding=ft.padding.all(10),
                content=ft.Column(
                    [
                        ft.Text("Mapa interactivo", color="white", size=18),
                        ft.Icon(ft.Icons.MAP, size=80, color="#22FF00"),
                        ft.ElevatedButton(
                            "Abrir en Google Maps",
                            on_click=open_external_maps,
                            bgcolor="#22FF00",
                            color="black",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),

            # Lista de estaciones
            ft.Column(
                [
                    ft.Text("Estaciones cercanas:", color="white", size=18, weight=ft.FontWeight.BOLD),
                    ft.ListView(
                        expand=False,
                        controls=[
                            ft.Text("🔋 Estación 1 - Asunción", color="#7EE26C"),
                            ft.Text("🔋 Estación 2 - Ciudad del Este", color="#7EE26C"),
                        ],
                    ),
                ]
            ),
        ]
    )

    return ft.View(
        "/mapa",
        [
            ft.Container(
                expand=True,
                bgcolor="#01040F",
                content=contenido
            )
        ],
    )

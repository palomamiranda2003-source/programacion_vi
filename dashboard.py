import flet as ft
import webbrowser

def main_menu_view(page: ft.Page):
    COLOR_PRIMARIO = "#32BD18"
    COLOR_LIMA = "#7EE26C"
    COLOR_AMARILLO = "#FFC700"
    COLOR_FONDO = "#FFFFFF"
    COLOR_GRIS_BORDE = "#E0E0E0"

    page.bgcolor = COLOR_FONDO


    def open_maps(e):
        page.go("/mapa")

    def open_qr(e):
        webbrowser.open("https://example.com/qr-payment")

    def open_profile(e):
        page.go("/perfil")

    def go_login(e):
        page.go("/")

    header = ft.Container(
        width=page.width,
        padding=ft.padding.symmetric(horizontal=20, vertical=50),
        bgcolor=COLOR_PRIMARIO,
        border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
        content=ft.Column(
            [
                ft.Text("EcoCharge", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("Energía limpia para tu viaje", size=14, color=ft.Colors.WHITE70),
            ],
            spacing=3
        )
    )

    puntos_carga = ft.Container(
        width=350,
        height=140,
        border_radius=15,
        bgcolor=COLOR_FONDO,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 2),
        ),
        padding=ft.padding.all(15),
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Icon(ft.Icons.LOCATION_ON, size=30, color=COLOR_FONDO),
                    width=60,
                    height=60,
                    border_radius=30,
                    bgcolor=COLOR_AMARILLO,
                    alignment=ft.alignment.center,
                ),
                ft.Text("Puntos de Carga", color=ft.Colors.BLACK, size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Encuentra estaciones cercanas", color=ft.Colors.BLACK54, size=14),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4
        ),
        on_click=open_maps
    )

    bateria_porcentaje = 68
    autonomia_km = 245

    estado_vehiculo = ft.Container(
        width=350,
        border_radius=15,
        bgcolor=COLOR_FONDO,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 2),
        ),
        padding=15,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.FLASH_ON_OUTLINED, color=COLOR_PRIMARIO),
                        ft.Text("Estado del Vehículo", color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),

                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),

                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Row(
                                    [
                                        ft.Text("Batería", color=ft.Colors.BLACK, size=14)
                                    ],
                                    spacing=5
                                ),
                                ft.Text(f"{bateria_porcentaje}%", color=ft.Colors.BLACK, size=24, weight=ft.FontWeight.BOLD),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Container(
                            ft.ProgressBar(value=bateria_porcentaje / 100, bgcolor=COLOR_GRIS_BORDE, color=COLOR_LIMA, width=320, height=10),
                            margin=ft.margin.only(top=5, bottom=5)
                        ),
                    ],
                    spacing=0
                ),

                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),

                ft.Container(
                    bgcolor=COLOR_LIMA + "33",
                    border_radius=10,
                    padding=ft.padding.symmetric(vertical=10, horizontal=15),
                    content=ft.Row(
                        [
                            ft.Text("Autonomía restante", color=ft.Colors.BLACK, size=16),
                            ft.Text(f"{autonomia_km}", color=ft.Colors.BLACK, size=24, weight=ft.FontWeight.BOLD),
                            ft.Text("kilómetros", color=ft.Colors.BLACK54, size=16),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            ],
            spacing=8,
        )
    )

    tarifa_rapida = ft.Container(
        expand=True,
        height=180,
        border_radius=15,
        bgcolor=COLOR_AMARILLO,
        padding=15,
        content=ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.FLASH_ON, color=ft.Colors.BLACK), ft.Text("Rápida", color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)], spacing=5),
                ft.Text("$8", color=ft.Colors.BLACK, size=30, weight=ft.FontWeight.BOLD),
                ft.Text("por hora", color=ft.Colors.BLACK87, size=14),
                ft.Container(
                    ft.Text("~80% en 30 min", color=ft.Colors.BLACK, size=12),
                    padding=ft.padding.symmetric(horizontal=5, vertical=2),
                    bgcolor=ft.Colors.BLACK12,
                    border_radius=5
                )
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    tarifa_lenta = ft.Container(
        expand=True,
        height=180,
        border_radius=15,
        bgcolor=COLOR_LIMA,
        padding=15,
        content=ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.WATCH_LATER_OUTLINED, color=ft.Colors.BLACK), ft.Text("Lenta", color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD)], spacing=5),
                ft.Text("$4", color=ft.Colors.BLACK, size=30, weight=ft.FontWeight.BOLD),
                ft.Text("por hora", color=ft.Colors.BLACK87, size=14),
                ft.Container(
                    ft.Text("100% en 4 horas", color=ft.Colors.BLACK, size=12),
                    padding=ft.padding.symmetric(horizontal=5, vertical=2),
                    bgcolor=ft.Colors.BLACK12,
                    border_radius=5
                )
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    tarifas_carga = ft.Container(
        width=350,
        padding=ft.padding.all(15),
        content=ft.Column(
            [
                ft.Text("Tarifas de Carga", color=ft.Colors.BLACK, size=18, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        tarifa_rapida,
                        ft.VerticalDivider(width=10, color=ft.Colors.TRANSPARENT),
                        tarifa_lenta,
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=10
        )
    )

    co2_ahorrado = ft.Container(
        width=350,
        padding=ft.padding.only(left=15, right=15, top=5, bottom=20),
        content=ft.Row(
            [
                ft.Icon(ft.Icons.SPA_OUTLINED, color=COLOR_PRIMARIO, size=30),
                ft.Text("CO₂ ahorrado este mes: ", color=ft.Colors.BLACK, size=16),
                ft.Text("142 kg", color=ft.Colors.BLACK, size=20, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    nav_bar = ft.Container(
        width=page.width,
        height=70,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(top=ft.border.BorderSide(1, COLOR_GRIS_BORDE)),
        padding=ft.padding.symmetric(horizontal=30, vertical=5),
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.IconButton(ft.Icons.MENU_OPEN, icon_size=28, icon_color=ft.Colors.BLACK54),
                        ft.Text("Menú", color=ft.Colors.BLACK54, size=12)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                ),
                ft.Container(
                    content=ft.IconButton(
                        ft.Icons.QR_CODE_2,
                        icon_size=35,
                        on_click=open_qr,
                        icon_color=ft.Colors.BLACK,
                        tooltip="Pagar con QR"
                    ),
                    width=60,
                    height=60,
                    border_radius=30,
                    bgcolor=COLOR_AMARILLO,
                    alignment=ft.alignment.center,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=5,
                        color=ft.Colors.BLACK12,
                        offset=ft.Offset(0, 2),
                    )
                ),
                ft.Column(
                    [
                        ft.IconButton(ft.Icons.PERSON_OUTLINE, icon_size=28, on_click=open_profile, icon_color=ft.Colors.BLACK54),
                        ft.Text("Perfil", color=ft.Colors.BLACK54, size=12)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )

    scrollable_content = ft.Container(
        expand=True,
        bgcolor=COLOR_FONDO,
        content=ft.ListView(
            controls=[
                header,
                ft.Row([puntos_carga], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([estado_vehiculo], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([tarifas_carga], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([co2_ahorrado], alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=15,
            padding=ft.padding.only(bottom=0, top=10),
        ),
    )

    return ft.View(
        "/menu",
        [
            scrollable_content,

            ft.Container(
                content=nav_bar,
                alignment=ft.alignment.bottom_center,
            )
        ],
        bgcolor=COLOR_FONDO,
        padding=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH
    )
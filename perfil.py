import flet as ft
# import webbrowser

COLOR_FONDO = ft.Colors.WHITE
COLOR_PRIMARIO_VERDE = "#32BD18"
COLOR_VERDE_CLARO_HEADER = "#6CCF5C"
COLOR_LIMA_SUAVE = "#F0FFF0"
COLOR_AMARILLO_SUAVE = "#FFFDE7"
COLOR_ICONO = COLOR_PRIMARIO_VERDE
COLOR_AVATAR = "#7EE26C"
COLOR_GRIS_BORDE = "#E0E0E0"
COLOR_TEXTO_GRIS = ft.Colors.GREY_700
COLOR_CERRAR_SESION = ft.Colors.RED_500
COLOR_AMARILLO_QR = "#FFC700"


def create_action_tile(icon, title, subtitle, on_click_handler=None, icon_color=COLOR_AVATAR, title_color=ft.Colors.BLACK, subtitle_color=COLOR_TEXTO_GRIS):
    list_tile = ft.ListTile(
        leading=ft.Icon(icon, color=icon_color),
        title=ft.Text(title, color=title_color, weight=ft.FontWeight.BOLD),
        subtitle=ft.Text(subtitle, color=subtitle_color),
        trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=16, color=ft.Colors.GREY_400),
        on_click=on_click_handler,
        content_padding=ft.padding.only(left=5),
        min_vertical_padding=15
    )
    return ft.Container(
        content=list_tile,
        border=ft.border.only(bottom=ft.BorderSide(1, COLOR_GRIS_BORDE)),
    )

def create_stat_block(value, label, background_color, flex_weight=1):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(value, size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text(label, color=COLOR_TEXTO_GRIS, size=14, text_align=ft.TextAlign.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        expand=flex_weight,
        height=100,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
        bgcolor=background_color,
        border_radius=ft.border_radius.all(15),
        shadow=ft.BoxShadow(
            blur_radius=5,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 3)
        )
    )

def perfil_view(page: ft.Page):

    def open_dashboard(e):
        page.snack_bar = ft.SnackBar(ft.Text("Navegando al Dashboard (Menú)..."), bgcolor=COLOR_PRIMARIO_VERDE)
        page.snack_bar.open = True
        page.update()
        page.go("/dashboard")

    def open_qr(e):
        page.snack_bar = ft.SnackBar(ft.Text("Navegando al Escáner QR..."), bgcolor=COLOR_PRIMARIO_VERDE)
        page.snack_bar.open = True
        page.update()
        page.go("/qr")

    def open_profile(e):
        page.snack_bar = ft.SnackBar(ft.Text("Ya estás en tu Perfil."), bgcolor=COLOR_PRIMARIO_VERDE)
        page.snack_bar.open = True
        page.update()

    def editar_perfil(e):
        page.snack_bar = ft.SnackBar(ft.Text("Editar perfil aún no implementado"), bgcolor=COLOR_PRIMARIO_VERDE)
        page.snack_bar.open = True
        page.update()

    def cerrar_sesion(e):
        page.snack_bar = ft.SnackBar(ft.Text("Cerrando sesión..."), bgcolor=COLOR_CERRAR_SESION)
        page.snack_bar.open = True
        page.update()
        page.go("/")

    header = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(width=35, height=35),
                        ft.Text(
                            "Mi Perfil",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Container(
                            content=ft.Icon(ft.Icons.EDIT_OUTLINED, color=ft.Colors.WHITE, size=20),
                            alignment=ft.alignment.center,
                            width=35,
                            height=35,
                            border_radius=ft.border_radius.all(10),
                            bgcolor=ft.Colors.WHITE24,
                            on_click=editar_perfil,
                            tooltip="Editar Perfil"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=30),

                ft.Container(height=45),
            ]
        ),
        padding=ft.padding.only(left=25, right=25, top=20),

        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[COLOR_VERDE_CLARO_HEADER, COLOR_PRIMARIO_VERDE],
            stops=[0.0, 1.0],
        ),
        width=ft.Container.width,
        height=200,
        border_radius=ft.border_radius.only(bottom_left=30, bottom_right=30)
    )

    card_content = ft.Container(
        content=ft.Column(
            [
                ft.Column(
                    [
                        ft.CircleAvatar(
                            content=ft.Icon(ft.Icons.PERSON, size=50, color=ft.Colors.WHITE),
                            radius=40,
                            bgcolor=COLOR_AVATAR
                        ),
                        ft.Text("Paloma Quintana",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK),
                        ft.Text("paloma@example.com",
                                size=14,
                                color=COLOR_TEXTO_GRIS),
                        ft.Row([
                            ft.Icon(ft.Icons.DIRECTIONS_CAR_FILLED, size=16, color=COLOR_TEXTO_GRIS),
                            ft.Text("Usuario Eco", size=14, color=COLOR_TEXTO_GRIS)
                        ], spacing=5)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                ),

                ft.Container(height=20),

                ft.Column(
                    [
                        ft.Text("Información Personal", color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD),
                        ft.Container(height=10),
                        create_action_tile(ft.Icons.PHONE, "Teléfono", "+595 123 456 789", editar_perfil),
                        create_action_tile(ft.Icons.EMAIL, "Correo electrónico", "paloma@example.com", editar_perfil),
                        create_action_tile(ft.Icons.DIRECTIONS_CAR, "Vehículo", "EcoStar Model X", editar_perfil),
                        create_action_tile(ft.Icons.CALENDAR_TODAY, "Miembro desde", "Enero 2024", editar_perfil, icon_color=COLOR_AVATAR, subtitle_color=COLOR_TEXTO_GRIS),
                    ],
                    spacing=0,
                ),

                ft.Container(height=20),

                ft.Text("Estadísticas", color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
                ft.Row(
                    [
                        create_stat_block("12", "Recargas totales", COLOR_LIMA_SUAVE),
                        ft.Container(width=10),
                        create_stat_block("345 km", "Kilómetros recorridos", COLOR_AMARILLO_SUAVE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                ft.Container(height=20),

                ft.Text("Opciones", color=ft.Colors.BLACK, size=16, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
                ft.Column(
                    [
                        create_action_tile(ft.Icons.HISTORY, "Historial de pagos", "Revisa tus transacciones", open_dashboard),
                        create_action_tile(ft.Icons.PAYMENT, "Métodos de pago", "Administra tus tarjetas", open_dashboard),
                        create_action_tile(ft.Icons.SETTINGS, "Configuración", "Ajustes de la aplicación", open_dashboard),
                        create_action_tile(ft.Icons.LOGOUT, "Cerrar sesión", "Finaliza tu sesión actual", cerrar_sesion, icon_color=COLOR_CERRAR_SESION, title_color=COLOR_CERRAR_SESION, subtitle_color=COLOR_TEXTO_GRIS),
                    ],
                    spacing=0,
                ),

                ft.Container(height=90)
            ]
        ),
        margin=ft.margin.only(top=-70, left=20, right=20),
        padding=ft.padding.all(25),
        bgcolor=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(20),
        shadow=ft.BoxShadow(
            blur_radius=10,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 5)
        )
    )

    nav_bar = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(top=ft.border.BorderSide(1, COLOR_GRIS_BORDE)),
        padding=ft.padding.symmetric(horizontal=30, vertical=5),
        height=70,
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.IconButton(ft.Icons.MENU_OPEN, icon_size=28, icon_color=ft.Colors.BLACK54, on_click=open_dashboard),
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
                    bgcolor=COLOR_AMARILLO_QR,
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
                        ft.IconButton(ft.Icons.PERSON, icon_size=28, on_click=open_profile, icon_color=COLOR_PRIMARIO_VERDE),
                        ft.Text("Perfil", color=COLOR_PRIMARIO_VERDE, size=12, weight=ft.FontWeight.BOLD)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )


    return ft.View(
        "/perfil",
        [
            ft.Stack(
                [
                    header,

                    ft.ListView(
                        controls=[
                            ft.Container(height=180),
                            card_content,
                        ],
                        expand=True,
                        padding=ft.padding.only(top=0),
                        spacing=0,
                    )
                ],
                expand=True,
            ),
            nav_bar
        ],
        bgcolor=COLOR_FONDO,
        padding=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH
    )

def main(page: ft.Page):
    page.title = "Perfil EcoCharge"
    page.vertical_alignment = ft.CrossAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = COLOR_FONDO

    def route_change(route):
        page.views.clear()

        if page.route == "/perfil":
            page.views.append(perfil_view(page))
        elif page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        ft.AppBar(title=ft.Text("Dashboard (Menú)"), bgcolor=COLOR_PRIMARIO_VERDE),
                        ft.Text("Contenido del Dashboard"),
                    ],
                    bgcolor=COLOR_FONDO
                )
            )
        elif page.route == "/qr":
            page.views.append(
                ft.View(
                    "/qr",
                    [
                        ft.AppBar(title=ft.Text("Escáner QR"), bgcolor=COLOR_PRIMARIO_VERDE),
                        ft.Text("Vista de Escaneo QR"),
                    ],
                    bgcolor=COLOR_FONDO
                )
            )
        else:
            page.views.append(perfil_view(page))

        page.update()

    page.on_route_change = route_change
    page.go("/perfil")

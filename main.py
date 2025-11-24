import flet as ft
from login import LoginView
from dashboard import HomeView
from perfil import ProfileView
from qr_view import QRView
from bottom_nav import BottomNav
from mapa import MapView


def main(page: ft.Page):
    page.title = "EcoCharge"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window.width = 430
    page.window.height = 812
    page.window_resizable = False

    # Estado de la aplicación
    current_view = {"value": "home"}
    is_logged_in = {"value": False}
    logged_user_data = {"value": None}  # 🔹 Contendrá datos del usuario logeado

    # Containers principales
    main_content = ft.Container()
    bottom_navigation = ft.Container()

    # 🔹 on_login recibe datos del usuario
    def on_login_success(user_data):
        logged_user_data["value"] = user_data
        is_logged_in["value"] = True
        update_view()

    def on_view_change(view_name):
        current_view["value"] = view_name
        update_view()

    def logout(e=None):
        is_logged_in["value"] = False
        logged_user_data["value"] = None  # 🔹 Limpiamos datos al cerrar sesión
        update_view()

    def on_navigate_to_map():
        current_view["value"] = "map"
        update_view()

    def _station_item(city, address, availability, distance):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.LOCATION_ON, size=16, color="#10b981"),
                            ft.Text(city, size=14, weight=ft.FontWeight.W_600, expand=True),
                            ft.Text(distance, size=12, color="#6b7280"),
                        ],
                        spacing=8,
                    ),
                    ft.Text(address, size=12, color="#6b7280"),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.BOLT, size=12, color="#10b981"),
                            ft.Text(f"{availability} disponibles", size=12, color="#6b7280"),
                        ],
                        spacing=4,
                    ),
                ],
                spacing=4,
            ),
            bgcolor="#f0fdf4",
            border_radius=8,
            padding=12,
            border=ft.border.all(1, "#d1fae5"),
        )

    def update_view():
        page.clean()

        if not is_logged_in["value"]:
            # Pantalla de login
            page.add(LoginView(on_login=on_login_success))
        else:
            # Mostrar vista correspondiente
            if current_view["value"] == "profile":
                main_content.content = ProfileView(
                    on_logout=logout,
                    user_data=logged_user_data["value"]  # 🔹 Pasamos datos del usuario
                )
            elif current_view["value"] == "map":
                main_content.content = MapView(on_back=lambda e: on_view_change("home"))
            elif current_view["value"] == "qr":
                main_content.content = QRView()
            else:  # home
                main_content.content = HomeView(on_navigate_to_map=on_navigate_to_map)

            # Navegación inferior
            bottom_navigation.content = BottomNav(
                current_view=current_view["value"],
                on_view_change=on_view_change
            )

            # App container (teléfono)
            app_container = ft.Container(
                content=ft.Column([ft.Container(content=main_content, expand=True), bottom_navigation], spacing=0),
                width=430,
                height=812,
                bgcolor=ft.Colors.WHITE,
                border_radius=24,
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=30, color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)),
            )

            # Fondo general
            wrapper = ft.Container(
                content=app_container,
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#ecfdf5", "#f7fee7"],
                ),
                expand=True,
            )

            page.add(wrapper)

        page.update()

    # Inicializamos la app
    update_view()

if __name__ == "__main__":
    ft.app(target=main)

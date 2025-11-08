import flet as ft
from login import LoginView
from dashboard import main_menu_view
from perfil import perfil_view
from mapa import mapa_view

def main(page: ft.Page):
    page.title = "EcoCharge"
    page.window.width = 430
    page.window.height = 812
    page.window.resizable = False
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE

    user_data = {"value": None}

    # --- Callback login ---
    def on_login_success(data):
        user_data["value"] = data
        page.views.clear()
        page.go("/dashboard")  # redirige al dashboard

    # --- Manejar rutas ---
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(ft.View("/", controls=[LoginView(on_login=on_login_success)]))
        elif page.route == "/dashboard":
            page.views.append(main_menu_view(page))
        elif page.route == "/perfil":
            page.views.append(perfil_view(page))
        elif page.route == "/qr":
            # Vista QR simple de ejemplo
            page.views.append(
                ft.View(
                    "/qr",
                    [ft.AppBar(title=ft.Text("Escáner QR")), ft.Text("Aquí irá el QR Scanner")],
                    bgcolor=ft.Colors.WHITE
                )
            )
        elif page.route == "/mapa":
            page.views.append(mapa_view(page))
        page.update()

    page.on_route_change = route_change

    # Inicializar login
    page.views.append(ft.View("/", controls=[LoginView(on_login=on_login_success)]))
    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)

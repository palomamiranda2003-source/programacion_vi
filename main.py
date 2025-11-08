import flet as ft
from login import LoginView
from dashboard import main_menu_view
from perfil import perfil_view
from mapa import mapa_view

def main(page: ft.Page):
    page.title = "EcoCharge"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window.width = 430
    page.window.height = 812
    page.window.resizable = False

    # Estado
    user_data = {"value": None}

    # --- Callback login ---
    def on_login_success(data):
        user_data["value"] = data
        # Limpiar vistas y agregar dashboard
        page.views.clear()
        page.views.append(main_menu_view(page))
        page.go("/menu")

    # --- Manejar rutas ---
    def route_change(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(
                ft.View("/", controls=[LoginView(on_login=on_login_success)])
            )
        elif page.route == "/menu":
            page.views.clear()
            page.views.append(main_menu_view(page))
        elif page.route == "/perfil":
            page.views.clear()
            page.views.append(perfil_view(page))
        elif page.route == "/mapa":
            page.views.clear()
            page.views.append(mapa_view(page))
        page.update()

    page.on_route_change = route_change

    # --- Inicializar login ---
    page.views.append(
        ft.View("/", controls=[LoginView(on_login=on_login_success)])
    )
    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)

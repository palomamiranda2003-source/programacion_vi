import flet as ft
from login import login_view
from dashboard import main_menu_view 
from perfil import perfil_view
from mapa import mapa_view

def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/dashboard":
            page.views.append(main_menu_view(page))
        elif page.route == "/mapa":
            page.views.append(mapa_view(page))
        elif page.route == "/perfil":
            page.views.append(perfil_view(page))
        page.update()

    page.on_route_change = route_change
    page.go("/")  # arranca en login

ft.app(target=main)

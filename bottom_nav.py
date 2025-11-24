import flet as ft

def BottomNav(current_view, on_view_change):
    def is_active(view):
        return view == current_view or (view == "home" and current_view == "menu")
    
    return ft.Container(
            content=ft.Row(
                [
                    # Menú Principal
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(
                                    ft.Icons.HOME,
                                    size=24,
                                    color="#10b981" if is_active("home") else "#9ca3af",
                                ),
                                ft.Text(
                                    "Inicio",
                                    size=12,
                                    color="#10b981" if is_active("home") else "#9ca3af",
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=4,
                        ),
                        on_click=lambda _: on_view_change("home"),
                        expand=True,
                        alignment=ft.alignment.center,
                        padding=8,
                    ),
                    
                    # QR
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Icon(
                                        ft.Icons.QR_CODE_SCANNER,
                                        size=28,
                                        color=ft.Colors.WHITE,
                                    ),
                                    width=56,
                                    height=56,
                                    border_radius=28,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_left,
                                        end=ft.alignment.bottom_right,
                                        colors=["#10b981", "#84cc16"],
                                    ),
                                    alignment=ft.alignment.center,
                                    shadow=ft.BoxShadow(
                                        spread_radius=0,
                                        blur_radius=12,
                                        color=ft.Colors.with_opacity(0.3, "#10b981"),
                                    ),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        on_click=lambda _: on_view_change("qr"),
                        expand=True,
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=-20),
                    ),
                    
                    # Perfil
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(
                                    ft.Icons.PERSON,
                                    size=24,
                                    color="#10b981" if is_active("profile") else "#9ca3af",
                                ),
                                ft.Text(
                                    "Perfil",
                                    size=12,
                                    color="#10b981" if is_active("profile") else "#9ca3af",
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=4,
                        ),
                        on_click=lambda _: on_view_change("profile"),
                        expand=True,
                        alignment=ft.alignment.center,
                        padding=8,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor=ft.Colors.WHITE,
            border=ft.border.only(top=ft.BorderSide(1, "#e5e7eb")),
            padding=ft.padding.only(left=8, right=8, top=8, bottom=16),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, -5),
            ),
        )

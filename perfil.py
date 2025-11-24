import flet as ft

def _info_row(icon, label, value):
    return ft.Container(
        content=ft.Row(
            [
                ft.Icon(icon, size=20, color="#6b7280"),
                ft.Column(
                    [
                        ft.Text(label, size=12, color="#9ca3af"),
                        ft.Text(value, size=14, color="#1f2937"),
                    ],
                    spacing=2,
                    expand=True,
                ),
            ],
            spacing=12,
        ),
        padding=ft.padding.symmetric(vertical=12),
        border=ft.border.only(bottom=ft.BorderSide(1, "#f3f4f6")),
    )

def _option_button(icon, text):
    return ft.Container(
        content=ft.Row(
            [
                ft.Icon(icon, size=20, color="#6b7280"),
                ft.Text(text, size=14, color="#1f2937", expand=True),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=20, color="#9ca3af"),
            ],
            spacing=12,
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        padding=16,
        margin=ft.margin.only(bottom=8),
        on_click=lambda _: None,
        ink=True,
    )

def ProfileView(on_logout=None, user_data=None):
    """
    user_data: diccionario con los datos del usuario logeado
    {
        "first_name": str,
        "last_name": str,
        "email": str,
        "phone": str,
        "city": str,
        "vehicle": str,
        "plan": str
    }
    """
    # Si no hay datos, usamos valores por defecto
    if user_data is None:
        user_data = {
            "first_name": "Usuario",
            "last_name": "",
            "email": "correo@ejemplo.com",
            "phone": "-",
            "city": "-",
            "vehicle": "-",
            "plan": "-"
        }

    full_name = f"{user_data['first_name']} {user_data['last_name']}".strip()

    return ft.Column(
        [
            # Header
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Icon(ft.Icons.PERSON, size=40, color=ft.Colors.WHITE),
                                        width=80,
                                        height=80,
                                        bgcolor="#10b981",
                                        border_radius=40,
                                        alignment=ft.alignment.center,
                                        border=ft.border.all(3, ft.Colors.WHITE),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Container(height=12),
                            ft.Text(
                                full_name,
                                size=24,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                user_data.get("email", ""),
                                size=14,
                                color="#d1fae5",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(left=24, right=24, top=48, bottom=32),
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=["#10b981", "#84cc16"],
                ),
            ),
            
            # Estadísticas (pueden seguir fijas o adaptarse si quieres luego)
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("156", size=24, weight=ft.FontWeight.BOLD, color="#10b981"),
                                    ft.Text("Cargas", size=12, color="#6b7280"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=4,
                            ),
                            expand=True,
                        ),
                        ft.Container(width=1, bgcolor="#e5e7eb", height=40),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("2.4t", size=24, weight=ft.FontWeight.BOLD, color="#10b981"),
                                    ft.Text("CO₂ ahorrado", size=12, color="#6b7280"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=4,
                            ),
                            expand=True,
                        ),
                        ft.Container(width=1, bgcolor="#e5e7eb", height=40),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("3.2k", size=24, weight=ft.FontWeight.BOLD, color="#10b981"),
                                    ft.Text("km recorridos", size=12, color="#6b7280"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=4,
                            ),
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                bgcolor=ft.Colors.WHITE,
                border_radius=16,
                padding=20,
                margin=ft.margin.only(left=24, right=24, top=-20, bottom=24),
                shadow=ft.BoxShadow(spread_radius=0, blur_radius=20, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
            ),
            
            # Información personal
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Información Personal", size=18, weight=ft.FontWeight.W_600, color="#1f2937"),
                        ft.Container(height=16),
                        
                        _info_row(ft.Icons.PHONE, "Teléfono", user_data.get("phone", "-")),
                        _info_row(ft.Icons.LOCATION_ON, "Ciudad", user_data.get("city", "-")),
                        _info_row(ft.Icons.ELECTRIC_CAR, "Vehículo", user_data.get("vehicle", "-")),
                        _info_row(ft.Icons.CREDIT_CARD, "Plan", user_data.get("plan", "-")),
                    ],
                ),
                padding=ft.padding.symmetric(horizontal=24),
                margin=ft.margin.only(bottom=24),
            ),
            
            # Opciones
            ft.Container(
                content=ft.Column(
                    [
                        _option_button(ft.Icons.HISTORY, "Historial de cargas"),
                        _option_button(ft.Icons.PAYMENT, "Métodos de pago"),
                        _option_button(ft.Icons.SETTINGS, "Configuración"),
                        _option_button(ft.Icons.HELP_OUTLINE, "Ayuda y soporte"),
                        
                        ft.Container(height=12),
                        
                        # Botón de cerrar sesión
                        ft.Container(
                            content=ft.TextButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.LOGOUT, color="#ef4444", size=20),
                                        ft.Text("Cerrar sesión", color="#ef4444", size=16),
                                    ],
                                    spacing=8,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                on_click=on_logout,
                            ),
                            bgcolor="#fef2f2",
                            border_radius=12,
                            padding=8,
                        ),
                    ],
                ),
                padding=ft.padding.symmetric(horizontal=24),
                margin=ft.margin.only(bottom=100),
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
    )

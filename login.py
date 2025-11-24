import flet as ft
from bd.users_db import verify_user  # función que verifica usuario y contraseña en DB

def LoginView(on_login):
    # Campos de input
    email_input = ft.TextField(
        label="Correo electrónico",
        hint_text="tu@email.com",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border_color="#d1d5db",
        focused_border_color="#10b981",
    )

    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINED,
        border_color="#d1d5db",
        focused_border_color="#10b981",
    )

    # Función para manejar login
    def handle_login(e):
        email = email_input.value
        password = password_input.value

        # 🔹 Verificamos el usuario y obtenemos los datos
        user_data = verify_user(email, password)

        if user_data:  # Si se devuelve un diccionario con los datos
            on_login(user_data)  # 🔹 Pasamos los datos al callback
        else:
            # Mostrar error
            email_input.error_text = "Usuario o contraseña incorrectos"
            email_input.update()
            password_input.update()

    # Estructura visual (igual que antes)
    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#10b981", "#84cc16"],
        ),
        content=ft.Column(
            [
                # Logo y título
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Text("⚡", size=80, color=ft.Colors.WHITE),
                                width=120,
                                height=120,
                                border_radius=60,
                                alignment=ft.alignment.center,
                                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
                            ),
                            ft.Container(height=20),
                            ft.Text(
                                "EcoCharge",
                                size=36,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Energía limpia para tu viaje",
                                size=14,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    margin=ft.margin.only(bottom=40),
                ),

                # Formulario
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Iniciar Sesión",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#1f2937",
                            ),
                            ft.Container(height=20),

                            email_input,
                            password_input,

                            ft.Container(height=10),

                            # Botón de login
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text("Iniciar Sesión", size=16),
                                    width=float("inf"),
                                    height=50,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                        bgcolor="#10b981",
                                    ),
                                    on_click=handle_login,  # llamamos a nuestra función
                                ),
                                margin=ft.margin.only(top=10),
                            ),

                            ft.Container(height=20),

                            # Registro
                            ft.Row(
                                [
                                    ft.Text("¿No tienes cuenta?", size=14, color="#6b7280"),
                                    ft.TextButton(
                                        "Regístrate",
                                        style=ft.ButtonStyle(color="#10b981"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                    ),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=20,
                    padding=30,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                    ),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=20,
    )

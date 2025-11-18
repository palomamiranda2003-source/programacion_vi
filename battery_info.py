import flet as ft

def BatteryInfo():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Estado del Vehículo",
                        size=20,
                        weight=ft.FontWeight.W_600,
                        color="#1f2937",
                    ),
                    ft.Container(height=16),
                    
                    # Batería
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.BATTERY_CHARGING_FULL,
                                    size=32,
                                    color="#10b981",
                                ),
                                width=56,
                                height=56,
                                bgcolor="#ecfdf5",
                                border_radius=28,
                                alignment=ft.alignment.center,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "Batería",
                                        size=14,
                                        color="#6b7280",
                                    ),
                                    ft.Text(
                                        "78%",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color="#1f2937",
                                    ),
                                ],
                                spacing=0,
                                expand=True,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "Autonomía",
                                        size=14,
                                        color="#6b7280",
                                    ),
                                    ft.Text(
                                        "312 km",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color="#1f2937",
                                    ),
                                ],
                                spacing=0,
                                expand=True,
                            ),
                        ],
                        spacing=16,
                    ),
                    
                    ft.Container(height=16),
                    
                    # Barra de progreso
                    ft.Container(
                        content=ft.ProgressBar(
                            value=0.78,
                            color="#10b981",
                            bgcolor="#d1fae5",
                            height=8,
                            border_radius=4,
                        ),
                    ),
                ],
            ),
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            padding=20,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
            ),
        )

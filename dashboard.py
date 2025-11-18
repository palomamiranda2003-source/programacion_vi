import flet as ft
from battery_info import BatteryInfo
from charging_pricing import ChargingPricing

def HomeView(on_navigate_to_map):
    return ft.Container(
        # Fondo degradado general
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#10b981", "#84cc16"],
        ),
        expand=True,
        content=ft.Column(
            [
                # Header
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "EcoCharge",
                                size=32,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.W_500,
                            ),
                            ft.Text(
                                "Energía limpia para tu viaje",
                                size=14,
                                color="#d1fae5",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(left=24, right=24, top=48, bottom=32),
                ),
                
                # Botón de encontrar puntos de carga
                ft.Container(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Icon(ft.Icons.LOCATION_ON, size=32, color=ft.Colors.WHITE),
                                    width=64,
                                    height=64,
                                    border_radius=32,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_left,
                                        end=ft.alignment.bottom_right,
                                        colors=["#fbbf24", "#eab308"],
                                    ),
                                    alignment=ft.alignment.center,
                                    shadow=ft.BoxShadow(
                                        spread_radius=0,
                                        blur_radius=10,
                                        color=ft.Colors.with_opacity(0.3, "#fbbf24"),
                                    ),
                                ),
                                ft.Container(height=12),
                                ft.Text(
                                    "Encontrar punto de carga",
                                    size=18,
                                    weight=ft.FontWeight.W_600,
                                    color="#1f2937",
                                ),
                                ft.Text(
                                    "Localiza estaciones cercanas",
                                    size=14,
                                    color="#6b7280",
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.Colors.WHITE,
                        border_radius=16,
                        padding=24,
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=20,
                            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                        ),
                        on_click=lambda _: on_navigate_to_map(),
                        ink=True,
                    ),
                    margin=ft.margin.only(left=24, right=24, top=-16, bottom=24),
                ),
                
                # Información de batería
                ft.Container(
                    content=BatteryInfo(),
                    padding=ft.padding.symmetric(horizontal=24),
                    margin=ft.margin.only(bottom=24),
                ),
                
                # Impacto ambiental
                ft.Container(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text("🌱", size=32),
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "CO₂ ahorrado este mes",
                                                    size=14,
                                                    color="#6b7280",
                                                ),
                                                ft.Text(
                                                    "142 kg",
                                                    size=18,
                                                    weight=ft.FontWeight.W_600,
                                                    color="#059669",
                                                ),
                                            ],
                                            spacing=2,
                                            expand=True,
                                        ),
                                    ],
                                    spacing=12,
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Text("🌳", size=18),
                                            ft.Text(
                                                "Es como si hubieras plantado un árbol",
                                                size=14,
                                                color="#059669",
                                                italic=True,
                                            ),
                                        ],
                                        spacing=8,
                                    ),
                                    margin=ft.margin.only(left=56, top=8),
                                ),
                            ],
                        ),
                        bgcolor="#ecfdf5",
                        border=ft.border.all(1, "#d1fae5"),
                        border_radius=16,
                        padding=16,
                    ),
                    padding=ft.padding.symmetric(horizontal=24),
                    margin=ft.margin.only(bottom=24),
                ),
                
                # Precios de carga
                ft.Container(
                    content=ChargingPricing(),
                    padding=ft.padding.symmetric(horizontal=24),
                    margin=ft.margin.only(bottom=100),
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=0,
        ),
    )

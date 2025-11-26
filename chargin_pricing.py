import flet as ft
from monitor.db_utils_monitor import get_charge_prices

def ChargingPricing():

    # Leer precios desde la base de datos ecocharge.db
    prices = get_charge_prices()

    fast_price = prices.get("fast", "—")
    slow_price = prices.get("normal", "—")

    return ft.Column(
        [
            ft.Text(
                "Cotizaciones de Carga",
                size=20,
                weight=ft.FontWeight.W_600,
                color="#1f2937",
            ),
            ft.Container(height=16),
            
            # --- CARGA RÁPIDA ---
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(ft.Icons.BOLT, size=24, color="#f59e0b"),
                            width=48,
                            height=48,
                            bgcolor="#fef3c7",
                            border_radius=24,
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Carga Rápida",
                                    size=16,
                                    weight=ft.FontWeight.W_600,
                                    color="#1f2937",
                                ),
                                ft.Text(
                                    "30 min - 80%",
                                    size=14,
                                    color="#6b7280",
                                ),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Text(
                            fast_price,
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="#f59e0b",
                        ),
                    ],
                    spacing=12,
                ),
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, "#fde68a"),
                border_radius=12,
                padding=16,
                margin=ft.margin.only(bottom=12),
            ),
            
            # --- CARGA LENTA ---
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(ft.Icons.POWER, size=24, color="#10b981"),
                            width=48,
                            height=48,
                            bgcolor="#d1fae5",
                            border_radius=24,
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Carga Lenta",
                                    size=16,
                                    weight=ft.FontWeight.W_600,
                                    color="#1f2937",
                                ),
                                ft.Text(
                                    "2-3 horas - 100%",
                                    size=14,
                                    color="#6b7280",
                                ),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.Text(
                            slow_price,
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="#10b981",
                        ),
                    ],
                    spacing=12,
                ),
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, "#a7f3d0"),
                border_radius=12,
                padding=16,
            ),
        ],
    )

import flet as ft

def _instruction_item(number, text):
    return ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        number,
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    width=28,
                    height=28,
                    bgcolor="#10b981",
                    border_radius=14,
                    alignment=ft.alignment.center,
                ),
                ft.Text(text, size=14, color="#4b5563", expand=True),
            ],
            spacing=12,
        ),
        margin=ft.margin.only(bottom=12),
    )


def QRView():
    return ft.Container(
        # 🌿 Fondo general en degradado verde
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#10b981", "#84cc16"],
        ),
        expand=True,
        content=ft.Column(
            [
                # Header (sin degradado)
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Código QR",
                                size=28,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                "Escanea para pagar tu carga",
                                size=14,
                                color="#d1fae5",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(left=24, right=24, top=48, bottom=32),
                ),
                
                # Contenido principal
                ft.Container(
                    content=ft.Column(
                        [
                            # Simulación de QR Code
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("📱", size=80),
                                        ft.Container(height=8),
                                        ft.Text(
                                            "Tu código QR",
                                            size=18,
                                            weight=ft.FontWeight.W_600,
                                            color="#1f2937",
                                        ),
                                        ft.Text(
                                            "ID: EC-2024-78945",
                                            size=14,
                                            color="#6b7280",
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                width=280,
                                height=280,
                                bgcolor=ft.Colors.WHITE,
                                border_radius=20,
                                border=ft.border.all(2, "#d1fae5"),
                                alignment=ft.alignment.center,
                                shadow=ft.BoxShadow(
                                    spread_radius=0,
                                    blur_radius=20,
                                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                                ),
                            ),
                            
                            ft.Container(height=32),
                            
                            # Instrucciones
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(
                                            "Cómo usar:",
                                            size=16,
                                            weight=ft.FontWeight.W_600,
                                            color="#1f2937",
                                        ),
                                        ft.Container(height=12),
                                        
                                        _instruction_item("1", "Acércate a una estación EcoCharge"),
                                        _instruction_item("2", "Escanea el código QR de la estación"),
                                        _instruction_item("3", "Selecciona el tipo de carga"),
                                        _instruction_item("4", "Confirma el pago"),
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
                            ),
                            
                            ft.Container(height=24),
                            
                            # Botón de escanear
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.Icons.QR_CODE_SCANNER, color=ft.Colors.WHITE),
                                            ft.Text("Abrir escáner", size=16, color=ft.Colors.WHITE),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8,
                                    ),
                                    width=float("inf"),
                                    height=56,
                                    style=ft.ButtonStyle(
                                        bgcolor="#16a34a",
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                    ),
                                ),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.all(24),
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=0,
        ),
    )

import flet as ft
from db_utils_monitor import get_charge_prices

def main(page: ft.Page):
    page.title = "Estación de Carga EcoCharge"
    page.window.width = 1100
    page.window.height = 750
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_900

    # Obtener precios desde la base de datos
    charge_prices = get_charge_prices()

    # Estado de la aplicación
    selected_charge_type = ft.Ref[str]()
    selected_charge_type.current = "fast"
    selected_payment = ft.Ref[str]()
    selected_payment.current = None
    current_step = ft.Ref[int]()
    current_step.current = 1

    # Estado para pantalla de carga
    loading_active = ft.Ref[bool]()
    loading_active.current = False
    loading_messages = [
        "La energía limpia impulsa tu camino.",
        "Reduciendo emisiones de CO₂ con cada carga.",
        "Optimizando tu carga para mayor eficiencia.",
        "EcoCharge: cada carga cuenta para el planeta.",
        "Cargando con energía sustentable y responsable."
    ]
    loading_index = ft.Ref[int]()
    loading_index.current = 0
    loading_timer = None  # se guardará el Timer si está activo

    def rotate_loading_message(e=None):
        """Cambia el mensaje de la pantalla de carga."""
        loading_index.current = (loading_index.current + 1) % len(loading_messages)
        page.update()

    def start_loading_screen():
        """Activa pantalla de carga usando threading.Timer (compatible con cualquier versión de Flet)."""
        import threading
        nonlocal loading_timer

        loading_active.current = True
        loading_index.current = 0

        def _rotate():
            if loading_active.current:
                rotate_loading_message()
                page.update()
                # Reprogramar el timer
                nonlocal loading_timer
                loading_timer = threading.Timer(5, _rotate)
                loading_timer.daemon = True
                loading_timer.start()

        # Iniciar el primer timer
        loading_timer = threading.Timer(5, _rotate)
        loading_timer.daemon = True
        loading_timer.start()

        page.update()

    def stop_loading_screen():
        """Detiene la pantalla de carga y el timer."""
        nonlocal loading_timer
        loading_active.current = False

        try:
            if loading_timer is not None:
                loading_timer.cancel()
        except Exception:
            pass

        loading_timer = None
        page.update()

    def charging_option(title, description, price, duration, charge_type, recommended=False):
        """Componente de opción de carga"""
        is_selected = selected_charge_type.current == charge_type

        def on_click(e):
            selected_charge_type.current = charge_type
            page.update()

        option_card = ft.Container(
            content=ft.Stack(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    title,
                                                    size=18,
                                                    weight=ft.FontWeight.W_600,
                                                    color=ft.Colors.GREEN_900,
                                                ),
                                                ft.Text(
                                                    description,
                                                    size=14,
                                                    color=ft.Colors.GREY_600,
                                                ),
                                            ],
                                            spacing=4,
                                            expand=True,
                                        ),
                                        ft.Container(
                                            content=ft.Icon(
                                                ft.Icons.CHECK,
                                                size=16,
                                                color=ft.Colors.WHITE,
                                            ) if is_selected else None,
                                            width=24,
                                            height=24,
                                            border_radius=12,
                                            border=ft.border.all(
                                                2,
                                                ft.Colors.GREEN_500 if is_selected else ft.Colors.GREY_300
                                            ),
                                            bgcolor=ft.Colors.GREEN_500 if is_selected else None,
                                            alignment=ft.alignment.center,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.Container(height=16),
                                ft.Column(
                                    [
                                        ft.Text(
                                            price,
                                            size=32,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.GREEN_700,
                                        ),
                                        ft.Text(
                                            duration,
                                            size=14,
                                            color=ft.Colors.GREY_500,
                                        ),
                                    ],
                                    spacing=2,
                                ),
                            ],
                            spacing=0,
                        ),
                        padding=24,
                        border_radius=16,
                        bgcolor=ft.Colors.GREEN_50 if is_selected else ft.Colors.WHITE,
                        border=ft.border.all(
                            2 if is_selected else 1,
                            ft.Colors.GREEN_500 if is_selected else ft.Colors.GREY_200
                        ),
                    ),
                ]
            ),
            on_click=on_click,
            ink=True,
        )

        return option_card

    def payment_method(icon, label, payment_type):
        """Componente de método de pago"""
        is_selected = selected_payment.current == payment_type

        def on_click(e):
            selected_payment.current = payment_type
            page.update()

        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            size=24,
                            color=ft.Colors.WHITE if is_selected else ft.Colors.GREY_600,
                        ),
                        width=48,
                        height=48,
                        border_radius=24,
                        bgcolor=ft.Colors.GREEN_500 if is_selected else ft.Colors.GREY_100,
                        alignment=ft.alignment.center,
                    ),
                    ft.Text(
                        label,
                        size=14,
                        color=ft.Colors.GREEN_700 if is_selected else ft.Colors.GREY_700,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
            ),
            padding=24,
            border_radius=12,
            bgcolor=ft.Colors.GREEN_50 if is_selected else ft.Colors.WHITE,
            border=ft.border.all(
                2 if is_selected else 1,
                ft.Colors.GREEN_500 if is_selected else ft.Colors.GREY_200
            ),
            on_click=on_click,
            ink=True,
        )

    def handle_continue(e):
        if current_step.current == 1 and selected_charge_type.current:
            current_step.current = 2
            selected_payment.current = None
            page.update()

    def handle_back(e):
        current_step.current = 1
        page.update()

    def handle_start_charging(e):
        # En vez de mostrar un diálogo simple, mostramos la pantalla de carga
        if selected_payment.current:
            start_loading_screen()

    def build_step_indicator():
        """Indicador de progreso de pasos"""
        return ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "1",
                                size=14,
                                color=ft.Colors.WHITE if current_step.current >= 1 else ft.Colors.GREY_500,
                            ),
                            width=32,
                            height=32,
                            border_radius=16,
                            bgcolor=ft.Colors.GREEN_500 if current_step.current >= 1 else ft.Colors.GREY_200,
                            alignment=ft.alignment.center,
                        ),
                        ft.Text(
                            "Tipo de carga",
                            size=14,
                            color=ft.Colors.GREEN_700 if current_step.current >= 1 else ft.Colors.GREY_500,
                        ),
                    ],
                    spacing=8,
                ),
                ft.Container(
                    content=ft.Container(
                        height=4,
                        bgcolor=ft.Colors.GREEN_500 if current_step.current >= 2 else ft.Colors.GREY_200,
                        border_radius=2,
                    ),
                    width=100,
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "2",
                                size=14,
                                color=ft.Colors.WHITE if current_step.current >= 2 else ft.Colors.GREY_500,
                            ),
                            width=32,
                            height=32,
                            border_radius=16,
                            bgcolor=ft.Colors.GREEN_500 if current_step.current >= 2 else ft.Colors.GREY_200,
                            alignment=ft.alignment.center,
                        ),
                        ft.Text(
                            "Método de pago",
                            size=14,
                            color=ft.Colors.GREEN_700 if current_step.current >= 2 else ft.Colors.GREY_500,
                        ),
                    ],
                    spacing=8,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=16,
        )

    def build_step_1():
        """Paso 1: Selección de tipo de carga"""
        return ft.Container(
            content=ft.Column(
                [
                    # Título
                    ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.BATTERY_CHARGING_FULL,
                                size=24,
                                color=ft.Colors.GREEN_600,
                            ),
                            ft.Text(
                                "Selecciona tu tipo de carga",
                                size=20,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.GREEN_900,
                            ),
                        ],
                        spacing=12,
                    ),
                    ft.Container(height=20),
                    # Opciones de carga
                    ft.Row(
                        [
                            ft.Container(
                                content=charging_option(
                                    "Carga Rápida",
                                    "Carga completa en menos tiempo",
                                    charge_prices["fast"],
                                    "20-30 minutos",
                                    "fast",
                                    recommended=True,
                                ),
                                expand=True,
                            ),
                            ft.Container(
                                content=charging_option(
                                    "Carga Lenta",
                                    "Carga económica y eficiente",
                                    charge_prices["normal"],
                                    "45-60 minutos",
                                    "normal",
                                ),
                                expand=True,
                            ),
                        ],
                        spacing=24,
                    ),
                    ft.Container(height=24),
                    # Botón continuar
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                content=ft.Row(
                                    [
                                        ft.Text("Continuar", size=16),
                                        ft.Icon(ft.Icons.ARROW_FORWARD, size=20),
                                    ],
                                    spacing=8,
                                ),
                                bgcolor=ft.Colors.GREEN_600,
                                color=ft.Colors.WHITE,
                                on_click=handle_continue,
                                style=ft.ButtonStyle(
                                    padding=ft.padding.symmetric(horizontal=32, vertical=20),
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            padding=32,
            bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
            border_radius=24,
            border=ft.border.all(1, ft.Colors.GREEN_100),
        )

    def build_loading_card():
        """Construye la tarjeta de la pantalla de carga (estilo similar a otras tarjetas)."""
        message = loading_messages[loading_index.current]
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.BATTERY_FULL, size=28, color=ft.Colors.GREEN_700),
                            ft.Text("Iniciando carga", size=22, weight=ft.FontWeight.W_700, color=ft.Colors.GREEN_900),
                        ],
                        spacing=12,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=12),
                    ft.Text(message, size=16, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=18),
                    # Animación decorativa: círculo pulsante + texto
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(width=120, height=120, border_radius=60, bgcolor=None, content=ft.Icon(ft.Icons.FLASH_ON, size=48, color=ft.Colors.GREEN_600), alignment=ft.alignment.center),
                                ft.Container(height=8),
                                ft.Text("Conectando con la red sustentable...", size=14, color=ft.Colors.GREY_600),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.all(18),
                        border_radius=16,
                        bgcolor=ft.Colors.GREEN_50,
                        border=ft.border.all(1, ft.Colors.GREEN_100),
                    ),
                    ft.Container(height=18),
                    ft.Row(
                        [
                            ft.ElevatedButton("Cancelar", on_click=lambda e: stop_loading_screen(), style=ft.ButtonStyle(bgcolor=ft.Colors.GREY_200, color=ft.Colors.GREY_900)),
                            ft.Container(width=12),
                            ft.ElevatedButton("Volver al inicio", on_click=lambda e: (stop_loading_screen(), setattr(current_step, 'current', 1), page.update()), bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
            ),
            padding=32,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.95, ft.Colors.WHITE),
            width=720,
        )

    def build_step_2():
        """Paso 2: Selección de método de pago"""
        charge_name = "Carga Rápida" if selected_charge_type.current == "fast" else "Carga Lenta"
        charge_price = charge_prices[selected_charge_type.current]

        return ft.Column(
            [
                # Tarjeta principal
                ft.Container(
                    content=ft.Column(
                        [
                            # Título con botón volver
                            ft.Row(
                                [
                                    ft.Row(
                                        [
                                            ft.Icon(
                                                ft.Icons.CREDIT_CARD,
                                                size=24,
                                                color=ft.Colors.GREEN_600,
                                            ),
                                            ft.Text(
                                                "Selecciona tu método de pago",
                                                size=20,
                                                weight=ft.FontWeight.W_600,
                                                color=ft.Colors.GREEN_900,
                                            ),
                                        ],
                                        spacing=12,
                                    ),
                                    ft.TextButton(
                                        "Volver",
                                        on_click=handle_back,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.GREEN_600,
                                        ),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Container(height=20),
                            # Resumen
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Tipo de carga seleccionada",
                                                    size=14,
                                                    color=ft.Colors.GREY_600,
                                                ),
                                                ft.Text(
                                                    charge_name,
                                                    size=16,
                                                    color=ft.Colors.GREEN_900,
                                                    weight=ft.FontWeight.W_500,
                                                ),
                                            ],
                                            spacing=4,
                                        ),
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Total a pagar",
                                                    size=14,
                                                    color=ft.Colors.GREY_600,
                                                    text_align=ft.TextAlign.RIGHT,
                                                ),
                                                ft.Text(
                                                    charge_price,
                                                    size=28,
                                                    color=ft.Colors.GREEN_700,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                            ],
                                            spacing=4,
                                            horizontal_alignment=ft.CrossAxisAlignment.END,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                padding=16,
                                bgcolor=ft.Colors.GREEN_50,
                                border_radius=12,
                                border=ft.border.all(1, ft.Colors.GREEN_200),
                            ),
                            ft.Container(height=20),
                            # Métodos de pago
                            ft.Row(
                                [
                                    ft.Container(
                                        content=payment_method(
                                            ft.Icons.CREDIT_CARD,
                                            "Tarjeta",
                                            "card",
                                        ),
                                        expand=True,
                                    ),
                                    ft.Container(
                                        content=payment_method(
                                            ft.Icons.QR_CODE,
                                            "Código QR",
                                            "qr",
                                        ),
                                        expand=True,
                                    ),
                                    ft.Container(
                                        content=payment_method(
                                            ft.Icons.ATTACH_MONEY,
                                            "Efectivo",
                                            "cash",
                                        ),
                                        expand=True,
                                    ),
                                ],
                                spacing=16,
                            ),
                            ft.Container(height=24),
                            # Botón iniciar carga
                            ft.ElevatedButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.FLASH_ON, size=20),
                                        ft.Text("Iniciar Carga", size=16),
                                    ],
                                    spacing=8,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor=ft.Colors.GREEN_600,
                                color=ft.Colors.WHITE,
                                on_click=handle_start_charging,
                                disabled=selected_payment.current is None,
                                width=float("inf"),
                                style=ft.ButtonStyle(
                                    padding=ft.padding.symmetric(horizontal=32, vertical=20),
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                            ),
                        ],
                    ),
                    padding=32,
                    bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                    border_radius=24,
                    border=ft.border.all(1, ft.Colors.GREEN_100),
                ),
            ],
            spacing=0,
        )

    # Contenido principal con estado reactivo
    content_container = ft.Container()

    def update_content():
        """Actualiza el contenido según el paso actual"""
        nonlocal charge_prices
        charge_prices = get_charge_prices()
        # Mostrar encabezado solo en el paso 1
        if current_step.current == 1:
            header = ft.Column(
                [
                    ft.Text(
                        "Estación de Carga EcoCharge",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_900,
                    ),
                    ft.Text(
                        "Energía limpia para tu vehículo eléctrico",
                        size=15,
                        color=ft.Colors.GREY_600,
                    ),
                    ft.Container(height=18),
                    build_step_indicator(),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
            # En el paso 2 solo se muestra el indicador de pasos
            header = ft.Column(
                [
                    build_step_indicator(),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

        # Contenido principal
        if loading_active.current:
            # Mostrar la pantalla de carga como tarjeta central
            step_content = ft.Column(
                [
                    build_loading_card(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
            if current_step.current == 1:
                step_content = build_step_1()
            else:
                step_content = build_step_2()

        content_container.content = ft.Column(
            [
                header,
                ft.Container(height=24),
                step_content,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        )

    update_content()

    # Override page.update para actualizar el contenido
    original_update = page.update
    def custom_update():
        update_content()
        original_update()
    page.update = custom_update

    # Pantalla principal con fondo degradado
    main_screen = ft.Container(
        content=ft.Container(
            content=ft.Container(
                content=content_container,
                padding=ft.padding.symmetric(horizontal=48, vertical=28),
            ),
            width=1000,
            height=650,
            bgcolor=ft.Colors.with_opacity(0.95, ft.Colors.WHITE),
            border_radius=16,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    ft.Colors.GREEN_50,
                    ft.Colors.WHITE,
                    ft.Colors.YELLOW_50,
                ],
            ),
        ),
        alignment=ft.alignment.center,
        expand=True,
    )

    page.add(main_screen)

if __name__ == "__main__":
    ft.app(target=main)

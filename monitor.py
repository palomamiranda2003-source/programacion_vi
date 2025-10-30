import flet as ft

def main(page: ft.Page):
    page.title = "EcoCharge - Estación de Carga"
    page.window.width = 800
    page.window.height = 600
    page.bgcolor = "#01040F"

    # Valores fijos (sin base de datos)
    charge_prices = {
        "fast": "25.000 Gs",
        "normal": "15.000 Gs"
    }

    # Estado de la app
    current_step = 1
    selected_charge = "fast"
    selected_payment = None

    # --- Funciones auxiliares ---
    def update_view():
        """Actualiza la vista según el paso"""
        page.controls.clear()

        if current_step == 1:
            show_step_1()
        else:
            show_step_2()

        page.update()

    def next_step(e):
        nonlocal current_step
        current_step = 2
        update_view()

    def back_step(e):
        nonlocal current_step
        current_step = 1
        update_view()

    def start_charge(e):
        if not selected_payment:
            dlg = ft.AlertDialog(title=ft.Text("Selecciona un método de pago"))
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Carga iniciada ⚡"),
                content=ft.Text(f"Carga {selected_charge} pagada con {selected_payment.upper()}"),
                actions=[ft.TextButton("OK", on_click=lambda e: page.close_dialog())],
            )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # --- Paso 1 ---
    def show_step_1():
        def select_charge(e, charge_type):
            nonlocal selected_charge
            selected_charge = charge_type
            update_view()

        page.add(
            ft.Column(
                [
                    ft.Text("Seleccione su tipo de carga", size=22, color="white", weight=ft.FontWeight.BOLD),
                    ft.Container(height=20),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("⚡ Carga Rápida", size=18, color="white"),
                                        ft.Text(charge_prices["fast"], color="#22FF00"),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                width=300,
                                padding=20,
                                bgcolor="#1A1F2B" if selected_charge == "fast" else "#10141E",
                                border_radius=12,
                                on_click=lambda e: select_charge(e, "fast"),
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("🔋 Carga Lenta", size=18, color="white"),
                                        ft.Text(charge_prices["normal"], color="#22FF00"),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                width=300,
                                padding=20,
                                bgcolor="#1A1F2B" if selected_charge == "normal" else "#10141E",
                                border_radius=12,
                                on_click=lambda e: select_charge(e, "normal"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "Continuar",
                        on_click=next_step,
                        bgcolor="#22FF00",
                        color="black",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

    # --- Paso 2 ---
    def show_step_2():
        def select_payment(e, method):
            nonlocal selected_payment
            selected_payment = method
            update_view()

        charge_name = "Rápida ⚡" if selected_charge == "fast" else "Lenta 🔋"
        charge_price = charge_prices[selected_charge]

        page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(ft.Icons.ARROW_BACK, on_click=back_step, icon_color="white"),
                            ft.Text("Selecciona método de pago", size=20, color="white", weight=ft.FontWeight.BOLD),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(f"Tipo de carga: {charge_name}", color="white"),
                                ft.Text(f"Total a pagar: {charge_price}", color="#22FF00", size=18),
                            ],
                            spacing=5,
                        ),
                        padding=20,
                        bgcolor="#1A1F2B",
                        border_radius=12,
                    ),
                    ft.Container(height=30),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text("💳 Tarjeta", color="white"),
                                padding=20,
                                bgcolor="#1A1F2B" if selected_payment == "tarjeta" else "#10141E",
                                border_radius=12,
                                on_click=lambda e: select_payment(e, "tarjeta"),
                                width=150,
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                content=ft.Text("📱 QR", color="white"),
                                padding=20,
                                bgcolor="#1A1F2B" if selected_payment == "qr" else "#10141E",
                                border_radius=12,
                                on_click=lambda e: select_payment(e, "qr"),
                                width=150,
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                content=ft.Text("💵 Efectivo", color="white"),
                                padding=20,
                                bgcolor="#1A1F2B" if selected_payment == "efectivo" else "#10141E",
                                border_radius=12,
                                on_click=lambda e: select_payment(e, "efectivo"),
                                width=150,
                                alignment=ft.alignment.center,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Container(height=40),
                    ft.ElevatedButton(
                        "Iniciar carga",
                        on_click=start_charge,
                        bgcolor="#22FF00",
                        color="black",
                        width=200,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

    # --- Mostrar paso inicial ---
    update_view()

if __name__ == "__main__":
    ft.app(target=main)

import flet as ft

def main(page: ft.Page):
    page.title = "EcoCharge - Estación de Carga"
    page.window.width = 800
    page.window.height = 600
    page.bgcolor = ft.Colors.WHITE

    charge_prices = {
        "fast": "50.000 Gs",
        "normal": "20.000 Gs"
    }

    current_step = 1
    selected_charge = "normal"
    selected_payment = None

    def update_view():
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
                title=ft.Text("Carga iniciada ⚡", size=22, weight=ft.FontWeight.BOLD, color="#2E7D32"),
                content=ft.Text(f"Carga {selected_charge} pagada con {selected_payment}", size=18),
                actions=[ft.TextButton("OK", on_click=lambda e: page.close_dialog())],
            )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def show_step_1():
        def select_charge(e, charge_type):
            nonlocal selected_charge
            selected_charge = charge_type
            update_view()

        page.add(
            ft.Column(
                [
                    ft.Text(
                        "Estación de Carga EcoCharge",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color="#2E7D32"
                    ),
                    ft.Text(
                        "Energía limpia para tu vehículo eléctrico",
                        size=20,
                        color="#4E4E4E"
                    ),
                    ft.Container(height=30),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Carga Rápida ⚡", size=22, weight=ft.FontWeight.BOLD, color="#000000"),
                                        ft.Text(charge_prices["fast"], size=24, weight=ft.FontWeight.BOLD, color="#000000"),
                                        ft.Text("20-30 minutos", size=16, color="#000000")
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                padding=ft.padding.all(20),
                                width=300,
                                border_radius=12,
                                bgcolor="#A5D6A7" if selected_charge=="fast" else "#E8F5E9",
                                on_click=lambda e: select_charge(e, "fast"),
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Carga Lenta 🔋", size=22, weight=ft.FontWeight.BOLD, color="#000000"),
                                        ft.Text(charge_prices["normal"], size=24, weight=ft.FontWeight.BOLD, color="#000000"),
                                        ft.Text("45-60 minutos", size=16, color="#000000")
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                padding=ft.padding.all(20),
                                width=300,
                                border_radius=12,
                                bgcolor="#A5D6A7" if selected_charge=="normal" else "#E8F5E9",
                                on_click=lambda e: select_charge(e, "normal"),
                                alignment=ft.alignment.center
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Continuar ➜",
                            on_click=next_step,
                            bgcolor="#2E7D32",
                            color="white",
                            width=200,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12),
                                                 padding=ft.padding.symmetric(vertical=15))
                        ),
                        alignment=ft.alignment.center
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    def show_step_2():
        def select_payment(e, method):
            nonlocal selected_payment
            selected_payment = method
            update_view()

        page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(ft.Icons.ARROW_BACK, on_click=back_step, icon_color="#2E7D32"),
                            ft.Text("Selecciona método de pago", size=28, weight=ft.FontWeight.BOLD, color="#2E7D32"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(f"Tipo de carga: {'Rápida ⚡' if selected_charge=='fast' else 'Lenta 🔋'}",
                                        size=20, weight=ft.FontWeight.BOLD, color="#000000"),
                                ft.Text(f"Total a pagar: {charge_prices[selected_charge]}",
                                        size=22, weight=ft.FontWeight.BOLD, color="#000000"),
                            ],
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=ft.padding.all(20),
                        border_radius=12,
                        bgcolor="#A5D6A7",
                        width=700,
                        alignment=ft.alignment.center
                    ),
                    ft.Container(height=30),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text("💳 Tarjeta", size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                                width=180,
                                padding=ft.padding.all(15),
                                border_radius=12,
                                bgcolor="#E8F5E9" if selected_payment!="tarjeta" else "#A5D6A7",
                                alignment=ft.alignment.center,
                                on_click=lambda e: select_payment(e, "tarjeta")
                            ),
                            ft.Container(
                                content=ft.Text("📱 QR", size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                                width=180,
                                padding=ft.padding.all(15),
                                border_radius=12,
                                bgcolor="#E8F5E9" if selected_payment!="qr" else "#A5D6A7",
                                alignment=ft.alignment.center,
                                on_click=lambda e: select_payment(e, "qr")
                            ),
                            ft.Container(
                                content=ft.Text("💵 Efectivo", size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                                width=180,
                                padding=ft.padding.all(15),
                                border_radius=12,
                                bgcolor="#E8F5E9" if selected_payment!="efectivo" else "#A5D6A7",
                                alignment=ft.alignment.center,
                                on_click=lambda e: select_payment(e, "efectivo")
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30
                    ),
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.ElevatedButton(
                            "Iniciar Carga ⚡",
                            on_click=start_charge,
                            bgcolor="#2E7D32",
                            color="white",
                            width=250,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12),
                                                 padding=ft.padding.symmetric(vertical=15))
                        ),
                        alignment=ft.alignment.center
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    update_view()

if __name__ == "__main__":
    ft.app(target=main)

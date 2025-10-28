import flet as ft

def login_view(page: ft.Page):
    # --- Configuración de la Ventana---
    page.window.width = 375
    page.window.height = 750 
    page.window.resizable = False
    page.padding = 0
    
    
    # --- Definición de Colores y Estilos ---
    COLOR_LIMA = "#7EE26C"
    COLOR_FONDO_TARJETA = ft.Colors.WHITE
    
    # Degradado del fondo de la página
    GRADIENT_BACKGROUND = ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=["#39D31F", "#6EDD5A"], 
        tile_mode=ft.GradientTileMode.CLAMP
    )

    #Función login
    def login_click(e):
        if usuario.value and contrasena.value:
            page.go("/dashboard") 
        else:
            mensaje.value = "Por favor, completa todos los campos."
            mensaje.color = ft.Colors.RED_500
            page.update()

    # --- 1. Header (Logo y Título) ---
    header_content = ft.Column(
        [
            ft.Container(
                content=ft.Icon(ft.Icons.FLASH_ON, size=35, color=COLOR_FONDO_TARJETA),
                width=60, height=60, border_radius=30, bgcolor=COLOR_LIMA,
                alignment=ft.alignment.center, margin=ft.margin.only(bottom=15)
            ),
            ft.Text("EcoCharge", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text("Energía limpia para tu viaje", size=15, color=ft.Colors.WHITE70),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    header_area = ft.Container(
        content=header_content, 
        alignment=ft.alignment.bottom_center,
        height=240, 
        padding=ft.padding.only(top=50) 
    )

    # --- 2. Elementos de Formulario y Tarjeta Blanca ---
    usuario = ft.TextField(
        label="Correo electrónico", hint_text="tu@email.com", height=50, width=300,
        bgcolor=ft.Colors.WHITE, border_radius=10, border_color=ft.Colors.TRANSPARENT,
        focused_border_color=COLOR_LIMA, content_padding=15, prefix_icon=ft.Icons.MAIL_OUTLINE, dense=True
    )
    
    contrasena = ft.TextField(
        label="Contraseña", hint_text="•••••••••", password=True, can_reveal_password=True,
        height=50, width=300, bgcolor=ft.Colors.WHITE, border_radius=10, 
        border_color=ft.Colors.TRANSPARENT, focused_border_color=COLOR_LIMA, 
        content_padding=15, prefix_icon=ft.Icons.LOCK_OUTLINE, dense=True
    )
    
    enlace_olvido = ft.TextButton(
        "¿Olvidaste tu contraseña?", style=ft.ButtonStyle(color=COLOR_LIMA)
    )

    boton_login = ft.ElevatedButton(
        "Iniciar sesión", width=300, height=50,
        style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=COLOR_LIMA, shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=login_click,
    )
    
    enlace_registro = ft.Row(
        [
            ft.Text("¿No tienes cuenta?", color=ft.Colors.BLACK54),
            ft.TextButton("Regístrate", style=ft.ButtonStyle(color=COLOR_LIMA))
        ],
        alignment=ft.MainAxisAlignment.CENTER, spacing=0
    )

    mensaje = ft.Text("", color=ft.Colors.RED_500, size=14)
    
    footer_inline = ft.Row(
        [
            ft.Icon(ft.Icons.LANGUAGE, size=18, color=COLOR_LIMA), 
            ft.Text("Juntos por un planeta más verde", color=ft.Colors.BLACK54, size=14),
        ],
        spacing=5,
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    card_content = ft.Column(
        [
            ft.Text("Bienvenido", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
            ft.Text("Inicia sesión para continuar", size=15, color=ft.Colors.BLACK54),
            
            ft.Container(height=30), 
            usuario,
            ft.Container(height=10),
            contrasena,
            
            ft.Container(width=300, content=ft.Row([enlace_olvido], alignment=ft.MainAxisAlignment.END, height=35)),
            
            boton_login,
            
            ft.Text("o", color=ft.Colors.BLACK38),
            
            enlace_registro,
            
            ft.Container(height=10),
            mensaje,
            
            ft.Container(expand=True), 
            footer_inline
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
        expand=True,
        scroll=ft.ScrollMode.ADAPTIVE
    )
    
    login_card = ft.Container(
        height=480, 
        width=page.width,
        padding=30,
        bgcolor=COLOR_FONDO_TARJETA,
        border_radius=ft.border_radius.only(top_left=30, top_right=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.BLACK12, offset=ft.Offset(0, -5)),
        content=card_content
    )

    # --- 3. Contenido Principal del View ---
    main_column = ft.Column(
        [
            ft.Container(expand=True), 
            header_area,
            login_card,
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.END, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
    
    # --- 4. Container Principal con el Degradado ---
    main_container = ft.Container(
        content=main_column,
        expand=True,
        gradient=GRADIENT_BACKGROUND
    )
    
    return ft.View(
        "/",
        controls=[main_container],
        bgcolor=ft.Colors.TRANSPARENT 
    )

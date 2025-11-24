import flet as ft
import sqlite3
import os
import tempfile

def obtener_estaciones():
    """Lee las estaciones desde la base de datos."""
    conn = sqlite3.connect("ecocharge.db")
    cursor = conn.cursor()

    # Aseguramos que existan columnas ciudad, direccion, latitud, longitud
    cursor.execute("SELECT ciudad, direccion, latitud, longitud FROM estaciones")
    rows = cursor.fetchall()

    conn.close()
    return rows

def MapView(on_back=None):
    """
    Vista de mapa que abre Leaflet en el navegador y muestra tarjetas con estaciones debajo.
    """
    estaciones = obtener_estaciones()

    # Función para abrir mapa en navegador
    def abrir_mapa(e):
        markers_js = ""
        for ciudad, direccion, lat, lon in estaciones:
            markers_js += f"""
            L.marker([{lat}, {lon}]).addTo(map)
                .bindPopup("<b>{ciudad}</b><br>{direccion}");
            """

        html_map = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
            <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
            <style>
                html, body, #map {{
                    height: 100%;
                    margin: 0;
                }}
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                var map = L.map('map').setView([-25.2637, -57.5759], 11);
                L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                    maxZoom: 19,
                    attribution: '© OpenStreetMap'
                }}).addTo(map);
                {markers_js}
            </script>
        </body>
        </html>
        """

        # Guardar HTML temporal y abrirlo
        temp_file = os.path.join(tempfile.gettempdir(), "mapa_ecocharge.html")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(html_map)
        os.startfile(temp_file)  # Esto abre el navegador por defecto

    # Componente para cada estación
    def station_item(city, address):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.LOCATION_ON, size=16, color="#10b981"),
                            ft.Text(city, size=14, weight=ft.FontWeight.W_600),
                        ],
                        spacing=8,
                    ),
                    ft.Text(address, size=12, color="#6b7280"),
                ],
                spacing=4,
            ),
            bgcolor="#f0fdf4",
            border_radius=8,
            padding=12,
            border=ft.border.all(1, "#d1fae5"),
        )

    return ft.Column(
        [
            # Encabezado
            ft.Container(
                content=ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color=ft.Colors.WHITE,
                            on_click=on_back,
                        ),
                        ft.Text(
                            "Puntos de Carga",
                            size=22,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.WHITE,
                        ),
                        ft.ElevatedButton(
                            text="Abrir Mapa",
                            bgcolor="#10b981",
                            on_click=abrir_mapa,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor="#10b981",
                padding=ft.padding.symmetric(horizontal=16, vertical=20),
            ),

            # Lista de estaciones
            ft.Container(
                content=ft.Column(
                    [station_item(ciudad, direccion) for ciudad, direccion, _, _ in estaciones],
                    spacing=12,
                ),
                padding=ft.padding.symmetric(horizontal=24),
                expand=True,
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
    )

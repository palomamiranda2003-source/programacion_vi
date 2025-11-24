import sqlite3

# Nombre de la base de datos
DB_FILE = "ecocharge.db"

# Conectar (o crear) la base de datos
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Crear tabla si no existe (con latitud y longitud)
cursor.execute("""
CREATE TABLE IF NOT EXISTS estaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ciudad TEXT NOT NULL,
    direccion TEXT NOT NULL,
    latitud REAL NOT NULL,
    longitud REAL NOT NULL
)
""")

# Solicitar datos al usuario
print("=== Agregar nueva estación de carga ===")
ciudad = input("Ciudad: ").strip()
direccion = input("Dirección: ").strip()
latitud = input("Latitud (ej: -25.2637): ").strip()
longitud = input("Longitud (ej: -57.5759): ").strip()

# Validar que todos los datos sean correctos
try:
    lat = float(latitud)
    lon = float(longitud)
except ValueError:
    print("\n⚠️ Latitud o longitud no válidas. No se agregó ninguna estación.")
    conn.close()
    exit()

if ciudad and direccion:
    cursor.execute(
        "INSERT INTO estaciones (ciudad, direccion, latitud, longitud) VALUES (?, ?, ?, ?)",
        (ciudad, direccion, lat, lon)
    )
    conn.commit()
    print(f"\n✅ Estación agregada correctamente:")
    print(f"   Ciudad: {ciudad}")
    print(f"   Dirección: {direccion}")
    print(f"   Latitud: {lat}")
    print(f"   Longitud: {lon}")
else:
    print("\n⚠️ No se ingresaron datos válidos. No se agregó ninguna estación.")

# Cerrar conexión
conn.close()

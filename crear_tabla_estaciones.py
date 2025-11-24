import sqlite3

# Conectar o crear la base de datos
conn = sqlite3.connect("ecocharge.db")
cursor = conn.cursor()

# Crear tabla de estaciones (si no existe)
cursor.execute("""
CREATE TABLE IF NOT EXISTS estaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ciudad TEXT NOT NULL,
    direccion TEXT NOT NULL,
    latitud REAL NOT NULL,
    longitud REAL NOT NULL
)
""")

# Insertar algunas estaciones de ejemplo (con coordenadas reales aproximadas)
estaciones = [
    ("Asunción Centro", "Av. España y Brasilia", -25.2820, -57.6359),
    ("Fernando de la Mora", "Av. Mariscal López y Ruta 2", -25.3112, -57.5637),
    ("San Lorenzo", "Av. San Blas 1234", -25.3400, -57.5200)
]

# Limpiar duplicados (por si ya existen)
cursor.execute("DELETE FROM estaciones")

# Insertar datos nuevos
cursor.executemany(
    "INSERT INTO estaciones (ciudad, direccion, latitud, longitud) VALUES (?, ?, ?, ?)",
    estaciones
)

conn.commit()
conn.close()

print("✅ Base de datos creada e inicializada con estaciones de carga (con coordenadas).")

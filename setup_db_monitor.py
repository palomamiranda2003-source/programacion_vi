import sqlite3

# Conectar (o crear) la base de datos
conn = sqlite3.connect("ecocharge.db")
cursor = conn.cursor()

# Crear tabla de precios si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS charge_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT UNIQUE NOT NULL,   -- "fast" o "normal"
    price TEXT NOT NULL          -- precio como string, ej: "45.000 Gs."
)
""")

# Insertar valores iniciales (si no existen)
cursor.execute("INSERT OR IGNORE INTO charge_prices (type, price) VALUES ('fast', '45.000 Gs.')")
cursor.execute("INSERT OR IGNORE INTO charge_prices (type, price) VALUES ('normal', '25.000 Gs.')")

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos creada y precios iniciales insertados.")

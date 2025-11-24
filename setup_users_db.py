import sqlite3
from hashlib import sha256

# Conectar (o crear) la base de datos
conn = sqlite3.connect("ecocharge_users.db")
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    city TEXT,
    vehicle TEXT,
    plan TEXT,
    password TEXT NOT NULL
)
""")

# Función para encriptar contraseña
def hash_password(password):
    return sha256(password.encode("utf-8")).hexdigest()

# Insertar usuarios iniciales (si no existen)
cursor.execute("""
INSERT OR IGNORE INTO users (first_name, last_name, email, phone, city, vehicle, plan, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ("Juan", "Pérez", "juan@example.com", "099111111", "Asunción", "Nissan Leaf", "Premium", hash_password("1234")))

cursor.execute("""
INSERT OR IGNORE INTO users (first_name, last_name, email, phone, city, vehicle, plan, password)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ("María", "González", "maria@example.com", "098222222", "Luque", "Tesla Model 3", "Básico", hash_password("abcd")))

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos de usuarios creada y usuarios iniciales insertados.")


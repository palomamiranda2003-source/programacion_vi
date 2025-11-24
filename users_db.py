import sqlite3
from hashlib import sha256

DB_FILE = "ecocharge_users.db"

def hash_password(password):
    return sha256(password.encode("utf-8")).hexdigest()

def verify_user(email, password):
    """
    Verifica si el email y la contraseña coinciden con algún usuario en la DB.
    Retorna un diccionario con los datos del usuario si es correcto, o None si no.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, first_name, last_name, email, phone, city, vehicle, plan, password FROM users WHERE email = ?",
        (email,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None  # Usuario no encontrado

    user_id, first_name, last_name, email, phone, city, vehicle, plan, stored_password = row

    if stored_password == hash_password(password):
        # Devolvemos un diccionario con los datos del usuario
        return {
            "id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "city": city,
            "vehicle": vehicle,
            "plan": plan,
        }
    else:
        return None  # Contraseña incorrecta

import sqlite3

DB_FILE = "ecocharge.db"

def get_charge_prices():
    """
    Devuelve un diccionario con los precios actuales de cada tipo de carga.
    Ejemplo: {"fast": "45.000 Gs.", "normal": "25.000 Gs."}
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT type, price FROM charge_prices")
    rows = cursor.fetchall()
    conn.close()
    return {row[0]: row[1] for row in rows}

def update_charge_price(charge_type, new_price):
    """
    Actualiza el precio de un tipo de carga ("fast" o "normal") en la base de datos.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE charge_prices SET price = ? WHERE type = ?",
        (new_price, charge_type)
    )
    conn.commit()
    conn.close()


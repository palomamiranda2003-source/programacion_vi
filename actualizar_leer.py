from db_utils_monitor import get_charge_prices, update_charge_price

# Leer precios
precios = get_charge_prices()
print(precios["fast"])   # ej: "45.000 Gs."
print(precios["normal"]) # ej: "25.000 Gs."

# Actualizar precio de carga rápida
update_charge_price("normal", "20.000 Gs.")

# Volver a leer precios
precios = get_charge_prices()
print(precios["normal"])   # ahora "50.000 Gs."

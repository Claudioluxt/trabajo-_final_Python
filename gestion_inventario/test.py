# test.py
from database import inicializar_db
from productos import registrar_producto, reporte_bajo_stock

inicializar_db()
# Registrá algunos productos con cantidades bajas (0, 1, 3, 10, etc.)
reporte_bajo_stock()   # Probá con límite 5, luego con límite 0
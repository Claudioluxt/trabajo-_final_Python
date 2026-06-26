# database.py
# Módulo encargado de la conexión y la inicialización de la base de datos.

import sqlite3  # Módulo nativo de Python 

# Constante con el nombre del archivo de la base de datos.

NOMBRE_DB = "inventario.db"


def crear_conexion():
    """
    Crea y retorna una conexión al archivo de base de datos SQLite.
   
    
    Returns:
        conexion: objeto de conexión a la base de datos, o None si hay error.
    """
    try:
        conexion = sqlite3.connect(NOMBRE_DB)
        return conexion
    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo conectar a la base de datos: {e}")
        return None


def inicializar_db():
    """
    Crea la tabla 'productos' en la base de datos si todavía no existe.
    Esta función se llama UNA SOLA VEZ al arrancar el programa. 
    """
    conexion = crear_conexion()

    
    if conexion is None:
        return

    try:
        
        cursor = conexion.cursor()

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre      TEXT    NOT NULL,
                descripcion TEXT,
                cantidad    INTEGER NOT NULL,
                precio      REAL    NOT NULL,
                categoria   TEXT
            )
        """)

       
        conexion.commit()
        print("[OK] Base de datos inicializada correctamente.")

    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo crear la tabla: {e}")

    finally:
        
        conexion.close()
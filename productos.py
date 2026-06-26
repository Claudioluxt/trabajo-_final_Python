import sqlite3
from database import crear_conexion  # Importamos la función que ya construimos (Clase 11)


# ==============================================================================
# SECCIÓN 1 — REGISTRAR PRODUCTO 
# ==============================================================================

def registrar_producto():
    """
    Solicita los datos de un nuevo producto al usuario y lo guarda en la BD.
    Valida que cantidad sea un número entero y precio un número decimal.
    """
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")

    
 

    nombre = ""
    while nombre == "":
        nombre = input("Nombre del producto: ").strip()
        if nombre == "":
            print("[AVISO] El nombre no puede estar vacío.")

    descripcion = input("Descripción (opcional, Enter para omitir): ").strip()

    categoria = input("Categoría (opcional, Enter para omitir): ").strip()

    
    cantidad = None
    while cantidad is None:
        try:
            cantidad = int(input("Cantidad disponible: "))
            if cantidad < 0:
                print("[AVISO] La cantidad no puede ser negativa.")
                cantidad = None
        except ValueError:
            
            print("[ERROR] Ingresá un número entero válido para la cantidad.")

    
    precio = None
    while precio is None:
        try:
            precio = float(input("Precio unitario: "))
            if precio < 0:
                print("[AVISO] El precio no puede ser negativo.")
                precio = None
        except ValueError:
            print("[ERROR] Ingresá un número válido para el precio (ej: 150.99).")

     
    nombre     = nombre.title()
    categoria  = categoria.title()

    
    conexion = crear_conexion()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()

       
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))

        conexion.commit()
        print(f"\n[OK] Producto '{nombre}' registrado con éxito.")

    except sqlite3.Error as e:
       
        conexion.rollback()
        print(f"[ERROR] No se pudo registrar el producto: {e}")

    finally:
        conexion.close()



# ==============================================================================
# SECCIÓN 2 — VISUALIZAR PRODUCTOS 
# ==============================================================================

def visualizar_productos():
    """
    Recupera todos los productos de la base de datos y los muestra
    en formato de tabla por consola, ordenados por nombre.
    """
    conexion = crear_conexion()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()

        
        cursor.execute("SELECT * FROM productos ORDER BY nombre")

        
        productos = cursor.fetchall()

       
        if len(productos) == 0:
            print("\n[AVISO] No hay productos registrados en el inventario.")
            return

        
        print("\n" + "=" * 70)
        print(f"{'ID':<5} {'NOMBRE':<20} {'CATEGORÍA':<15} {'CANTIDAD':<10} {'PRECIO':<10} {'DESCRIPCIÓN'}")
        print("=" * 70)

        
        for producto in productos:
            id_p        = producto[0]
            nombre      = producto[1]
            descripcion = producto[2] if producto[2] else "-"  # Si es None, mostramos "-"
            cantidad    = producto[3]
            precio      = producto[4]
            categoria   = producto[5] if producto[5] else "-"

            
            print(f"{id_p:<5} {nombre:<20} {categoria:<15} {cantidad:<10} ${precio:<9.2f} {descripcion}")

        print("=" * 70)
        print(f"  Total de productos registrados: {len(productos)}")
        print("=" * 70)

    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo obtener los productos: {e}")

    finally:
        conexion.close()        




# ==============================================================================
# SECCIÓN 3 — ACTUALIZAR PRODUCTO (Update)
# ==============================================================================

def actualizar_producto():
    """
    Busca un producto por su ID y permite modificar sus datos.
    El usuario elige qué campo actualizar. Usa consultas parametrizadas.
    """
    print("\n--- ACTUALIZAR PRODUCTO ---")

   
    id_producto = None
    while id_producto is None:
        try:
            id_producto = int(input("Ingresá el ID del producto a actualizar: "))
        except ValueError:
            print("[ERROR] El ID debe ser un número entero.")

    conexion = crear_conexion()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()

        
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()  # fetchone() trae solo un registro o None

        if producto is None:
            print(f"[AVISO] No se encontró ningún producto con ID {id_producto}.")
            return

       
        print(f"\nProducto encontrado:")
        print(f"  Nombre    : {producto[1]}")
        print(f"  Descripción: {producto[2]}")
        print(f"  Cantidad  : {producto[3]}")
        print(f"  Precio    : ${producto[4]:.2f}")
        print(f"  Categoría : {producto[5]}")

        
        print("\n¿Qué campo deseas actualizar?")
        print("  1. Nombre")
        print("  2. Descripción")
        print("  3. Cantidad")
        print("  4. Precio")
        print("  5. Categoría")

        opcion = input("\nElegí una opción (1-5): ").strip()

        campo = None
        nuevo_valor = None

        match opcion:
            case "1":
                campo = "nombre"
                nuevo_valor = input("Nuevo nombre: ").strip().title()
                while nuevo_valor == "":
                    print("[AVISO] El nombre no puede estar vacío.")
                    nuevo_valor = input("Nuevo nombre: ").strip().title()

            case "2":
                campo = "descripcion"
                nuevo_valor = input("Nueva descripción: ").strip()

            case "3":
                campo = "cantidad"
                nuevo_valor = None
                while nuevo_valor is None:
                    try:
                        nuevo_valor = int(input("Nueva cantidad: "))
                        if nuevo_valor < 0:
                            print("[AVISO] La cantidad no puede ser negativa.")
                            nuevo_valor = None
                    except ValueError:
                        print("[ERROR] Ingresá un número entero válido.")

            case "4":
                campo = "precio"
                nuevo_valor = None
                while nuevo_valor is None:
                    try:
                        nuevo_valor = float(input("Nuevo precio: "))
                        if nuevo_valor < 0:
                            print("[AVISO] El precio no puede ser negativo.")
                            nuevo_valor = None
                    except ValueError:
                        print("[ERROR] Ingresá un número válido (ej: 150.99).")

            case "5":
                campo = "categoria"
                nuevo_valor = input("Nueva categoría: ").strip().title()

            case _:
                print("[ERROR] Opción no válida. Volvé al menú principal.")
                return

      
        cursor.execute(
            f"UPDATE productos SET {campo} = ? WHERE id = ?",
            (nuevo_valor, id_producto)
        )

        conexion.commit()
        print(f"\n[OK] Campo '{campo}' actualizado correctamente.")

    except sqlite3.Error as e:
        conexion.rollback()
        print(f"[ERROR] No se pudo actualizar el producto: {e}")

    finally:
        conexion.close()


# ==============================================================================
# SECCIÓN 4 — ELIMINAR PRODUCTO (Delete)
# ==============================================================================

def eliminar_producto():
    """
    Busca un producto por su ID y lo elimina de la base de datos.
    Solicita confirmación explícita al usuario antes de ejecutar el DELETE.
    Esta confirmación es un requisito de seguridad obligatorio del TFI.
    """
    print("\n--- ELIMINAR PRODUCTO ---")

    
    id_producto = None
    while id_producto is None:
        try:
            id_producto = int(input("Ingresá el ID del producto a eliminar: "))
        except ValueError:
            print("[ERROR] El ID debe ser un número entero.")

    conexion = crear_conexion()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()

        
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if producto is None:
            print(f"[AVISO] No se encontró ningún producto con ID {id_producto}.")
            return

        # Mostramos los datos del producto que se va a eliminar
        print(f"\nEstás por eliminar el siguiente producto:")
        print(f"  ID        : {producto[0]}")
        print(f"  Nombre    : {producto[1]}")
        print(f"  Categoría : {producto[5] if producto[5] else '-'}")
        print(f"  Cantidad  : {producto[3]}")
        print(f"  Precio    : ${producto[4]:.2f}")

        
     
        print("\n¡ATENCIÓN! Esta acción no se puede deshacer.")
        confirmacion = input("¿Confirmás la eliminación? (s/n): ").strip().lower()

        if confirmacion not in ("s", "si", "sí"):
            print("[INFO] Eliminación cancelada por el usuario.")
            return

        
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        print(f"\n[OK] Producto '{producto[1]}' (ID: {id_producto}) eliminado correctamente.")

    except sqlite3.Error as e:
        conexion.rollback()
        print(f"[ERROR] No se pudo eliminar el producto: {e}")

    finally:
        conexion.close()

# ==============================================================================
# SECCIÓN 5 — BUSCAR PRODUCTO (Search)
# ==============================================================================

def buscar_producto():
    """
    Permite buscar productos por tres criterios: ID, nombre o categoría.
    La búsqueda por nombre y categoría es parcial (no necesita ser exacta).
    """
    print("\n--- BUSCAR PRODUCTO ---")

    
    print("¿Cómo querés buscar?")
    print("  1. Por ID")
    print("  2. Por nombre")
    print("  3. Por categoría")

    opcion = input("\nElegí una opción (1-3): ").strip()

    conexion = crear_conexion()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()
        productos = []  

        match opcion:
            case "1":
                
                id_producto = None
                while id_producto is None:
                    try:
                        id_producto = int(input("Ingresá el ID a buscar: "))
                    except ValueError:
                        print("[ERROR] El ID debe ser un número entero.")

                cursor.execute(
                    "SELECT * FROM productos WHERE id = ?",
                    (id_producto,)
                )
                
                resultado = cursor.fetchone()
                if resultado:
                    productos.append(resultado) 

            case "2":
                # Búsqueda parcial por nombre 
                termino = input("Ingresá el nombre (o parte del nombre): ").strip()
                cursor.execute(
                    "SELECT * FROM productos WHERE nombre LIKE ?",
                    (f"%{termino}%",)
                )
                productos = cursor.fetchall()

            case "3":
               
                termino = input("Ingresá la categoría (o parte de la categoría): ").strip()
                cursor.execute(
                    "SELECT * FROM productos WHERE categoria LIKE ?",
                    (f"%{termino}%",)
                )
                productos = cursor.fetchall()

            case _:
                print("[ERROR] Opción no válida.")
                return

       
        if len(productos) == 0:
            print("\n[AVISO] No se encontraron productos con ese criterio.")
            return

      
        print(f"\n{len(productos)} resultado(s) encontrado(s):")
        print("=" * 70)
        print(f"{'ID':<5} {'NOMBRE':<20} {'CATEGORÍA':<15} {'CANTIDAD':<10} {'PRECIO':<10} {'DESCRIPCIÓN'}")
        print("=" * 70)

        for producto in productos:
            id_p        = producto[0]
            nombre      = producto[1]
            descripcion = producto[2] if producto[2] else "-"
            cantidad    = producto[3]
            precio      = producto[4]
            categoria   = producto[5] if producto[5] else "-"

            print(f"{id_p:<5} {nombre:<20} {categoria:<15} {cantidad:<10} ${precio:<9.2f} {descripcion}")

        print("=" * 70)

    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo realizar la búsqueda: {e}")

    finally:
        conexion.close()




# ==============================================================================
# SECCIÓN 6 — REPORTE DE BAJO STOCK (Report)
# ==============================================================================

def reporte_bajo_stock():
    """
    Solicita al usuario un límite numérico y lista todos los productos
    cuya cantidad sea igual o inferior a ese límite, ordenados de menor
    a mayor cantidad para identificar los más críticos primero.
    """
    print("\n--- REPORTE DE BAJO STOCK ---")

   
    limite = None
    while limite is None:
        try:
            limite = int(input("Ingresá el límite de stock (ej: 5): "))
            if limite < 0:
                print("[AVISO] El límite no puede ser negativo.")
                limite = None
        except ValueError:
            print("[ERROR] Ingresá un número entero válido.")

    conexion = crear_conexion()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()

        
        cursor.execute("""
            SELECT * FROM productos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC
        """, (limite,))

        productos = cursor.fetchall()

       
        print(f"\n{'=' * 70}")
        print(f"  REPORTE: Productos con stock igual o inferior a {limite} unidades")
        print(f"{'=' * 70}")

        if len(productos) == 0:
            print(f"  [OK] No hay productos con stock igual o inferior a {limite}.")
            print(f"{'=' * 70}")
            return

        
        print(f"{'ID':<5} {'NOMBRE':<20} {'CATEGORÍA':<15} {'CANTIDAD':<10} {'PRECIO'}")
        print("-" * 70)

        
        total_unidades = 0

        for producto in productos:
            id_p      = producto[0]
            nombre    = producto[1]
            cantidad  = producto[3]
            precio    = producto[4]
            categoria = producto[5] if producto[5] else "-"

          
            total_unidades += cantidad

           
            alerta = " ⚠ SIN STOCK" if cantidad == 0 else ""

            print(f"{id_p:<5} {nombre:<20} {categoria:<15} {cantidad:<10} ${precio:<9.2f}{alerta}")

       
        print("-" * 70)
        print(f"  Productos en situación de bajo stock : {len(productos)}")
        print(f"  Total de unidades restantes en riesgo: {total_unidades}")
        print(f"{'=' * 70}")

    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo generar el reporte: {e}")

    finally:
        conexion.close()
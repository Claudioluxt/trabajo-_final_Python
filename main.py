# main.py
# Punto de entrada principal del sistema de Gestión de Inventario.
# Talento Tech - Proyecto Final Integrador



from database import inicializar_db
from productos import (
    registrar_producto,
    visualizar_productos,
    actualizar_producto,
    eliminar_producto,
    buscar_producto,
    reporte_bajo_stock
)



# ==============================================================================
# FUNCIÓN PRINCIPAL
# ==============================================================================
def mostrar_menu():
    """Imprime las opciones del menú principal en la consola."""
    print("\n" + "="*40)
    print("  GESTIÓN DE INVENTARIO ")
    print("="*40)
    print("1. Registrar producto")
    print("2. Visualizar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("0. Salir")
    print("="*40)
    
def main():
    """
    Función principal que inicializa la base de datos y ejecuta
    
    """
    
    inicializar_db()

   

    
    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ").strip()

        
        match opcion:
            case "1":
                registrar_producto()
            case "2":
                visualizar_productos()
            case "3":
                actualizar_producto()
            case "4":
                eliminar_producto()
            case "5":
                buscar_producto()
            case "6":
                reporte_bajo_stock()
            case "0":
              
                break  
           



if __name__ == "__main__":
    main()
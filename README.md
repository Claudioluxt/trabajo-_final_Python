# 📦 Sistema de Gestión de Inventario

Aplicación de consola desarrollada en **Python + SQLite** como Trabajo Final Integrador del programa **Talento Tech** – Ciudad de Buenos Aires .

---

## 📋 Descripción

Sistema CRUD completo para la gestión de inventario de productos desde la terminal. Permite registrar, consultar, actualizar y eliminar productos, además de generar reportes de bajo stock en tiempo real.

---

## 🚀 Funcionalidades

| Opción | Funcionalidad |
|--------|--------------|
| 1 | Registrar nuevo producto |
| 2 | Visualizar todos los productos |
| 3 | Actualizar datos de un producto |
| 4 | Eliminar un producto (con confirmación) |
| 5 | Buscar producto por ID, nombre o categoría |
| 6 | Reporte de bajo stock (límite dinámico) |
| 0 | Salir del sistema |

---

## 🗂️ Estructura del proyecto

```
gestion_inventario/
│
├── main.py          # Punto de entrada: menú principal con bucle while
├── database.py      # Conexión e inicialización de la base de datos SQLite
├── productos.py     # Funciones CRUD y reportes
├── inventario.db    # Base de datos (se genera automáticamente al ejecutar)
└── README.md        # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- El módulo `sqlite3` es nativo de Python — **no requiere instalación**

---

## ▶️ Cómo ejecutar

1. Cloná el repositorio o descargá los archivos:

```bash
git clone https://github.com/tu-usuario/gestion-inventario.git
cd gestion-inventario/gestion_inventario
```

2. Ejecutá el programa:

```bash
python main.py
```

La base de datos `inventario.db` se crea automáticamente en el primer uso.

---

## 🗄️ Base de datos

Archivo: `inventario.db` (SQLite)

Tabla: `productos`

| Columna | Tipo | Restricción |
|---------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| nombre | TEXT | NOT NULL |
| descripcion | TEXT | — |
| cantidad | INTEGER | NOT NULL |
| precio | REAL | NOT NULL |
| categoria | TEXT | — |

---

## 🔒 Seguridad aplicada

- Consultas parametrizadas con `?` para prevenir inyección SQL
- Confirmación explícita del usuario antes de cualquier eliminación
- Control de transacciones con `commit()` y `rollback()`
- Validación de todos los campos numéricos con `try-except`

---


## 📸 Vista previa

```
==================================================
   SISTEMA DE GESTIÓN DE INVENTARIO
==================================================
  1. Registrar nuevo producto
  2. Visualizar todos los productos
  3. Actualizar un producto
  4. Eliminar un producto
  5. Buscar producto
  6. Reporte de bajo stock
  0. Salir del sistema
==================================================

======================================================================
ID    NOMBRE               CATEGORÍA       CANTIDAD   PRECIO     DESCRIPCIÓN
======================================================================
1     Auriculares Bt       Electrónica     15         $2999.99   Inalámbricos
2     Remera Blanca        Indumentaria    3          $1500.00   Talle M
3     Zapatillas Running   Calzado         0          $8500.00   -
======================================================================
  Total de productos registrados: 3
======================================================================
```

---

## 👤 Autor: Claudio Gabriel LUXEN ESPINOZA

Desarrollado como Trabajo Final Integrador del curso  
**Iniciación a la Programación con Python**  
Programa **Talento Tech** – Ministerio de Educación – Ciudad de Buenos Aires  
Año 2026

---

## 📄 Licencia

Proyecto educativo de uso libre.
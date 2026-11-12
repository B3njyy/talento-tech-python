import sqlite3


def crear_base_datos():
    conexion = sqlite3.connect("Productos.db")
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()


crear_base_datos()


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("El nombre del producto no puede estar vacio.")
        return

    try:
        precio = float(input("Ingrese el precio del producto: "))

        if precio <= 0:
            print("El precio del producto debe ser mayor a 0. ")
            return

        cantidad = int(input("Ingrese la cantidad del producto: "))

        if cantidad < 0:
            print("La cantidad del producto no puede ser negativa.")
            return

    except ValueError:
        print("Error: El precio y la cantidad deben ser numeros.")
        return

    conexion = sqlite3.connect("Productos.db")
    cursor = conexion.cursor()

    cursor.execute('''
        INSERT INTO productos (nombre, precio, cantidad)
        VALUES (?, ?, ?)
    ''', (nombre, precio, cantidad))

    conexion.commit()
    conexion.close()

    print(f"Producto '{nombre}' agregado exitosamente.")


def listar_productos():
    conexion = sqlite3.connect("Productos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if productos:
        print("\n=== Lista de Productos ===")

        for producto in productos:
            print(
                f"ID: {producto[0]} | "
                f"Nombre: {producto[1]} | "
                f"Precio: ${producto[2]:.2f} | "
                f"Cantidad: {producto[3]}"
            )
    else:
        print("No hay productos registrados.")

    conexion.close()


def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()

    conexion = sqlite3.connect("Productos.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM productos WHERE nombre = ?",
        (nombre_buscar,)
    )

    producto = cursor.fetchone()

    if producto:
        print(
            f"ID: {producto[0]} | "
            f"Nombre: {producto[1]} | "
            f"Precio: ${producto[2]:.2f} | "
            f"Cantidad: {producto[3]}"
        )
    else:
        print(f"No se encontro el producto con nombre '{nombre_buscar}'.")

    conexion.close()


def eliminar_producto():
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))

        conexion = sqlite3.connect("Productos.db")
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM productos WHERE id = ?",
            (id_producto,)
        )

        conexion.commit()

        if cursor.rowcount > 0:
            print(f"Producto con ID {id_producto} eliminado exitosamente. ")
        else:
            print(f"No se encontro el producto con ID {id_producto}.")

        conexion.close()

    except ValueError:
        print("Error: El ID del producto debe ser un numero entero.")


def menu():
    while True:
        print("\n=== Menu de Productos ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto por ID")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Por favor, seleccione una opcion valida.")


menu()

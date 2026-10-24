productos = []


def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("Nombre no valido")
        return None

    entrada_precio = input("Ingrese el precio: ").strip()

    if entrada_precio.isdigit() == False:
        print("Precio no valido")
        return None

    precio = int(entrada_precio)

    if precio <= 0:
        print("Precio no valido")
        return None

    producto = [nombre, precio]
    productos.append(producto)

    return producto


def consultar_productos():
    if productos:
        return productos
    else:
        return []


def eliminar_producto():
    if productos:
        nombre_eliminar = input("Ingrese el producto a eliminar: ").strip()

        for producto in productos:
            if producto[0].lower() == nombre_eliminar.lower():
                productos.remove(producto)
                return producto

        return None

    else:
        return None


def menu_interactivo():
    while True:

        print("\nSistema de gestion de productos")
        print("1. Agregar producto")
        print("2. Consultar productos")
        print("3. Eliminar producto")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":

            producto_agregado = agregar_productos()

            if producto_agregado:
                print(
                    f"Producto agregado: {producto_agregado[0]} | "
                    f"Precio: ${producto_agregado[1]}"
                )


        elif opcion == "2":

            lista_productos = consultar_productos()

            if lista_productos:
                print("Lista de productos:")

                for i, producto in enumerate(lista_productos, start=1):
                    print(
                        f"{i}. Nombre: {producto[0]} | "
                        f"Precio: ${producto[1]}"
                    )

            else:
                print("No hay productos registrados")


        elif opcion == "3":

            producto_eliminado = eliminar_producto()

            if producto_eliminado:
                print(
                    f"Producto eliminado: {producto_eliminado[0]} | "
                    f"Precio: ${producto_eliminado[1]}"
                )

            else:
                print("Producto no encontrado")


        elif opcion == "4":

            print("Saliendo del programa...")
            break


        else:

            print("Opcion no valida")


menu_interactivo()
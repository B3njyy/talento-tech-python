productos = []

def agregar_productos(): 
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("Nombre no valido")
    else: 
        entrada_precio = input("Ingrese el precio: ").strip()

        if entrada_precio.isdigit() == False:
            print("Precio no valido")
        else: 
            precio = int(entrada_precio)

            producto = [nombre, precio]
            productos.append(producto)

            print("Producto agregado correctamente")


def consultar_productos(): 
    if productos:
        print("Lista de productos")

        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto[0]} | Precio: ${producto[1]}")

    else:
        print("No hay productos registrados")


def eliminar_producto():
    if productos:
        nombre_eliminar = input("Ingrese el producto a eliminar: ").strip()

        encontrado = False

        for producto in productos:
            if producto[0].lower() == nombre_eliminar.lower():
                productos.remove(producto)
                print("Producto eliminado correctamente")
                encontrado = True
                break
        
        if encontrado == False:
            print("Producto no encontrado")

    else:
        print("No hay productos registrados")


def menu_interactivo():
    while True:
        print("\n1. Agregar producto")
        print("2. Consultar productos")
        print("3. Eliminar producto")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            agregar_productos()

        elif opcion == "2":
            consultar_productos()

        elif opcion == "3":
            eliminar_producto()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida")


menu_interactivo()
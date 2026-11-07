import datetime
from colorama import Fore, Style, init

init()

productos = []


def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print(Fore.RED + "Nombre no valido" + Style.RESET_ALL)
        return None

    entrada_precio = input("Ingrese el precio: ").strip()

    if entrada_precio.isdigit() == False:
        print(Fore.RED + "Precio no valido" + Style.RESET_ALL)
        return None

    precio = int(entrada_precio)

    if precio <= 0:
        print(Fore.RED + "Precio no valido" + Style.RESET_ALL)
        return None

    fecha_hora = datetime.datetime.now()
    fecha_formateada = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")

    producto = [nombre, precio, fecha_formateada]
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
                    Fore.GREEN +
                    f"Producto agregado: {producto_agregado[0]} | "
                    f"Precio: ${producto_agregado[1]} | "
                    f"Fecha: {producto_agregado[2]}" +
                    Style.RESET_ALL
                )


        elif opcion == "2":

            lista_productos = consultar_productos()

            if lista_productos:
                print("Lista de productos:")

                for i, producto in enumerate(lista_productos, start=1):
                    print(
                        f"{i}. Nombre: {producto[0]} | "
                        f"Precio: ${producto[1]} | "
                        f"Fecha: {producto[2]}"
                    )

            else:
                print(Fore.YELLOW + "No hay productos registrados" + Style.RESET_ALL)

        elif opcion == "3":
            producto_eliminado = eliminar_producto()

            if producto_eliminado:
                print(
                    Fore.GREEN +
                    f"Producto eliminado: {producto_eliminado[0]} | "
                    f"Precio: ${producto_eliminado[1]} | "
                    f"Fecha: {producto_eliminado[2]}" +
                    Style.RESET_ALL
                )
            else:
                print(Fore.YELLOW + "Producto no encontrado" + Style.RESET_ALL)

        elif opcion == "4":
            print(Fore.CYAN + "Saliendo del programa..." + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Opcion no valida" + Style.RESET_ALL)

menu_interactivo()
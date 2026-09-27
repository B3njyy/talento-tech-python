productos = []

opcion = 0

while opcion != 5:
    print("\nSistema de gestion basica de productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    entrada_opcion = input("Seleccione una opcion: ").strip()
    if entrada_opcion.isdigit() == False:
        print("Opcion no valida")
        continue
    opcion = int(entrada_opcion)
    if opcion == 1:
        print("Agregar producto")
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre == "":
            print("Nombre no valido")
        else:
            categoria = input("Ingrese la categoria del producto: ").strip()
            if categoria == "":
                print("Categoria no valida")
            else:
                entrada_precio = input("Ingrese el precio del producto: ").strip()
                if entrada_precio.isdigit() == False:
                    print("Precio no valido")
                    continue
                precio = int(entrada_precio)
                if precio <= 0:
                    print("Precio no valido")
                    continue
                producto = [nombre, categoria, precio]
                productos.append(producto)
                print(f"Producto {nombre} agregado correctamente")
    elif opcion == 2:
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. Nombre: {productos[i][0]} | "
                    f"Categoria: {productos[i][1]} | "
                    f"Precio: ${productos[i][2]}"
                )
    elif opcion == 3:
        busqueda = input(
            "Ingrese el nombre del producto a buscar: "
        ).strip().lower()
        if busqueda == "":
            print("Nombre de busqueda no valido")
            continue
        encontrado = False
        for i in range(len(productos)):
            if productos[i][0].lower() == busqueda:
                print(
                    f"Producto encontrado: "
                    f"Nombre: {productos[i][0]} | "
                    f"Categoria: {productos[i][1]} | "
                    f"Precio: ${productos[i][2]}"
                )
                encontrado = True
        if encontrado == False:
            print("No se encontro el producto")
    elif opcion == 4:
        if len(productos) == 0:
            print("No hay productos registrados para eliminar")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. Nombre: {productos[i][0]} | "
                    f"Categoria: {productos[i][1]} | "
                    f"Precio: ${productos[i][2]}"
                )
            entrada_posicion = input(
                "Ingrese el numero del producto que desea eliminar: "
            ).strip()
            if entrada_posicion.isdigit() == False:
                print("Posicion no valida")
                continue
            posicion = int(entrada_posicion)
            if posicion < 1 or posicion > len(productos):
                print("Posicion no valida")
            else:
                productos.pop(posicion - 1)
                print("Producto eliminado correctamente")
    elif opcion == 5:
        print("Saliendo del sistema chauuu")
    else:
        print("Opcion no valida")
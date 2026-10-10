productos = {}

while True:
    nombre = input("Ingresa el nombre del producto: ").strip()

    if nombre.lower() == "fin":
        break

    if nombre == "":
        print("El nombre no puede estar vacio")
        continue 

    entrada_precio = input("Ingrese el precio del producto: ").strip()

    if entrada_precio.isdigit() == False:
        print("Precio no valido")
        continue

    precio = int(entrada_precio) 

    if precio <= 0:
        print("Precio no valido")
        continue

    productos[nombre] = precio

    print("Produtos registrados:")

    for producto, valor in productos.items():
        print(f"{producto}: ${valor}")
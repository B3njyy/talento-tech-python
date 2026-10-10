clientes = [] 

while True:
    nombre = input("Ingrese el nombre del cliente: ").strip()

    if  nombre.lower() == "fin":
        break

    if nombre == "": 
        print ("El nombre no puede estar vacio")
    else:
        clientes.append(nombre)
        print(f"Cliente agregado: {nombre}")

clientes.sort()

print("Lista de clientes ordenada:")

for cliente in clientes:
    print(cliente)



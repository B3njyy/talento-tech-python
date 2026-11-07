print("===Registro de Clientes===")

nombre = input("Nombre: ").strip()
apellido = input("Apellido: ").strip()
correo = input("Correo: ").strip()

if nombre == "":
    print("Nombre no valido")

elif apellido == "":
    print("Apellido no valido")

elif "@" not in correo:
    print("Correo no valido")

else:
    try:
        archivo = open("clientes.txt", "a")
        archivo.write(f"{nombre}, {apellido}, {correo}\n")
        archivo.close()
        print("Cliente registrado con exito en clientes.txt")
    except:
        print("[ERROR] No se pudo guardar la informacion")
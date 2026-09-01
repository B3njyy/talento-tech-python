nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip()
edad = input("Ingrese su edad: ").strip()
correo = input("Ingrese su correo electrónico: ").strip()

if nombre != "" and apellido != "" and correo != "" and edad.isdigit() and int(edad) > 18:
    print(nombre)
    print(apellido)
    print(edad)
    print(correo)
else:
    print("ERROR!")

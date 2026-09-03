nombre = input("Cual es tu nombre? ").strip().title()
apellido = input("Cual es tu apellido? ").strip().title()
edad = int(input("Cual es tu edad? ").strip())
email = input("Cual es tu email? ")

if email.find(" ") == -1 and email.count("@") == 1:

    if edad < 15:
        rango_etario = "Niño/a"
    elif edad <= 18:
        rango_etario = "Adolescente"
    else:
        rango_etario = "Adulto/a"

    print(f"Apellido: {apellido}, Nombre: {nombre}, Email: {email}, Rango etario: {rango_etario}")

else:
    print("Email invalido")
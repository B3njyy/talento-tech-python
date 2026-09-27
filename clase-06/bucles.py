clientes = ["ana", "JUAN", "", "mArTa" ]

for i in range(len(clientes)):
    if clientes[i] == "":
        print(f"Cliente {i + 1}: [ALERTA] Nombre no valido")
    else:
        print(f"Cliente {i + 1}: {clientes[i].capitalize()}")
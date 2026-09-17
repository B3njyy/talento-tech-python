mes = 1
total = 0 

while mes <= 6:
    print(f"Ingrese el ingreso del mes {mes}: ")
    ingreso = int(input().strip())
    if ingreso <= 0:
        print("Ingreso invalido")
        continue
    total += ingreso
    mes += 1


promedio = total / 6

print(f"El promedio de ingresos de los 6 meses es: {promedio}")
print(f"El total de ingresos de los 6 meses es: {total}")
import sqlite3

conexion = sqlite3.connect("productos.db")

cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
precio REAL NOT NULL
)
''')
conexion.commit()

nombre = input("Ingrese el nombre del producto: ").strip()

if nombre == "":
    print("Nombre no valido")
else:
    try:
        precio = float(input("Ingrese el precio del producto: "))

        if precio <= 0:
            print("Precio no valido")
        else:
          cursor.execute('''
            INSERT INTO productos (nombre, precio)
            VALUES (?, ?)
        ''', (nombre, precio))
        conexion.commit()

    except ValueError:
        print("Precio no valido")

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print("\n === Lista de Productos ===")

for producto in productos:
    print(f"ID: {producto[0]} | Nombre: {producto[1]} | Precio: ${producto[2]:.2f}")

conexion.close()
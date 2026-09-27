productos = {}


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip().lower()


    if nombre in productos:
        print("\nEl producto ya se encuentra registrado.")
        return

    try:
        precio = float(input("Ingrese el precio del producto: $"))
        cantidad = int(input("Ingrese la cantidad disponible: "))

        if precio < 0 or cantidad < 0:
            print("\nEl precio y la cantidad no pueden ser negativos.")
            return

        productos[nombre] = {
            "precio": precio,
            "cantidad": cantidad
        }

        print("\nProducto registrado correctamente.")

    except ValueError:
        print("\nError: debe ingresar valores numéricos correctos.")

def mostrar_productos():
    if not productos:
        print("\nNo existen productos registrados.")
        return

    print("\n--------- PRODUCTOS REGISTRADOS ---------")
    print(f"{'PRODUCTO':<20}{'PRECIO':<15}{'CANTIDAD':<10}")
    print("-" * 45)

    for nombre, datos in productos.items():
        print(
            f"{nombre.title():<20}"
            f"${datos['precio']:<14.2f}"
            f"{datos['cantidad']:<10}"
        )

def buscar_producto():
    nombre = input("Ingrese el producto que desea buscar: ").strip().lower()

    if nombre in productos:
        datos = productos[nombre]

        print("\nProducto encontrado:")
        print("Nombre:", nombre.title())
        print(f"Precio: ${datos['precio']:.2f}")
        print("Cantidad disponible:", datos["cantidad"])

    else:
        print("\nEl producto no se encuentra registrado.")

def eliminar_producto():
    nombre = input("Ingrese el producto que desea eliminar: ").strip().lower()

    if nombre in productos:
        del productos[nombre]
        print("\nProducto eliminado correctamente.")

    else:
        print("\nEl producto no se encuentra registrado.")

def calcular_inventario():
    total = 0

    for datos in productos.values():
        total += datos["precio"] * datos["cantidad"]

    print(f"\nValor total del inventario: ${total:.2f}")

def mostrar_menu():
    print("     REGISTRO DE PRODUCTOS")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Calcular valor del inventario")
    print("6. Salir")
   
while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        calcular_inventario()

    elif opcion == "6":
        print("\nGracias por utilizar el programa.")
        print("Programa finalizado.")
        break

    else:
        print("\nOpción incorrecta. Intente nuevamente.")

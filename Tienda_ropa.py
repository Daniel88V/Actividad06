productos = {}
print("Bienvenido a la tienda de ropa")
print("Cuantos productos desea ingresar?")
cantidad = int(input())
for i in range(cantidad):
    print(f"Producto {i+1}")
    while True:
        codigo = input(f"Ingrese el código del producto: ")
        if codigo in productos:
            print(f"Error, codigo existente. Pruebe de nuevo")
        else:
            break
    nombre = input(f"Ingrese el nombre del producto: ")
    categoria = input(f"Ingrese la categoria del producto: ")
    talla =input(f"Ingrese la talla del producto: ")

    precio = float(input(f"Ingrese el precio del producto: "))
    cantidad = int(input(f"Ingrese la cantidad del producto: "))
    productos[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "talla": talla,
        "precio": precio,
        "cantidad": cantidad,
    }
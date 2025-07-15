productos = {}
print("Bienvenido a la tienda de ropa")
print("¿Cuántos productos desea ingresar? ")
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
    while True:
        try:
            precio = float(input(f"Ingrese el precio del producto: "))
            if precio > 0:
                break
            else:
                print("Error, por favor ingrese un precio mayor a 0")
        except ValueError:
            print("Por favor ingrese un número valido")
    while True:
        existencias = int(input(f"Ingrese la cantidad del producto: "))
        if existencias > 0:
            break
        else:
            print("Error, por favor ingrese una cantidad mayor a 0")
    productos[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "talla": talla,
        "precio": precio,
        "cantidad": existencias,
    }
print("¿Desea realizar alguna de las siguientes acciones: ?")
print("1. Mostrar lista de productos")
print("2. Buscar producto")
print("3. Calcular coste de inventario")
print("4. Mostrar productos por categoría")
print("5. Salir")
opcion = input()
if opcion == "1":
    print("---Lista de productos---")
    for codigo, datos in productos.items():
        print(f"Codigo: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Categoría: {datos['categoria']}")
        print(f"Talla: {datos['talla']}")
        print(f"Precio: {datos['precio']}")
        print(f"Cantidad: {datos['cantidad']}")
elif opcion == "2":
    print("---Buscar producto---")
    objeto = input("Ingrese el codigo del producto: ")
    if objeto in productos:
        print(f"Nombre: {productos[objeto]['nombre']}")
        print(f"Categoria: {productos[objeto]['categoria']}")
        print(f"Talla: {productos[objeto]['talla']}")
        print(f"Precio: {productos[objeto]['precio']}")
        print(f"Cantidad: {productos[objeto]['cantidad']}")
elif opcion == "3":
    costo = 0
    print("---Coste de inventario---")
    for producto in productos.values():
        costo += producto['precio'] * producto['cantidad']
    print(f"El costo del inventario es de: {costo:.2f}")
elif opcion == "4":
    print("---Mostrar productos (por categoría)---")
    busqueda = input("Ingrese la categoria del producto: ")
    bandera = False
    for codigo, buscar in productos.items():
        if buscar["categoria"].lower() == buscar.lower():
            if not bandera:
                print(f"***Productos en la categoría {buscar}:***")
            print(f"Código: {codigo}")
            print(f"Nombre: {buscar['nombre']}")
            print(f"Categoria: {buscar['categoria']}")
            print(f"Talla: {buscar['talla']}")
            print(f"Precio: {buscar['precio']}")
            print(f"Cantidad: {buscar['cantidad']}")
            bandera = True
    if not bandera:
        print("No se encontró nigun producto de esta categoría")


# Vas a crear un programa que administre productos de una tienda:
# agregar, ver, actualizar cantidades, y calcular el valor total del inventario.

inventario = [
    {"nombre": "Camiseta", "precio": 25000, "cantidad": 10},
    {"nombre": "Pantalón", "precio": 60000, "cantidad": 5},
    {"nombre": "Zapatos", "precio": 120000, "cantidad": 3},
]

def mostrar_inventario(lista):
    for i, producto in enumerate(lista, start=1):
        subtotal_producto = int(producto["precio"] * producto["cantidad"])
        print(f"""
{i}. {producto["nombre"]} - {producto['precio']} x {producto['cantidad']} = {subtotal_producto}
""")
    return

def valor_total(lista):
    total = 0
    for producto in lista:
        total = total + (producto["precio"] * producto["cantidad"])
    return total

ses = True

while ses == True:
    opcion = int(input("""Que desea hacer: 
1. Ver inventario
2. Agregar producto
3. Actualizar cantidad de un producto
4. Actualizar precio de un producto
5. Ver valor total del inventario
6. Salir
elija una opcion: """))
    if opcion == 1:
        mostrar_inventario(inventario)
    elif opcion == 2:
        nombre_producto_nv = input("Escriba el nombre del producto: ")
        precio_producto_nv = int(input("Escriba el precio del producto: "))
        cantidad_producto_nv = int(input("Escriba la cantidad del producto: "))
        inventario.append({"nombre": nombre_producto_nv, "precio": precio_producto_nv, "cantidad": cantidad_producto_nv})
    elif opcion == 3:
        mostrar_inventario(inventario)
        producto_actualizar = int(input("Que producto desea actualizar?: "))
        producto_actualizar -= 1
        producto_cantidad_actualizar = int(input("Cual es la nueva cantidad?: "))
        inventario[producto_actualizar]["cantidad"] = producto_cantidad_actualizar
    elif opcion == 4:
        mostrar_inventario(inventario)
        precio_producto_actualizar = int(input("Que producto desea actualizar: "))
        precio_producto_actualizar -= 1
        precio_producto_actualizar_num = int(input("Cual es el precio nuevo?: "))
        inventario[precio_producto_actualizar]["precio"] = precio_producto_actualizar_num
    elif opcion == 5:
        print(f"El valor total es: {valor_total(inventario)}")
    elif opcion == 6:
        ses = False
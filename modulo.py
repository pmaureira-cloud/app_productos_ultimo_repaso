# actualizar_precio
# agregar_producto
# eliminar_producto
# mostrar_producto

#-----FUNCIONES VALIDADORAS------
def validar_codigo(codigo, producto):
    # No vacío
    if len(codigo.strip()) == 0:
        return False
    # Sin espacios en blanco
    if " " in codigo:
        return False
    # no existente previamente.
    for clave in producto.keys():
        if codigo == clave:
            return False
    return True
def validar_nombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    else:
        return False
def validar_categoria(categoria):
    if len(categoria.strip()) > 0:
        return True
    else:
        return False
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False
def validar_disponible(disponible):
    if disponible == "S" or disponible == "N":
        return True
    else:
        return False
def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        return False
def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    else:
        return False
#--FUNCIONES DE BUSQUEDA --
# buscar_codigo   
def buscar_codigo(codigo, producto):
    for clave in producto.keys():
        if codigo == clave:
            print(f"Producto : {producto[clave][0]}")
            return True
# stock_categoria
def stock_categoria(categoria, producto, inventario):
    stock_total = 0 
    for clave in producto.keys():
        if categoria.upper() == producto[clave][1].upper():
            #sumamos su stock al acumulador
            stock_total += inventario[clave][0]
    print(f"El stock total es: {stock_total}")
# buscar_precio
def buscar_por_precio(precio_min, precio_max, producto, inventario):
    print(f"\n=== Productos entre ${precio_min} y ${precio_max} ===")
    productos_filtrados = []
    for clave in producto.keys():
        # Aseguramos que la clave exista también en el inventario para no lanzar error
        if clave in inventario:
            stock = inventario[clave][0]      # Índice 0 de inventario = Stock
            # El precio se saca del diccionario producto, índice 2
            precio = producto[clave][2]       
            nombre_producto = producto[clave][0]  # Índice 0 de producto = Nombre
            # Filtramos con las condiciones correctas usando el precio real
            if precio_min <= precio <= precio_max and stock > 0:
                productos_filtrados.append(f"{nombre_producto}--{clave}")
    # Mostramos los resultados ordenados
    if productos_filtrados:
        productos_filtrados.sort()
        for prod in productos_filtrados:
            print(prod)
    else:
        print("No se encontraron productos en ese rango de precios con stock disponible.")
# actualizar_precio
def actualizar_precio(codigo, nuevo_precio, productos):
# Si existe, actualizamos el precio. 
# Asumiendo que el precio es el segundo elemento [2] de la lista en ese código
    if codigo in productos.keys():
        productos[codigo][2] = nuevo_precio
        return True
    else:
        return False
# eliminar_producto
def eliminar_producto(codigo, productos, inventario):
    # Verificamos si existe en productos (o inventario, da igual porque comparten el código)
    if codigo in productos:
        # Eliminamos el producto de ambos diccionarios usando 'del'
        del productos[codigo]
        del inventario[codigo]
        return True
    else:
        return False

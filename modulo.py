import os
#EN ESTE ARCHIVO TENDREMOS: 
# Validar_ ... 
# buscar_codigo
# stock_categoria
# buscar_precio
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


# buscar_codigo
# stock_categoria
# buscar_precio
# actualizar_precio
# agregar_producto
# eliminar_producto
# mostrar_producto
os.system('cls')

# print("Estas en el archivo modulos")
##FUNCIONES MENU
#def stock_por_categoria()
    #print("Agregando")
#def buscar_por_precio()
    
#def actualizar_precio()
    
#def agregar_producto()
    
#def eliminar_producto()

#def mostrar_productos()
        
#def salir()
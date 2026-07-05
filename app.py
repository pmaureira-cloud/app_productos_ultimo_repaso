import os
#import modulo as me

#EN ESTE ARCHIVOS CREAREMOS :
# Crear Diccionarios, 
# Menú principal, (listo)
# Solicitar datos, (listo)
# Validar,
# Llamados

#-----CREANDO LOS DICCIONARIOS------
dic_inventario = {}
dic_productos = {}

#-----FUNCIONES VALIDADORAS------
def validar_codigo(codigo):
    # No vacío
    if len(codigo.strip()) == 0:
        return False
    # Sin espacios en blanco
    if " " in codigo:
        return False
    # no existente previamente.
    for clave in dic_productos.keys():
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
    
while True:    
    #MENU PRINCIPAL

    def leer_opcion():
        os.system('cls')
        while True:
            try:
                opcion = int(input("""
                

                ========= MENU PRINCIPAL =========
                1. STOCK POR CATEGORIA
                2. BUSCAR POR RANGO DE PRECIO
                3. ACTUALIZAR PRECIO
                4. AGREGAR PRODUCTOS
                5. ELIMINAR PRODUCTOS
                6. MOSTRAR PRODUCTOS
                7. SALIR
                ==================================
                >>INGRESA UNA OPCIÓN : 
                """))
                
                match opcion:
                    case 1:
                        #me.stock_por_categoria()
                        print("STOCK POR CATEGORIA")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 2:
                        #me.buscar_por_precio()
                        print("BUSCAR POR RANGO DE PRECIO")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 3:
                        #me.actualizar_precio()
                        print("ACTUALIZAR PRECIO")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 4:
                        print("AGREGAR PRODUCTOS")
                        #input("\nPresione Enter para continuar...")
                        agregar_producto()
                        os.system('cls')
                    case 5:
                        #me.eliminar_producto()
                        print("ELIMINAR PRODUCTOS")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 6:
                        mostrar_productos(dic_productos, dic_inventario)
                        
                        os.system('cls')
                    case 7:
                        #me.salir()
                        print("Gracias por usar el programa... Hasta luego")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case _:
                        print("Debe seleccionar una opción válida")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                return opcion
            except ValueError:
                print("Ingresa un número entero")
                input("\nPresione Enter para continuar...")
                os.system('cls')
    
    #========================================

    #-----FUNCIONES SOLICITAR DATOS------
    #opcion 4 "agregar productos"
            
    def agregar_producto():
        os.system('cls')
        print("AGREGA UN PRODUCTO:")
        
        #--solicita codigo
        os.system('cls')
        codigo = str(input("Ingresa código : ")).strip().upper()
        while not validar_codigo(codigo):
            print("ERROR. Codigo no es válido")
            codigo = str(input("Ingresar código : ")).strip().upper()
            
        #--solicita nombre producto
        nombre = str(input("Ingresa Nombre : ")).strip().upper()
        while not validar_nombre(nombre):
            nombre = str(input("Debes ingresar Nombre : ")).strip().upper()
                
        #--solicita categoria
        categoria = str(input("Ingresa Categoría : ")).strip().upper()
        while not validar_categoria(categoria):
            categoria = str(input("Debes ingresar Categoría : ")).strip().upper()
        
        #--solicita el Precio
        while True:
            try:
                precio = int(input("Ingresa Precio $ "))
                if validar_precio(precio):
                    break
                else:
                    print("ERROR. El precio debe ser un número mayor que 0")
            except ValueError:
                print("ERROR. Debe ingresar un número entero")
                
        #--solicita stock
        while True:
            try:
                stock = int(input("Ingresa stock: "))
                if validar_stock(stock):
                    break
            except ValueError:
                print("ERROR. Debe ingresar un número entero")
        
        #--solicita vendidos
        while True:
                    try:
                        vendidos = int(input("Ingresa vendidos: "))
                        if validar_vendidos(vendidos):
                            break
                    except ValueError:
                        print("ERROR. Debe ingresar un número entero")
                        
        #--solicita disponible
        disponible = str(input("¿Está disponible para la venta? (S/N): ")).strip().upper()
        while not validar_disponible(disponible):
            disponible = str(input("¿Disponible para la venta? (S/N): ")).strip().upper()
        #transformamos a True o False real para el diccionario:
        disponible = True if disponible == "S" else False
        print(f"""
            PRODUCTO AGREGADO  
            ===========================
            Código ID : {codigo}
            Nombre : {nombre}
            Categoría : {categoria}
            Precio $ {precio}
            Disponible : {disponible}
            Stock : {stock}
            Vendidos : {vendidos}
            ===========================
            """)
        
        #CREAMOS EL OBJETO DEL DIC PRODUCTO
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "disponible": disponible,
            "stock": stock,
            "vendidos": vendidos
        }
        
        #CREAMOS EL OBJETO DEL DIC INVENTARIO
        inventario = {
            "codigo": codigo,
            "stock": stock,
            "vendidos": vendidos
                }
        
        #AGREGAMOS AL DIC DE PRODUCTO 
        dic_productos[codigo] = producto
        
        #AGREGAMOS AL DIC DE INVENTARIO 
        dic_inventario[codigo] = inventario
        
        print("Producto Agregado")
        input("\nEnter para continuar...")
    
    
    
    #opcion 5 "eliminar productos"
    
    
    
    #opcion 6 "mostrar productos"
    def mostrar_productos(dic_productos, dic_inventario):
        os.system('cls')
        print("================================")
        print("=======LISTA DE PRODUCTOS=======")
        print("================================")        
        if len(dic_productos) == 0:
            print("El inventario está vacío. \nNo hay productos que mostrar.")
        else:
            # Recorremos el diccionario usando .items()
            for codigo, datos in dic_productos.items():
                print(f"CÓDIGO ID  : {codigo}")
                print("---------------------------------------")
                print(f"Nombre     : {datos['nombre']}")
                print(f"Categoría  : {datos['categoria']}")
                print(f"Precio     : ${datos['precio']}")
                print(f"Disponible : {datos['disponible']}")
                print(f"Stock      : {dic_inventario[codigo]['stock']}")
                print(f"Vendidos   : {dic_inventario[codigo]['vendidos']}")
                print("=======================================")
        input("\nPresione Enter para regresar al menú...")
        
    #-----FUNCIONES LLAMADOS -----


    #========================================
    #LLAMADO A LA FUNCION leer_opcion() DEL MENU PRINCIPAL 
    leer_opcion()
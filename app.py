import os
#import modulo as me

#EN ESTE ARCHIVOS CREAREMOS :
# Crear Diccionarios, 
# Menú principal, (listo)
# Solicitar datos, 
# Validar,
# Llamados

#-----CREANDO LOS DICCIONARIOS------
dic_inventario = {}
dic_productos = {}

#-----FUNCIONES VALIDADORAS------

#-----FUNCIONES VALIDAR ------
def validar_codigo(codigo):
    # No vacío Y  no espacios
    if len(codigo.strip()) > 0:
        return True
    else:
        return False
    # no existente previamente. 
    for clave in dic_productos.keys():
        if codigo == clave:
            return False
        else:
            return True
    # Retorna True/False    
    

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
    
while True:    
    #MENU PRINCIPAL

    def leer_opcion():
        os.system('cls')
        while True:
            try:
                opcion = int(input("""Bienvenido, ¿qué quieres hacer? : \n

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
                        mostrar_productos(dic_productos)
                        
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
        
        #--------solicita codigo
        os.system('cls')
        codigo = str(input("Ingresa código : ")).strip().upper()
        while not validar_codigo(codigo):
            codigo = str(input("debes ingresar el código : ")).strip().upper()
            
        #--------solicita nombre producto
        nombre = str(input("Ingresa Nombre : ")).strip().upper()
        while not validar_nombre(nombre):
            nombre = str(input("Debes ingresar Nombre : ")).strip().upper()
                
        #--------solicita categoria
        categoria = str(input("Ingresa Categoría : ")).strip().upper()
        while not validar_categoria(categoria):
            categoria = str(input("Debes ingresar Categoría : ")).strip().upper()
        
        #--------solicita el Precio
        while True:
            try:
                precio = int(input("Ingresa Precio $ "))
                if validar_precio(precio):
                    break
                else:
                    print("ERROR. El precio debe ser un número mayor que 0")
            except ValueError:
                print("ERROR. Debe ingresar un número entero")

        #--------solicita disponible
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
            ===========================
            """)
        
        #CREAMOS EL OBJETO DEL DICCIONARIO
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "disponible": disponible
        }
        
        #AGREGAMOS AL DICCIONARIO EL OBJETO 
        dic_productos[codigo] = producto
        
        print("Producto Agregado")
        input("\nEnter para continuar...")
    
    #opcion 5 "eliminar productos"
    
    #opcion 6 "mostrar productos"
    def mostrar_productos(dic_productos):
        os.system('cls')
        print("================================")
        print("======MOSTRANDO  PRODUCTOS======")
        print("================================")        
        if len(dic_productos) == 0:
            print("El inventario está vacío. No hay productos que mostrar.")
        else:
            # Recorremos el diccionario usando .items()
            # 'codigo' se queda con la clave (P101) y 'datos' con el diccionario interno
            for codigo, datos in dic_productos.items():
                print(f"CÓDIGO     : {codigo}")
                print(f"Nombre     : {datos['nombre']}")
                print(f"Categoría  : {datos['categoria']}")
                print(f"Precio     : ${datos['precio']}")
                print(f"Disponible : {datos['disponible']}")
                print("================================")
            
        input("\nPresione Enter para regresar al menú...")
    #-----FUNCIONES LLAMADOS -----


    #========================================
    #LLAMADO A LA FUNCION leer_opcion() DEL MENU PRINCIPAL 
    leer_opcion()
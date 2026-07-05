import modulo as me
import os

#EN ESTE ARCHIVOS CREAREMOS :
# Crear Diccionarios, 
# Menú principal, (listo)
# Solicitar datos, (listo)
# Validar,
# Llamados

#LISTAS DE PRUEBA 
dic_productos = {
    "P101": ["MORA", "FRUTAS", 1200, True],  #[nombre, categoria, precio, disponible]
    "P102": ["FRESAS", "FRUTAS", 4800, True],
    "P103": ["ARANDANOS", "FRUTAS", 3800, False],
    "P104": ["TOMATE", "VERDURAS", 4300, True],
    "P105": ["LECHUGA", "VERDURAS", 2800, True],
    "P106": ["LIMONES", "VERDURAS", 3200, True],
    "P107": ["ARROZ", "ABARROTES", 2800, True],
    "P108": ["HARINA", "ABARROTES", 1800, False],
    "P109": ["TALLARINES", "ABARROTES", 1800, False]
}

dic_inventario = {
    "P101": [30, 12],  # [stock, vendidos]
    "P102": [0, 11],
    "P103": [49, 33],
    "P104": [70, 3],
    "P105": [32, 10],
    "P106": [43, 9],
    "P107": [53, 0],
    "P108": [43, 29],
    "P109": [43, 14]
}
        
#-----CREANDO LOS DICCIONARIOS------
dic_inventario = {}
dic_productos = {}

#MENU PRINCIPAL
while True: 
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

    #--FUNCIONES SOLICITAR DATOS--
    #opcion 4 "agregar productos"
    def agregar_producto():
        os.system('cls')
        print("AGREGA UN PRODUCTO:")
        os.system('cls')
        #--CODIGO
        codigo = str(input("Ingresa código : ")).strip().upper()
        while not me.validar_codigo(codigo, dic_productos):
            print("ERROR. Codigo no es válido")
            codigo = str(input("Ingresar código : ")).strip().upper()
            
        #--NOMBRE
        nombre = str(input("Ingresa Nombre : ")).strip().upper()
        while not me.validar_nombre(nombre):
            nombre = str(input("Debes ingresar Nombre : ")).strip().upper()
                
        #--CATEGORIA
        categoria = str(input("Ingresa Categoría : ")).strip().upper()
        while not me.validar_categoria(categoria):
            categoria = str(input("Debes ingresar Categoría : ")).strip().upper()
        
        #--PRECIO
        while True:
            try:
                precio = int(input("Ingresa Precio $ "))
                if me.validar_precio(precio):
                    break
                else:
                    print("ERROR. El precio debe ser un número mayor que 0")
            except ValueError:
                print("ERROR. Debe ingresar un número entero")
                
        #--STOCK
        while True:
            try:
                stock = int(input("Ingresa stock: "))
                if me.validar_stock(stock):
                    break
            except ValueError:
                print("ERROR. Debe ingresar un número entero")
        
        #--VENDIDOS
        while True:
                    try:
                        vendidos = int(input("Ingresa vendidos: "))
                        if me.validar_vendidos(vendidos):
                            break
                    except ValueError:
                        print("ERROR. Debe ingresar un número entero")
                        
        #--DISPONIBLE
        disponible = str(input("¿Está disponible para la venta? (S/N): ")).strip().upper()
        while not me.validar_disponible(disponible):
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

        #GUARDANDO EN LISTAS
        lista_productos = [nombre, categoria, precio, disponible]
        lista_inventario = [stock, vendidos]
        

        #AGREGANDO LISTAS A LOS DICCIONARIOS
        dic_productos[codigo] = lista_productos  
        dic_inventario[codigo] = lista_inventario 
        
        print("Producto Agregado con éxito")
        input("\nEnter para continuar...")
    
    
    #opcion 5 "eliminar productos"
    
    
    #opcion 6 "mostrar productos"
    def mostrar_productos(dic_productos, dic_inventario):
        os.system('cls')
        print("========================================")
        print("           LISTA DE PRODUCTOS           ")
        print("========================================")        
        if len(dic_productos) == 0:
            print("El inventario está vacío. \nNo hay productos que mostrar.")
        else:
            # Recorremos el diccionario usando .items()
            for codigo, datos in dic_productos.items():
                print(f"CÓDIGO ID  : {codigo}")
                print("----------------------------------------")
                print(f"Nombre     : {datos[0]}")
                print(f"Categoría  : {datos[1]}")
                print(f"Precio     : ${datos[2]}")
                print(f"Disponible : {datos[3]}")
                print(f"Stock      : {dic_inventario[codigo][0]}")
                print(f"Vendidos   : {dic_inventario[codigo][1]}")
                print("----------------------------------------")
        input("\nPresione Enter para regresar al menú...")
        
    #========================================
    #LLAMADO A LA FUNCION leer_opcion() DEL MENU PRINCIPAL 
    leer_opcion()
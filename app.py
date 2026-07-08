import modulo as me
import os
#EN ESTE ARCHIVOS CREAREMOS : # Crear Diccionarios, Menú principal, (listo), Solicitar datos, (listo), Validar, Llamados
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
                    case 1: # BUSCAR STOCK POR CATEGORÍA
                        print("BUSCAR STOCK POR CATEGORÍA")
                        categoria = input("Ingrese categoría a buscar: ").strip().upper()
                        #Llamamos a la función pasando 'categoria' y los diccionarios reales
                        #Nota: Asegúrate de usar los nombres de tus diccionarios (ej. dic_productos, dic_inventario)
                        me.stock_categoria(categoria, dic_productos, dic_inventario)
                        input("\nPresione Enter para continuar...")
                    case 2: #BUSCAR POR RANGO DE PRECIOS
                        print("BUSCAR POR RANGO DE PRECIOS")                        
                        #Ingresa precio mínimo
                        while True:
                            try:
                                precio_min = int(input("Ingrese precio mínimo: "))
                                break
                            except ValueError:
                                print("Error: Ingrese un número válido.")
                        #Ingresa precio máximo 
                        while True:
                            try:
                                precio_max = int(input("Ingrese precio máximo: "))
                                break
                            except ValueError:
                                print("Error: Ingrese un número válido.")
                        else:
                            print("No se encontraron productos en ese rango de precios con stock disponible.")
                        # 3. ¡AQUÍ SÍ! Ahora que las variables ya existen con sus datos, llamas a la función
                        me.buscar_por_precio(precio_min, precio_max, dic_productos, dic_inventario)
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 3: #ACTUALIZAR PRECIOS
                        print("ACTUALIZAR PRECIOS")
                        continuar = "S"
                        while continuar.upper() == "S":
                            codigo = input("\nIngrese el código a buscar: ").strip().upper()
                            # 1. Buscas en dic_productos (imprime el nombre)
                            if me.buscar_codigo(codigo, dic_productos): 
                                # 2. Pides el nuevo precio entero
                                while True:
                                    try:
                                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                                        if nuevo_precio < 0:
                                            print("El precio no puede ser negativo.")
                                            continue
                                        break
                                    except ValueError:
                                        print("Error: Ingrese un número válido.")
                                # 3. ¡CAMBIO AQUÍ!: Le pasas dic_productos para modificar el índice [2]
                                me.actualizar_precio(codigo, nuevo_precio, dic_productos)
                                print("¡Precio actualizado con éxito!")
                            else:
                                print("Código inexistente")
                            continuar = input("\n¿Desea buscar y actualizar otro código? (s/n): ").strip().upper()
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 4: #AGREGAR PRODUCTO
                        print("AGREGAR PRODUCTOS")
                        #input("\nPresione Enter para continuar...")
                        agregar_producto()
                        os.system('cls')
                    case 5: #ELIMINAR PRODUCTO
                        print("ELIMINAR PRODUCTO")
                        continuar = "S"
                        while continuar.upper() == "S":
                            codigo = input("\nIngrese el código del producto a eliminar: ").strip().upper()
                            
                            # 1. Buscamos el código en productos (imprime el Nombre en pantalla: MORA, etc.)
                            if me.buscar_codigo(codigo, dic_productos):
                                
                                # 2. Pregunta de seguridad antes de borrar de verdad
                                confirmar = input("¿Desea eliminar permanentemente este producto? (S/N): ").strip().upper()
                                
                                if confirmar == "S":
                                    # 3. Llamamos a la función pasando AMBOS diccionarios
                                    me.eliminar_producto(codigo, dic_productos, dic_inventario)
                                    print("¡Producto eliminado con éxito de todo el sistema!")
                                else:
                                    print("Operación cancelada. El producto no fue eliminado.")
                                    
                            else:
                                print("Código inexistente")
                            
                            # Pregunta de continuidad para el bucle
                            continuar = input("\n¿Desea eliminar otro código? (s/n): ").strip().upper()
                        
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                    case 6: #MOSTRAR PRODUCTO
                        mostrar_productos(dic_productos, dic_inventario)
                        os.system('cls')
                    case 7: #SALIR
                        print("\n========================================")
                        print("   ¡Gracias por usar el sistema! 👋")
                        print("========================================")
                        input("\nPresione Enter para salir...")
                        break # Este break rompe el "while True" principal del menú y cierra el programa
                    case _: #DEFAULT ERRORES
                        print("Debe seleccionar una opción válida")
                        input("\nPresione Enter para continuar...")
                        os.system('cls')
                return opcion
            except ValueError:
                print("Ingresa un número entero")
                input("\nPresione Enter para continuar...")
                os.system('cls')
    #========================================
    #opcion 4 "agregar productos"
    def agregar_producto(): #FUNCION AGREGAR PRODUCTOS
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
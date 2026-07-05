**Restricciones Generales del Proyecto**
• Todo el sistema debe desarrollarse mediante funciones. 
• No se permite utilizar variables globales.
• Los diccionarios deben crearse únicamente en app.py y enviarse como parámetros.
• Las funciones de validación únicamente retornan True o False y NINGUNA debe imprimir mensajes en pantalla.
• El programa principal (app.py) será el encargado de la interacción con el usuario y mostrar mensajes.
• Debe utilizarse manejo de excepciones (try-except) para todas las entradas numéricas.
• La búsqueda de códigos y categorías no debe distinguir entre mayúsculas y minúsculas.

**VALIDACIONES**
*PARA AGREGAR PRODUCTOS*
Solicita todos los campos validando de forma independiente mediante las siguientes funciones:

• (LISTO) validar_codigo(codigo): No vacío, no espacios, no existente previamente. Retorna True/False.
• (LISTO) validar_nombre(nombre): No vacío, no espacios. Retorna True/False.
• (LISTO) validar_categoria(categoria): No vacío, no espacios. Retorna True/False.
• (LISTO) validar_precio(precio): Entero mayor que cero. Retorna True/False.
• (LISTO) validar_disponible(opcion): Valida 's' o 'n' y convierte internamente a True/False. Retorna True/False.
• (LISTO) validar_stock(stock): Entero mayor o igual a cero. Retorna True/False.
• (LISTO) validar_vendidos(vendidos): Entero mayor o igual a cero. Retorna True/False.
Función de Transacción:

**FUNCIONES MENU PRINCIPAL**
======= MENU PRINCIPAL =======
1. STOCK POR CATEGORIA 
2. BUSCAR POR RANGO DE PRECIO
3. ACTUALIZAR PRECIO
4. AGREGAR PRODUCTOS  (LISTO) 
5. ELIMINAR PRODUCTOS
    eliminar_producto(codigo, productos, inventario) -> Retorna True/False
6. MOSTRAR PRODUCTOS  (LISTO)  
7. SALIR
==============================
>>INGRESA UNA OPCIÓN :
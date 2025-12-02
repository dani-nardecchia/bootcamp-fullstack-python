# definiremos el menu principal LISTO 

def mostrar_menu():
    saludo = "Bienvenido/a a tu Ecommerce" \
        "\n 1. Ver catálogo de productos" \
        "\n 2. Buscar producto por nombre o categoría" \
        " \n 3. Agregar producto al carrito  " \
        "\n 4. Ver carrito y total" \
        "\n 5. Vaciar carrito " \
        "\n 0. Salir"
    print(saludo)

# creacion de diccionarios con productos LISTO  
#Creamos los diccionarios con los datos de las plantas, prints y botellas con imagenes que tendria mi tienda ficticia 
planta_1 = {'id': 'p1', 'nombre' :'Planta de Alstromeria pellegrina', 'categoria': "planta" , 'precio' : 5000}
planta_2 = {'id': 'p2', 'nombre' :'Planta de Puya venusta', 'categoria': "planta" , 'precio' : 1500}
planta_3 = {'id': 'p3', 'nombre' :'Planta de Solanum maritimum', 'categoria': "planta" , 'precio' : 2500}

print_1 = {'id': 'f1', 'nombre' :'Print de Alstromeria pellegrina', 'categoria': "print" , 'precio' : 2500}
print_2 = {'id': 'f2', 'nombre' :'Print de Puya venusta', 'categoria': "print" , 'precio' : 2500}
print_3= {'id': 'f3', 'nombre' :'Print de Solanum maritimum', 'categoria': "print" , 'precio' : 2500}

bot_1 = {'id': 'b1', 'nombre' :'Botella de Alstromeria pellegrina', 'categoria': "botella" , 'precio' : 7000}
bot_2 = {'id': 'b2', 'nombre' :'Botella de Puya venusta', 'categoria': "botella" , 'precio' : 7000}
bot_3= {'id': 'b3', 'nombre' :'Botella de Solanum maritimum', 'categoria': "botella" , 'precio' : 7000}

#Creamos una lista con los diccionarios
productos = [planta_1, planta_2, planta_3, print_1, print_2, print_3, bot_1, bot_2, bot_3]

#  Opcion 1: Ver catalogo de productos  LISTO 
def ver_catalogo():
    print("-----------------------------" \
            "Catálogo de productos"
            "-----------------------------")
    for producto in productos:
        print(f"""Nombre: {producto["nombre"]} Categoria: {producto["categoria"]} Precio: {producto["precio"]} Id: {producto["id"]}""")


#  Opcion 2: Búsqueda de productos LISTA 
# - Permitir buscar productos por nombre o por categoría.
# Mostrar todos los productos que coincidan con el texto ingresado (ej: si escribe “ropa”, mostrar todas las prendas)

def buscar_productos():
    busqueda = input("Ingrese búsqueda:").lower().replace("á","a").replace("é", "e").replace("í","i").replace("ó","o").replace("ú","u") 

    for producto in productos: 
        if (busqueda in producto["nombre"].lower().replace("á","a").replace("é", "e").replace("í","i").replace("ó","o").replace("ú","u")) or (busqueda in producto["categoria"].lower().replace("á","a").replace("é", "e").replace("í","i").replace("ó","o").replace("ú","u")):
            print(producto['nombre'])


# Opcion 3: Agregar producto al carrito LISTO 
#definiremos el carrito de compras 

def agregar_carrito():
    carrito = []
    otra_compra = 1
    
    while otra_compra != 0:
        id_compra = input("Ingrese id del producto: ").lower()
        cant_compra = int(input("Ingrese la cantidad deseada: "))
        
        id_encontrado = False

        #aca busco si existe el producto
        for producto in productos: 
            if id_compra == producto["id"]:
                carrito.append([producto["nombre"], cant_compra]) 
                id_encontrado = True
                break  
        
        if id_encontrado == False:
            print("Id no encontrado")
        
        otra_compra = int(input("Ingrese 1 si desea hacer otra compra, 0 para salir: ")) 
        
        if otra_compra != 0 and otra_compra != 1:
            print("Opcion invalida. Ingrese solo 0 o 1.")
            otra_compra = int(input("Ingrese 1 si desea hacer otra compra, 0 para salir: "))
        
    
#Ver carrito y total (opción 4)
# - Listar los ítems del carrito: id, nombre, cantidad, precio unitario, subtotal.
# - Mostrar el total a pagar: suma de todos los subtotales.


#Vaciar carrito (opción 5)
#- Dejar el carrito vacío y mostrar un mensaje de confirmación.
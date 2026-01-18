#Creamos las clases de errores personalizadas 
class ProductoNoEncontradoError(Exception):
    pass

class StockInsuficienteError(Exception):
    pass 

class CantidadInvalidaError(Exception):
    pass 

class ProductoDuplicadoError(Exception):
    pass

#=======Clase principal inventario=========#

class Inventario():
    def __init__(self, nombre):
        self.nombre = nombre 
        self.productos = {"Carolina Herrera": 3, "Channel 5":5, 
                          "Anillo oro":2, "Cadena":4}
    
    def agregar_producto(self,nombre, cantidad):
        if cantidad <= 0:
            raise CantidadInvalidaError(f"Cantidad {cantidad} no es valida.")
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        print(f"Se ha actualizado el producto {nombre} con {cantidad} unidades.") 
        
        #if nombre in self.productos:
            #raise ProductoDuplicadoError (f"El producto {self.nombre} ya se encuentra en el catalogo.")
    
    def vender_producto(self, nombre, cantidad):
        if nombre not in self.productos:
            raise ProductoNoEncontradoError(f"Producto {nombre} no se encuentra en el catalogo.") 
        if cantidad <= 0:
            raise CantidadInvalidaError(f"Cantidad {cantidad} invalida.")
        if cantidad > self.productos[nombre]: 
            raise StockInsuficienteError(f"Stock insuficiente.")
        
        self.productos[nombre] -= cantidad 
        print(f"Venta realizada. {nombre}: {cantidad}")
    
    def consultar_stock(self,nombre):
        if nombre not in self.productos:
            raise ProductoNoEncontradoError(f"Producto {nombre} no se encuentra en el catalogo.")
        return self.productos[nombre]
    
    def eliminar_producto(self, nombre):
        if nombre not in self.productos:
            raise ProductoNoEncontradoError(f"Producto {nombre} no se encuentra en el catalogo.")
        
        del self.productos[nombre]
        print(f"Producto {nombre} eliminado.")
    
    def mostrar_inventario(self):
        print("Inventario actual\n")
        for producto, cantidad in self.productos.items():
            print(f"{producto}: {cantidad}")

#======Menu principal============# 
def mostrar_menu():
    """Muestra el menu de opciones"""
    print("\n" + "="*50)
    print("Sistema de gestion de inventario")
    print("="*50)
    print("1. Agregar nuevo producto")
    print("2. Vender producto")
    print("3. Consultar stock de un producto")
    print("4. Eliminar producto")
    print("5. Mostrar inventario completo")
    print("0. Salir")
    print("="*50)

#=======Crear obejto inventario===#
nombre_tienda = input("Ingrese el nombre de la tienda: ")
inventario = Inventario(nombre_tienda)

while True:
    mostrar_menu()
    try: 
        opcion = int(input("Ingrese opcion: "))
    except:
        print("Debe ingresar un numero.")
    
    if opcion == 0:
        break 
    
    elif opcion == 1: 
        try: 
            nombre_producto = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            inventario.agregar_producto(nombre_producto, cantidad)

        except (CantidadInvalidaError) as e:
            print(e)
    
    elif opcion == 2:
        try: 
            nombre_producto = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            inventario.vender_producto(nombre_producto, cantidad)
        except (CantidadInvalidaError, StockInsuficienteError,ProductoNoEncontradoError) as e:
            print(e)
    
    elif opcion == 3:
        try:
            nombre_producto = input("Ingrese nombre del producto: ")
            inventario.consultar_stock(nombre_producto)
        except (ProductoNoEncontradoError) as e:
            print(e)
    
    elif opcion == 4:
        try:
            nombre_producto = input("Ingrese nombre del producto: ")
            inventario.eliminar_producto(nombre_producto)
        except (ProductoNoEncontradoError) as e:
            print(e)
    elif opcion == 5:
        inventario.mostrar_inventario()
    else:
        print("Ingrese una opcion valida")
        continue

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio 
        print(f"Producto creado: {nombre} ${precio}")
    
    #==GETTERS 
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio 
    
    #==SETTERS 
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Inserte un precio mayor a 0.")
    
    def mostrar(self):
        print(f"Producto: {self.get_nombre()}: $ {self.get_precio()}")


class Carrito:
    def __init__(self, dueno):
        self.__dueno = dueno
        self.__productos = []
        print("Carrito creado para ", dueno)
    
    #==GETTERS 
    def get_dueno(self):
        return self.__dueno
    
    def get_productos(self):
        return self.__productos
    
    #==SETTERS 
    def set_dueno(self, nuevo_dueno):
        self.__dueno = nuevo_dueno 

    #crear metodo agregar_producto(producto): agrega un producto al carrito
    def agregar_producto(self, producto):
        self.__productos.append(producto)
        print(f"Se ha agregado el producto {producto.get_nombre()} a su carrito.")
    
    #mostrar_productos(): muestra todos los productos en el carrito
    #aca en la clase carrito, usamos el objeto productos de clase carrito 
    # para recorrerlo en su ciclo for 
    # y usamos el metodo mostrar de la clase producto para mostrar que productos
    # hay dentro de la lista productos  
    def mostrar_productos(self):
        for p in self.get_productos():
            p.mostrar()
    
    #calcular_total(): suma los precios de todos los productos
    def calcular_total(self):
        precio_total = 0 
        for p in self.get_productos():
            precio_total += p.get_precio()
            #si pusiera el return aqui dentro, me daria solo el valor
            #del primer producto y cerraria el ciclo. 
        return precio_total

#=================

p1 = Producto("Leche", 1290)
p2 = Producto("Queso", 2500)
p3 = Producto("Cereal", 2400)
p4 = Producto("Cafe", 3800)
p5 = Producto("Helado", 5990)
p6 = Producto("Jaleas", 340)

carro1 = Carrito("Raulito")
carro2 = Carrito("Dani")


carro1.agregar_producto(p4)
carro1.agregar_producto(p1)
carro1.mostrar_productos()
print(f"Valor total: {carro1.calcular_total()}")


carro2.agregar_producto(p1)
carro2.agregar_producto(p3)
carro2.mostrar_productos()
print(f"Valor total: {carro2.calcular_total()}")

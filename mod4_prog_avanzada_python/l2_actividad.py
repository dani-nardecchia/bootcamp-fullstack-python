class Editorial:
    def __init__(self, nombre, pais):
        self.__nombre = nombre
        self.__pais = pais 

    def get_nombre(self):
        return self.__nombre
    def get_pais(self):
        return self.__pais

class Libro:
    def __init__(self, titulo,autor,anio_pub, editorial_nombre, editorial_pais):
        self.__titulo = titulo
        self.__autor = autor 
        self.__anio_pub = anio_pub
        self.__editorial = Editorial(editorial_nombre, editorial_pais)
    
    #==GETTERS==# 
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_anio(self):
        return self.__anio_pub
    def get_editorial(self):
        return self.__editorial

    #====SETTERS==# 
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo   
    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor
    def set_anio(self, nuevo_anio):
        self.__anio_pub = nuevo_anio 
    def set_editorial(self, nueva_editorial):
        self.__anio_pub = nueva_editorial

    def mostrar_info(self):
        print(f"Título: {self.get_titulo()} \n")
        print(f"Autor: {self.get_autor()} \n")
        print(f"Año de publicación: {self.get_anio()}\n")
        print(f"Editorial: {self.get_editorial().get_nombre()}. País: {self.get_editorial().get_pais()}\n")
    
    def resumen(self,resumen = None):
        if resumen is None:
            print("Libro sin resumen disponible")
        elif isinstance(resumen,str):
            print(f"Resumen para este libro es: {resumen}")
        else:
            print("Por favor ingrese un resumen escrito.")




#==MAI1N==#
mi_libro = Libro("Bury our Bones", "V.E.Schwab","2025", "Tor Books", "USA")

mi_libro.set_titulo("Bury our Bones in the Midnight Soil")

mi_libro.mostrar_info()

mi_libro.resumen("This is a story about life, how it ends, and how it starts.")


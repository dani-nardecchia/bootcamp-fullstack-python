#¿Qué es la programación orientada a objetos?
#Es un paradigma o una manera de programar, donde organizamos el codigo usando objetos, 
#con atributos y metodos para representar cosas del mundo real. 

#¿En qué se diferencia de la programación estructurada?
#La programacion estructura usa mas funciones para organizar el codigo en cambio en la orientada a objetos 
#el codigo se centra en las clases y objetos y sus interacciones 

#Menciona un ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto.
#Por ejemplo un objeto auto, podria tener los atributos marca, modelo y color y 
#los metodos prender el auto, acelerar, frenar 

#En comentarios, explica la diferencia entre:
#Clase, instancia y objeto
#Una clase es la receta que define los objetos. Objeto e instancia son lo mismo
#un elemento concreto y en particular creado a partir de la clase. 

#Atributo y estado
#Un atributo es una de las variables que puede tener un objeto y el estado
#Es el conjunto de valores que tienen los atributos en este momento. 

#Método y comportamiento
#El metodo es una accion que puede tener un objeto, que se define en la clase. El comportamiento
#es como lo que el objeto en si puede hacer, usando los metodos.  



class Perro:
    nombre = ""
    edad = ""
    raza = ""

    def __init__(self, nombre, edad,raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza 
    
    def ladrar(self):
        print("Guau!! Guau!!")
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self._edad}, Raza: {self._raza}")


mi_perro = Perro("Toby","15","Quilterrier")

mi_perro.ladrar()

mi_perro.mostrar_info()

#Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo.

#La abstraccion es modelar algo del mundo real como un objeto en Python mostrando solo las 
#caracteristicas que mas importan. 
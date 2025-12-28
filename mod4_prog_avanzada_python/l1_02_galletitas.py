#creamos una clase y vemos la diferencia entre 
#atributos de clase y de instancia 
#y metodos de clase e instancia 

class Galleta:
    sabor = ""
    contador_galletas = 0 

    def __init__(self, sabor):
        self.sabor = sabor 
        #hacer el contador usando self. indica que cada objeto tiene su propio contador 
        #o sea cada galleta trata de llevar su propio contador, lo que no tiene sentido
        #self.contador_galletas+= 1 

        #la forma correcta seria 
        Galleta.contador_galletas += 1 
        #con esta sintaxis ahora el contador es de la clase 
        #es comun para todas las instancias y cada vez q se crea una, sube 

    
    def comer(self):
        print("Que rica galletita sabor ", self.sabor)

    #este metodo no lleva self dentro porque es un atributo de clase 
    #no de cada instancia 
    def imprime_contador_galletas():
        print("La cantidad de galletas es ", Galleta.contador_galletas)

#Asi se llamaria cuando lo teniamos como atributo de instancia 
#otra_mas.imprime_contador_galletas()

#creamos una galleta y llamamos al contador para ver si funciona 
primera_galletita = Galleta("chocolate")
Galleta.imprime_contador_galletas()
otra_galletita = Galleta("Coco")
Galleta.imprime_contador_galletas()
otra_mas = Galleta("Mantequilla")
Galleta.imprime_contador_galletas()
aun_otra_galletita = Galleta("Turron")
Galleta.imprime_contador_galletas()


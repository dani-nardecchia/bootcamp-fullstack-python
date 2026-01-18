#primero creamos una clase principal 
class Figura:
    def __init__(self, color, nombre):
        self.color = color
        self.nombre = nombre 
    
    #tiene un metodo para mostrar info 
    def mostrar_info(self):
        print(f"{self.nombre} - Color: {self.color}")
    #tiene un metodo calcular area que aca queda en cero 
    def calcular_area(self):
        return 0 

#ahora creamos una clase que hereda de esta 
class Cuadrado(Figura):
    #lleva todos los atributos de figura y ademas un atributo lado 
    def __init__(self, color, nombre, lado):
        #con super se llama al constructor de la clase padre
        super().__init__(color, nombre)
        self.lado = lado 
        print(f"Cuadrado {self.nombre} creado con lado = {self.lado}")
    
    #esta lleva un metodo calcular area que sobre escribira el anterior 
    def calcular_area(self):
        area = self.lado * self.lado 
        return area 
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cuadrado {self.nombre} con lado = {self.lado}")

#creamos otra clase 
class Circulo(Figura):
    def __init__(self, color, nombre, radio):
        super().__init__(color, nombre)
        self.radio = radio 
        print(f"Circulo {self.nombre} creado con radio = {self.radio}.")
    
    #esta lleva un metodo calcular area que sobre escribira el anterior 
    def calcular_area(self):
        area = 3.14 * self.radio*self.radio
        return area 
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Circulo {self.nombre} con radio = {self.radio}.")

#creamos una tercera clase 
class Triangulo(Figura):
    def __init__(self, color, nombre, base, altura):
        super().__init__(color, nombre)
        self.base = base
        self.altura = altura
        print(f"Triangulo {self.nombre} creado con Base = {self.base} y altura = {self.altura}")
    
    def calcular_area(self):
        area = (self.base * self.altura)/2
        return area
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Triangulo {self.nombre} con base = {self.base} y altura = {self.altura}")





#crearemos una de cada figura 
fig1 = Cuadrado("Verde", "Cuadrado xy", 3)
fig2 = Circulo("Morado", "Circulo abc", 2)
fig3 = Triangulo("Azul", "Triangulo sdf", 2,3)

print(f"El área del cuadrado es: {fig1.calcular_area()}")
print(f"El área del circulo es: {fig2.calcular_area()}")
print(f"El área del triangulo es: {fig3.calcular_area()}")


fig1.mostrar_info()
fig2.mostrar_info()
fig3.mostrar_info()

def mostrar_area_figura(figura):
    print(f"Calculando área de {figura.nombre}")
    print(f"Área: {figura.calcular_area()}")

mostrar_area_figura(fig1)
mostrar_area_figura(fig2)
mostrar_area_figura(fig3)
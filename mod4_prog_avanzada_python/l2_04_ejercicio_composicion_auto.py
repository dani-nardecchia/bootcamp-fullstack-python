class Motor:
    def __init__(self, tipo):
        self.__encendido = False #False indica q parte apagado 
        self.__tipo = tipo
    
    #====GETTERS====#
    def estado(self):
        if self.__encendido:
            return "Motor encendido"
        else:
            return "Motor Apagado"
        
    def get_tipo(self):
        return self.__tipo
    
    #===SETTERS===#
    def encender(self):
        if self.__encendido == False:
            self.__encendido = True 
            print("Se ha encendido el motor")
        else:
            ("El motor ya esta encendido")

    def apagar(self):
        if self.__encendido:
            self.__encendido = False 
            print ("Se ha apagado el motor")
        else:
            ("El motor ya esta apagado.")

class Auto:
    def __init__(self, marca, modelo, tipo):
        self.__marca = marca
        self.__modelo = modelo 
        self.__motor = Motor(tipo)
    
    #==GETTERS===#
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_motor(self):
        return self.__motor 
    
    #===SETTERS==# 
    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca
    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo
    def set_motor(self, nuevo_motor):
        self.__motor = nuevo_motor
    
    def encender_auto(self):
        self.__motor.encender()

    def apagar_auto(self):
        #self.__motor.apagar()
        #esto tambien se podria hacer con 
        #el get not retorna self.__motor 
        self.get_motor().encender
    
    def informacion(self):
        print(f"Auto marca: {self.get_marca()} \n")
        print(f"Auto modelo: {self.get_modelo()} \n")
        print(f"Tipo motor: {self.__motor.get_tipo()} \n")



#==============# 

mi_auto = Auto("Toyota", "Yaris","gasolina")




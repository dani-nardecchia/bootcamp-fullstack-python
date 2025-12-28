class ControlRemoto:
    def __init__(self, dispositivo):
        self.__dispositivo = dispositivo
        self.__canal = 1 
        self.__volumen = 20 
        self.__encendido = False #false indica que el dispositivo ta apagado 
        
        #ponemos un mensajito 
        print("Control para dispositivo ", dispositivo, "creado.")
    
    #==Getters==#
    def get_dispositivo(self):
        return self.__dispositivo
    
    def get_canal(self):
        return self.__canal
    
    def get_volumen(self):
        return self.__volumen
    
    def get_estado(self):
        if self.__encendido:
            return "Encendido"
        else:
            return "Apagado"
    
    #==Setters==# 

    #set_canal(nuevo_canal): cambia el canal (solo si está encendido y entre 1-99)
    def set_canal(self,nuevo_canal):
        if self.__encendido:
            if 1 <= nuevo_canal <= 99:
                self.__canal = nuevo_canal
            else:
                print("Canal fuera de rango. Eliga entre 1 - 99")
        else: 
            print("El dispositivo esta apagado")
        print("se ha cambiado el canal a ", self.__canal)

    #set_volumen(nuevo_volumen): cambia el volumen (solo si está encendido y entre 0-100)
    def set_volumen(self, nuevo_volumen):
        if self.__encendido: 
            if 0 <= nuevo_volumen <= 100:
                self.__volumen = nuevo_volumen
            else:
                print("Volumen debe ser entre 0 - 100.")
        else:
            print("El dispositivo esta apagado")
        print("se ha cambiado el volumen a ", self.__volumen)
    
    #set_encendido(estado): enciende/apaga (True/False)
    #aca no hay validacion, solo cambiamos el atributo al estado contrario
    def set_encendido(self):
        if self.__encendido:
            self.__encendido = False 
            print("Se ha apagado el dispositivo")
        else: 
            self.__encendido = True 
            print("Se ha prendido el dispositivo")
    
    #metodo con comportamiento adaptable 
    #el metodo debe hacer cuatro cosas diferente
    #dependiendo de que recibe: 
    #encender/apagar cambia el estado 
    #canal,15 cambia al canal indicado 
    #volumen, 75 cambia el volumen
    #subir_volumen/bajar_volumen sube/baja 10 puntos 
    #siguiente_canal/anterior_canal cambia al canal siguiente/anterior 

    #usamos valor = None para decirle el valor por default, si es que 
    #al llamar al metodo no ponemos nada 
    #asi no se rompe si no ingresamos el segundo parametro 
    def controlar(self,comando,valor = None):
        #encender/apagar cambia el estado 
        if comando == "encender" or comando == "apagar":
            #llamamos al metodo!! xq para eso sirven 
            self.set_encendido()
        
        elif comando == "canal":
            if valor is None:
                print("Debe indicar un canal")
            else:
                self.set_canal(valor)
        
        elif comando == "volumen":
            if valor is None:
                print("Debe indicar un volumen.")
            else:
                self.set_volumen(valor)
        
        #esta es la manera en que se me ocurrio a mi hacerlo
        #que involucra copiar/pegar y un codigo mas voluminoso 
        #subir_volumen/bajar_volumen sube/baja 10 puntos 

        elif comando == "subir_volumen":
            volumen = self.get_volumen()
            volumen_nuevo = volumen + 10
            self.set_volumen(volumen_nuevo)

        elif comando == "bajar_volumen":
            volumen = self.get_volumen()
            volumen_nuevo = volumen - 10
            self.set_volumen(volumen_nuevo)
        
        #hare el siguiente con la sugerencia de gepete 
        #que es mas conciso 
        #siguiente_canal/anterior_canal cambia al canal siguiente/anterior 

        elif comando in ("siguiente_canal", "anterior_canal"):
            canal = self.get_canal()
            cambio = 1 if comando == "siguiente_canal" else -1 
            self.set_canal(canal + cambio)
            

        
        



            




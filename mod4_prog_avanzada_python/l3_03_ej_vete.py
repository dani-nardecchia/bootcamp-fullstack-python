class Dueno: 
    def __init__(self, nombre, telefono):
        self.__nombre = nombre 
        self.__telefono = telefono 
        self.__mascotas = []
        print(f"Se ha creado el dueño {self.get_nombre()}")
    
    #==GETTERS==#
    def get_nombre(self):
        return self.__nombre
    def get_telefono(self):
        return self.__telefono
    def get_mascotas(self):
        return self.__mascotas
    
    #==SETTERS==#
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    def set_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono
    
    #def agregar_mascota(self,nueva_mascota):
        #for mascota in self.__mascotas:
            #if mascota == nueva_mascota:
                #print("La mascota ya existe.")
                #break 
            #else:
                #self.__mascotas.append(nueva_mascota)
                #print(f"Se ha añadido la mascota.")

    #Yo lo hice asi, pero gepete me mostro una forma mas corrcta
    #Y mas simple 

    def agregar_mascota(self, nueva_mascota):
        if nueva_mascota in self.__mascotas:
            print("La mascota ya existe.")
        else:
            self.__mascotas.append(nueva_mascota)
            print("Se ha añadido la mascota.")


    def mostrar_mascotas(self):
        print(f"Las mascotas de {self.get_nombre} son: ")
        #aca llamo al metodo get nombre de la clase mascota, para 
        #solo mostrar su nombre
        for mascota in self.__mascotas:
            print(f"- {mascota.get_nombre()}")
            
    def buscar_mascotas(self, nombre_mascota):
        for mascota in self.get_mascotas():
            if mascota.get_nombre() == nombre_mascota:
                print(f"La mascota {mascota} existe.")
                return 
        print("La mascota no existe.")



#primero creamos la clase padre 
class ContenidoDigital:
    def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion):
        self.__titulo = titulo
        self.__autor = autor 
        self.__fecha_pub = fecha_publicacion
        self.__duracion = duracion
        self.__calificacion = calificacion
    
    #no voy a hacer los getters y setter para centrarme en herencia 
    def reproducir(self):
        print(f"Reproduciendo {self.__titulo}")
    
    def calificar(self, nueva_calificacion):
        self.__calificacion = nueva_calificacion
    
    def es_largo(self):
        if self.__duracion > 30:
            return True
        
    #añadimos un metodo str 
    def __str__(self):
        imprime = f"CONTENIDO: {self.__titulo}\n"
        imprime += f"Autor: {self.__autor} | Duración: {self.__duracion} | Calificacion: {self.__calificacion} \n"
        return imprime 
                


#ahora haremos primera clase hija 
class Video(ContenidoDigital):
    def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, formato, resolucion):
        super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion)
        self.__formato = formato
        self.__resolucion = resolucion
    
    def subir_calidad(self):
        if self.__resolucion == "4K":
            print("No se puede subir a una resolucion mayor")
        elif self.__resolucion == "Full HD":
            self.__resolucion = "4K"
            print("Se ha subido la resolucion a 4K")
        else:
            self.__resolucion = "Full HD"
            print("Se ha subido la resolucion a Full HD")

    def agregar_subs(self, idioma):
        print("Subtítulos añadidos.")
    
    #el metodo str agarra el metodo de la clase padre y luego añade
    #cosas especificas a esta clase
    def __str__(self):
        imprime =  super().__str__()
        imprime += f"Formato: {self.__formato} | Resolucion: {self.__resolucion}\n"
        return imprime
    

#haremos otra clase hija 
class Podcast(ContenidoDigital):
    def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, invitados, tema):
        super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion)
        self.__invitados = invitados
        self.__tema = tema 
    
    def agregar_invitado(self, nuevo_invitado):
        self.__invitados.append(nuevo_invitado)
        print(f"Se ha añadido a {nuevo_invitado} a la lista de invitados.")

    def generar_transcripcion():
        print("Transcripción generada.")
    
    def __str__(self):
        imprime = super().__str__()
        imprime += f"Tema: {self.__tema} | Invitados: {self.__invitados}"
        return imprime 
    
#otra clase hija mas 
class LibroDigital(ContenidoDigital):
    def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, num_paginas, formato):
        super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion)
        self.__num_paginas = num_paginas
        self.__formato = formato 
    
    def marcar_pagina():
        return 
    
    def calcular_tiempo_lectura(self):
        return self.__num_paginas/2 
    
    def __str__(self):
        imprime =  super().__str__()
        imprime += f"Numero paginas: {self.__num_paginas} | Formato lectura: {self.__formato}\n"
        imprime += f"Tiempo de lectura {self.calcular_tiempo_lectura()}"
        return imprime 

#ahora viene una clase que hereda de las hijas 
class Tutorial(Video):
    def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, formato, resolucion, dificultad,materiales_necesarios):
        super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion, formato, resolucion)
        self.__dificultad = dificultad
        self.__materiales = materiales_necesarios
    
    def agregar_material(self, nuevo_material):
        self.__materiales.append(nuevo_material)
    
    def __str__(self):
        imprime = super().__str__()
        imprime += f"Dificultad: {self.__dificultad} | Materiales: {self.__materiales}."
        return imprime  
    
#otra clase que hereda de una de las hijas 
class Entrevista(Podcast):
    def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, invitados, tema, entrevistado, empresa):
        super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion, invitados, tema)
        self.__entrevistado = entrevistado
        self.__empresa = empresa
    
    def generar_resumen(self):
        print("Generando resumen...")
    
    def __str__(self):
        imprime = super().__str__()
        imprime += f"Entrevistado: {self.__entrevistado} | Empresa: {self.__empresa}."

#===========FIN CLASES=================#



obj1 = Tutorial("Aprende Python en 30 días", "Carlos Méndez", 
                "10-10-2020", 45, 4.8,"mp4", "Full HD", 
                "Principiante", ["Python", "VS Code"])

print(obj1.__str__())

obj2 = Podcast("Historia de la IA", "Tech Radio", "11-01-2025", 60, 4.5,
               ["Dr. Smith", "Dra. Johnson"], "Tecnologia")

print(obj2.__str__())

obj3 = LibroDigital("POO para todos", "Ana Torres", "20-09-2021",
                     0, 0, 300, "epub")

print(obj3.__str__())
    
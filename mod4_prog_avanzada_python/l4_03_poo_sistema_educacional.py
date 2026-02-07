#decidi añadir la clase persona, para poder incorporar la herencia a mi trabajo 
class Persona():
    def __init__(self, nombre, rut, sexo):
        self.nombre = nombre 
        self.rut = rut 
        self.sexo = sexo 
    
    def get_nombre(self):
        return self.nombre
    def get_rut(self):
        return self.rut
    def get_sexo(self):
        return self.sexo
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def set_rut(self, nuevo_rut):
        self.rut = nuevo_rut
    def set_sexo(self, nuevo_sexo):
        self.sexo = nuevo_sexo

class Alumno(Persona):
    def __init__(self, nombre, rut, sexo, n_matricula,promedio = 0,carga_academica = None):
        super().__init__(nombre, rut, sexo)
        self.promedio = promedio
        self.n_matricula = n_matricula
        self.carga_academica = carga_academica
    
    #==Getters==#
    def get_n_matricula(self):
        return self.n_matricula
    def get_promedio(self):
        return self.promedio
    def get_carga_academica(self):
        return self.carga_academica
    
    #==Setters==#
    def set_n_matricula(self, nuevo_n_matricula):
        self.n_matricula = nuevo_n_matricula
    def set_promedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio

    #==Otros metodos==#
    def inscribirse_materia(self,nueva_materia):
        self.carga_academica.append(nueva_materia)
    def entregar_tarea(self,tarea):
        tarea.entregar_tarea()  

class Profesor(Persona):
    def __init__(self, nombre, rut, sexo, n_id, especialidad, materias_enseñadas):
        super().__init__(nombre, rut, sexo)
        self.n_id = n_id
        self.especialidad = especialidad
        self.materias_enseñadas = materias_enseñadas
    
     #==Getters==#
    def get_n_id(self):
        return self.n_id
    def get_especialidad(self):
        return self.especialidad
    def get_materias_enseñadas(self):
        return self.materias_enseñadas
    
    #==Setters==#
    def set_n_id(self, nuevo_n_id):
        self.n_id = nuevo_n_id
    def set_especialidad(self, nueva_especialidad):
        self.especialidad = nueva_especialidad
    def set_materias(self, nueva_materia):
        self.get_materias_enseñadas().append(nueva_materia)
    
    def asignar_tarea(self,tarea):
        pass 
    def revisar_tarea(self,tarea,nota):
        tarea.set_nota(nota)

class Materia():
    def __init__(self, nombre_materia, codigo_materia, creditos):
        self.nombre_materia = nombre_materia
        self.codigo_materia = codigo_materia
        self.creditos = creditos 
    
    def get_nombre(self):
        return self.nombre_materia
    def get_codigo_materia(self):
        return self.codigo_materia
    def get_creditos(self):
        return self.creditos 
    
    def set_nombre_materia(self, nuevo_nombre):
        self.nombre_materia = nuevo_nombre
    def set_codigo_materia(self, nuevo_codigo):
        self.codigo_materia = nuevo_codigo
    def set_creditos(self, nuevo_creditos):
        self.creditos = nuevo_creditos

#agregar materia a Tarea no estaba en el UML, pero lo agregue para que se viera la relacion entre ambas 
class Tarea():
    def __init__(self, nombre, fecha_entrega,materia,nota = None):
        self.nombre = nombre
        self.fecha_entrega = fecha_entrega
        self.materia = materia 
        self.nota = nota 
        self.entregada = False
    
    def get_nombre(self):
        return self.nombre
    def get_fecha_entrega(self):
        return self.fecha_entrega
    def get_materia(self):
        return self.materia 
    def get_nota(self):
        return self.nota 
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def set_fecha_entrega(self,nueva_fecha):
        self.fecha_entrega = nueva_fecha
    def set_materia(self, nueva_materia):
        self.materia = nueva_materia
    def set_nota(self, nueva_nota):
        self.nota = nueva_nota
    
    def entregar_tarea(self):
        self.entregada = True 
    

#lo que tenemos que hacer es recibir un archibo con tareas en este formato
#[ ]|Estudiar Python|2023-10-25 09:15:2
#usando la clase GestorTareas, lo abrimos y 
#dividimos la string obtenida para pasarselas a la clase Tarea 
#con esto creamos un objeto de tarea y lo agregamos a nuestra lista 

class Tarea:
    def __init__(self, descripcion, fecha_creacion, completada):
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.completada = False
    
    def marcar_completada(self):
        self.completada = True 
    
    def __str__(self):
        if self.completada: 
            estado = "X"
        else:
            estado = ""
        return (f"[{estado}] | {self.descripcion} | {self.fecha_creacion}")
    

class GestorTareas:
    def __init__(self, nombre_archivo = "tareas.txt"):
        self.nombre_archivo = nombre_archivo
        self.tareas = []
        self.cargar_tareas()
    
    #cargar_tareas(self): Lee el archivo y carga las tareas en memoria
    def cargar_tareas(self):
        #la apertura de archivos puede dar errores asi que va en try/exp
        try:
            with open(self.nombre_archivo, "r", encoding = "utf-8") as archivo:
                #open abre el archivo y lo convierte en un objeto tipo archivo
                for linea in archivo:
                    linea = linea.strip()
                    if linea: #un string vacio da falso, me aseguro que tenga algo antes de procesarlo 
                        partes = linea.split("|")
                        if len(partes) == 3:
                            #aca separamos los 3 elementos de la lista en una variable
                            estado, descripcion, fecha = partes
                            if estado == "[X]":
                                estado = True
                            else:
                                estado = False
                            nueva_tarea = Tarea(descripcion, fecha, estado)
                            self.tareas.append(nueva_tarea)
                            print(f"Se ha cargado la tarea {descripcion}")
            print("Se ha procesado el archivo con exito.")
                
        except FileNotFoundError:
            print("Soy un error en la parte de abrir un archivo.")
    
    #guardar_tareas: Guarda todas las tareas en el archivo
    def guardar_tareas(self):
        try:
            with open(self.nombre_archivo, "w", encoding = "utf-8") as archivo:
                #aca recorro cada elemento de mi lista de tareas
                for tarea in self.tareas:
                    #y escribo cada elemento en mi archivo
                    archivo.write(tarea.__str__()+ "\n")
                print("Tareas guardadas correctamente.")
        #con esto agarramos cualquier error que pueda salir. 
        except Exception as e:
            print(f"Error al guardar tarea: {e}")
    
    #agregar_tarea: Crea y agrega una nueva tarea
    def agregar_tarea(self, descripcion, fecha):
        nueva_tarea = Tarea(descripcion, fecha, False)
        self.tareas.append(nueva_tarea)
        #ademas va a guardar la tarea inmediatamente al archivo 
        self.guardar_tareas() 
    
    #marca una tarea como completada, eligiendo de la lista de tareas 
    def marcar_completada(self, indice):
        try:
            indice_real = indice-1
            if indice_real >= 0 and indice_real < len(self.tareas):
                #aca llamamos al objeto tarea q buscamos de la lista 
                self.tareas[indice_real].marcar_completada()
                #una vez que fue modificada hay que guardarla 
                self.guardar_tareas()
                print("Tarea completada.")
        except Exception as e:
            print(f"Error al completar tarea: {e}")
    
    def mostrar_tareas(self):
        i = 1
        for tarea in self.tareas:
            print(f"{i}. {tarea.__str__()}")
            i+= 1
    
    def eliminar_tarea(self, indice):
        try:
            indice_real = indice-1
            if indice_real >= 0 and indice_real < len(self.tareas):
                del self.tareas[indice_real]
                self.guardar_tareas()
                print("Tarea eliminada.")
        except Exception as e:
            print(f"Error al completar tarea: {e}")


#====MENU====# 
def menu():
    print("="*5)
    print(F"GESTOR DE TAREAS")
    print("="*5)
    print("1.Ver todas las tareas.\n")
    print("2.Agregar nueva tarea. \n")
    print("3. Marcar tarea como completada. \n")
    print("4.Eliminar tarea. \n")
    print("5.Salir. \n")

gestor = GestorTareas()
while True:
    menu()
    try:
        opcion = int(input("Seleccione una opcion:"))
    except ValueError:
        print("Ingrese un numero valido.")
    if opcion == 1:
        gestor.mostrar_tareas()

    elif opcion == 2:
        try:
            descripcion = input("Ingrese una tarea: ")
            fecha = input("Ingrese una fecha.")
            gestor.agregar_tarea(descripcion, fecha)
        except Exception as e:
            print(f"Error en ingreso de tarea: {e}")

    elif opcion == 3:
        try: 
            gestor.mostrar_tareas()
            indice = int(input("Ingrese el numero de tarea a completar: "))
            gestor.marcar_completada(indice)
        except Exception as e:
            print(f"Error en la ejecucion: {e}")

    elif opcion == 4:
        try:
            gestor.mostrar_tareas()
            indice = int(input("Ingrese el numero de tarea a eliminar: "))
            gestor.eliminar_tarea(indice)
        except Exception as e:
            print(f"Error en la ejecucion: {e}")

    elif opcion == 5:
        print("Saliendo")
        break 
    else:
        print("Por favor ingrese una opción valida.")


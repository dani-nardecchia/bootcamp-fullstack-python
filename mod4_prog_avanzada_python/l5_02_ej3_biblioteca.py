libros = {"Python":2, "C++": 3, "SQL": 10}

#creamos un par de clases para manejras nuestros errores 
class LibroNoEncontradoError(Exception):
    pass 
class StockAgotadoError(Exception):
    pass 

####=========Funciones==========###

#hay que crear una funcion con manejo de excepciones y raise 
#debe lanzar una excepcion personalizada si el libro no existe 
#o si no se encuentra en stock 
def consultar_stock(nombre_libro):
    if nombre_libro not in libros:
        raise LibroNoEncontradoError(f"El libro {nombre_libro} no existe en stock.\n")
    
    elif libros[nombre_libro] == 0:
        raise StockAgotadoError(f"No hay ejemplares de {nombre_libro} disponibles para prestamo.\n")
    
    print(f"Stock de {nombre_libro}: {libros[nombre_libro]} ejemplares.\n")

#hay que crear una funcion con manejo de excepciones y raise 
#debe lanzar una excepcion personalizada si el libro no existe 
#o si no se encuentra en stock 
def prestar_libro(nombre_libro):
    consultar_stock(nombre_libro)

    libros[nombre_libro] -= 1 
    print(f"Se ha realizado el prestamo de {nombre_libro} con exito.\n")


def devolver_libro(nombre_libro):
    if nombre_libro not in libros:
        raise LibroNoEncontradoError(f"El libro {nombre_libro} no existe en stock.\n")
    
    libros[nombre_libro] += 1
    print(f"Se ha devuelto el libro {nombre_libro} exitosamente.\n")

#========Interfaz principal=======#

def menu():
    while True:
        print(f"Bienvenido a la biblioteca! \n")
        print(f"Presione 1 para consultar stock.\n")
        print(f"Presione 2 para pedir un libro en prestamo.\n")
        print(f"Presione 3 para devolver un libro.\n")
        print(f"Presione 4 para salir.\n")
        
        try:
            opcion = int(input("Seleccione una opcion: "))
            
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if opcion == 4:
                print("Vuelva pronto!")
                break

        try:
            nombre_libro = input("Ingrese el nombre del libro: ")
            if opcion == 1:
                consultar_stock(nombre_libro)

            elif opcion == 2:
                prestar_libro(nombre_libro)
            
            elif opcion == 3:
                devolver_libro(nombre_libro)

            #esto maneja que el usuario ingrese un numero q no sea una opcion valida 
            else:
                print("Ingrese un número valido de opcion: 1 a 4.")
    
        #esto maneja los errores de que el libro no exista o este agotado
        except (LibroNoEncontradoError, StockAgotadoError) as e:
            print(e)
        
        #esto maneja que el usuario ingrese algo raro en la seleccion de opcion
        except (ValueError, KeyError):
            print("Error inesperado durante la operacion. ")

#==========Ejecucion=======#


menu()


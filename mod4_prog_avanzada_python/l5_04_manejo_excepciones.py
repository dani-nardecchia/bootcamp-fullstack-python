#Escribe un programa que pida al usuario dividir dos números
#Utiliza try/except para capturar una división por cero y mostrar un mensaje de error amigable
#Agrega validación para que el usuario ingrese solo números.
#Usa un bloque try/except con múltiples excepciones (ZeroDivisionError, ValueError).

try: 
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    print (f"El resultado de la division de {num1} y {num2} es {num1/num2}")

except ValueError:
    print("Debe ingresar un número entero.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

#Crea una función validar_edad(edad) que lance una excepción EdadInvalidaError si la edad es menor que 0.
#Define esta excepción como clase hija de Exception.

class EdadInvalidaError(Exception):
    pass 
def validar_edad(edad):   
        if edad < 0: 
            raise EdadInvalidaError ("Error: edad no puede ser menor que cero.")
        else:
            print(f"Edad validada: {edad} años.")

#ahora lo probamos con try/except
try:
     validar_edad(-5)

except EdadInvalidaError as e:
     print (e) 

#Simula la apertura de un archivo (puede ser un print("Abriendo archivo...")) y utiliza finally para imprimir "Cerrando archivo..." aunque haya ocurrido un error
try:
    print("Abriendo archivo...")
    raise FileNotFoundError("Archivo no encontrado")
except FileNotFoundError as e:
    print(e)
finally:
    print("Cerrando archivo...")
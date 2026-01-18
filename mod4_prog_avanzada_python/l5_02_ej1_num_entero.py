#aca manejamos el error de que el usuario 
#no ingrese un numero como le pedimos 
try:
    num = int(input("Ingrese un numero: "))
    print(f"Numero ingresado: {num}")

#la linea de codigo despues del except se ejecutara dsps de un ValueError,
# causado por la ejecucion del codigo anterior
#no cualquier ValueError en todo el codigo 
except ValueError:
    print("Debes ingresar un numero entero.")

#========Segundo ejercicio=============#




try: 
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    op = input("Ingrese una operación: ")
    
    if op == "+":
        print (f"El resultado de la suma de {num1} y {num2} es {num1 + num2}") 
    elif op == "-":
        print (f"El resultado de la resta de {num1} y {num2} es {num1 - num2}")
    elif op == "*":
        print (f"El resultado de la multiplicacion de {num1} y {num2} es {num1 * num2}")
    elif op == "/":
        print (f"El resultado de la division de {num1} y {num2} es {num1/num2}")
    else:
        #print("Error: operacion no válida")
        raise TypeError

except ValueError:
    print("Debe ingresar un número entero.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except NameError:
    print("Error: Variable no definida en la operación.") 
except TypeError:
    print("Error: tipos de datos incompatibles.")

#Tambien se podia hacer asi#

try: 
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    op = input("Ingrese una operación: ")

    if op not in ["+", "-", "*", "/"]:
        #queremos usar raise para llamar un tipo de error especifico 
        raise TypeError
        #print("Error: operacion no valida.")
        
    if op == "+":
        resultado = num1+num2
    elif op == "-":
        resultado = num1 - num2 
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        resultado = num1/num2
    print(f"El resultado de {num1} {op} {num2} es {resultado}.")

except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except NameError:
    print("Error: Variable no definida en la operación.") 
except TypeError:
    print("Error: tipos de datos incompatibles.")
except ValueError:
    print("Debe ingresar un número entero.")

1




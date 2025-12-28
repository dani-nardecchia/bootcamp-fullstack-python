#Al ingresar un numero par cualquiera que sea del 2 al 100, este imprima en pantalla todos los
#números pares siguientes, y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en
#pantalla todos los números impares siguientes hasta el 99.
#Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, el programa debe enviar un
#mensaje de que no es posible realizarlo y volver a preguntar por el ingreso del número.

def par_impar():
    numero = int(input("Ingrese un numero: "))
    while numero <= 0 or numero > 100:
        print("No es posible realizarlo.")
        numero = int(input("Ingrese un numero: "))
    
    if 2 <= numero <= 100:
        if numero % 2 == 0:
            while numero <= 100:
                print (numero)
                numero += 2
        elif numero % 2 != 0:
            while numero <= 99:
                print(numero)
                numero += 2
    
par_impar()

#Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

def notas():
    lista_notas = []

    for i in range(1,6):
        nota = int(input(f'Ingrese nota {i}:'))
        while nota < 0 or nota > 10:
            print("Ingrese notas del 0 al 10")
            nota =int(input(f'Ingrese nota {i}:'))
        lista_notas.append(nota)
    
    print("Notas: ", lista_notas)
    print("Promedio: ", sum(lista_notas)/len(lista_notas))
    print("Nota mas alta: ", max(lista_notas))
    print("Nota mas baja: ", min(lista_notas))

notas()

#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. 
# Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

def dia_mes():

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    num = int(input("Ingrese un número de mes: "))
    
    if 1 <= num <= 12:
        nombre_mes = meses[num -1]
        dia_num = dias_mes[num -1]

        print (f"El mes {nombre_mes} tiene {dia_num} dias.")
    else:
        print("Ese mes no existe, intentelo de nuevo.")


dia_mes()
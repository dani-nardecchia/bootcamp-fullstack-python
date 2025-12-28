#Crear estructuras

lista = ["frambuesas", "cerezas", "platanos", "melon tuna"]

tupla = (1, 2, 3)             

set = { "a", "b", "c" }  

dic = { "nombre": "Dani", "edad": 32, "hobby": "Leer" }

print(f"lista:{lista}")
print(f"tupla:{tupla}")
print(f"set:{set}")
print(f"diccionario:{dic}")

#Las diferencias principales son que: 
#la lista es mutable, la tupla es inmutable
#el set no tiene orden y no lleva duplicados 
#el diccionario lleva pares de clave y valor y es mutable 

#Acceder a elementos
print(f"El segundo elemento de la lista es: {lista[1]}")
print(f"Una clave y su valor seria: 'nombre' y {dic['nombre']}")

#Explica con comentarios por qué no puedes acceder por índice a un set.
#No se puede porque los sets no son ordenados, asi q no tiene indice para
#decir primer elemento o segundo elemento 

#Usa len() para mostrar la cantidad de elementos en cada estructura.
print(f"Cantidad elementos lista: {len(lista)}")
print(f"Cantidad elementos tupla: {len(tupla)}")
print(f"Cantidad elementos conjunto: {len(set)}")
print(f"Cantidad elementos diccionario:{len(dic)}")

#Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.
print("\nIterando lista:")
for i in lista:
    print(i)

print("\nIterando tupla:")
for i in tupla:
    print(i)

print("\nIterando conjunto:")
for i in set:
    print(i)

print("\nIterando diccionario (claves y valores):")
for clave, valor in dic.items():
    print(clave, ":", valor)

#Modificar estructuras

#Agrega un nuevo elemento a la lista y al conjunto.
lista.append("ciruela")

set.add("d")

#Borra un elemento de la lista.
lista.remove("frambuesas")

#Agrega una nueva clave al diccionario.
dic["ciudad"] = "Rancagua"

#Intenta modificar la tupla y comenta qué ocurre.
tupla[0] = 0
#esta linea da el error "tuple object does not support item assignment" que indica q no puedo modificar la tupla
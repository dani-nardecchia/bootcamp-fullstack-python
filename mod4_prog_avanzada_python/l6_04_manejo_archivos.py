#Crea un archivo llamado datos.txt desde Python (modo escritura)
#Escribe al menos 3 líneas de texto en él usando write().

with open("datos.txt", "w") as archivo:
    archivo.write(""""When Mr. Bilbo Baggins of Bag End announced that he would shortly \n 
                  be celebrating his eleventy first birthday with a party\n 
                  of special magnificence there was much talk and excitement in Hobbiton.""")

#Abre el archivo datos.txt en modo lectura y muestra su contenido en pantalla usando read().
with open("datos.txt") as texto:
    print(texto.read())

#Usa readline() para leer e imprimir solo la primera línea del archivo.
with open("datos.txt") as texto:
    print(texto.readline())
    
#Luego, usa un ciclo for para leer línea por línea el resto del archivo.
with open("datos.txt") as texto:
    for linea in texto:
        print(linea)

#Vuelve a abrir el archivo en modo append y agrega una línea nueva.
with open("datos.txt", "a") as archivo:
    archivo.write("\n Bilbo was very rich and very peculiar, and had been the " \
    "wonder of the Shire for sixty years.")

#Luego vuelve a abrirlo en modo lectura para comprobar que se agregó correctamente.
with open("datos.txt","r") as texto:
    print(texto.read())

#Muestra por pantalla el nombre del archivo (.name), si está cerrado (.closed) y el modo de apertura (.mode).
with open("datos.txt") as archivo:
    print(f"Nombre: {archivo.name}")
    print(f"Esta cerrado?: {archivo.closed}")
    print(f"Modo de apertura: {archivo.mode}")



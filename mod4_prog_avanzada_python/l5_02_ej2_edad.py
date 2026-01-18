try: 
    edad = int(input("Ingrese edad: "))
    if edad < 0: 
        raise ValueError ("Error: edad no puede ser menor que cero.")
    elif edad > 120: 
        raise ValueError ("Error: edad no puede ser mayor que 120.")
    else:
        print(f"Edad registrada: {edad} años.")

except ValueError as obj_error:
    #print("Error: Debes ingresar un numero entero.")
    print(f"Error: {obj_error}")

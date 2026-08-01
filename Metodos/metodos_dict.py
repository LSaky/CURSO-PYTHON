diccionario = {
    "nombre" : "Dissel",
    "apellido" : "Leal",
    "edad" : 23
}

#KEYS = Sirve para devolvernos las claves que hay en un diccionario 
claves = diccionario.keys()

#GET - Sirve para traer el valor de la llave que le pongamos
valor = diccionario.get("nombre")

#ITEMS - Modifica el diccionario para que los elementos se puedan iterar
diccionario_iterable = diccionario.items()

#POP - Elimina un elemento del diccionario
diccionario.pop("nombre")

#CLEAR - Elimina todo del diccionario
diccionario.clear()





print(diccionario_iterable)
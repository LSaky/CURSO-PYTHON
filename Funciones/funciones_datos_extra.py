#Creando funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#Utilizando keyword arguments
frase_resultante = frase(adjetivo = "Capo", nombre = "Dissel", apellido= "Leal")
print(frase_resultante)

#Creando la misma funcion pero con un parametro opcional
def frase(nombre,apellido,adjetivo = "Tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#Utilizando keyword arguments
frase_resultante = frase("Dissel", "Leal")
print(frase_resultante)
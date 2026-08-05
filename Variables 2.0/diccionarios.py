#Creando diccionarios con dict() 
diccionario = dict(nombre = "Dissel", apellido = "Leal")

#Podemos meter una lista a una clave de un diccionario con frozenset
diccionario2 = {frozenset(["dissel","leal"]): "jajaja"}

#Creando diccionarios y que todos los valores sean NONE
diccionario3 = dict.fromkeys(["Nombre", "Apellido"])

#Creando diccionario y le colocamos que los valores sean igual a NO SE
diccionario4 = dict.fromkeys(["Nombre", "Apellido"], "no se")


print(diccionario)
print(diccionario2)
print(diccionario3)
print(diccionario4)

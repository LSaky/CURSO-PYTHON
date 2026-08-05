diccionario = {
    "nombre" : "Dissel",
    "apellido" : "Leal",
    "edad" : 23
}

#Iterando solamente las KEYS de el diccionario
for elemento in diccionario:
    print(elemento)

#Iterando el diccionario con .ITEMS() donde vamos a poder seleccionar el valor 
for elemento in diccionario.items():
    key = elemento[0]
    dato = elemento[1]
    print(f"La llave es {key} y el dato es {dato}")    


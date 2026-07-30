#lista (Se pueden modificar)
Lista = ["Dissel", 23, "calle 89", True]

#Esto es valido
Lista[3] = "calle90"

print(Lista[2])
#-------------------------------------------------
#Tupla (No se puede modificar)
Tupla = ("Dissel", 23, "Calle 89", True)

#Esto no es valido
Tupla[3] = "calle90"

print(Tupla[2])

#--------------------------------------------------
#Conjunto SET
conjunto = {"Dissel", 23, "calle 89", True}

#Si es vaido
conjunto = {"Modificandolo", True}

#No es valido
conjunto[0] = "Camilo"

print(conjunto)

#-------------------------------------------------
#Diccionario
Diccionario = {
    "nombre" : "Dissel",
    "edad" : 23,
    "direccion" : "calle 89",
    "es guapo?" : True
}

print(Diccionario["edad"])

print(Lista[3])
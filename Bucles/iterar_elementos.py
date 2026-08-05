animales = ["Perro", "Gato", "Loro", "Pez", "Cocodrilo"]
numeros = [2,4,5,6,23]

#Iterando la lista ANIMALES
for animal in animales:
    print(animal)

#Iterando la lista NUMEROS y multiplicandola po 10
for numero in numeros:
    print(numero * 10)


#Iterando las 2 listas a la vez
for numero,animal in zip(animales,numeros):
    print(animal)
    print(numero)

#Recorrer una lista por su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es : {indice} y el valor es: {valor}")

#Usando FOR ELSE 
for numero in numeros:
    print(f"numero: {numero}")
else:
    print("El bucle termino")  
frutas = ["babano","manzana","pera","durazno","granadilla","naranja"]

#Usando el comando CONTINUE para saltarse una iteracion
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")

#Usando el comando BREAK para terminar el bucle for
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"me voy a comer una {fruta}")

cadena = "Hola Dissel"

for letra in cadena:
    print(letra)

numeros = [1,45,23,21,32]

#FOR en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
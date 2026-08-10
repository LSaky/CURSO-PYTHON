#Utilizando el operador * como argumento args()
def suma (nombre,*numeros):
    return print(f"{nombre} la suma de tus numeros es: {sum(numeros)}")

resultado = suma("Camilo",2,6,45,23,12,34)
print(resultado)


# Utilizando args() dentro de la funcion
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([1,2,3,45,23,12,67])
print(resultado2)
print("----------------------EJERCICIO A y C --------------------------")
frase = input("Dime una frase y te calculo cuanto tiempo tardarias en decirle: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras /2} segundos en decirlas")
print(f"Dalto tardaria {cantidad_de_palabras /2 * 0.7} segundos en decirlas")

print("----------------------EJERCICIO B --------------------------")
if cantidad_de_palabras > 120:
    print("Para flaco, tampoco te pedi un testamento")


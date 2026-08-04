#Creando un conjunto con SET()
conjunto = set(["DATO 1"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

#TEORIA DE CONJUNTOS
conjunto1 = {1,3,5,7,9}
conjunto2 = {1,3,5}

#Verificando si es un subconjunto
resultado1 = conjunto2.issubset(conjunto1)
resultado1 = conjunto2 <= conjunto1

#Verificando si es un superconjunto
resultado2 = conjunto2.issuperset(conjunto1)
resultado2 = conjunto2 >= conjunto1

#Verificar si hay algun numero en comun
resultado3 = conjunto2.isdisjoint(conjunto1)


print(resultado1)
print(resultado2)
print(resultado3)

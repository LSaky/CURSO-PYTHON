numeros = [11,5,3,78,43,23,12]

# MAX - Encontrando el numero mayor de una lista
numero_mas_alto =  max(numeros)

# MIN - Encontrando el numero menor de una lista
numero_menor =  min(numeros)

print(numero_mas_alto)
print(numero_menor)

# ROUND - Redondeando un numero y elegir cuantos decimales va a tener
numero = round(12.324535323, 2)
print(numero)

# BOOL - Hace que si algun dato que le pasemos es (0, vacio, false, nose) nos arroge un FALSE pero si le pasamos un dato (distinto a 0, True, cadena, datos no vacios) nos arroge un TRUE

resultado_bool1 = bool(0)

resultado_bool2 = bool("hola")

print(resultado_bool1)
print(resultado_bool2)

#ALL - ALL nos devuelve TRUE si agregamos varios datos y todos son verdaderos (12,hola,true) Y nos devuelve FALSE si algun dato es falso (12, hola, None)
resultado_all = all([10,23,"hola", False])
print(resultado_all)

# SUM - Nos suma todos los valores de una lista o los valores que elijamos
suma = sum(numeros)
print(suma)


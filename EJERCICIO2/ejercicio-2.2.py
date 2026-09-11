#Creando una funcion que nos devuelva los numeros primos entre el 0
#Y el numero que le pasemos

#Creamos una funcion que verifique si un numero es primo
def es_primo(num):
    #Verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #Si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    #Si termna el bucle, significa que no fue divisible entonces es primo 
    return True

#Creando una funcion que retorne una lista con todos los primos 
def primos_hasta(num):
    #Creamos lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo 
        resultado = es_primo(i)
        #En caso de que si sea primo lo agregamos a la lista 
        if resultado == True: primos.append(i)
    
    #Devolvemos la lista 
    return primos

#Creamos el resultado llamando la funcion y lo mostramos
resultado = primos_hasta(98)
print(resultado)

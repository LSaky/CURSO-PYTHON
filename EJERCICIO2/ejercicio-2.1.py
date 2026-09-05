#Falto el profesor y ahora los estudiantes van a armar la clase, el qu etenga mas 
#edad va a ser el profesor y el que tenga menos edad va a ser su asistente

#Funcion para obtener al profesor y al asistente segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    #Creando la lista con los compañeros
    compañeros = []
    
    #Ejecutando un FOR para pedir iinformacion de cada compañero
    for i in range (cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #Agregando la informacion de la lista 
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segun su edad 
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros [x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre 
    #para definir al profesor y al asistente
    profesor = compañeros[-1][0]
    asistente = compañeros[0][0]
    
    #Retornamos una tupla  
    return asistente,profesor

#Desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#Mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")    
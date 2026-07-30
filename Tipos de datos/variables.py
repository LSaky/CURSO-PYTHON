#Variable con cadena de texto
nombre = "Dissel"

#Variable con numeros
numero = 10

#El =+ se usa para sumarle un numero al que ya teniamos
numero =+5

#El =- se usa para restarle un numero alq ue ya teniamos
numero =-5

nombre2 = "Leal"

#Concatenar con +
NombreCompleto1= "Hola este es mi nombre completo: " + nombre + " Camilo " + nombre2 + " Varon"

#Concatenar con F STRING
NombreCompleto2 = f"Hola este es mi nombre completo: {nombre} Camilo {nombre2} Varon"

print(NombreCompleto1)
print(NombreCompleto2)

#Operadores de pertenencia 
print ("Dissel" in NombreCompleto1)

print("Dissel" not in NombreCompleto2)
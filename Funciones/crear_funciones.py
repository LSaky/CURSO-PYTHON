#Creando una funcion simple
def saludar():
    print("Hola, Buenos dias, Como estas?")

saludar()
saludar()
saludar()
saludar()

#Creando una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "Reina"
    elif sexo == "hombre":
        adjetivo = "Rey"
    else:
        adjetivo = "Amor"
    print(f"Hola {nombre}, como estas mi {adjetivo}")


saludar("Dissel", "Hombre")
saludar("Camila", "muJer")
saludar("Leal", "No binario")

#Crear una funcion que nos retorne multiples valores
def crear_contraseña_aleatoria(num):
    letras = "abcdefghi"
    num_string = str(num)
    num = int(num_string[0])
    c1 = num -2
    c2 = num 
    c3 = num -7
    contraseña = f"{letras[c1]}{letras[c2]}{letras[c3]}{num*2}"
    return contraseña

password = crear_contraseña_aleatoria(1)
print(f"Tu contraseña es {password}")
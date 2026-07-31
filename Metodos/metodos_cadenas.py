cadena1 = "Hola soy Dissel"
cadena2 = "Bienvenido"

#resultado = dir(cadena1)
#Convierte todo a mayusculas
mayusculas = cadena1.upper()

#convierte todo a minusculas
minusculas = cadena1.lower()

#Convierte solo la primera letra a mayuscula
p_l_mayuscula = cadena1.capitalize()

#Busca texto en la cadena, si no lo encuentra devuelve -1
encontrar = cadena1.find("Dissel")

#Busca texto en la cadena, si no lo encuentra devuelve un error
encontrar = cadena1.index("Dissel")

#Si es numerico devolvemos TRUE, si no devolvemos FALSE
es_numerico = cadena1.isnumeric()

#Si es ALPHAnumerico devolvemos TRUE, si no devolvemos FALSE
es_alpha = cadena1.isalpha()

#Buscar un texto en una cadena de texto y nos muestra cuantas veces esta ese texto
contar = cadena1.count("s")

#Sirve para contar cuantos caracteres hay en una cadena de texto
longitud = len(cadena1)

#Sirve para sabe si una cadena de texto empieza con lo que nosotros querramos consultar
empieza_con = cadena1.startswith("Hola")

#Sirve para sabe si una cadena de texto termina con lo que nosotros querramos consultar
termina_con = cadena1.endswith("issel")

#Sirve para reemplazar una parte de la cadena de texto por otra que nosotros queramos
reemplazar = cadena1.replace("Dissel", "Camilo")

#Sirve para separar una cadena de texto y convertirla en una lista
cadena_separada = cadena1.split(" ")


print(cadena_separada)
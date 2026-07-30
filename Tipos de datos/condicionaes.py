edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

contraseña_sql = "DisselMaestro"
contraseña_escrita = "DisselMaestro"

if contraseña_sql == contraseña_escrita:
    print("INICIANDO SESION...")
else:
    print("CONTRASEÑA INCORRECTA")
    
#--------------ELIF-------------------------------

ingreso_mensual = 12000
gasto_mensual = 9000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 5000:
        print("Eres Rico")
    elif ingreso_mensual - gasto_mensual <= 0:
        print("Estas en deficit")
    else:
        print("Estas gastando mucho dinero")

elif ingreso_mensual >= 5000:
    print("Estas bien en latinoamerica")

elif ingreso_mensual >= 1000:
    print("Estas bien en colombia")

elif ingreso_mensual >= 500:
    print("Estas bien en argentina")

else:
    print("Eres probre")

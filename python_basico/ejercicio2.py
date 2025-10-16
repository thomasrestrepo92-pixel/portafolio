#especificaciones
# = es para darle avlor a algo
# == es para decir si es igual
# === es para decir que el caractes es identico 
edad = 22

if edad < 18: 
    print ("Es menor de edad")
elif edad == 18:
    print ("tienes la mayoria de edad")
else: 
    print("Es mayor de edad")
    

usuario = "admin"
contrasena = "1234"

if usuario == "admin" and contrasena == "1234": 
    print ("acceso consedido")
else:
    print("acceso denegado")

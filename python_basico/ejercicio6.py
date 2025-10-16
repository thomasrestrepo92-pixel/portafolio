# funciones
def saludar():
    print("hola , bienvenido!")

saludar()

#funcion con parametro
def saludo_personal(nombre):
    print(f"hola , {nombre}")

saludo_personal("thomas")

# otra condicionada
def saludo_personal(nombre):
    print(f"hola , {nombre}") 

nombre_usuario = input("ingrese su nombre: ")
saludo_personal(nombre_usuario)

# funcion con valores de retorno pidiendo valores
def suma(num1, num2):
    resultado= num1 + num2
    return resultado
num1=int(input("imgrese un numero: "))
num2=int(input("ingrese otro numero: "))

total=suma (num1,num2)
print(f"la suma es:{total}")

# funcion con valores de retorno
def suma(num1, num2):
    resultado= num1 + num2
    return resultado

total=suma (5,2)
print(f"la suma es:{total}")

# funcion con parametros por defecto25

def perfil (nombre , edad , ciudad="medellin"):
    return{
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
perfil1=perfil("thomas",16)
perfil2=perfil("ana",25,"bogota")
print(perfil1)
print(perfil2)
# diccionario creacion 
estudiante = {
    "nombre":"thomas",
    "edad":16,
    "profesion":"estudiante",
    "competencias": ["programacion", "base de datos", "algoritmos"]
}


print(estudiante["nombre"])
print(estudiante["edad"])
print(estudiante["profesion"])
print(estudiante["competencias"][2]) # el numero significa lo de la lista

#modificar un valor del diccionario
estudiante["edad"] = 17
estudiante["celular"] = 3235628234

# recorrer un diccionario
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
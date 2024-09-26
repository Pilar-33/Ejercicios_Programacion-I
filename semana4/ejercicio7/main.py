from os import system
system("cls")

from ejercicio7 import menor_edad
# Datos
nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
        "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

# Mostrar informacón
nombres_menores, edad_menores = menor_edad(edades, nombres)

for i in range(len(nombres_menores)): 
    print(f"{nombres_menores[i]}, {edad_menores[i]} años")

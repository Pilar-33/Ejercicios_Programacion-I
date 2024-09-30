from os import system
system("cls")

from ejercicio8 import transponer_matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta = transponer_matriz(matriz)
print("Matriz Original")
for i in matriz:
    for j  in i:
        print(j, end=" ")
    print("")

print(" ")
print("Matriz transpuesta")
for i in transpuesta:
    for j  in i:
        print(j, end=" ")
    print("")

from os import system
system("cls")

from ejercicio1 import agregar_columna

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

columna = [10, 11, 12]
matriz_nueva = agregar_columna(matriz, columna)

print("Matriz original:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print("")

print("\nMatriz nueva:")
if matriz_nueva is not None:
    for i in range(len(matriz_nueva)):
        for j in range(len(matriz_nueva[i])):
            print(matriz_nueva[i][j], end=" ")
        print("")
from os import system
system("cls")

from ejercicio7 import multiplicar_matrices

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]  #3*3
    ]

matriz2 = [
    [9, 8],
    [6, 5],
    [3, 2]   # 3*2
    ]

producto = multiplicar_matrices(matriz1, matriz2)

print("Resultado de Multiplicar dos matrices")
for i in producto:
    for j  in i:
        print(j, end="\t")
    print("")

    
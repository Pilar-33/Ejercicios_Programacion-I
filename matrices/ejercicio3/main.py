from os import system
system("cls")

import ejercicio3 as fm

matriz = fm.inicializar_matriz(4, 4, 0)
print("Matriz del producto de los índices")
matriz_multiplicada = fm.multiplicar_matriz(matriz)
fm.mostrar_matriz(matriz_multiplicada)
from os import system
system("cls")

from ejercicio11 import buscar_binario_recursivo

lista_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_buscado = 15

inicio = 0
final = len(lista_ejemplo) - 1

resultado = buscar_binario_recursivo(lista_ejemplo, valor_buscado, inicio, final)

if resultado == None:
    print(f"Valor {valor_buscado} no encontrado")
else:
    print(f"Valor {valor_buscado} encontrado en el índice: {resultado}")

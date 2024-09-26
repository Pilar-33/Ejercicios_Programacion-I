from os import system
system("cls")

from ejercicio5 import corregir_lista

lista_nombres = ["Maria", "Juan", "Pedro", "Ana", "Luis", "Carlos", "Laura", "Sofia"]

print("Lista original")
for posicion in range(len(lista_nombres)):
        if posicion == len(lista_nombres) - 1:
            print(lista_nombres[posicion])
        else:
            print(lista_nombres[posicion], end = ", ")


corregir_lista(lista_nombres)

print("Lista corregida")
for posicion in range(len(lista_nombres)):
        if posicion == len(lista_nombres) - 1:
            print(lista_nombres[posicion])
        else:
            print(lista_nombres[posicion], end = ", ")
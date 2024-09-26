from os import system
system("cls")

from ejercicio8 import verificar_elementos

# Datos
lista = ["Julia", "Juana", "Carlos", 1234, False, 3.12]
rpta = verificar_elementos(lista)
print(rpta)

lista1 = [124, 568, 10, -1]
rpta1 = verificar_elementos(lista1)
print(rpta1)
from os import system
system("cls")

from ejercicio6 import validar_numeros

inferior = int(input("Ingrese el límite inferior del rango: "))
superior = int(input("Ingrese el límite superior del rango: "))

numeros_validos = validar_numeros(inferior, superior)
print("Números válidos:", numeros_validos)

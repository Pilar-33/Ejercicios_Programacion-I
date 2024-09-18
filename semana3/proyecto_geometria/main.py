from os import system
system("cls")

from geometria import *

#cálculos áreas
# usa valor del parametro por defecto
area_circulo = f"El área de circulo es (valor por defecto): {calcular_area_circulo()}" 
print(area_circulo)

#usa otro valor
area_circulo = f"El área de circulo es: {calcular_area_circulo(8)}" 
print(area_circulo)

area_cuadrado = f"El área del cuadrado es: {calcular_area_cuadrado(4)}"
print(area_cuadrado)

area_triangulo = f"El área del triángulo es: {calcular_area_triangulo(5, 7)}"
print(area_triangulo)

#cálculos perímetros
# usa valor del parametro por defecto
perimetro_circulo = f"El perímetro de circulo es (valor por defecto): {calcular_perimetro_circulo()}"
print(perimetro_circulo)

#usa otro valor
perimetro_circulo = f"El perímetro de circulo es: {calcular_perimetro_circulo(8)}"
print(perimetro_circulo)

perimetro_cuadrado = f"El perímetro del cuadrado es: {calcular_perimetro_cuadrado(4)}"
print(perimetro_cuadrado)

perimetro_triangulo = f"El perímetro del triángulo es: {calcular_perimetro_triangulo(5, 7, 10)}"
print(perimetro_triangulo)


from os import system
system("cls")
from ejercicio4 import calcular_media_etaria

nombres = ["Juan", "Ricardo", "Nahuel", "Eugenia", "Jimena"]
edades = [23, 35, 34, 40, 24]
generos = ["Hombre", "Hombre", "Hombre", "Mujer", "Mujer"]

media_hombres, media_mujeres, mujeres, hombres = calcular_media_etaria(nombres, edades, generos)
print(f"La media etaria de los hombres es: {media_hombres:.2f} años")
print(f"La media etaria de las mujeres es: {media_mujeres:.2f} años")
print(f"Nombres de hombres: {hombres}")
print(f"Nombres de mujeres: {mujeres}")
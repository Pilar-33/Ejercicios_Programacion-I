from os  import system
system("cls")

"""6- Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que menos gana. No es necesario
ordenar, utilizar listas anidadas y resolver usando listas"""

lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

tamanio = len(lista_ingresos)
porcentaje_personas = int(0.20 * tamanio)
minimos = []
for ingreso in lista_ingresos:
    if len(minimos) < porcentaje_personas:
        # Si hay menos de 4 elementos en'minimos', añadimos el valor
        minimos += [ingreso] # [10,15,33,8]
    else:
        indice_mayor = 0
        for i in range(1, porcentaje_personas):
            if minimos[i] > minimos[indice_mayor]: 
                indice_mayor = i 

        if ingreso < minimos[indice_mayor]:
            minimos[indice_mayor] = ingreso
suma_minimos = 0
for ingreso in minimos:
    suma_minimos += ingreso

promedio = suma_minimos / porcentaje_personas

msje = f"Promedio de ingresos/hora del 20% que menos ganan: {promedio} ingresos/hora\n"
msje += f"Lista de los que menos ganan: {minimos}"
print(msje)
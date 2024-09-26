from os import system
system("cls")

# 4- Desarrollar una función que calcule la media de ingresos por cuartil
lista_ingresos = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

# ordenar la lista:
# Algoritmo de ordenamiento burbuja
n = len(lista_ingresos)

# Recorrer la lista n veces
for i in range(n):
    # Realizar comparaciones entre elementos adyacentes
    for j in range(0, n - i - 1):
        # Si el elemento actual es mayor que el siguiente
        if lista_ingresos[j] > lista_ingresos[j + 1]:
            # Intercambiar los elementos usando una variable temporal
            temp = lista_ingresos[j]
            lista_ingresos[j] = lista_ingresos[j + 1]
            lista_ingresos[j + 1] = temp

print("Lista ordenada:", lista_ingresos)
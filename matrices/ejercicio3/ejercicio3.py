
"""
3- Inicializar una matriz de 4 columnas y 4 filas. 
Cargar en cada cruce de fila y columna el
valor correspondiente a la multiplicación del índice 
de fila y columna"""

def inicializar_matriz(cantidad_filas: int, 
                    cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz: list) -> list: 
    # Verificar si es na lista:
    if type(matriz) != list:
        print("La función debe recibir una lista.")
        return None
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

def multiplicar_matriz(matriz: list) -> list:
    # Verificar si es na lista:
    if type(matriz) != list:
        print("La función debe recibir una lista.")
        return None
    
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_multiplicar = inicializar_matriz(filas, columnas, 0)

    for i  in range(filas):
        for j in range(columnas):
            matriz_multiplicar[i][j] = i * j

    return matriz_multiplicar



#2- Crear una función que imprima por pantalla el tamaño de una matriz
def mostrar_tamanio(matriz: list) -> None:
    """Imprime el tamaño de una matriz en la forma (filas, columnas).
    Args
    matriz (list): Matriz a verificar
    
    Returns
    None
    """
    # Verificar si es na lista:
    if type(matriz) != list:
        print("La función debe recibir una lista.")
        return None
    
    # Calcula el tamaño de la matriz:
    filas = len(matriz)
    columnas = len(matriz[0])
    print(f"La matriz tiene {filas} filas y {columnas} columnas.")



"""1- Crear una función que agregue una columna a una matriz existente. No se pueden usar
funciones preexistentes como append, se debe resolver con lo visto en las clases.
(concatenar)"""

def agregar_columna(matriz: list, columna: list) -> list:
    """La funcíón agrega columna a la matriz existente
    Args:
    matriz (list): Matriz a la que se agregará la columna
    columna (list): Columna a agregar a la matriz
    
    Returns:
    list: Matriz con la columna agregada al final
    """
    # Verificar si es na lista:
    if type(matriz) != list or type(columna) != list:
        print("La función debe recibir una lista.")
        return None
    matriz_nueva = []
    for i in range(len(matriz)):
        fila_nueva = matriz[i] + [columna[i]] #[1, 2, 3] + [10]...
        matriz_nueva += [fila_nueva]
    return matriz_nueva


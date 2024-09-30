
""" Ver el apunte de algoritmos matemáticos 
y generar una función que devuelva una
matriz transpuesta"""

def transponer_matriz(matriz: list) -> list:
    """Devuelve una matriz transpuesta de la entrada.
    Args
    matriz (list): Lista de listas que representa la matriz a transponer
    
    Returns
    list: Lista de listas que representa la matriz transpuesta
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    
    for i in range(columnas):
            nueva_fila = []  
            for j in range(filas):
                nueva_fila += [matriz[j][i]]  
            transpuesta += [nueva_fila]  

    return transpuesta


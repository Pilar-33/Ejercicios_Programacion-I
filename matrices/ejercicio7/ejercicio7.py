
""" 7- Crear una función que multiplique matrices. 
Verificar previamente que las matrices
puedan ser multiplicadas"""

def multiplicar_matrices(matriz1: list, matriz2: list) -> list:
    """Multiplica dos matrices
    Args:
    matriz1 (list): Primera matriz
    matriz2 (list): Segunda matriz
    
    Returns
    list: Resultado de la multiplicación de las matrices
    """
    # Verificar que las matrices sean listas
    if type(matriz1)!= list or type(matriz2)!= list:
        print("Las matrices deben ser listas.")
        return None
    
    # Verificar que las matrices tengan el mismo número de columnas
    if len(matriz1[0]) != len(matriz2):
        print("Las matrices no pueden ser multiplicadas.")
        return None
    
    
    # Inicializar la matriz resultado
    filas_resultado = len(matriz1)
    columnas_resultado = len(matriz2[0])
    resultado = []
    for _ in range(filas_resultado):
        fila = [0] * columnas_resultado
        resultado += [fila]
    
    # Multiplicar las matrices
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado



#11- Programar el algoritmo de búsqueda binaria de forma recursiva
# 11- Programar el algoritmo de búsqueda binaria de forma recursiva

def buscar_binario_recursivo(lista: list, buscado: any, inicio: int, final: int) -> int:  
    """Busca un elemento en una lista ordenada utilizando el algoritmo 
    de búsqueda binaria recursiva.
    Args:
    lista (list): Lista ordenada.
    buscado (any): Elemento a buscar.
    inicio (int): Indice inicial del segmento de la lista a buscar.
    final (int): Indice final del segmento de la lista a buscar.
    
    Returns:
    int: Indice del elemento buscado en caso de encontrarlo, None en caso contrario."""  
    if inicio > final: #Si esta ordenada la lista significa que se revisaron todos
        return None
    medio = (inicio + final) // 2
    
    if lista[medio] == buscado:
        return medio
    elif lista[medio] < buscado:
        return buscar_binario_recursivo(lista, buscado, medio + 1, final) #coloco donde inicia
    else:
        return buscar_binario_recursivo(lista, buscado, inicio, medio - 1) #coloco donde termina
    


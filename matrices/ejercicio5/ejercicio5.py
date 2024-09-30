
""" 5- Realizar una función que calcula la media 
de cualquier lista. 
Validar que lo que se recibe
sean números"""

def calcular_media(lista: list) -> float:
    """
    Calcula la media de una lista de números.

    Args:
    lista (list): Lista de números

    Returns:
    media (float): Media de los números de la lista
    """
    # Verificar si es una lista:
    if type(lista) != list:
        print("La función debe recibir una lista.")
        return None
    
    #Verificar que los elementos sean números
    for i in lista:
        if not(type(i) == int or type(i) == float):
            print("La lista debe contener solo números.")
            return None
        
    suma = 0
    cantidad = 0
    
    for i in range(len(lista)): 
        suma += lista[i]
        cantidad += 1

    if cantidad > 0:
        media = suma/cantidad
    else:
        media = 0

    return media

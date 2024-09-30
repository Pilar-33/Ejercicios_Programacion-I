

"""4- Dadas las siguientes listas anidadas:
nombres = [“Juan”, “Ricardo”, “Nahuel”, “Eugenia”, “Jimena”]
edades = [23, 35, 34, 40, 24]
generos = [“Hombre”, “Hombre”, “Hombre”, “Mujer”, “Mujer”]
a) Calcular media etaria para hombres y mujeres"""


def calcular_media_etaria(nombres: list, edades: list, generos: list) -> list:
    """
    Calcula la media etaria de hombres y mujeres y devuelve tres listas con los nombres de cada grupo.
    Args:
    nombres (list): Lista de nombres
    edades (list): Lista de edades
    generos (list): Lista de géneros
    Returns:
    media_hombres (float): Media de edad de hombres
    media_mujeres (float): Media de edad de mujeres
    hombres (list): Lista de nombres de hombres
    mujeres (list): Lista de nombres de mujeres
    """
    # Verificar si es na lista:
    if type(nombres) != list or type(edades) != list or type(generos) != list:
        print("La función debe recibir una lista.")
        return None
    
    suma_hombre = 0
    cantidad_hombres = 0
    hombres = []
    cantidad_mujeres = 0
    suma_mujer = 0
    mujeres = []
    
    for i in range(len(edades)): 
        if generos[i] == "Hombre":
            suma_hombre += edades[i]
            cantidad_hombres += 1
            hombres += [nombres[i]]
            
        elif generos[i] == "Mujer":
            suma_mujer += edades[i]
            cantidad_mujeres += 1
            mujeres += [nombres[i]]

    if cantidad_hombres > 0:
        media_hombres = suma_hombre/cantidad_hombres
    else:
        media_hombres = 0

    if cantidad_mujeres > 0:
        media_mujeres = suma_mujer/cantidad_mujeres
    else:
        media_mujeres = 0

    return media_hombres, media_mujeres, mujeres, hombres


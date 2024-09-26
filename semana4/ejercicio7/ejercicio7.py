
"""7- Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia",
"Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las personas
de menor edad (puede ser más de una) y las retorne. El programa principal deberá mostrar
nombre y edad de los menores"""

# Funciones
def menor_edad(edades: list, nombres: list) -> list:
    """Busca a las personas 
    de menor edad y las retorna

    Args:
    edades (list): Lista de edades de las personas.

    Returns:
    list: Lista de nombres y edades de las 
    personas de menor edad.
    """
    menor_edad = edades[0]
    edad_menores = []
    nombres_menores = []

    for edad in edades:
        if edad < menor_edad:
            menor_edad = edad
    
    for i in range(len(edades)):
        if edades[i] == menor_edad:
            edad_menores += [edades[i]]
            nombres_menores += [nombres[i]]

    return nombres_menores, edad_menores


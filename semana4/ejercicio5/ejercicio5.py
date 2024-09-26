from os import system
system("cls")
"""5- Realizar una función que permita corregir las listas del ejercicio 3 en caso de ser
necesario. Para ello se debe poder acceder a una posición particular y cargar nuevos
valores para el listado con valor incorrecto en dicha posición."""


def corregir_lista(lista_nombres: list) -> list:
    """Permite corregir una posición de una lista.
    Args:
    lista_nombres (list): Lista en la que se corregirá un dato.
    posicion (int): Posición en la que se corregirá un dato.
    nuevo_dato (str): Nuevo dato que se cargará en la posición 
    ingresada por el usuario.
    
    Returns:
    list: Lista corregida.
    """
    
    cargar_dato = "si"
    
    while cargar_dato == "si":
        posicion = int(input("Ingrese la posicion a corregir: "))
        while posicion < 0 or posicion > len(lista_nombres):
            posicion = int(input("Posicion invalida. Ingrese nuevamente la posicion: "))
            
        nuevo_dato = input("Ingrese el nuevo dato: ")
        lista_nombres[posicion] = nuevo_dato

        cargar_dato = input("Desea corregir otro dato (si/no)? ")
        while cargar_dato != "si" and cargar_dato != "no":
            cargar_dato = input("Opcion invalida. Desea corregir otro dato (si/no)? ")

    return lista_nombres



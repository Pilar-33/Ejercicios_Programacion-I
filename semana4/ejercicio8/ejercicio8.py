"""8- Desarrollar una función que verifique si todos 
los elementos de una lista son del mismo tipo. En ese caso que 
devuelva el tipo que contiene, en caso contrario
que informe qué tiposde elementos contiene.
"""

def verificar_elementos(lista: list) -> str:
    """Verifica si todos los elementos de una lista son del mismo tipo
    o de diferentes tipos.
    
    Args:
    (lista: list):  Lista de elementos a verificar.
    
    Returns:
    str: Mensaje con la información sobre los tipos de 
    datos en la lista.
    """

    tipos_datos = []
    for elemento in lista:
        tipo = type(elemento)
        if tipo not in tipos_datos:
            tipos_datos += [tipo]
    
    if len(tipos_datos) == 1:
        tipo = f"Los elementos son del mismo tipo: {tipos_datos[0]}"
    else:
        tipo = f"Los elementos son de distintos tipos: {tipos_datos}"

    return tipo




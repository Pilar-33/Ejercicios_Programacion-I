
# 6- Desarrollar una función que pida 10 números dentro de un rango especificado,
# validar los números solicitados dentro de ese rango, guardar en una 
# lista y retornarla. El programa principal debe invocar a la función 
# y mostrar por pantalla el retorno

def validar_numeros(inferior: int, superior: int) -> list:
    """Valida y devuelve una lista de números validados dentro de un rango.
    Args:
    inferior (int): Límite inferior del rango.
    superior (int): Límite superior del rango.
    
    Returns:
    list: Lista de números válidos dentro del rango.
    """ 
    lista_numeros = []
    for i in range(10):
        numero = int(input(f"Ingrese un número {i+1} entre {inferior} y {superior}: "))
        while numero < inferior or  numero > superior:
            numero = int(input(f"Fuera del rango!!.\nIngrese un número {i+1} entre {inferior} y {superior}: "))
        lista_numeros += [numero]
    return lista_numeros



    
        
        
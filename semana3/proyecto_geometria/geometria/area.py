
""" Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github
"""
# Función área círculo
def calcular_area_circulo(radio = 3) -> float:

    """Calcula el área de un círculo.
    Args
    radio (int, opcional): Valor del radio del círculo
    
    Returns
    float: Valor del área del círculo
    """
    PI = 3.14
    area_circulo = PI * radio ** 2
    return area_circulo

# Función cuadrado
def calcular_area_cuadrado(lado: float) -> float:

    """Calcula el área de un cuadrado.
    Args
    longitud_lado (int): Valor de la longitud 
    del lado del cuadrado
    
    Returns
    float: Valor del área del cuadrado
    """
    area_cuadrado = lado ** 2
    return area_cuadrado

# Función triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:

    """Calcula el perímetro de un triángulo.
    Args
    base (int): Valor de la base del triángulo
    altura (int): Valor de la altura del triángulo
    
    Returns
    float: Valor del perímetro del triángulo
    """
    area_triangulo = (base * altura) / 2
    return area_triangulo
    
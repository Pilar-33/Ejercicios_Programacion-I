
# Función perimetro de círculo
def calcular_perimetro_circulo(radio: int = 3) -> float:
    """Calcula el perímetro de un círculo.

    Aegs
    radio (int, optional): Radio del círculo.
    Returns

    float: Valor del perímetro del círculo.
    """
    PI =  3.14
    perimetro = 2 * radio * PI
    return perimetro

# Funcón perimetro del cuadrado
def calcular_perimetro_cuadrado(lado: int) -> float:
    """
    Calcula el perímetro de un cuadrado.
    Args
    lado (int): Lado del cuadrado.

    Returns
    float: Valor del perímetro del cuadrado.
    """
    perimetro = 4 * lado
    return perimetro

# Función perimetro del triángulo
def calcular_perimetro_triangulo(lado1: float, lado2: float, lado3: float) -> float:
    """
    Calcula el perímetro de un triángulo.
    Args
    lado1 (int): Lado 1 del triángulo.
    lado2 (int): Lado 2 del triángulo.
    lado3 (int): Lado 3 del triángulo.

    Returns
    float: Valor del perímetro del triángulo.
    """
    perimetro = lado1 + lado2 + lado3
    return perimetro
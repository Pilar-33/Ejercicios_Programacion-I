from os import system
system("cls")

"""
1 - Calcular mediante recursividad la potencia de un número, mediante una función que
recibe un número base de tipo entero y un exponente de tipo entero. Utilizar parámetros
opcionales para definir que si la función no recibe ningún parámetro devolverá 2 al
cuadrado."""


def calcular_potencia(base: int = 2, exponente: int = 2) -> int:
    """Calcula la potencia de un número utilizando recursión.
    Args
    base (int): Número base
    exponete (int): Exponente

    Returns
    int: Resultado de la potencia
    """
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado


# Testeo de la función
# valores por defecto
potencia = calcular_potencia()
print(f"La potencia de 2 elevado a 2 es: {potencia}")

# valores ingresados
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
while exponente < 0:
    print("Error! El exponente debe ser un número entero positivo.")
    exponente = int(input("Ingrese el exponente: "))
potencia = calcular_potencia(base, exponente)
print(f"La potencia de {base} elevado a {exponente} es: {potencia}")

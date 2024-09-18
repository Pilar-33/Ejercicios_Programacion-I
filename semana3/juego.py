from os import system
system("cls")

def torres_de_hanoi(n: int, origen: str, destino: str, auxiliar: str) -> None:
    """
    Solución de problema del problema de las torres de Hanoi utilizando recursion.
    Args:
    n (int): Número de discos.
    origen (str): Pieza de origen.
    destino (str): Pieza de destino.
    auxiliar (str): Pieza auxiliar.
    Returns:
    None
    Muestra los pasos para resilver problema de las 
    torres de Honoi.
    """
    if n == 1:
        # Caso base: solo queda un disco, lo movemos directamente
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        # Mover los n-1 discos de origen a auxiliar
        torres_de_hanoi(n-1, origen, auxiliar, destino)
        # Mover el disco n de origen a destino
        print(f"Mover disco {n} de {origen} a {destino}")
        # Mover los n-1 discos de auxiliar a destino
        torres_de_hanoi(n-1, auxiliar, destino, origen)

# Número de discos
n = int(input("Indique el número de discos: "))
# Probando
torres_de_hanoi(n, 'A', 'C', 'B')



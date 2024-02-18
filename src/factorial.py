"""
Mòdul per a calcular el factorial
"""
def factorial(num):
    """
    Funció per a calcular el factorial de un número
    Entrada: Número per a calcular el factorial
    Salida: Factorial del número
    """
    if not isinstance (num,int):
        raise TypeError ("Introdueix un número la proxima vegada")
    if num==1 or num==0:
        return 1
    if num < 0:
        raise ValueError ("El número es negatiu")
    return num * factorial(num - 1)
    
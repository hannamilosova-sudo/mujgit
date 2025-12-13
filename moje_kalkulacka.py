def soucet(a, b):
    """
    Sečte dvě čísla.

    :param a: První sčítanec
    :param b: Druhý sčítanec
    :return: Součet hodnot a a b
    """
    return a + b


def rozdil(a, b):
    """
    Odečte druhé číslo od prvního.

    :param a: Menšenec
    :param b: Menšitel
    :return: Rozdíl a - b
    """
    return a - b


def soucin(a, b):
    """
    Vynásobí dvě čísla.

    :param a: První činitel
    :param b: Druhý činitel
    :return: Součin a * b
    """
    return a * b


def podil(a, b):
    """
    Vydělí první číslo druhým.

    :param a: Dělenec
    :param b: Dělitel
    :return: Podíl a / b
    :raises ZeroDivisionError: Pokud je b rovno 0
    """
    if b == 0:
        raise ZeroDivisionError("Nelze dělit nulou")
    return a / b

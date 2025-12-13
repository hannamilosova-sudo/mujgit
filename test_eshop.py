def vypocitej_cenu(cena_bez_dane, dph):
    """
    Vypočítá finální cenu produktu včetně DPH.

    :param cena_bez_dane: Cena bez DPH
    :param dph: Hodnota DPH (např. 0.21 pro 21 %)
    :return: Cena včetně DPH
    :raises ValueError: Pokud je DPH záporné
    """
    if dph < 0:
        raise ValueError("DPH musí být větší nebo rovno nule")

    return cena_bez_dane * (1 + dph)


def vypocitej_slevu(cena, sleva_procenta):
    """
    Vypočítá finální cenu produktu po aplikaci slevy.

    :param cena: Původní cena produktu
    :param sleva_procenta: Sleva v procentech (0–100)
    :return: Cena po slevě
    :raises ValueError: Pokud sleva není v rozsahu 0–100
    """
    if not 0 <= sleva_procenta <= 100:
        raise ValueError("Sleva musí být mezi 0 a 100")

    return cena * (1 - sleva_procenta / 100)


def ma_zadarmo_dodani(celkova_cena):
    """
    Určí, zda má zákazník nárok na dopravu zdarma.

    :param celkova_cena: Celková cena objednávky
    :return: True, pokud je cena alespoň 1500 Kč, jinak False
    """
    return celkova_cena >= 1500


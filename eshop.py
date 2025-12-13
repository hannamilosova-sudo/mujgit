def vypocitej_cenu(cena_bez_dane, dph):
    """Vrátí cenu včetně DPH"""
    if dph < 0:
        raise ValueError("DPH musí být větší nebo rovno 0")
    return cena_bez_dane * (1 + dph)


def vypocitej_slevu(cena, sleva_procenta):
    if not 0 <= sleva_procenta <= 100:
        raise ValueError("Sleva musí být mezi 0 a 100")
    return cena * (1 - sleva_procenta / 100)


def ma_zadarmo_dodani(celkova_cena):
    return celkova_cena >= 1500

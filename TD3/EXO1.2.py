def diviser(a: float, b: float) -> float:
    if isinstance(a, int):
        raise TypeError("la valeur fourni doit etre de typer entier")
    return a/b


def Principale():
    try:
        resultat = diviser(8, 0)
    except ValueError as verr:
        print("erreur: tu peux pas diviser comme ça")
    except TypeError as e:
        print(f"erreur : {e}")   # traitement de toute les autres exepctions
    else:
        print(f"resultat : {resultat}")
    finally:
        print("fin calcul")


if __name__ == "__main__":
    Principale()
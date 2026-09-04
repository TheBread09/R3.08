def affiche(texte: str) -> None:
    print(f"texte à afficher : {texte}")


class Velo:

    def __init__(self, marque: str, taille_pneu: int, couleur: str, nb_vitesses: int):
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nb_vitesses = nb_vitesses
        self.vitesse_courante = 1

    def __str__(self) -> str:
        return (f"Vélo {self.marque} {self.couleur}, pneus {self.taille_pneu} pouces, "
                f"vitesse {self.vitesse_courante}/{self.nb_vitesses}")

    def vitesse_plus(self) -> int:
        if self.vitesse_courante < self.nb_vitesses:
            self.vitesse_courante += 1
        else:
            print("Déjà à la vitesse maximale.")
        return self.vitesse_courante

    def vitesse_moin(self) -> int:
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1
        else:
            print("Déjà à la vitesse minimale.")
        return self.vitesse_courante


def main() -> None:
    str1 = "Bonjour, ceci est le TD sur les classes."
    affiche(str1)

    v1 = Velo("Decathlon", 26, "rouge", 21)
    print(v1)

    print("Passage vitesse supérieure :", v1.vitesse_plus())
    print("Passage vitesse supérieure :", v1.vitesse_plus())
    print("Passage vitesse inférieure :", v1.vitesse_moin())


if __name__ == "__main__":
    main()
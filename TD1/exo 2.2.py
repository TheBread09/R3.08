class Tasse:

    matiere: str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque


    def __str__(self) -> str:
        return (f"la tasse de matière {self.matiere}, de couleur {self.couleur} "
                f"et de marque {self.marque} a une contenance de {self.contenance} ml")



    def remplir(self, boisson: str) -> None:

        self.contenu = boisson
        print(f"La tasse contient maintenant : {self.contenu}")



    def boire(self) -> None:
        if hasattr(self, "contenu"):
            print(f"Vous buvez : {self.contenu}. La tasse est  vide.")
            del self.contenu
        else:
            print("La tasse est déjà vide.")

if __name__ == "__main__":
    t1 = Tasse("bleue", 50, "TEFAL")
    t2 = Tasse("blanche", 250, "NIKE")
    print(t1)
    print(t2)
    t1.remplir("café")
    print(vars(t1))
    t1.boire()
    print(vars(t1))
    t1.boire()
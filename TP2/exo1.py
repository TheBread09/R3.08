class Personnage:

    def __init__(self, pseudo: str, niveau: int = 1, pv: int = None, initiative: int = None):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__initiative = initiative if initiative is not None else niveau
        self.__pv = pv if pv is not None else niveau
        self.__pv_max = self.__pv

    @property
    def niveau(self) -> int:
        return self.__niveau

    @property
    def initiative(self) -> int:
        return self.__initiative

    @property
    def pseudo(self) -> str:
        if not isinstance(self.__pseudo, str):
            raise TypeError
        return self.__pseudo

    @property
    def pv(self) -> int:
        return self.__pv

    @pv.setter
    def pv(self, point: int):
        self.__pv = point

    def degats(self) -> int:
        return self.__niveau

    def soigner(self):
        self.pv = self.__pv_max

    def attaque(self, opposant: "Personnage"):
        if self.initiative > opposant.initiative:
            opposant.pv -= self.degats()
            if opposant.pv > 0:
                self.pv -= opposant.degats()

        elif self.initiative < opposant.initiative:
            self.pv -= opposant.degats()
            if self.pv > 0:
                opposant.pv -= self.degats()

        else:
            opposant.pv -= self.degats()
            self.pv -= opposant.degats()

    def combattre(self, opposant: "Personnage"):
        tour = 1
        while self.pv > 0 and opposant.pv > 0:
            print(f"--- Tour {tour} ---")
            self.attaque(opposant)
            print(f"{self.pseudo}: {self.pv} PV   |   {opposant.pseudo}: {opposant.pv} PV")
            tour += 1

        gagnant = self if self.pv > 0 else opposant
        print(f"{gagnant.pseudo} remporte le combat !")

    def __eq__(self, other):
        return isinstance(other, Personnage) and self.pseudo == other.pseudo

    def __repr__(self):
        return f"{type(self).__name__}({self.pseudo}, niveau={self.niveau})"


class Guerrier(Personnage):

    def __init__(self, pseudo: str, niveau: int = 1):
        pv = niveau * 8 + 4
        init = niveau * 4 + 6
        super().__init__(pseudo, niveau, pv, init)

    def degats(self) -> int:
        return self.niveau * 2


class Mage(Personnage):

    def __init__(self, pseudo: str, niveau: int = 1):
        pv = niveau * 5 + 10
        init = niveau * 6 + 4
        super().__init__(pseudo, niveau, pv, init)
        self.__mana = niveau * 5

    @property
    def mana(self) -> int:
        return self.__mana

    def degats(self) -> int:
        if self.__mana >= 4:
            self.__mana -= 4
            return self.niveau + 3
        return self.niveau




class Joueur:
    def __init__(self, nom:str, max_perso: int):
        self.__nom = nom
        self.__niveau = max_perso
        self.__personnages = []

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def personnages(self) -> list:
        return self.__personnages

    def ajouter_personnage(self, personnage: Personnage):
        if len(self.__personnages) < self.__niveau:
            self.__personnages.append(personnage)
            return True
        return False

    def personnage_num(self, numero: int):
        if 0 <= numero <= len(self.__personnages):
            return self.__personnages[numero]
        return False

    def personnage_nom(self, pseudo: str):
        for p in self.__personnages:
            if p.pseudo == pseudo :
                return p
        return None


    def elimine_personnage_num(self, numero: int):
        if 0 <= numero < len(self.__personnages):
            p = self.__personnages.pop(numero)
            print (f"personnage {p.pseudo} elimine")

    def eliminer_personnage_pseudo(self, pseudo: str):
        p = self.get_personnage_pseudo(pseudo)
        if p:
            self.__personnages.remove(p)
            print (f"personnage {p.pseudo} elimine")

    def eliminer_personnage_perso(self, p_recherche):
        if p_recherche in self.__personnages:
            self.__personnages.remove(p_recherche)
            print(f"personnage {p_recherche} elimine")





if __name__ == "__main__":
    p1 = Personnage("el diablo, chevalier", 50)
    p2 = Mage("gandalf", 67)
    p3 = Guerrier("darius",10)

    g = Guerrier("Roi arthur", 29)
    m = Mage("Harry", 45)


    joueur1 = Joueur("Joueur 1", 3)
    joueur2 = Joueur("Joueur 2", 4)
    joueur3 = Joueur("Joueur 3", 5)


    joueur1.ajouter_personnage(p1)
    print("personnage 1 ajouter")
    joueur2.ajouter_personnage(p2)
    print("personnage 2 ajouter")
    joueur1.elimine_personnage_num(1)
    joueur2.eliminer_personnage_pseudo(2)
    print("joueur 1 et 2 mort")

    joueur1.ajouter_personnage(p1)
    print("personnage 1 ajouter")
    joueur2.ajouter_personnage(p2)
    print("personnage 2 ajouter")
    joueur3.ajouter_personnage(p3)
    print("personnage 3 ajouter")



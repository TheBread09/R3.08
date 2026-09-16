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






if __name__ == "__main__":
    p1 = Personnage("el diablo, chevalier", 50)
    p2 = Personnage("gandalf", 67)
    p1.combattre(p2)

    g = Guerrier("Roi arthur", 29)
    m = Mage("Harry", 45)
    g.combattre(m)
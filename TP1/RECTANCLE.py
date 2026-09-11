from POINT import Point


class Rectangle:

    def __init__(self, pointBasGauche: "Point" = None, longueur: float = 1,
                 hauteur: float = 1, pointHautDroit: "Point" = None):
        if pointBasGauche is None:
            pointBasGauche = Point()
        if pointHautDroit is not None:
            longueur = pointHautDroit.get_x() - pointBasGauche.get_x()
            hauteur = pointHautDroit.get_y() - pointBasGauche.get_y()
        self.__pointBasGauche = pointBasGauche  # __ = privé en python
        self.__longueur = longueur
        self.__hauteur = hauteur

    def __str__(self):
        return f"Rectangle pointBasGauche={self.__pointBasGauche}, " \
               f"longueur={self.__longueur}, hauteur={self.__hauteur}"

    def surface(self) -> float:
        return self.__longueur * self.__hauteur

    def perimetre(self) -> float:
        return 2 * (self.__longueur + self.__hauteur)

    def pointBasGauche(self) -> "Point":
        return self.__pointBasGauche

    def pointBasDroit(self) -> "Point":
        return Point(self.__pointBasGauche.get_x() + self.__longueur,
                      self.__pointBasGauche.get_y())

    def pointHautGauche(self) -> "Point":
        return Point(self.__pointBasGauche.get_x(),
                      self.__pointBasGauche.get_y() + self.__hauteur)

    def pointHautDroit(self) -> "Point":
        return Point(self.__pointBasGauche.get_x() + self.__longueur,
                      self.__pointBasGauche.get_y() + self.__hauteur)

    def contient(self, point: "Point") -> bool:
        xMin = self.__pointBasGauche.get_x()
        yMin = self.__pointBasGauche.get_y()
        return (xMin <= point.get_x() <= xMin + self.__longueur) and \
               (yMin <= point.get_y() <= yMin + self.__hauteur)


def Principale():
    rectangle1 = Rectangle()
    rectangle2 = Rectangle(Point(1, 1), 5, 3)
    rectangle3 = Rectangle(pointBasGauche=Point(0, 0), pointHautDroit=Point(4, 2))

    print(f"Rectangle 1 : {rectangle1}")
    print(f"Rectangle 2 : {rectangle2}")
    print(f"Rectangle 3 : {rectangle3}")

    print(f"Surface rectangle 2 : {rectangle2.surface()}")
    print(f"Perimetre rectangle 2 : {rectangle2.perimetre()}")
    print(f"Point bas gauche rectangle 2 : {rectangle2.pointBasGauche()}")
    print(f"Point bas droit rectangle 2 : {rectangle2.pointBasDroit()}")
    print(f"Point haut gauche rectangle 2 : {rectangle2.pointHautGauche()}")
    print(f"Point haut droit rectangle 2 : {rectangle2.pointHautDroit()}")
    print(f"Rectangle 2 contient Point(2,2) : {rectangle2.contient(Point(2, 2))}")
    print(f"Rectangle 2 contient Point(10,10) : {rectangle2.contient(Point(10, 10))}")


if __name__ == "__main__":
    Principale()
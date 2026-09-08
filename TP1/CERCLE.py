import math
from POINT import Point


class Cercle:

    def __init__(self, rayon: float, centre: "Point" = None):
        if centre is None:
            centre = Point()
        self.__centre = centre  # __ = privé en python
        self.__rayon = rayon

    def __str__(self):
        return f"Cercle centre={self.__centre}, rayon={self.__rayon}"

    def diametre(self) -> float:
        return 2 * self.__rayon

    def perimetre(self) -> float:
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        return math.pi * math.pow(self.__rayon, 2)

    def intersecte(self, autre: "Cercle") -> bool:
        distance = self.__centre.distancePoint(autre.__centre)
        return distance <= (self.__rayon + autre.__rayon) and distance >= abs(self.__rayon - autre.__rayon)

    def contient(self, point: "Point") -> bool:
        return self.__centre.distancePoint(point) <= self.__rayon


def Principale():
    cercle1 = Cercle(5)
    cercle2 = Cercle(3, Point(4, 0))

    print(f"Cercle 1 : {cercle1}")
    print(f"Cercle 2 : {cercle2}")

    print(f"Diametre cercle 1 : {cercle1.diametre()}")
    print(f"Perimetre cercle 1 : {cercle1.perimetre()}")
    print(f"Surface cercle 1 : {cercle1.surface()}")
    print(f"Cercle 1 intersecte cercle 2 : {cercle1.intersecte(cercle2)}")
    print(f"Cercle 1 contient Point(1,1) : {cercle1.contient(Point(1, 1))}")


if __name__ == "__main__":
    Principale()
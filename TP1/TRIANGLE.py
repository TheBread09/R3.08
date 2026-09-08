import math
from POINT import Point


class Triangle:

    def __init__(self, cote1: float, cote2: float, angleDroit: "Point" = None):
        if angleDroit is None:
            angleDroit = Point()
        self.__cote1 = cote1  # __ = privé en python
        self.__cote2 = cote2
        self.__angleDroit = angleDroit

    def __str__(self):
        return f"Triangle cote1={self.__cote1}, cote2={self.__cote2}, angleDroit={self.__angleDroit}"

    def hypotenuse(self) -> float:
        return math.sqrt(math.pow(self.__cote1, 2) + math.pow(self.__cote2, 2))

    def perimetre(self) -> float:
        return self.__cote1 + self.__cote2 + self.hypotenuse()

    def surface(self) -> float:
        return (self.__cote1 * self.__cote2) / 2

    def estIsocele(self) -> bool:
        return self.__cote1 == self.__cote2


def Principale():
    triangle1 = Triangle(3, 4)
    triangle2 = Triangle(5, 5, Point(1, 1))

    print(f"Triangle 1 : {triangle1}")
    print(f"Triangle 2 : {triangle2}")

    print(f"Hypotenuse triangle 1 : {triangle1.hypotenuse()}")
    print(f"Perimetre triangle 1 : {triangle1.perimetre()}")
    print(f"Surface triangle 1 : {triangle1.surface()}")
    print(f"Triangle 1 isocele : {triangle1.estIsocele()}")


if __name__ == "__main__":
    Principale()
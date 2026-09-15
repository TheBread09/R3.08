import math


class Point:

    def __init__(self, x: float = 0, y: float = 0):
        if not isinstance(x, (int, float)):
            raise TypeError("les coordonnees x doivent reel")
        if not isinstance(y, (int, float)):
            raise TypeError("les coordonnees y doivent reel")
        self.__x = x
        self.__y = y  # __ = privé en python

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def set_x(self, x: float):
        self.__x = x

    def set_y(self, y: float):
        self.__y = y

    def __str__(self):
        return f"Point {self.__x},{self.__y}"

    def distanceCoord(self, a: float, b: float) -> float:
        return math.sqrt(math.pow(self.__x - a, 2) + math.pow(self.__y - b, 2))

    def distancePoint(self, camarade: "Point") -> float:
        return self.distanceCoord(camarade.__x, camarade.__y)


def Principale():
    try:
        point1 = Point('a', 0)  # fait l'erreur pour le reel
        point2 = Point(3, 4)

        print(f"Point 1 : {point1}")
        print(f"Point 2 : {point2}")
        print(f"Distance entre Point 1 et les coordonnées (3, 4) : {point1.distanceCoord(3, 4)}")
        print(f"Distance entre Point 1 et Point 2 : {point1.distancePoint(point2)}")

    except TypeError as e:
        print(f"erreur : {e}")
    finally:
        print("fin du programme")


if __name__ == "__main__":
    Principale()
import math


class Point:

    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y  # __ = privé en python

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def __str__(self):
        return f"Point {self.__x},{self.__y}"

    def distanceCoord(self, a: float, b: float) -> float:
        return math.sqrt(math.pow(self.__x - a, 2) + math.pow(self.__y - b, 2))

    def distancePoint(self, camarade: "Point") -> float:
        return self.distanceCoord(camarade.__x, camarade.__y)


def Principale():
    point1 = Point(0, 0)
    point2 = Point(3, 4)

    print(f"Point 1 : {point1}")
    print(f"Point 2 : {point2}")

    print(f"Distance entre Point 1 et les coordonnées (3, 4) : {point1.distanceCoord(3, 4)}")
    print(f"Distance entre Point 1 et Point 2 : {point1.distancePoint(point2)}")


if __name__ == "__main__":
    Principale()
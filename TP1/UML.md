Point
- x : float
- y : float
+ Point()
+ Point(a : float, b : float)
+ distanceCoord(a : float, b : float) : float
+ distancePoint(camarade : Point) : float



Cercle
- centre : Point
- rayon : float
+ Cercle(rayon : float)
+ Cercle(rayon : float, centre : Point)
+ diametre() : float
+ perimetre() : float
+ surface() : float
+ intersecte(autre : Cercle) : bool
+ contient(point : Point) : bool


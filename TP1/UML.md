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



Rectangle
- pointBasGauche : Point
- longueur : float
- hauteur : float
+ Rectangle()
+ Rectangle(pointBasGauche : Point, longueur : float, hauteur : float)
+ Rectangle(pointBasGauche : Point, pointHautDroit : Point)
+ surface() : float
+ perimetre() : float
+ pointBasGauche() : Point
+ pointBasDroit() : Point
+ pointHautGauche() : Point
+ pointHautDroit() : Point
+ contient(point : Point) : bool




Triangle
- cote1 : float
- cote2 : float
- angleDroit : Point
+ Triangle(cote1 : float, cote2 : float)
+ Triangle(cote1 : float, cote2 : float, angleDroit : Point)
+ hypotenuse() : float
+ perimetre() : float
+ surface() : float
+ estIsocele() : bool
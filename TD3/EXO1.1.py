def diviser (a : float, b : float ) -> float:
   return a/b


def Principale():
    try :
        resultat = diviser (10,2)
        print (resultat)
    except :
        print("Impossible")
if __name__ == "__main__":
    Principale()


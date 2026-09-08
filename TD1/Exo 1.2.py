"""
def chnombre (ch1 : int, ch2: int) -> int:
    print ("Veuillez rentre un nombre ")
    ch1 = int (input ("Nombre: "))
    ch2 = int (input ("Nombre: "))
    if ch1 > ch2:
        return ch1
    else:
        return ch2
print(chnombre (1, 2))




def seuilnombre (ch1 : int, seuil : int) -> int:

    if ch1 > seuil:
        return print('AU DESSSUS')
    else:
        return print("dessous")

ch1 = int (input ("Nombre: "))
print (seuilnombre (1,10))




def Gnombre(*nombre):
  maxN = nombre[0]
  for i in nombre:
    if i > maxN:
      maxN = i
  return maxN

print(Gnombre(3, 7, 2, 9, 1, 18, 7))



def mini(*nombre)-> int:
    b = 3
    total = 0
    for i in nombre:
        if i < b :
            total += i
    return total
print(mini(1, 3, 5,4,5,8,9,1,2,0,2,1,4,8,6))





def afficheDico(dico, prefixe):
    for cle in dico:
        print(prefixe, cle, ":", dico[cle])

monDico = {"nom": "nordmann", "prenom": "maxence", "age": 21}
afficheDico(monDico, "->")


"""
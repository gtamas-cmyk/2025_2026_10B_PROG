import random as r
#Csutortokon For, Ciklusok, Szoveg szetszedese megforditasa stb

#generaljon ki 10db veletlen szamot
#irassa ki a szamok oszzeget
osszeg = 0
for tiz in range(0, 10, 1):
    velszam = r.randint(1, 9)
    osszeg += velszam
    print(velszam, end=" ")
print()
print("Osszeg:", osszeg)

#hf 
#hany db paros veletlen szamot generalt ki?
# melyik a legnagyobb veletlen szam?
import random as r
#Csutortokon For, Ciklusok, Szoveg szetszedese megforditasa stb

#generaljon ki 10db veletlen szamot
#irassa ki a szamok oszzeget
osszeg = 0
parosdb = 0
maxsz = 0
for tiz in range(0, 10, 1):
    velszam = r.randint(1, 9)
    osszeg += velszam
    if velszam % 2 == 0:
        parosdb += 1
    if maxsz == 0 or velszam > maxsz:
        maxsz = velszam
    print(velszam, end=" ")
print()
print("Osszeg:", osszeg)
print("paros szamok darabja:", parosdb)
print("legnagyobb veletlen szam:", maxsz)

#hf 
#hany db paros veletlen szamot generalt ki?
# melyik a legnagyobb veletlen szam?
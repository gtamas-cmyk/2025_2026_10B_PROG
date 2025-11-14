import random
import math
# 1. Számgenerálásos feladat:
# a. Generáljon ki egy 2 jegyű véletlen számot!
# b. Írasson ki egymás mellé szóközzel elválasztva annyi 3 jegyű véletlen számot, 
# amennyit az előző feladat kért! (Ha az előző feladatot nem sikerült 
# megcsinálnia, akkor dolgozzon 13-mal)
# c. Számolja meg, hány darab 3-al osztható szám van közöttük!
# d. Adja meg az összes szám összegének gyökét két tizedesjegyre kerekítve! (Ha 
# nem sikerült összeadnia a számokat akkor számoljon 300-al)
# 2. Szöveges feladat:
# a. Kérjen be a felhasználótól egy szöveget!
# b. Adja meg a szöveg középső karakterét. Ha két középső karaktere van, akkor 
# kettőt!
# c. Szedje ki a szöveg minden páros indexű karakterét!
# d. Írassa ki úgy, hogy minden betű után rak egy $ jelet!

#1.a
velszam = random.randint(10,99)
print(velszam)
#1.b
db = 0
osszeg = 0
for a in range(0, velszam, 1):
    haromjegyu = random.randint(100,999)
    if(haromjegyu % 3 == 0):
        db+=1
    osszeg += haromjegyu
    print(haromjegyu, end=" ")
print()
print(db)
print(round(math.sqrt(osszeg), 2))

#2. feladat
szoveg = input("Adjon meg egy szoveget: ")
if(len(szoveg) % 2 == 0):
    index = len(szoveg)//2
    print(szoveg[index])
else:
    index1 = len(szoveg) //2
    index2 = (len(szoveg) //2) -1
    print(szoveg[index1], szoveg[index2])

for ix in range(0, len(szoveg), 2):
    print(szoveg[ix],end="$")
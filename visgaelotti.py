#chatgpt altal adott feladatok lolol
# 1. Kérj be a felhasználótól egy szót, és for loop segítségével írasd ki fordítva.
import random as r
input_szo = input("Adjon meg egy szot: ")
forditott_input_szo = ""

for index in range(len(input_szo) -1, -1, -1):
    forditott_input_szo += input_szo[index]
print(forditott_input_szo)
print()

# 2. Kérj be egy mondatot, és írasd ki belőle a szóközök nélküli verziót.

mondat = input("Adj meg egy mondatot: ")
uj = ""

for karakter in mondat:
    if karakter != " ":
        uj += karakter
print(uj)
print()

# 3. Írj egy programot, ami 10 darab véletlen számot generál 1 és 100 között, majd:
# kiírja mindet
# kiszámolja az összegüket
# megmondja, melyik a legnagyobb páros szám.

osszeg = 0
velmax = 0
velmin = 0
parmax = 0

for tiz in range(0, 10, 1):
    velszam = r.randint(1, 100)
    osszeg += velszam
    if velmax == 0 or velszam > velmax:
        velmax = velszam
    if velmin == 0 or velszam < velmin:
        velmin = velszam
    if velszam % 2 == 0 and (parmax == 0 or velszam > parmax):
        parmax = velszam
    print(velszam, end=" ")
print()
print("Szamok osszege:", osszeg)
print("Legnagyobb veletlen szam:", velmax)
print("Legkisebb veletlen szam:", velmin)
print("Legnagyobb paros szam:", parmax)
print()

# 4. Kérj be egy szót, és számold meg, hány darab magánhangzó van benne.

szo = input("Irj Be egy szot: ")
mghk = {"a", "e", "i", "o", "u"}
szamlalo = 0

for betu in szo:
    if betu.lower() in mghk:
        szamlalo += 1
print(szamlalo)
print()

# 5. Kérj be egy mondatot, és írasd ki minden szavát külön sorba (for ciklussal, nem a split() függvénnyel).

mendemondat = input("Irj be egy mondatot: ")
szo2 = ""
for betu in mendemondat:
    if betu != " ":
        szo2 += betu
    else:
        print(szo2)
        szo2 = ""
print(szo2)
print()

#PDFBOL: 29. Generálj ki 10 db véletlen számot és add meg hány darab páros szám van!
parosdb = 0
for kalamajka in range(0, 10, 1):
    tebolyda = r.randint(2, 200)
    print(tebolyda, end=" ")
    if tebolyda % 2 == 0:
        parosdb += 1
print()
print("Paros szamok darabszama:", parosdb)
print()
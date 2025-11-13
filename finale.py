import random as r
# 1. feladat
# Kérj be a felhasználótól egy szót, és írasd ki fordítva for loop segítségével.
szo = input("(1) Adjon meg egy szot: ")
ujra = ""

for forditas in range(len(szo) -1, -1, -1):
    ujra += szo[forditas]
print(ujra)
print()

# 2. feladat
# Kérj be egy mondatot, és írasd ki belőle minden szóköz nélkül.
mondat = input("(2) Adjon meg egy mondatot: ")
ures = ""
for szokoz in mondat:
    if szokoz != " ":
        ures += szokoz
print(ures)
print()

# 3. feladat
# Generálj 10 véletlen számot 1 és 100 között, majd:
# írasd ki mindet
# számold ki az összegüket
# írd ki a legnagyobb számot
# írd ki a legkisebb számot
# írd ki a legnagyobb páros számot

osszeg = 0
velmin = 0
velmax = 0
parmax = 0

for rand in range(0, 10, 1):
    velszam = r.randint(1, 100)
    if velmin == 0 or velmin > velszam:
        velmin = velszam
    if velmax == 0 or velmax < velszam:
        velmax = velszam

    osszeg += velszam

    if velszam % 2 == 0 and (parmax == 0 or velszam > parmax):
        parmax = velszam
    print(velszam, end=" ")
print()
print("Osszeg:", osszeg)
print("Legkisebb Veletlen szam:", velmin)
print("Legnagyobb Veletlen Szam:", velmax)
print("Legnagyobb Paros szam:", parmax)
print()
# 4. feladat
# Kérj be egy szót, és számold meg, hány magánhangzó van benne (kis- és nagybetűt is vegyél figyelembe).

szo2 = input("(4) Adjon meg egy szot: ")
mgh = {"a","e","i","o","u"}
darab = 0

for betu in szo2:
    if betu.lower() in mgh:
        darab += 1
print("Maganhangzok szama:", darab)
print()

# 5. feladat
# Kérj be egy mondatot, és írasd ki minden szavát külön sorba (for loop + if, ne split()).

mondat2 = input("(5) Adjon meg egy mondatot: ")
szokoz = ""
for tetu in mondat2:
    if tetu != " ":
        szokoz += tetu
    else:
        print(szokoz)
        szokoz = ""
print(szokoz)
print()

# 6. feladat
# Generálj 10 véletlen számot 1 és 200 között, és számold meg, hány páros szám van.
darabszam = 0

for szamok in range (0, 10, 1):
    szam = r.randint(1, 200)
    print(szam, end=" ")
    if szam % 2 == 0:
        darabszam += 1
print()
print(darabszam, "Paros Szam Van")
print()
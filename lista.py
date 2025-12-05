"""
lista - dinamikus

tudunk bele uj elemet rakni, ezzel no az elemszama
-||- belole elemet elvenni -||- csokken -||-
modosithato barmelyik elem

deklaralas + inicializalas:
letrehozas + kezdoertek adas:

lista_neve = []

uj elem hozzaadasa:

lista_neve.remove(elem)

beegetett lista:

lista_neve = [3, 7, 6, 5, 4, 9, 1]

lista hossza:

len(lista_neve)
"""
szamok = [3,2,5,7,1]
szamok.append(12)
print(szamok)
szamok.remove(3)
print(szamok)
print("Hossz:", len(szamok))
print("Elso:", szamok[0])
print("Utso:", szamok[len(szamok)-1])


















#Szovegben van e betu
szoveg = input("adja meg a szoveget: ")
dube = input("keresett betu(k): ")
# if dube in szoveg:
#     print("benne van a(z)", dube)
# else:
#     print("nincsen benne a(z)", dube)

    #dupla betu keresese a szovegben

index = 0
while(index < len(szoveg)-1 and not (szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index += 1
if(index<len(szoveg) -1):
    print("benne van a(z)", dube)
else:
    print("nincsen benne a(z)", dube)


    #Palindrom Szoveg Kereses, Szokozkivonassal


mondat = input("Adja meg a szoveget: ")
uj = ""
for betu in mondat:
    if betu != " ":
        uj += betu

vissza = ""
for index1 in range(len(uj)-1, -1, -1):
    vissza += uj[index1]
if uj == vissza:
    print("a szoveg palindrom")
else:
    print("a szoveg nem palindrom")

    #Orai modszerrel

j = 0
while(j<len(mondat) / 2 and mondat[j] == szoveg[len(szoveg) -1 -j]):
    j += 1
if(j<len(szoveg)/2):
    print("A szoveg nem palindrom")
else:
    print("A szoveg palindrom")

    





"""
hazi feladat
tolts fel egy 13 elemu listat [0,20] kozotti veletlen szammal
szamok atlaga
hany db paros szam van a listaban
van e benne nulla
"""
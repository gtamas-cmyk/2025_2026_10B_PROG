# '''
# elotesztelos ciklus azaz a while ciklus, nem tudjuk hanyszor fog lefutni/ismetelni, feltetelhez kotott, akkor ismetel ha a feltetel igaz

# while(Feltetel):
#     Utasitasok (szekvencia)
# '''

# #generaljon veletlen szamokat {0 es 10 kozott}, amig nullast nem kapunk

# import random as r
# szamok = r.randint(0, 10)
# while(szamok != 0):
#     szamok = r.randint(0,10)
#     print(szamok, end=" ")
# print()

# # kerjen be szamokat addig amig nullat nem adnak meg
# # ADJA MEG A beir t szamok atlagat
# osszeg = 0
# db = 0
# keres = int(input("Adjon meg egy szamot: "))
# while keres != 0:
#     keres = int(input("Adjon meg megegy szamot: "))
#     db += 1
#     osszeg += keres
# print("Atlag:", osszeg/(db -1))


# #Adott egy szoveg. adja meg h van e benne x betu

szoveg = input("adja meg a szoveget: ")
x = "x"

if x.lower() in szoveg:
    print("Van X")
else:
    print("nincs x")


#hf feladatsor 29 ig minden
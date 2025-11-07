"""
Ciklusok - ismetles -loop

Szamlalos - For Ciklus
Vegigmegy a megadott elemeken vagy intervallumokon
for elem in range(mettol, meddig, hanyasaval):
    Ismetlendo folyamat

Tesztelos - While

for karakter in szoveg:
    Ismetlodo folyamat, szekvencia

"""
#1 - 10
for elem in range(1, 11, 1):
    print(elem, end=" ")
print()

#elso tiz paros szam 
for paros in range(0, 20, 2):
    print(paros, end=" ")
print()

#szoveg betui koze vesszot
szoveg = input("Adjon meg egy szöveget: ")
print(", ".join(szoveg))
print()


#hf feladatsorbol aaaaaaaaaaaaa
#14, 15, 16

#30tol 50ig 4gyel oszthato szamok

for negy in range(32, 51, 4):
    print(negy)
print()

for negy1 in range(30, 50, 4):
    print(negy1+2)
print()


for  index in range(0, len(szoveg)-1, 1):
    print (szoveg[index]+",",end="")
#print(szoveg[len(szoveg)-1])
print(szoveg[-1])
print()

# 10-tol 1 ig visszafele a szamokat
for tizegy in range(10, 0, -1):
    print(tizegy, end=" ")
print()

szovg = "kalapacs"

for indx in range(len(szovg)-1, -1, -1):
    print(szovg[indx],end=" ")
print()


# irass a ki a szoveget az helyevel tarsitvalvelvalavele (1k 2a 3l 4a 5p 6a 7c 8s ) eredeti szo kalapacs

ak1 = "kalapacs"
for hely in range(len(ak1)):
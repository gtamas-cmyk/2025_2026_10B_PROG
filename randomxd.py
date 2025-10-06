import random # random ban levo fuggvenyeket meghivjuk, hasznaljuk
import math # math ban levo fuggvenyeket hasznaljuk

a = random.randint(-5,5) *2 # -10 es 10 kozotti paros szam
eredeti = a # eredeti ertek megorzes

#abszolut ertek
if a < 0:
    a = a * -1
else:
    a = a

#gyok
if eredeti >= 0: 
    gyok = math.sqrt(eredeti)
else:
    gyok = "A negativ szamoknak nincs valos gyoke"
print("abs: " + str(a))
print("eredeti: " + str(eredeti))
print("gyok: " + str(gyok))

#pozitiv, negativ, nulla
if eredeti > 0:
    print("pozitiv")
elif eredeti < 0:
    print("negativ")
else:
    print("nulla")

#felhasznalotol bekeres

szoveg = input("Adj meg egy szamot: ")
print("A megadott szam: " + szoveg)

#HF a PDF-bol:
# 8-tol 13-ig feladatokat megoldani



#Szekvencia - utasitasok sorozata
#szelekcio - elagazas
#iteracio - ciklus, ismetles

#python compiler mobile
#python compiler online

#hf megoldasok

sec = 3923
# 1 ora 5 perc 23 masodperc
# 1*3600 + *5300 + 23 = 3923 sec

ora = sec // 3600
perc = (sec - ora * 3600) // 60
masodperc = sec % 60  
print(str(ora) + " ora " + str(perc) + " perc " + str(masodperc) + " masodperc")

#POTOLNIIIII A HF-T
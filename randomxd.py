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
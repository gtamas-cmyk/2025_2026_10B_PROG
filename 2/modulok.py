import math
import random

a = 2
gyoka = math.sqrt(a)
print("gyok(" + str(a) + ") =", gyoka)

felkerekit = math.ceil(gyoka)
print("felkerekit: ", felkerekit)
lekerekit = math.floor(gyoka)
print("lekerekit: ", lekerekit)
#felsoegeszresz alsoegeszresz
kerekites = round(gyoka,2)
print("kerekites: (2 tizedesre)", kerekites)
hatvanyozas1 = math.pow(gyoka, 2)
print("gyoka negyzete: ",hatvanyozas1)
alap = 2
kitevo = 5
#hatvanyozas2 = math.pow(alap,kitevo)
hatvanyozas2 = alap ** kitevo #2 ^ ugyanaz
print(alap,"^",kitevo,"=",hatvanyozas2)



#randomos cuc
vszam1 = random.randint(2,10)
print(vszam1)
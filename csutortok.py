import random

# """
# Fuggvenyek
# (Scratch blokkok)

# elore definialt (megirt, megfogalmazott) folyamatok, amik kulso ertektol fuggoen, vegrehajtjak a belso utasitasokat!

# def fuggvengyNev():
#     #fuggeveny tartalma

# fuggvenyNev() #fuggveny meghivasa
# """

# #visszateresi ertek nelkuli fuggvenyek - Eljaras
# #osszeadas fuggveny definialasa
# def osszeadas():
#     a = 12
#     b = 17
#     print(a+b)

# #osszeadas kulso ertektol fuggoen PARAMETEREN keresztul
# def osszeadasPARAM(a,b):
#     c = a + b
#     print(c)

# #osszeadas fuggveny meghivasa
# osszeadas()
# osszeadasPARAM(121, 18)

# #visszateressel rendelkezo fuggevenyek
# def kettoAtizediken():
#     #a = math.pow(2, 10)
#     a = 2**10
#     return a

# valtozo = kettoAtizediken()
# print(valtozo)

# def osszeadasVisszateressel(a,b):
#     c = a + b
#     return c
# print(round(osszeadasVisszateressel(33.5, 33.5)))
# print(osszeadasVisszateressel(6, 7))

# def veletlenszamKiiratas(db):
#     for i in range(0, db, 1):
#         print(random.randint(100,999), end=" ")
#     print()

# veletlenszamKiiratas(5)

# def szoVisszafele(szoveg):
#     for index in range(len(szoveg) -1, -1, -1):
#         print(szoveg[index], end="")
#     print()

# szoVisszafele("gejza kek azj eg")

# def szoVisszafele2(szoveg):
#     forditott = ""
#     for index in range(len(szoveg) -1, -1, -1):
#         forditott += szoveg[index]
#     return(forditott)
#     print()

# print(szoVisszafele2("fuggveny"))
 
#palindrom check fuggv es vissza adja valaszul

def palindrom(szo):
    i = 0
    while(i<=len(szo)//2 and szo[i] == szo[len(szo)-1-i] == szo[len(szo)-1-i]):
        i+=1
    if(i>len(szo)//2):
        return True
    else:
        return False
    print()
print("Palindrom-e a szo:", palindrom("geza kek az eg"))

# def palindromG(szo):
#     for i in range(0, len(szo), 1):
#         #mindegy

def listagen(db):
    lista = []
    for i in range(0, db, 1):
        lista.append(random.randint(-10,50))
    return(lista)
lista
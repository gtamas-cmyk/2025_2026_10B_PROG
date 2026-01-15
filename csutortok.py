"""
Fuggvenyek
(Scratch blokkok)

elore definialt (megirt, megfogalmazott) folyamatok, amik kulso ertektol fuggoen, vegrehajtjak a belso utasitasokat!

def fuggvengyNev():
    #fuggeveny tartalma

fuggvenyNev() #fuggveny meghivasa
"""

#visszateresi ertek nelkuli fuggvenyek - Eljaras
#osszeadas fuggveny definialasa
def osszeadas():
    a = 12
    b = 17
    print(a+b)

#osszeadas kulso ertektol fuggoen PARAMETEREN keresztul
def osszeadasPARAM(a,b):
    c = a + b
    print(c)

#osszeadas fuggveny meghivasa
osszeadas()
osszeadasPARAM(121, 18)

#visszateressel rendelkezo fuggevenyek
def kettoAtizediken():
    #a = math.pow(2, 10)
    a = 2**10
    return a

valtozo = kettoAtizediken()
print(valtozo)

def osszeadasVisszateressel(a,b):
    c = a + b
    return c
print(round(osszeadasVisszateressel(33.5, 33.5)))
print(osszeadasVisszateressel(6, 7))
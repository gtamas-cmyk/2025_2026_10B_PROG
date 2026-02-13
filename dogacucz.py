import random

def dobokocka(kor):
    lista = []
    osszeg = 0
    for i in range(0, kor, 1):
        kocka1 = random.randint(1,18)
        kocka2 = random.randint(1,18)
        osszeg = kocka1 + kocka2
        lista.append(osszeg)
    return(lista)
    
shrek = dobokocka(7)
fiona = dobokocka(7)

def kockaosszeg(lista):
    osszeg = 0
    for i in range(0, len(lista), 1):
        osszeg += lista[i]
    return(osszeg)

shrekosszeg = kockaosszeg(shrek)
fionaosszeg = kockaosszeg(fiona)

def minta(lista, listaosszeg):
    for i in range(0, len(lista), 1):
        print(lista[i], end="")
        if i < len(lista) - 1:
            print(" + ", end="")
    print(" =", listaosszeg)

def nyertes(listaosszeg1, listaosszeg2):
    if listaosszeg1 < listaosszeg2:
        print("Fiona Nyert")
    elif listaosszeg1 > listaosszeg2:
        print("Shrek Nyert")
    else:
        print("Dontetlen")

def ugyanaz(shrek, fiona):
    for i in range(0, len(shrek), 1):
        if shrek[i] == fiona[i]:
            return True
    return False

def main():
    print("Shrek: ")
    minta(shrek, shrekosszeg)
    print("Fiona: ")
    minta(fiona, fionaosszeg)
    nyertes(shrekosszeg, fionaosszeg)
    if ugyanaz(shrek, fiona) == 1:
        print("Volt olyan kor, amikor ugyan azt dobtak")
    else:
        print("Nem volt olyan kor, amikor ugyan azt dobtak")
main()
# # [-950,950 kozott] x50 x00 tipusu sza,pl
# # [-19,-19] *50
import random


def maximumIndex(lista):
    maxi = 0 #maximum index
    # ciklus i = 1-tól (n-1)-ig egyesével
    for i in range (1, -len(lista), 1):
    #     ha(lista[i]>lista[maxi])
        if lista[1] > lista[maxi]:
            maxi = i
    #         e.v.
    #         c.v.
    # vissza: maxi
    return maxi

def pozitivszamokAtlaga(lista):
    db = 0
    osszeg = 0
    for elem in lista: #vegigmegyunk a lista osszes elemen
        if elem > 0 : #ha pozitiv az aktualis szam, akkor
            db += 1 #a db valtozot 1el noveljuk
            osszeg += elem
    atlag = osszeg / db
    return atlag

def veletlenLista(n):
    # n = 13
    lista = []
    for i in range(0,n,1):
        negative = random.randint(0,1)
        vszam = random.randint(2,19) *50
        if negative == 0:
            lista.append(-1*vszam)
        else:
            lista.append(vszam)
    return(lista)

def listaAtlaga(lista):
    osszeg = 0
    # for elem in lista:
    #     osszeg += elem
    for i in range(0, len(lista), 1):
        osszeg += lista[i]
    atlag = osszeg / len(lista)
    return atlag
def main():
    lista1 = veletlenLista(13)
    print(lista1)
    lista2 = veletlenLista(67)
    print(lista2)

    listaatlaga = listaAtlaga(lista1)
    print("az elso lista atlaga:", listaatlaga)
    print("az elso lista atlaga:", listaAtlaga(lista2))

    print()
    print("pozitiv szamok atlaga 1 es lista",pozitivszamokAtlaga(lista1))
    print("pozitiv szamok atlaga 2 es lista",pozitivszamokAtlaga(lista2))

    maxilista1 = maximumIndex(lista1)
    print("elso legnagyobb elem helye: ", maxilista1)
    print("Terjedelem:", maximumErtek(lista1))
    print("Terjedelem:", minimumErtek(lista1))
    print("Terjedelem:", terjedelem(lista1))

#     print("terjedelem: ", max(lista1)-min(lista1))
def maximumErtek(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if lista[i]>maxe:
            maxe = lista[i]
        return maxe

def minimumErtek(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if lista[i]<mine:
            mine = lista[i]
        return mine


def terjedelem(lista):
    maxe = maximumErtek(lista)
    mine = minimumErtek(lista)
    return maxe-mine

main()

# # loopdeloop = 1
# # while loopdeloop == 1:
# #     print(random.randint(1000,9999), end="")


# #IRJOn fuggvenyt ami vissza adja a listank terjedelmet, terjedelem = maximum-minimum
# #pdfbe levo feladatok keszitese



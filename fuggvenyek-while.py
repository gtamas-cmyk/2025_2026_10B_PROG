#Hazi feladat
#Jancsi es juliska elmennek minden nap gombat gyujteni. 14 napig folyamatosan gyujtik majd osszevetik az adatokat.
#Szimulald a gyujtest. kosarak nagysaga [2,9] kozotti lebegopontos (tort szam, 2 tizedes jegy pontossaggal.)
#Fent van a foly a tanarur gitjen

def vaneKetjegyuListaban(lista):
    i = 0
    # ciklus amíg (i<hossz(lista) és NEM Ttul(lista[i]))
    while (i < len(lista) and not (lista[i] >= 10 and lista[i] < 99)):
            i+=1
        # c.v.
    vane = i < hossz(lista)
    # vissza: vane
    return vane



def main():
    szamok = [2, 5, 7, 3, 7, 11, 9, 1, 2]
    print(szamok)
    #van-e ketjegyu szam a listaban?
    vaneKetjegyu = vaneKetjegyuListaban(lista)
    print(vaneKetjegyu)

main()
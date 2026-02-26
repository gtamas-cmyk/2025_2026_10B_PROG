# Hf - szeleromu.txt
    # telepules, vármegye, tájolás, hány darab szélerőmű, szélerőművenkénti teljesítmény kw/h, mikor telepítették
    # Magyarországon hány szélerőmű van?
    # Írjuk ki, hogy melyik településen és melyik évben telepítették a legtöbb szélerőművet
    # Kérjünk be egy települést! Nézzük meg, hogy van-e ott szélerőmű (pl.: Cegléd: nincs)

def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(';')
        lista.append((st[0],st[1],st[2],int(st[3]), int(st[4]), int(st[5])))
    return lista

def szeleromumvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][3]
    return osszeg

def maxindexDB(lista):
    maxi = 0
    for i in range(len(lista)):
        if(lista[i][3]>lista[maxi][3]):
            maxi = i
    return maxi

def vaneSzeleromu(lista, varos):
    i = 0
    while i < len(lista) and lista[i][0] != varos:
        i += 1
    vane = i < len(lista)
    return vane

def main():
    t = adatokBeolvasasa()
    #print(t)

    db = szeleromumvekDarab(t)
    print(db, "db eromu van Mo-n")

    maxindex = maxindexDB(t)
    print(t[maxindex][0], "varosban", t[maxindex][5], "eveben csinaltak egyszerre a legtobb eromuvet")


    varos = input("adjon meg egy varost: ")
    vane = vaneSzeleromu(t, varos)
    if vane:
        print("ebben a varosban van")
    else:
        print("nincs")

    # 2013 május digit kult emelt prog
    # szavazatok.txt
    # http://informatika.fazekas.hu/erettsegi/emelt-szintu-feladatok/
main()

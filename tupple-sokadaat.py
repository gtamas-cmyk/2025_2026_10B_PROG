def listaFeltoltes():
    db = int(input())
    t = []
    for i in range(db):
        sor = input() #alma 12 500
        st = sor.split(" ") #seged lista ["alma", "12", "500"]
        tupe = (st[0],int(st[1]), int(st[2]))
        t.append(tupe)
    return t

adatok = listaFeltoltes()

#irjo egy fuggvenyt ami visszaadja az osszetett szerkezetbol hogy osszesen hany mazsa gyumolcs van

def mazsa(adatok):
    osszesen = 0
    for adat in adatok:
        osszesen += adat[1]
    return osszesen

#irjon egy fuggvenyt ami visszaadja a parameterben megadott ertekrol nagyobb osszeggel rendelkezo gyumolcsok darabszamat
def legnagyobbAr(adatok):
    legnagyobb = 0
    for adat in adatok:
        if(adat[2] > legnagyobb):
            legnagyobb = adat[2]
    return legnagyobb


def hanyArNagyobb(adatok, ar):
    db = 0
    for i in range(0, len(adatok), 1):
        if(adatok[i][2] > ar):
            db += 1
    return db

def main():
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    print(mazsa(adatok))
    print(legnagyobbAr(adatok))
    print(hanyArNagyobb(adatok, 100))


main()
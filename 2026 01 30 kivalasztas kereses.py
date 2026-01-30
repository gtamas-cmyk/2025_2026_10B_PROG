#kerjen be egy szamot a felhasznalotol [10,20] kozott ugy h ha rossz erteket adott meg ismetelhje meg a bekerest
import random
def szamBekeres():
    szam = int(input("Adjon meg egy szamot 10 es 20 kozott: "))
    while szam < 10 or szam > 20:
            szam = int(input("Hibas szam, Probalja Ujra: "))
    return szam

def listasFuggveny(n):
    lista = []
    szam = random.randint(10,99)
    for i in range(0, n, 1):
        szam = random.randint(10,99)
        if szam % 4 == 1:
            szam += 1
        lista.append(szam)
    return lista

def kereses(lista):
    i = 0
    while(i < len(lista) and not lista[i] % 10 != 7):
        i+=1
    vane = i < len(lista)
    if vane: return i
    else: return -1

def main():
    db = szamBekeres()
    szamokLista = listasFuggveny(db)
    print("A Bekert szam:", db)
    print("Lista:", szamokLista)
    index = kereses(szamokLista)
    if index == -1:
        print("nincs 7tel oszthato")
    else:
        print("van 7tel oszthato az,", index+1, "helyen")
main()

#keszits egy listat ami feltolti a francia kartya lapjaival T mint Tref K min Karo S mint sziv P min pikk, T1 T2 ... T13, K1, K2 ... K13
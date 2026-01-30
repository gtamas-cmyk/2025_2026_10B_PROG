import random

def listaFeltolt(n):
    lista = []
    for i in range(0, n, 1):
        lista.append(random.randint(200, 900) / 100)
        #lista.append(round(random.random()*7+2, 2)) # [0, 1] * (9-2) + 2
    return lista

def vaneSzamnalNagyobb(szam, lista):
    index = 0
    while (index < len(lista) and lista[index] <= szam):
    #Ttul: lista[index] > szam NEM Ttul: lista[index] <= szam
        index += 1
    vane = index < len(lista)
    return vane
    # ha index < len(lista) akkor vane erteke true
    # kulonben (index >= len(lista)) akkor vane erteke false

def vaneKetszamKozott(a, b, lista):
    index = 0
    #while (index < len(lista) and (lista[index] < a or lista[index] < b)):    
    while (index < len(lista) and not (lista[index] >= a and lista[index] <= b)):
        # Ttul: lista[index] >= a and lista[index] >= b 
        index += 1
    vane = index < len(lista)
    return vane

def main():
    jancsi = []
    juliska = []
    #db = int(input())
    #db = random.random(12, 96)
    #print(listaFeltolt(14))
    jancsi = listaFeltolt(14)
    juliska = listaFeltolt(14)
    print("Juliska: ", juliska)
    print("Jancsi: ", jancsi)


    vaneJuliska = vaneSzamnalNagyobb(8.5, juliska)

    if(vaneJuliska):
        print("Van Juliskanal 8.5-nel nagyobb")
    else:
        print("Nincs Juliskanal 8.5-nel nagyobb")

    vaneJancsi = vaneSzamnalNagyobb(8.5, jancsi)

    if(vaneJancsi):
        print("Van Jancsinal 8.5-nel nagyobb")
    else:
        print("Nincs Jancsinal 8.5-nel nagyobb")


    vaneJuliskaKozott = vaneKetszamKozott(4.9, 5.1, juliska)

    if(vaneJuliskaKozott):
        print("Juliskanak van 4.9 es 5.1 kozotti erteke")
    else:
        print("Juliskanak nincs 4.9 es 5.1 kozotti erteke")
    
        vaneJancsiKozott = vaneKetszamKozott(4.9, 5.1, jancsi)

    if(vaneJancsiKozott):
        print("Jancsinak van 4.9 es 5.1 kozotti erteke")
    else:
        print("Jancsinak nincs 4.9 es 5.1 kozotti erteke")





        
main()
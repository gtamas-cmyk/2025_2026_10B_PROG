# # a = 23
# # b = "alma"
# # c = True

# # t = [a, b, c, ["k1", "k2"]]
# # t[0]
# def eredmeny(atlag, honapok):
#     maxe = atlag[0]
#     for i in range(1, len(atlag)-1, 1):
#         if(atlag[i] > maxe):
#             maxe = atlag[i]
#     return(honapok[i])

# def maxIndex2(szamok, honapok):
#     maxi = 0
#     honap = honapok[0]
#     for i in range (0,len(szamok),1):
#         if(szamok[i]>szamok[maxi]):
#             maxi = i
#             honap = honapok[i]
#     return(honap,maxi, szamok[maxi])

def main():
#     honapok = ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
#     Jani = [4.0, 3.8, 4.2, 4.1, 3.8, 4.2, 3.0, 3.6, 4.2, 4.1, 4.7, 4.2]
#     print(eredmeny(Jani, honapok))
#     print(maxIndex2(Jani, honapok))
#     # tordelt = szoveg.split(" ")
#     # print(tordelt)
#     # print(2026-int(tordelt[i]))
#     print()
#     szoveg = "2026.02.19 3 Programozaas"
#     szovegtordel = szoveg.split(" ")
#     datum = szovegtordel[0].split(".")

#     print(szovegtordel)
#     print(datum[1])
#     #2026. 02. 19
#     #2 - februar

#     #ABC - 123, Kis Pista, KJ567654345678987, 1992.03.10
#     #Ev?
#     #Vezeteknev

    auto = "ABC - 123, Kis Pista, KJ567654345678987, 1992.03.10"
    tor3 = auto.split(", ")
    datum = tor3[3].split(".")
    nev = tor3[1].split(" ")
    print(nev[0], datum[0])

    #hf rendszamot egybe
    #ABC123, Kis Pista, KJ-567654345678987, 1992_03_10
    #rendszam utolso 3 szama
    #keresztnev
    #honap

    #"Nagy bela:2026_02_19 - 12:13:20"
    #nap
    #ora
    #keresztnev
    
    main()
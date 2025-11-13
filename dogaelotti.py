# 1. Adottak a téglalap alapélei. Írassa ki az oldalakat és a kerületet, területet!

# tegla = int(input("Adja meg az A oldalt: "))
# teglb = int(input("Adja meg a B oldalt: "))


# print("A:", tegla, "B:", teglb)
# if tegla > teglb:
#     print("A oldal hosszabb")
# elif tegla < teglb:
#     print("B oldal hosszabb")
# else:
#     print("Egyenloen hosszu mindketto oldal")

# print("Terulet:" ,tegla * teglb)
# print("Kerulet:", 2 * (tegla + teglb))

# 20. Kérj be a felhasználótól egy szöveget, majd írasd ki a szöveget szóközök nélkül!

# szoveg0 = str(input("Adjon meg egy szoveget: "))
# szokoznelkul = szoveg0.replace(" ", "")
# print(szokoznelkul)

szo = "kalapacs"
n = len(szo)
forditott = ""

for index in range(n -1, -1, -1):
    forditott += szo[index]
    print(forditott)
print()

for betu in szo:
    print(betu)
print()
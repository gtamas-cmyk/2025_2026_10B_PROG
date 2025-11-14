#22. Adott egy szöveg. Szóközteleníts! Nézd meg, hogy palindrom-e! "géza kék az ég"

mondat = "geza kek az eg"
uj = ""
szokoz = " "
forditott = ""

#szokoztelenites

for betu in mondat:
    if betu != szokoz:
        uj += betu
print(uj)

# szoveg megforditasa, palindrom check

n = len(uj)

for index in range(n -1, -1, -1):
    forditott += uj[index]

if forditott == uj:
    print("A szoveg palindrom")
else:
    print("A szoveg nem palindrom")

# 23. Adott egy szöveg. Mondd meg, hogy hány szóból áll?
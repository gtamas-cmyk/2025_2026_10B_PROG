# 14. Írasd ki egy bekért szó utolsó karakterét
szo = input("Adj meg egy szót: ")
if len(szo) > 0:
    print("Utolsó karakter:", szo[-1])
else:
    print("Nem adtál meg szót.")

# 15. Írassa ki, hogy az adott szó első és utolsó karaktere egyezik-e?
if len(szo) > 0:
    if szo[0] == szo[-1]:
        print("Az első és utolsó karakter egyezik.")
    else:
        print("Az első és utolsó karakter nem egyezik.")
else:
    print("Nem adtál meg szót.")

# 16. Írassuk ki egy bekért szöveg minden második betűjét
szoveg = input("Adj meg egy szöveget: ")
print("Minden második betű:", szoveg[1::2])

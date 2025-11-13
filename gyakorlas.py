#forditsd meg a szoveget
szoveg = input("hallo:")
n = len(szoveg)
forditott = ""
for index in range(n -1, -1, -1):
    forditott += szoveg[index]
print(forditott)

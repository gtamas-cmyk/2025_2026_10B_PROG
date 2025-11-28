user = str(input("Adjon meg egy szoveget: "))
index = 0
while (index < len(user)-1 and not (user[index] != "c") and (user[index+1] != "s")):
    index += 1
if (index < len(user)-1):
    print("van benne cs")
else:
    print("nincs benne cs")
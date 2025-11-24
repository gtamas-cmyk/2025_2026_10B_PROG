import random as r
#mesterremekem frfr
szam = r.randint(10,99)
print("Gondoltam egy ketjegyu szamra")
user = 0
db = 1
#print(szam) # Debug
while user != szam:
    user = int(input(str(db) + ". " + "Melyik szamra gondoltam? : "))
    if szam < user:
        print("A kigondolt szam kissebb")
        db += 1
    elif szam > user:
        print("A kigondolt szam nagyobb")
        db += 1
    else:
        print("Helyes, a szam:", szam, "volt, es a probalkozasaid szama:", db, "db")
    if user < 10 or user > 99:
        db -= 1
# 8. Segítsd az osztályfőnök munkáját a bizonyítvány íráshoz! Ha az érdemjegy 1,2,3,4,5 - írassa ki
# szövegesen: 1-elégtelen, 2-elégséges, 3-közepes, 4-jó, 5-jeles. Felhasználó adja meg az
# érdemjegyet!
# 9. Megvan adva a víz hőfoka. Írassa ki, a hőfok alapján hogy szilárd, folyékony, gáz
# halmazállapotú!
# 10. Háromszög egyenlőtlenség. Adva van három oldal hossza. Adja meg, hogy szerkeszthető-e a
# háromszög! HE - akkor szerkeszthető egy háromszög, ha bármely két oldal összege, nagyobb
# a harmadiknál.
# 11. Adott a hőmérséklet farenheitben. Számolja át cfokba!
# 12. Adott a hőmérséklet cfokban. Számolja át farenheitbe!
# 13. Kérjen be a felhasználótól egy időtávot másodpercben. Számolja át órára, percre,
# másodpercre!

# 8. Bizonyitvany
jegy = int(input("Add meg a jegyet (1-5): "))
if jegy == 1:
    print("Elegtelen")
elif jegy == 2:
    print("Elegseges")
elif jegy == 3:
    print("Kozepes")
elif jegy == 4:
    print("Jo")
elif jegy == 5:
    print("Jeles")
else:
    print("Ez nem 1-5 halo")

# 9. Viz
ho = float(input("\nAdd meg a víz hőmérsékletét (°C): "))
if ho <= 0:
    print("Jeg")
elif ho < 100:
    print("Viz, folyekony")
else:
    print("Goz")

# 10. Haromszog 
a = float(input("\nAdd meg az első oldal hosszát: "))
b = float(input("Add meg a második oldal hosszát: "))
c = float(input("Add meg a harmadik oldal hosszát: "))

if a + b > c and a + c > b and b + c > a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")

# 11. Fahrenheitbol Celsius
fahrenheit = float(input("\nAdd meg a hőmérsékletet Fahrenheitben: "))
celsius = (fahrenheit - 32) * 5/9
print(f"A hőmérséklet Celsiusban: {celsius:.2f} °C")

# 12. Celsiusbol Fahrenheit
celsius2 = float(input("\nAdd meg a hőmérsékletet Celsiusban: "))
fahrenheit2 = (celsius2 * 9/5) + 32
print(f"A hőmérséklet Fahrenheitben: {fahrenheit2:.2f} °F")

# 13. Mpbol ora perc mp
seconds = int(input("\nAdj meg egy időt másodpercben: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print(f"{seconds} másodperc = {hours} óra, {minutes} perc, {secs} másodperc")

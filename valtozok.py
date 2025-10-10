from datetime import datetime
var = "Ez az elso valtozom hihihiha"
print(var)
#matematik
nev = input("Mi a Neved? ")
osztaly = input("Hanyadikos vagy? ")
dnow = datetime.now()
formatted_date = dnow.strftime("%Y. %m. %d.")
print (f"Szia {nev}", osztaly, formatted_date, sep="\n")
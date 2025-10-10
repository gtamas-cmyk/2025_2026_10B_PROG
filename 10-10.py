#generaljon ki harom veletlen haromjegyu szamot, amelyek 13-al oszthatoak
#allitssa ezeket sorrendbe
#adja meg az atlagukat
#van e kozottuk 4-el vegzodo?
import random
a = random.randint(100,999) #Megkell csinalni a 13-mal oszthatosagot
b = random.randint(100,999)
c = random.randint(100,999)

szamok = [a, b, c]
szamok.sort
print(szamok)

atlag = (a+b+c)//3
print("Atlag:", atlag)
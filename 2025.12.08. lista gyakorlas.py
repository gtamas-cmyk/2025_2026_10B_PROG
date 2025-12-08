#hf
import random
lista = []
for _ in range(13):
    lista.append(random.randint(0,20))

print(lista)

#szamok atlaga
osszeg = 0
db = 0
for index in range(0, len(lista), 1):
    osszeg += lista[index]
    db += 1 
print(osszeg / db)
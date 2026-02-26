t = [("alma", 5, 300),("korte", 6, 500),("meggy", 4, 1100)]
# t [sor index] [oszlop index]

# print(t[0][0]) #> alma
# print(t[0][1]) #> 5
# print(t[0][2]) #> 300
# print()
# print(t[1][0]) #> korte
# print(t[1][1]) #> 6
# print(t[1][2]) #> 500
# print()
# print(t[2][0]) #> meggy
# print(t[2][1]) #> 4
# print(t[2][2]) #> 1100
# print()

# for i in range(0, len(t), 1):
#     print(t[i][2])

def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(';')
        lista.append((st[0], st[1], st[2], int(st[3]), int(st[4]), int(st[5])))
    return lista

def szeleromuvekDarab(lista):
    osszeg = 0
    for i in range(0, len(lista), 1):
        osszeg += lista[i][3]
    return osszeg
def main():
    t = adatokBeolvasasa()
    # print(t)

    db = szeleromuvekDarab(t)
    print(db)
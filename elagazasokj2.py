import math
# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

# szam = int(input("Adjon meg egy egész számot:"))
# if(szam % 2 == 0):
#     print("páros")
# else:
#     print("páratlan")

#kerjen be a felhazsnalotol egy szamot  es mondja meg h 10zel oszthato e, ha nem akk irja ki az ultoso szamjegyet
#pl be 10 ki tizzel oszthato
#pl be 12 ki tisszel nem oszthato, utso szamjegy 2

a = int(input("adj meg egy szamot: "))
if(a % 10 == 0):
    print("tizzel nem oszthato, utolso szamjegy: " + str(a % 10))
else:
    print("tizzel oszthato")

# kerjen be egy  masik szamot es irassaki a ket szam reciprokanak oszzeget

# b = int(input("adjon meg egy masik szamot: "))
# if (a == 0 or b == 0):
#     print("Nullaval nem osztunk te buta")
# else:
#     rec = 1/a
#     rec2 = 1/b
#     print(rec+rec2)
b = int(input("adjon meg egy masik szamot: "))
if (a != 0):
    if(b != 0):
        rec = 1/a
        rec2 = 1/b
        print(rec+rec2)
    else:
        print("a masodik szamnak nincs reciproka")
else:
    print("az elso szamnak nincs reciproka")

# adja meg a ket szaam osszegenek gyoket

gyok = a+b
if (gyok >= 0):
    
    print("ket szam gyoke " + str(math.sqrt(gyok)))
else:
    print("ribarik nemjol szamol")

#logikai operatorok
#and, or, xor, not

#bool algebra (HF)

# A | B | A and B | A or B
# T | T |    T    |   T
# T | F |    F    |   T
# F | T |    F    |   T
# F | F |    F    |   F

#hf kerjen be a felhasznalotol 3 db szamot lehet tort is. ez a harom szam egy haromszog harom oldala
#1 derekszogu e a  haromszog?
#2 egyenlo szaru e a haromszog
#3 szabalyos e a haromszog
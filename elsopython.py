import random
from datetime import datetime

ascii_art = """                     
   ,---,                               
,`--.' |              .--.,            
|   :  :      ,---, ,--.'  \   ,---.   
:   |  '  ,-+-. /  ||  | /\/  '   ,'\  
|   :  | ,--.'|'   |:  : :   /   /   | 
'   '  ;|   |  ,"' |:  | |-,.   ; ,. : 
|   |  ||   | /  | ||  : :/|'   | |: : 
'   :  ;|   | |  | ||  |  .''   | .; : 
|   |  '|   | |  |/ '  : '  |   :    | 
'   :  ||   | |--'  |  | |   \   \  /  
;   |.' |   |/      |  : \    `----'   
'---'   '---'       |  |,'             
                    `--'               
"""
print(ascii_art)

# # Egy soros komment
# """
# Tobb
# soros
# Komment
# """

# # kod kod
# # kod kod
# # kod kod
# # kod hibakod
# # Ctrl + Ü
# # Ctrl + /
# \n uj sort kezd
print("hello world!") #<---- python expert
szam = random.randint(1000,9999) #random 4 jegyu szam
szam2 = random.randint(100,999) #random 3 jegyu szam
szamok = szam,szam2
print(szamok)
print()
dnow = datetime.now()
formatted_date = dnow.strftime("%Y. %m. %d.")
print("Geréb Tamás")
print("10.b")
print(formatted_date)
print("egyik szoveg", "masik szoveg", "", end="*=*")
print("\nharmadik szoveg", "negyedik szoveg", "", end="\n*=*")
print("\nalma", "Szilva", "Korte", "Labda", sep="---")
print()
print("*", "**", "***", "****", "*****", sep="\n")
print()
print("*")
print("**")
print("***")
print("****")
print("*****")

# Div egeszresz, mod modulus (maradek)
#div - //
#mod - %
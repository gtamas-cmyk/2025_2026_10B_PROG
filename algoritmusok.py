#irjon fuggvenyt ami fugg egy egesz szamtol es megadja h prim v nem prim!
#irjon fuggvenyt ami megmondja ket pozitiv egesz szamrrol a Legnagyobb kozos osztojat

def prime(szam):
    for i in range(2, szam, 1):
        if szam % i == 0:
            return("Nem Prim")
        return("Prim")

def lnko(szam1, szam2):
    for i in range

def main():
    a = 13
    b = 26
    print(prime(a)) # a=13 true
    # print(lnko(a,b)) #a=13, b=26 LNKO=13

main()
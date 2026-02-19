import math


def prime(szam):
    a = 2
    while(a<szam/2 and szam % a != 0):
        a += 1
    return a >= math.sqrt(szam)

def LNKO(szam1,szam2):
    if a == b:
        return a
    if b < a:
        c = a
        a = b
        b = c
    while (0 < a):
        a, b = b % a, a
    return b
 

def main():
    a = 131
    b = 26
    # for i in range(2, 100000, 1):
    #     if prime(i):
    #         print(i)
    print(prime(a)) #a=13 true
    print(LNKO(a,b)) #a=13 b=26 LNKO=13
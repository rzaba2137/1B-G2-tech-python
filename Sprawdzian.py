from math import gcd
licz1 = int(input())
mian1 = int(input())
licz2 = int(input())
mian2 = int(input())
wspolny = mian1 * mian2 / gcd(mian1,mian2)
licznik = (wspolny/mian1) * licz1 + (wspolny/mian2) * licz2
print(str(licznik) + "/" + str(wspolny))
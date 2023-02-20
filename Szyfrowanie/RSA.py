#pre
# from math import gcd
# print(gcd(15,20))

#1 wybór dwóch dużych liczb pierwszych
p = 101
q = 97

#2 liczymy n = p*q oraz funkcje Eulera F = (p-1) * (q-1)
n = p * q
F = (p-1) * (q-1)
print(n)
print(F)

#3 generujemy klucz publiczny e taki, że NWD(F,e) = 1
from math import gcd
for i in range(2, F):
    if gcd(i, F) == 1:
        e = i
        break
print(e, n)

#4 generujemy klucz prywatny d taki, że d*e mod F = 1
for j in range(2, F):
    if ((j * e) % F) == 1:
        d = j
        break
print(d,n)

#jak szyfrować
# mamy n - wiadomość
# c = m**e % n (c - cipher - szyfogram, tekst zaszyfrowany)
# t = c**d % n (t - text - tekst jawny - znów wiadomość n)
m = input()
cipher = ""
for i in m:
    cipher += (chr((ord(i)**e)%n))   

print(m)
print(cipher)

tekst =""
for i in cipher:
    tekst += chr((ord(i)**d)%n)
print(tekst)


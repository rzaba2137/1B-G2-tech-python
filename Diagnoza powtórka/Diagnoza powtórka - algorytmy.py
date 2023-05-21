#ALGORYTMY

#zad 1
#Sprawdź czy wpisana przez usera liczba jest pierwsza

import math

def czy_liczba_pierwsza(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

wprowadzona_liczba = int(input("Wprowadź liczbę: "))
if czy_liczba_pierwsza(wprowadzona_liczba):
    print("Podana liczba jest liczbą pierwszą.")
else:
    print("Podana liczba nie jest liczbą pierwszą.")

#zad 2
#Sprawdź czy wpisana przez usera liczba jest złożona

import math

def czy_liczba_zlozona(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True

    return False

wprowadzona_liczba = int(input("Wprowadź liczbę: "))
if czy_liczba_zlozona(wprowadzona_liczba):
    print("Podana liczba jest liczbą złożoną.")
else:
    print("Podana liczba jest liczbą pierwszą.")

#zad 3
#Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24

def czy_wzglednie_pierwsza_z_24(liczba):
    if liczba == 1:
        return False

    dzielniki_wspolne = [2, 3, 4, 6, 8, 12]
    for dzielnik in dzielniki_wspolne:
        if liczba % dzielnik == 0:
            return False

    return True

wprowadzona_liczba = int(input("Wprowadź liczbę: "))
if czy_wzglednie_pierwsza_z_24(wprowadzona_liczba):
    print("Podana liczba jest względnie pierwsza z 24.")
else:
    print("Podana liczba nie jest względnie pierwsza z 24.")

#zad 4
#Zakoduj szyfrem cezara i kluczem k słowo s

def szyfr_cezara(slowo, klucz):
    zaszyfrowane_slowo = ""
    for litera in slowo:
        
        if litera.isupper():
            pozycja = ord(litera) - ord('A')
            nowa_pozycja = (pozycja + klucz) % 26
            nowa_litera = chr(nowa_pozycja + ord('A'))
            zaszyfrowane_slowo += nowa_litera
        
        elif litera.islower():
            pozycja = ord(litera) - ord('a')
            nowa_pozycja = (pozycja + klucz) % 26
            nowa_litera = chr(nowa_pozycja + ord('a'))
            zaszyfrowane_slowo += nowa_litera
        
        else:
            zaszyfrowane_slowo += litera

    return zaszyfrowane_slowo

slowo = input("Wprowadź słowo: ")
klucz = int(input("Wprowadź klucz k: "))
zaszyfrowane_slowo = szyfr_cezara(slowo, klucz)
print("Zaszyfrowane słowo:", zaszyfrowane_slowo)

#zad 5
#Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną

def znajdz_najwiekszy_wspolny_dzielnik(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def dodaj_ulamki(a, b, c, d):
    wspolny_mianownik = b * d
    licznik = a * d + c * b

    najwiekszy_wspolny_dzielnik = znajdz_najwiekszy_wspolny_dzielnik(licznik, wspolny_mianownik)

    skrocony_licznik = licznik // najwiekszy_wspolny_dzielnik
    skrocony_mianownik = wspolny_mianownik // najwiekszy_wspolny_dzielnik

    liczba_mieszana = skrocony_licznik // skrocony_mianownik
    reszta = skrocony_licznik % skrocony_mianownik

    return skrocony_licznik, skrocony_mianownik, liczba_mieszana, reszta

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
d = int(input("Podaj d: "))

skrocony_licznik, skrocony_mianownik, liczba_mieszana, reszta = dodaj_ulamki(a, b, c, d)

if liczba_mieszana == 0:
    print("Suma ułamków:", skrocony_licznik, "/", skrocony_mianownik)
else:
    print("Suma ułamków:", liczba_mieszana, "i", reszta, "/", skrocony_mianownik)

#zad 6
#Znajdź NWW dwóch wpisanych przez usera liczb 

def znajdz_nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def znajdz_nww(a, b):
    nwd = znajdz_nwd(a, b)
    nww = (a * b) // nwd
    return nww

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

nww = znajdz_nww(a, b)
print("Najmniejsza wspólna wielokrotność (NWW) liczb", a, "i", b, "to:", nww)
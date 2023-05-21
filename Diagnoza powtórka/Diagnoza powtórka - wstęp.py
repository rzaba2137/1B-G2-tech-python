#WSTĘP

#zad 1 
#Oblicz sumę liczb 3 cyfrowych

suma = (100 + 999) * 900 // 2
print(suma)

#zad 2
#Oblicz sumę i ilosć dwucyfrowych wielokrotności liczy 6

suma = 0
licznik = 0
for i in range(10, 100):
    if i % 6 == 0:
        suma += i
        licznik += 1
print("Suma:", suma)
print("Ilość:", licznik)

#zad 3 
#Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4 - cyfrowych 

import random
liczby = []
for i in range(5):
    liczby.append(random.randint(1000, 9999))

print("Wylosowane liczby:", liczby)
print("Najwięszka liczba:", max(liczby))

#zad 4
#Podaj sumę cyfr w dowolnej liczbie

liczba = 12345
suma_cyfr = 0
for cyfra in str(liczba):
    suma_cyfr += int(cyfra)
print("Suma cyfr w liczbie", liczba, "to", suma_cyfr)

#zad 5
#Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3 - cyfrowej

liczba = int(input("Podaj liczbę trzycyfrową: "))

cyfra_setek = liczba // 100
cyfra_dziesiatek = (liczba // 10) % 10
cyfra_jednosci = liczba % 10

najmniejsza_cyfra = cyfra_setek

if cyfra_dziesiatek < najmniejsza_cyfra: najmniejsza_cyfra = cyfra_dziesiatek

if cyfra_jednosci < najmniejsza_cyfra: najmniejsza_cyfra = cyfra_jednosci

print("Najmniejsza cyfra w liczbie", liczba, "to", najmniejsza_cyfra)
while True:
    n = int(input())
licznik = 0
for i in range(2, n):
    if n % i == 0:
        licznik += 1

if licznik == 0:
    print("Liczba jest pierwsza ")
else:
    print("Liczba nie jest pierwsza")
znak = input("Chcesz kolejną liczbę T/N")
if znak == 'N':
    break

#zad1
# a, b, c = int(input()), int(input()), int(input())
# suma = 0
# print(ord("a"))
# print(ord("b"))
# print(ord("c"))

#zad3
# for i in range(99, 9, -1):
#     if i & 7 == 0:
#         podzielnik = i
#         break
# ilosc = 0
# for i in range(1000, 10000):
#     if i % podzielnik == 0:
#         ilosc +- 1
# print(ilosc)

#zad4
# ilosc = 0
# for i in range(10,100):
#     cd = i // 10
#     cj = i % 10
#     if cd >= 2*cj:
#         ilosc = ilosc + 1

#zad5
# print((456 // 10) % 10)

#zad6
#opcja1
# n = int(input())
# licznik = 0
# suma = 0
# i = 10
# while True:
#     if i % 19 == 0:
#         suma = suma + i
#         licznik = licznik + 1
#     if licznik == n:
#         break
#     i = i + 1
# print(suma)

#opcja2
# n=int(input())
# licznik = 0
# suma = 0
# for i in range(10, 100):
#     if i % 19 == 0:
#         suma = suma + i
#         licznik = licznik + 1
#     if licznik == n:
#         break
# print(suma)

#opcja3
# n=int(input())
# suma = 0
# for i in range(19, 19*n + 1, 19):
#     suma = suma + i
# print(suma)

#opcja4
# n = int(input())
# suma = 0
# for i in range(1, n+1):
#     suma = suma + 19*i
# print(suma)

#zad7
#opcja1
# n=int(input())
# suma = 0
# for i in range(999-(999 % 37), 999-(999 % 37) - (37*n), -37):
#     suma = suma + i
# print(suma)

#zad2

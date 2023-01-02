#zad1
# x = int(input())
# suma = 0
# while x > 0:
#     cyfra = x % 10
#     suma = suma + cyfra
#     x = x // 10
# print(suma)

#zad2
# a = int(input())
# flaga = True
# for i in range(2, a):
#     if a % i == 0:
#         flaga = False
#         break
# if flaga == True:
#     print("TAK")
# else:
#     print("NIE")

#wersja2
# a = int(input())
# for i in range(2, a):
#     if a % i == 0:
#         print("NIE")
#         exit(0)
# print("TAK")

#wersja3
# a = int(input())
# suma = 0
# for i in range(2, a):
#     if a % i == 0:
#         suma = suma + i
# if suma == 0:
#     print("TAK")
# else:
#     print("NIE")

#zad3
# n = int(input())
# suma = 0
# for i in range(1, n):
#     if n % i == 0:
#         suma = suma + i
# if suma == n:
#     print(" TAK, jest doskonała ")
# else:
#     print(" NIE, nie jest doskonała ")

#zad4
# x = int(input())
# y = int(input())
# while y > 0:
#     x, y == y, x%y
# if x == 1:
#     print(f" TAK, {x} i {y} względne sa pierwsze ")
# else:
#     print(f" NIE, względne {x} i {y}  nie są pierwsze ")

#zad5
# m = int(input())
# for i in range(10, 20):
#     x, y = i, m
#     while y > 0:
#         x, y = y, x%y
#     if x == 1:
#         print(f" TAK, {i} i {m} są względnie pierwsze ")
#     else:
#         print(f" NIE, {i} i {m} nie są względnie pierwsze ")
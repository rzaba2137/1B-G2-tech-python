#zad 1 
# for i in range(1, 31):
#     print(i, end = " " )

#zad 2
# for i in range(1, 10, 2):
#     print(i**2, end=" ")

#zad 3 
# for i in range(1137, 10000, 379):
#     print(i, end=" ")

#zad 4
# for i in range(100, 1000):
#     if i%5 == 0 or i%6 == 0 or i%11 == 0:
#         print(i)

#zad 5
# n = int(input(" ilość liczb "))
# suma = 0
# for i in range(n):
#     k = int(input())
#     suma +- k
# print(suma)

#zad 6
# k = int(input())
# a = 0
# for i in range(0,2 * k,2):
#     a += i 
# print(a)

#zad 7
# m = int(input())
# for i in range(11, m * 2 + 10,2):
#     if i < 100:
#         m += i
# print(m)

#zad 8
# w = int(input("Kapitał początkowy: "))
# l = int(input("Lata trwania inwestycji: "))
# wl = 0
# suma = w
# for i in range(1, l * 12):
#     lw = suma * 0.06 * (1/12)
# suma = suma + wl
# print("Końcowy kapitał będzie wynosił: ", suma)

#zad 9
# n = int(input())
# b = 21
# suma = 0
# for i in range(0, n + 1):
#     for n in range(0, i, b):
#         suma = 0
#         n = n + 100
# print(suma)

# zad 10
# for i in range (1, 1000):
#     if i % 10 == i ** (1/2):
#         print(i)
#     elif i % 100 == i ** (1/2):
#         print(i)
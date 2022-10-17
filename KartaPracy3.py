# Pre
# for i in range(10,22): print(i, end=" ")
# Pre 2
# for i in range(15, 33, 2): print(i, end=" ")
# Pre 3
# for i in range(99,9,1): print(i, end=" ")
# Pre 4 
# for i in range(-99,-9,-1): print(i*(-1), end=" ")
# Pre 5

#Zad 1 
# n = int(input())
# for i in range(n):
#     print(i**3+3, end=" ")

#Zad 2
# for i in range(105, 1000, 15) :
#     print (i, end = "")

#PRE 2
# pętle for liczb trzycyfrowych podzielnych przez 13
# for i in range(100, 1000):
#     if i% 13 == 0:
#         print(i, end = "")
# pętle for liczb dwucyfrowych parzystych
# for i in range(10, 100): 
#     if i % 2, == 0:
#         print(i, end = "")
# pętle for potęg cyfr: 0, 1, 4, 9, 16, .. 81
# for i in range(10):
#     print(i*i, end = " ")

#zad 3
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i)
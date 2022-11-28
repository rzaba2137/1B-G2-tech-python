#zad1
# n=int(input())
# for i in range(2,n):
#     if n & i == 0:
#         print(" nie, liczba nie jest pierwsza ")
#         exit(0)

# print(" tak, liczba jest pierwsza ")

#zad2
# n=int(input())
# for i in range(2,n):
#     if n % i == 0:
#         print("NIE")
#         exit(0)
# print("TAK")

#zad3
# p, q = int(input()), int(input())

# for j in range(p, q+1):
#     flaga = True
#     for i in range(2, j):
#         if j % i == 0:
#             flaga = False
#             break
# if flaga == True:
#     print(j, end="")

#zad4
n = int(input("Podaj, ile chcesz liczb pierwszych"))
k = 2
ilosc = 0
while 1:
    flaga = True
    for i in range(2, k):
        if k % i == 0:
            flaga = False
            break
    if flaga == True:
        print(k, end = "")
   
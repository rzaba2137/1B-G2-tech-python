#zad1
n=int(input())
for i in range(2,n):
    if n & i == 0:
        print(" nie, liczba nie jest pierwsza ")
        exit(0)

print(" tak, liczba jest pierwsza ")
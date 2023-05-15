from random import randint
n = 10
L = [randint(1,30) for i in range(n)]
print(L)

for i in range(n):
    mi = i
    for j in range(i+1, n):
        if L[j] < L[mi]:
            mi = j
        
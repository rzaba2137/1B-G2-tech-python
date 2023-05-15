#anagramy np. adam dama
a = input()
b = input()
X, Y = list(a), list(b)
X.sort()
Y.sort()
a = "".join(X)
b = "".join(Y)
print(a,b)
if a == b:
    print("TAK")
else:
    print("NIE")

#anagramy przez tablicę
a = input()
b = input()
X = [0] * 200
Y = [0] * 200
for i in range(len(a)):
    X[ord(a[i])] += 1
for j in range(len(b)):
    Y[ord(b[j])] += 1
if X == Y:
    print("TAK")
else:
    print("NIE")
print(X)

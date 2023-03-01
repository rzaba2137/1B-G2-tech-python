#napis jest prawie "listą" 
# s = input()
# print(s)

# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(s[i])

# L = [5,7,2,4]
# print(L)
# L.sort()
# print(L)
# s = input()
# s.sort() - to jest błąd, napis to nie normalna lista
# print(s)

#przechodzenie: napis <-> lista (list() i join())

# s = input()
# L = list(s)
# print(s, L)
# L.sort()
# print(s, L)
# s = "" .join(L)
# print(s, L)


#napisz algorytm, który sprawdzi, czy wyraz jest palindromem
s = input()
L1 = list(s)
L2 = list(s)
L2.reverse()
if L1 == L2:
    print("TAK")
else:
    print("NIE")

#wersja 2
s = input()
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        exit("NIE")
exit("TAK")
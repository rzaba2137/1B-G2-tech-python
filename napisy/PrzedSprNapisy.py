# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisany napis
# d = input()
# s = 0
# for x in d:
#     s += ord(x)
# znak = s // len(d)
# print(chr(znak))

# 5. Policz ile we wpisanym napisie jest liter A.

# e = input()
# ilość = 0
# for x in e:
#     if x == "A":
#         ilość += 1
# print(ilość)

#SAMO = ["A", "E", "I", "O", "U"]

#ilość_samo = 0
#for x in e:
#    if x in SAMO:
#        ilość_samo += 1
#ilość_samo

# 6. Podaj dominującą literkę we wpsianym napisie
# Niech to będzie jedna literka

# f = input()
# maksiu = 0
# for x in f:
#     if f.count(x) > maksiu:
#         maksiu = f.count(x)
#         literka = x
# print(literka, maksiu)

# 8. Sprawdź, czy w napisie występują 3 podciągi "LA"

h = input()
ilość = 0
for i in range(len(h)):
    if h[i:i+2] == "LA":
    if h[i] == "L" and h[i+1] == "a":    
    if h[i] + h[i+1] == "LA":
        ilość += 1
# funkcja ord() - zwraca kod ascii danego znaku
print(ord( "A" ))
print(ord( "B" ))
print(ord( "C" ))

# funkcja chr() - zwraca znak danego kodu ascii
print(chr(65))
print(chr(75))
print(chr(89))

# znaki ascii od A-Z mają kody 65-90 !!!!!!!!

# wypisz pętlą range cały alfabet A-Z
for i in range(65, 91):
    print(chr(i), end = " ")

# jak słowo rozbić na litery...?

napis = "POLSKA"
print(len(napis)) # zwraca długosć napisu 
print(napis[0])   # napis to lista
print(napis[1])
print(napis[2])

# wypisz kody ASCII literek napisu 
napis = "POLSKA"
for i in range(len(napis)):
    print(ord(napis[i]))
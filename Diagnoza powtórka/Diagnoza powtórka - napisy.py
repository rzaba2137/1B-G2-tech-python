#zad1
#znajdź ilość liter c we wpisanym napisie

def policz_wystapienia_litery_c(napis):
    licznik = 0
    for znak in napis:
        if znak == 'c' or znak == 'C':
            licznik += 1
    return licznik

napis = input("Wprowadź napis: ")

liczba_wystapien = policz_wystapienia_litery_c(napis)
print("Ilość wystąpień litery 'c':", liczba_wystapien)

#zad2
#sprawdź czy literki w napisie są w porządku nierosnącym

def sprawdz_czy_napis_nierosnacy(napis):
    for i in range(1, len(napis)):
        if napis[i] < napis[i - 1]:
            return False
    return True

napis = input("Wprowadź napis: ")

czy_nierosnacy = sprawdz_czy_napis_nierosnacy(napis)
if czy_nierosnacy:
    print("Litery w napisie są ułożone w porządku nierosnącym.")
else:
    print("Litery w napisie nie są ułożone w porządku nierosnącym.")


#zad 3
#podaj najdłuższy z 3 wpisanych przez usera wyrazów

def znajdz_najdluzszy_wyraz(wyraz1, wyraz2, wyraz3):
    dlugosc1 = len(wyraz1)
    dlugosc2 = len(wyraz2)
    dlugosc3 = len(wyraz3)

    if dlugosc1 >= dlugosc2 and dlugosc1 >= dlugosc3:
        return wyraz1
    elif dlugosc2 >= dlugosc1 and dlugosc2 >= dlugosc3:
        return wyraz2
    else:
        return wyraz3

wyraz1 = input("Wprowadź pierwszy wyraz: ")
wyraz2 = input("Wprowadź drugi wyraz: ")
wyraz3 = input("Wprowadź trzeci wyraz: ")

najdluzszy_wyraz = znajdz_najdluzszy_wyraz(wyraz1, wyraz2, wyraz3)
print("Najdłuższy wyraz:", najdluzszy_wyraz)
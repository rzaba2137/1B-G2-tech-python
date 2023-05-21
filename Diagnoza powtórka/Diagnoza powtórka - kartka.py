#zad 1
#oblicz wartość ONP

def oblicz_onp(wyrazenie):
    stack = []

    for element in wyrazenie:
        if element.isdigit():
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if element == '+':
                stack.append(operand1 + operand2)
            elif element == '-':
                stack.append(operand1 - operand2)
            elif element == '*':
                stack.append(operand1 * operand2)
            elif element == '/':
                stack.append(operand1 / operand2)

    return stack.pop()

wyrazenie_onp = input("Wprowadź wyrażenie w ONP: ").split()

wynik = oblicz_onp(wyrazenie_onp)
print("Wynik:", wynik)

#zad 2
#znajdź postać ONP dla pisanego wyrażenia

def precedencja(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def konwersja_do_onp(wyrazenie):
    onp = []
    stos_operatorow = []

    for element in wyrazenie:
        if element.isdigit():
            onp.append(element)
        elif element == '(':
            stos_operatorow.append(element)
        elif element == ')':
            while stos_operatorow and stos_operatorow[-1] != '(':
                onp.append(stos_operatorow.pop())
            if stos_operatorow and stos_operatorow[-1] == '(':
                stos_operatorow.pop()
        else:
            while stos_operatorow and precedencja(stos_operatorow[-1]) >= precedencja(element):
                onp.append(stos_operatorow.pop())
            stos_operatorow.append(element)

    while stos_operatorow:
        onp.append(stos_operatorow.pop())

    return onp


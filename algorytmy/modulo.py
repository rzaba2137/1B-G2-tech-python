# a = int(input())
# b = int(input())
# while b > 0:
#     a, b = b, a % b

a, b = int(input()), int(input())
iloczyn = a * b
a, b = b, a%b
nwd = a
print(iloczyn // nwd)
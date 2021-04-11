from math import pow, sqrt

def calcular_hipotenusa(a, b):
    return sqrt(pow(a, 2) + pow(b, 2))


a = int(input("A: "))
b = int(input("B: "))
hipotenusa = calcular_hipotenusa(a, b)
print(f"A hipotenusa que possui os catetos {a} e {b} é {hipotenusa}")
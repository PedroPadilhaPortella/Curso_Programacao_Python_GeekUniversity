from math import pow


conjunto = set()
for i in range(0, 10):
    x = int(input("Numero Real: "))
    conjunto.add(x)
conjunto2 = set()
for i in conjunto:
    n = pow(i, 2)
    conjunto2.add(n)
print(conjunto2)
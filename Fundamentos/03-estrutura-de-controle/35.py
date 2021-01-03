def somarImpares(a, b):
    impares = 0
    c = 0
    if(b < a):
        c = a
        a = b
        b = c
    for i in range(a, b + 1):
        if(i % 2 != 0):
            impares += i
    return impares

n1 = int(input("Primeiro valor: "))
n2 = int(input("Ultimo valor: "))
print("A soma dos valores impares entre {} e {} é {}".format(n1, n2, somarImpares(n1, n2)))
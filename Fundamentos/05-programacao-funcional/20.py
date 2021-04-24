def fatorial(n):
    fat = 1
    for i in range(n, 1, -1):
        fat *= i
    return fat


numero = int(input("Insira um numero: "))
print(f"O fatorial de {numero}! é {fatorial(numero)}")
def soma_inteiros(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma



n = int(input("Entre com um numero: "))
print(f'Soma: {soma_inteiros(n)}')
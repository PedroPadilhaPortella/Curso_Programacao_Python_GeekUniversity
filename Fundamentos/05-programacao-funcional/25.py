from math import pow


def soma_serie(N):
    soma = 0
    for i in range(1, N + 1):
        soma += (pow(N, 2) + 1) / (N + 3)
    return soma


print(soma_serie(1))
print(soma_serie(2))
print(soma_serie(4))
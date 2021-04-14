def soma_dos_valores_entre(inferior, superior):
    soma = 0
    for i in range(inferior + 1, superior):
        soma += i
    return soma


print(soma_dos_valores_entre(0, 51))
print(soma_dos_valores_entre(0, 11))
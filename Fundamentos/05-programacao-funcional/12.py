def soma_algarismos(numero):
    soma = 0
    string = str(numero)
    for letter in string:
        soma += int(letter)
    return soma


numero = int(input("Digite um numero: "))
print(f"A soma dos algarismos desse numero é {soma_algarismos(numero)}")
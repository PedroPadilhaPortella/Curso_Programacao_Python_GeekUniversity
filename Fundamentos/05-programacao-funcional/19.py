def maior_fator_primo(x):
    primo = 'não há primos'
    for numero in range(0, x):

        quantidadeDeDivisores = 0
        for divisores in range(1, numero):
            if(numero % divisores == 0):
                quantidadeDeDivisores += 1
        if(quantidadeDeDivisores==1):
            primo = numero
    return primo


numero = int(input("Insira um numero: "))
print(f"O maior fator primo entre 0 e {numero} é {maior_fator_primo(numero)}")
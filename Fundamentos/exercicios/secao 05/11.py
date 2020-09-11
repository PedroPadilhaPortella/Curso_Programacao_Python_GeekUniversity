def calcular(n):
    if(n != 0):
        soma = 0
        while n:
            soma += n % 10 # Soma `s` ao ultimo numeral de `n`
            n //= 10 # Remove o ultimo numero de `n`
        return soma
    else:
        print("Numero Inválido")
        exit()


numero = int(input("Numero Inteiro não nulo: "))
soma =  calcular(numero)
print(f"Soma: {soma}")


n = input("Digite um número inteiro: ")
print(sum(int(i) for i in n))
def divisor(num):
    divisores = []
    soma = 0
    for i in range(1, num):
        if(num % i == 0):
            divisores.append(i)
            soma += i
    return [divisores, soma]


num = int(input("Insira um numero positivo: "))
[divisores, soma] = divisor(num)
print("A soma dos divisores de {} é {}".format(num, soma))
print("Divisores: {}".format(divisores))
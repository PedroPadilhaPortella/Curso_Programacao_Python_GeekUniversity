def soma():
    soma = 0
    valores = []
    for i in range(1, 1001):
        if(i % 3 == 0 and i % 5 == 0):
            soma += i
            valores.append(i)
    print("A soma dos valores divisiveis por 3 e 5 é {}\n\n".format(soma))
    print("Valores: {}".format(valores))

soma()
def sequence():
    soma = 0
    n1 = 1
    n2 = 1
    while(n1 <= 99 or n2 <= 50):
        soma += n1/n2
        n1 += 1
        n2 += 2
    return soma

print("Soma da Sequencia: {:.4f}".format(sequence()))

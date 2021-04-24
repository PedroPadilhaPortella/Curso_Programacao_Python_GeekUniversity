def print_exclamacao(quantidade):
    exclamacao = ''
    for i in range(0, quantidade):
        exclamacao += '!'
        print(exclamacao)


n = int(input("Quantas exclamações serão apresentadas: "))
print_exclamacao(n)
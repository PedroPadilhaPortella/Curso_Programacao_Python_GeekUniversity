def print_asteriscos_piramide(linhas):
    for linha in range(linhas):
        espacos = linhas - linha - 1
        asteriscos = 1 + linha * 2
        print(' ' * espacos + '*' * asteriscos)



n = int(input("Quantos asteriscos serão apresentadas: "))
print_asteriscos_piramide(n)
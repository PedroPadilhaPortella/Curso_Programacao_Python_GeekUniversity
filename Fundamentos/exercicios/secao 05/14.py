def media(n1, n2, n3):
    return ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10


trabalho = float(input("Trabalho de Laboratório: "))
avaliacao = float(input("Avaliação Semestral: "))
exame = float(input("Exame Final: "))

print("Media: {}".format(media(trabalho, avaliacao, exame)))
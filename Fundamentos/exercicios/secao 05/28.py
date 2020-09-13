import math

def geometrica(a, b, c):
    media = (a * b * c) ** (1/3)
    print("A Média Geométrica de {}, {} e {} = {:.2f}".format(a, b, c, media))


def ponderada(a, b, c):
    media = (a * 2 + b * 3 + c) / 6
    print("A Média Ponderada de {}, {} e {} = {:.2f}, com A valendo 2 e B valendo 3".format(a, b, c, media))


def harmonica(a, b, c):
    media = 1 / (1/a) + (1/b) + (1/c)
    print("A Média Harmônica de {}, {} e {} = {:.2f}".format(a, b, c, media))


def aritmetica(a, b, c):
    media = (a + b + c) / 3
    print("A Média Aritmética de {}, {} e {} = {:.2f}".format(a, b, c, media))


def main():
    print("Escolha um tipo de media para ser calculada:")
    print("1- Média Geométrica\n2- Média Ponderada\n3- Média Harmônica\n4- Média Aritmética")
    option = int(input("Opção:__"))
    a = float(input("A:"))
    b = float(input("B:"))
    c = float(input("C:"))

    if(option == 1):
        geometrica(a, b, c)
    elif(option == 2):
        ponderada(a, b, c)
    elif(option == 3):
        harmonica(a, b, c)
    elif(option == 4):
        aritmetica(a, b, c)
    else:
        print("Opção Inválida!")


main()
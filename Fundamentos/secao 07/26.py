from math import pow, sqrt


def CalcularMedia(vetor):
    return sum(vetor) / len(vetor)

def CalcularVariancia(vetor):
    mediaNotas = CalcularMedia(vetor)
    numerador = variancia = 0
    for amostra in vetor:
        variancia += pow(amostra - mediaNotas, 2)
    return variancia / (len(vetor) - 1)

def CalcularDesvioPadrao(vetor):
    variancia = CalcularVariancia(vetor)
    return sqrt(variancia)

notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(CalcularDesvioPadrao(notas))

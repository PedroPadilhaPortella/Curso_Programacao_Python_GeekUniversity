from math import factorial


def fatorialHarmonico():
    harmonico = 0
    n = 1
    a = 1
    b = 2
    while(n <= 5):
        harmonico += a/factorial(b)
        a += 2
        b += 2
        n += 1
    return harmonico


harmonico = fatorialHarmonico()
print("O Valor da Série Harmônica de 5 valores é {:.3f}".format(harmonico))
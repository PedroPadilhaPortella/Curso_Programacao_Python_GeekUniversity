from math import factorial

def fatorialHarmonico(num):
    harmonico = 0
    for i in range(1, num + 1):
        harmonico += 1/factorial(i)
    return harmonico


num = int(input("Insira um numero: "))
harmonico = fatorialHarmonico(num)
print("O Numero Harmônico de {} é {:.3f}".format(num, harmonico))
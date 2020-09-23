def numeroHarmonico(num):
    harmonico = 0
    for i in range(1, num + 1):
        harmonico += 1/i
    return harmonico


num = int(input("Insira um numero: "))
harmonico = numeroHarmonico(num)
print("O Numero Harmônico de {} é {:.3f}".format(num, harmonico))
def fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

n = int(input("Fatorial: "))
print("O fatorial de {} é {}".format(n, fatorial(n)))
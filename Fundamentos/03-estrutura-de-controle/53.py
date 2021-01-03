print("**Triangulo de Floyd**")
lines = int(input("Quantas linhas o triangulo vai ter? "))

def escada(lines):
    n = 1
    for i in range(1, lines + 1):
        for j in range(1, i + 1):
            print(n, end=" ")
            n += 1
        print('')

escada(lines)

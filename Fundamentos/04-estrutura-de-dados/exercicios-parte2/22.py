from random import randint


def printar(matriz):
    for l in range(3):
        for c in range(3):
            print(f'[{matriz[l][c]:^5}]', end=" ")
        print()
    print('- ' * 15)


a = [[randint(1, 9) for x in range(3)] for y in range(3)]
b = [[randint(1, 9) for s in range(3)] for t in range(3)]

c = [[a[lin][col] * b[lin][col] for col in range(3)] for lin in range(3)]

printar(a)
printar(b)
printar(c)
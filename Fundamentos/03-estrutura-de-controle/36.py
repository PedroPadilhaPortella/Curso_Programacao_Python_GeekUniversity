from math import pow


def somaDosQuadrados():
    quad = 0
    for i in range(1, 101):
        quad += pow(i, 2)
    return quad

def QuadradoDaSoma():
    sum = 0
    for i in range(1, 101):
        sum += i
    sum = pow(sum, 2)
    return sum


n = QuadradoDaSoma() - somaDosQuadrados()
print("A diferenca entre a soma dos quadrados e o quadrado da soma dos valores de 1 a 100 é\n{:.0f}".format(n))
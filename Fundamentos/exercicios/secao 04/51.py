from math import sqrt, pow



def calcularDistancia(x, y):
    return sqrt(pow(0 - x, 2) + pow(0 - y, 2))


x = int(input("Ponto X: "))
y = int(input("Ponto Y: "))
dist = calcularDistancia(x, y)
print("Distancia do eixo (0, 0): {}".format(dist))
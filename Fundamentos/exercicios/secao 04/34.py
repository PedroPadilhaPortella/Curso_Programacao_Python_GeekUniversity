from math import pi, pow

def areaCirculo(r):
    return pi * pow(r, 2)

raio = float(input("Raio: "))
area = areaCirculo(raio)
print("A area do circulo de raio {} é {:.2f}".format(raio, area))
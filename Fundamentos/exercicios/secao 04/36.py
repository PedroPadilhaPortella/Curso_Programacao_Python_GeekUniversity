from math import pi, pow

def volumeCilindro(r, h):
    return pi * pow(r, 2) * h

raio = float(input("Raio do Cilindro: "))
altura = float(input("Altura do Cilindro: "))
volume = volumeCilindro(raio, altura)
print("O volume de um cilindro de altura {} e raio {} é {:.2f}".format(altura, raio, volume))
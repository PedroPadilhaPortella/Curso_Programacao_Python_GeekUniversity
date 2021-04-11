from math import pi, pow

def calcular_cilindro(altura, raio):
    volume = pi * pow(raio, 2) * altura
    return round(volume, 2)

altura = int(input("Altura: "))
raio = int(input("Raio: "))
volume = calcular_cilindro(altura, raio)
print(f"O cilindro de altura {altura} cm e raio de {raio} cm possui o volume de {volume} cm2")
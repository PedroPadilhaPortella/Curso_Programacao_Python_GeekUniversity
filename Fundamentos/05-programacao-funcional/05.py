from math import pi as PI
from math import pow


def volume_esfera(raio):
    return (4 / 3) * PI * pow(raio, 2)


raio = 10
print(f"O Volume de uma esfera de raio {raio} é de {volume_esfera(raio)}")
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return self.raio * self.raio * 3.14

    def calcularPerimetro(self):
        return self.raio * 2 * 3.14

    def imprimir(self):
        print(f'Raio: {self.raio}, Area: {self.calcularArea()}, Perimetro: {self.calcularPerimetro()}')

rect = Circulo(5)

print(rect.calcularArea())
print(rect.calcularPerimetro())

rect.imprimir()
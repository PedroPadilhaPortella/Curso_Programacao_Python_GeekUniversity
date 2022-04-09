class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return self.lado * 4

    def imprimir(self):
        print(f'Lado: {self.lado}, Area: {self.calcularArea()}, Perimetro: {self.calcularPerimetro()}')


square = Quadrado(5)

print(square.calcularArea())
print(square.calcularPerimetro())

square.imprimir()
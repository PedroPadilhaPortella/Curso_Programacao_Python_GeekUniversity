class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)

    def imprimir(self):
        print(f'Comprimento: {self.comprimento}, Largura: {self.largura}, Area: {self.calcularArea()}, Perimetro: {self.calcularPerimetro()}')

rect = Retangulo(5, 10)

print(rect.calcularArea())
print(rect.calcularPerimetro())

rect.imprimir()
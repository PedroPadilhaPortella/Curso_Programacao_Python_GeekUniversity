class Eletrodomestico:
    def __init__(self, name, voltagem):
        self.name = name
        self.voltagem = voltagem
        self.ligado = False

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def imprimir(self):
        print(f'Nome: {self.name}, Voltagem: {self.voltagem}, Ligada? {self.ligada}')

microwave = Eletrodomestico('Microwave', 110)
microwave.ligar()

microwave.imprimir()
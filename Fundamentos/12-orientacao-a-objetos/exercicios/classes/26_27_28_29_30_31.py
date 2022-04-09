from pickle import FALSE


class Microondas:
    def __init__(self):
        self.ligado = False
        self.porta_aberta = False

    def ligar(self):
        if self.porta_aberta == False:
            self.ligado = True

    def desligar(self):
        self.ligado = False

    def abrir_porta(self):
        self.porta_aberta = True

    def fechar_porta(self):
        self.porta_aberta = False

    def imprimir(self):
        print(f'Ligado? {self.ligado}')
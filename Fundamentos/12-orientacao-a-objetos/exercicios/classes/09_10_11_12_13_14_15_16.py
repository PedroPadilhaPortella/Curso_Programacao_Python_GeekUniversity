class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.ligada = False
        self.menor_marcha = 0
        self.maior_marcha = 7

    def marcha_acima(self):
        if(self.marcha + 1 < self.maior_marcha):
            self.marcha += 1

    def marcha_abaixo(self):
        if(self.marcha - 1 > self.menor_marcha):
            self.marcha -= 1

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def imprimir(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Marcha: {self.marcha}, Ligada? {self.ligada}')

xre = Moto('XRE', 'XR-10', 'Preto', 1)

xre.marcha_acima()
xre.marcha_acima()
xre.marcha_abaixo()
xre.ligar()

xre.imprimir()

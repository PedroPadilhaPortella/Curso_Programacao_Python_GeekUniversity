class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self):
        print(f'{self.nome}, Address: {self.endereco}, Tel:. {self.telefone}')


p1 = Pessoa('Pedro', 'R Um, São Paulo', '11987654321')

p1.imprimir()
'''
Iterador Customizado

    Criar uma classe e implementar um iterador para ela com os metodos __iter__() e __next__().
'''

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration

print(next(iter(Contador(1, 10))))


for n in Contador(1, 11):
    print(n)
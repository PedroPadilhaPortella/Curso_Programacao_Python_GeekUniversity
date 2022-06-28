'''
    Pickle -> Serialização/Deserialização de Objetos Python
'''
import pickle

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f'{self.nome} está comendo')


class Cavalo(Animal):    
    def __init__(self, nome):
        super().__init__(nome)

    def cavalgar(self):
        print(f'{self.nome} está cavalgando')


class Cachorro(Animal):    
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome} está latindo')


cavalo = Cavalo('Tempestade')
cachorro = Cachorro('Billy')

# Serialização e escrita de dados
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((cavalo, cachorro), arquivo)

# Deserialização e leitura de dados
with open('animais.pickle', 'rb') as arquivo:
    cavalo, cachorro = pickle.load(arquivo)
    cavalo.cavalgar()
    cachorro.latir()
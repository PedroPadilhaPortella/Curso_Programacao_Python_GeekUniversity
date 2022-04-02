'''
super()

    Referencia da superclasse para a subclasse.

'''

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        print("O animal fala")

class Cachorro(Animal):
    def __init__(self, nome):
        Animal.__init__(self, nome) # chama o construtor da superclasse pelo nome da superclasse

    def falar(self):
        print("O cachorro late")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome) # chama o construtor da superclasse via super()

    def falar(self):
        print("O gato mia")

class Passaro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print("O passaro pia")

cachorro = Cachorro("Bobby")
gato = Gato("Garfield")
passaro = Passaro("Polly")

cachorro.falar()
gato.falar()
passaro.falar()

print(cachorro.nome)
print(gato.nome)
print(passaro.nome)

print(isinstance(cachorro, Cachorro))
print(isinstance(cachorro, Animal))
print(isinstance(cachorro, Passaro))
print(isinstance(cachorro, Gato))
'''
    Trabalhando com Json e Pickle

    > pip install jsonpickle
'''
import json
import jsonpickle

class Cavalo:    
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def cavalgar(self):
        print(f'{self.nome}, um {self.raca}, está cavalgando')

cavalo = Cavalo('Pegasus', 'Mustangue')

cavaloJson = json.dumps(cavalo.__dict__)
print(cavaloJson)

cavaloEncoded = jsonpickle.encode(cavalo)
print(cavaloEncoded)

with open('cavalo.json', 'w') as arquivo:
    ret = jsonpickle.encode(cavalo)
    arquivo.write(ret)

with open('cavalo.json', 'r') as arquivo:
    content = arquivo.read()
    ret = jsonpickle.decode(content)
    print(ret.__dict__)
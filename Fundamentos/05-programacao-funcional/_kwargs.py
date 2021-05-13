"""                  **kwargs

O *args coloca os argumentos do metodo em uma tupla,
porém o **kwargs exige que os parametros sejam nomeados,
e transforma esses parametros em um dicionário.
"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita do {pessoa.title()} é a cor {cor.title()}')


cores_favoritas(pedro="laranja", casalli="roxo", bunhak="preto", vinicius="verde")

# Os parametros *args e **kwargs não são obrigatórios, 
cores_favoritas()


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return "Perfeito"
    elif 'geek' in kwargs:
        return "Aceitavel"
    else:
        return "Péssimo"

print(cumprimento_especial(geek="python", teste="teste"))
print(cumprimento_especial(geek="java", teste="teste"))
print(cumprimento_especial(udemy="python", teste="teste"))


# A ordem da declaração dos parametros segue a regra:
# - Parametros obrigatórios
# - *args
# - Parametros default (não obrigatórios)
# - ** kwargs

def params(nome, idade, *args, solteiro=True, **kwargs):
    print()
    print(f'{nome} tem {idade}')
    print(f'args: {args}')
    print(f'solteiro: {solteiro}')
    print(f'kwargs: {kwargs}')

params('pedro', 19)
params('pedro', 19, 4, 2, 5, 2, solteiro=False)
params('daniel', 12, 4, sexo='masculino', teste="teste")


def info(a, *args, nome="Pedro", **kwargs):
    return [a, args, nome, kwargs]

print(info(1, 2, 3,  'masculino', sobrenome="Portella", idade="19"))


# Desempacotamento [spread operator] de objetos e listas,
# os nomes dos parametros das chaves precisam ser os mesmos da função
def nomes(**kwargs):
    return f"\n{kwargs['nome']} {kwargs['sobrenome']}"

nome = {'nome': "Pedro", 'sobrenome': "Portella"}
print(nomes(**nome))


def soma(a, b, c):
    print(a + b + c)

lista = [4, 2, 1]
soma(*lista)
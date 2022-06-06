'''
Preservando Metadata com Wraps

    Metadata são dados intrínsecos de arquivos, ou de uma função, como o nome, docstring, etc.
    Wraps são funções que envolvem e preservam esses dados.

    O objetivo do wraps é manter a documentação da função original, sempre que a função decorada for chamada. Evitando de alterar a documentação original, sendo ela substituída pela documentação da função decorada.
'''
from functools import wraps


def ver_log(funcao):
    @wraps(funcao) # Preserva o nome da função original
    def logar(*args, **kwargs):
        '''Eu sou a função interna Logar'''
        print(f'Função {logar.__name__} chamada')
        print(f'Documentação: {logar.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def somar(a, b):
    '''Somar dois numeros'''
    return a + b


print(somar(10, 30))
print(somar.__name__)
print(somar.__doc__)
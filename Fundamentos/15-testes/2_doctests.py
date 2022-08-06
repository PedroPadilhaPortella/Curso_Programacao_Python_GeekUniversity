'''
    DocTests
        De certa forma, o próprio teste serve de documentação do projeto. Mas podemos criar 
        documentações específicas para nossos código usando testes dentro das funções e métodos.

        Doctests são testes que colocamos na doctring dos metodos e funções em python.
    Para rodar os testes do doctest, execute:
        python -m doctest -v 2_doctests.py
'''

def soma(a, b):
    """Soma dois valores numericos.

    >>> soma(1,2)
    3
    >>> soma(1, -3)
    -2
    """
    return a + b



def duplicar(valores):
    """Duplica os valores de uma lista.

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    >>> duplicar([])
    []
    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * valor for valor in valores]


def saudacao():
    """ Retorna 'oi'

    >>> saudacao()
    'oi'
    """
    return "oi"


def veracidade():
    """ Retorna a verdade

    >>> veracidade()
    True
    """
    return True
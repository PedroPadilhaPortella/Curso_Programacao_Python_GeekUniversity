'''
Pacotes e Modulos
    Módulo --> Um arquivo Pyhton que pode conter um conjunto de classes e funções.

    Pacotes --> Um diretório contendo um conjunto de módulos.

    Nas versões do Python 2.X, um pacote precisava ter um aruivo __init__.py para sializar que era um pacote.
    Nas versões do Python 3.X, essa adoção é opcional.
'''

from pacote import module_1, module_2
from pacote.subpacote import module_3, module_4

module_1.funcao1()
module_2.funcao2()
module_3.funcao3()
module_4.funcao4()
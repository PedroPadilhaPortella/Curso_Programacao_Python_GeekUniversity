'''
    Lançando erros com Raise

    Semelhante ao throw do Java, podemos lançar um erro com o raise.
'''
from colorama import Fore

def colorir(texto, cor):
    cores = {
        'RED':Fore.RED, 
        'GREEN':Fore.GREEN, 
        'YELLOW':Fore.YELLOW, 
        'BLUE':Fore.BLUE, 
        'MAGENTA':Fore.MAGENTA, 
        'CYAN':Fore.CYAN, 
        'WHITE':Fore.WHITE
    }

    if cor not in cores.keys():
        raise ValueError(f'A cor precisa ser uma das seguintes: {cores}')
    print(cores[cor] + f"O texto '{texto}' será impresso em {cor}" + Fore.RESET)

try:
    texto = input('Digite uma texto: ')
    cor = input('Digite uma cor: ')
    colorir(texto, cor)
except ValueError as err:
    print(err)
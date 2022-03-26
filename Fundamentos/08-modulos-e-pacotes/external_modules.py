'''
External Modules
    São os módulos desenvolvidos por outros desenvolvedores na comunidade Python, e podem ser instalados
    em seus projetos.

    https://pypi.org/

    Ex -> colorama: Impressão de textos coloridos no terminal
'''
from colorama import init, Fore, Back, Style

print(Fore.RED + 'Tests FAILED - 0%')
print(Fore.YELLOW + 'Tests OK - 60%')
print(Fore.GREEN + 'Tests are Okay - 100%')
print(Back.WHITE + Fore.BLACK + "Project ready to Deploy" + Style.RESET_ALL)
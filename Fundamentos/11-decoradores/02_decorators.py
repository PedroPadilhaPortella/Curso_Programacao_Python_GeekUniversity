'''
Decoradores (Decorators)

    Decoradores são funções que envolvem outras funções e aprimoram seu comportamento.
    Eles possuem uma sintaxe propria, usando o decorador @.
'''

def be_educated(fun):
    def beeing():
        print('Hajimemashite')
        fun()
        print('Ja ne')

    return beeing


def saudacao():
    print('Anata no namae wa pedro')

def despedida():
    print('Konnichiwa')


teste = be_educated(saudacao)
teste2 = be_educated(despedida)

teste()
teste2()


# Decorators como Syntax Sugar
def exercicio(fun):
    def resultado(a, b):
        print("O resultado da operacao é:")
        fun(a, b)
    return resultado

@exercicio
def somar(a, b):
    print(a + b)

somar(2, 2)
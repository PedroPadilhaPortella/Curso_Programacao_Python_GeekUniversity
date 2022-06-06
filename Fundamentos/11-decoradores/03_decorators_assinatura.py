'''
Decorators com diferentes assinaturas

    Decorators com diferentes assinaturas são funções decoradoras com diferentes parametros de entrada.
    
    A Assinatura de uma função é definida pelo Nome da função, tipo de retorno e pelos parametros de entrada.
    
    Utilizamos o padrão de projetos Decorator Pattern, com o *args e **kwargs.
'''
# Função que recebe uma função como argumento e retorna uma função com a assinatura alterada
def calcular(funcao):
    def executar(*args):
        return funcao(*args)
    return executar


@calcular
def somar(*args):
    return args[0] + args[1]

@calcular
def subtrair(*args):
    return args[0] - args[1]

@calcular
def multiplicar(*args):
    return args[0] * args[1]

@calcular
def dividir(*args):
    return args[0] / args[1]


print(somar(10, 5))
print(subtrair(10, 5))
print(multiplicar(10, 5))
print(dividir(10, 5))

# Decorator com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! o primeiro valore precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args

@verifica_primeiro_argumento(10)
def soma_dez(a, b):
    return a + b


print(comida_favorita('pizza', 'frango', 'batata'))
print(soma_dez(10, 20))
print(comida_favorita('strogonoff', 'frango', 'batata'))
print(soma_dez(1, 20))
'''
    Utilizando lambdas
    São conhecidas como Expressões Lambda, as funções sem nome, funções anonimas.
'''

# Funcao Normal
def funcao_normal(x):
    return x * 3 + 1

print(funcao_normal(4))
print(funcao_normal(7))

# Funcao Lambda (anonima)
funcao_lambda = lambda x: x * 3 + 1

print(funcao_lambda(4))
print(funcao_lambda(7))


nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo('pedro henrique', 'padilha portella da cruz'))

sem_parametros = lambda: 'Lambda sem parametros'
print(sem_parametros())


# Lambda no sort
autores = ['Issac', 'Ray Bradbury', 'Arthur C. Clark', 'Frank Castle', 'H. G. Whells', 'Doug Addams']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
print()

# Funcao Quadratica
def geradora_funcao_quadratica(a, b, c):
    '''
        Retorna a funcao de f(x) = a*x**2 + b*x + c
    '''
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(0, 1, 2)(13))
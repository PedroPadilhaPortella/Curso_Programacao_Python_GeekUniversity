'''
    Argumentos Unicamente Posicionais
'''

# função normal
def funcao_1(nome):
    print(f"Olá, meu nome é {nome}")

# função com argumento posicional usando /
def funcao_2(nome, /):
    print(f"Olá, meu nome é {nome}")

# função com um argumento posicional usando /, e um argumento normal
def funcao_3(nome, /, idade):
    print(f"Olá, meu nome é {nome}, eu tenho {idade} anos")

# função com todos argumentos posicionais
def funcao_4(nome, idade, /):
    print(f"Olá, meu nome é {nome}, eu tenho {idade} anos")

# função com todos argumentos nomeados
def funcao_5(*, nome, idade):
    print(f"Olá, meu nome é {nome}, eu tenho {idade} anos")

# utilizando todas as estratégias
def funcao_6(nome, /, idade, *, message):
    print(f"Olá, meu nome é {nome}, eu tenho {idade} anos. {message}")


funcao_1('Pedro')
funcao_1(nome='Pedro')

funcao_2('Pedro')
# funcao_2(nome='Pedro')

funcao_3('Pedro', idade=21)
funcao_3('Pedro', 21)

funcao_4('Pedro', 21)
# funcao_4(nome='Pedro', idade=21)

funcao_5(nome='Pedro', idade=21)
# funcao_5('Pedro', 21)

funcao_6('Pedro', 21, message='Eu sou desenvolvedor fullstack!')
funcao_6('Pedro', idade=21, message='Eu sou desenvolvedor fullstack!')
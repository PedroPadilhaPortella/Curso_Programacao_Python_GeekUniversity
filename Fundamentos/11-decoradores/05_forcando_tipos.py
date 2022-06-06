'''
Forçando Tipos de dados com Decoradores  
'''

def forcar_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novos_args = []
            for (valor, tipo) in zip(args, tipos):
                novos_args.append(tipo(valor))
            return funcao(*novos_args, **kwargs)
        return converter
    return decorador


@forcar_tipo(str, int, float)
def pessoa(nome, idade, altura):
    print(f'{nome} tem {idade} anos e mede {altura}m')

pessoa('pedro', 21, 1.74)
pessoa(0, 'a', 'b')
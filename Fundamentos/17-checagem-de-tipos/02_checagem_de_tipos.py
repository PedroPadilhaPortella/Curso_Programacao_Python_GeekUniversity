'''
    Checagem de tipos com MyPy

    execute mypy 02_checagem_de_tipos.py
'''


def cumprimentar(nome: str) -> str :
    return f"Olá {nome}"

print(cumprimentar('Pedro'))

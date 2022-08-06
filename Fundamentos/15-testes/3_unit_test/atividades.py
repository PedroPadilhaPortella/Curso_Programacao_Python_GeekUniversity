def comer(comida, is_saudavel):
    if(is_saudavel):
        return f'{comida} é saudável'
    else:
        return f'{comida} não é saudável'


def dormir(tempo):
    if(tempo >= 8):
        return 'parece que a noite foi longa'
    else:
        return 'você está dormindo pouco'


def is_funny(nome):
    return nome in ['Danilo Gentili', 'Léo Lins', 'Maurício Meireles', 'Rafinha Bastos', 'Thiago Ventura']
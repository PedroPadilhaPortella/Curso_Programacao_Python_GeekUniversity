'''
Min
    min() -> Função que retorna o menor valor de um iterável ou de dois ou mais elementos.
Max
    max() -> Função que retorna o maior valor de um iterável ou de dois ou mais elementos.

'''

lista = {1, 2, 3, 4, 5}

print("Max:", max(lista))
print("Min", min(lista))

# Outros exemplos de uso

print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'z'))
print(max(1.9999, 1.9999999))
print(max('pedro'))

# Usando Lambdas
users = [
 {'username': 'pedro123', 'tweets': []},
 {'username': 'carlosborba', 'tweets': ['Something', 'Something else', 'nothing']},
 {'username': 'isananda', 'tweets': ['Something', 'Something else']},
 {'username': 'gal0909', 'tweets': []},
 {'username': 'zeca_#', 'tweets': []},
 {'username': 'ed_sam', 'tweets': ['Something']},
]
print(max(users, key=lambda user: user['tweets']))

musicas = [
    {'titulo': 'Thunderstruck', 'visualizacoes': 1000230},
    {'titulo': 'Hells Bells', 'visualizacoes': 4502},
    {'titulo': 'Memento Mori', 'visualizacoes': 200},
    {'titulo': 'Bodies', 'visualizacoes': 60339},
    {'titulo': 'Fall Apart', 'visualizacoes': 522},
]
print(max(musicas, key=lambda musica: musica['visualizacoes'])['titulo'])
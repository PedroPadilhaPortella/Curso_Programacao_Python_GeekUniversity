'''
Filter
    A função filter serve para filtrar dados de uma coleção.
    Ela é uma função que recebe dois paramentros, uma função booleana e um iterável,
    que pode ser uma lista, tupla, etc... e retorna um <filter object>, que é
    Filter Object: f(a), f(b), f(c), f(d) ... sendo f() a função passada por parâmetro.
'''

import statistics


dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calcula a média
media = statistics.mean(dados)
acima_da_media = list(filter(lambda x: x > media, dados))

print(f"Média: {media}")
print(f"Valores acima da média: {acima_da_media}")

# Obs: assim como no map, após ser utilizados os dados do filter, eles são removidos da memória.


dados = ['', 'Brasil', '', '', 'Argentina', 'Colombia', '', 'Equador']

# paises = list(filter(None, dados))
paises = list(filter(lambda x: len(x) > 0, dados))

print(f"Paises: {paises}")


# Filtrar usuarios que estão inativos no twitter
users = [
 {'username': 'pedro123', 'tweets': []},
 {'username': 'carlosborba', 'tweets': ['Something', 'Something else']},
 {'username': 'isananda', 'tweets': ['Something', 'Something else']},
 {'username': 'gal0909', 'tweets': []},
 {'username': 'zeca_#', 'tweets': []},
 {'username': 'ed_sam', 'tweets': ['Something']},
]

# inactive_usernames = list(map(lambda user: user['username'], filter(lambda user: not user['tweets'], users)))
inactive_users = list(filter(lambda user: len(user['tweets']) == 0, users))
inactive_usernames = list(map(lambda user: user['username'], inactive_users))

print(f"Usuarios Inativos: {inactive_usernames}")
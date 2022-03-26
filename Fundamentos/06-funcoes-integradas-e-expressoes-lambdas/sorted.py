'''
Sorted
    sorted() -> Serve para ordenar elementos de acordo com uma expressão.

    Obs. Não confunda com o metodo sort(), o sort só funciona em Listas. 
    Podemos usar o Sorted em qualquer iterável.
'''

numeros = [1, 4, 3, 2, 5, 8, 6, 7]

print(sorted(numeros))
print(sorted(numeros, reverse=True))

# Mostrar os usuarios de acordo com quem tem mais tweets
users = [
 {'username': 'pedro123', 'tweets': []},
 {'username': 'carlosborba', 'tweets': ['Something', 'Something else']},
 {'username': 'isananda', 'tweets': ['Something', 'Something else']},
 {'username': 'gal0909', 'tweets': []},
 {'username': 'zeca_#', 'tweets': []},
 {'username': 'ed_sam', 'tweets': ['Something']},
]

print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))

# Ordenar por mais visualizadas
musicas = [
    {'titulo': 'Thunderstruck', 'visualizacoes': 1000230},
    {'titulo': 'Hells Bells', 'visualizacoes': 4502},
    {'titulo': 'Memento Mori', 'visualizacoes': 200},
    {'titulo': 'Bodies', 'visualizacoes': 60339},
    {'titulo': 'Fall Apart', 'visualizacoes': 522},
]

print(sorted(musicas, key=lambda musica: musica['visualizacoes'], reverse=True))
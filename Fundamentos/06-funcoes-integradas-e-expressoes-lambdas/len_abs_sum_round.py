'''
Len
    len() -> Função que retorna o comprimento de um iterável.
Abs
    abs() -> Função que retorna o valor absoluto de um inteiro ou real.
Sum
    sum() -> Função que retorna o maior valor de um iterável ou de dois ou mais elementos.
Round
    round() -> Função que retorna o maior valor de um iterável ou de dois ou mais elementos.

'''

from cmath import pi


musicas = [
    {'titulo': 'Thunderstruck', 'visualizacoes': 1000230},
    {'titulo': 'Hells Bells', 'visualizacoes': 4502},
    {'titulo': 'Memento Mori', 'visualizacoes': 200},
    {'titulo': 'Bodies', 'visualizacoes': 60339},
    {'titulo': 'Fall Apart', 'visualizacoes': 522},
]

# print(f"Total de Musicas: {musicas.__len__()}")
print(f"Total de Musicas: {len(musicas)}")

print(f"Abs de -100 = {abs(-100)}")

total_views = sum(map(lambda musica: musica['visualizacoes'], musicas))
print(f"Soma de todas as Views das Musicas: {total_views}")

print(f"PI Arredondado = {round(pi, 2)}")

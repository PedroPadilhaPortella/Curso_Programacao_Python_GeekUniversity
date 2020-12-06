# dicionarios são mapas ou coleções chave valor, podem conter qualquer tipo de dado, inclusive outras estruturas como tuples e listas
paises = dict()
paises = {'br': 'Brasil', 'ur': 'Reino Unido', 'us': 'Estados Unidos', 'ar': 'Argentina', 'ja' :'Jamaica'}
print(paises)

#dicionarios não sao indexados, só podem ser acessados pelas chaves

print(paises['br'], paises['ja'], paises['us'])

print(paises.get('br'), paises.get('ur'), paises.get('li', 'pais nao encontrado'))

print('br' in paises)
print('Brasil' in paises)
print('se' in paises)

coordinates = {(12.42, 17.33): 'Escritorio', (14.892, 99.81): 'Basement',  (12.89, 45.212): 'Quartil'}

print(coordinates)

#atualizar dados de um dicionario
receita = {'jan': 110, 'fev':120, 'mar': 500, 'abr': 90, 'mai': 210, 'jun': 140, 'jul': 400, 'ago': 430, 'set': 200, 'out': 80, 'nov': 120, 'dez': 700}

receita['mai'] = 1000
jun = {'jun': 300}

receita.update(jun)

# remoção de elementos de um dicionario
res = receita.pop('jan')
del receita['fev']

print(receita, res)


produto1 = {'produto': 'PS4', 'quantidade': 1, 'preco': 2000.00}
produto2 = {'produto': 'Call Of Duty MW3', 'quantidade': 1, 'preco': 90.00}
carrinho = [produto1, produto2]

print(carrinho)

#metodos de dicionarios
d = dict(a = 1, b = 2, c = 3)

e = d.copy()   #deep copy
f = d          #shallow copy

e.clear()
f.pop('a')
d['d'] = 4

print(d, e, f)

#o metodo fromkeys receb dois parametros, um iteravel e um valor, gerando chaves e valores
outro = {}.fromkeys(['nome', 'idade', 'nacionalidade'], 'desconhecido')
print(outro)
outro = {}.fromkeys('abc', 'teste')
print(outro)
outro = {}.fromkeys(range(1, 5), 'int')
print(outro)

# mapas

receita = {'jan': 110, 'fev':120, 'mar': 500, 'abr': 90, 'mai': 210, 'jun': 140, 'jul': 400, 'ago': 430, 'set': 200, 'out': 80, 'nov': 120, 'dez': 700}

for key in receita:
    print(f'{key}: {receita[key]}', end=', ')
print()

for key in receita.keys():
    print(key, end="  ")

print("\n",receita.keys())
print(receita.values())

for value in receita.values():
    print(value, end="  ")
print()

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(chave, valor, end="  ")

#podemos usar funções para encontrar Sum(), Max(), Min(), Len(), mas apenas para valores numéricos ou int
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
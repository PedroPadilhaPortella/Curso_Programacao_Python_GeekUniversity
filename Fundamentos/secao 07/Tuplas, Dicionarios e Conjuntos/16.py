notas = [
    {'nome': '', 'notas': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {'nome': '', 'notas': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {'nome': '', 'notas': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
]

gabarito = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

resultados = [
    {'nome': '', 'nota': 0, 'aprovado': 'Reprovado'},
    {'nome': '', 'nota': 0, 'aprovado': 'Reprovado'},
    {'nome': '', 'nota': 0, 'aprovado': 'Reprovado'}
]


for prova in notas:
    prova['nome'] = input(f"Nome do Aluno {prova + 1}: ")
    for questao in prova['notas']:
        questao = input(f'Questão {questao + 1} da prova {prova + 1}:')

print("\n------Gabarito dos Alunos------")
for prova in range(0, 5):
    print(f"Aluno {notas[prova]['nome']}:", end="  ")
    for questao in range (0, 10):
        print(f"[{notas[prova][questao]['nota']}]", end=" ")
    print()

for questao in range(0, 10):
        gabarito[questao] = input(f'Gabarito da questão {questao + 1}:')

print(f"\nGabarito da Prova: ", end="")
for i, e in enumerate(gabarito):
    print(f"{i}) {e};", end=" ")
print("\n")

for prova in range(0, len(notas)):
    resultados[prova]['nome'] = prova['nome']
    for questao in range (0, len(notas[prova])):
        if(gabarito[questao] == notas[prova][questao]):
            resultados[prova]['nota'] += 1
    if(resultados[prova]['nota'] >= 7):
        resultados[prova]['aprovado'] = 'Aprovado'

for aluno in enumerate(resultados):
    print(f"Resultado do Aluno {aluno['nome']}: Média: {aluno['nota']}, {aluno['aprovado']}")
print()
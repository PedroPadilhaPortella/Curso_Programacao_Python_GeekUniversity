notas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

gabarito = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

resultados = [0, 0, 0, 0, 0]

for prova in range(0, 5):
    for questao in range (0, 10):
        notas[prova][questao] = input(f'Questão {questao + 1} da prova {prova + 1}:')

print("\n------Gabarito dos Alunos------")
for prova in range(0, 5):
    print(f"Aluno {prova + 1}:", end="  ")
    for questao in range (0, 10):
        print(f"[{notas[prova][questao]}]", end=" ")
    print()

for questao in range(0, 10):
        gabarito[questao] = input(f'Gabarito da questão {questao + 1}:')

print(f"\nGabarito da Prova: ", end="")
for i, e in enumerate(gabarito):
    print(f"{i}) {e};", end=" ")
print("\n")

for prova in range(0, len(notas)):
    for questao in range (0, len(notas[prova])):
        if(gabarito[questao] == notas[prova][questao]):
            resultados[prova] += 1

for aluno, nota in  enumerate(resultados):
    print(f"Resultado do Aluno {aluno}: {nota}")
print()
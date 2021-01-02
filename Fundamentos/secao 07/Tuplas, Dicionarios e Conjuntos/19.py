aluno = {}
turma = []
media = 0
soma = 0

for i in range(5):
    aluno['matrícula'] = input(f'Matrícula {i+1}º aluno: ')
    aluno['média provas'] = float(input(f'Média das provas: '))
    aluno['média trabalhos'] = float(input(f'Média dos trabalhos: '))
    media = (aluno['média provas'] + aluno['média trabalhos']) / 2
    aluno['nota final'] = media
    turma.append(aluno.copy())

print('- ' * 15)

for aluno in turma:
    for k, v in aluno.items():
        print(f"{k.title()}: {v}")
        soma += aluno['nota final']
    print('- ' * 10)

media_arit = soma / len(turma)
print(f'\nA média da turma é {media_arit:.1f}')
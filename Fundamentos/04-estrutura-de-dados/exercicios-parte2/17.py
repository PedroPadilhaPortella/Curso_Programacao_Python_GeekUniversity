from random import randint


array = [[0 for x in range(3)] for y in range(5)]
prova1 = prova2 = prova3 = 0

for aluno in range(5):
    for nota in range(3):
        array[aluno][nota] = randint(1, 10)

for aluno in range(5):
    if array[aluno][0] < 5:
        prova1 += 1
print(f'{prova1} aluno(s) tiraram nota(s) abaixo de 5.0')

for a in range(5):
    if array[a][1] < 5:
        prova2 += 1
print(f'{prova2} aluno(s) tiraram nota(s) abaixo de 5.0')

for a in range(5):
    if array[a][2] < 5:
        prova3 += 1
print(f'{prova3} aluno(s) tiraram nota(s) abaixo de 5.0')
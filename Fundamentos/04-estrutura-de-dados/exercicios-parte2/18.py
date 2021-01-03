from random import randint


array = [[0 for x in range(3)] for y in range(3)]
soma = [0 for n in range(3)]


for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        array[i][j] = randint(-10, 10)

for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        print(f'[{array[i][j]:^5}]', end=" ")
    print()

for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        soma[i] += array[j][i]

print(' + ' * 8)
for i in range(0, len(soma)):
    print(f'[{soma[i]:^5}]', end=" ")

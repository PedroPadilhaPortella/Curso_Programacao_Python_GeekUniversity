matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maiores = []

for l in range(0, 4):
    for c in  range(0, 4):
        matriz[l][c] = int(input(f"Valor [{l}, {c}]:"))


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz)):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
        if(matriz[l][c] > 10):
            maiores.append(matriz[l][c])
    print()

print(f"\nValores maiores que 10: {maiores}")
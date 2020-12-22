from math import pow

matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        if(i < j):
            matriz[i][j] = (2*i) - (7*j) - 2
        elif(i == j):
            matriz[i][j] = (3*pow(i,2)) - 1
        else:
            matriz[i][j] = (4*pow(i,3)) - (5*pow(j,2)) + 1

        
for l in range(0, len(matriz)):
    for c in  range(0, len(matriz[l])):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
    print()
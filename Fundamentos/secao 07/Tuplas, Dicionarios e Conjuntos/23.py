from random import randint
from math import pow

A = [[randint(1, 9) for i in range(3)] for j in range(3)]

B = [[0 for i in range(3)] for j in range(3)]


for i in range(0, len(A)):
    for j in range(0, len(A)):
        B[i][j] = pow(A[i][j], 2)


for i in range(0, len(A)):
    for j in range(0, len(A)):
        print(f"[{B[i][j]:^5}]", end=" ")
    print()
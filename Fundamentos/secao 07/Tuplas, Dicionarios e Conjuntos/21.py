from random import randint


def mostrarMatriz(matriz):
    for li in range(2):
        for cm in range(2):
            print(f'{matriz[li][cm]:^5}', end="")
        print()
    print('- ' * 10)


def somar(matrizA, matrizB):
    resultado = [[0 for m in range(2)] for n in range(2)]
    for l in range(0, 2):
        for c in range(0, 2):
            resultado[l][c] = matrizA[l][c] + matrizB[l][c]
    return resultado


def subtrair(matrizA, matrizB):
    resultado = [[0 for m in range(2)] for n in range(2)]
    for l in range(0, 2):
        for c in range(0, 2):
            resultado[l][c] = matrizA[l][c] - matrizB[l][c]
    return resultado


def addConstante(num, mat1, mat2):
    r1 = [[0 for m in range(2)] for n in range(2)]
    r2 = [[0 for m in range(2)] for n in range(2)]
    for l in range(0, 2):
        for c in range(0, 2):
            r1[l][c] = mat1[l][c] + num
            r2[l][c] = mat2[l][c] + num
    return [ r1, r2 ]


# Main Program

mat1 = [[randint(1, 9) for x in range(2)] for y in range(2)]
mat2 = [[randint(1, 9) for s in range(2)] for t in range(2)]
resultado = [[0 for i in range(2)] for j in range(2)]


mostrarMatriz(mat1)
mostrarMatriz(mat2)

while True:
    opt = input('Escolha a operação:\n'
                    '[ 1 ] Somar\n'
                    '[ 2 ] Subtrair\n'
                    '[ 3 ] Adicionar Constante\n'
                    '[ 4 ] Imprimir as matrizes\n'
                    '[ 5 ] Sair\n'
                    'Digite a opção desejada: '
    )
    print('- ' * 15)

    if(opt == '1'):
        print("Somando...")
        resultado = somar(mat1, mat2)
        mostrarMatriz(resultado)

    elif(opt == '2'):
        print("Subtraindo...")
        resultado = subtrair(mat1, mat2)
        mostrarMatriz(resultado)

    elif(opt == '3'):
        num = int(input("Constante: "))
        print("Somando a uma constante...")
        [matriz1, matriz2] = addConstante(num, mat1, mat2)
        mostrarMatriz(matriz1)
        mostrarMatriz(matriz2)

    elif(opt == '4'):
        mostrarMatriz(mat1)
        mostrarMatriz(mat2)

    elif(opt == '5'):
        print('Saindo...')
        break
    
    else:
        print("Opção Inválida!")

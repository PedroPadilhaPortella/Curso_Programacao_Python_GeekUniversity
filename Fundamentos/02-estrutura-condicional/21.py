
from io import StringIO


def soma():
    print("Soma de dois Numeros")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print("{} + {} = {}".format(n1, n2, n1 + n2))

def diferenca():
    print("Diferenca de dois Numeros")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    maior = n1 if n1 > n2 else n2
    menor = n2 if n2 < n1 else n1
    print("{} - {} = {}".format(maior, menor, maior - menor))

def produto():
    print("Produto entre dois Numeros")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print("{} * {} = {}".format(n1, n2, n1 * n2))

def divisao():
    print("Divisao entre dois Numeros")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    if(n2 == 0):
        print("Divisão Impossível")
        exit()
    print("{} / {} = {}".format(n1, n2, n1 / n2))


def menu():
    print("Escolha uma opção:\n1- Soma de dois Numeros\n2-Diferença entre dois Numeros (maior pelo menor)\n3- Produto entre 2 numeros\n-4 Divisão entre 2 numeros (O denominador não pode ser zero)\n")
    option = int(input("Opção:_"))

    if(option == 1):
        soma()
    elif(option == 2):
        diferenca()
    elif(option == 3):
        produto()
    elif(option == 4):
        divisao()
    else:
        print("Operacao Inválida!")


again = True
while(again == True):
    menu()
    valid = str(input("Executar Novamente? [S/N] "))
    if(valid.upper() == "S"):
        again == True
    else:
        print("Adeus...")
        exit()

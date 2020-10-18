array = [7, 4, 12, 8, 3, 17]


while True:
    choice = int(input("Escolha uma opção:\n1) Mostra os numeros em ordem crescente\n2)Mostrar os numeros em ordem decrescente\n0)Sair\n:_"))
    if(choice == 1):
        array.sort()
        print(array)
        break
    elif(choice == 2):
        array.sort(reverse=True)
        print(array)
        break
    elif(choice == 0):
        break
    else:
        print("Opcão Invalida!")
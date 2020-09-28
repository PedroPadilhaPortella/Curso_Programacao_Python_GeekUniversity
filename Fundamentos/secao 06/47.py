from time import sleep


option = 0
while(option != 5):
    sleep(1.5)
    option = int(input("1 Adicao\n2 Subtracao\n3 Produto\n4 Divisao \n5 Sair\n:_"))
    if(option == 1):
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
        print("{} + {} = {}".format(n1, n2, n1 + n2))
    elif(option == 2):
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
        print("{} - {} = {}".format(n1, n2, n1 - n2))
    elif(option == 3):
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
        print("{} * {} = {}".format(n1, n2, n1 * n2))
    elif(option == 4):
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
        try:
            div = n1 / n2
            print("{} / {} = {:.2n}".format(n1, n2, div))
        except:
            print("Impossivel realizar uma divisão de base Nula")
sleep(0.5)
print("Saindo...")
sleep(1)
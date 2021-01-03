def multiplosEspecificos(num):
    while(True):
        if(num % 11 == 0 or num % 13 == 0 or num % 17 == 0):
            print("O Primeiro Multiplo de 11, 13 ou 17 foi {}".format(num))
            break
        num += 1


num = int(input("Insira um numero: "))
multiplosEspecificos(num)
def calcular(numero):
    if(numero >= 0):
        resultado = numero ** 2
        print("{} elevado ao quadrado = {}".format(numero, resultado))
    else:
        print("Numero Inválido")
        exit()


numero = int(input("Numero: "))
calcular(numero)
def successorAntecessor(numero):
    return [numero - 1, numero, numero + 1]

numero = int(input("Numero Inteiro:"))
array = successorAntecessor(numero)
print("O sucessor de {} é {} e o antecessor é {}".format(array[1], array[2], array[0]))
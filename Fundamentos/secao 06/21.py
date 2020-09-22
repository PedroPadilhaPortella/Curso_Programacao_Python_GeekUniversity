inicial = int(input("Valor Inicial: "))
final = int(input("Valor Final: ")) + 1
pares, arrPares = 0, []
imparesMultiplicados, arrImpares = 1, []
for i in range(inicial, final):
    if(i % 2 == 0):
        pares += i
        arrPares.append(i)
    elif(i % 2 != 0):
        imparesMultiplicados *= i
        arrImpares.append(i)
print("Soma dos Pares: {}".format(pares))
print("Array dos Pares: {}".format(arrPares))
print("Produto entre os Impares: {}".format(imparesMultiplicados))
print("Array dos Impares: {}".format(arrImpares))
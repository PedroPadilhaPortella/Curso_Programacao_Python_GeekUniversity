def converterQuilometrosToMihas(milha):
    quilometro = milha * 1.61
    print("{} milhas é igual a {} quilometros".format(milha, quilometro))

milha = float(input("Qual a distancia em milhas? "))
converterQuilometrosToMihas(milha)
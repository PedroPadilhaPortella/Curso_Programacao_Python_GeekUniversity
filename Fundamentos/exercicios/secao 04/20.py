def quilosParaLibras(kg):
    libra = kg / 0.45
    return libra


kg = float(input("Peso em Quilogramas: "))
print("O peso de {}kg é {} libs".format(kg, quilosParaLibras(kg)))
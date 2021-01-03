def calcularValorNotas(valorSaque):
    if(valorSaque >= 100):
        return 100
    elif(valorSaque >= 50):
        return 50
    elif(valorSaque >= 20):
        return 20
    elif(valorSaque >= 10):
        return 10
    elif(valorSaque >= 5):
        return 5
    elif(valorSaque >= 2):
        return 2
    elif(valorSaque >= 1):
        return 1

def concatenarResultados(contador100, contador50, contador20, contador10, contador5, contador2, contador1):
    resultado = 'Saque de.: '
    if(contador100 > 0):
        resultado += f" {contador100} nota(s) de R$ 100."
    if(contador50 > 0):
        resultado += f" {contador50} nota(s) de R$ 50."
    if(contador20 > 0):
        resultado += f" {contador20} nota(s) de R$ 20."
    if(contador10 > 0):
        resultado += f" {contador10} nota(s) de R$ 10."
    if(contador5 > 0):
        resultado += f" {contador5} nota(s) de R$ 5."
    if(contador2 > 0):
        resultado += f" {contador2} nota(s) de R$ 2."
    if(contador1 > 0):
        resultado += f" {contador1} nota(s) de R$ 1."
    return resultado

def sacarDinheiro(valorSaque):
    contador100 = 0
    contador50 = 0
    contador20 = 0
    contador10 = 0
    contador5 = 0
    contador2 = 0
    contador1 = 0
    valorNota = calcularValorNotas(valorSaque)
    while(valorSaque >= valorNota):
        if(valorNota == 100):
            contador100 += 1
            valorSaque -= 100
        elif(valorNota == 50):
            contador50 += 1
            valorSaque -= 50
        elif(valorNota == 20):
            contador20 += 1
            valorSaque -= 20
        elif(valorNota == 10):
            contador10 += 1
            valorSaque -= 10
        elif(valorNota == 5):
            contador5 += 1
            valorSaque -= 5
        elif(valorNota == 2):
            contador2 += 1
            valorSaque -= 2
        elif(valorNota == 1):
            contador1 += 1
            valorSaque -= 1
        valorNota = calcularValorNotas(valorSaque)
    return concatenarResultados(contador100, contador50, contador20, contador10, contador5, contador2, contador1)


total = sacarDinheiro(180)
print(total)
from random import *

pesoInicial1 = random()
pesoInicial2 = random()

entrada1 = int(input('Digite a primeira entrada: '))
entrada2 = int(input('Digite a segunda entrada: '))

erro = 1

while(erro != 0):
    if(entrada1 == 1 and entrada2 == 1):
        resultadoEsperado = 1
    else:
        resultadoEsperado = 0

    somatoria = pesoInicial1 * entrada1
    somatoria += pesoInicial2 * entrada2

    if(somatoria < 1):
        resultado = 0
    elif(somatoria >= 1):
        resultado = 1


    erro = resultadoEsperado - resultado

    print(f"resultado = {resultado}")
    print(f"peso inicial 1 = {pesoInicial1}")
    print(f"peso inicial 2 = {pesoInicial2}")
    print(f'erro = {erro}\n')

    pesoInicial1 = pesoInicial1 + (0.1 * entrada1 * erro)
    pesoInicial2 = pesoInicial2 + (0.1 * entrada2 * erro)

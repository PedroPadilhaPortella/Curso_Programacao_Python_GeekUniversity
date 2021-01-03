menor = 0
maior = 0
soma = 0
somaPar = 0
quant = 0
quantPar = 0
valor = 1
while(True):
    valor = int(input("Digite um valor, digite 0 para sair: "))
    if(valor == 0):
        break
    quant += 1
    soma += valor
    if(quant == 1):
        maior = valor
        menor = valor
    else:
        if(valor > maior):
            maior = valor
        if(valor < menor):
            menor = valor
    if(valor % 2 == 0):
        somaPar += valor
        quantPar += 1

try:
    media = soma / quant
except:
    media = 0
print("A soma de todos os valores foi {}, e a media deles foi {:.2f}".format(soma, media))
print("Foram lidos {} valores".format(quant))
print("O maior valor foi {}, e o menor valor foi {}".format(maior, menor))

try:
    mediaPar = somaPar / quantPar
except:
    mediaPar = 0
print("A media dos numeros pares foi {:.2f}".format(mediaPar))
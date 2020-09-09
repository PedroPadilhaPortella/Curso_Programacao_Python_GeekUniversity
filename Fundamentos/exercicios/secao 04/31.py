def reaisToDolares(reais, cotacao):
    return reais / cotacao

reais = float(input("Qual o valor em reais? "))
cotacao = float(input("Qual a cotacao atual do dolar em reais? "))
dolares = reaisToDolares(reais, cotacao)
print("R${:.2f} são US${:.2f}".format(reais, dolares))
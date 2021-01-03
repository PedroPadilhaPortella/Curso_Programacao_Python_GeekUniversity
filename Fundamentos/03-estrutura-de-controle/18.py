def estatisticas():
    maior = 0
    aumento = 0
    numeros = []
    quant = int(input("Quantos numeros serão lidos? "))
    for i in range(0, quant):
        numero = int(input(f"Numero {i + 1}: "))
        if(i == 0):
            maior = numero
        if(numero > maior):
            maior = numero
            aumento += 1
    return [maior, aumento]

maior, aumento = estatisticas()
print("O maior Numero foi {}\nO maior Numero foi alterado {} vezes.".format(maior, aumento))
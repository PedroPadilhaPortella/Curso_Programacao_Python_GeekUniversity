def aumento(salario, tempo):
    reajuste = salario
    if(salario < 500):
        reajuste *= 1.25
    elif(salario < 1000):
        reajuste *= 1.2
    elif(salario < 1500):
        reajuste *= 1.15
    elif(salario < 2000):
        reajuste *= 1.1

    if(tempo >= 10):
        reajuste += 500
    elif(tempo >= 7 and tempo < 10):
        reajuste += 300
    elif(tempo >= 4 and tempo < 7):
        reajuste += 200
    elif(tempo >= 1 and tempo < 4):
        reajuste += 100
    return reajuste

nome = input("Nome do funcionário: ")
salario = float(input(f"Qual seu salario, {nome.title()}: "))
tempo = float(input(f"Qual seu tempo de trabalho, {nome.title()}: "))
print("O reajuste salário de {} será de {:.2f}".format(nome.title(), aumento(salario, tempo)))
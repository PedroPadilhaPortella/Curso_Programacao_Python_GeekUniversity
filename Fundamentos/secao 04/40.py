def calcularSalario(dias):
    imposto = (dias * 30) * 0.08
    return dias * 30 - imposto


dias = int(input("Quantos dias trabalhados?"))
salario = calcularSalario(dias)
print("O salario de {} dias de trabalho será {:.2f}".format(dias, salario))
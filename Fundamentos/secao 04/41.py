def calcularSalario(horas, custo):
    return horas * custo * 1.1


horas = int(input("Quantas horas trabalhadas?"))
custo = float(input("Salario/Hora?"))
salario = calcularSalario(horas, custo)
print("O salario de {} horas de trabalho será {:.2f}".format(horas, salario))
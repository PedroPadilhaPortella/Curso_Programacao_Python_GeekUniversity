def calcularSalario(salario_base):
    gratificacao = salario_base * 0.05
    imposto = salario_base * 0.07
    return salario_base + gratificacao - imposto


base = float(input("Salario-Base? R$"))
salario = calcularSalario(base)
print("O salario de com gratificacao e impostos será de {:.2f}".format(salario))
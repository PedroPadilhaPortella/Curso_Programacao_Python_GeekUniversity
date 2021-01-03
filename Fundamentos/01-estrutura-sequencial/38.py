def aumento(salario):
    return salario * 1.25

salario = float(input("Qual o salario do funcionario? R$ "))
print("O salario com aumento será de {:.2f}".format(aumento(salario)))
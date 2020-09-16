def emprestimo(sal, emp):
    if(emp > (sal * 0.2)):
        return 'Emprestimo Negado'
    else:
        return 'Emprestimo Concedido'

nome = input("Nome do Funcionario: ")
salario = float(input("Salario: "))
prestacao = float(input("Prestação: "))
status = emprestimo(salario, prestacao)
print(status + f" para {nome}")
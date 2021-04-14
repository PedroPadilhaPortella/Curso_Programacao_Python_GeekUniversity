def calcular(n1, n2, operator):
    if(operator in '+'):
        return n1 + n2
    elif(operator in '-_'):
        return n1 - n2
    elif(operator in '/%'):
        if(n2 == 0): return 0
        return n1 / n2
    elif(operator in '*xX'):
        return n1 * n2


n1 = float(input("Digite o primeiro valor: "))
op = input("Digite a operacao [+ - / *]: ")
n2 = float(input("Digite o segundo valor: "))
resultado = calcular(n1, n2, op)
print(f"{n1} {op} {n2} = {resultado}")
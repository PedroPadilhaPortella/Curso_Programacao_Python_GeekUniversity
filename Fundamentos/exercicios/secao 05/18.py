def calculadora(a, b, operation):
    if(operation == "+"):
        return a + b
    elif(operation == "-"):
        return a - b
    elif(operation == "*"):
        return a * b
    elif(operation == "/"):
        if(b == 0):
            print("Operacao de divisão por 0 Inválida!")
            exit()
        return a / b


a = float(input("Valor 1: "))
op = input("Operacao: ")
b = float(input("Valor 2: "))
print(f"Operacao em execução....\n:  {a} {op} {b}")
resultado = calculadora(a, b, op)
print(f"{a} {op} {b} = {resultado}")
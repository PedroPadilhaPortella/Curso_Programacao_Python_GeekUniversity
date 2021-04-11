def verificar_inteiros(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

values = [1, -1, 0, 98, -12, 31]
print("Integridade do Valor (1 = positivo, -1 = negativo, 0 = nulo)")
for i in values:
    print(f"Valor: {i} - Integridade: {verificar_inteiros(i)}")
from math import pow

def calcularRendimento(inicial, quant, taxa, tempo):
    total = inicial
    for meses in range(1, tempo + 1):
        print(f"mes {meses}")
        total += quant + quant * taxa
    return total


inicial = float(input("Quanto será o capital inicial? "))
quant = float(input("Quanto será aplicado ao mes? "))
taxa = float(input("Qual sera a taxa de rendimento? "))
tempo = int(input("Qual será o tempo do resgate? "))
total = calcularRendimento(inicial, quant, taxa, tempo)
print("R${:.2f}".format(total))
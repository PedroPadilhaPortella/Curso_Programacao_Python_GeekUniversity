def dividirPremio(premio, p1, p2, p3):
    investimento = p1 + p2 + p3
    part1 = premio / (investimento / p1)
    part2 = premio / (investimento / p2)
    part3 = premio / (investimento / p3)
    return [part1, part2, part3]

nome1 = input("Nome do amigo 1: ")
p1 = float(input(f"Investimento do {nome1}: R$"))
nome2 = input("Nome do amigo 2: ")
p2 = float(input(f"Investimento do {nome2}: R$"))
nome3 = input("Nome do amigo 3: ")
p3 = float(input(f"Investimento do {nome3}: R$"))
premio = float(input("Premio da Loteria: R$"))

[part1, part2, part3] = dividirPremio(premio, p1, p2, p3)

print("\n\nPremio do {}: R${:.2f}".format(nome1, part1))
print("Premio do {}: R${:.2f}".format(nome2, part2))
print("Premio do {}: R${:.2f}".format(nome3, part3))
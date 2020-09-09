def premiacao(premio):
    premio1 = premio * 0.46
    premio -= premio1
    premio2 = premio * 0.32
    premio -= premio2
    premio3 = premio
    return [premio1, premio2, premio3]


premio = 780000.00
resultados = premiacao(premio)
print("1° colocado => R${:.2f}\n2° colocado => R${:.2f}\n3° colocado => R${:.2f}".format(resultados[0], resultados[1], resultados[2]))

print("Total => R${:.2f}".format(resultados[0] + resultados[1] + resultados[2]))
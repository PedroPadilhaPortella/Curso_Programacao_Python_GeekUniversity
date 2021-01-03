reais = list()
for r in range(0, 10):
    reais.append(float(input("Insira um valor real: ")))
print(reais)

somaPos = 0
quantNeg = 0
for real in reais:
    if(real >= 0):
        somaPos += real
    else:
        quantNeg += 1

print("Há {} valores negativos e a soma dos positivos é {:.2f}".format(quantNeg, somaPos))
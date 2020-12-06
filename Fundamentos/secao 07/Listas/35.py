a = 1814
b = 1945

stra = str(a)
strb = str(b)

vetora = list()
vetorb = list()
soma = []

for i in stra:
    vetora.append(int(i))
print(vetora)

for i in strb:
    vetorb.append(int(i))
print(vetorb)

for i, e in enumerate(vetora):
    soma.append(vetora[i] + vetorb[i])

print(soma)
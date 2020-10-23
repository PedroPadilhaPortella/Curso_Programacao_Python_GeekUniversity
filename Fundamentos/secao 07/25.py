lista = []
c = 0
i = 0
while(c < 100):
    i += 1
    if((str(i))[-1] == '7'):
        continue
    if(i % 7 == 0):
        continue
    lista.append(i)
    c += 1
    if(c == 100):
        break

print(lista)
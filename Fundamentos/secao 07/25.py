lista = []
c = 0
i = 0
while(c < 100):
    if((i % 7 == 0) or ((str(i))[-1]) == '7'):
        continue
    lista.append(i)
    i += 1
    c += 1
    if(c == 100):
        break

print(lista)
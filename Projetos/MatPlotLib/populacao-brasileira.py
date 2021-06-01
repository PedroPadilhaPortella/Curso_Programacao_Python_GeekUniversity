'''
    Crescimento Populacional Brasileiro (1980-2016)
'''
import matplotlib.pyplot as plt

title = 'Crescimento Populacional Brasileiro (1980-2016)'

x = []
y = []
dados = open('populacao_brasileira.csv').readlines()

for i in range(len(dados)):
    if(i != 0):
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title(title)
plt.ylabel('Ano')
plt.xlabel('População')

plt.plot(x, y, color="blue", linestyle='--')
plt.bar(x, y, color="#e4e4e4")
plt.grid()

# plt.show()
plt.savefig('populacao-brasileira.png', dpi=300)
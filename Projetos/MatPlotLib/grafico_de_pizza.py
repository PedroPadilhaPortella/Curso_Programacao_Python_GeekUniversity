import matplotlib.pyplot as plt

label = ['Amazonia', 'Caatinga', 'Cerrado', 'Mata Atlântica', 'Pampa', 'Pantanal']
dados = [49, 24, 13, 10, 2, 2]

fig, ax = plt.subplots()
ax.pie(dados, labels=label, autopct="%2.f%%")
plt.show()
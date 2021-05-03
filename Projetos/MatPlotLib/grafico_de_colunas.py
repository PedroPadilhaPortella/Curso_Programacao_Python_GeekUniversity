import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12, 14, 16, 18]
y = [6, 9, 14, 18, 20, 18, 9, 5, 3]

plt.bar(x, y, label = "Meninos", color="blue")

x = [1, 3, 5, 7, 9, 11, 13, 15, 17]
y = [1, 3, 10, 13, 15, 14, 11, 6, 5]

plt.bar(x, y, label = "Meninas", color="red")

plt.ylabel('Idades')
plt.xlabel('Quantidade de Alunos')
plt.title("Idade dos Alunos do IEMS")
plt.legend()
plt.show()
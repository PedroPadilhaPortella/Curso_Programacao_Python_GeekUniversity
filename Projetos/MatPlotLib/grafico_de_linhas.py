import matplotlib.pyplot as plt

plt.plot([12, 13, 14, 15, 16, 17, 18, 19, 20], [6, 9, 14, 18, 20, 18, 9, 5, 3], label = "Meninos", color="red", linestyle="solid")
plt.plot([12, 13, 14, 15, 16, 17, 18, 19, 20], [1, 3, 10, 13, 15, 14, 11, 6, 5], label = "Meninas", color="blue", linestyle="solid")

plt.ylabel('Idades')
plt.xlabel('Quantidade de Alunos')
plt.title("Idade dos Alunos do IEMS")
plt.legend()
plt.show()
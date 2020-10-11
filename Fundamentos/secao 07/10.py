notas = list()
for i in range(0, 15):
    notas.append(float(input(f"Nota {i}:")))
print(notas)

soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print("Media Geral: {:.2f}".format(media))
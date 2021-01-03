def media(n1, n2):
    if(n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10):
        print("Notas Inválidas")
        exit()
    else:
        media = (n1 + n2) / 2
        return media

nome = input("Nome do Aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
print("Media do {}: {:.1f}".format(nome, media(nota1, nota2)))
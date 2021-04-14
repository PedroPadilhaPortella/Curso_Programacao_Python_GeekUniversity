def media_aritmetica(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def media_ponderada(nota1, nota2, nota3):
    return ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5 + 3 + 2)


def calcular_media(nota1, nota2, nota3, tipo):
    media = 0
    if(tipo in 'Aa'):
        media = media_aritmetica(nota1, nota2, nota3)
    elif(tipo in 'Pp'):
        media = media_ponderada(nota1, nota2, nota3)
    return media


aluno = input("Calculo de Média\nNome do Aluno:")
nota1 = float(input("Nota1:"))
nota2 = float(input("Nota2:"))
nota3 = float(input("Nota3:"))
tipo = input("Média Aritmética [A] / Média Ponderada [P]: ")
if(tipo in 'PpAa'):
    media = calcular_media(nota1, nota2, nota3, tipo)
    print(f"A média do Aluno {aluno} é {media}")
else:
    print("Opção de Média Inválida")
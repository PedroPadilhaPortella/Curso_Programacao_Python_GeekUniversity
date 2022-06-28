'''
    Escrevendo arquivos CSV (Comma Separated Values)

    writer -> Permite persistir linhas em um arquivo csv
    DictWriter -> Permite que iteremos pelas linhas do arquivo como OrderedDicts
'''
from csv import writer, DictWriter

# with open('filmes.csv', 'w', newline='') as file:
#     escritor_csv = writer(file)
#     filme = None
#     escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
#     while filme != 'sair':
#         filme = input('Digite o titulo: ')
#         if(filme != 'sair'):
#             genero = input('Digite o genero: ')
#             duracao = input('Digite a duracao: ')
#             escritor_csv.writerow([filme, genero, duracao])

with open('filmes.csv', 'w', newline='') as file:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(file, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Digite o titulo: ')
        if(filme != 'sair'):
            genero = input('Digite o genero: ')
            duracao = input('Digite a duracao: ')
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao': duracao})
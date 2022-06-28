'''
    Lendo arquivos CSV (Comma Separated Values)

    reader -> Permite que iteremos pelas linhas do arquivo como listas
    DictReader -> Permite que iteremos pelas linhas do arquivo como OrderedDicts
'''
from csv import reader, DictReader

# with open('lutadores.csv') as file:
#     leitor_csv = reader(file, delimiter=',')
#     print(type(leitor_csv)) # Tipo do Leitor
#     next(leitor_csv) # Pula o cabecalho
#     for linha in leitor_csv:
#         print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} cms')


with open('lutadores.csv') as file:
    leitor_csv = DictReader(file, delimiter=',')
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['Pais']} e mede {linha['Altura (em cm)']} cms")
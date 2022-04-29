filename = input('Digite o nome do arquivo: ')

try:
    file = open(filename, 'r')
    print(f"O arquivo possui {len(file.readlines())} linhas.")
except:
    print('Arquivo não encontrado')
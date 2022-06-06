import re


filename = input('Digite o nome do arquivo: ')

try:
    file = open(filename, 'r')
    texto = file.read()
    vowels = re.findall('[aeiouAEIOU]', texto)
    print(f"O arquivo {filename} contém {len(vowels)} vogais.")
except:
    print('Arquivo não encontrado')
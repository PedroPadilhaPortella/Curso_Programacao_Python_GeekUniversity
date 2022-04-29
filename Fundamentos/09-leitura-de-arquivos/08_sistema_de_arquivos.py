'''
    Sistema de Arquivos e Navegação

'''

import os
import tempfile
import send2trash

print(os.path.exists('arquivo.txt'))
print(os.path.exists('frutas.txt'))
print(os.path.exists('files'))

with open('arquivo.txt', 'w') as arquivo:
    pass

# os.remove('arquivo.txt') # Remove o arquivo

send2trash.send2trash('arquivo.txt') # Move o arquivo para a lixeira

# Trabalhando com diretorios e arquivos temporarios

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretorio temporario em: {tmp}')
    with open(os.path.join(tmp, 'arquivo.txt'), 'w') as arquivo:
        arquivo.write('Teste')
    input()
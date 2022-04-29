# -*- coding: utf-8 -*-
'''
Escrita de Arquivos

    - O método write() é usado para escrever dados em um arquivo, ele recebe um parâmetro, 
    que é o dado que será escrito e não retorna nada.
'''

with open('escrita.txt', 'w') as arquivo:
    arquivo.write('primeira linha\n')
    arquivo.write('segunda linha\n')
    arquivo.write('terceira linha\n')

with open('frutas.txt', 'w') as file:
    while True:
        fruta = input('Inform uma fruta o digite SAIR para sair: ')
        if fruta == 'SAIR':
            break
        file.write(fruta + '\n')
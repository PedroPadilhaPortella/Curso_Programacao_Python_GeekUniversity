s# -*- coding: utf-8 -*-
'''
Modos de Abertura de Arquivos

    r - abre para leitura
    w - abre para escrita, cria um arquivo novo se não existir
    a - abre para escrita, adiciona o conteúdo ao final do arquivo se não existir
    x - abre para escrita, cria um arquivo novo se não existir, caso exista uma exceção
    r+ - abre para leitura e escrita
    w+ - abre para leitura e escrita, cria um arquivo novo se não existir
    a+ - abre para leitura e escrita, adiciona o conteúdo ao final do arquivo se não existir
    x+ - abre para leitura e escrita, cria um arquivo novo se não existir, caso exista uma exceção
'''

with open('frutas.txt', 'a') as file:
    while True:
        fruta = input('Inform uma fruta o digite SAIR para sair: ')
        if fruta.upper() == 'SAIR':
            break
        file.write(fruta + '\n')
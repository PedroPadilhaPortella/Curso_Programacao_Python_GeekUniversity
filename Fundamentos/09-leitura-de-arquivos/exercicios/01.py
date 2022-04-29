with open('arq.txt', 'w') as arquivo:
    while(True):
        print('Digite uma frase, 0 para sair:')
        frase = input()
        if(frase == '0'):
            break
        arquivo.write(frase)
        arquivo.write('\n')
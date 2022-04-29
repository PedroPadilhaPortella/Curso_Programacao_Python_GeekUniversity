'''
Bloco With

    O bloco with é usado para abrir e fechar recursos de forma mais eficiente.

    - Abrimos um arquivo com o método open()
    - Dentro do bloco with, abrimos o arquivo com o método open()
    - Dentro do bloco with, podemos fazer operações com o arquivo
    - Fechamos o arquivo com o método close()
'''

with open('file.txt', 'r') as arquivo:
    print(arquivo.read())
    print("Arquivo está fechado? " + str(arquivo.closed))

print("Arquivo está fechado? " + str(arquivo.closed))
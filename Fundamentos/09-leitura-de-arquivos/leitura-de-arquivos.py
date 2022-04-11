'''
Leitura de Arquivos
    Ler arquivos de texto e gravar os dados em um dicionário.

    open() -> função que abre um arquivo para leitura e escrita. Retorna um objeto do tipo file.
    Retorna um _io.TextIOWrapper se o arquivo for do tipo texto.
        Ex: <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
    Se não encontrar o arquivo, retorna um FileNotFoundError. 
        Ex: FileNotFoundError: [Errno 2] No such file or directory: 'filae.txt'

    read() -> função que retorna o conteúdo do arquivo.
    readlines() -> função que retorna uma lista com as linhas do arquivo.
'''

file = open('file.txt', mode='r', encoding='cp1252')
print(file.readlines())

file = open('file.txt')
print("Qauntidade de linhas: ", len(file.read().split('\n')))

file = open('file.txt')
print(file.read())
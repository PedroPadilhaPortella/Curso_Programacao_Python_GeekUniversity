'''
Seek e Cursors
    
    seek() - usada para movimentar o cursor pelo arquivo
'''

file = open('file.txt')

print(file.read()) # lê o arquivo inteiro

file.seek(0) # volta para o inicio do arquivo
print(file.readline()) # lê a primeira linha

file.seek(0) # volta para o inicio do arquivo
print(file.readlines()) # lê todas as linhas e retorna uma lista

file.seek(0)
print(file.read(2)) # lê 2 caracteres

file.close()
print("Arquivo está fechado? " + str(file.closed)) # verifica se o arquivo está fechado
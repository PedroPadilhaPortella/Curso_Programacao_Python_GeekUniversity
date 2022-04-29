'''
String I/O

    Permite manipular um arquivo sem precisar abrir e fechar ele ou ter as permições de acesso,
    escrita ou edição.
    O arquivo é criado apenas em memória, e não é salvo em disco.
'''

from io import StringIO


message = 'um arquivo em memória'
file = StringIO(message)  # Criar um arquivo em Memória

print(file.read())

file.seek(0)

file.write('\nOutra linha')

print(file.read())
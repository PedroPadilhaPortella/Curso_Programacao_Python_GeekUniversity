filename = input('Digite o nome do arquivo: ')

try:
    file = open(filename, 'r')
    texto = file.read()
    print(f"O arquivo {filename} contém {texto.count(['a', 'e', 'i', 'o', 'u'])} caracteres.")
except:
    print('Arquivo não encontrado')
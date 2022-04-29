'''
    Sistema de Arquivos e Navegação
    os
    os.getcwd() - Retorna o diretório atual
    os.chdir() - Altera o diretório atual
    os.listdir() - Lista os arquivos e diretórios do diretório atual
    os.path.join() - Junta dois caminhos de diretório
    os.path.split() - Separa o caminho do nome do arquivo
    os.path.exists() - Verifica se o arquivo ou diretório existe
    os.path.isfile() - Verifica se o arquivo existe
    os.path.isdir() - Verifica se o diretório existe
    os.path.abspath() - Retorna o caminho absoluto
    os.path.basename() - Retorna o nome do arquivo
    os.path.dirname() - Retorna o nome do diretório
    os.path.realpath() - Retorna o caminho real
    os.path.getsize() - Retorna o tamanho do arquivo
    os.path.getmtime() - Retorna a data de modificação do arquivo
    os.path.getatime() - Retorna a data de acesso do arquivo
    os.path.getctime() - Retorna a data de criação do arquivo

    platform
    platform.system() - Retorna o sistema operacional
    platform.release() - Retorna a versão do sistema operacional
    platform.version() - Retorna a versão do kernel
    platform.machine() - Retorna o tipo de máquina
    platform.processor() - Retorna o tipo de processador
    platform.python_version() - Retorna a versão do python
    platform.python_compiler() - Retorna o compilador do python
    platform.python_build() - Retorna a data de compilação do python
    platform.python_branch() - Retorna a versão do branch do python
    platform.python_revision() - Retorna a versão do revision do python
'''

import os
import platform
import sys

os.chdir('..')
print(f"Path Absoluto: {os.getcwd()}")

print('Arquivos no diretório:')
for i in os.listdir():
    print(i)

print(os.path.isabs("C:\\Users\\User"))

print(f"OS Name: {os.name}")
print(f"Plataforma: {sys.platform}")
print(f"Versão do python: {sys.version}")
print(f"Versão do : {sys.executable}")
print(f"Versão da API: {sys.api_version}")
print(f"Máquina: {platform.machine()}")
print(f"Processador: {platform.processor()}")
print(f"Sistema Operacional: {platform.system()}")
print(f"Versão do Sistema: {platform.version()}")
print(f"Implementação do Python: {platform.python_implementation()}")

print("Versões do Python:", end=' ')
for atr in platform.python_version_tuple():
    print(atr, end='; ')
class Pessoa:
 
    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
 
    def exibe(self, num=None):
        if num == 1:
            print(f'Nome: {self.__nome}, Idade: {self.__idade}, Codigo: {self.__codigo}')
        else:
            print(f'Nome: {self.__nome}, Codigo: {self.__codigo}')
 
 

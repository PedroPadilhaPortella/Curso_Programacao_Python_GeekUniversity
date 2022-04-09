elf.__nome = nome
        self.__idade = idade
        self.__codigo = codigo
 
    @classmethod
    def instanciar(cls):
        tipo_pessoa1 = cls('vitor', 19, 122573)
        return tipo_pessoa1
 
    def exibe(self, num=None):
        if num == 1:
            print(f'Nome: {self.__nome}, Idade:{self.__idade}, Codigo: {self.__codigo}')
        else:
            print(f'Nome: {self.__nome}, Codigo: {self.__codigo}')
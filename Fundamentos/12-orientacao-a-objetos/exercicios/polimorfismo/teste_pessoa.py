from pessoa import Pessoa


class TestePessoa:
    def __main__():
        pessoa1 = Pessoa(123, 'vitor', 19)
        pessoa1.exibe()
        pessoa1.exibe(1)
        pessoa1.exibe(2)
 
 
if __name__ == '__main__':
    TestePessoa.__main__()
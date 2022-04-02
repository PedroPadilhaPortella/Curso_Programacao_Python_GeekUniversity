'''
Métodos de Classe e Métodos de Instância
    
    Os Métodos de Classe são aqueles metodos que podem ser chamados 
  sem precisar de uma instância de classe para ser executado. 

    Já os Métodos de Instância são aqueles que precisam de uma instância de classe para ser executado.

    Há também os metodos Estáticos, que são aqueles que não tem acesso nem a classe e nem a instancia da classe.

    Os Métodos também podem ser públicos ou privados.

'''
from passlib.hash import sha256_crypt


# Classe Produto
class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor): 
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return self.__valor * (100 - porcentagem) / 100


p1 = Produto('Playstation 4', 'Video Game', 2400)
print(p1.desconto(50))   # print(p1.desconto(p1, 50))



# Classe Usuario
class Usuario:
    contador = 0

    @classmethod
    def get_total_contas(cls):
        return "Total de contas: " + str(cls.contador)

    @staticmethod
    def static_method_test():
        return "TESTE METODO ESTATICO - SEM ESTANCIA DO OBJETO NEM A CLASSE"

    def __init__(self, nome, sobrenome, email, senha):
        Usuario.contador = Usuario.contador + 1
        self.__id = Usuario.contador
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = sha256_crypt.hash(senha, rounds=20000, salt_size=16)
        print(f"Bem Vindo, usuário {self.__gerar_usuario()}")
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        return sha256_crypt.verify(senha, self.__senha)

    def __gerar_usuario(self):
        return self.__email.split('@')[0]


print(Usuario.static_method_test())

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
confirmSenha = input('Confirme sua senha: ')

if(senha == confirmSenha):
    user1 = Usuario(nome, sobrenome, email, senha)
    print(Usuario.get_total_contas())
    print(user1.nome_completo())
else:
    print('Senhas não conferem!')
    exit(0)

senha = input('Digite sua senha para Login: ')

if(user1.checar_senha(senha)):
    print('Login efetuado com sucesso!')
else:
    print('Senha incorreta!')
    exit(0)

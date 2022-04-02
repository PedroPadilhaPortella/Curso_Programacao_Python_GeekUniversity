'''
    POO é um paradigma de programação que visa mapear objetos do mundo real para modelos computacionais.

    Paradigma de programação: metodologia para representar e desenvolder programas computacionais.

    Principais Elementos:
    - Classes: modelos computacionais para representar e desenvolder programas computacionais.
    - Objetos: instâncias de classes.
    - Atributos: características de um objeto.
    - Métodos: funções que podem ser acessadas diretamente pelo objeto.
    - Construtor: função que é executada quando um objeto é criado.

'''

# Classe Lampada
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

lampada1 = Lampada(220, 'amarela')
print(type(lampada1).__name__)   # nome do tipo da classe 
print(type(lampada1).__module__) # modulo em que a classe se encontra
print(type(lampada1).__bases__)  # classe pai


# Classe Usuario
class Usuario:
    def __init__(this, nome, email, senha):
        this.nome = nome
        this.email = email
        this.senha = senha


# Classe ContaCorrente
class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

    def saque(self, valor):
        self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor

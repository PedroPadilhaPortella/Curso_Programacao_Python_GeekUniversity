'''
    Herança (Inheritance)

    A ideia de herança é que uma classe filha herda todos os atributos e métodos de uma classe pai.
    A classe filha herda todos os atributos e métodos da classe pai, mas pode sobrescrever os métodos que desejar.
    A classe filha pode adicionar novos atributos e métodos.

    OBS: A herança é uma relação de composição, não é uma relação de agregação.
    O Python possui herança múltipla.
'''

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula

    def nome_completo(self):
        return super().nome_completo() + " - Matrícula: " + str(self.matricula)


cliente1 = Cliente("João", "da Silva", "123.456.789-10", 2000)
funcionario1 = Funcionario("Maria", "da Silva", "987.654.321-10", 3000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
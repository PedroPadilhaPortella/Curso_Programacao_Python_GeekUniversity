# Atributos Publicos e Privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.__senha


user = Acesso('user@email.com', 'user@1234')
print(user.email) # Atributo Publico
# print(user.__senha) # Atributo Privado
print(user._Acesso__senha) # Name Mangling de um Atributo Privado

print(user.get_email()) # Metodo Getter da Senha
print(user.get_senha()) # Metodo Getter da Senha



# Atributos de Classe e Atributos de Instância
# Os atributos de classe também são chamados de atributos estáticos, como em Java.
class Produto:
    imposto = 0.05
    contador = 0

    def __init__(self, nome, descricao, valor): 
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


produto1 = Produto('Notebook', 'Notebook Lenovo Ideapad', 2999.90)
produto2 = Produto('Notebook', 'Notebook Lenovo Ideapad', 2999.90)
produto3 = Produto('Notebook', 'Notebook Lenovo Ideapad', 2999.90)

print(produto1.nome) # Atributos de Instância
print(Produto.imposto) # Atributos de Classe

print(produto1.id)
print(produto2.id)
print(produto3.id)
print(Produto.contador)

# Atributos Dinamicos -> Atributos de Instancia que podem ser criados em tempo de execução
produto3.marca = 'Lenovo'
print(produto3.marca)


# Remover Atributos de Instância
del produto2.nome; del produto2.descricao; del produto2.valor; del produto2.id

# Transformando Classes em Dicionarios
print(produto1.__dict__)
print(produto2.__dict__)
print(produto3.__dict__)
import datetime

nascimento = int(input("Qual seu ano de nascimento? "))
atual = datetime.datetime.now().year
idade = atual - nascimento
print(f"Sua idade em {atual} é de {idade} anos")
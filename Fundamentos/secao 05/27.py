from datetime import date

nome = input("Nome: ")
nascimento = int(input("Ano de nascimento:"))
atual = date.today().year
idade = atual - nascimento
categoria = 'none'

if(idade > 5 and idade <= 7):
    categoria = 'Infantil A'
elif(idade > 7 and idade <= 10):
    categoria = 'Infantil B'
elif(idade > 10 and idade <= 13):
    categoria = 'Juvenil A'
elif(idade > 13 and idade <= 17):
    categoria = 'Juvenil B'
elif(idade > 18):
    categoria = 'Senior'

print("A categoria de {} é {}".format(nome, categoria))
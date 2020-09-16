import random
from time import sleep
from math import trunc

nota = 0

def dividendos():
    div = []
    for i in range(1, 100):
        if(i % 2 == 0):
            div.append(i)
        if(i % 3 == 0):
            div.append(i)
        if(i % 5 == 0):
            div.append(i)
        if(i % 7 == 0):
            div.append(i)
        if(1 % 11 == 0):
            div.append(i)
    return div


def questao(questao):
    global nota
    print("\n\nQuestão {}".format(questao))
    op = random.randint(1, 4)
    resultado = 0
    a = 0
    b = 0
    if(op == 1):
        op = '+'
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        resultado = a + b
    elif(op == 2):
        op = '-'
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        resultado = a - b
    elif(op == 3):
        op = '*'
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        resultado = a * b
    elif(op == 4):
        op = '/'
        a = random.choice(dividendos())
        b = random.randint(1, 10)
        resultado = trunc(a / b)
    
    resposta = float(input("{} {} {} = ".format(a, op, b)))
    print("Corrigindo...")
    sleep(1)
    if(resposta == resultado):
        print("Parabéns, Você acertou!")
        nota += 1
    else:
        print("Essa você errou, a resposta era {}".format(resultado))
    sleep(1)



questoes = int(input("Prova de Matemática\n------------------\nQuantas questões terá a prova? "))

for i in range(1, questoes + 1):
    questao(i)

nota = nota * 10 / questoes

if(nota >= 7):
    cor = "0;32m"
elif(nota < 7 and nota >= 5):
    cor = "0;33m"
else:
    cor = "0;31m"

print("\n{}\nSua Nota foi \033[{}{:.2f}\033[m".format("-" * 30,cor ,nota))
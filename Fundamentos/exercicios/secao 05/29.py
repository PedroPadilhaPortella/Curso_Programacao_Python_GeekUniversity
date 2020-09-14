import random
from time import sleep

nota = 0

def questao(questao):
    global nota
    print("\n\nQuestão {}".format(questao))
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    soma = a + b
    resultado = int(input("Qual a soma entre {} e {}? ".format(a, b)))
    print("Corrigindo...")
    sleep(2)
    if(soma == resultado):
        print("Parabéns, Você acertou!")
        nota += 1
    else:
        print("Essa você errou, a resposta era {}".format(soma))
    sleep(2)

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
print("\n{}\nSua Nota foi \033[{}{}\033[m".format("-" * 30,cor ,nota))
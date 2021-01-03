from random import randint


aleatorio = randint(1, 1000)
user = 0
chutes = 0

while(aleatorio != user):
    user = int(input("Chute um numero: "))
    if(user > aleatorio):
        print("É menor")
    if(user < aleatorio):
        print("É maior")
    chutes += 1

print("Parabens, vc acertou, era {}".format(aleatorio))
print("Foram necessários {} chutes".format(chutes))
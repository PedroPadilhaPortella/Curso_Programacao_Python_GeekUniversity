from random import sample

cartela = sample(range(0, 99), 25)

print("----Bingo do Seu Jorge----")
for i, numero in enumerate(cartela):
    if(i % 5 == 0):
        print()
    print(f"[{numero: ^5}]", end=" ")

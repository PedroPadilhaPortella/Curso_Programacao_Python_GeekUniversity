from random import randint

def lancarDados():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    relacao = ""
    if(d1 > d2):
        relacao = ">"
    elif(d1 < d2):
        relacao = "<"
    else:
        relacao = "="
    print(f"{d1} {relacao} {d2}")

n = int(input("Quantos lançamentos serão feitos? "))
print("D1-D2")
for i in range(0, n):
    lancarDados()
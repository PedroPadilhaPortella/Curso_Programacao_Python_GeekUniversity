valor = 89
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

total = valor

while(total >= 100):
    nota100 += 1
    total = total - 100

while(total >= 50):
    nota50 += 1
    total = total - 50

while(total >= 20):
    nota20 += 1
    total = total - 20

while(total >= 10):
    nota10 += 1 
    total = total - 10

while(total >= 5):
    nota5 += 1
    total = total - 5

while(total >= 2):
    nota2 += 1
    total = total - 2

while(total >= 1):
    nota1 += 1
    total = total - 1

print(valor)
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")

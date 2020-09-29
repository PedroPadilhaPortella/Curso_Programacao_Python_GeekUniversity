from datetime import date


salario = 2000
ano = 1995
aumento = 0
while(ano <= date.today().year):
    aumento = aumento * 2
    salario += salario * aumento
    if(ano == 1996):
        aumento = 0.015
    ano += 1

print("Salario Atual: R$ {:.2f}".format(salario))
print("Puta salario einh?")
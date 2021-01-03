dia = int(input("Mês: "))
month = 0

if (dia == 1):
    month = "Janeiro"
elif (dia == 2):
    month = "Fevereiro"
elif (dia == 3):
    month = "Março"
elif (dia == 4):
    month = "Abril"
elif (dia == 5):
    month = "Maio"
elif (dia == 6):
    month = "Junho"
elif (dia == 7):
    month = "Julho"
elif (dia == 8):
    month = "Agosto"
elif (dia == 9):
    month = "Setembro"
elif (dia == 10):
    month = "Outubro"
elif (dia == 11):
    month = "Novembro"
elif (dia == 12):
    month = "Dezembro"
else:
   month = "mês 13, entao lascou kkk"

print(f"Hoje é {month}")
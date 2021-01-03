dia = int(input("Dia da semana: "))
weekday = 0
if (dia == 1):
    weekday = "Domingo"
elif (dia == 2):
    weekday = "Segunda-feira"
elif (dia == 3):
    weekday = "Terça-feira"
elif (dia == 4):
    weekday = "Quarta-feira"
elif (dia == 5):
    weekday = "Quinta-feira"
elif (dia == 6):
    weekday = "Sexta-feira"
elif (dia == 7):
    weekday = "Sábado"
else:
   weekday = "nenhum dia da semana, voce esta em um loop colocado pelo Castiel!"

print(f"Hoje é {weekday}")
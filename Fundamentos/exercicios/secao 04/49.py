horaI = int(input("Hora inicial "))
minutoI = int(input("Minuto inicial "))
segundoI = int(input("Segundo inicial "))
hourLong = int(input("Duracao de horas "))
minLong = int(input("Duracao de minutos"))
segLong = int(input("Duracao de segundos "))

finalHour = horaI + hourLong
finalMinute = minutoI + minLong
finalSecond = segundoI + segLong
while(int(finalSecond) >= 60):
    finalSecond -= 60
    finalMinute += 1
while(int(finalMinute) >= 60):
    finalMinute -= 60
    finalHour += 1

print("{}\nHorario do fim do esperimento:\n{}:{}:{}".format('==' * 10,finalHour, finalMinute, finalSecond))
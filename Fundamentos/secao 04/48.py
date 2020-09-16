def convertToTime(segs):
    horas = 0
    minutos = 0
    while(segs >= 360):
        segs -= 360
        horas += 1
    while(segs >= 60):
        segs -= 60
        minutos += 1
    return [horas, minutos, segs]



segs = int(input("Quantos segundos? "))
[horas, minutos, segundos] = convertToTime(segs)
print("{} segs são {} horas, {} minutos e {} segundos".format(segs, horas, minutos, segundos))
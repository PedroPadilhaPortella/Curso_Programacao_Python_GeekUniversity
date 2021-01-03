n = 1
while(n != 0):
    n = int(input(f'''{'='*30}\n1 Converter km/h para m/s\n2 Converter m/s para km/h\n0 Sair\n:_'''))
    if(n == 1):
        km = float(input("Distancia em quilometros: "))
        h = float(input("Horas: "))
        kmh = km/h
        ms = kmh / 3.6
        print("{:1n} km/h são {:.2n} m/s".format(kmh, ms))
    elif(n == 2):
        m = float(input("Distancia em metros: "))
        s = float(input("Segundos: "))
        ms = m/s
        kmh = ms * 3.6
        print("{:1n} m/s são {:.2n} km/h".format(ms, kmh))
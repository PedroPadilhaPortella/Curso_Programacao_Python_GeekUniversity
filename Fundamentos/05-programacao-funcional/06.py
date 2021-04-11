def get_time():
    try:
        time = dict()

        str_time = input("Qual a hora atual (HH:MM:SS)? ")
        arr_time = str_time.split(':')
        time['hora'] = arr_time[0]
        time['minuto'] = arr_time[1]
        time['segundo'] = arr_time[2]

        print(converter_para_segundos(time))
    except:
        print("Horario em formato inválido")


def converter_para_segundos(time):
    try:
        segundos = int(time['segundo'])
        segundos += int(time['minuto']) * 60
        segundos += int(time['hora']) * 360
        return f"{time['hora']} hora(s), {time['minuto']} minuto(s) e {time['segundo']} segundo(s) são {segundos} segundo(s)"
    except:
        return "Horario em formato inválido"

get_time()
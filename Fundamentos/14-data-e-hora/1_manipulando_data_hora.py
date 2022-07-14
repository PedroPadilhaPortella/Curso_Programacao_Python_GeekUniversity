'''
    Manipulando Data e Hora
'''
import datetime

# print(dir(datetime))
print(f'Ano máximo {datetime.MAXYEAR} e mínimo {datetime.MINYEAR}')

print(f'Data e hora atual: {datetime.datetime.now()}') # 2022-07-13 03:52:12.825100

inicio = datetime.datetime.now()
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Recebendo dados e criando datas
aniversario = input('Informe sua data de nascimento (dd/mm/yyyy): ').split('/')
aniversario = datetime.datetime(day=int(aniversario[0]), month=int(aniversario[1]), year=int(aniversario[2]))

print(aniversario)
'''
    Deltas de Data e Hora

    Deltas de data e hora são os calculos entre datas.
'''
import datetime

data_atual = datetime.datetime.now()
data_aniversario = datetime.datetime(2001, 6, 10)
idade = data_atual - data_aniversario
print(idade)
print(type(idade))
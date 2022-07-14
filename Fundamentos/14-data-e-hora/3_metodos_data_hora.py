'''
    Metodos de Data e Hora
'''
from datetime import datetime, timedelta, time
import timeit, functools

print(datetime.now())
print(datetime.today())

manutencao = datetime.combine((datetime.now() + timedelta(days=1)), time())
print(f'Data de manutenção {manutencao}')

# Encontrar o dia da semana
print(manutencao.weekday())

# Horas
almoco = time(12, 30, 10)
print(almoco)

# Marcar o tempo de execução de um código com timeit

# Loop for
tempo = timeit.timeit("''.join(str(n) for n in range(100))", number=10000)
print(tempo)

# List Comprehention
tempo = timeit.timeit("''.join([str(n) for n in range(100)])", number=10000)
print(tempo)

# Map
tempo = timeit.timeit("''.join(map(str, range(100)))", number=10000)
print(tempo)

# Map
tempo = timeit.timeit("''.join(map(str, range(100)))", number=10000)
print(tempo)


def loop(n):
    soma = 0
    for num in range(n * 200):
        soam = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(loop, 2), number=10000))
'''
Module Collections -> High Performance Container Datetypes

Deque() => semelhante as listas, possui alguns metodos adicionais e maior performance
'''

from collections import deque

deq =  deque('Geek')

deq.append('y')
deq.appendleft('@')

print(deq)

deq.pop()
deq.popleft()

print(deq)

help(deque)
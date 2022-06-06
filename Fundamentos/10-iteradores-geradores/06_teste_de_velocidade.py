'''
Teste de Velocidade com Generators
'''

import time


# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_fim = time.time() - gen_inicio

print("Duracao", gen_fim)

# List Comprehention
gen_inicio = time.time()
print(sum([num for num in range(100000000)]))
gen_fim = time.time() - gen_inicio

print("Duracao", gen_fim)
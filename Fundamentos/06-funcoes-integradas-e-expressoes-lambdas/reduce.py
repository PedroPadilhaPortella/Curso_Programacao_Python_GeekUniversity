'''
Reduce
    Com o reduce, fazemos a redução dos valores de um iterável para um valor único.
    Ela é uma função que recebe dois paramentros, uma função com dois parametros e um iterável.

    Ela executa a função sobre os dois primeiros elementos do iterável e guarda o resultado,
    depois ela pega o proximo elemento do iterável e executa a função sobre ele, e assim por diante. 

    A partir do Python 3, o Reduce deixou de ser uma função Built In do Python,
    precisa ser importada do módulo functools.
'''

import functools

gastos_mensais = [19.99, 200, 3, 1.5, 140, 789]

total_gastos = functools.reduce(lambda gasto, subtotal: subtotal + gasto, gastos_mensais)

print(f"Gastos Totais do mês: {total_gastos}")


# Mesmo caso, mas usando um Loop For
total_gastos = 0

for gasto in gastos_mensais:
    total_gastos += gasto

print(f"Gastos Totais do mês: {total_gastos}")
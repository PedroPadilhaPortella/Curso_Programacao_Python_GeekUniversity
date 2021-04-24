"""
O *args representa a coletânea de propriedades que podem ser recebidas por uma função,
ele recebe os argumentos e reune eles em uma tupla.
O operador * serve como rest and spread operator.
"""

def somar_todos_numeros(*args): #rest
    return sum(args)


numeros = [5, 3, 7, 2, 7, 1, 3]

print(somar_todos_numeros())
print(somar_todos_numeros(1, 2, 3, 4, 5))
print(somar_todos_numeros(*numeros)) #spread
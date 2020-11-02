from random import randint


array = []
somapares = 0
somaimpares = 0
pares = []
impares = []

for i in range(1, 10):
    array.append(randint(1, 10))
print(array)

for i in array:
    if(i % 2 == 0):
        pares.append(i)
        somapares += i
    else:
        impares.append(i)
        somaimpares += i

print(f"Pares: {pares}\nSoma dos Pares: {somapares}\nImpares: {impares}\nSoma dos Impares: {somaimpares}")

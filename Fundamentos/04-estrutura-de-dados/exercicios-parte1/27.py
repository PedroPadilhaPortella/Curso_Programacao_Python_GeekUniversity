from random import randint

def primos(array):
    primos = []
    for i, e in enumerate(array):
        count = 0
        for divisor in range(1, e):
            if e % divisor == 0:
                count += 1
            if count > 1:
                break
        if count <= 1:
            primos.append([e, i])
    return primos



array = []
for i in range(1, 10):
    array.append(randint(1, 10))
print(array)
numeros = primos(array)

print("Numeros Primos")
for value in numeros:
    print(f"Numero: {value[0]}, Posição: {value[1]}")
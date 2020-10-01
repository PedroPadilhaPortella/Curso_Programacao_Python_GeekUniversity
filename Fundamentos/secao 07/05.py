from random import randint


array = []
for i in range(0, 10):
    array.append(randint(1, 99))
print(array)

pares = 0
for i in array:
    if(i % 2 == 0):
        pares += 1
print("O Array tem {} valores pares".format(pares))
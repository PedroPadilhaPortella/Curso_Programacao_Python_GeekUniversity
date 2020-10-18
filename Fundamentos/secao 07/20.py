from random import randint


array = list()
impares = list()
for i in range(0, 10):
    n = randint(1, 50)
    array.append(n)
    if(n % 2 == 0):
        impares.append(n)
    else:
        impares.append("")

for i in range(0, 10):
    print(array[i], end=", ")
    print(impares[i], end="\n")
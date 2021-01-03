from random import randint

seis = 0
array = list()
while seis < 6:
    n = randint(1, 99)
    if(n % 2 == 0):
        array.append(n)
        seis += 1
print(array)
print(array[::-1])
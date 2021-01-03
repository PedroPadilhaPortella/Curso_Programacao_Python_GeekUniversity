from random import randint


array = list()
for i in range(0, 6):
    array.append(randint(1, 99))
print(array)
print(array[::-1])

array.reverse()
print(array)
from random import randint
array = list()
for i in range(0, 10):
    array.append(randint(-10, 10))
print(array)

for i,e in enumerate(array):
    if(e < 0):
        array[i] = 0

print(array)
from random import randint


array = []
compact = []
for i in range(1, 10):
    array.append(randint(-10, 10))
print(array)

for i in array:
    if(i != 0):
        compact.append(i)
print("Compacto: {}".format(compact))
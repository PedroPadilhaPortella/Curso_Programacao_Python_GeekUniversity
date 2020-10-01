from random import randint


array = []
for i in range(0, 10):
    array.append(randint(1, 99))
print(array)

pos = 0
maior = 0
for i in range(0, len(array)):
    if():
        maior = array[i]
    if(array[i] > maior):
        maior = array[i]
        pos = i

print("O maior elemento é {}, na posicao array[{}]".format(maior, pos))
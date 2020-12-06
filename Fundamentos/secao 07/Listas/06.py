from random import randint


array = []
for i in range(0, 10):
    array.append(randint(1, 99))
print(array)


maior = 0
menor = 0
for elemento in array:
    if(elemento == array[0]):
        maior = elemento
        menor = elemento
    if(elemento > maior):
        maior = elemento
    if(elemento < menor):
        menor = elemento

print("O maior elemento é {} e o menor elemento é {}".format(maior, menor))
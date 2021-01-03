from random import randint


array = list()
multiples = list()
for i in range(0, 10):
    array.append(randint(1, 100))

value = int(input("Descubra os multiplos de algum no array: "))
for i in array:
    if(i % value == 0):
        multiples.append(i)
print(array)
if(multiples == []):
    print(f"Não há multiplos de {value} no vetor")
else:
    print(f"Os multiplos de {value} são {multiples}")
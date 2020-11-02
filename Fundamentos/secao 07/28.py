from random import randint


array = []
for i in range(1, 10):
    array.append(randint(1, 10))
print(array)

v1 = []
v2 = []

for n in array:
    if(n % 2 == 0):
        v1.append(n)
    else:
        v2.append(n)

print(f"Pares: {v1}\nImpares: {v2}")

array = list()
for i in range(0, 50):
    array.append((i + 5 * i) % (i + 1))
print(array)
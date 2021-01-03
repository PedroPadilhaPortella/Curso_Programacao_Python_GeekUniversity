set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = set()

zipped = zip(set1, set2)

print(list(zip(set1, set2)))

for a, b in zipped:
    print(a * b)


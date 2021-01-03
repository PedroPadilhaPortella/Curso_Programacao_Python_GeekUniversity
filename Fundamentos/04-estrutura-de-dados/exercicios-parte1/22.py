from random import randint

a = list()
b = list()
for i in range(0, 10):
    a.append(randint(1, 30))
    b.append(randint(1, 30))

c = list()
d = tuple(range(0, 21))
for i in range(0, len(a)):
        c.append(a[i])
        c.append(b[i])


print(a)
print(b)
for i in range(0, len(c)):
    print(f"{d[i]}) {c[i]}")
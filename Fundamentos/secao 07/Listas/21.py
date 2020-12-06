from random import randint

a = list()
b = list()
for i in range(0, 10):
    a.append(randint(1, 100))
    b.append(randint(1, 100))
a.sort()
b.sort()

c = a[:]
for i in b:
    if(i in c):
        c.remove(i)

print(a)
print(b)
print(c)

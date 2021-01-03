lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
middleware = []
n = 0
for i, e in enumerate(lista[:6]):
    middleware.append(e)

for i, e in enumerate(lista[11:5:-1]):
    middleware.append(e)

print(middleware)